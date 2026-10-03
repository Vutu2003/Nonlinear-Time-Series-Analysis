# Final Supplementary source check — internal author record

The English version is authoritative for journal submission. The Vietnamese version is its complete parallel translation for author review. Paths below are relative to the research-project root; notebook indices are zero-based. This record is separate from publication prose.

Authority order: fixed manuscript → approved publication drafts → frozen content map → master evidence summary → saved outputs for transcription verification. No analysis notebook was executed. Checks compare saved text/results and typeset documents, rather than regenerating inference.

## A. Structural validation

| Check | English | Vietnamese | Status |
| --- | --- | --- | --- |
| Main sections | S1–S15, in the specified order | Identical sequence | PASS |
| S12 subsections | S12.1–S12.3 | Identical sequence | PASS |
| Tables | S1–S14, 14 unique table labels | Identical numbering/panels | PASS |
| Figures | S1–S10, 10 resolved PDF assets | Same assets/numbering | PASS |
| Display equations | 12; unnumbered because none is referenced by equation number | Identical mathematical expressions | PASS |
| Labels | 42 unique, resolved labels (18 section/subsection + 14 table + 10 figure) | 42 | PASS |
| Reference calls | 87; all resolve to the intended numbered object | 87 | PASS |
| Compilation | SUCCESS; 38 pages | SUCCESS; 38 pages | PASS |

Optional reconstruction Figure S9 was omitted because Table S10 already provides its complete evidence and exposes DET delay dependence. The former repeated-session Figure S10 is final Figure S9; the former symbolic Figure S11 is final Figure S10. All prose/caption references follow final numbering. No stale phase labels, production instructions, placeholders, internal issue IDs or Simplex aggregation discussion appears in publication content.

## B. Numerical validation

Every numerical table cell was compared with the corresponding approved Markdown table, preserving sign, decimal precision, CI endpoints, p/q/r values, numerator/denominator counts and scientific notation. The added Family column in Tables S9/S10 is editorial; it does not replace any statistic. Nominal publication rows remain those of Table S7. Method and interpretation details follow the approved sections and their existing provenance records. Saved outputs below identify the underlying evidence; no raw-signal re-audit is claimed.

### Table S1 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2A_draft.md`, Table S1. Integrated coverage: 21 rows in 1 panel(s).

All 20 session identifiers plus total row; n, sampling-rate display, Awake/Drowsy sample composition, gap count, integrity and eligibility. Total 1,620,038 samples and 69 gaps retained. State samples are not durations.

Underlying source locations:

- `phase1/verification_result/verification_data/verification_data.ipynb` — cell 8, output 1, session integrity table; output 3, row alignment.
- `phase1/writting_manuscript/supplementary/supplementary_results_master_summary.md` — §§2–3, dataset and segment summaries.

### Table S2 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2A_draft.md`, Table S2. Integrated coverage: 8 rows in 1 panel(s).

All 8 state–duration rows; post-SQI/gap counts, non-LLE final counts, LLE counts, literal numerator/denominator fractions and percentages. The 30-s inherited-QC cohort has no invented independent screening stage.

Underlying source locations:

- `phase1/notebook/data_segmentation.ipynb` — cell 9, saved retained-window summary.
- `phase1/outputs/lle/lle_qc_summary_60s_processed.csv` — All/Awake/Drowsy retained-fit rows.
- `phase1/writting_manuscript/supplementary/supplementary_results_master_summary.md` — §§4–5 and §9.5, post-QC and LLE-valid counts at all durations.

### Table S3 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2A_draft.md`, Table S3. Integrated coverage: 18 rows in 2 panel(s).

All 8 nominal configuration rows and 10 correction-family rows, including 60 s, τ=0.16 s, m=8, Simplex k=9/W=1.0 s/18 horizons, RQA RR=0.02 and LLE fit/QC thresholds.

Underlying source locations:

- `phase1/writting_manuscript/manuscript/methods_ntsa_statistics_version2_vi.tex` — reconstruction, Simplex, RQA, LLE, PPS and statistical-analysis subsections.
- `phase1/writting_manuscript/supplementary/supplementary_results_master_summary.md` — nominal configuration and correction-family summary.

### Table S4 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2A_draft.md`, Table S4. Integrated coverage: 8 rows in 3 panel(s).

All 2 AMI state rows, 3 dimension rows and 3 delay rows; counts, medians, Q25/Q75 and below-1% session counts. Quartiles remain descriptive, not CIs.

Underlying source locations:

- `phase1/outputs/phase_space/tables/ami_state_summary.csv` — state rows for delay median, quartiles and successes.
- `phase1/outputs/phase_space/tables/fnn_dimension_summary.csv` — dimensions 7–9.
- `phase1/verification_result/verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb` — cell 5, output 1, FNN delay diagnostic.

### Table S5 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2B_draft.md`, Table S5. Integrated coverage: 25 rows in 2 panel(s).

All 18 physical horizons and 25/50-Hz offsets; all 7 adjacent-setting calibration rows, change magnitudes, minimum support and selection descriptions. Scientific notation is retained for small nonzero changes.

Underlying source locations:

- `phase1/notebook/simplex_projection.ipynb` — HORIZON_SECONDS; cell 6, saved calibration rule.
- `phase1/results/simplex_projection/theiler_sensitive/processed_theiler_sensitivity_summary.csv` — seven adjacent-setting rows.

### Table S6 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2B_draft.md`, Table S6. Integrated coverage: 26 rows in 2 panel(s).

All 14 rejection rows and 12 session-gap rows; every count, percentage, median/IQR, gap, CI, raw p, q and r_rb. Distinguishes pooled fractions from session medians; retains the one opposite-direction Drowsy LAM rejection; no LLE session-gap CI/p/q added.

Underlying source locations:

- `phase1/outputs/statistic/rq1_pps_rank_rejection_summary_60s.csv` — 14 metric–state rows for rejection counts, percentages, medians, IQR and signs.
- `phase1/outputs/statistic/rq1_pps_primary_statistics_60s.csv` — 12 non-LLE metric–state rows for session gaps, CI, p, q and rank-biserial effects.
- `phase1/main/surrogate_testing.ipynb` — cells 1/7, saved session-gap definition and inference family.

### Table S7 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase2B_draft.md`, Table S7. Integrated coverage: 7 rows in 1 panel(s).

All 7 primary rows, including paired n, median Δ, CI, raw p, manuscript q and r_rb, and direction counts. All 28 effect/CI/r/q fields were also compared directly with the fixed manuscript table.

Underlying source locations:

- `phase1/writting_manuscript/manuscript/results_version2_vi.tex` — tab:awake_drowsy_statistics, all seven rows.
- `phase1/outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv` — seven primary metric rows; raw p and direction counts.

### Table S8 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S8. Integrated coverage: 16 rows in 1 panel(s).

All 16 metric–duration rows; metric-specific eligible state-window counts, paired n, Δ, CI, raw p, r_rb and direction counts. Retains DET CI-zero crossings at 30/180 s and raw p=0.053169 at 180 s. No q column or correction added.

Underlying source locations:

- `phase1/outputs/robust_window/robust_window_summary.csv` — four headline metrics × four durations, manuscript-approved saved series.
- `phase1/main/robust_window.ipynb` — cell 0, output 2, eligible-window coverage.

### Table S9 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S9. Integrated coverage: 25 rows in 2 panel(s).

All 5 retention rows (901/860/787/900/846) and 20 inference rows. n=20 except S5 (19). All CI/p/q/r/direction values retained. T60 CC [-0.0561,+0.0059] and T30 LLE [-0.0535,+0.0020] crossings remain explicit.

Underlying source locations:

- `phase1/results/data_label_sensitive/master_summary.csv` — alternative-rule effects and retained cohorts.
- `phase1/verification_result/verification_data/label_sensitive_validation.ipynb` — cell 8, output 0, exact BH4 inference; primary rows use Table S7.

### Table S10 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S10. Integrated coverage: 24 rows in 2 panel(s).

All 24 setting–metric rows, including 8 primary reference rows; every n, Δ, CI, raw p, q, r_rb and direction count. DET delay effects +0.0025/+0.0015 remain visible; dimension support variability is retained. No alternative nominal values substituted.

Underlying source locations:

- `phase1/verification_result/verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb` — cell 8, output 0, delay; cell 11, output 0, dimension; nominal rows use Table S7.

### Table S11 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S11. Integrated coverage: 26 rows in 2 panel(s).

All 18 RQA and 8 LLE rows; settings, state-window counts, paired n, Δ, CI, raw p, r_rb and direction counts. Every LLE median effect remains negative; passing totals 802/872/889, 734 and 874 retained. No q introduced.

Underlying source locations:

- `phase1/verification_result/verification_ntsa_parameter/verification_rqa.ipynb` — cell 6, outputs 6/8, RR/Theiler sensitivity.
- `phase1/verification_result/verification_ntsa_parameter/verification_lle.ipynb` — cell 5, outputs 1/3/5, fit interval, R² threshold and Theiler sensitivity; nominal publication values use Table S7.

### Table S12 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S12. Integrated coverage: 15 rows in 2 panel(s).

All 7 matching-distribution rows and 8 cumulative convergence rows; nominal sign, sign-preservation fraction, q-support fraction, median and 2.5th–97.5th matching percentiles. Headline support 19.36/27.82/22.59/79.69%; all four sign frequencies 100.00%. Ranges remain matching distributions, not bootstrap CIs.

Underlying source locations:

- `phase1/sensitivy_data/unknown_repeated_session_dependence_v1/random_pairing_summary_v1.csv` — seven metric rows, sign preservation, q-support and matching-effect percentiles.
- `phase1/sensitivy_data/unknown_repeated_session_dependence_v1/convergence_v1.csv` — 50k/100k cumulative rows; 1k/10k additionally used in Figure S9.
- `phase1/sensitivy_data/unknown_repeated_session_dependence_v1/protocol.json` — matching design and within-pair arithmetic mean.
- `phase1/sensitivy_data/unknown_repeated_session_dependence_v1/manifest.json` — sampled/unique/theoretical matching counts.

### Table S13 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S13. Integrated coverage: 9 rows in 1 panel(s).

All 9 category–duration rows, including paired n, percentage-point Δ/CI, raw p, within-duration q, r_rb and direction counts. All nine lack BH support; same-sign counts 17/20, 11/20 and 14/20 retained. The positive reporting convention for 1V direction counts is stated.

Underlying source locations:

- `phase1/outputs/symbolic/60/symbolic_state_comparison_60s.csv` — 0V/1V/2V rows at 60 s.
- `phase1/outputs/symbolic/120/symbolic_state_comparison_120s.csv` — 0V/1V/2V rows at 120 s.
- `phase1/outputs/symbolic/180/symbolic_state_comparison_180s.csv` — 0V/1V/2V rows at 180 s.
- `phase1/main/symbolic_main.ipynb` — cell 18, output 1, cross-duration same-sign counts.

### Table S14 — PASS

Approved transcription source: `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md`, Table S14. Integrated coverage: 5 rows in 1 panel(s).

All 5 qualitative rows and all 8 columns. Direction, uncertainty, support, DET delay dependence, fit/QC cohort changes, exploratory symbolic status and unresolved participant linkage retained. No pooled test or robustness score.

Underlying source locations:

- `phase1/writting_manuscript/supplementary/supplementary_phase3_draft.md` — Table S14; qualitative synthesis of Tables S7–S13.
- `phase1/writting_manuscript/manuscript/results_version2_vi.tex` — robustness synthesis and interpretation limits.

Precision policy: manuscript rounding in Table S7 and all reference rows is unchanged. Sensitivity raw p/q and estimator perturbation values retain their approved higher precision. No new scientific rounding, CI, p or q was generated. Typesetting small values as powers of ten changes notation only.

## C. Manuscript consistency

Publication reference files:

- `phase1/writting_manuscript/manuscript/results_version2_vi.tex`.
- `phase1/writting_manuscript/manuscript/methods_ntsa_statistics_version2_vi.tex`.
- `phase1/writting_manuscript/manuscript/methods_data_preprocessing_qc_version2_vi.tex`.

| Repeated manuscript content | Check | Status |
| --- | --- | --- |
| Dataset and labeling | 20 recording sessions; 10 participants; 17.40/11.33/6.07 h; KSS with video cross-check; unavailable participant–session linkage. No new demographic, KSS-threshold or video detail added. | PASS |
| QC and reconstruction | Filter/QC thresholds, nominal 60 s, τ=0.16 s, m=8 and metric-specific settings preserve approved methods. Parent-gated 30-s detail follows the approved Supplementary without replacing manuscript window reporting. | PASS |
| Simplex reporting | Whole-window normalization, horizon averaging within windows followed by session-state medians, 18 horizons, W=1.0 s; fixed Mean CC/Mean NRMSE results. | PASS |
| Primary statistics | 28 manuscript effect/CI/r/q fields, compared directly for all seven metrics; raw p and counts additionally match approved Table S7. | PASS |
| Label effects | 20 manuscript table effects compared directly; paired-session retention and the two CI-zero crossings preserved. | PASS |
| Reconstruction effects | 24 manuscript table effects compared directly, including DET sign reversal at both non-nominal delays. | PASS |
| Hypothetical dependence | Four manuscript q-support frequencies compared directly; all-four sign preservation retained; no participant recovery claimed. | PASS |
| Symbolic evidence | Nine manuscript table effects and three same-sign counts compared directly; exploratory qualification retained. | PASS |
| Window reporting/conclusions | Fixed manuscript directions, changing magnitudes/uncertainty, relatively wide 180-s DET interval and practical 60-s configuration preserved; all 16 saved numeric rows match approved Table S8. | PASS |

No manuscript inconsistency was found. SHA-256 comparison confirms all 23 pre-existing manuscript/Supplementary files captured before integration remain unchanged; hashes are retained in `qa/preexisting_file_hashes.json`.

## D. Statistical-family validation

| Analysis | Family / presentation | Location | Status |
| --- | --- | --- | --- |
| Primary 60-s | BH7 across seven metrics once | S9; Table S7 | PASS |
| Primary reference rows | Original BH7 q, explicitly labeled and bold in Family column | P0 in Table S9; τ=0.16/m=8 in Table S10 | PASS |
| Alternative labels | BH4 separately within T30/T60/S3/S5 | S11; Table S9 | PASS |
| Alternative reconstruction | BH4 separately within each delay/dimension setting | S12.1; Table S10 | PASS |
| Window lengths | Raw p only; no q calculated | S10; Table S8 | PASS |
| RQA RR/Theiler | Raw p only | S12.2; Table S11A | PASS |
| LLE estimator settings | Raw p only; no BH across settings | S12.3; Table S11B | PASS |
| PPS window tests | Unadjusted, tie-inclusive, two-sided rank p≤0.05; M=39 | S8; Table S6A | PASS |
| PPS session gaps | BH12, six non-LLE metrics × two states | S8; Table S6B | PASS |
| Hypothetical matching | BH7 within each matching; support fractions and matching-distribution percentiles | S13; Table S12 | PASS |
| Symbolic | BH3 separately within each duration; no nine-test support | S14; Table S13 | PASS |

Correction families are never pooled across settings, metrics from separate analyses or hypothetical draws. Signed-rank support and percentile median-effect CIs remain distinct. Non-significant primary secondary-metric, RR=0.01 DET, dimension-sensitive DET, window-dependent DET and all symbolic results are retained.

## E. Interpretation validation

| Interpretation boundary | Publication treatment | Status |
| --- | --- | --- |
| Simplex | Finite-horizon forecastability; no chaos scale | PASS |
| RQA / DET | Recurrence geometry and diagonal recurrence-line organization; no physical-determinism equivalence | PASS |
| LLE | Finite-window local trajectory divergence; no proof of deterministic chaos | PASS |
| PPS | Departure from the tested noisy pseudoperiodic null; does not exclude every stochastic/structured pseudoperiodic model | PASS |
| Sensitivities | Supportive reuse of the same recordings; direction, magnitude, CI and support distinguished; no independent replication | PASS |
| DET reconstruction | Explicit near-zero positive effects at τ=0.12/0.20 s; no uniform delay-stability claim | PASS |
| Repeated-session grouping | Hypothetical matching design only; frequencies are not probabilities of true significance; no participant mapping or participant-level inference | PASS |
| Unknown linkage | Explicit in S1, cross-referenced in S13, retained in synthesis | PASS |
| Symbolic categories | Exploratory PPI occurrence proportions; no direct sympathetic/vagal interpretation; all 1V results retained | PASS |
| Overall synthesis | No pooled significance, robustness score, absolute robustness claim or best-metric ranking | PASS |

## F. English–Vietnamese parity

The English scientific text and table data were frozen before full translation. Both versions were checked as 117 parallel content nodes, including every section, paragraph, equation, table and caption. Translation covers prose, table headings/cells/notes and captions; standard technical terms and the shared scientific figure axes remain in English where appropriate.

| Automated check | Coverage / result |
| --- | --- |
| Parallel content blocks | 2,086 comparisons including table cells, headers, panel names and notes |
| Table cells | 1,760 EN–VI cell pairs |
| Ordered numerical tokens | 2,401 compared tokens; signs, scientific exponents, CIs, p/q/r, counts, durations and thresholds included |
| Display equations | 12 identical expressions |
| Inline mathematics | 202 compared expressions |
| Metric names | Identical ordered technical metric/category tokens in every corresponding block |
| Labels / references | Same label keys, reference keys and intended numbers; all resolved in both PDFs |
| Whole-source numeric sequence | Identical ordered numerical sequences for both complete Markdown files and both complete TeX files |
| Mismatches | **0** |

Vietnamese wording was reviewed for the same directions, negation, cohort changes, inferential limits and explanatory scope. It is a full translation rather than a simplified summary. Numeric and structural parity is automatic; semantic review is editorial, not an automated proof of translation quality.

## G. Compilation and visual QA

Both standalone files compiled successfully with Tectonic 0.17.0 (XeTeX/xdvipdfmx), using repeated passes when reference files changed. Bundled Noto Serif/Sans fonts support all Vietnamese characters; `fonts/FONT_LICENSE.txt` accompanies them. Tables use booktabs rules and 10-pt text; wide tables use landscape longtables with clean panel breaks and repeated headers. No resizebox was used. Figure captions stay with their panels.

| QA check | English | Vietnamese |
| --- | --- | --- |
| Compilation errors | 0 | 0 |
| Undefined references | 0 | 0 |
| Duplicate labels/destinations | 0 | 0 |
| Overfull boxes / equation overflow | 0 | 0 |
| Missing glyphs/assets | 0 | 0 |
| Extracted text outside page bounds | 0 | 0 |
| Blank pages | 0 | 0 |
| PDF pages | 38 | 38 |

Page contact sheets and selected full-size table/figure pages were inspected for clipping, panel readability, equation overflow, Vietnamese glyphs, table continuation headers and caption placement. Source vector axes/data remain intact. The broad qualitative matrix and explicit statistical-family columns remain readable at normal page size.

Non-blocking notices: English has one underfull hbox (badness 1275, S10 prose at TeX lines 454–455), without overflow or clipping; Vietnamese has none. Tectonic also notes that four assembled vector inputs declare PDF 1.7 while its output default is PDF 1.5. All four are included and render correctly in both PDFs; these version notices are retained in the console logs (eight EN notices over two passes; four in the final VI pass). No unresolved compilation error is present.

Machine-readable validation, figure provenance, original-file hashes and compilation records are in `qa/`. No remaining scientific wording or numerical decision is identified. Routine final author approval of prose/translation and any journal-specific submission-format adjustment remain normal human review, rather than a scientific blocker.

**Final gate:** PASS. No experiment was rerun. No inferential statistic was recomputed. No manuscript-fixed result was changed. Only editorial integration, translation, saved-result visualization, vector-panel assembly and typesetting/validation were performed.
