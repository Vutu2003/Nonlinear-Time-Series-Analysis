# Final Supplementary change log — editorial integration

The English document is the authoritative submission version; Vietnamese is a complete author-review translation. Changes below are editorial and presentational. The manuscript and approved source documents remain unchanged.

## Document integration

- Joined S1–S15 into a single continuous document with the specified S12.1–S12.3 subsections. Removed stage headings, draft notes, placeholder lists and production directions.
- Consolidated QC definitions in S2, nominal configurations/families in S3 and paired-effect/CI/rank-test definitions in S9. Later sections use cross-references while retaining branch-specific qualifications.
- Kept all unique reviewer-useful tables and all selected non-significant results. Preserved explicit DET delay sensitivity, the two label CI-zero crossings, the hypothetical grouping limit and exploratory symbolic framing.
- Harmonized metric names to Mean CC, Mean NRMSE, DET, L_mean, LAM, TT and LLE. L_mean, r_rb, q_BH, τ, R² and units use consistent mathematical typography.
- Harmonized the Rosenstein mean-log-distance curve symbol to D(t), matching the existing fit figure. Its expression and estimator are unchanged.
- Retained approved display precision: manuscript primary/reference rounding, more precise stored sensitivity p/q and estimator perturbation values, and two-decimal symbolic effects. No new scientific rounding was applied.

## Table and LaTeX presentation

- Retained Tables S1–S14 and their panel structure. Added an explicit Family column to Tables S9/S10, with primary BH7 reference labels in bold and separate Sensitivity BH4 labels. Removed dagger-only reference markers after replacing them with these labels.
- Converted wide tables to landscape longtables with 10-pt type, booktabs rules, repeated continuation headers and clean panel page breaks. Table S9 retention remains portrait; its inference panel is landscape. No table was scaled with resizebox.
- Used a conservative standalone A4 article layout with 20-mm margins, bundled Noto fonts and Vietnamese-compatible Unicode typesetting. Existing project files did not provide a compatible complete Elsevier class/preamble to reuse.
- Replaced hard-coded prose references with labeled section/table/figure references. Added distinct panel hyperlink anchors so multi-panel table numbering does not create duplicate PDF destinations.
- Kept display equations unnumbered because none is cited by equation number. Split paired displayed definitions across lines where needed, preserving their mathematics.
- Replaced figure placeholders with final vector-PDF includes and complete captions. Figures S2/S9 use landscape pages for readable multi-panel content.

## Figure selection and assembly

The optional reconstruction Figure S9 was omitted because Table S10 already provides the effects, CIs, inference families and visible DET delay dependence. Repeated-session and symbolic figures were renumbered to final S9 and S10. Final numbering is continuous S1–S10.

### Figure S1

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S01.pdf`. Production: Vector assembly plus saved-count plot.

Filtering axes/data preserved; counts transcribed from approved Table S2. Optional pre-QC availability panel omitted for focus.

Exact source list:

- `phase1/outputs/data_audit/preprocessing/ppg_before_after_filtering.pdf`.
- `phase1/writting_manuscript/supplementary/supplementary_phase2A_draft.md, Table S2`.

### Figure S2

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S02.pdf`. Production: Vector assembly.

Three original panels retained, with external panel/state labels; landscape presentation.

Exact source list:

- `phase1/outputs/phase_space/figures/phase_space_ami_60s_processed.pdf`.
- `phase1/outputs/phase_space/figures/phase_space_fnn_60s_processed_awake.pdf`.
- `phase1/outputs/phase_space/figures/phase_space_fnn_60s_processed_drowsy.pdf`.

### Figure S3

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S03.pdf`. Production: Unmodified PDF copy.

Original axes, numerical data, and panel typography preserved.

Exact source list:

- `phase1/outputs/prediction/prediction_horizon_60s_processed.pdf`.

### Figure S4

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S04.pdf`. Production: Unmodified PDF copy.

Original axes, numerical data, and panel typography preserved.

Exact source list:

- `phase1/outputs/rqa/recurrence_plot_session_1_60s_processed.pdf`.

### Figure S5

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S05.pdf`. Production: Unmodified PDF copy.

Original axes, numerical data, and panel typography preserved.

Exact source list:

- `phase1/outputs/lle/lle_session_1_60s_processed_awake_window_1.pdf`.

### Figure S6

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S06.pdf`. Production: Vector assembly.

PPS 15-s illustrative view above heatmaps; heatmap letters changed to B/C. No surrogate regenerated and no rejection data altered.

Exact source list:

- `phase1/outputs/pps/pps_visual_sanity_check_session_01_60s_window_0_15s_processed.pdf`.
- `phase1/outputs/statistic/rq1_pps_rank_rejection_heatmap_60s.pdf`.

### Figure S7

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S07.pdf`. Production: Unmodified PDF copy.

Original axes, numerical data, and panel typography preserved.

Exact source list:

- `phase1/outputs/robust_window/robust_window_primary_metrics.pdf`.

### Figure S8

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S08.pdf`. Production: Plot of approved stored summaries.

Retention and four-metric effects/CIs transcribed from approved Tables S7/S9; no testing or CI computation.

Exact source list:

- `phase1/results/data_label_sensitive/master_summary.csv`.
- `phase1/verification_result/verification_data/label_sensitive_validation.ipynb, cell 8/output 0`.
- `phase1/writting_manuscript/supplementary/supplementary_phase2B_draft.md, Table S7`.

### Figure S9

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S09.pdf`. Production: Plot of saved matching summaries.

Final figure formerly S10; percentages are display conversions of saved fractions. No matching sampled, no inference recomputed, no bootstrap CI plotted.

Exact source list:

- `phase1/sensitivy_data/unknown_repeated_session_dependence_v1/random_pairing_summary_v1.csv`.
- `phase1/sensitivy_data/unknown_repeated_session_dependence_v1/convergence_v1.csv`.

### Figure S10

Asset: `phase1/writting_manuscript/supplementary/final/figures/figure_S10.pdf`. Production: Vector assembly.

Final figure formerly S11. Original paired state axes/data preserved; repeated source letters removed and duration letters A/B/C added.

Exact source list:

- `phase1/outputs/symbolic/60/symbolic_0V_2V_state_60s.pdf`.
- `phase1/outputs/symbolic/120/symbolic_0V_2V_state_120s.pdf`.
- `phase1/outputs/symbolic/180/symbolic_0V_2V_state_180s.pdf`.

For vector assemblies, source axes and numerical plot content were preserved; only external panel/state/duration labels and panel lettering were harmonized. New count/effect/convergence panels visualize approved stored summaries. They contain no new model fits, tests, resampling or generated CIs.

## Vietnamese translation

- Translated frozen English prose, section titles, table labels/headings/textual cells/notes and figure captions into academic Vietnamese. Standard metric/method names and the shared figure axes remain in English where useful.
- Shared equations, numbers, scientific symbols, counts, labels and references were preserved. The full parallel translation has zero quantitative, equation, metric-token or reference mismatches in the recorded parity check.

## Final presentation check

Both PDFs compile to 38 pages with resolved references and no overfull boxes, missing glyphs/assets, duplicate destinations or extracted text beyond page bounds. The source-check document records the minor non-blocking typesetting/version notices and review scope. No remaining core wording decision is open.
