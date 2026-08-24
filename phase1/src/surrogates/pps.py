import numpy as np


# PPS CORE PSEUDOCODE
#
# Inputs: scalar signal x[0:N], delay tau, dimension m, noise radius rho,
#         surrogate length L, and a random-number generator.
#
# 1. Delay embedding
#    N_e <- N - (m - 1) * tau
#    Z[i] <- [x[i], x[i + tau], ..., x[i + (m - 1) * tau]]
#
# 2. PPS trajectory generation
#    candidates <- {0, ..., N_e - 2}
#    I[0] <- Uniform({0, ..., N_e - 1})
#    for t <- 1, ..., L - 1:
#        d[j] <- EuclideanDistance(Z[I[t - 1]], Z[j])
#        w[j] <- exp(-(d[j] - min(d)) / rho), for j in candidates
#        p[j] <- w[j] / sum(w)
#        j <- CategoricalSample(p)
#        I[t] <- j + 1
#    y[t] <- Z[I[t], 0], for t <- 0, ..., L - 1
#    return surrogate y and, optionally, source indices I
#
#    Self-matches and temporal neighbors remain valid candidates. The last
#    state is excluded only because it has no observed successor.
#
# 3. Noise-radius selection
#    for each candidate rho_k and each independent trial q:
#        generate source indices I[k, q]
#        split I[k, q] into maximal runs satisfying I[t + 1] = I[t] + 1
#        C_n[k, q] <- number of runs with length >= n
#    rho_star <- argmax_k Mean_q(C_n[k, q])
#    return rho_star and the mean and standard deviation of C_n for each rho_k
#
#    Exact-length run counts are retained as a diagnostic, not as the default
#    optimization criterion.


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


def consecutive_run_lengths(indices):
    """Trả về độ dài các maximal consecutive runs."""
    indices = np.asarray(indices, dtype=int)

    if indices.ndim != 1:
        raise ValueError("indices phải là mảng 1D.")
    if len(indices) == 0:
        return np.array([], dtype=int)

    consecutive = np.diff(indices) == 1
    boundaries = np.flatnonzero(~consecutive) + 1
    return np.diff(
        np.concatenate(
            (
                np.array([0]),
                boundaries,
                np.array([len(indices)]),
            )
        )
    )


def count_matching_segments(
    indices,
    segment_length=2,
    mode="at_least",
):
    """Đếm maximal runs theo ngưỡng hoặc độ dài chính xác."""
    if segment_length < 2:
        raise ValueError("segment_length phải >= 2.")
    if mode not in {"at_least", "exact"}:
        raise ValueError("mode phải là 'at_least' hoặc 'exact'.")

    run_lengths = consecutive_run_lengths(indices)
    if mode == "exact":
        matches = run_lengths == segment_length
    else:
        matches = run_lengths >= segment_length

    return int(np.count_nonzero(matches))


def summarize_pps_indices(indices):
    """Tóm tắt mức liên tục theo quỹ đạo gốc."""
    indices = np.asarray(indices, dtype=int)
    run_lengths = consecutive_run_lengths(indices)
    n_transitions = max(len(indices) - 1, 0)
    successor_fraction = (
        float(np.sum(np.diff(indices) == 1) / n_transitions)
        if n_transitions
        else 0.0
    )

    return {
        "run_count": int(len(run_lengths)),
        "mean_run_length": (
            float(run_lengths.mean()) if len(run_lengths) else 0.0
        ),
        "max_run_length": (
            int(run_lengths.max()) if len(run_lengths) else 0
        ),
        "successor_fraction": successor_fraction,
        "run_lengths": run_lengths,
    }


def generate_pps_signal(
    signal,
    tau,
    m,
    rho,
    rng=None,
    return_indices=False,
):
    """Sinh một tín hiệu PPS có cùng độ dài tín hiệu gốc."""
    signal = np.asarray(signal, dtype=float)
    z = embed_phase_space(signal, tau, m)

    indices = generate_pps_indices(
        z=z,
        rho=rho,
        length=len(signal),
        rng=rng,
    )

    surrogate = z[indices, 0]
    if return_indices:
        return surrogate, indices

    return surrogate


def optimize_rho(
    signal,
    tau,
    m,
    rho_candidates,
    trials=10,
    segment_length=2,
    count_mode="at_least",
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
    if count_mode not in {"at_least", "exact"}:
        raise ValueError("count_mode phải là 'at_least' hoặc 'exact'.")

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
                mode=count_mode,
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
        "count_mode": count_mode,
        "trials": trials,
    }

    return result
