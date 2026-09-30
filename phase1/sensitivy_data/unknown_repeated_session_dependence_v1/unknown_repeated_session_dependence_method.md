# Unknown repeated-session dependence sensitivity — frozen method

Protocol version: `unknown_repeated_session_dependence_v1`. Frozen on 2026-09-30 UTC after the corrected n=20 baseline gate passed and **before** generating any hypothetical matching. This document and [`protocol.json`](protocol.json) are hashed in [`manifest.json`](manifest.json). The executable implementation is [`run_analysis.py`](run_analysis.py).

## 1. Motivation

The primary analysis contains 20 recording sessions from 10 healthy young adults. The true participant–session linkage is unavailable, so the amount of repeated-session dependence in the 20 session-level inferential units cannot be estimated directly. The analysis asks how the seven Awake–Drowsy results change if the 20 sessions are aggregated into ten possible two-session clusters.

## 2. Scope and claim boundary

This is a **sensitivity analysis to unknown repeated-session dependence**. A matching is a hypothetical two-session clustering, not an estimate of the true mapping. The procedure cannot reconstruct participant identity, measure actual within-participant correlation, or replace cluster-aware inference with known participant identifiers. Windows remain computational units in the source analyses; only session-level paired differences enter this sensitivity experiment.

## 3. Canonical input and mandatory baseline gate

The input is [`canonical_20_session_7metric_P0_60s_v1.csv`](canonical_20_session_7metric_P0_60s_v1.csv), exactly 20 rows × 22 columns, 60-s P0 Processed PPG, one row per session, seven paired metrics and three columns per metric. Session IDs are normalized to `session_XX` and sorted numerically: 01, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25. The same ID set is required in all three sources, with finite Awake/Drowsy values and no duplicate session. Every canonical delta is recomputed from full-precision source state values as Drowsy − Awake and checked against the source delta.

| Metrics | Frozen source | Definition used |
| --- | --- | --- |
| Mean CC; Mean NRMSE | [`primary_simplex_session_paired_60s_processed_P0_v1.csv`](../primary_simplex_windowfirst_v1/primary_simplex_session_paired_60s_processed_P0_v1.csv) | Corrected window-first Simplex: mean across 18 prediction horizons in each valid window, then median of windows within session-state. The legacy mean-of-horizon-medians source is excluded. |
| DET; Lmean; LAM; TT | [`rqa_state_paired_values_60s_processed.csv`](../../outputs/rqa/rqa_state_paired_values_60s_processed.csv) | Median of eligible RQA windows within session-state. |
| LLE | [`lle_session_paired_deltas_60s_processed.csv`](../../outputs/lle/lle_session_paired_deltas_60s_processed.csv) | Median of valid Rosenstein LLE windows within session-state; unit s⁻¹. |

SHA-256 of these sources, respectively: `58d33e413b4f7582ebb0b8627efd3712ab218ed8b210c2263abc06fd361ce90c`, `b7c3206322ffbb5ff1ef7a16f0e54e8ab73946c4bdb7260732eb85198754f7dc`, `1385247cce74beceee7c7dc1e874593ab5b38d4563be5894ff35ee423f5ec62a`. Canonical SHA-256: `3cdc90d0bf214244fcced56a44a692bd941432352837fe285d31be0c9f375286`. The manifest records these and the hashes of the reference statistics and code. The underlying primary configuration remains the corrected 60-s P0 Processed branch: Simplex m=8, τ=0.16 s, Theiler=1.0 s and 18 horizons; RQA target RR=0.02, line minima 2; LLE unit s⁻¹ with valid-window QC from its frozen source. No metric is re-estimated from window data here.

**Gate before matching:** from the canonical 20 deltas, compute each metric's median delta, two-sided exact signed-rank p, matched-pairs rank-biserial correlation, then one monotone BH correction over seven p values. Compare median, p, r_rb and q against the frozen corrected primary tables with absolute tolerance `2e-8`; require the supported set at q<0.05 to be Mean CC, Mean NRMSE, DET and LLE. A mismatch aborts before random generation. The verified values are saved in [`corrected_n20_baseline_v1.csv`](corrected_n20_baseline_v1.csv).

## 4. Hypothetical clustering model

A perfect matching partitions 20 sessions into ten nonoverlapping pairs. For each metric and pair `(i,j)`, the hypothetical cluster difference is `delta* = (delta_i + delta_j)/2`, an unweighted arithmetic mean. The 10 differences are used as the reduced-unit vector for that matching. No biological or identity claim is attached to a particular pair.

## 5. Random pairing procedure

Generate exactly **100,000** independent realizations with replacement, using NumPy `default_rng(20260930)`. For each realization, permute the 20 numerically ordered session positions, pair adjacent positions, sort IDs inside each pair, then sort the ten pairs lexicographically. This permutation construction uniformly samples the **654,729,075** possible perfect matchings; it does not enumerate the entire space. Retain duplicate draws in all Monte Carlo summaries, and report unique count and duplicate fraction. Canonical text serialization uses `[(01,04),(05,13),...]`.

## 6. Statistics for every pairing

For all seven metrics, calculate the median of the ten `delta*` values, the number of clusters in the expected direction, and whether the median preserves that direction. Headline signs are −1 for Mean CC, +1 for Mean NRMSE, −1 for DET and −1 for LLE. For Lmean, LAM and TT, direction descriptions refer only to the sign of their observed n=20 median. An oriented effect counts as positive only when it is greater than `1e-12`; zero within this tolerance does not preserve direction.

The signed-rank test is always two-sided and exact, with `zero_method='wilcox'`: remove values satisfying `abs(delta*) <= 1e-12` (`rtol=0`), rank nonzero absolute values with average ranks for ties, calculate `W+` and `W−`, and enumerate all `2^n_eff` sign assignments conditional on those ranks. The p value is the fraction of assignments whose `min(W+,W−)` is no larger than observed. A vector with no nonzero values has p=1, `r_rb=NaN`, and an explicit flag. The matched-pairs rank-biserial correlation is `(W+−W−)/(W++W−)`. A vectorized exact n=10/no-tie path is cross-checked against the general enumerator at prespecified row indices; zero/tie rows use the general enumerator.

For **each** matching, apply monotone Benjamini–Hochberg correction jointly to its seven raw p values. Save `raw_p < 0.05` and `q_BH < 0.05` flags. Percentiles use NumPy's default linear interpolation. Report per-metric median-effect minimum, 2.5th, 25th, median, 75th, 97.5th and maximum; rank-biserial 2.5th/median/97.5th; raw-p and BH support fractions; direction-preservation fraction; full direction-count frequencies 0–10; and the descriptive ratio `abs(median delta*)/abs(original n=20 median delta)` with 2.5th/median/97.5th. No bootstrap is nested within random pairings. Random-pairing percentiles describe sensitivity over hypothetical matchings, not a confidence interval for a participant effect.

## 7. Robustness hierarchy

Interpret the four headline metrics first by expected direction, then magnitude, `r_rb`, cluster direction count, raw-p support, and finally BH support. Reduced statistical support with ten hypothetical units is not by itself evidence of an effect reversal. There is no post hoc composite robustness score or significance-only decision rule.

## 8. Convergence analysis

Use prefixes **1,000; 10,000; 50,000; 100,000** from the same fixed sequence. For each headline metric compare sign-preservation fraction, median and 2.5th/97.5th percentiles of the sampled median effect, median `r_rb`, and BH-support fraction. This is diagnostic; the final sample count stays 100,000 regardless of the prefix pattern.

## 9. Conservative pairing search

Only after the random experiment and convergence outputs are complete, search separately for each headline metric and each of four objectives: minimize (A) expected-sign × median effect, (B) expected-sign × `r_rb`, (C) expected-direction cluster count, or (D) negative exact two-sided p (equivalent to maximizing p). Objectives are never combined. For each objective, choose the 100 best **unique** sampled matchings, ranking by objective then lexicographic canonical matching. Starting from each, examine all 90 one-step neighbors formed by choosing two pairs and using either cross-repairing. Move to the best strictly improving neighbor (improvement greater than `1e-12`), using lexicographic matching order to break equal-score ties. Stop when none improves. Keep the best final matching across 100 starts, again breaking score ties lexicographically. Save all starts, endpoints, step counts and number of distinct local optima; for the retained matching, recompute all seven p values and its seven-metric BH q. The result is the **most conservative pairing found by the prespecified multi-start local search**, without a global optimality claim.

## 10. Reproducibility record

The frozen source/implementation hashes, canonical and baseline hashes, settings, UTC times, and final artifact hashes are in [`manifest.json`](manifest.json); [`protocol.json`](protocol.json) contains machine-readable method settings. This method file is sealed by SHA-256 before any random matching is generated. Implementation: Python 3.11.7, NumPy 2.4.6, pandas 3.0.3, SciPy 1.17.1 in the project `.venv`; run `run_analysis.py prepare`, write this method, `run_analysis.py seal`, then `run_analysis.py run`. Inputs and protocol are verified again immediately before sampling. Canonical floating values are written with 17 significant digits. The baseline comparison tolerance is `2e-8`; signed-rank zero tolerance and local-search improvement tolerance are `1e-12`.

Outputs are the canonical CSV, baseline CSV, gzipped random matching definitions and per-metric results, per-metric summary CSV, convergence CSV, adversarial best-found CSV, full adversarial starts CSV, this Method file, and the separate Results file. The final manifest hashes every output. Gzipped CSVs retain the entire fixed 100,000-draw sequence and all 700,000 metric evaluations.

## 11. Interpretation boundaries

A stable direction under many hypothetical matchings supports robustness of the **session-level finding to this specified reduction in effective independent units**. It cannot establish which matching is real, estimate the actual intraparticipant correlation, or confirm a participant-level effect. The local search probes more conservative configurations but does not quantify their real-world probability or prove a global extreme.
