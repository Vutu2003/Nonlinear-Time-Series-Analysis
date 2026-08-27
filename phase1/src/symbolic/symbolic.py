"""Symbolic dynamics based on Guzzetti et al. (2005)."""

from dataclasses import dataclass
from numbers import Integral

import numpy as np
from numpy.typing import ArrayLike, NDArray


__all__ = [
    "FAMILY_0V",
    "FAMILY_1V",
    "FAMILY_2LV",
    "FAMILY_2UV",
    "SymbolicDynamicsResult",
    "quantize_intervals",
    "build_words",
    "classify_patterns",
    "compute_family_percentages",
    "analyze_symbolic_dynamics",
]


FAMILY_0V = 0
FAMILY_1V = 1
FAMILY_2LV = 2
FAMILY_2UV = 3


@dataclass(frozen=True, slots=True)
class SymbolicDynamicsResult:
    """Store symbolic dynamics metrics and sequences."""

    pct_0v: float
    pct_1v: float
    pct_2lv: float
    pct_2uv: float
    pct_2v: float
    n_intervals: int
    n_words: int
    symbols: NDArray[np.int64]
    families: NDArray[np.int64]


def _as_1d_array(values: ArrayLike, name: str) -> NDArray:
    """Return a non-empty one-dimensional array."""
    try:
        array = np.asarray(values)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be one-dimensional.") from exc

    if array.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional.")
    if array.size == 0:
        raise ValueError(f"{name} must not be empty.")

    return array


def _as_integer_array(
    values: ArrayLike,
    name: str,
) -> NDArray[np.int64]:
    """Return a validated integer array."""
    array = _as_1d_array(values, name)

    if np.issubdtype(array.dtype, np.bool_):
        raise TypeError(f"{name} must contain integers.")
    if not np.issubdtype(array.dtype, np.integer):
        raise TypeError(f"{name} must contain integers.")

    return np.asarray(array, dtype=np.int64)


def _validate_n_levels(n_levels: int) -> int:
    """Validate the number of symbolic levels."""
    if isinstance(n_levels, (bool, np.bool_)):
        raise TypeError("n_levels must be an integer.")
    if not isinstance(n_levels, Integral):
        raise TypeError("n_levels must be an integer.")
    if n_levels < 1:
        raise ValueError("n_levels must be at least 1.")

    return int(n_levels)


def quantize_intervals(
    intervals: ArrayLike,
    n_levels: int = 6,
) -> NDArray[np.int64]:
    """Quantize beat intervals into equal-width symbolic levels."""
    n_levels = _validate_n_levels(n_levels)
    raw = _as_1d_array(intervals, "intervals")

    if np.iscomplexobj(raw):
        raise ValueError("intervals must contain real values.")

    try:
        values = np.asarray(raw, dtype=np.float64)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            "intervals must contain real numeric values."
        ) from exc

    if not np.isfinite(values).all():
        raise ValueError("intervals must contain only finite values.")

    minimum = float(np.min(values))
    maximum = float(np.max(values))
    value_range = maximum - minimum

    if value_range == 0.0 or n_levels == 1:
        return np.zeros(values.size, dtype=np.int64)

    internal_edges = minimum + (
        value_range
        * np.arange(1, n_levels, dtype=np.float64)
        / n_levels
    )

    return np.searchsorted(
        internal_edges,
        values,
        side="right",
    ).astype(np.int64)


def build_words(symbols: ArrayLike) -> NDArray[np.int64]:
    """Build overlapping words of length three."""
    values = _as_integer_array(symbols, "symbols")

    if values.size < 3:
        raise ValueError("symbols must contain at least three values.")
    if np.any(values < 0):
        raise ValueError("symbols must be non-negative.")

    return np.lib.stride_tricks.sliding_window_view(
        values,
        3,
    ).copy()


def classify_patterns(words: ArrayLike) -> NDArray[np.int64]:
    """Classify words into 0V, 1V, 2LV, and 2UV families."""
    try:
        values = np.asarray(words)
    except (TypeError, ValueError) as exc:
        raise ValueError("words must be a rectangular array.") from exc

    if values.ndim != 2 or values.shape[1] != 3:
        raise ValueError("words must have shape (n_words, 3).")
    if values.shape[0] == 0:
        raise ValueError("words must not be empty.")
    if np.issubdtype(values.dtype, np.bool_):
        raise TypeError("words must contain integers.")
    if not np.issubdtype(values.dtype, np.integer):
        raise TypeError("words must contain integers.")

    values = np.asarray(values, dtype=np.int64)

    if np.any(values < 0):
        raise ValueError("words must be non-negative.")

    d1 = values[:, 1] - values[:, 0]
    d2 = values[:, 2] - values[:, 1]

    mask_0v = (d1 == 0) & (d2 == 0)
    mask_1v = (d1 == 0) ^ (d2 == 0)
    mask_2lv = ((d1 > 0) & (d2 > 0)) | ((d1 < 0) & (d2 < 0))
    mask_2uv = ((d1 > 0) & (d2 < 0)) | ((d1 < 0) & (d2 > 0))

    families = np.empty(values.shape[0], dtype=np.int64)
    families[mask_0v] = FAMILY_0V
    families[mask_1v] = FAMILY_1V
    families[mask_2lv] = FAMILY_2LV
    families[mask_2uv] = FAMILY_2UV

    assigned = (
        mask_0v.astype(np.int8)
        + mask_1v.astype(np.int8)
        + mask_2lv.astype(np.int8)
        + mask_2uv.astype(np.int8)
    )

    if not np.all(assigned == 1):
        raise RuntimeError("Pattern classification failed.")

    return families


def compute_family_percentages(
    families: ArrayLike,
) -> tuple[float, float, float, float, float]:
    """Compute symbolic family percentages."""
    values = _as_integer_array(families, "families")

    if np.any((values < FAMILY_0V) | (values > FAMILY_2UV)):
        raise ValueError("families must contain values from 0 to 3.")

    counts = np.bincount(values, minlength=4)
    percentages = counts.astype(np.float64) * (100.0 / values.size)

    pct_0v = float(percentages[FAMILY_0V])
    pct_1v = float(percentages[FAMILY_1V])
    pct_2lv = float(percentages[FAMILY_2LV])
    pct_2uv = float(percentages[FAMILY_2UV])
    pct_2v = pct_2lv + pct_2uv

    return pct_0v, pct_1v, pct_2lv, pct_2uv, pct_2v


def analyze_symbolic_dynamics(
    intervals: ArrayLike,
    n_levels: int = 6,
) -> SymbolicDynamicsResult:
    """Run the Guzzetti symbolic dynamics analysis."""
    symbols = quantize_intervals(intervals, n_levels=n_levels)
    words = build_words(symbols)
    families = classify_patterns(words)

    (
        pct_0v,
        pct_1v,
        pct_2lv,
        pct_2uv,
        pct_2v,
    ) = compute_family_percentages(families)

    return SymbolicDynamicsResult(
        pct_0v=pct_0v,
        pct_1v=pct_1v,
        pct_2lv=pct_2lv,
        pct_2uv=pct_2uv,
        pct_2v=pct_2v,
        n_intervals=int(symbols.size),
        n_words=int(families.size),
        symbols=symbols,
        families=families,
    )
