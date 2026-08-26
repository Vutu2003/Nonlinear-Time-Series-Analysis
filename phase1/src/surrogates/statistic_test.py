"""PPS surrogate generation and statistical inference."""

# OUTPUT OF run_session_test()
#
# Returns: (window_results_df, surrogate_results_df)
#
# window_results_df contains one row per signal window. Its metadata columns
# are session, representation, state, window_size, window_id, rho_star,
# sampling_rate, m, tau_seconds, tau_samples, n_horizons, hmax_seconds,
# hmax_samples, theiler_seconds, theiler_samples, M, and master_seed.
# Each metric adds:
# <metric>_original, <metric>_surrogate_mean, <metric>_surrogate_sd,
# <metric>_surrogate_median, <metric>_rank, <metric>_p, <metric>_reject,
# and <metric>_direction.
#
# surrogate_results_df contains M rows per signal window, one for each PPS
# realization. Its columns are the window identity, surrogate_id, seed, and
# the scalar metrics CC, NRMSE, DET, Lmean, ENTR, Lmax, LAM, TT, and Vmax.
# No PPS waveform, embedding, distance matrix, or recurrence matrix is kept.
# With fail_fast=False, failed-window details are stored in
# DataFrame.attrs["failures"]; failed windows are absent from both tables.
#
# FROZEN METRIC CORES
#
# Shared embedding:
# m = 8.
# tau = 0.16 s for Processed and 0.20 s for Raw.
# At 25 Hz, tau = 4 and 5 samples; at 50 Hz, tau = 8 and 10 samples.
# Original signals and PPS surrogates use exactly the same settings.
#
# Simplex Projection:
# prediction curve = 18 frozen horizons from 0.04 s to Hmax = 4 s;
# Theiler window = 1 s;
# horizons and Theiler are converted using each window's sampling rate;
# Euclidean nearest neighbors;
# k = m + 1 = 9;
# exponential simplex distance weighting;
# leave-one-out prediction.
# Returns mean CC and mean NRMSE across the curve. NRMSE is normalized by
# the standard deviation of the evaluated signal.
#
# RQA:
# Euclidean distance;
# fixed target recurrence rate RR = 0.02;
# Theiler window = (m - 1) * tau;
# l_min = 2;
# v_min = 2.
# Returns DET, Lmean, ENTR, Lmax, LAM, TT, and Vmax.

from __future__ import annotations

import copy
import hashlib
import json
import math
import re
import time
import warnings
from collections.abc import Mapping
from typing import Any

import numpy as np
import pandas as pd
from joblib import Parallel, delayed, parallel_config
from threadpoolctl import threadpool_limits

try:
    from .pps import generate_pps_signal
    from ..prediction.simplex_projection import prediction_curve
    from ..rqa.rqa import run_rqa
except ImportError:
    from prediction.simplex_projection import prediction_curve
    from rqa.rqa import run_rqa
    from surrogates.pps import generate_pps_signal


METRIC_NAMES = (
    "CC",
    "NRMSE",
    "DET",
    "Lmean",
    "ENTR",
    "Lmax",
    "LAM",
    "TT",
    "Vmax",
)

METADATA_COLUMNS = (
    "session",
    "representation",
    "state",
    "window_size",
    "window_id",
)

SURROGATE_CONFIG = {
    "m": 8,
    "M": 39,
    "alpha": 0.05,
    "alternative": "two-sided",
    "tau_seconds": {
        "Processed": 0.16,
        "Raw": 0.20,
    },
    "pps": {
        "return_indices": False,
    },
    "simplex": {
        "horizon_seconds": (
            0.04,
            0.08,
            0.12,
            0.16,
            0.20,
            0.28,
            0.40,
            0.60,
            0.80,
            1.00,
            1.20,
            1.60,
            2.00,
            2.40,
            2.80,
            3.20,
            3.60,
            4.00,
        ),
        "theiler_seconds": 1.0,
        "nrmse_scale": "signal_std",
    },
    "rqa": {
        "l_min": 2,
        "v_min": 2,
        "target_rr": 0.02,
    },
}

COMPUTE_CONFIG = {
    "n_jobs": 6,
    "backend": "loky",
    "inner_threads": 1,
    "verbose": 1,
}


class WindowTestError(RuntimeError):
    """Report a failed window with its scientific context."""


def _python_scalar(value: Any) -> Any:
    """Convert NumPy scalars to built-in Python values."""
    return value.item() if isinstance(value, np.generic) else value


def _representation_name(value: Any) -> str:
    """Return a supported representation label."""
    name = str(value).strip().casefold()
    labels = {"processed": "Processed", "raw": "Raw"}
    if name not in labels:
        raise ValueError(
            "representation must be either 'Processed' or 'Raw'."
        )
    return labels[name]


def _representation_value(
    value: Any,
    representation: str,
    name: str,
) -> Any:
    """Resolve a scalar or representation-specific setting."""
    if not isinstance(value, Mapping):
        return value

    if representation not in value:
        raise ValueError(
            f"{name} has no value for representation={representation!r}."
        )
    return value[representation]


def _positive_integer(value: Any, name: str) -> int:
    """Validate a positive integer setting."""
    if isinstance(value, (bool, np.bool_)) or not isinstance(
        value,
        (int, np.integer),
    ):
        raise TypeError(f"{name} must be an integer.")
    if value < 1:
        raise ValueError(f"{name} must be at least 1.")
    return int(value)


def _nonnegative_integer(value: Any, name: str) -> int:
    """Validate a non-negative integer setting."""
    if isinstance(value, (bool, np.bool_)) or not isinstance(
        value,
        (int, np.integer),
    ):
        raise TypeError(f"{name} must be an integer.")
    if value < 0:
        raise ValueError(f"{name} must be non-negative.")
    return int(value)


def _positive_float(value: Any, name: str) -> float:
    """Validate a positive finite number."""
    number = float(value)
    if not np.isfinite(number) or number <= 0.0:
        raise ValueError(f"{name} must be positive and finite.")
    return number


def _sample_integer(value: Any, name: str) -> int:
    """Validate a positive integer-valued sample count."""
    number = float(value)
    rounded = round(number)
    if not np.isfinite(number) or not np.isclose(number, rounded):
        raise ValueError(f"{name} must be an integer-valued number.")
    return _positive_integer(int(rounded), name)


def _validate_config(config: Mapping[str, Any]) -> dict[str, Any]:
    """Validate and copy the scientific configuration."""
    if not isinstance(config, Mapping):
        raise TypeError("config must be a mapping.")

    required = {
        "m",
        "M",
        "alpha",
        "alternative",
        "tau_seconds",
        "pps",
        "simplex",
        "rqa",
    }
    missing = sorted(required.difference(config))
    if missing:
        raise ValueError(f"config is missing keys: {missing}.")

    checked = copy.deepcopy(dict(config))
    checked["m"] = _positive_integer(checked["m"], "m")
    checked["M"] = _positive_integer(checked["M"], "M")

    alpha = float(checked["alpha"])
    if not np.isfinite(alpha) or not 0.0 < alpha < 1.0:
        raise ValueError("alpha must be in (0, 1).")
    checked["alpha"] = alpha

    alternative = str(checked["alternative"]).strip().casefold()
    alternative = alternative.replace("_", "-")
    if alternative not in {"two-sided", "greater", "less"}:
        raise ValueError(
            "alternative must be 'two-sided', 'greater', or 'less'."
        )
    checked["alternative"] = alternative

    tau_config = checked["tau_seconds"]
    if not isinstance(tau_config, Mapping):
        raise TypeError("tau_seconds must be a mapping.")
    for representation in ("Processed", "Raw"):
        tau = _representation_value(
            tau_config,
            representation,
            "tau_seconds",
        )
        tau_config[representation] = _positive_float(
            tau,
            f"tau_seconds[{representation!r}]",
        )

    pps_config = checked["pps"]
    if not isinstance(pps_config, Mapping):
        raise TypeError("pps config must be a mapping.")
    if pps_config.get("return_indices", False):
        raise ValueError("pps.return_indices must be False.")

    simplex_config = checked["simplex"]
    if not isinstance(simplex_config, Mapping):
        raise TypeError("simplex config must be a mapping.")
    simplex_required = {
        "horizon_seconds",
        "theiler_seconds",
        "nrmse_scale",
    }
    simplex_missing = sorted(simplex_required.difference(simplex_config))
    if simplex_missing:
        raise ValueError(
            f"simplex config is missing keys: {simplex_missing}."
        )
    horizons = np.asarray(simplex_config["horizon_seconds"], dtype=float)
    if horizons.ndim != 1 or horizons.size == 0:
        raise ValueError("simplex.horizon_seconds must be a non-empty 1D grid.")
    if not np.all(np.isfinite(horizons)) or np.any(horizons <= 0.0):
        raise ValueError("simplex.horizon_seconds must be positive and finite.")
    if np.any(np.diff(horizons) <= 0.0):
        raise ValueError("simplex.horizon_seconds must be strictly increasing.")
    simplex_config["horizon_seconds"] = tuple(float(x) for x in horizons)
    simplex_config["theiler_seconds"] = _positive_float(
        simplex_config["theiler_seconds"],
        "simplex.theiler_seconds",
    )
    for representation in ("Processed", "Raw"):
        scale = _representation_value(
            simplex_config["nrmse_scale"],
            representation,
            "simplex.nrmse_scale",
        )
        if isinstance(scale, str):
            valid_scales = {
                "std",
                "signal_std",
                "iqr",
                "signal_iqr",
                "range",
                "signal_range",
            }
            if scale.strip().casefold() not in valid_scales:
                raise ValueError("unsupported simplex.nrmse_scale setting.")
        elif not np.isfinite(float(scale)) or float(scale) <= 0.0:
            raise ValueError("simplex.nrmse_scale must be positive.")

    rqa_config = checked["rqa"]
    if not isinstance(rqa_config, Mapping):
        raise TypeError("rqa config must be a mapping.")
    rqa_required = {"l_min", "v_min", "target_rr"}
    rqa_missing = sorted(rqa_required.difference(rqa_config))
    if rqa_missing:
        raise ValueError(f"rqa config is missing keys: {rqa_missing}.")

    l_min = _positive_integer(rqa_config["l_min"], "rqa.l_min")
    v_min = _positive_integer(rqa_config["v_min"], "rqa.v_min")
    if l_min < 2 or v_min < 2:
        raise ValueError("rqa.l_min and rqa.v_min must be at least 2.")
    target_rr = float(rqa_config["target_rr"])
    if not np.isfinite(target_rr) or not 0.0 < target_rr < 1.0:
        raise ValueError("rqa.target_rr must be in (0, 1).")

    return checked


def _validate_signal(signal: Any) -> np.ndarray:
    """Return a finite, non-constant one-dimensional signal."""
    values = np.asarray(signal, dtype=float)
    if values.ndim != 1:
        raise ValueError("signal must be one-dimensional.")
    if values.size == 0:
        raise ValueError("signal must not be empty.")
    if not np.all(np.isfinite(values)):
        raise ValueError("signal must contain only finite values.")
    if np.std(values) <= 0.0:
        raise ValueError("signal must have positive variance.")
    return values


def _nrmse_scale(
    signal: np.ndarray,
    setting: Any,
    representation: str,
) -> float:
    """Resolve the frozen NRMSE normalization scale."""
    setting = _representation_value(
        setting,
        representation,
        "simplex.nrmse_scale",
    )

    if isinstance(setting, str):
        name = setting.strip().casefold()
        if name in {"std", "signal_std"}:
            scale = float(np.std(signal))
        elif name in {"iqr", "signal_iqr"}:
            q25, q75 = np.percentile(signal, [25.0, 75.0])
            scale = float(q75 - q25)
        elif name in {"range", "signal_range"}:
            scale = float(np.ptp(signal))
        else:
            raise ValueError(
                "simplex.nrmse_scale must be a positive number, "
                "'signal_std', 'signal_iqr', or 'signal_range'."
            )
    else:
        scale = float(setting)

    if not np.isfinite(scale) or scale <= 0.0:
        raise ValueError("simplex NRMSE scale must be positive and finite.")
    return scale


def _resolve_metric_parameters(
    representation: str,
    sampling_rate: float,
    tau_samples: int,
    config: Mapping[str, Any],
) -> dict[str, Any]:
    """Convert frozen time parameters to window-specific samples."""
    representation = _representation_name(representation)
    sampling_rate = _positive_float(sampling_rate, "sampling_rate")
    tau_samples = _sample_integer(tau_samples, "tau_samples")

    tau_seconds = float(config["tau_seconds"][representation])
    expected_tau = max(1, int(round(tau_seconds * sampling_rate)))
    if tau_samples != expected_tau:
        raise ValueError(
            f"tau_samples={tau_samples} is inconsistent with "
            f"representation={representation!r}, sampling_rate="
            f"{sampling_rate:.6g}, and tau_seconds={tau_seconds:.6g}; "
            f"expected {expected_tau}."
        )

    simplex_config = config["simplex"]
    horizon_seconds = tuple(simplex_config["horizon_seconds"])
    theiler_seconds = float(simplex_config["theiler_seconds"])
    horizon_samples = tuple(
        max(1, int(round(horizon * sampling_rate)))
        for horizon in horizon_seconds
    )
    if len(set(horizon_samples)) != len(horizon_samples):
        raise ValueError(
            "sampling_rate maps distinct Simplex horizons to duplicate "
            "sample counts."
        )
    theiler_samples = max(0, int(round(theiler_seconds * sampling_rate)))

    return {
        "sampling_rate": sampling_rate,
        "tau_seconds": tau_seconds,
        "tau_samples": tau_samples,
        "horizon_seconds": horizon_seconds,
        "horizon_samples": horizon_samples,
        "n_horizons": len(horizon_samples),
        "hmax_seconds": horizon_seconds[-1],
        "hmax_samples": horizon_samples[-1],
        "theiler_seconds": theiler_seconds,
        "theiler_samples": theiler_samples,
    }


def compute_metrics(
    signal: Any,
    representation: str,
    sampling_rate: float,
    tau_samples: int,
    config: Mapping[str, Any] = SURROGATE_CONFIG,
) -> dict[str, float]:
    """Compute curve-mean Simplex metrics and frozen RQA metrics."""
    checked = _validate_config(config)
    values = _validate_signal(signal)
    representation = _representation_name(representation)
    parameters = _resolve_metric_parameters(
        representation,
        sampling_rate,
        tau_samples,
        checked,
    )

    m = checked["m"]
    tau = int(parameters["tau_samples"])
    simplex_config = checked["simplex"]
    horizons = parameters["horizon_samples"]
    theiler = int(parameters["theiler_samples"])
    scale = _nrmse_scale(
        values,
        simplex_config["nrmse_scale"],
        representation,
    )

    try:
        curve = prediction_curve(
            signal=values,
            tau=tau,
            m=m,
            horizons=horizons,
            theiler_window=theiler,
            scale_function=lambda _: scale,
        )
    except Exception as exc:
        raise RuntimeError(
            f"Simplex metric computation failed: {exc}"
        ) from exc

    if len(curve) != int(parameters["n_horizons"]):
        raise RuntimeError("Simplex core returned an incomplete curve.")
    cc_curve = np.asarray([item.cc for item in curve], dtype=float)
    nrmse_curve = np.asarray([item.nrmse for item in curve], dtype=float)
    if not np.all(np.isfinite(cc_curve)):
        raise ValueError("Simplex curve contains undefined CC values.")
    if not np.all(np.isfinite(nrmse_curve)):
        raise ValueError("Simplex curve contains undefined NRMSE values.")

    rqa_config = checked["rqa"]
    try:
        rqa_summary = run_rqa(
            signal=values,
            m=m,
            tau=tau,
            l_min=int(rqa_config["l_min"]),
            v_min=int(rqa_config["v_min"]),
            target_rr=float(rqa_config["target_rr"]),
        )
    except Exception as exc:
        raise RuntimeError(f"RQA metric computation failed: {exc}") from exc

    metrics = {
        "CC": float(np.mean(cc_curve)),
        "NRMSE": float(np.mean(nrmse_curve)),
        "DET": float(rqa_summary.det),
        "Lmean": float(rqa_summary.l_mean),
        "ENTR": float(rqa_summary.entr),
        "Lmax": float(rqa_summary.l_max),
        "LAM": float(rqa_summary.lam),
        "TT": float(rqa_summary.tt),
        "Vmax": float(rqa_summary.v_max),
    }

    invalid = [name for name, value in metrics.items() if not np.isfinite(value)]
    if invalid:
        raise ValueError(f"undefined metrics: {invalid}.")
    return metrics


def surrogate_rank_test(
    original_value: float,
    surrogate_values: Any,
    alpha: float = 0.05,
    alternative: str = "two-sided",
) -> dict[str, Any]:
    """Run a finite-sample surrogate rank test with inclusive ties."""
    original = float(original_value)
    surrogates = np.asarray(surrogate_values, dtype=float)

    if not np.isfinite(original):
        raise ValueError("original_value must be finite.")
    if surrogates.ndim != 1 or surrogates.size == 0:
        raise ValueError("surrogate_values must be a non-empty 1D array.")
    if not np.all(np.isfinite(surrogates)):
        raise ValueError("surrogate_values must contain only finite values.")
    if not np.isfinite(alpha) or not 0.0 < alpha < 1.0:
        raise ValueError("alpha must be in (0, 1).")

    alternative = str(alternative).strip().casefold().replace("_", "-")
    if alternative not in {"two-sided", "greater", "less"}:
        raise ValueError(
            "alternative must be 'two-sided', 'greater', or 'less'."
        )

    n_lower = int(np.count_nonzero(surrogates <= original))
    n_upper = int(np.count_nonzero(surrogates >= original))
    n_equal = int(np.count_nonzero(surrogates == original))
    n_less = int(np.count_nonzero(surrogates < original))
    denominator = surrogates.size + 1

    p_upper = (n_upper + 1) / denominator
    p_lower = (n_lower + 1) / denominator

    if alternative == "two-sided":
        p_value = min(1.0, 2.0 * min(p_upper, p_lower))
    elif alternative == "greater":
        p_value = p_upper
    else:
        p_value = p_lower

    reject = bool(p_value <= alpha)
    direction = "none"
    if reject and alternative == "greater":
        direction = "higher"
    elif reject and alternative == "less":
        direction = "lower"
    elif reject and p_upper < p_lower:
        direction = "higher"
    elif reject and p_lower < p_upper:
        direction = "lower"

    # Midrank gives a deterministic rank when surrogate values tie.
    rank = 1.0 + n_less + 0.5 * n_equal

    return {
        "rank": float(rank),
        "n_lower": n_lower,
        "n_upper": n_upper,
        "p_value": float(p_value),
        "reject": reject,
        "direction": direction,
    }


def _identity_value(value: Any) -> Any:
    """Normalize metadata for deterministic hashing and matching."""
    value = _python_scalar(value)
    if isinstance(value, float):
        if not np.isfinite(value):
            raise ValueError("metadata values must be finite.")
        return int(value) if value.is_integer() else format(value, ".17g")
    if isinstance(value, int):
        return value
    return str(value).strip().casefold()


def _session_key(value: Any) -> Any:
    """Normalize common numeric session labels."""
    normalized = _identity_value(value)
    if isinstance(normalized, int):
        return normalized

    match = re.fullmatch(r"(?:sample|session)[ _-]*(\d+)", normalized)
    if match:
        return int(match.group(1))
    if normalized.isdigit():
        return int(normalized)
    return normalized


def _derive_window_seed(
    master_seed: int,
    metadata: Mapping[str, Any],
) -> int:
    """Derive a stable seed from the complete window identity."""
    master_seed = _nonnegative_integer(master_seed, "master_seed")
    missing = [name for name in METADATA_COLUMNS if name not in metadata]
    if missing:
        raise ValueError(f"window metadata is missing keys: {missing}.")

    identity = {
        "master_seed": master_seed,
        "session": _session_key(metadata["session"]),
        "representation": _representation_name(metadata["representation"]),
        "state": _identity_value(metadata["state"]),
        "window_size": _identity_value(metadata["window_size"]),
        "window_id": _identity_value(metadata["window_id"]),
    }
    payload = json.dumps(identity, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(payload.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], byteorder="little", signed=False)


def _derive_surrogate_seeds(window_seed: int, count: int) -> list[int]:
    """Derive stable surrogate seeds independent of execution order."""
    window_seed = _nonnegative_integer(window_seed, "window_seed")
    count = _positive_integer(count, "count")
    seeds = []

    for surrogate_id in range(count):
        payload = f"{window_seed}:{surrogate_id}".encode("ascii")
        digest = hashlib.sha256(payload).digest()
        seeds.append(
            int.from_bytes(digest[:8], byteorder="little", signed=False)
        )
    return seeds


def _window_context(
    metadata: Mapping[str, Any],
    surrogate_id: int | None = None,
) -> str:
    """Format a compact window error context."""
    parts = [f"{name}={metadata.get(name)!r}" for name in METADATA_COLUMNS]
    for name in ("sampling_rate", "tau_samples"):
        if name in metadata:
            parts.append(f"{name}={metadata[name]!r}")
    if surrogate_id is not None:
        parts.append(f"surrogate_id={surrogate_id}")
    return ", ".join(parts)


def run_window_test(
    signal: Any,
    rho_star: float,
    representation: str,
    window_metadata: Mapping[str, Any],
    master_seed: int,
    config: Mapping[str, Any] = SURROGATE_CONFIG,
    *,
    window_seed: int | None = None,
) -> dict[str, Any]:
    """Test one window against sequentially generated PPS surrogates."""
    checked = _validate_config(config)
    values = _validate_signal(signal)
    representation = _representation_name(representation)
    rho_star = float(rho_star)
    if not np.isfinite(rho_star) or rho_star <= 0.0:
        raise ValueError("rho_star must be positive and finite.")

    metadata = {
        name: _python_scalar(window_metadata[name])
        for name in METADATA_COLUMNS
    }
    metadata["representation"] = representation
    parameters = _resolve_metric_parameters(
        representation,
        window_metadata["sampling_rate"],
        window_metadata["tau_samples"],
        checked,
    )
    metadata.update(parameters)
    if window_seed is None:
        window_seed = _derive_window_seed(master_seed, metadata)
    else:
        window_seed = _nonnegative_integer(window_seed, "window_seed")

    try:
        original_metrics = compute_metrics(
            values,
            representation,
            sampling_rate=float(parameters["sampling_rate"]),
            tau_samples=int(parameters["tau_samples"]),
            config=checked,
        )
    except Exception as exc:
        context = _window_context(metadata)
        raise WindowTestError(
            f"Original metrics failed for {context}: {exc}"
        ) from exc

    count = checked["M"]
    tau = int(parameters["tau_samples"])
    seeds = _derive_surrogate_seeds(window_seed, count)
    surrogate_metrics = {
        metric: np.empty(count, dtype=float)
        for metric in METRIC_NAMES
    }

    for surrogate_id, seed in enumerate(seeds):
        try:
            rng = np.random.default_rng(seed)
            surrogate = generate_pps_signal(
                signal=values,
                tau=tau,
                m=checked["m"],
                rho=rho_star,
                rng=rng,
                return_indices=False,
            )
        except Exception as exc:
            context = _window_context(metadata, surrogate_id)
            raise WindowTestError(
                f"PPS generation failed for {context}: {exc}"
            ) from exc

        try:
            metrics = compute_metrics(
                surrogate,
                representation,
                sampling_rate=float(parameters["sampling_rate"]),
                tau_samples=int(parameters["tau_samples"]),
                config=checked,
            )
        except Exception as exc:
            context = _window_context(metadata, surrogate_id)
            raise WindowTestError(
                f"Surrogate metrics failed for {context}: {exc}"
            ) from exc
        finally:
            del surrogate

        for metric in METRIC_NAMES:
            surrogate_metrics[metric][surrogate_id] = metrics[metric]

    tests = {
        metric: surrogate_rank_test(
            original_metrics[metric],
            surrogate_metrics[metric],
            alpha=checked["alpha"],
            alternative=checked["alternative"],
        )
        for metric in METRIC_NAMES
    }

    metadata.update(
        {
            "rho_star": rho_star,
            "m": checked["m"],
            "M": count,
            "master_seed": int(master_seed),
            "window_seed": window_seed,
        }
    )
    return {
        "metadata": metadata,
        "original": original_metrics,
        "surrogates": surrogate_metrics,
        "tests": tests,
    }


def _window_worker(
    task: Mapping[str, Any],
    config: Mapping[str, Any],
    fail_fast: bool,
    inner_threads: int,
) -> dict[str, Any]:
    """Run one window while limiting native numerical threads."""
    try:
        with threadpool_limits(limits=inner_threads):
            result = run_window_test(
                signal=task["signal"],
                rho_star=task["rho_star"],
                representation=task["representation"],
                window_metadata=task["metadata"],
                master_seed=task["master_seed"],
                config=config,
                window_seed=task["window_seed"],
            )
        return {
            "task_index": task["task_index"],
            "result": result,
            "error": None,
        }
    except Exception as exc:
        context = _window_context(task["metadata"])
        message = f"Window test failed for {context}: {exc}"
        if fail_fast:
            raise WindowTestError(message) from exc
        return {
            "task_index": task["task_index"],
            "result": None,
            "error": message,
            "metadata": dict(task["metadata"]),
        }


def _require_columns(
    frame: pd.DataFrame,
    required: set[str],
    name: str,
) -> None:
    """Require a dataframe schema before computation."""
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"{name} is missing columns: {missing}.")


def _boundary_value(value: Any) -> bool:
    """Parse a strict boundary flag value."""
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if isinstance(value, (int, np.integer)) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().casefold()
        if normalized in {"true", "1"}:
            return True
        if normalized in {"false", "0"}:
            return False
    raise ValueError(f"invalid boundary_flag value: {value!r}.")


def _add_matching_keys(frame: pd.DataFrame) -> pd.DataFrame:
    """Add normalized keys without changing public metadata."""
    keyed = frame.copy()
    keyed["_representation"] = keyed["representation"].map(
        _representation_name
    )
    keyed["_state"] = keyed["state"].map(_identity_value)
    keyed["_window_size"] = keyed["window_size"].map(_identity_value)
    keyed["_window_id"] = keyed["window_id"].map(_identity_value)
    return keyed


def _validate_session_inputs(
    windows_df: pd.DataFrame,
    rho_lookup_df: pd.DataFrame,
    session_id: Any,
    config: Mapping[str, Any],
) -> pd.DataFrame:
    """Validate a complete session and attach its frozen rho values."""
    if not isinstance(windows_df, pd.DataFrame):
        raise TypeError("windows_df must be a pandas DataFrame.")
    if not isinstance(rho_lookup_df, pd.DataFrame):
        raise TypeError("rho_lookup_df must be a pandas DataFrame.")

    _require_columns(
        windows_df,
        set(METADATA_COLUMNS).union({"signal"}),
        "windows_df",
    )
    _require_columns(
        rho_lookup_df,
        set(METADATA_COLUMNS).union(
            {
                "rho_star",
                "sampling_rate",
                "tau_samples",
                "boundary_flag",
            }
        ),
        "rho_lookup_df",
    )

    target_session = _session_key(session_id)
    windows = windows_df.loc[
        windows_df["session"].map(_session_key).eq(target_session)
    ].copy()
    lookup = rho_lookup_df.loc[
        rho_lookup_df["session"].map(_session_key).eq(target_session)
    ].copy()

    if windows.empty:
        raise ValueError(f"No windows found for session {session_id!r}.")
    if lookup.empty:
        raise ValueError(f"No rho lookup found for session {session_id!r}.")

    for name, frame in (("windows_df", windows), ("rho_lookup_df", lookup)):
        missing_metadata = frame[list(METADATA_COLUMNS)].isna().any(axis=1)
        if missing_metadata.any():
            raise ValueError(f"{name} contains missing metadata values.")

    windows = _add_matching_keys(windows)
    lookup = _add_matching_keys(lookup)
    key_columns = [
        "_representation",
        "_state",
        "_window_size",
        "_window_id",
    ]

    if windows.duplicated(key_columns, keep=False).any():
        raise ValueError("windows_df contains duplicated window identities.")
    if lookup.duplicated(key_columns, keep=False).any():
        raise ValueError("rho_lookup_df contains duplicated lookup identities.")

    try:
        lookup["_boundary"] = lookup["boundary_flag"].map(_boundary_value)
    except ValueError as exc:
        raise ValueError(f"rho_lookup_df contains {exc}") from exc
    if lookup["_boundary"].any():
        count = int(lookup["_boundary"].sum())
        raise ValueError(
            f"rho_lookup_df contains {count} unresolved boundary cases."
        )

    rho_values = pd.to_numeric(lookup["rho_star"], errors="coerce")
    if not np.all(np.isfinite(rho_values)) or np.any(rho_values <= 0.0):
        raise ValueError("rho_lookup_df.rho_star must be positive and finite.")
    lookup["rho_star"] = rho_values.astype(float)

    sampling_rates = pd.to_numeric(
        lookup["sampling_rate"],
        errors="coerce",
    )
    if not np.all(np.isfinite(sampling_rates)) or np.any(
        sampling_rates <= 0.0
    ):
        raise ValueError(
            "rho_lookup_df.sampling_rate must be positive and finite."
        )
    lookup["_lookup_sampling_rate"] = sampling_rates.astype(float)

    try:
        lookup["_lookup_tau_samples"] = lookup["tau_samples"].map(
            lambda value: _sample_integer(value, "tau_samples")
        )
    except ValueError as exc:
        raise ValueError(f"rho_lookup_df contains {exc}") from exc

    parameter_errors = []
    for row in lookup.to_dict(orient="records"):
        try:
            _resolve_metric_parameters(
                row["_representation"],
                row["_lookup_sampling_rate"],
                row["_lookup_tau_samples"],
                config,
            )
        except Exception as exc:
            metadata = {
                "session": session_id,
                "representation": row["_representation"],
                "state": row["state"],
                "window_size": row["window_size"],
                "window_id": row["window_id"],
                "sampling_rate": row["_lookup_sampling_rate"],
                "tau_samples": row["_lookup_tau_samples"],
            }
            parameter_errors.append(f"{_window_context(metadata)}: {exc}")
    if parameter_errors:
        details = "\n".join(parameter_errors[:10])
        suffix = "" if len(parameter_errors) <= 10 else "\n..."
        raise ValueError(f"Invalid metric parameters:\n{details}{suffix}")

    attached = windows.merge(
        lookup[
            key_columns
            + [
                "rho_star",
                "_lookup_sampling_rate",
                "_lookup_tau_samples",
            ]
        ],
        on=key_columns,
        how="left",
        validate="one_to_one",
    )
    if attached["rho_star"].isna().any():
        missing = int(attached["rho_star"].isna().sum())
        raise ValueError(f"Missing rho_star for {missing} eligible windows.")

    if "sampling_rate" in windows.columns:
        window_rates = pd.to_numeric(
            attached["sampling_rate"],
            errors="coerce",
        )
        matched_rates = np.isclose(
            window_rates,
            attached["_lookup_sampling_rate"],
            rtol=1e-6,
            atol=1e-9,
        )
        if not np.all(matched_rates):
            raise ValueError(
                "windows_df.sampling_rate conflicts with rho_lookup_df."
            )

    if "tau_samples" in windows.columns:
        try:
            window_tau = attached["tau_samples"].map(
                lambda value: _sample_integer(value, "tau_samples")
            )
        except ValueError as exc:
            raise ValueError(f"windows_df contains {exc}") from exc
        if not np.array_equal(
            window_tau.to_numpy(),
            attached["_lookup_tau_samples"].to_numpy(),
        ):
            raise ValueError("windows_df.tau_samples conflicts with rho_lookup_df.")

    attached["sampling_rate"] = attached["_lookup_sampling_rate"]
    attached["tau_samples"] = attached["_lookup_tau_samples"]

    signal_errors = []
    for row in attached.to_dict(orient="records"):
        metadata = {
            "session": session_id,
            "representation": row["_representation"],
            "state": row["state"],
            "window_size": row["window_size"],
            "window_id": row["window_id"],
            "sampling_rate": row["sampling_rate"],
            "tau_samples": row["tau_samples"],
        }
        try:
            _validate_signal(row["signal"])
        except Exception as exc:
            signal_errors.append(f"{_window_context(metadata)}: {exc}")
    if signal_errors:
        details = "\n".join(signal_errors[:10])
        suffix = "" if len(signal_errors) <= 10 else "\n..."
        raise ValueError(f"Invalid window signals:\n{details}{suffix}")

    attached["session"] = _python_scalar(session_id)
    attached["representation"] = attached["_representation"]
    return attached.sort_values(
        ["representation", "state", "window_size", "window_id"],
        kind="stable",
    ).reset_index(drop=True)


def _window_result_columns() -> list[str]:
    """Return the stable window-level output schema."""
    columns = [
        *METADATA_COLUMNS,
        "rho_star",
        "sampling_rate",
        "m",
        "tau_seconds",
        "tau_samples",
        "n_horizons",
        "hmax_seconds",
        "hmax_samples",
        "theiler_seconds",
        "theiler_samples",
        "M",
        "master_seed",
    ]
    suffixes = (
        "original",
        "surrogate_mean",
        "surrogate_sd",
        "surrogate_median",
        "rank",
        "p",
        "reject",
        "direction",
    )
    for metric in METRIC_NAMES:
        columns.extend(f"{metric}_{suffix}" for suffix in suffixes)
    return columns


def _surrogate_result_columns() -> list[str]:
    """Return the stable surrogate-level output schema."""
    return [*METADATA_COLUMNS, "surrogate_id", "seed", *METRIC_NAMES]


def _flatten_results(
    results: list[dict[str, Any]],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Convert compact worker results into the two public dataframes."""
    window_rows = []
    surrogate_rows = []

    for result in results:
        metadata = result["metadata"]
        base = {name: metadata[name] for name in METADATA_COLUMNS}
        window_row = {
            **base,
            "rho_star": metadata["rho_star"],
            "sampling_rate": metadata["sampling_rate"],
            "m": metadata["m"],
            "tau_seconds": metadata["tau_seconds"],
            "tau_samples": metadata["tau_samples"],
            "n_horizons": metadata["n_horizons"],
            "hmax_seconds": metadata["hmax_seconds"],
            "hmax_samples": metadata["hmax_samples"],
            "theiler_seconds": metadata["theiler_seconds"],
            "theiler_samples": metadata["theiler_samples"],
            "M": metadata["M"],
            "master_seed": metadata["master_seed"],
        }

        for metric in METRIC_NAMES:
            values = result["surrogates"][metric]
            test = result["tests"][metric]
            ddof = 1 if values.size > 1 else 0
            window_row.update(
                {
                    f"{metric}_original": result["original"][metric],
                    f"{metric}_surrogate_mean": float(np.mean(values)),
                    f"{metric}_surrogate_sd": float(np.std(values, ddof=ddof)),
                    f"{metric}_surrogate_median": float(np.median(values)),
                    f"{metric}_rank": test["rank"],
                    f"{metric}_p": test["p_value"],
                    f"{metric}_reject": test["reject"],
                    f"{metric}_direction": test["direction"],
                }
            )
        window_rows.append(window_row)

        seeds = _derive_surrogate_seeds(
            metadata["window_seed"],
            metadata["M"],
        )
        for surrogate_id, seed in enumerate(seeds):
            row = {
                **base,
                "surrogate_id": surrogate_id,
                "seed": seed,
            }
            row.update(
                {
                    metric: result["surrogates"][metric][surrogate_id]
                    for metric in METRIC_NAMES
                }
            )
            surrogate_rows.append(row)

    window_frame = pd.DataFrame(
        window_rows,
        columns=_window_result_columns(),
    )
    surrogate_frame = pd.DataFrame(
        surrogate_rows,
        columns=_surrogate_result_columns(),
    )
    return window_frame, surrogate_frame


def _progress_message(completed: int, total: int, started: float) -> str:
    """Format elapsed and estimated remaining time."""
    elapsed = time.perf_counter() - started
    average = elapsed / completed
    remaining = max(total - completed, 0) * average
    return (
        f"Completed: {completed} / {total} | "
        f"Elapsed: {elapsed:.1f} s | "
        f"Average/window: {average:.1f} s | "
        f"Estimated remaining: {remaining:.1f} s"
    )


def _validate_compute_config(
    n_jobs: int,
    compute_config: Mapping[str, Any],
) -> dict[str, Any]:
    """Validate process-level computation settings."""
    if not isinstance(compute_config, Mapping):
        raise TypeError("compute_config must be a mapping.")
    checked = copy.deepcopy(dict(compute_config))
    n_jobs = _positive_integer(n_jobs, "n_jobs")
    checked["n_jobs"] = n_jobs
    checked["inner_threads"] = _positive_integer(
        checked.get("inner_threads", 1),
        "inner_threads",
    )
    checked["verbose"] = _nonnegative_integer(
        checked.get("verbose", 0),
        "verbose",
    )
    backend = str(checked.get("backend", "loky")).strip()
    if backend != "loky":
        raise ValueError("compute_config.backend must be 'loky'.")
    checked["backend"] = backend
    return checked


def run_session_test(
    windows_df: pd.DataFrame,
    rho_lookup_df: pd.DataFrame,
    session_id: Any,
    master_seed: int = 2026,
    n_jobs: int = 6,
    config: Mapping[str, Any] = SURROGATE_CONFIG,
    *,
    fail_fast: bool = True,
    compute_config: Mapping[str, Any] = COMPUTE_CONFIG,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run deterministic PPS tests for every window in one session."""
    checked_config = _validate_config(config)
    checked_compute = _validate_compute_config(n_jobs, compute_config)
    master_seed = _nonnegative_integer(master_seed, "master_seed")
    if not isinstance(fail_fast, (bool, np.bool_)):
        raise TypeError("fail_fast must be boolean.")

    attached = _validate_session_inputs(
        windows_df,
        rho_lookup_df,
        session_id,
        checked_config,
    )

    tasks = []
    for task_index, row in enumerate(attached.to_dict(orient="records")):
        metadata = {
            "session": _python_scalar(row["session"]),
            "representation": row["_representation"],
            "state": _python_scalar(row["state"]),
            "window_size": _python_scalar(row["window_size"]),
            "window_id": _python_scalar(row["window_id"]),
            "sampling_rate": float(row["sampling_rate"]),
            "tau_samples": int(row["tau_samples"]),
        }
        tasks.append(
            {
                "task_index": task_index,
                "signal": np.asarray(row["signal"], dtype=float),
                "rho_star": float(row["rho_star"]),
                "representation": row["_representation"],
                "metadata": metadata,
                "master_seed": master_seed,
                "window_seed": _derive_window_seed(master_seed, metadata),
            }
        )

    total = len(tasks)
    verbose = checked_compute["verbose"]
    if verbose:
        print(
            f"Session {session_id}\n"
            f"Windows: {total}\n"
            f"Workers: {checked_compute['n_jobs']}\n"
            f"M: {checked_config['M']}"
        )

    started = time.perf_counter()
    outputs = []
    report_step = max(1, math.ceil(total / 20))

    with parallel_config(
        backend=checked_compute["backend"],
        inner_max_num_threads=checked_compute["inner_threads"],
    ):
        generated = Parallel(
            n_jobs=checked_compute["n_jobs"],
            batch_size=1,
            return_as="generator_unordered",
        )(
            delayed(_window_worker)(
                task,
                checked_config,
                bool(fail_fast),
                checked_compute["inner_threads"],
            )
            for task in tasks
        )

        for completed, output in enumerate(generated, start=1):
            outputs.append(output)
            if verbose and (
                completed == 1
                or completed == total
                or completed % report_step == 0
            ):
                print(_progress_message(completed, total, started))

    outputs.sort(key=lambda item: item["task_index"])
    failures = [output for output in outputs if output["error"] is not None]
    successful = [
        output["result"]
        for output in outputs
        if output["result"] is not None
    ]
    window_results, surrogate_results = _flatten_results(successful)

    if failures:
        failure_records = [
            {
                **failure["metadata"],
                "error": failure["error"],
            }
            for failure in failures
        ]
        window_results.attrs["failures"] = failure_records
        surrogate_results.attrs["failures"] = failure_records
        warnings.warn(
            f"{len(failures)} window tests failed; details are stored in "
            "DataFrame.attrs['failures'].",
            RuntimeWarning,
            stacklevel=2,
        )

    return window_results, surrogate_results


__all__ = [
    "COMPUTE_CONFIG",
    "METRIC_NAMES",
    "SURROGATE_CONFIG",
    "WindowTestError",
    "compute_metrics",
    "run_session_test",
    "run_window_test",
    "surrogate_rank_test",
]
