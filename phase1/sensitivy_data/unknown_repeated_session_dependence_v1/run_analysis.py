"""Frozen unknown repeated-session dependence sensitivity analysis.

Execute in order: prepare, seal, run. No participant linkage is inferred.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import scipy
from scipy.stats import rankdata

ROOT = Path(__file__).resolve().parents[3]
PHASE1 = ROOT / "phase1"
HERE = Path(__file__).resolve().parent
PRED = PHASE1 / "sensitivy_data/primary_simplex_windowfirst_v1/primary_simplex_session_paired_60s_processed_P0_v1.csv"
RQA = PHASE1 / "outputs/rqa/rqa_state_paired_values_60s_processed.csv"
LLE = PHASE1 / "outputs/lle/lle_session_paired_deltas_60s_processed.csv"
REF_BH = PHASE1 / "sensitivy_data/primary_simplex_windowfirst_v1/primary_bh_fdr_7metrics_windowfirst_P0_v1.csv"
REF_PRED_STATS = PHASE1 / "sensitivy_data/primary_simplex_windowfirst_v1/primary_simplex_statistics_60s_processed_P0_v1.csv"
REF_OLD = PHASE1 / "outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv"
METHOD = HERE / "unknown_repeated_session_dependence_method.md"
RESULTS = HERE / "unknown_repeated_session_dependence_results.md"
CANONICAL = HERE / "canonical_20_session_7metric_P0_60s_v1.csv"
BASELINE = HERE / "corrected_n20_baseline_v1.csv"
PROTOCOL = HERE / "protocol.json"
MANIFEST = HERE / "manifest.json"
METRICS = ("Mean_CC", "Mean_NRMSE", "DET", "Lmean", "LAM", "TT", "LLE")
IDS = (1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25)
HEADLINE = ("Mean_CC", "Mean_NRMSE", "DET", "LLE")
EXPECTED_SIGN = {"Mean_CC": -1, "Mean_NRMSE": 1, "DET": -1, "LLE": -1}
SEED = 20260930
N = 100_000
ZERO_TOL = 1e-12
BASELINE_TOL = 2e-8
PREFIXES = (1000, 10_000, 50_000, 100_000)
OBJECTIVES = ("weakest_median", "weakest_r_rb", "weakest_direction_count", "weakest_wilcoxon_support")
STARTS = 100
RANDOM_PAIRINGS = HERE / "random_pairings_v1.csv.gz"
RANDOM_RESULTS = HERE / "random_pairing_metric_results_v1.csv.gz"
SUMMARY = HERE / "random_pairing_summary_v1.csv"
CONVERGENCE = HERE / "convergence_v1.csv"
ADVERSARIAL = HERE / "adversarial_best_found_v1.csv"
SEARCH_STARTS = HERE / "adversarial_local_search_starts_v1.csv"


def require(test: bool, message: str) -> None:
    if not test:
        raise ValueError(message)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sid(value) -> int:
    s = str(value)
    tail = s.removesuffix(".csv").split("_")[-1]
    return int(tail)


def bh(p: np.ndarray) -> np.ndarray:
    p = np.asarray(p, dtype=float)
    require(p.shape[-1] == 7 and np.isfinite(p).all() and ((0 <= p) & (p <= 1)).all(), "Invalid BH input")
    order = np.argsort(p, axis=-1, kind="stable")
    sorted_p = np.take_along_axis(p, order, axis=-1)
    ranks = np.arange(1, 8, dtype=float)
    adjusted_sorted = np.minimum.accumulate((sorted_p * 7 / ranks)[..., ::-1], axis=-1)[..., ::-1]
    result = np.empty_like(adjusted_sorted)
    np.put_along_axis(result, order, np.clip(adjusted_sorted, 0, 1), axis=-1)
    return result


def exact_signed_rank(values: np.ndarray) -> tuple[float, float, float, float, int, bool]:
    """Exact conditional sign-enumeration p; average abs ranks; wilcox zeros."""
    d = np.asarray(values, dtype=float)
    d = d[np.abs(d) > ZERO_TOL]
    n = len(d)
    if not n:
        return 0.0, 0.0, math.nan, 1.0, 0, True
    ranks = rankdata(np.abs(d), method="average")
    wp = float(ranks[d > 0].sum())
    wm = float(ranks[d < 0].sum())
    scaled = np.rint(2 * ranks).astype(int)
    counts = np.array([1], dtype=np.int64)
    for rank in scaled:
        updated = np.zeros(len(counts) + rank, dtype=np.int64)
        updated[: len(counts)] += counts
        updated[rank:] += counts
        counts = updated
    total = int(scaled.sum())
    observed = int(round(2 * wp))
    stat = min(observed, total - observed)
    possible = np.arange(len(counts))
    p = float(counts[np.minimum(possible, total - possible) <= stat].sum() / (1 << n))
    return wp, wm, (wp - wm) / (wp + wm), min(p, 1.0), n, False


def exact_p_lookup_ten() -> np.ndarray:
    ranks = np.arange(1, 11)
    sums = np.zeros(1 << 10, dtype=int)
    for bits in range(1 << 10):
        sums[bits] = int(sum(int(ranks[i]) for i in range(10) if bits & (1 << i)))
    return np.array([np.mean(np.minimum(sums, 55 - sums) <= min(w, 55 - w)) for w in range(56)])

P_LOOKUP_TEN = exact_p_lookup_ten()


def signed_rank_batch(values: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Fast exact n=10 path, exact conditional fallback for zero/tie rows."""
    x = np.asarray(values, dtype=float)
    require(x.ndim == 2 and x.shape[1] == 10 and np.isfinite(x).all(), "Expected finite 10-cluster vectors")
    zero = np.abs(x) <= ZERO_TOL
    ordered_abs = np.sort(np.abs(x), axis=1)
    ties = (np.diff(ordered_abs, axis=1) == 0).any(axis=1)
    fast = ~zero.any(axis=1) & ~ties
    wp = np.empty(len(x), dtype=float)
    wm = np.empty(len(x), dtype=float)
    rrb = np.empty(len(x), dtype=float)
    p = np.empty(len(x), dtype=float)
    n_eff = np.full(len(x), 10, dtype=np.int8)
    all_zero = np.zeros(len(x), dtype=bool)
    if fast.any():
        xf = x[fast]
        order = np.argsort(np.abs(xf), axis=1, kind="stable")
        ranks = np.empty(order.shape, dtype=np.int16)
        np.put_along_axis(ranks, order, np.arange(1, 11, dtype=np.int16), axis=1)
        positive = (ranks * (xf > 0)).sum(axis=1)
        wp[fast] = positive
        wm[fast] = 55 - positive
        rrb[fast] = (2 * positive - 55) / 55
        p[fast] = P_LOOKUP_TEN[positive]
    for i in np.flatnonzero(~fast):
        wp[i], wm[i], rrb[i], p[i], n_eff[i], all_zero[i] = exact_signed_rank(x[i])
    return wp, wm, rrb, p, n_eff, all_zero


def load_canonical() -> pd.DataFrame:
    data = pd.read_csv(CANONICAL, float_precision="round_trip")
    required = ["session_id"] + [f"{m}_{field}" for m in METRICS for field in ("Awake", "Drowsy", "delta")]
    require(data.columns.tolist() == required and len(data) == 20, "Canonical schema/shape changed")
    require(data.session_id.tolist() == [f"session_{v:02d}" for v in IDS], "Canonical order changed")
    require(np.isfinite(data[required[1:]].to_numpy(float)).all(), "Canonical missing/nonfinite values")
    for m in METRICS:
        err = np.max(np.abs(data[f"{m}_delta"] - (data[f"{m}_Drowsy"] - data[f"{m}_Awake"])))
        require(err <= 1e-14, f"Delta identity failed: {m}: {err}")
    return data


def prepare() -> None:
    for p in (CANONICAL, BASELINE, PROTOCOL, MANIFEST, RANDOM_PAIRINGS, RANDOM_RESULTS, RESULTS):
        require(not p.exists(), f"Refusing to overwrite: {p}")
    source_paths = (PRED, RQA, LLE, REF_BH, REF_PRED_STATS, REF_OLD, Path(__file__).resolve())
    require(all(p.is_file() for p in source_paths), "Missing source file")
    frames = {"prediction": pd.read_csv(PRED, float_precision="round_trip"),
              "rqa": pd.read_csv(RQA, float_precision="round_trip"),
              "lle": pd.read_csv(LLE, float_precision="round_trip")}
    columns = {"Mean_CC": ("prediction", "Mean_CC_Awake", "Mean_CC_Drowsy", "Mean_CC_delta"),
               "Mean_NRMSE": ("prediction", "Mean_NRMSE_Awake", "Mean_NRMSE_Drowsy", "Mean_NRMSE_delta"),
               **{m: ("rqa", f"{m}_awake", f"{m}_drowsy", f"{m}_delta") for m in ("DET", "Lmean", "LAM", "TT")},
               "LLE": ("lle", "lle_awake", "lle_drowsy", "delta_lle_drowsy_minus_awake")}
    normalized = {}
    for name, frame in frames.items():
        id_col = "session_id" if name == "prediction" else "session"
        frame = frame.copy()
        frame["_sid"] = frame[id_col].map(sid)
        require(len(frame) == 20 and frame._sid.is_unique and set(frame._sid) == set(IDS), f"Session coverage failed: {name}")
        if name != "prediction":
            require(frame.representation.eq("Processed").all(), f"Wrong representation: {name}")
            size_col = "window_size" if name == "rqa" else "window_size_s"
            require(frame[size_col].eq(60).all(), f"Wrong window size: {name}")
        normalized[name] = frame.set_index("_sid").loc[list(IDS)]
    canonical = pd.DataFrame({"session_id": [f"session_{i:02d}" for i in IDS]})
    for metric, (name, awake_col, drowsy_col, delta_col) in columns.items():
        source = normalized[name]
        awake = source[awake_col].to_numpy(float)
        drowsy = source[drowsy_col].to_numpy(float)
        recorded = source[delta_col].to_numpy(float)
        delta = drowsy - awake
        require(np.isfinite(np.column_stack([awake, drowsy, delta])).all(), f"Nonfinite: {metric}")
        require(np.max(np.abs(recorded - delta)) <= (2e-8 if name == "prediction" else 2e-9), f"Recorded delta mismatch: {metric}")
        for label, values in (("Awake", awake), ("Drowsy", drowsy), ("delta", delta)):
            canonical[f"{metric}_{label}"] = values
    CANONICAL.parent.mkdir(parents=True, exist_ok=True)
    canonical.to_csv(CANONICAL, index=False, float_format="%.17g")
    canonical = load_canonical()
    # Mandatory gate: no hypothetical matching is generated before every metric reproduces.
    rows = []
    for metric in METRICS:
        d = canonical[f"{metric}_delta"].to_numpy(float)
        wp, wm, rrb, p, n_eff, all_zero = exact_signed_rank(d)
        require(not all_zero and n_eff == 20, f"Unexpected baseline zero: {metric}")
        rows.append({"Metric": metric, "n": 20, "Median_Delta": float(np.median(d)),
                     "W_plus": wp, "W_minus": wm, "r_rb": rrb, "raw_p": p})
    baseline = pd.DataFrame(rows)
    baseline["q_BH"] = bh(baseline.raw_p.to_numpy())
    reference = pd.read_csv(REF_BH, float_precision="round_trip").set_index("Metric").reindex(METRICS)
    old = pd.read_csv(REF_OLD, float_precision="round_trip").set_index("Metric")
    pred_stats = pd.read_csv(REF_PRED_STATS, float_precision="round_trip").set_index("Metric")
    for _, row in baseline.iterrows():
        m = row.Metric
        target_median = pred_stats.loc[m, "Median_Delta"] if m in ("Mean_CC", "Mean_NRMSE") else old.loc[m, "Median_Delta"]
        for field, target in (("Median_Delta", target_median), ("raw_p", reference.loc[m, "raw_p"]),
                              ("r_rb", pred_stats.loc[m, "r_rb"] if m in ("Mean_CC", "Mean_NRMSE") else old.loc[m, "r_rb"]),
                              ("q_BH", reference.loc[m, "q_BH"])):
            require(abs(float(row[field]) - float(target)) <= BASELINE_TOL,
                    f"BASELINE MISMATCH: {m} {field}: {row[field]} vs {target}; STOP")
    require(set(baseline.loc[baseline.q_BH.lt(.05), "Metric"]) == {"Mean_CC", "Mean_NRMSE", "DET", "LLE"}, "Baseline supported set differs; STOP")
    baseline.to_csv(BASELINE, index=False, float_format="%.17g")
    protocol = {
        "version": "unknown_repeated_session_dependence_v1", "frozen_utc": utc_now(),
        "canonical_sha256": sha256(CANONICAL), "session_order": list(IDS), "metrics": list(METRICS),
        "headline_expected_sign": EXPECTED_SIGN, "n_random_pairings": N, "random_seed": SEED,
        "matching": "NumPy default_rng(seed).permutation(20), adjacent pairs, sort within/across pairs; with replacement",
        "n_total_possible_matchings": 654729075, "pair_aggregation": "arithmetic mean of the two session deltas",
        "zero_tolerance_abs": ZERO_TOL, "zero_tolerance_rtol": 0.0,
        "wilcoxon": "two-sided exact conditional sign enumeration; wilcox zeros; average abs ranks for ties; p=1 and r_rb=NaN if all zero",
        "rank_biserial": "(W_plus-W_minus)/(W_plus+W_minus)", "BH": "monotone BH across all seven metrics per matching",
        "direction": "expected_sign * effect > 1e-12; zero within tolerance does not preserve direction",
        "summary_percentiles": [0, 2.5, 25, 50, 75, 97.5, 100], "convergence_prefixes": list(PREFIXES),
        "adversarial_objectives": list(OBJECTIVES), "adversarial_starts_per_objective": STARTS,
        "adversarial_neighborhood": "90 two-pair swaps; two cross-repairings per pair-of-pairs",
        "adversarial_improvement_tolerance": 1e-12,
        "adversarial_tie_break": "lexicographically smallest sorted canonical pair representation",
        "bootstrap_inside_pairings": False, "baseline_tolerance_abs": BASELINE_TOL,
        "software": {"python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__},
    }
    PROTOCOL.write_text(json.dumps(protocol, indent=2, ensure_ascii=False) + "\n")
    manifest = {"status": "prepared_baseline_verified", "created_utc": utc_now(),
                "source_sha256": {str(p.relative_to(ROOT)): sha256(p) for p in source_paths},
                "canonical_sha256": sha256(CANONICAL), "baseline_sha256": sha256(BASELINE),
                "protocol_sha256": sha256(PROTOCOL), "method_sha256": None, "output_sha256": {}}
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print("BASELINE PASS; no matchings generated", flush=True)
    print(baseline.to_string(index=False), flush=True)
    print("canonical_sha256", sha256(CANONICAL), flush=True)


def seal() -> None:
    manifest = json.loads(MANIFEST.read_text())
    require(manifest["status"] == "prepared_baseline_verified" and METHOD.is_file(), "Prepare and write Method before seal")
    require(sha256(CANONICAL) == manifest["canonical_sha256"] and sha256(PROTOCOL) == manifest["protocol_sha256"], "Pre-run freeze changed")
    manifest["method_sha256"] = sha256(METHOD)
    manifest["status"] = "method_sealed_before_pairing"
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print("METHOD SEALED BEFORE PAIRINGS", manifest["method_sha256"], flush=True)


def pairing_key(pairs: np.ndarray) -> tuple[int, ...]:
    return tuple(int(x) for x in np.asarray(pairs).reshape(-1))


def canonicalize(pairs: np.ndarray) -> np.ndarray:
    pairs = np.sort(np.asarray(pairs, dtype=np.uint8), axis=1)
    return pairs[np.lexsort((pairs[:, 1], pairs[:, 0]))]


def pairing_text(pairs: np.ndarray) -> str:
    return "[" + ",".join(f"({IDS[int(a)]:02d},{IDS[int(b)]:02d})" for a, b in pairs) + "]"


def objective_values(x: np.ndarray, sign: int, objective: str) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    if objective == "weakest_median":
        return sign * np.median(x, axis=1)
    if objective == "weakest_direction_count":
        return np.sum(sign * x > ZERO_TOL, axis=1).astype(float)
    _, _, rrb, p, _, _ = signed_rank_batch(x)
    return sign * rrb if objective == "weakest_r_rb" else -p


def neighbors(key: tuple[int, ...]) -> tuple[list[tuple[int, ...]], np.ndarray]:
    current = np.array(key, dtype=np.uint8).reshape(10, 2)
    keys = []
    for i in range(10):
        for j in range(i + 1, 10):
            a, b = (int(v) for v in current[i])
            c, d = (int(v) for v in current[j])
            for replacement in (((a, c), (b, d)), ((a, d), (b, c))):
                trial = current.copy()
                trial[i] = replacement[0]
                trial[j] = replacement[1]
                keys.append(pairing_key(canonicalize(trial)))
    require(len(keys) == 90 and len(set(keys)) == 90, "Neighborhood must have 90 distinct swaps")
    return keys, np.array(keys, dtype=np.uint8).reshape(90, 10, 2)


def local_search(start_key: tuple[int, ...], metric_index: int, objective: str, delta: np.ndarray, sign: int) -> tuple[tuple[int, ...], float, int]:
    current_key = start_key
    current_pairs = np.array(current_key, dtype=np.uint8).reshape(10, 2)
    x = .5 * (delta[current_pairs[:, 0], metric_index] + delta[current_pairs[:, 1], metric_index])
    current_value = float(objective_values(x[None, :], sign, objective)[0])
    steps = 0
    while True:
        keys, candidates = neighbors(current_key)
        values = .5 * (delta[candidates[:, :, 0], metric_index] + delta[candidates[:, :, 1], metric_index])
        objective_scores = objective_values(values, sign, objective)
        best = min(range(90), key=lambda i: (float(objective_scores[i]), keys[i]))
        best_value = float(objective_scores[best])
        if best_value >= current_value - 1e-12:
            return current_key, current_value, steps
        current_key, current_value = keys[best], best_value
        steps += 1
        require(steps < 10000, "Local search failed to terminate")


def csv_gzip(frame: pd.DataFrame, path: Path) -> None:
    with path.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0, compresslevel=6) as zipped:
            frame.to_csv(zipped, index=False, float_format="%.17g")


def run() -> None:
    manifest = json.loads(MANIFEST.read_text())
    require(manifest["status"] == "method_sealed_before_pairing", "Method must be sealed before random pairings")
    for p in (RANDOM_PAIRINGS, RANDOM_RESULTS, SUMMARY, CONVERGENCE, ADVERSARIAL, SEARCH_STARTS, RESULTS):
        require(not p.exists(), f"Refusing to overwrite: {p}")
    for path, digest in manifest["source_sha256"].items():
        require(sha256(ROOT / path) == digest, f"Source changed after freeze: {path}")
    require(sha256(CANONICAL) == manifest["canonical_sha256"] and sha256(BASELINE) == manifest["baseline_sha256"], "Canonical/baseline changed")
    require(sha256(PROTOCOL) == manifest["protocol_sha256"] and sha256(METHOD) == manifest["method_sha256"], "Method/protocol changed")
    protocol = json.loads(PROTOCOL.read_text())
    require(protocol["n_random_pairings"] == N and protocol["random_seed"] == SEED and tuple(protocol["convergence_prefixes"]) == PREFIXES, "Frozen settings differ")
    canonical = load_canonical()
    baseline = pd.read_csv(BASELINE, float_precision="round_trip").set_index("Metric").reindex(METRICS)
    delta = canonical[[f"{m}_delta" for m in METRICS]].to_numpy(float)
    rng = np.random.default_rng(SEED)
    pairings = np.empty((N, 10, 2), dtype=np.uint8)
    for i in range(N):
        pairings[i] = canonicalize(rng.permutation(20).reshape(10, 2))
    flat = pairings.reshape(N, 20)
    unique_flat, unique_idx = np.unique(flat, axis=0, return_index=True)
    n_unique = len(unique_flat)
    matching_strings = [pairing_text(pair) for pair in pairings]
    csv_gzip(pd.DataFrame({"pairing_id": np.arange(1, N + 1), "matching": matching_strings}), RANDOM_PAIRINGS)
    print(f"Generated {N} matchings; unique={n_unique}; duplicate_fraction={(N-n_unique)/N:.8f}", flush=True)
    clusters = .5 * (delta[pairings[:, :, 0]] + delta[pairings[:, :, 1]])
    medians = np.median(clusters, axis=1)
    signs = np.array([EXPECTED_SIGN.get(m, int(np.sign(baseline.loc[m, "Median_Delta"]))) for m in METRICS], dtype=int)
    require(np.all(signs != 0), "A reference direction is zero")
    directions = np.sum(signs[None, None, :] * clusters > ZERO_TOL, axis=1)
    preserved = signs[None, :] * medians > ZERO_TOL
    wp = np.empty((N, 7)); wm = np.empty((N, 7)); rrb = np.empty((N, 7)); p = np.empty((N, 7))
    n_eff = np.empty((N, 7), dtype=np.int8); all_zero = np.empty((N, 7), dtype=bool)
    for j, metric in enumerate(METRICS):
        wp[:, j], wm[:, j], rrb[:, j], p[:, j], n_eff[:, j], all_zero[:, j] = signed_rank_batch(clusters[:, :, j])
        print("Computed", metric, "all-zero cases", int(all_zero[:, j].sum()), flush=True)
    q = bh(p)
    # Audit vectorized exact path against the general conditional sign enumerator.
    for i in (0, 1, 999, 9999, 49999, 99999):
        for j in range(7):
            awp, awm, arr, ap, an, az = exact_signed_rank(clusters[i, :, j])
            require(abs(awp - wp[i, j]) < 1e-12 and abs(awm - wm[i, j]) < 1e-12 and abs(ap - p[i, j]) < 1e-15 and an == n_eff[i, j], "Fast exact Wilcoxon mismatch")
    result_frame = pd.DataFrame({
        "pairing_id": np.repeat(np.arange(1, N + 1), 7), "metric": np.tile(METRICS, N),
        "median_delta_star": medians.ravel(), "direction_preserved": preserved.ravel(),
        "direction_count": directions.ravel(), "W_plus": wp.ravel(), "W_minus": wm.ravel(),
        "r_rb": rrb.ravel(), "raw_p": p.ravel(), "q_BH": q.ravel(),
        "raw_p_below_05": (p < .05).ravel(), "q_BH_below_05": (q < .05).ravel(),
        "n_eff": n_eff.ravel(), "all_zero": all_zero.ravel()})
    csv_gzip(result_frame, RANDOM_RESULTS)
    summaries = []
    for j, metric in enumerate(METRICS):
        m = medians[:, j]
        rr = rrb[:, j]
        ratio = np.abs(m) / abs(float(baseline.loc[metric, "Median_Delta"]))
        row = {"metric": metric, "headline": metric in HEADLINE, "original_n20_median_delta": float(baseline.loc[metric, "Median_Delta"]),
               "expected_sign": int(signs[j]), "median_delta_star_min": float(np.min(m)),
               "median_delta_star_p025": float(np.percentile(m, 2.5)), "median_delta_star_p25": float(np.percentile(m, 25)),
               "median_delta_star_median": float(np.median(m)), "median_delta_star_p75": float(np.percentile(m, 75)),
               "median_delta_star_p975": float(np.percentile(m, 97.5)), "median_delta_star_max": float(np.max(m)),
               "r_rb_p025": float(np.nanpercentile(rr, 2.5)), "r_rb_median": float(np.nanmedian(rr)),
               "r_rb_p975": float(np.nanpercentile(rr, 97.5)),
               "direction_preserved_fraction": float(np.mean(preserved[:, j])),
               "direction_count_min": int(np.min(directions[:, j])),
               "direction_count_p025": float(np.percentile(directions[:, j], 2.5)),
               "direction_count_median": float(np.median(directions[:, j])),
               "direction_count_max": int(np.max(directions[:, j])),
               "magnitude_ratio_p025": float(np.percentile(ratio, 2.5)),
               "magnitude_ratio_median": float(np.median(ratio)),
               "magnitude_ratio_p975": float(np.percentile(ratio, 97.5)),
               "raw_p_below_05_fraction": float(np.mean(p[:, j] < .05)),
               "q_BH_below_05_fraction": float(np.mean(q[:, j] < .05)),
               "all_zero_count": int(all_zero[:, j].sum())}
        row.update({f"direction_count_{k}_frequency": int(np.sum(directions[:, j] == k)) for k in range(11)})
        summaries.append(row)
    summary = pd.DataFrame(summaries)
    summary.to_csv(SUMMARY, index=False, float_format="%.17g")
    convergences = []
    for prefix in PREFIXES:
        for metric in HEADLINE:
            j = METRICS.index(metric); v = medians[:prefix, j]
            convergences.append({"prefix": prefix, "metric": metric,
                                 "direction_preserved_fraction": float(np.mean(preserved[:prefix, j])),
                                 "median_of_median_delta_star": float(np.median(v)),
                                 "median_delta_star_p025": float(np.percentile(v, 2.5)),
                                 "median_delta_star_p975": float(np.percentile(v, 97.5)),
                                 "median_r_rb": float(np.nanmedian(rrb[:prefix, j])),
                                 "q_BH_below_05_fraction": float(np.mean(q[:prefix, j] < .05))})
    convergence = pd.DataFrame(convergences)
    convergence.to_csv(CONVERGENCE, index=False, float_format="%.17g")
    # The adversarial search begins only after every random result and convergence file exists.
    starts_rows = []; best_rows = []
    for metric in HEADLINE:
        j = METRICS.index(metric); sign = EXPECTED_SIGN[metric]
        for objective in OBJECTIVES:
            if objective == "weakest_median": values = sign * medians[:, j]
            elif objective == "weakest_r_rb": values = sign * rrb[:, j]
            elif objective == "weakest_direction_count": values = directions[:, j].astype(float)
            else: values = -p[:, j]
            unique_scores = values[unique_idx]
            unique_keys = flat[unique_idx]
            sort_keys = [unique_keys[:, c] for c in range(19, -1, -1)] + [unique_scores]
            ranked = np.lexsort(tuple(sort_keys))[:STARTS]
            finals = []
            for start_rank, pos in enumerate(ranked, 1):
                start_idx = int(unique_idx[pos])
                start_key = pairing_key(pairings[start_idx])
                final_key, final_value, steps = local_search(start_key, j, objective, delta, sign)
                finals.append((final_value, final_key, start_idx, steps, start_rank))
                starts_rows.append({"metric": metric, "objective": objective, "start_rank": start_rank,
                                    "start_pairing_id": start_idx + 1, "start_matching": pairing_text(pairings[start_idx]),
                                    "start_objective": float(values[start_idx]),
                                    "final_matching": pairing_text(np.array(final_key).reshape(10, 2)),
                                    "final_objective": final_value, "local_search_steps": steps})
            best = min(finals, key=lambda x: (x[0], x[1]))
            best_key = best[1]; best_pairs = np.array(best_key, dtype=np.uint8).reshape(10, 2)
            best_cluster = .5 * (delta[best_pairs[:, 0]] + delta[best_pairs[:, 1]])
            best_p = np.array([exact_signed_rank(best_cluster[:, t])[3] for t in range(7)])
            best_q = bh(best_p)
            bwp, bwm, brr, bp, _, _ = exact_signed_rank(best_cluster[:, j])
            best_rows.append({"metric": metric, "objective": objective,
                              "most_conservative_matching_found": pairing_text(best_pairs),
                              "median_delta_star": float(np.median(best_cluster[:, j])),
                              "direction_count": int(np.sum(sign * best_cluster[:, j] > ZERO_TOL)),
                              "W_plus": bwp, "W_minus": bwm, "r_rb": brr, "raw_p": bp, "q_BH": float(best_q[j]),
                              "objective_value": best[0], "best_start_pairing_id": best[2] + 1,
                              "best_start_rank": best[4], "best_start_steps": best[3],
                              "n_distinct_local_optima": len({entry[1] for entry in finals}),
                              "n_starts_at_best_matching": sum(entry[1] == best_key for entry in finals),
                              "n_starts": STARTS, "global_optimality_proven": False})
            print("Search", metric, objective, "best", best[0], "unique optima", best_rows[-1]["n_distinct_local_optima"], flush=True)
    pd.DataFrame(starts_rows).to_csv(SEARCH_STARTS, index=False, float_format="%.17g")
    adversarial = pd.DataFrame(best_rows)
    adversarial.to_csv(ADVERSARIAL, index=False, float_format="%.17g")
    write_results(summary, convergence, adversarial, baseline, n_unique, all_zero)
    output_files = (CANONICAL, BASELINE, PROTOCOL, METHOD, RANDOM_PAIRINGS, RANDOM_RESULTS, SUMMARY, CONVERGENCE, ADVERSARIAL, SEARCH_STARTS, RESULTS)
    manifest["status"] = "complete"
    manifest["completed_utc"] = utc_now()
    manifest["n_generated_matchings"] = N
    manifest["n_unique_matchings"] = n_unique
    manifest["duplicate_fraction"] = (N - n_unique) / N
    manifest["output_sha256"] = {p.name: sha256(p) for p in output_files}
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print("ANALYSIS COMPLETE", flush=True)


def fmt(value: float, digits=4) -> str:
    return f"{float(value):.{digits}f}"


def write_results(summary: pd.DataFrame, convergence: pd.DataFrame, adversarial: pd.DataFrame,
                  baseline: pd.DataFrame, n_unique: int, all_zero: np.ndarray) -> None:
    s = summary.set_index("metric")
    lines = ["# Unknown repeated-session dependence sensitivity — results", "",
             "## 1. Executive result", ""]
    for metric in HEADLINE:
        row = s.loc[metric]
        lines.append(f"- **{metric}:** expected median direction in {100*row.direction_preserved_fraction:.3f}% of 100,000 random hypothetical pairings; median Δ*={row.median_delta_star_median:+.6f}, 2.5–97.5% [{row.median_delta_star_p025:+.6f}, {row.median_delta_star_p975:+.6f}]; q<0.05 in {100*row.q_BH_below_05_fraction:.2f}%.")
    lines += ["", "These are hypothetical two-session clusters, not recovered participant mappings. Direction and magnitude are the primary evidence; p/q support is secondary.", "",
              "## 2. Input and baseline verification", "",
              f"Canonical input: [`{CANONICAL.name}`]({CANONICAL.name}); SHA-256 `{sha256(CANONICAL)}`. Exactly 20 numerically sorted sessions and seven complete paired metrics; baseline validation passed **before any matching was generated**. Source hashes and frozen settings are in [`manifest.json`](manifest.json) and [`protocol.json`](protocol.json).", "",
              "| Metric | n=20 median Δ | n=20 p | n=20 r_rb | n=20 q_BH |", "| --- | ---: | ---: | ---: | ---: |"]
    for metric in METRICS:
        r = baseline.loc[metric]
        lines.append(f"| {metric} | {r.Median_Delta:+.6f} | {r.raw_p:.8f} | {r.r_rb:+.6f} | {r.q_BH:.8f} |")
    lines += ["", "## 3. Random-pairing sensitivity", "",
              f"Generated **{N:,}** matchings with replacement from the **654,729,075** possible perfect matchings; **{n_unique:,} unique**, duplicate fraction **{(N-n_unique)/N:.6%}**. The complete ordered sequence and 700,000 metric results are in the compressed CSVs. The 2.5–97.5% interval below describes variation across sampled hypothetical matchings; it is not a bootstrap confidence interval for a participant effect.", "",
              "| Metric | Original n=20 Δ | Median Δ* | Δ* 2.5–97.5% | Same-direction % | Median r_rb | r_rb 2.5–97.5% | p<0.05 % | q<0.05 % |",
              "| --- | ---: | ---: | --- | ---: | ---: | --- | ---: | ---: |"]
    for metric in METRICS:
        r = s.loc[metric]
        name = f"**{metric}**" if metric in HEADLINE else metric
        lines.append(f"| {name} | {r.original_n20_median_delta:+.6f} | {r.median_delta_star_median:+.6f} | [{r.median_delta_star_p025:+.6f}, {r.median_delta_star_p975:+.6f}] | {100*r.direction_preserved_fraction:.3f} | {r.r_rb_median:+.3f} | [{r.r_rb_p025:+.3f}, {r.r_rb_p975:+.3f}] | {100*r.raw_p_below_05_fraction:.2f} | {100*r.q_BH_below_05_fraction:.2f} |")
    lines += ["", "For Lmean, LAM and TT, ‘same direction’ is descriptive relative to the observed n=20 median sign; the four predefined headline signs govern primary interpretation. Full min/25th/75th/max and magnitude distributions are in [`random_pairing_summary_v1.csv`](random_pairing_summary_v1.csv).", "",
              "## 4. Directional robustness of headline metrics", "",
              "A cluster counts toward the expected direction only when its oriented Δ* exceeds 1e-12; a median within that tolerance of zero does not preserve direction.", "",
              "| Metric | Expected direction | Preserved % | Direction-count min / 2.5th / median / max | Sampled median crossed/touched zero? |",
              "| --- | --- | ---: | --- | --- |"]
    for metric in HEADLINE:
        r = s.loc[metric]; sign = EXPECTED_SIGN[metric]
        crossed = r.median_delta_star_max >= -ZERO_TOL if sign < 0 else r.median_delta_star_min <= ZERO_TOL
        lines.append(f"| {metric} | {'negative' if sign < 0 else 'positive'} | {100*r.direction_preserved_fraction:.3f} | {int(r.direction_count_min)} / {r.direction_count_p025:.2f} / {r.direction_count_median:.2f} / {int(r.direction_count_max)} | {'Yes' if crossed else 'No'} |")
    lines += ["", "Full direction-count distribution across the fixed 100,000 matchings (percentages):", "",
              "| Metric | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |",
              "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for metric in HEADLINE:
        r = s.loc[metric]
        frequencies = [f"{float(r[f'direction_count_{k}_frequency']) / N * 100:.3f}" for k in range(11)]
        lines.append(f"| {metric} | " + " | ".join(frequencies) + " |")
    lines += ["", "## 5. Effect-magnitude stability", "",
              "Magnitude ratio is |median Δ*| / |original n=20 median Δ|, a descriptive scale comparison. Distribution endpoints and inner quantiles of Δ* are recorded in the summary CSV.", "",
              "| Metric | Δ* min / 2.5th / median / 97.5th / max | Magnitude ratio 2.5th / median / 97.5th |",
              "| --- | --- | --- |"]
    for metric in METRICS:
        r = s.loc[metric]
        lines.append(f"| {metric} | {r.median_delta_star_min:+.6f} / {r.median_delta_star_p025:+.6f} / {r.median_delta_star_median:+.6f} / {r.median_delta_star_p975:+.6f} / {r.median_delta_star_max:+.6f} | {r.magnitude_ratio_p025:.3f} / {r.magnitude_ratio_median:.3f} / {r.magnitude_ratio_p975:.3f} |")
    lines += ["", "Inner quartiles of sampled median effects:", "", "| Metric | 25th percentile Δ* | 75th percentile Δ* |", "| --- | ---: | ---: |"]
    for metric in METRICS:
        r = s.loc[metric]
        lines.append(f"| {metric} | {r.median_delta_star_p25:+.6f} | {r.median_delta_star_p75:+.6f} |")
    lines.append("")
    for metric in HEADLINE:
        r = s.loc[metric]
        zero_or_reverse = 100 * (1 - float(r.direction_preserved_fraction))
        lines.append(f"- **{metric}:** {zero_or_reverse:.3f}% of sampled median effects were zero or opposite to the expected direction; the 2.5th percentile of the magnitude ratio was {r.magnitude_ratio_p025:.3f}. This quantifies observed movement toward zero without imposing a post hoc collapse threshold.")
    lines += ["", "## 6. Inferential support under n=10 hypothetical clusters", "",
              "The p<0.05 and seven-metric BH q<0.05 fractions are shown in Section 3. Lower support fractions at n=10 can reflect reduced effective sample size and do not by themselves imply a reversed effect. Exact two-sided Wilcoxon used the same zero/tie rule for every matching; no nested bootstrap was run.", "",
              f"All-zero hypothetical-cluster vectors: **{int(all_zero.sum())}** across 700,000 metric-matching evaluations; when present, the frozen convention is p=1 and r_rb=NaN.", "",
              "## 7. Monte-Carlo convergence", "",
              "All prefixes use the same prespecified sequence; N=100,000 was not adapted. The full 16-row table including 2.5th/97.5th percentiles and median r_rb is [`convergence_v1.csv`](convergence_v1.csv).", "",
              "| Metric | Prefix | Sign % | Median Δ* | Δ* 2.5–97.5% | Median r_rb | q<0.05 % |",
              "| --- | ---: | ---: | ---: | --- | ---: | ---: |"]
    for metric in HEADLINE:
        for _, r in convergence.loc[convergence.metric.eq(metric)].iterrows():
            lines.append(f"| {metric} | {int(r.prefix):,} | {100*r.direction_preserved_fraction:.3f} | {r.median_of_median_delta_star:+.6f} | [{r.median_delta_star_p025:+.6f}, {r.median_delta_star_p975:+.6f}] | {r.median_r_rb:+.3f} | {100*r.q_BH_below_05_fraction:.2f} |")
    lines += ["", "Change from the 50,000 to 100,000 prefix, reported without a post hoc stopping threshold:", "", "| Metric | Sign-fraction change (percentage points) | Median Δ* absolute change | 2.5th / 97.5th Δ* absolute change | Median r_rb absolute change | q-support change (percentage points) |", "| --- | ---: | ---: | --- | ---: | ---: |"]
    for metric in HEADLINE:
        group = convergence.loc[convergence.metric.eq(metric)].set_index("prefix")
        a, b = group.loc[50_000], group.loc[100_000]
        lines.append(f"| {metric} | {100*abs(b.direction_preserved_fraction-a.direction_preserved_fraction):.4f} | {abs(b.median_of_median_delta_star-a.median_of_median_delta_star):.8f} | {abs(b.median_delta_star_p025-a.median_delta_star_p025):.8f} / {abs(b.median_delta_star_p975-a.median_delta_star_p975):.8f} | {abs(b.median_r_rb-a.median_r_rb):.6f} | {100*abs(b.q_BH_below_05_fraction-a.q_BH_below_05_fraction):.4f} |")
    lines.append("These prefix comparisons are diagnostic; the prespecified 100,000 draw remains the final analysis.")
    lines += ["", "## 8. Conservative/adversarial search", "",
              "The table reports the **most conservative pairing found** for each prespecified metric/objective by 100-start steepest local search over 90 swaps per step. Each metric was optimized independently. These are discovered local optima, not proven global optima; the pairing is hypothetical. The full CSV includes the objective, starting candidate, number of steps and convergence across starts.", "",
              "| Metric | Objective | Most conservative median Δ* | Direction count /10 | r_rb | p | q_BH for that matching | Pairing |",
              "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |"]
    for _, r in adversarial.iterrows():
        lines.append(f"| {r.metric} | {r.objective} | {r.median_delta_star:+.6f} | {int(r.direction_count)}/10 | {r.r_rb:+.3f} | {r.raw_p:.6f} | {r.q_BH:.6f} | `{r.most_conservative_matching_found}` |")
    lines += ["", "## 9. Integrated interpretation", ""]
    for metric in HEADLINE:
        r = s.loc[metric]
        if r.direction_preserved_fraction == 1:
            wording = "preserved the expected direction in every sampled matching"
        else:
            wording = f"preserved the expected direction in {100*r.direction_preserved_fraction:.3f}% of sampled matchings; reversals/zeros did occur"
        lines.append(f"- **{metric}:** {wording}. Median magnitude ratio {r.magnitude_ratio_median:.3f} (2.5–97.5% {r.magnitude_ratio_p025:.3f}–{r.magnitude_ratio_p975:.3f}); median r_rb {r.r_rb_median:+.3f}; q support {100*r.q_BH_below_05_fraction:.2f}%.")
    lines += ["", "The conservative searches show additional possible fragility within the specified local-search neighborhood; they do not estimate how likely any particular matching is in the actual dataset.", "",
              "## 10. Manuscript implication", "",
              "The corrected window-first Mean CC/Mean NRMSE baseline must replace the legacy prediction numbers. The random and conservative results above can be described as sensitivity to **unknown repeated-session dependence** under hypothetical two-session clustering. Manuscript claims about significance should use the reported support frequencies and should not describe the hypothetical clusters as observed participants.", "",
              "## 11. Remaining limitation", "",
              "True participant-session linkage remains unavailable, so actual within-participant correlation cannot be estimated. Hypothetical pairings do not replace cluster-aware inference using identified participants and do not establish participant-level effects. The analysis only measures how the present session-level conclusions change under the prespecified plausible clustering model.", "",
              "## 12. Final conclusion", ""]
    if all(float(s.loc[m, "direction_preserved_fraction"]) == 1 for m in HEADLINE):
        lines.append("**Do the principal Awake–Drowsy conclusions appear dependent on treating all 20 sessions as independent inferential units?** Their **directions did not** depend on that assumption across the 100,000 sampled hypothetical pairings; the size of the effects and statistical support varied under ten-cluster aggregation. Conservative local-search findings above delimit the interpretation without identifying actual participant clusters.")
    else:
        lines.append("**Do the principal Awake–Drowsy conclusions appear dependent on treating all 20 sessions as independent inferential units?** At least one predefined headline direction changed in sampled hypothetical pairings. The per-metric frequencies, magnitude ranges, and conservative searches above show which findings are sensitive; no participant linkage is inferred.")
    RESULTS.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    require(len(sys.argv) == 2 and sys.argv[1] in {"prepare", "seal", "run"}, "Usage: run_analysis.py prepare|seal|run")
    {"prepare": prepare, "seal": seal, "run": run}[sys.argv[1]]()
