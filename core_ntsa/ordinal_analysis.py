"""Ordinal analysis based on Keller and Sinn (2005)."""

from collections import Counter
from dataclasses import dataclass
from math import factorial, fsum, nextafter
from numbers import Integral
from typing import Iterable, Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray


OrdinalPattern = tuple[int, ...]
InversionVector = tuple[int, ...]

__all__ = [
    "OrdinalAnalysisResult",
    "validate_series",
    "build_delayed_windows",
    "encode_ordinal_pattern",
    "compute_inversion_vector",
    "inversion_to_permutation",
    "compute_ordinal_number",
    "compute_normalized_ordinal_value",
    "build_ordinal_pattern_sequence",
    "build_inversion_sequence",
    "build_ordinal_number_sequence",
    "build_ordinal_transformed_series",
    "compute_pattern_distribution",
    "ordinal_analysis",
]


@dataclass(frozen=True, slots=True)
class OrdinalAnalysisResult:
    """Store the outputs of the ordinal-analysis pipeline."""

    d: int
    tau: int
    n_samples: int
    n_windows: int
    time_indices: NDArray[np.int64]
    delayed_windows: NDArray[np.float64]
    ordinal_patterns: tuple[OrdinalPattern, ...]
    inversion_vectors: NDArray[np.int64]
    ordinal_numbers: NDArray
    ordinal_values: NDArray[np.float64]


def _validate_positive_integer(value: int, name: str) -> int:
    """Validate a positive integer parameter."""
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be an integer.")
    if value < 1:
        raise ValueError(f"{name} must be at least 1.")
    return int(value)


def _as_finite_array(
    values: ArrayLike,
    name: str,
    ndim: int,
) -> NDArray[np.float64]:
    """Convert input to a finite float array."""
    try:
        array = np.asarray(values)
        if np.iscomplexobj(array):
            raise ValueError
        array = np.asarray(values, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain real numeric values.") from exc

    if array.ndim != ndim:
        dimension = "one" if ndim == 1 else "two"
        raise ValueError(f"{name} must be {dimension}-dimensional.")
    if not np.isfinite(array).all():
        raise ValueError(f"{name} must contain only finite values.")
    return array


def _validate_window(window: ArrayLike) -> NDArray[np.float64]:
    """Validate one delayed window."""
    values = _as_finite_array(window, "Window", ndim=1)
    if values.size < 2:
        raise ValueError("Window must contain at least two values.")
    return values


def _validate_windows(windows: ArrayLike) -> NDArray[np.float64]:
    """Validate a collection of delayed windows."""
    values = _as_finite_array(windows, "Windows", ndim=2)
    if values.shape[0] == 0:
        raise ValueError("Windows must contain at least one row.")
    if values.shape[1] < 2:
        raise ValueError("Each window must contain at least two values.")
    return values


def _validate_inversion(inversion: Sequence[int]) -> InversionVector:
    """Validate an inversion vector."""
    try:
        raw_values = tuple(inversion)
    except TypeError as exc:
        raise ValueError("Inversion must be an integer sequence.") from exc

    if not raw_values:
        raise ValueError("Inversion must contain at least one value.")

    values: list[int] = []
    for position, value in enumerate(raw_values, start=1):
        if isinstance(value, (bool, np.bool_)) or not isinstance(
            value, Integral
        ):
            raise TypeError("Inversion values must be integers.")
        if not 0 <= value <= position:
            raise ValueError(
                f"Inversion value at position {position} must be between "
                f"0 and {position}."
            )
        values.append(int(value))
    return tuple(values)


def _validate_inversion_sequence(
    inversion_sequence: ArrayLike,
) -> NDArray[np.int64]:
    """Validate a two-dimensional inversion sequence."""
    try:
        raw_values = np.asarray(inversion_sequence)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "Inversion sequence must be a rectangular array."
        ) from exc

    if raw_values.ndim != 2:
        raise ValueError("Inversion sequence must be two-dimensional.")
    if raw_values.shape[0] == 0 or raw_values.shape[1] == 0:
        raise ValueError("Inversion sequence must not be empty.")

    rows = [_validate_inversion(row) for row in raw_values]
    return np.asarray(rows, dtype=np.int64)


def _validate_pattern(pattern: Sequence[int]) -> OrdinalPattern:
    """Validate one ordinal pattern."""
    try:
        raw_values = tuple(pattern)
    except TypeError as exc:
        raise ValueError("Pattern must be an integer sequence.") from exc

    if len(raw_values) < 2:
        raise ValueError("Pattern must contain at least two indices.")
    if any(
        isinstance(value, (bool, np.bool_))
        or not isinstance(value, Integral)
        for value in raw_values
    ):
        raise TypeError("Pattern indices must be integers.")

    values = tuple(int(value) for value in raw_values)
    if sorted(values) != list(range(len(values))):
        raise ValueError("Pattern must be a permutation of 0 to n - 1.")
    return values


def validate_series(
    x: ArrayLike,
    d: int,
    tau: int = 1,
) -> NDArray[np.float64]:
    """Validate a time series and its ordinal parameters."""
    dimension = _validate_positive_integer(d, "d")
    delay = _validate_positive_integer(tau, "tau")
    values = _as_finite_array(x, "Series", ndim=1)
    if values.size <= dimension * delay:
        raise ValueError("Series length must be greater than d * tau.")
    return values


def build_delayed_windows(
    x: ArrayLike,
    d: int,
    tau: int = 1,
) -> NDArray[np.float64]:
    """Build windows ordered from the present to the past."""
    values = validate_series(x, d, tau)
    dimension = int(d)
    delay = int(tau)
    time_indices = np.arange(dimension * delay, values.size)
    offsets = np.arange(dimension + 1) * delay
    return values[time_indices[:, None] - offsets]


def encode_ordinal_pattern(window: ArrayLike) -> OrdinalPattern:
    """Encode a window using Keller's descending convention."""
    values = _validate_window(window)
    indices = np.arange(values.size)
    order = np.lexsort((-indices, -values))
    return tuple(int(index) for index in order)


def compute_inversion_vector(window: ArrayLike) -> InversionVector:
    """Compute the inversion vector of one delayed window."""
    values = _validate_window(window)
    return tuple(
        int(np.count_nonzero(values[:position] <= values[position]))
        for position in range(1, values.size)
    )


def inversion_to_permutation(
    inversion: Sequence[int],
) -> OrdinalPattern:
    """Recover an ordinal pattern from its inversion vector."""
    values = _validate_inversion(inversion)
    pattern = [0]
    for index, count in enumerate(values, start=1):
        pattern.insert(index - count, index)
    return tuple(pattern)


def compute_ordinal_number(inversion: Sequence[int]) -> int:
    """Map an inversion vector to its exact ordinal number."""
    values = _validate_inversion(inversion)
    scale = factorial(len(values) + 1)
    return sum(
        value * scale // factorial(position + 1)
        for position, value in enumerate(values, start=1)
    )


def compute_normalized_ordinal_value(
    inversion: Sequence[int],
) -> float:
    """Map an inversion vector to a normalized ordinal value."""
    values = _validate_inversion(inversion)
    ordinal_value = fsum(
        value / factorial(position + 1)
        for position, value in enumerate(values, start=1)
    )
    return min(ordinal_value, nextafter(1.0, 0.0))


def build_ordinal_pattern_sequence(
    windows: ArrayLike,
) -> tuple[OrdinalPattern, ...]:
    """Encode delayed windows as ordinal patterns."""
    values = _validate_windows(windows)
    return tuple(encode_ordinal_pattern(window) for window in values)


def build_inversion_sequence(
    windows: ArrayLike,
) -> NDArray[np.int64]:
    """Encode delayed windows as inversion vectors."""
    values = _validate_windows(windows)
    inversions = [compute_inversion_vector(window) for window in values]
    return np.asarray(inversions, dtype=np.int64)


def build_ordinal_number_sequence(
    inversion_sequence: ArrayLike,
) -> NDArray:
    """Convert inversion vectors to exact ordinal numbers."""
    values = _validate_inversion_sequence(inversion_sequence)
    numbers = [compute_ordinal_number(row) for row in values]
    return np.asarray(numbers)


def build_ordinal_transformed_series(
    inversion_sequence: ArrayLike,
) -> NDArray[np.float64]:
    """Convert inversion vectors to normalized ordinal values."""
    values = _validate_inversion_sequence(inversion_sequence)
    return np.asarray(
        [compute_normalized_ordinal_value(row) for row in values],
        dtype=np.float64,
    )


def compute_pattern_distribution(
    pattern_sequence: Iterable[Sequence[int]],
) -> tuple[dict[OrdinalPattern, int], dict[OrdinalPattern, float]]:
    """Compute empirical counts and probabilities of patterns."""
    counts: Counter[OrdinalPattern] = Counter()
    pattern_length: int | None = None

    for pattern in pattern_sequence:
        values = _validate_pattern(pattern)
        if pattern_length is None:
            pattern_length = len(values)
        elif len(values) != pattern_length:
            raise ValueError("All patterns must have the same length.")
        counts[values] += 1

    if not counts:
        raise ValueError("Pattern sequence must not be empty.")

    count_dict = dict(counts)
    total = sum(count_dict.values())
    probabilities = {
        pattern: count / total for pattern, count in count_dict.items()
    }
    return count_dict, probabilities


def ordinal_analysis(
    x: ArrayLike,
    d: int,
    tau: int = 1,
) -> OrdinalAnalysisResult:
    """Run the complete Keller ordinal-analysis pipeline."""
    values = validate_series(x, d, tau)
    dimension = int(d)
    delay = int(tau)
    windows = build_delayed_windows(values, dimension, delay)
    patterns = build_ordinal_pattern_sequence(windows)
    inversions = build_inversion_sequence(windows)
    numbers = build_ordinal_number_sequence(inversions)
    ordinal_values = build_ordinal_transformed_series(inversions)

    return OrdinalAnalysisResult(
        d=dimension,
        tau=delay,
        n_samples=values.size,
        n_windows=windows.shape[0],
        time_indices=np.arange(dimension * delay, values.size),
        delayed_windows=windows,
        ordinal_patterns=patterns,
        inversion_vectors=inversions,
        ordinal_numbers=numbers,
        ordinal_values=ordinal_values,
    )
