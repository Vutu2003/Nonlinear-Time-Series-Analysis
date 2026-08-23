"""Simplex projection for nonlinear state-space prediction."""

from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import pearsonr


@dataclass
class SimplexResult:
    """Store predictions for one forecast horizon."""

    horizon: int
    times: np.ndarray
    y_true: np.ndarray
    y_pred: np.ndarray
    valid: np.ndarray

    @property
    def n_valid(self) -> int:
        """Count predictions marked as valid by the result mask."""
        return int(np.sum(self.valid))


@dataclass
class PredictionMetrics:
    """Store prediction metrics for one forecast horizon."""

    horizon: int
    cc: float
    rmse: float
    nrmse: float
    n_valid: int


def _validate_inputs(
    signal: np.ndarray,
    tau: int,
    m: int,
    horizon: int,
    theiler_window: int,
) -> np.ndarray:
    """Validate prediction settings and return the signal as a float array.

    The signal must be finite and one-dimensional. The remaining arguments
    must define a valid embedding with enough samples for prediction.
    """

    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be one-dimensional.")

    if not np.all(np.isfinite(signal)):
        raise ValueError("signal must contain only finite values.")

    if tau < 1:
        raise ValueError("tau must be at least 1.")

    if m < 1:
        raise ValueError("m must be at least 1.")

    if horizon < 1:
        raise ValueError("horizon must be at least 1.")

    if theiler_window < 0:
        raise ValueError("theiler_window must be non-negative.")

    min_length = (m - 1) * tau + horizon + 2
    if len(signal) < min_length:
        raise ValueError("signal is too short for this configuration.")

    return signal


def _build_embedding(
    signal: np.ndarray,
    tau: int,
    m: int,
    horizon: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build delay-coordinate states and their future prediction targets.

    Each state is ordered as ``[x(t), x(t - tau), ...]``. The matching target
    is ``x(t + horizon)``, and ``times`` stores every state time ``t``.
    """

    start = (m - 1) * tau
    stop = len(signal) - horizon
    times = np.arange(start, stop)

    offsets = np.arange(m) * tau
    indices = times[:, None] - offsets[None, :]

    states = signal[indices]
    targets = signal[times + horizon]

    return states, targets, times


def _query_valid_neighbors(
    tree: cKDTree,
    query: np.ndarray,
    query_time: int,
    times: np.ndarray,
    n_neighbors: int,
    theiler_window: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Find nearest states outside the query's temporal exclusion window.

    Returns neighbor distances and row indices in ``times``. Fewer than the
    requested number may be returned when too few admissible states exist.
    """

    n_states = len(times)

    if n_states <= n_neighbors:
        return np.array([]), np.array([], dtype=int)

    query_k = min(max(2 * n_neighbors, 16), n_states)

    while True:
        distances, indices = tree.query(query, k=query_k)

        distances = np.atleast_1d(distances)
        indices = np.atleast_1d(indices)

        time_distance = np.abs(times[indices] - query_time)
        admissible = time_distance > theiler_window

        valid_distances = distances[admissible]
        valid_indices = indices[admissible]

        if len(valid_indices) >= n_neighbors:
            return (
                valid_distances[:n_neighbors],
                valid_indices[:n_neighbors],
            )

        if query_k == n_states:
            return valid_distances, valid_indices

        query_k = min(2 * query_k, n_states)


def _simplex_weights(distances: np.ndarray) -> np.ndarray:
    """Convert neighbor distances into normalized exponential weights.

    Exact matches share the full weight equally; otherwise, nearer neighbors
    receive more weight relative to the closest-neighbor distance.
    """

    zero_mask = np.isclose(
        distances,
        0.0,
        rtol=0.0,
        atol=np.finfo(float).eps,
    )

    if np.any(zero_mask):
        weights = zero_mask.astype(float)
        return weights / np.sum(weights)

    reference_distance = distances[0]
    weights = np.exp(-distances / reference_distance)

    return weights / np.sum(weights)


def simplex_projection(
    signal: np.ndarray,
    tau: int,
    m: int,
    horizon: int,
    theiler_window: int,
) -> SimplexResult:
    """
    Predict future signal values with leave-one-out simplex projection.

    The signal is reconstructed into ``m``-dimensional delay states. For each
    state, the method finds ``m + 1`` nearest admissible states, combines their
    future values using distance-based weights, and excludes temporally close
    neighbors according to ``theiler_window``.

    Parameters
    ----------
    signal : array-like
        One-dimensional finite time series.
    tau : int
        Embedding delay in samples.
    m : int
        Embedding dimension.
    horizon : int
        Prediction horizon in samples.
    theiler_window : int
        Number of neighboring time steps excluded on each side of a query.

    Returns
    -------
    SimplexResult
        State times, observed targets, predictions, and their validity mask.
    """

    signal = _validate_inputs(
        signal,
        tau,
        m,
        horizon,
        theiler_window,
    )

    states, targets, times = _build_embedding(
        signal,
        tau,
        m,
        horizon,
    )

    n_neighbors = m + 1

    if len(states) <= n_neighbors:
        raise ValueError("Not enough embedded states for simplex prediction.")

    tree = cKDTree(states)

    predictions = np.full(len(states), np.nan)

    for query_idx, query in enumerate(states):
        distances, indices = _query_valid_neighbors(
            tree=tree,
            query=query,
            query_time=times[query_idx],
            times=times,
            n_neighbors=n_neighbors,
            theiler_window=theiler_window,
        )

        if len(indices) < n_neighbors:
            continue

        weights = _simplex_weights(distances)
        neighbor_targets = targets[indices]

        predictions[query_idx] = np.dot(
            weights,
            neighbor_targets,
        )

    valid = np.isfinite(predictions)

    return SimplexResult(
        horizon=horizon,
        times=times,
        y_true=targets,
        y_pred=predictions,
        valid=valid,
    )


def prediction_metrics(
    result: SimplexResult,
    nrmse_scale: float,
) -> PredictionMetrics:
    """
    Compute CC, RMSE, and NRMSE from simplex predictions.

    Parameters
    ----------
    result : SimplexResult
        Simplex prediction result.
    nrmse_scale : float
        Explicit normalization scale for NRMSE.

    Returns
    -------
    PredictionMetrics
        Prediction metrics.
    """

    if not np.isfinite(nrmse_scale) or nrmse_scale <= 0:
        raise ValueError("nrmse_scale must be positive and finite.")

    y_true = result.y_true[result.valid]
    y_pred = result.y_pred[result.valid]

    if len(y_true) < 2:
        return PredictionMetrics(
            horizon=result.horizon,
            cc=np.nan,
            rmse=np.nan,
            nrmse=np.nan,
            n_valid=len(y_true),
        )

    errors = y_true - y_pred
    rmse = float(np.sqrt(np.mean(errors**2)))
    nrmse = rmse / nrmse_scale

    if np.std(y_true) == 0 or np.std(y_pred) == 0:
        cc = np.nan
    else:
        cc = float(pearsonr(y_true, y_pred).statistic)

    return PredictionMetrics(
        horizon=result.horizon,
        cc=cc,
        rmse=rmse,
        nrmse=nrmse,
        n_valid=len(y_true),
    )


def prediction_curve(
    signal: np.ndarray,
    tau: int,
    m: int,
    horizons: Iterable[int],
    theiler_window: int,
    scale_function: Callable[[np.ndarray], float],
) -> list[PredictionMetrics]:
    """
    Compute simplex prediction metrics across forecast horizons.

    Parameters
    ----------
    signal : array-like
        Input time series.
    tau : int
        Embedding delay in samples.
    m : int
        Embedding dimension.
    horizons : iterable of int
        Prediction horizons in samples.
    theiler_window : int
        Temporal exclusion window in samples.
    scale_function : callable
        Function returning the NRMSE normalization scale.

    Returns
    -------
    list of PredictionMetrics
        Metrics for all prediction horizons.
    """

    metrics = []

    for horizon in horizons:
        result = simplex_projection(
            signal=signal,
            tau=tau,
            m=m,
            horizon=int(horizon),
            theiler_window=theiler_window,
        )

        y_true = result.y_true[result.valid]

        if len(y_true) == 0:
            metrics.append(
                PredictionMetrics(
                    horizon=int(horizon),
                    cc=np.nan,
                    rmse=np.nan,
                    nrmse=np.nan,
                    n_valid=0,
                )
            )
            continue

        scale = float(scale_function(y_true))

        metrics.append(
            prediction_metrics(
                result=result,
                nrmse_scale=scale,
            )
        )

    return metrics
