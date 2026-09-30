"""Recompute and freeze the P0 60 s Simplex window-first primary estimator.

This is a standalone, read-only rerun of the frozen Simplex estimator except for
its versioned outputs. It never edits legacy outputs or runs a pairing experiment.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import numpy as np
import pandas as pd
import scipy
from joblib import Parallel, delayed
from scipy.spatial import cKDTree

PHASE1 = Path(__file__).resolve().parents[1]
PROJECT = PHASE1.parent
sys.path.insert(0, str(PHASE1 / "src"))
from dataloader.loader import get_data
from prediction.simplex_projection import SimplexResult, prediction_metrics

OUT = PHASE1 / "sensitivy_data" / "primary_simplex_windowfirst_v1"
HORIZONS = np.array([
    0.04, 0.08, 0.12, 0.16, 0.20, 0.28, 0.40, 0.60, 0.80,
    1.00, 1.20, 1.60, 2.00, 2.40, 2.80, 3.20, 3.60, 4.00,
])
EXPECTED_IDS = (1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25)
M, TAU_S, THEILER_S, WINDOW_S = 8, 0.16, 1.0, 60
BOOTSTRAPS, BOOTSTRAP_SEED, ZERO_TOL = 20_000, 20260829, 1e-12
METRICS = ("Mean_CC", "Mean_NRMSE", "DET", "Lmean", "LAM", "TT", "LLE")
FILE_NAMES = {
    "horizons": "primary_simplex_window_horizons_60s_processed_P0_v1.csv",
    "windows": "primary_simplex_window_means_60s_processed_P0_v1.csv",
    "paired": "primary_simplex_session_paired_60s_processed_P0_v1.csv",
    "statistics": "primary_simplex_statistics_60s_processed_P0_v1.csv",
    "bh": "primary_bh_fdr_7metrics_windowfirst_P0_v1.csv",
    "manifest": "manifest.json",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def standardize_signal(signal):
    """Copied from notebook/simplex_projection.ipynb cell 4."""
    signal = np.asarray(signal, dtype=float)
    scale = np.std(signal)
    if signal.ndim != 1 or not np.all(np.isfinite(signal)):
        raise ValueError("Signal must be finite and one-dimensional.")
    if scale <= 0:
        raise ValueError("Signal must have non-zero variance.")
    return (signal - np.mean(signal)) / scale


def build_embedding(signal, tau, m, horizon):
    """Copied from notebook/simplex_projection.ipynb cell 4."""
    start = (m - 1) * tau
    times = np.arange(start, len(signal) - horizon)
    offsets = np.arange(m) * tau
    states = signal[times[:, None] - offsets[None, :]]
    targets = signal[times + horizon]
    return states, targets, times


def simplex_all_theiler(signal, tau, m, horizon, theiler_values):
    """Frozen batched Simplex from notebook cell 4, here with only W=1.0 s."""
    states, targets, times = build_embedding(signal, tau, m, horizon)
    n_neighbors = m + 1
    max_theiler = int(np.max(theiler_values))
    query_k = min(len(times), 2 * max_theiler + n_neighbors + 1)
    if query_k < n_neighbors + 1:
        raise ValueError("Not enough embedded states for prediction.")
    distances, indices = cKDTree(states).query(states, k=query_k, workers=1)
    time_distance = np.abs(times[indices] - times[:, None])
    results = {}
    for theiler in theiler_values:
        admissible = time_distance > int(theiler)
        rank = np.cumsum(admissible, axis=1)
        selected = admissible & (rank <= n_neighbors)
        counts = np.sum(selected, axis=1)
        valid = counts == n_neighbors
        predictions = np.full(len(states), np.nan)
        if np.any(valid):
            selected_valid = selected[valid]
            valid_distances = distances[valid][selected_valid].reshape(-1, n_neighbors)
            valid_indices = indices[valid][selected_valid].reshape(-1, n_neighbors)
            zero_mask = np.isclose(valid_distances, 0.0, rtol=0.0, atol=np.finfo(float).eps)
            has_zero = np.any(zero_mask, axis=1)
            weights = np.zeros_like(valid_distances)
            if np.any(has_zero):
                weights[has_zero] = zero_mask[has_zero] / np.sum(zero_mask[has_zero], axis=1, keepdims=True)
            nonzero = ~has_zero
            if np.any(nonzero):
                reference = valid_distances[nonzero, :1]
                raw_weights = np.exp(-valid_distances[nonzero] / reference)
                weights[nonzero] = raw_weights / np.sum(raw_weights, axis=1, keepdims=True)
            neighbor_targets = targets[valid_indices]
            predictions[valid] = np.sum(weights * neighbor_targets, axis=1)
        results[int(theiler)] = SimplexResult(
            horizon=horizon, times=times, y_true=targets,
            y_pred=predictions, valid=np.isfinite(predictions),
        )
    return results


def evaluate_window(task):
    session_id, state, window_id, fs, signal = task
    signal = standardize_signal(signal)
    tau_samples = int(round(TAU_S * fs))
    theiler_samples = int(round(THEILER_S * fs))
    rows = []
    for horizon_s in HORIZONS:
        horizon_samples = int(np.rint(horizon_s * fs))
        result = simplex_all_theiler(signal, tau_samples, M, horizon_samples, np.array([theiler_samples]))[theiler_samples]
        metric = prediction_metrics(result, nrmse_scale=1.0)
        require(np.isfinite(metric.cc) and np.isfinite(metric.nrmse), f"Nonfinite Simplex metric: {task[:3]}, {horizon_s}")
        rows.append((session_id, state, window_id, WINDOW_S, fs, M, TAU_S, tau_samples,
                     THEILER_S, theiler_samples, horizon_s, horizon_samples,
                     metric.cc, metric.nrmse, metric.n_valid,
                     metric.n_valid / len(result.y_true), True))
    return rows


def exact_wilcoxon(values):
    """Copied from main/prediction_nonlinear.ipynb cell 8."""
    values = np.asarray(values, dtype=float)
    nonzero = values[~np.isclose(values, 0.0, atol=ZERO_TOL, rtol=0.0)]
    require(len(nonzero) > 0, "Wilcoxon requires a nonzero difference")
    ranks = pd.Series(np.abs(nonzero)).rank(method="average").to_numpy()
    scaled = np.rint(2.0 * ranks).astype(int)
    total = int(scaled.sum())
    positive = int(scaled[nonzero > 0].sum())
    statistic = min(positive, total - positive)
    counts = np.array([1], dtype=np.int64)
    for rank in scaled:
        updated = np.zeros(len(counts) + rank, dtype=np.int64)
        updated[:len(counts)] += counts
        updated[rank:] += counts
        counts = updated
    possible = np.arange(len(counts))
    extreme = counts[np.minimum(possible, total - possible) <= statistic].sum()
    return statistic / 2.0, min(float(extreme / (2 ** len(nonzero))), 1.0)


def rank_biserial(values):
    nonzero = np.asarray(values, dtype=float)
    nonzero = nonzero[~np.isclose(nonzero, 0.0, atol=ZERO_TOL, rtol=0.0)]
    ranks = pd.Series(np.abs(nonzero)).rank(method="average").to_numpy()
    return float((ranks[nonzero > 0].sum() - ranks[nonzero < 0].sum()) / ranks.sum()) if len(nonzero) else 0.0


def bh_adjust(p_values):
    p_values = np.asarray(p_values, dtype=float)
    order = np.argsort(p_values, kind="stable")
    adjusted_sorted = p_values[order] * len(p_values) / np.arange(1, len(p_values) + 1)
    adjusted_sorted = np.minimum.accumulate(adjusted_sorted[::-1])[::-1]
    adjusted = np.empty_like(adjusted_sorted)
    adjusted[order] = np.clip(adjusted_sorted, 0.0, 1.0)
    return adjusted


def main():
    require(not OUT.exists() or not any(OUT.iterdir()), f"Refusing to overwrite existing freeze: {OUT}")
    source_dir = PHASE1 / "segmentated_data" / "dhdata"
    paths = sorted(source_dir.glob("sample_*.npz"), key=lambda p: int(p.stem.split("_")[-1]))
    ids = tuple(int(path.stem.split("_")[-1]) for path in paths)
    require(ids == EXPECTED_IDS, f"Unexpected primary sessions: {ids}")
    index_path = source_dir / "segments_index.csv"
    index = pd.read_csv(index_path)
    index = index.loc[index.window_size_s.eq(WINDOW_S) & index.stationarity_pass_processed.eq(True)].copy()
    require(len(index) == 901, "Expected 901 P0 processed-stationarity windows")
    index["session_id"] = index.session.str.extract(r"(\d+)")[0].astype(int)
    index["state"] = index.label.map({0: "Awake", 1: "Drowsy"})
    require(index.state.notna().all() and not index.duplicated(["session_id", "window_id"]).any(), "Invalid P0 index")
    tasks = []
    for path in paths:
        session_id = int(path.stem.split("_")[-1])
        awake, drowsy = get_data(path.stem, data_dir=source_dir, window_sizes=(WINDOW_S,), stationarity="processed")
        for state, batch in (("Awake", awake[WINDOW_S]), ("Drowsy", drowsy[WINDOW_S])):
            for k, signal in enumerate(batch["processed"]):
                tasks.append((session_id, state, int(batch["window_id"][k]), float(batch["fs"]), np.asarray(signal, dtype=float)))
    keys = {(s, state, w) for s, state, w, _, _ in tasks}
    index_keys = set(zip(index.session_id, index.state, index.window_id))
    require(len(tasks) == len(keys) == 901 and keys == index_keys, "Loader does not match P0 index")
    require(sum(state == "Awake" for _, state, *_ in tasks) == 596, "Awake coverage changed")
    require(sum(state == "Drowsy" for _, state, *_ in tasks) == 305, "Drowsy coverage changed")
    print(f"Computing {len(tasks)} frozen P0 windows × {len(HORIZONS)} horizons", flush=True)
    batches = Parallel(n_jobs=min(6, os.cpu_count() or 1), verbose=10, batch_size=1)(delayed(evaluate_window)(task) for task in tasks)
    columns = ["session_id", "state", "window_id", "window_size_s", "fs", "m", "tau_s", "tau_samples",
               "theiler_s", "theiler_samples", "horizon_s", "horizon_samples", "cc", "nrmse", "n_valid", "valid_fraction", "qc_pass"]
    horizon = pd.DataFrame([row for batch in batches for row in batch], columns=columns)
    require(len(horizon) == 901 * 18 and not horizon.duplicated(["session_id", "state", "window_id", "horizon_s"]).any(), "Incomplete or duplicate horizon results")
    require(horizon.groupby(["session_id", "state", "window_id"]).horizon_s.nunique().eq(18).all(), "Missing horizons")
    require(np.isfinite(horizon[["cc", "nrmse"]]).all().all(), "Nonfinite horizon metrics")
    require(horizon.valid_fraction.eq(1.0).all(), "Prediction support differs from frozen complete-support source")
    # Reproduce every saved horizon-wise session-state median to validate the estimator and data branch.
    summary = pd.read_csv(PHASE1 / "results/simplex_projection/summary/processed_simplex_summary.csv")
    summary = summary.loc[summary.representation.eq("Processed") & summary.window_size_s.eq(WINDOW_S)].copy()
    summary["session_id"] = summary.session.str.extract(r"(\d+)")[0].astype(int)
    regenerated = horizon.groupby(["session_id", "state", "horizon_s"], as_index=False).agg(
        median_cc=("cc", "median"), median_nrmse=("nrmse", "median"), n_windows=("window_id", "nunique"))
    crosscheck = regenerated.merge(summary, left_on=["session_id", "state", "horizon_s"],
                                   right_on=["session_id", "state", "horizon_seconds"], how="outer", validate="one_to_one", indicator=True)
    require(len(crosscheck) == 720 and crosscheck._merge.eq("both").all(), "Saved horizon summary key mismatch")
    cc_error = float(np.max(np.abs(crosscheck.median_cc_x - crosscheck.median_cc_y)))
    nrmse_error = float(np.max(np.abs(crosscheck.median_nrmse_x - crosscheck.median_nrmse_y)))
    require(cc_error <= 1e-12 and nrmse_error <= 1e-12 and crosscheck.n_windows_x.eq(crosscheck.n_windows_y).all(),
            f"Estimator/source mismatch: CC={cc_error}, NRMSE={nrmse_error}")
    print(f"Saved 720 horizon medians reproduced: CC max error={cc_error:.3g}, NRMSE={nrmse_error:.3g}", flush=True)
    window = horizon.groupby(["session_id", "state", "window_id"], as_index=False).agg(
        Mean_CC_window=("cc", "mean"), Mean_NRMSE_window=("nrmse", "mean"),
        n_horizons=("horizon_s", "nunique"))
    require(len(window) == 901 and window.n_horizons.eq(18).all(), "Window-level means incomplete")
    state = window.groupby(["session_id", "state"], as_index=False).agg(
        Mean_CC=("Mean_CC_window", "median"), Mean_NRMSE=("Mean_NRMSE_window", "median"),
        n_windows=("window_id", "nunique"))
    require(len(state) == 40 and state.groupby("session_id").state.nunique().eq(2).all(), "Incomplete session-state values")
    paired = pd.DataFrame({"session_id": [f"session_{sid:02d}" for sid in EXPECTED_IDS]})
    for metric in ("Mean_CC", "Mean_NRMSE"):
        pivot = state.pivot(index="session_id", columns="state", values=metric).reindex(EXPECTED_IDS)
        require(pivot.notna().all().all(), f"Missing paired {metric}")
        paired[f"{metric}_Awake"] = pivot.Awake.to_numpy(dtype=float)
        paired[f"{metric}_Drowsy"] = pivot.Drowsy.to_numpy(dtype=float)
        paired[f"{metric}_delta"] = paired[f"{metric}_Drowsy"] - paired[f"{metric}_Awake"]
    stats_rows = []
    for i, metric in enumerate(("Mean_CC", "Mean_NRMSE")):
        delta = paired[f"{metric}_delta"].to_numpy(dtype=float)
        statistic, p = exact_wilcoxon(delta)
        ranks = pd.Series(np.abs(delta)).rank(method="average")
        require(not np.isclose(delta, 0, atol=ZERO_TOL, rtol=0).any(), "Zero delta requires review")
        rng = np.random.default_rng(BOOTSTRAP_SEED + i)
        indices = rng.integers(0, 20, size=(BOOTSTRAPS, 20))
        low, high = np.quantile(np.median(delta[indices], axis=1), [0.025, 0.975])
        stats_rows.append({"Metric": metric, "n_sessions": 20, "Median_Delta": float(np.median(delta)),
                           "CI_low": float(low), "CI_high": float(high), "raw_p": p,
                           "r_rb": rank_biserial(delta), "wilcoxon_statistic": statistic,
                           "n_positive": int(np.sum(delta > 0)), "n_negative": int(np.sum(delta < 0)),
                           "n_zero": int(np.sum(delta == 0)), "bootstrap_resamples": BOOTSTRAPS,
                           "bootstrap_seed": BOOTSTRAP_SEED + i,
                           "n_absolute_ties": int(20 - ranks.nunique())})
    statistics = pd.DataFrame(stats_rows)
    old = pd.read_csv(PHASE1 / "outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv").set_index("Metric")
    p_values = [float(statistics.set_index("Metric").loc[metric, "raw_p"]) if metric in ("Mean_CC", "Mean_NRMSE")
                else float(old.loc[metric, "raw_p"]) for metric in METRICS]
    bh = pd.DataFrame({"Metric": METRICS, "raw_p": p_values, "q_BH": bh_adjust(p_values)})
    bh["BH_supported"] = bh.q_BH.lt(0.05)
    OUT.mkdir(parents=True, exist_ok=False)
    outputs = {"horizons": horizon, "windows": window, "paired": paired, "statistics": statistics, "bh": bh}
    for name, frame in outputs.items():
        frame.to_csv(OUT / FILE_NAMES[name], index=False, float_format="%.17g")
    source_files = [Path(__file__).resolve(), index_path, PHASE1 / "notebook/simplex_projection.ipynb", PHASE1 / "main/prediction_nonlinear.ipynb",
                    PHASE1 / "src/prediction/simplex_projection.py", PHASE1 / "src/dataloader/loader.py",
                    PHASE1 / "results/simplex_projection/summary/processed_simplex_summary.csv",
                    PHASE1 / "outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv", *paths]
    manifest = {
        "version": "primary_simplex_windowfirst_P0_v1", "created_utc": datetime.now(timezone.utc).isoformat(),
        "producer": str(Path(__file__).resolve().relative_to(PROJECT)),
        "definition": "mean of all 18 horizons within each valid window, then median of window means within each session-state, then Drowsy minus Awake",
        "configuration": {"representation": "Processed", "label": "P0", "window_s": WINDOW_S, "non_overlapping": True,
                          "valid_window_qc": "segmentation/SQI and stationarity_pass_processed via get_data(..., stationarity='processed')",
                          "m": M, "tau_s": TAU_S, "simplex_k": M + 1, "distance": "Euclidean",
                          "weighting": "normalized exponential", "leave_one_out": True,
                          "theiler_s": THEILER_S, "horizon_s": HORIZONS.tolist(), "nrmse_scale": 1.0},
        "checks": {"sessions": list(EXPECTED_IDS), "windows": 901, "awake_windows": 596, "drowsy_windows": 305,
                   "horizon_rows": len(horizon), "horizons_per_window": 18,
                   "saved_horizon_median_max_abs_cc_error": cc_error,
                   "saved_horizon_median_max_abs_nrmse_error": nrmse_error,
                   "tolerance_horizon_median_abs": 1e-12,
                   "session_order": "numeric ascending", "delta_tolerance": 1e-12},
        "statistics": {"wilcoxon": "notebook exact subset-sum two-sided; zero_method=wilcox; average abs ranks for ties",
                       "rank_biserial": "(sum positive ranks - sum negative ranks) / total ranks",
                       "bootstrap": "NumPy default_rng(seed).integers paired indices; median; 2.5/97.5 percentiles",
                       "bootstrap_resamples": BOOTSTRAPS, "bootstrap_seeds": {"Mean_CC": BOOTSTRAP_SEED, "Mean_NRMSE": BOOTSTRAP_SEED + 1},
                       "zero_tolerance_abs": ZERO_TOL, "BH": "monotone Benjamini-Hochberg over seven primary metrics"},
        "environment": {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__},
        "source_sha256": {str(p.relative_to(PROJECT)): sha256(p) for p in source_files},
        "output_sha256": {FILE_NAMES[name]: sha256(OUT / FILE_NAMES[name]) for name in outputs},
    }
    (OUT / FILE_NAMES["manifest"]).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(statistics.to_string(index=False), flush=True)
    print(bh.to_string(index=False), flush=True)
    print(f"Frozen outputs: {OUT}", flush=True)


if __name__ == "__main__":
    main()
