"""Permutation entropy based on Bandt and Pompe (2002)."""

from collections import Counter
from dataclasses import dataclass
from math import factorial, fsum, isfinite, log2
from numbers import Integral, Real
from typing import Iterable, Mapping, Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


OrdinalPattern = tuple[int, ...]

__all__ = [
    "PermutationEntropyResult",
    "validate_series",
    "build_windows",
    "encode_ordinal_pattern",
    "build_ordinal_sequence",
    "count_ordinal_patterns",
    "estimate_pattern_probabilities",
    "compute_permutation_entropy",
    "permutation_entropy",
]


@dataclass(slots=True)
class PermutationEntropyResult:
    """Results and metadata from the permutation entropy pipeline."""

    entropy: float
    maximum_entropy: float
    normalized_entropy: float
    entropy_per_symbol: float
    pattern_sequence: list[OrdinalPattern]
    pattern_counts: dict[OrdinalPattern, int]
    pattern_probabilities: dict[OrdinalPattern, float]
    order: int
    number_of_windows: int
    number_of_possible_patterns: int
    number_of_observed_patterns: int


def validate_series(
    series: ArrayLike,
    order: int,
    tie_method: str = "error",
) -> NDArray[np.float64]:
    """Validate and convert a time series for ordinal encoding.

    Parameters
    ----------
    series:
        One-dimensional time series.
    order:
        Number of consecutive samples in each ordinal pattern.
    tie_method:
        ``"error"`` rejects tied values within a window. ``"jitter"``
        allows ties to be resolved during ordinal encoding.

    Returns
    -------
    numpy.ndarray
        A one-dimensional ``float64`` representation of the input.

    Raises
    ------
    TypeError
        If ``order`` is not an integer.
    ValueError
        If the input cannot form valid ordinal patterns.
    """
    if isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral):
        raise TypeError("Order must be an integer.")
    if order < 2:
        raise ValueError("Order must be at least 2.")
    if not isinstance(tie_method, str) or tie_method not in {
        "error",
        "jitter",
    }:
        raise ValueError("Tie method must be either 'error' or 'jitter'.")

    try:
        values = np.asarray(series, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError("Series must contain real numeric values.") from exc

    if values.ndim != 1:
        raise ValueError("Series must be one-dimensional.")
    if values.size < order:
        raise ValueError(
            f"Series length ({values.size}) must be at least order ({order})."
        )
    if not np.isfinite(values).all():
        raise ValueError("Series must not contain NaN or infinite values.")

    if tie_method == "error":
        windows = np.lib.stride_tricks.sliding_window_view(values, order)
        sorted_windows = np.sort(windows, axis=1)
        tied_windows = np.any(np.diff(sorted_windows, axis=1) == 0, axis=1)
        if np.any(tied_windows):
            first_index = int(np.flatnonzero(tied_windows)[0])
            raise ValueError(
                "Tied values found in the window starting at index "
                f"{first_index}. Use tie_method='jitter' to resolve ties."
            )

    return values


def build_windows(
    series: ArrayLike,
    order: int,
) -> NDArray[np.float64]:
    """Create all overlapping windows of consecutive samples."""
    if isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral):
        raise TypeError("Order must be an integer.")
    if order < 2:
        raise ValueError("Order must be at least 2.")

    try:
        values = np.asarray(series, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError("Series must contain real numeric values.") from exc

    if values.ndim != 1:
        raise ValueError("Series must be one-dimensional.")
    if values.size < order:
        raise ValueError(
            f"Series length ({values.size}) must be at least order ({order})."
        )
    if not np.isfinite(values).all():
        raise ValueError("Series must not contain NaN or infinite values.")

    return np.lib.stride_tricks.sliding_window_view(values, order)


def encode_ordinal_pattern(
    window: ArrayLike,
    tie_method: str = "error",
    random_state: int | np.random.Generator | None = None,
) -> OrdinalPattern:
    """Encode one window as indices ordered by ascending sample value."""
    if not isinstance(tie_method, str) or tie_method not in {
        "error",
        "jitter",
    }:
        raise ValueError("Tie method must be either 'error' or 'jitter'.")

    try:
        values = np.asarray(window, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError("Window must contain real numeric values.") from exc

    if values.ndim != 1:
        raise ValueError("Window must be one-dimensional.")
    if values.size < 2:
        raise ValueError("Window must contain at least two values.")
    if not np.isfinite(values).all():
        raise ValueError("Window must not contain NaN or infinite values.")

    has_ties = np.unique(values).size != values.size
    if has_ties and tie_method == "error":
        raise ValueError(
            "Window contains tied values. Use tie_method='jitter' to "
            "resolve ties."
        )

    if not has_ties:
        indices = np.argsort(values)
    else:
        if isinstance(random_state, np.random.Generator):
            rng = random_state
        else:
            rng = np.random.default_rng(random_state)

        # Unique random keys act as infinitesimal tie-breaking noise.
        tie_breakers = rng.permutation(values.size)
        indices = np.lexsort((tie_breakers, values))

    return tuple(int(index) for index in indices)


def build_ordinal_sequence(
    windows: ArrayLike,
    tie_method: str = "error",
    random_state: int | np.random.Generator | None = None,
) -> list[OrdinalPattern]:
    """Encode a two-dimensional window array into ordinal patterns."""
    if not isinstance(tie_method, str) or tie_method not in {
        "error",
        "jitter",
    }:
        raise ValueError("Tie method must be either 'error' or 'jitter'.")

    try:
        window_array = np.asarray(windows, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError("Windows must contain real numeric values.") from exc

    if window_array.ndim != 2:
        raise ValueError("Windows must be a two-dimensional array.")
    if window_array.shape[0] == 0:
        raise ValueError("Windows must contain at least one window.")
    if window_array.shape[1] < 2:
        raise ValueError("Each window must contain at least two values.")
    if not np.isfinite(window_array).all():
        raise ValueError("Windows must not contain NaN or infinite values.")

    if tie_method == "error":
        rng = None
    elif isinstance(random_state, np.random.Generator):
        rng = random_state
    else:
        rng = np.random.default_rng(random_state)

    return [
        encode_ordinal_pattern(
            window,
            tie_method=tie_method,
            random_state=rng,
        )
        for window in window_array
    ]


def count_ordinal_patterns(
    pattern_sequence: Iterable[Sequence[int]],
) -> dict[OrdinalPattern, int]:
    """Count occurrences of every observed ordinal pattern."""
    counts: Counter[OrdinalPattern] = Counter()
    pattern_length: int | None = None

    for pattern in pattern_sequence:
        try:
            raw_pattern = tuple(pattern)
        except TypeError as exc:
            raise ValueError(
                "Pattern sequence must contain integer sequences."
            ) from exc

        if len(raw_pattern) < 2:
            raise ValueError(
                "Ordinal patterns must contain at least two indices."
            )
        if any(
            isinstance(index, (bool, np.bool_))
            or not isinstance(index, Integral)
            for index in raw_pattern
        ):
            raise TypeError("Ordinal pattern indices must be integers.")

        normalized_pattern = tuple(int(index) for index in raw_pattern)
        if sorted(normalized_pattern) != list(range(len(normalized_pattern))):
            raise ValueError(
                "Each ordinal pattern must be a permutation of 0 to n - 1."
            )

        if pattern_length is None:
            pattern_length = len(normalized_pattern)
        elif len(normalized_pattern) != pattern_length:
            raise ValueError("All ordinal patterns must have the same length.")

        counts[normalized_pattern] += 1

    if not counts:
        raise ValueError("Pattern sequence must not be empty.")

    return dict(counts)


def estimate_pattern_probabilities(
    pattern_counts: Mapping[Sequence[int], int],
) -> dict[OrdinalPattern, float]:
    """Normalize observed pattern counts into empirical probabilities."""
    if not pattern_counts:
        raise ValueError("Pattern counts must not be empty.")

    normalized_counts: dict[OrdinalPattern, int] = {}
    pattern_length: int | None = None
    for pattern, count in pattern_counts.items():
        if isinstance(count, (bool, np.bool_)) or not isinstance(
            count, Integral
        ):
            raise TypeError("Pattern counts must be integers.")
        if count <= 0:
            raise ValueError("Pattern counts must be positive.")
        try:
            raw_pattern = tuple(pattern)
        except TypeError as exc:
            raise ValueError(
                "Pattern keys must be integer sequences."
            ) from exc
        if any(
            isinstance(index, (bool, np.bool_))
            or not isinstance(index, Integral)
            for index in raw_pattern
        ):
            raise TypeError("Ordinal pattern indices must be integers.")

        normalized_pattern = tuple(int(index) for index in raw_pattern)
        if len(normalized_pattern) < 2:
            raise ValueError(
                "Ordinal patterns must contain at least two indices."
            )
        if sorted(normalized_pattern) != list(range(len(normalized_pattern))):
            raise ValueError(
                "Each ordinal pattern must be a permutation of 0 to n - 1."
            )
        if pattern_length is None:
            pattern_length = len(normalized_pattern)
        elif len(normalized_pattern) != pattern_length:
            raise ValueError("All ordinal patterns must have the same length.")

        normalized_counts[normalized_pattern] = int(count)

    total_count = sum(normalized_counts.values())
    return {
        pattern: count / total_count
        for pattern, count in normalized_counts.items()
    }


def compute_permutation_entropy(
    pattern_probabilities: Mapping[Sequence[int], float],
    order: int,
) -> dict[str, float]:
    """Calculate raw, normalized, and per-symbol permutation entropy."""
    if isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral):
        raise TypeError("Order must be an integer.")
    if order < 2:
        raise ValueError("Order must be at least 2.")
    if not pattern_probabilities:
        raise ValueError("Pattern probabilities must not be empty.")
    if len(pattern_probabilities) > factorial(order):
        raise ValueError(
            "Observed pattern count cannot exceed order factorial."
        )

    probabilities: list[float] = []
    for pattern, probability in pattern_probabilities.items():
        try:
            raw_pattern = tuple(pattern)
        except TypeError as exc:
            raise ValueError(
                "Pattern keys must be integer sequences."
            ) from exc
        if len(raw_pattern) != order:
            raise ValueError(
                "Every ordinal pattern must match the given order."
            )
        if any(
            isinstance(index, (bool, np.bool_))
            or not isinstance(index, Integral)
            for index in raw_pattern
        ):
            raise TypeError("Ordinal pattern indices must be integers.")
        normalized_pattern = tuple(int(index) for index in raw_pattern)
        if sorted(normalized_pattern) != list(range(order)):
            raise ValueError(
                "Each ordinal pattern must be a permutation of 0 to n - 1."
            )

        if isinstance(probability, (bool, np.bool_)) or not isinstance(
            probability, Real
        ):
            raise TypeError("Pattern probabilities must be real numbers.")
        probability_value = float(probability)
        if not isfinite(probability_value) or probability_value < 0.0:
            raise ValueError(
                "Pattern probabilities must be finite and non-negative."
            )
        probabilities.append(probability_value)

    probability_sum = fsum(probabilities)
    if not np.isclose(probability_sum, 1.0, rtol=1e-9, atol=1e-12):
        raise ValueError("Pattern probabilities must sum to 1.")

    positive_probabilities = [
        probability for probability in probabilities if probability > 0.0
    ]
    entropy = -fsum(
        probability * log2(probability)
        for probability in positive_probabilities
    )
    entropy = max(0.0, entropy)
    maximum_entropy = log2(factorial(order))

    return {
        "entropy": entropy,
        "maximum_entropy": maximum_entropy,
        "normalized_entropy": entropy / maximum_entropy,
        "entropy_per_symbol": entropy / (order - 1),
    }


def permutation_entropy(
    series: ArrayLike,
    order: int = 3,
    tie_method: str = "error",
    random_state: int | np.random.Generator | None = None,
) -> PermutationEntropyResult:
    """Run the complete Bandt-Pompe permutation entropy pipeline.

    The logarithm uses base 2, so entropy values are expressed in bits.
    Consecutive samples are used, corresponding to a delay of one.

    Parameters
    ----------
    series:
        One-dimensional time series.
    order:
        Ordinal-pattern length. Bandt and Pompe recommend 3 to 7 for
        practical applications.
    tie_method:
        Either ``"error"`` or ``"jitter"``.
    random_state:
        Optional seed or NumPy generator used when resolving ties.

    Returns
    -------
    PermutationEntropyResult
        Entropy measures, ordinal representation, pattern statistics,
        and lightweight pipeline metadata.
    """
    values = validate_series(series, order, tie_method=tie_method)
    windows = build_windows(values, order)
    pattern_sequence = build_ordinal_sequence(
        windows,
        tie_method=tie_method,
        random_state=random_state,
    )
    pattern_counts = count_ordinal_patterns(pattern_sequence)
    pattern_probabilities = estimate_pattern_probabilities(pattern_counts)
    entropy_results = compute_permutation_entropy(
        pattern_probabilities,
        order,
    )

    return PermutationEntropyResult(
        entropy=entropy_results["entropy"],
        maximum_entropy=entropy_results["maximum_entropy"],
        normalized_entropy=entropy_results["normalized_entropy"],
        entropy_per_symbol=entropy_results["entropy_per_symbol"],
        pattern_sequence=pattern_sequence,
        pattern_counts=pattern_counts,
        pattern_probabilities=pattern_probabilities,
        order=int(order),
        number_of_windows=len(pattern_sequence),
        number_of_possible_patterns=factorial(order),
        number_of_observed_patterns=len(pattern_counts),
    )

# Code was generated by Codex