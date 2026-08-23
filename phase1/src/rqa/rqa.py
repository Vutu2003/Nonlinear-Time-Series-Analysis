from dataclasses import dataclass

import numpy as np
from scipy.spatial.distance import cdist


@dataclass(frozen=True)
class RQAResult:
    """Kết quả RQA của một cửa sổ tín hiệu."""

    det: float
    l_mean: float
    entr: float
    l_max: int
    lam: float
    tt: float
    v_max: int
    recurrence_rate: float
    epsilon: float
    theiler: int
    n_diagonal_lines: int
    n_vertical_lines: int


def reconstruct_phase_space(
    signal: np.ndarray,
    m: int,
    tau: int,
) -> np.ndarray:
    """Tái dựng không gian pha bằng time-delay embedding."""
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be one-dimensional.")
    if not np.all(np.isfinite(signal)):
        raise ValueError("signal must contain only finite values.")
    if m < 1:
        raise ValueError("m must be at least 1.")
    if tau < 1:
        raise ValueError("tau must be at least 1.")

    n_vectors = signal.size - (m - 1) * tau
    if n_vectors <= 0:
        raise ValueError("signal is too short for the selected m and tau.")

    return np.column_stack(
        [signal[i * tau:i * tau + n_vectors] for i in range(m)]
    )


def compute_distance_matrix(states: np.ndarray) -> np.ndarray:
    """Tính ma trận khoảng cách Euclidean giữa các state vectors."""
    return cdist(states, states, metric="euclidean")


def compute_recurrence_matrix(
    distances: np.ndarray,
    radius_fraction: float = 0.10,
) -> tuple[np.ndarray, float]:
    """Tạo recurrence matrix theo đường kính phase space."""
    if distances.ndim != 2 or distances.shape[0] != distances.shape[1]:
        raise ValueError("distances must be a square matrix.")
    if not 0.0 < radius_fraction <= 1.0:
        raise ValueError("radius_fraction must be in (0, 1].")

    diameter = float(np.max(distances))
    if diameter <= 0.0:
        raise ValueError("phase-space diameter must be positive.")

    epsilon = radius_fraction * diameter
    recurrence = distances <= epsilon

    return recurrence, epsilon


def apply_theiler_window(
    recurrence: np.ndarray,
    theiler: int,
) -> np.ndarray:
    """Loại các điểm recurrence trong vùng Theiler."""
    if theiler < 0:
        raise ValueError("theiler must be non-negative.")

    corrected = recurrence.copy()
    indices = np.arange(corrected.shape[0])
    mask = np.abs(indices[:, None] - indices[None, :]) <= theiler
    corrected[mask] = False

    return corrected


def _run_lengths(values: np.ndarray) -> np.ndarray:
    """Trích độ dài các chuỗi True liên tiếp."""
    padded = np.pad(values.astype(np.int8), (1, 1))
    changes = np.diff(padded)

    starts = np.flatnonzero(changes == 1)
    ends = np.flatnonzero(changes == -1)

    return (ends - starts).astype(np.int32)


def extract_diagonal_lengths(
    recurrence: np.ndarray,
) -> np.ndarray:
    """Trích độ dài các diagonal lines ở nửa trên RP."""
    lengths = [
        _run_lengths(np.diag(recurrence, k=offset))
        for offset in range(1, recurrence.shape[0])
    ]

    nonempty = [item for item in lengths if item.size]
    if not nonempty:
        return np.empty(0, dtype=np.int32)

    return np.concatenate(nonempty)


def extract_vertical_lengths(
    recurrence: np.ndarray,
) -> np.ndarray:
    """Trích độ dài các vertical lines trong RP."""
    lengths = [
        _run_lengths(recurrence[:, column])
        for column in range(recurrence.shape[1])
    ]

    nonempty = [item for item in lengths if item.size]
    if not nonempty:
        return np.empty(0, dtype=np.int32)

    return np.concatenate(nonempty)


def _shannon_entropy(lengths: np.ndarray) -> float:
    """Tính Shannon entropy của phân bố line lengths."""
    if lengths.size == 0:
        return 0.0

    _, counts = np.unique(lengths, return_counts=True)
    probabilities = counts / counts.sum()

    return float(
        -np.sum(probabilities * np.log(probabilities))
    )


def _diagonal_metrics(
    recurrence: np.ndarray,
    lengths: np.ndarray,
    l_min: int,
) -> tuple[float, float, float, int, int]:
    """Tính các RQA metrics từ diagonal lines."""
    if l_min < 2:
        raise ValueError("l_min must be at least 2.")

    total_recurrence = int(
        np.count_nonzero(np.triu(recurrence, k=1))
    )
    valid = lengths[lengths >= l_min]

    det = (
        float(valid.sum() / total_recurrence)
        if total_recurrence > 0
        else 0.0
    )

    if valid.size == 0:
        return det, 0.0, 0.0, 0, 0

    return (
        det,
        float(valid.mean()),
        _shannon_entropy(valid),
        int(valid.max()),
        int(valid.size),
    )


def _vertical_metrics(
    recurrence: np.ndarray,
    lengths: np.ndarray,
    v_min: int,
) -> tuple[float, float, int, int]:
    """Tính các RQA metrics từ vertical lines."""
    if v_min < 2:
        raise ValueError("v_min must be at least 2.")

    total_recurrence = int(np.count_nonzero(recurrence))
    valid = lengths[lengths >= v_min]

    lam = (
        float(valid.sum() / total_recurrence)
        if total_recurrence > 0
        else 0.0
    )

    if valid.size == 0:
        return lam, 0.0, 0, 0

    return (
        lam,
        float(valid.mean()),
        int(valid.max()),
        int(valid.size),
    )


def _compute_recurrence_rate(
    recurrence: np.ndarray,
    theiler: int,
) -> float:
    """Tính RR trên vùng hợp lệ sau Theiler exclusion."""
    n = recurrence.shape[0]
    indices = np.arange(n)

    eligible = (
        np.abs(indices[:, None] - indices[None, :]) > theiler
    )
    denominator = int(np.count_nonzero(eligible))

    if denominator == 0:
        return 0.0

    return float(
        np.count_nonzero(recurrence) / denominator
    )


def run_rqa(
    signal: np.ndarray,
    m: int,
    tau: int,
    l_min: int = 2,
    v_min: int = 2,
    radius_fraction: float = 0.10,
) -> RQAResult:
    """Chạy RQA cho một cửa sổ tín hiệu."""
    states = reconstruct_phase_space(
        signal,
        m=m,
        tau=tau,
    )

    distances = compute_distance_matrix(states)

    recurrence, epsilon = compute_recurrence_matrix(
        distances,
        radius_fraction=radius_fraction,
    )

    theiler = (m - 1) * tau
    recurrence = apply_theiler_window(
        recurrence,
        theiler=theiler,
    )

    diagonal_lengths = extract_diagonal_lengths(recurrence)
    vertical_lengths = extract_vertical_lengths(recurrence)

    det, l_mean, entr, l_max, n_diag = _diagonal_metrics(
        recurrence,
        diagonal_lengths,
        l_min=l_min,
    )

    lam, tt, v_max, n_vert = _vertical_metrics(
        recurrence,
        vertical_lengths,
        v_min=v_min,
    )

    return RQAResult(
        det=det,
        l_mean=l_mean,
        entr=entr,
        l_max=l_max,
        lam=lam,
        tt=tt,
        v_max=v_max,
        recurrence_rate=_compute_recurrence_rate(
            recurrence,
            theiler,
        ),
        epsilon=epsilon,
        theiler=theiler,
        n_diagonal_lines=n_diag,
        n_vertical_lines=n_vert,
    )