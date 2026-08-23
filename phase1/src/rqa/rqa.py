from dataclasses import dataclass

import numpy as np
from scipy.spatial.distance import cdist


# Fixed-RR pipeline:
# signal -> embedding -> distances -> epsilon quantile -> recurrence plot
# -> Theiler exclusion -> line extraction -> RQA metrics.


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
    epsilon: float
    target_rr: float
    achieved_rr: float
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
        [
            signal[i * tau:i * tau + n_vectors]
            for i in range(m)
        ]
    )


def compute_distance_matrix(states: np.ndarray) -> np.ndarray:
    """Tính ma trận khoảng cách Euclidean giữa các state vectors."""
    return cdist(states, states, metric="euclidean")


def compute_fixed_rr_threshold(
    distances: np.ndarray,
    theiler: int,
    target_rr: float,
) -> float:
    """Tính epsilon từ target RR ngoài vùng Theiler."""
    distances = np.asarray(distances, dtype=float)

    if distances.ndim != 2 or distances.shape[0] != distances.shape[1]:
        raise ValueError("distances must be a square matrix.")
    if not np.all(np.isfinite(distances)):
        raise ValueError("distances must contain only finite values.")
    if isinstance(theiler, (bool, np.bool_)) or not isinstance(
        theiler,
        (int, np.integer),
    ):
        raise TypeError("theiler must be an integer.")
    if theiler < 0:
        raise ValueError("theiler must be non-negative.")
    if isinstance(target_rr, (bool, np.bool_)) or not isinstance(
        target_rr,
        (int, float, np.integer, np.floating),
    ):
        raise TypeError("target_rr must be numeric.")
    if not np.isfinite(target_rr) or not 0.0 < target_rr < 1.0:
        raise ValueError("target_rr must be in (0, 1).")

    n_vectors = distances.shape[0]
    n_eligible_rows = n_vectors - theiler - 1

    if n_eligible_rows <= 0:
        raise ValueError(
            "Theiler corridor leaves no eligible distances."
        )

    # Store each eligible pair once from the upper triangle. Row slices
    # start beyond the Theiler corridor and avoid a square boolean mask.
    n_eligible = (
        n_eligible_rows * (n_eligible_rows + 1) // 2
    )

    eligible_distances = np.empty(
        n_eligible,
        dtype=float,
    )

    cursor = 0

    # Copy eligible distances into one vector for exact quantile selection.
    for row in range(n_eligible_rows):
        values = distances[
            row,
            row + theiler + 1:
        ]

        next_cursor = cursor + values.size

        eligible_distances[
            cursor:next_cursor
        ] = values

        cursor = next_cursor

    # The vector is temporary, so quantile may partition it in place.
    epsilon = float(
        np.quantile(
            eligible_distances,
            target_rr,
            method="linear",
            overwrite_input=True,
        )
    )

    if epsilon <= 0.0:
        raise ValueError(
            "fixed-RR threshold must be positive."
        )

    return epsilon


def compute_recurrence_matrix(
    distances: np.ndarray,
    epsilon: float,
) -> np.ndarray:
    """Tạo recurrence matrix từ ngưỡng epsilon."""
    distances = np.asarray(distances, dtype=float)

    if distances.ndim != 2 or distances.shape[0] != distances.shape[1]:
        raise ValueError("distances must be a square matrix.")
    if not np.isfinite(epsilon) or epsilon <= 0.0:
        raise ValueError("epsilon must be positive.")

    # Theiler correction is applied separately after thresholding.
    return distances <= epsilon


def apply_theiler_window(
    recurrence: np.ndarray,
    theiler: int,
) -> np.ndarray:
    """Loại recurrence points trong vùng Theiler."""
    if theiler < 0:
        raise ValueError("theiler must be non-negative.")

    corrected = recurrence.copy()
    indices = np.arange(corrected.shape[0])

    # Exclude the line of identity and all pairs within the corridor.
    mask = (
        np.abs(indices[:, None] - indices[None, :])
        <= theiler
    )

    corrected[mask] = False

    return corrected


def _run_lengths(values: np.ndarray) -> np.ndarray:
    """Trích độ dài các chuỗi True liên tiếp."""
    padded = np.pad(
        values.astype(np.int8),
        (1, 1),
    )

    changes = np.diff(padded)

    starts = np.flatnonzero(changes == 1)
    ends = np.flatnonzero(changes == -1)

    return (ends - starts).astype(np.int32)


def extract_diagonal_lengths(
    recurrence: np.ndarray,
) -> np.ndarray:
    """Trích độ dài các diagonal lines ở nửa trên RP."""
    lengths = [
        _run_lengths(
            np.diag(recurrence, k=offset)
        )
        for offset in range(
            1,
            recurrence.shape[0],
        )
    ]

    nonempty = [
        item
        for item in lengths
        if item.size
    ]

    if not nonempty:
        return np.empty(
            0,
            dtype=np.int32,
        )

    return np.concatenate(nonempty)


def extract_vertical_lengths(
    recurrence: np.ndarray,
) -> np.ndarray:
    """Trích độ dài các vertical lines trong RP."""
    lengths = [
        _run_lengths(
            recurrence[:, column]
        )
        for column in range(
            recurrence.shape[1]
        )
    ]

    nonempty = [
        item
        for item in lengths
        if item.size
    ]

    if not nonempty:
        return np.empty(
            0,
            dtype=np.int32,
        )

    return np.concatenate(nonempty)


def _shannon_entropy(
    lengths: np.ndarray,
) -> float:
    """Tính Shannon entropy của phân bố line lengths."""
    if lengths.size == 0:
        return 0.0

    _, counts = np.unique(
        lengths,
        return_counts=True,
    )

    probabilities = counts / counts.sum()

    return float(
        -np.sum(
            probabilities
            * np.log(probabilities)
        )
    )


def _diagonal_metrics(
    recurrence: np.ndarray,
    lengths: np.ndarray,
    l_min: int,
) -> tuple[float, float, float, int, int]:
    """Tính các RQA metrics từ diagonal lines."""
    if l_min < 2:
        raise ValueError(
            "l_min must be at least 2."
        )

    # Diagonal lines are counted once in the upper RP triangle.
    total_recurrence = int(
        np.count_nonzero(
            np.triu(
                recurrence,
                k=1,
            )
        )
    )

    valid = lengths[lengths >= l_min]

    det = (
        float(
            valid.sum()
            / total_recurrence
        )
        if total_recurrence > 0
        else 0.0
    )

    if valid.size == 0:
        return (
            det,
            0.0,
            0.0,
            0,
            0,
        )

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
        raise ValueError(
            "v_min must be at least 2."
        )

    # Vertical metrics use all recurrence points in the symmetric RP.
    total_recurrence = int(
        np.count_nonzero(recurrence)
    )

    valid = lengths[lengths >= v_min]

    lam = (
        float(
            valid.sum()
            / total_recurrence
        )
        if total_recurrence > 0
        else 0.0
    )

    if valid.size == 0:
        return (
            lam,
            0.0,
            0,
            0,
        )

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
    """Tính RR trên vùng hợp lệ ngoài Theiler."""
    n_vectors = recurrence.shape[0]
    n_eligible_rows = (
        n_vectors - theiler - 1
    )

    # Ordered eligible pairs are twice the upper-triangle pair count.
    denominator = max(
        0,
        n_eligible_rows
        * (n_eligible_rows + 1),
    )

    if denominator == 0:
        return 0.0

    return float(
        np.count_nonzero(recurrence)
        / denominator
    )


def run_rqa(
    signal: np.ndarray,
    m: int,
    tau: int,
    l_min: int = 2,
    v_min: int = 2,
    target_rr: float = 0.02,
) -> RQAResult:
    """Chạy fixed-RR RQA cho một cửa sổ tín hiệu."""
    # Embedding and Euclidean geometry do not depend on target RR.
    states = reconstruct_phase_space(
        signal,
        m=m,
        tau=tau,
    )

    distances = compute_distance_matrix(
        states
    )

    theiler = (m - 1) * tau

    # Epsilon uses only nonduplicate distances outside the Theiler corridor.
    epsilon = compute_fixed_rr_threshold(
        distances,
        theiler=theiler,
        target_rr=target_rr,
    )

    recurrence = compute_recurrence_matrix(
        distances,
        epsilon=epsilon,
    )

    # Mask temporal neighbors before line extraction and metric evaluation.
    recurrence = apply_theiler_window(
        recurrence,
        theiler=theiler,
    )

    # Extract line geometry once for the fixed l_min and v_min cutoffs.
    diagonal_lengths = (
        extract_diagonal_lengths(
            recurrence
        )
    )

    vertical_lengths = (
        extract_vertical_lengths(
            recurrence
        )
    )

    (
        det,
        l_mean,
        entr,
        l_max,
        n_diag,
    ) = _diagonal_metrics(
        recurrence,
        diagonal_lengths,
        l_min=l_min,
    )

    (
        lam,
        tt,
        v_max,
        n_vert,
    ) = _vertical_metrics(
        recurrence,
        vertical_lengths,
        v_min=v_min,
    )

    achieved_rr = (
        _compute_recurrence_rate(
            recurrence,
            theiler=theiler,
        )
    )

    return RQAResult(
        det=det,
        l_mean=l_mean,
        entr=entr,
        l_max=l_max,
        lam=lam,
        tt=tt,
        v_max=v_max,
        epsilon=epsilon,
        target_rr=float(target_rr),
        achieved_rr=achieved_rr,
        theiler=theiler,
        n_diagonal_lines=n_diag,
        n_vertical_lines=n_vert,
    )
