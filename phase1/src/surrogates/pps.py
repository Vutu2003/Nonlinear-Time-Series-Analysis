import numpy as np


def embed_phase_space(signal, tau, m):
    """Tái cấu trúc không gian pha bằng delay embedding."""
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal phải là mảng 1D.")
    if tau < 1:
        raise ValueError("tau phải >= 1.")
    if m < 2:
        raise ValueError("m phải >= 2.")

    n_embedded = len(signal) - (m - 1) * tau

    if n_embedded < 2:
        raise ValueError(
            "Chuỗi quá ngắn so với tau và m."
        )

    indices = (
        np.arange(n_embedded)[:, None]
        + tau * np.arange(m)[None, :]
    )

    return signal[indices]


def generate_pps_indices(z, rho, length, rng=None):
    """Sinh chuỗi chỉ số quỹ đạo PPS."""
    z = np.asarray(z, dtype=float)

    if z.ndim != 2:
        raise ValueError("z phải là ma trận 2D.")
    if len(z) < 2:
        raise ValueError("Không gian pha phải có ít nhất 2 trạng thái.")
    if rho <= 0:
        raise ValueError("rho phải > 0.")
    if length < 1:
        raise ValueError("length phải >= 1.")

    if rng is None:
        rng = np.random.default_rng()

    n_states = len(z)

    # Chỉ các trạng thái có successor mới được chọn làm candidate.
    candidates = np.arange(n_states - 1)
    z_candidates = z[:-1]

    indices = np.empty(length, dtype=int)

    current_idx = rng.integers(0, n_states)
    indices[0] = current_idx

    for i in range(1, length):
        current_state = z[current_idx]

        distances = np.linalg.norm(
            z_candidates - current_state,
            axis=1,
        )

        # Dịch theo khoảng cách nhỏ nhất để tránh numerical underflow.
        scaled_distances = (
            distances - distances.min()
        ) / rho

        weights = np.exp(-scaled_distances)
        probabilities = weights / weights.sum()

        chosen_idx = rng.choice(
            candidates,
            p=probabilities,
        )

        # Bước tiến động lực học theo successor của candidate.
        current_idx = chosen_idx + 1
        indices[i] = current_idx

    return indices


def count_matching_segments(indices, segment_length=2):
    """Đếm các đoạn PPS liên tục theo quỹ đạo gốc."""
    indices = np.asarray(indices, dtype=int)

    if indices.ndim != 1:
        raise ValueError("indices phải là mảng 1D.")
    if segment_length < 2:
        raise ValueError("segment_length phải >= 2.")
    if len(indices) < segment_length:
        return 0

    consecutive = np.diff(indices) == 1

    if segment_length == 2:
        return int(np.sum(consecutive))

    run_length = segment_length - 1
    kernel = np.ones(run_length, dtype=int)

    matches = np.convolve(
        consecutive.astype(int),
        kernel,
        mode="valid",
    )

    return int(np.sum(matches == run_length))


def generate_pps_signal(signal, tau, m, rho, rng=None):
    """Sinh một tín hiệu PPS có cùng độ dài tín hiệu gốc."""
    signal = np.asarray(signal, dtype=float)
    z = embed_phase_space(signal, tau, m)

    indices = generate_pps_indices(
        z=z,
        rho=rho,
        length=len(signal),
        rng=rng,
    )

    return z[indices, 0]


def optimize_rho(
    signal,
    tau,
    m,
    rho_candidates,
    trials=10,
    segment_length=2,
    seed=None,
):
    """Chọn rho tối đa hóa số đoạn PPS trùng khớp."""
    signal = np.asarray(signal, dtype=float)
    rho_candidates = np.asarray(
        rho_candidates,
        dtype=float,
    )

    if rho_candidates.ndim != 1:
        raise ValueError("rho_candidates phải là mảng 1D.")
    if len(rho_candidates) == 0:
        raise ValueError("rho_candidates không được rỗng.")
    if np.any(rho_candidates <= 0):
        raise ValueError("Mọi rho candidate phải > 0.")
    if trials < 1:
        raise ValueError("trials phải >= 1.")

    z = embed_phase_space(signal, tau, m)
    master_rng = np.random.default_rng(seed)

    mean_counts = np.empty(
        len(rho_candidates),
        dtype=float,
    )
    std_counts = np.empty(
        len(rho_candidates),
        dtype=float,
    )

    for r_idx, rho in enumerate(rho_candidates):
        counts = np.empty(trials, dtype=float)

        for trial in range(trials):
            trial_seed = master_rng.integers(
                0,
                np.iinfo(np.uint32).max,
            )
            trial_rng = np.random.default_rng(
                trial_seed
            )

            indices = generate_pps_indices(
                z=z,
                rho=rho,
                length=len(signal),
                rng=trial_rng,
            )

            counts[trial] = count_matching_segments(
                indices,
                segment_length=segment_length,
            )

        mean_counts[r_idx] = counts.mean()
        std_counts[r_idx] = counts.std(ddof=1) if trials > 1 else 0.0

    best_idx = int(np.argmax(mean_counts))

    result = {
        "optimal_rho": float(rho_candidates[best_idx]),
        "rho_candidates": rho_candidates,
        "mean_counts": mean_counts,
        "std_counts": std_counts,
        "segment_length": segment_length,
        "trials": trials,
    }

    return result