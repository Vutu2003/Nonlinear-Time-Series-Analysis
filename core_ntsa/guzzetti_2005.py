"""Symbolic heart-rate dynamics based on Guzzetti et al. (2005)."""

from dataclasses import dataclass
from numbers import Integral

import numpy as np
from numpy.typing import ArrayLike, NDArray


__all__ = [
    "SymbolicDynamicsResult",
    "quantize_rr",
    "build_words",
    "classify_patterns",
    "compute_family_percentages",
    "analyze_symbolic_dynamics",
]


@dataclass(frozen=True, slots=True)
class SymbolicDynamicsResult:
    """Store percentages and intermediate symbolic sequences."""

    pct_0v: float
    pct_1v: float
    pct_2v: float
    symbols: NDArray[np.int64]
    families: NDArray[np.int64]


def _as_one_dimensional_array(
    values: ArrayLike,
    name: str,
) -> NDArray:
    """Convert input to a non-empty one-dimensional array."""
    try:
        array = np.asarray(values)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a one-dimensional array.") from exc

    if array.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional.")
    if array.size == 0:
        raise ValueError(f"{name} must not be empty.")
    return array


def _as_integer_array(values: ArrayLike, name: str) -> NDArray[np.int64]:
    """Validate and convert an integer sequence."""
    array = _as_one_dimensional_array(values, name)
    if np.issubdtype(array.dtype, np.bool_) or not np.issubdtype(
        array.dtype, np.integer
    ):
        raise TypeError(f"{name} must contain integers.")
    return np.asarray(array, dtype=np.int64)


def quantize_rr(
    rr: ArrayLike,
    n_levels: int = 6,
) -> NDArray[np.int64]:
    """Map RR intervals to equal-width symbolic levels."""
    if isinstance(n_levels, (bool, np.bool_)) or not isinstance(
        n_levels, Integral
    ):
        raise TypeError("n_levels must be an integer.")
    if n_levels < 1:
        raise ValueError("n_levels must be at least 1.")

    raw_values = _as_one_dimensional_array(rr, "rr")
    if np.iscomplexobj(raw_values):
        raise ValueError("rr must contain real numeric values.")

    try:
        values = np.asarray(raw_values, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError("rr must contain real numeric values.") from exc

    if not np.isfinite(values).all():
        raise ValueError("rr must contain only finite values.")

    minimum = float(np.min(values))
    value_range = float(np.max(values) - minimum)
    if value_range == 0.0 or n_levels == 1:
        return np.zeros(values.size, dtype=np.int64)

    normalized = (values - minimum) / value_range
    symbols = np.floor(normalized * int(n_levels)).astype(np.int64)

    # Keep the maximum value inside the last half-open interval.
    return np.clip(symbols, 0, int(n_levels) - 1)


def build_words(symbols: ArrayLike) -> NDArray[np.int64]:
    """Build overlapping three-symbol words."""
    values = _as_integer_array(symbols, "symbols")
    if values.size < 3:
        raise ValueError("symbols must contain at least three values.")
    if np.any(values < 0):
        raise ValueError("symbols must contain non-negative values.")

    return np.lib.stride_tricks.sliding_window_view(values, 3).copy()


def classify_patterns(words: ArrayLike) -> NDArray[np.int64]:
    """Classify three-symbol words as 0V, 1V, or 2V."""
    try:
        values = np.asarray(words)
    except (TypeError, ValueError) as exc:
        raise ValueError("words must be a rectangular array.") from exc

    if values.ndim != 2 or values.shape[1] != 3:
        raise ValueError("words must have shape (n_words, 3).")
    if values.shape[0] == 0:
        raise ValueError("words must contain at least one row.")
    if np.issubdtype(values.dtype, np.bool_) or not np.issubdtype(
        values.dtype, np.integer
    ):
        raise TypeError("words must contain integers.")
    if np.any(values < 0):
        raise ValueError("words must contain non-negative values.")

    changes = values[:, 1:] != values[:, :-1]
    return np.sum(changes, axis=1, dtype=np.int64)


def compute_family_percentages(
    families: ArrayLike,
) -> tuple[float, float, float]:
    """Compute the percentages of the 0V, 1V, and 2V families."""
    values = _as_integer_array(families, "families")
    if np.any((values < 0) | (values > 2)):
        raise ValueError("families must contain only 0, 1, or 2.")

    counts = np.bincount(values, minlength=3)
    percentages = counts.astype(np.float64) * (100.0 / values.size)
    return (
        float(percentages[0]),
        float(percentages[1]),
        float(percentages[2]),
    )


def analyze_symbolic_dynamics(
    rr: ArrayLike,
    n_levels: int = 6,
) -> SymbolicDynamicsResult:
    """Run the complete Guzzetti symbolic-dynamics pipeline."""
    symbols = quantize_rr(rr, n_levels=n_levels)
    words = build_words(symbols)
    families = classify_patterns(words)
    pct_0v, pct_1v, pct_2v = compute_family_percentages(families)

    return SymbolicDynamicsResult(
        pct_0v=pct_0v,
        pct_1v=pct_1v,
        pct_2v=pct_2v,
        symbols=symbols,
        families=families,
    )
