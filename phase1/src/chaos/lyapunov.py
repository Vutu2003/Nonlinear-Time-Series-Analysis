from dataclasses import dataclass

import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import linregress


@dataclass
class RosensteinResult:
    """Kết quả ước lượng số mũ Lyapunov lớn nhất (LLE) theo Rosenstein.

    Attributes
    ----------
    lle : float
        Độ dốc của đường log-phân kỳ theo thời gian, đơn vị ``s^-1``;
        ``nan`` nếu không thể hồi quy.
    fit_r2 : float
        Hệ số xác định R² của hồi quy tuyến tính; ``nan`` nếu không hồi quy.
    fit_start_s, fit_end_s : float
        Hai đầu đoạn thời gian thực tế dùng để fit, tính bằng giây.
    theiler_samples, theiler_s : int, float
        Cửa sổ Theiler sau khi làm tròn, lần lượt theo mẫu và giây.
    n_embedded : int
        Số vector trạng thái sau delay embedding.
    n_pairs_initial : int
        Số cặp láng giềng hợp lệ tại lag 0.
    n_pairs_fit_min : int
        Số cặp nhỏ nhất trong các lag dùng để fit; bằng 0 nếu không fit.
    time_s : numpy.ndarray
        Trục thời gian của đường phân kỳ, tính bằng giây.
    mean_log_distance : numpy.ndarray
        Trung bình log khoảng cách giữa các cặp tại từng lag.
    n_pairs_by_lag : numpy.ndarray
        Số cặp hợp lệ đóng góp tại từng lag.
    valid : bool
        ``True`` khi kết quả vượt qua các tiêu chí kiểm soát chất lượng.
    qc_reason : str
        Mã chất lượng: ``"ok"``, ``"insufficient_initial_pairs"``,
        ``"insufficient_fit_points"``, ``"non_finite_lle"`` hoặc
        ``"low_fit_r2"``.
    """

    lle: float
    fit_r2: float
    fit_start_s: float
    fit_end_s: float
    theiler_samples: int
    theiler_s: float
    n_embedded: int
    n_pairs_initial: int
    n_pairs_fit_min: int
    time_s: np.ndarray
    mean_log_distance: np.ndarray
    n_pairs_by_lag: np.ndarray
    valid: bool
    qc_reason: str


def estimate_mean_period(signal, sampling_rate):
    """Ước lượng chu kỳ phổ trung bình của tín hiệu một chiều.

    Tần số trung bình là trọng tâm phổ công suất một phía (bỏ thành phần DC);
    chu kỳ trả về là nghịch đảo của tần số này.

    Parameters
    ----------
    signal : array_like
        Chuỗi mẫu tín hiệu.
    sampling_rate : float
        Tần số lấy mẫu dương, đơn vị Hz.

    Returns
    -------
    float
        Chu kỳ trung bình, đơn vị giây.

    Raises
    ------
    ValueError
        Nếu phổ không có công suất hữu hạn dương hoặc tần số trung bình không
        hợp lệ.
    """
    signal = np.asarray(signal, dtype=float)
    centered = signal - np.mean(signal)

    spectrum = np.fft.rfft(centered)
    frequencies = np.fft.rfftfreq(
        len(centered),
        d=1.0 / sampling_rate,
    )
    power = np.abs(spectrum) ** 2

    frequencies = frequencies[1:]
    power = power[1:]

    total_power = np.sum(power)
    if total_power <= 0 or not np.isfinite(total_power):
        raise ValueError("Cannot estimate mean period from the signal.")

    mean_frequency = np.sum(frequencies * power) / total_power

    if mean_frequency <= 0 or not np.isfinite(mean_frequency):
        raise ValueError("Invalid mean frequency.")

    return 1.0 / mean_frequency


def reconstruct_phase_space(signal, m, tau_samples):
    """Tái cấu trúc không gian pha bằng delay embedding tiến.

    Vector thứ ``i`` có dạng
    ``[x[i], x[i + tau], ..., x[i + (m - 1) * tau]]``.

    Parameters
    ----------
    signal : array_like
        Chuỗi mẫu tín hiệu một chiều.
    m : int
        Số chiều nhúng.
    tau_samples : int
        Độ trễ giữa hai tọa độ liên tiếp, tính theo mẫu.

    Returns
    -------
    numpy.ndarray
        Ma trận trạng thái có shape ``(len(signal) - (m - 1) * tau_samples,
        m)``.

    Raises
    ------
    ValueError
        Nếu tín hiệu không đủ dài để tạo ít nhất hai vector trạng thái.
    """
    signal = np.asarray(signal, dtype=float)

    n_vectors = len(signal) - (m - 1) * tau_samples
    if n_vectors <= 1:
        raise ValueError("Signal is too short for the embedding.")

    indices = (
        np.arange(n_vectors)[:, None]
        + np.arange(m)[None, :] * tau_samples
    )

    return signal[indices]


def find_nearest_neighbors(states, theiler_samples):
    """Tìm láng giềng gần nhất ngoài cửa sổ Theiler cho mỗi trạng thái.

    Parameters
    ----------
    states : array_like
        Ma trận trạng thái shape ``(n_states, n_dimensions)``.
    theiler_samples : int
        Khoảng cách chỉ số tối thiểu bị loại; ứng viên chỉ hợp lệ khi
        ``abs(j - i) > theiler_samples``.

    Returns
    -------
    neighbors : numpy.ndarray
        Chỉ số láng giềng của từng trạng thái; ``-1`` nếu không tìm thấy.
    distances : numpy.ndarray
        Khoảng cách Euclid tương ứng; ``nan`` nếu không tìm thấy.
    """
    n_states = len(states)
    tree = cKDTree(states)

    neighbors = np.full(n_states, -1, dtype=int)
    distances = np.full(n_states, np.nan, dtype=float)

    unresolved = np.arange(n_states)
    k = min(8, n_states)

    while len(unresolved) > 0:
        query_states = states[unresolved]
        dist, idx = tree.query(query_states, k=k)

        if k == 1:
            dist = dist[:, None]
            idx = idx[:, None]

        for row, reference in enumerate(unresolved):
            candidates = idx[row]
            candidate_distances = dist[row]

            admissible = (
                (candidates < n_states)
                & (np.abs(candidates - reference) > theiler_samples)
            )

            if np.any(admissible):
                first = np.flatnonzero(admissible)[0]
                neighbors[reference] = candidates[first]
                distances[reference] = candidate_distances[first]

        unresolved = unresolved[neighbors[unresolved] < 0]

        if len(unresolved) == 0 or k >= n_states:
            break

        k = min(2 * k, n_states)

    return neighbors, distances


def compute_divergence_curve(
    states,
    neighbors,
    max_lag_samples,
    distance_tolerance,
):
    """Tính đường trung bình log-phân kỳ của các cặp láng giềng theo lag.

    Ở mỗi lag, hai phần tử của từng cặp được tiến đồng thời; các cặp vượt khỏi
    chuỗi, có khoảng cách không hữu hạn hoặc không lớn hơn ngưỡng đều bị loại.

    Parameters
    ----------
    states : array_like
        Ma trận trạng thái shape ``(n_states, n_dimensions)``.
    neighbors : array_like
        Chỉ số láng giềng cho từng trạng thái; giá trị âm là không hợp lệ.
    max_lag_samples : int
        Lag lớn nhất cần tính, theo mẫu và có bao gồm điểm cuối.
    distance_tolerance : float
        Ngưỡng khoảng cách dương để tránh lấy log của 0 hoặc giá trị quá nhỏ.

    Returns
    -------
    mean_log_distance : numpy.ndarray
        Trung bình log khoảng cách tại các lag từ 0 đến ``max_lag_samples``;
        ``nan`` tại lag không có cặp hợp lệ.
    n_pairs : numpy.ndarray
        Số cặp hợp lệ tại từng lag.
    """
    n_states = len(states)
    reference_indices = np.flatnonzero(neighbors >= 0)

    mean_log_distance = np.full(
        max_lag_samples + 1,
        np.nan,
        dtype=float,
    )
    n_pairs = np.zeros(max_lag_samples + 1, dtype=int)

    for lag in range(max_lag_samples + 1):
        refs = reference_indices
        nbrs = neighbors[refs]

        usable = (
            (refs + lag < n_states)
            & (nbrs + lag < n_states)
        )

        refs = refs[usable]
        nbrs = nbrs[usable]

        if len(refs) == 0:
            continue

        distances = np.linalg.norm(
            states[refs + lag] - states[nbrs + lag],
            axis=1,
        )

        valid = (
            np.isfinite(distances)
            & (distances > distance_tolerance)
        )
        distances = distances[valid]

        if len(distances) == 0:
            continue

        mean_log_distance[lag] = np.mean(np.log(distances))
        n_pairs[lag] = len(distances)

    return mean_log_distance, n_pairs


def compute_rosenstein_lle(
    signal,
    sampling_rate,
    m,
    tau_samples,
    fit_start_s,
    fit_end_s,
    max_follow_s=5.0,
    theiler_s=None,
    min_initial_pairs=50,
    min_fit_pairs=30,
    min_r2=0.90,
):
    """Ước lượng số mũ Lyapunov lớn nhất bằng phương pháp Rosenstein.

    Hàm delay-embed tín hiệu, ghép mỗi trạng thái với láng giềng gần nhất nằm
    ngoài cửa sổ Theiler, theo dõi trung bình log khoảng cách, rồi lấy độ dốc
    hồi quy tuyến tính trong khoảng fit làm LLE.

    Parameters
    ----------
    signal : array_like
        Tín hiệu một chiều, hữu hạn.
    sampling_rate : float
        Tần số lấy mẫu dương, đơn vị Hz.
    m : int
        Số chiều nhúng, tối thiểu 2.
    tau_samples : int
        Độ trễ nhúng, tính theo mẫu và tối thiểu 1.
    fit_start_s, fit_end_s : float
        Khoảng thời gian đóng để hồi quy, tính bằng giây.
    max_follow_s : float, default=5.0
        Thời gian tối đa theo dõi độ phân kỳ, tính bằng giây.
    theiler_s : float or None, default=None
        Cửa sổ Theiler theo giây. Nếu ``None``, ước lượng từ trọng tâm phổ;
        giá trị sau đó được làm tròn và chặn dưới ở một mẫu.
    min_initial_pairs : int, default=50
        Số cặp hợp lệ tối thiểu tại lag 0.
    min_fit_pairs : int, default=30
        Số cặp tối thiểu để một lag được đưa vào hồi quy.
    min_r2 : float, default=0.90
        R² tối thiểu để đánh dấu kết quả là hợp lệ.

    Returns
    -------
    RosensteinResult
        LLE, chất lượng phép fit, đường phân kỳ, số cặp và trạng thái QC.
        Kết quả QC không đạt vẫn được trả về với ``valid=False``.

    Raises
    ------
    ValueError
        Nếu tín hiệu không phải chuỗi một chiều hữu hạn đủ dài, tham số nhúng
        hoặc tần số lấy mẫu không dương, hay khoảng fit không thỏa
        ``0 <= fit_start_s < fit_end_s <= max_follow_s``.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be one-dimensional.")

    if len(signal) < 2:
        raise ValueError("signal is too short.")

    if not np.all(np.isfinite(signal)):
        raise ValueError("signal contains non-finite values.")

    if sampling_rate <= 0:
        raise ValueError("sampling_rate must be positive.")

    if m < 2:
        raise ValueError("m must be at least 2.")

    if tau_samples < 1:
        raise ValueError("tau_samples must be at least 1.")

    if not 0 <= fit_start_s < fit_end_s <= max_follow_s:
        raise ValueError("Invalid fitting interval.")

    if theiler_s is None:
        theiler_s = estimate_mean_period(signal, sampling_rate)

    theiler_samples = int(np.round(theiler_s * sampling_rate))
    theiler_samples = max(theiler_samples, 1)

    states = reconstruct_phase_space(
        signal,
        m=m,
        tau_samples=tau_samples,
    )
    n_embedded = len(states)

    neighbors, initial_distances = find_nearest_neighbors(
        states,
        theiler_samples=theiler_samples,
    )

    scale = max(np.std(states), 1.0)
    distance_tolerance = (
        np.finfo(float).eps * scale * np.sqrt(m) * 10
    )

    valid_initial = (
        (neighbors >= 0)
        & np.isfinite(initial_distances)
        & (initial_distances > distance_tolerance)
    )

    neighbors[~valid_initial] = -1
    n_pairs_initial = int(np.sum(valid_initial))

    max_lag_samples = int(
        np.floor(max_follow_s * sampling_rate)
    )

    max_possible_lag = max(n_embedded - 1, 0)
    max_lag_samples = min(
        max_lag_samples,
        max_possible_lag,
    )

    mean_log_distance, n_pairs_by_lag = compute_divergence_curve(
        states,
        neighbors,
        max_lag_samples=max_lag_samples,
        distance_tolerance=distance_tolerance,
    )

    time_s = (
        np.arange(max_lag_samples + 1, dtype=float)
        / sampling_rate
    )

    fit_mask = (
        (time_s >= fit_start_s)
        & (time_s <= fit_end_s)
        & np.isfinite(mean_log_distance)
        & (n_pairs_by_lag >= min_fit_pairs)
    )

    fit_indices = np.flatnonzero(fit_mask)

    if n_pairs_initial < min_initial_pairs:
        return RosensteinResult(
            lle=np.nan,
            fit_r2=np.nan,
            fit_start_s=fit_start_s,
            fit_end_s=fit_end_s,
            theiler_samples=theiler_samples,
            theiler_s=theiler_samples / sampling_rate,
            n_embedded=n_embedded,
            n_pairs_initial=n_pairs_initial,
            n_pairs_fit_min=0,
            time_s=time_s,
            mean_log_distance=mean_log_distance,
            n_pairs_by_lag=n_pairs_by_lag,
            valid=False,
            qc_reason="insufficient_initial_pairs",
        )

    if len(fit_indices) < 3:
        return RosensteinResult(
            lle=np.nan,
            fit_r2=np.nan,
            fit_start_s=fit_start_s,
            fit_end_s=fit_end_s,
            theiler_samples=theiler_samples,
            theiler_s=theiler_samples / sampling_rate,
            n_embedded=n_embedded,
            n_pairs_initial=n_pairs_initial,
            n_pairs_fit_min=0,
            time_s=time_s,
            mean_log_distance=mean_log_distance,
            n_pairs_by_lag=n_pairs_by_lag,
            valid=False,
            qc_reason="insufficient_fit_points",
        )

    fit_time = time_s[fit_indices]
    fit_divergence = mean_log_distance[fit_indices]

    regression = linregress(fit_time, fit_divergence)

    lle = float(regression.slope)
    fit_r2 = float(regression.rvalue ** 2)
    n_pairs_fit_min = int(
        np.min(n_pairs_by_lag[fit_indices])
    )

    if not np.isfinite(lle):
        valid = False
        qc_reason = "non_finite_lle"
    elif fit_r2 < min_r2:
        valid = False
        qc_reason = "low_fit_r2"
    else:
        valid = True
        qc_reason = "ok"

    return RosensteinResult(
        lle=lle,
        fit_r2=fit_r2,
        fit_start_s=float(fit_time[0]),
        fit_end_s=float(fit_time[-1]),
        theiler_samples=theiler_samples,
        theiler_s=theiler_samples / sampling_rate,
        n_embedded=n_embedded,
        n_pairs_initial=n_pairs_initial,
        n_pairs_fit_min=n_pairs_fit_min,
        time_s=time_s,
        mean_log_distance=mean_log_distance,
        n_pairs_by_lag=n_pairs_by_lag,
        valid=valid,
        qc_reason=qc_reason,
    )
