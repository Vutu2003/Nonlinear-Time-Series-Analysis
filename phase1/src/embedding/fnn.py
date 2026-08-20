import numpy as np
from scipy.spatial import cKDTree


def false_nearest_neighbors(
    signal,
    tau,
    max_m=10,
    r_tol=15.0,
    a_tol=2.0,
    theiler=0,
    fnn_threshold=1.0,
):
    """Estimate embedding dimension using false nearest neighbors."""
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be a 1D array.")
    if not np.isfinite(signal).all():
        raise ValueError("signal must contain only finite values.")
    if isinstance(tau, bool) or not isinstance(tau, (int, np.integer)):
        raise TypeError("tau must be an integer.")
    if isinstance(max_m, bool) or not isinstance(max_m, (int, np.integer)):
        raise TypeError("max_m must be an integer.")
    if isinstance(theiler, bool) or not isinstance(
        theiler, (int, np.integer)
    ):
        raise TypeError("theiler must be an integer.")
    if tau < 1 or max_m < 1 or theiler < 0:
        raise ValueError("tau and max_m must be positive; theiler >= 0.")
    if r_tol <= 0 or a_tol <= 0:
        raise ValueError("r_tol and a_tol must be greater than 0.")
    if not 0 <= fnn_threshold <= 100:
        raise ValueError("fnn_threshold must be between 0 and 100.")

    attractor_size = np.std(signal)
    if attractor_size <= np.finfo(float).eps:
        raise ValueError("signal must have non-zero variance.")

    dims = []
    fnn_percentages = []
    valid_counts = []

    for m in range(1, max_m + 1):
        n_vectors = len(signal) - m * tau
        if n_vectors < 2:
            break

        # Build aligned embeddings in m and m + 1 dimensions.
        embedded = np.column_stack([
            signal[offset:offset + n_vectors]
            for offset in range(0, (m + 1) * tau, tau)
        ])
        y_m = embedded[:, :m]
        new_coord = embedded[:, m]

        tree = cKDTree(y_m)
        k = min(len(y_m), max(2 * theiler + 3, 8))
        nn_index = np.full(len(y_m), -1, dtype=int)
        nn_distance = np.full(len(y_m), np.nan)

        # Expand the neighbor search until all possible points are resolved.
        unresolved = np.arange(len(y_m))

        while unresolved.size and k <= len(y_m):
            distances, indices = tree.query(y_m[unresolved], k=k)

            if k == 1:
                distances = distances[:, None]
                indices = indices[:, None]

            for row, point in enumerate(unresolved):
                candidates = indices[row]
                candidate_distances = distances[row]

                valid = (
                    (np.abs(candidates - point) > theiler)
                    & (candidate_distances > np.finfo(float).eps)
                )

                if valid.any():
                    first = np.flatnonzero(valid)[0]
                    nn_index[point] = candidates[first]
                    nn_distance[point] = candidate_distances[first]

            unresolved = np.flatnonzero(nn_index < 0)

            if k == len(y_m):
                break
            k = min(len(y_m), 2 * k)

        valid = nn_index >= 0
        n_valid = int(valid.sum())

        if n_valid == 0:
            break

        indices = nn_index[valid]
        r_m = nn_distance[valid]

        delta = np.abs(
            new_coord[valid] - new_coord[indices]
        )
        r_m1 = np.sqrt(r_m**2 + delta**2)

        # Kennel's relative and absolute false-neighbor criteria.
        criterion_1 = (delta / r_m) > r_tol
        criterion_2 = (r_m1 / attractor_size) > a_tol

        fnn_percentage = 100.0 * np.mean(
            criterion_1 | criterion_2
        )

        dims.append(m)
        fnn_percentages.append(fnn_percentage)
        valid_counts.append(n_valid)

    dims = np.asarray(dims, dtype=int)
    fnn_percentages = np.asarray(fnn_percentages, dtype=float)
    valid_counts = np.asarray(valid_counts, dtype=int)

    below_threshold = np.flatnonzero(
        fnn_percentages <= fnn_threshold
    )
    selected_m = (
        int(dims[below_threshold[0]])
        if below_threshold.size
        else None
    )

    return dims, fnn_percentages, valid_counts, selected_m