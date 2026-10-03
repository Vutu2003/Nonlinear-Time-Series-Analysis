# Supplementary unresolved issues

## CRITICAL — I01: Choose the canonical Simplex estimand and propagate it consistently

Current manuscript anchors use B = mean_h(median_w), whereas the declared method uses A = median_w(mean_h). Existing frozen A is hash-verified and used by repeated-session and reconstruction analyses. The numerical cause is resolved, but the canonical editorial choice is not. Keep manuscript B anchors as targets until a human decision. If A is chosen, update primary tables, seven-metric BH, figures, tau/m nominal rows, label P0 baseline, interpretation and conclusion. If B is retained, state B in Methods and recompute compatible sensitivity baselines; do not call A legacy merely because it differs.

Source / provenance: `phase1/sensitivy_data/primary_simplex_windowfirst_v1/primary_simplex_statistics_60s_processed_P0_v1.csv; phase1/outputs/prediction/prediction_state_comparison_60s_processed.csv; phase1/sensitivy_data/reports/primary_simplex_windowfirst_resolution.md`.

## HIGH — I02: Recover missing nominal input data for reproducibility

The 20 processed dhdata CSVs are not present at the notebook input paths. Frozen manifests also reference 21 absent inputs: segments_index.csv and 20 segmented NPZs. Existing results and hashes can be audited, but raw integrity and expensive algorithms cannot be independently reproduced from this checkout. Obtain the exact files matching recorded hashes; do not substitute the different mydataset CSVs.

Source / provenance: `phase1/data_processed/dhdata/; phase1/segmentated_data/dhdata/; phase1/sensitivy_data/primary_simplex_windowfirst_v1/manifest.json`.

## HIGH — I03: Resolve PPS rho calibration provenance and boundary flags

For 60-s Processed rows, 200 windows from sessions 13/14/23/25 match the 5–600 grid and the other 701 windows match 5–200 (the shared endpoint 5 also fits both). Current notebook writes to an absent update directory. One session-23 rho=5 row is marked boundary_flag=False. Actual rho used is verified against saved window tests, but the producing calibration version and asserted absence of boundary optima need review. Recover the producer snapshot/full calibration curves or rerun only affected calibration after deciding the intended grid.

Source / provenance: `phase1/notebook/pps.ipynb; phase1/results/pps/pps_radius_calibration/csv/; phase1/agent/STEP6_PPS_Radius_Audti.md`.

## HIGH — I04: Correct or verify the 30-s QC claim

Existing 30-s windows are two halves of each retained 60-s parent (1802 total), not an independently segmented and variance-screened 30-s cohort. Review Methods and Supplementary wording. If independently screened 30-s windows are required, recover nominal inputs and compute that cohort; existing results describe the parent-gated analysis.

Source / provenance: `phase1/notebook/30s_window.ipynb; phase1/results/30s_window/`.

## HIGH — I05: Verify acquisition, participant and labeling metadata

Twenty recording sessions are verified, but the claim of 10 participants, acquisition demographics, sensor details and KSS/video labeling provenance cannot be established from supplied experimental metadata. Participant-session mapping remains unavailable. Obtain original study/acquisition and labeling records or explicitly identify these as manuscript claims; no participant-level inference is justified.

Source / provenance: `phase1/writting_manuscript/manuscript/methods_data_preprocessing_qc_version2_vi.tex; phase1/verification_result/verification_data/verification_data.ipynb`.

## MEDIUM — I06: Select and document the duration convention

Saved integrity audit uses support durations with capped gap intervals and final sample support; older data audit uses sample-count/nominal-fs durations. Manuscript Awake 11.33 h and Drowsy 6.07 h mix quantities relative to those audits. Select one convention and reconcile both state durations and total.

Source / provenance: `phase1/verification_result/verification_data/verification_data.ipynb; phase1/notebook/data_audit.ipynb`.

## MEDIUM — I07: Make window-length Simplex aggregation comparable

Saved 30-s robustness uses A, whereas 60/120/180-s summaries use B. If A is the approved estimand, the 60-s alternative already exists; 120/180 per-window horizon caches are absent and require recovery or a targeted Simplex computation. If B is approved, 30-s summaries need compatible aggregation. Current cross-duration table cannot establish estimator consistency.

Source / provenance: `phase1/main/robust_window.ipynb; phase1/outputs/robust_window/robust_window_summary.csv`.

## MEDIUM — I08: Export missing sensitivity inference only if required for publication

Lmean/LAM/TT windows exist for all duration and label settings, but same-framework median-session CI/p/r/q are not saved for secondary duration/label settings. RQA estimator sensitivity caches omit Lmean entirely. Tau/m inference and label CI tables are display-only, limiting precision. Recover notebook in-memory summaries or perform inexpensive session-level inference for available window metrics; Lmean estimator sensitivity would require metric computation. Do not substitute legacy mean-session inference.

Source / provenance: `phase1/results/rqa/verification/; phase1/results/ntsa_label_sensitive/; phase1/verification_result/verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb`.

## MEDIUM — I09: Document the RQA threshold version used for the nominal results

Nominal cached RQA uses the historical linear-quantile threshold. Current tie-safe core changes 55 session-12 windows slightly; saved nominal paired effects agree at displayed precision but window-level identity is not exact. Decide whether to freeze the historical algorithm in the Supplementary or propagate the current algorithm, including Lmean which is absent from current sensitivity caches.

Source / provenance: `phase1/src/rqa/rqa.py; phase1/results/rqa/rqa_window_level.csv; phase1/verification_result/verification_ntsa_parameter/verification_rqa.ipynb`.

## LOW — I10: Map publication figure assets and review final exports

Most manuscript image/ paths are not present at those locations, while source figures are saved under phase1/outputs. Resolve export paths and inspect final publication panels after the canonical decision; forecast and robustness figures may inherit B. No figure regeneration was done in this audit.

Source / provenance: `phase1/writting_manuscript/manuscript/results_version2_vi.tex; phase1/outputs/`.
