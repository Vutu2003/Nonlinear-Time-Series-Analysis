# Supplementary Material — Phase 2A

## S1. Dataset, labeling, and data integrity

The analysis included 20 recording sessions from 10 participants, as reported in the manuscript. The retained recordings totaled 17.40 h: 11.33 h Awake and 6.07 h Drowsy. Awake/Drowsy labels were assigned using the Karolinska Sleepiness Scale (KSS), with video observation used for cross-checking. Participant–session linkage was unavailable. Primary inference therefore used recording sessions, and the results do not establish participant-level effects.

The saved data contained 1,620,038 samples. Session 01 was sampled at 50 Hz; the remaining sessions were sampled at approximately 25 Hz. Sampling rates were estimated as the reciprocal of the median positive timestamp interval. The saved integrity checks found strictly increasing timestamps, no duplicated timestamps, no invalid labels, and no missing, non-numeric, or infinite signal or time values. Raw PPG, processed PPG, and labels were aligned on the same row axis. All 20 sessions passed the recorded integrity and analysis-eligibility checks (Table S1).

There were 69 temporal gaps exceeding 1.5 times the session median sampling interval; 62 exceeded twice that interval, and none exceeded five times that interval. Gaps were retained as discontinuities without interpolation. The recorded labels contained 86 observed state transitions, with none occurring across a temporal gap. Splitting at state changes and temporal gaps yielded 175 contiguous state segments: 93 Awake and 82 Drowsy. The median segment duration was approximately 260.04 s. Of these segments, 60 were shorter than 60 s, 78 were shorter than 180 s, and 94 were shorter than 300 s.

**Table S1 (TS01).** Dataset and integrity summary. State composition is reported as saved sample counts.

| Session | Samples | Estimated fs (Hz) | Awake / Drowsy samples | Gaps | Integrity | Analysis eligible |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 117,828 | 50.000 | 77,805 / 40,023 | 0 | Pass | Yes |
| 04 | 75,416 | 24.992 | 46,897 / 28,519 | 3 | Pass | Yes |
| 05 | 91,211 | 25.003 | 59,235 / 31,976 | 4 | Pass | Yes |
| 06 | 79,179 | 24.993 | 51,240 / 27,939 | 5 | Pass | Yes |
| 07 | 79,768 | 24.994 | 59,225 / 20,543 | 3 | Pass | Yes |
| 08 | 77,595 | 24.994 | 61,405 / 16,190 | 4 | Pass | Yes |
| 09 | 119,272 | 25.001 | 83,631 / 35,641 | 8 | Pass | Yes |
| 10 | 60,386 | 24.998 | 45,365 / 15,021 | 3 | Pass | Yes |
| 11 | 61,582 | 24.994 | 33,062 / 28,520 | 2 | Pass | Yes |
| 12 | 89,853 | 24.989 | 34,376 / 55,477 | 2 | Pass | Yes |
| 13 | 76,473 | 25.000 | 40,272 / 36,201 | 2 | Pass | Yes |
| 14 | 85,948 | 24.994 | 54,871 / 31,077 | 5 | Pass | Yes |
| 15 | 69,362 | 24.996 | 54,511 / 14,851 | 6 | Pass | Yes |
| 17 | 68,752 | 24.993 | 45,601 / 23,151 | 2 | Pass | Yes |
| 18 | 69,937 | 24.997 | 30,634 / 39,303 | 3 | Pass | Yes |
| 19 | 73,041 | 24.996 | 54,123 / 18,918 | 4 | Pass | Yes |
| 21 | 69,660 | 25.000 | 41,549 / 28,111 | 2 | Pass | Yes |
| 22 | 74,710 | 25.001 | 50,359 / 24,351 | 3 | Pass | Yes |
| 23 | 109,452 | 24.997 | 87,703 / 21,749 | 3 | Pass | Yes |
| 25 | 70,613 | 24.996 | 46,905 / 23,708 | 5 | Pass | Yes |
| Total | 1,620,038 | Mixed | 1,058,769 / 561,269 | 69 | 20/20 | 20/20 |

Awake/Drowsy composition is a sample count, not a duration estimate. Gap counts use the >1.5 × median timestamp-interval threshold. Integrity and eligibility refer to the saved session checks; eligibility does not mean that every sample entered a retained analysis window.

*Duration note.* State-duration support in the saved integrity summaries was computed from sample-associated intervals, with gaps capped at the median sampling interval and the final sample assigned one median interval; the recording-duration totals in the text follow the manuscript.

## S2. Preprocessing, quality control, and retained-window counts

Raw PPG was multiplied by −1 before filtering. A second-order Butterworth band-pass filter (0.5–8 Hz) was then applied forward and backward to obtain zero-phase processed PPG. All subsequent quality control and nonlinear analyses used processed PPG.

Artifact screening used complete, non-overlapping 5-s blocks over each recording session, with block length round(5 fs) samples. For each block, amplitude and roughness were defined as

\[A=Q_{0.95}(x)-Q_{0.05}(x),\qquad R=\sqrt{\mathrm{mean}((\Delta x)^2)}.\]

Here, Qp denotes the pth quantile, and Δx is the first difference. Each feature F ∈ {A, R} was standardized across the complete blocks within the same session:

\[z_F=0.6745\,\frac{F-\mathrm{median}(F)}{\max(\mathrm{MAD}(F),\epsilon)}.\]

MAD(F) = median(|F − median(F)|), and ε is machine epsilon. A block was flagged when zA > 4.5 or zR > 4.5. All samples in a flagged block were marked, and any analysis window containing a marked sample was excluded. A trailing incomplete 5-s block was not screened.

Within each same-state run, complete 60-s windows were placed without overlap using round(60 fs) samples per window. Incomplete tails were discarded. Windows crossing a state boundary were not formed, and candidates containing a timestamp interval greater than 1.5/fs were excluded. This preserved state and gap boundaries in the retained windows. Gap rejection left the subsequent window positions anchored to the original state run. The same procedure was used for 120- and 180-s windows.

Each window that passed artifact and gap screening was assessed for variance stability using complete, non-overlapping 10-s subwindows of round(10 fs) samples. At least two complete subwindows were required. With vk = Var(xk), computed using ddof = 0, the variance-stability index was

\[S=\frac{\mathrm{IQR}(v)}{\max(\mathrm{median}(v),\epsilon)},\qquad \mathrm{IQR}(v)=Q_{0.75}(v)-Q_{0.25}(v).\]

Windows were accepted when S ≤ 0.5. This was a variance-stability screen for local quasi-stationarity; it did not establish full stationarity.

At 60 s, 623 Awake and 328 Drowsy windows passed artifact and gap screening. Variance screening retained 596 Awake and 305 Drowsy windows, giving 901 windows in total. The corresponding final counts were 269 Awake and 136 Drowsy at 120 s (405 total), and 161 Awake and 77 Drowsy at 180 s (238 total). The 30-s cohort was constructed by dividing each accepted 60-s parent window into two consecutive halves. These halves inherited parent-level QC and were not independently variance-screened, yielding 1,192 Awake and 610 Drowsy windows (1,802 total).

LLE fit acceptance was applied separately from general QC (Table S2). It retained 1,089 Awake and 549 Drowsy windows at 30 s; 579 and 293 at 60 s; 264 and 135 at 120 s; and 160 and 77 at 180 s. Nominal 60-s LLE retention was 872/901 (96.78%).

**Table S2 (TS02).** Quality-control stages and metric-specific retention by window duration and state.

| Duration (s) | State | Post-SQI/gap | Variance-pass / final non-LLE | LLE-valid | Variance-pass fraction | LLE-pass fraction |
| --- | --- | --- | --- | --- | --- | --- |
| 30 | Awake | Not applicable | 1,192 | 1,089 | Not applicable | 1089/1192 (91.36%) |
| 30 | Drowsy | Not applicable | 610 | 549 | Not applicable | 549/610 (90.00%) |
| 60 | Awake | 623 | 596 | 579 | 596/623 (95.67%) | 579/596 (97.15%) |
| 60 | Drowsy | 328 | 305 | 293 | 305/328 (92.99%) | 293/305 (96.07%) |
| 120 | Awake | 284 | 269 | 264 | 269/284 (94.72%) | 264/269 (98.14%) |
| 120 | Drowsy | 148 | 136 | 135 | 136/148 (91.89%) | 135/136 (99.26%) |
| 180 | Awake | 168 | 161 | 160 | 161/168 (95.83%) | 160/161 (99.38%) |
| 180 | Drowsy | 86 | 77 | 77 | 77/86 (89.53%) | 77/77 (100.00%) |

The variance-pass fraction is the final non-LLE count divided by the post-SQI/gap count; the LLE-pass fraction is the LLE-valid count divided by the final non-LLE count. SQI denotes the signal-quality screening based on amplitude and roughness. At 30 s, separate post-SQI/gap and variance-pass stages are not applicable because QC is inherited from accepted 60-s parents; the final non-LLE count reports the resulting cohort. Counts at different durations share source data.

### Figure S1 (FS01) — placeholder

**Intended panels:** (A) Before/after filtering; (B) potential state-specific window availability by session and duration; (C) final non-LLE and LLE-valid counts from Table S2. Combine existing panels A–B; compose C from saved counts during figure production.

**Exact existing sources (project-relative):**

- A: `phase1/outputs/data_audit/preprocessing/ppg_before_after_filtering.pdf`.
- B: `phase1/outputs/data_audit/figures/session_availability_by_window_duration.pdf`.
- C, 60/120/180-s QC counts: `phase1/notebook/data_segmentation.ipynb` (cell 9, final retention tables).
- C, 30-s counts: `phase1/notebook/30s_window.ipynb` (cells 0 and 2, input/method summaries).
- C, LLE counts: `phase1/writting_manuscript/supplementary/supplementary_results_master_summary.md` (§5, retained counts).

**Draft publication caption.** Preprocessing and retained-data illustration. (A) PPG before and after the 0.5–8 Hz zero-phase Butterworth filter; the pre-filter trace is sign-inverted raw PPG. (B) Recording-session availability for complete state-specific windows at the indicated durations, before final QC. (C) Retained-window counts by state and duration, with separate LLE-valid counts. The 30-s windows are consecutive halves of accepted 60-s windows and inherit parent-level QC.

## S3. Frozen nominal analysis configuration

Table S3 specifies the nominal 60-s configuration and the statistical families used in the study. The common embedding was fixed for both states. Windows were the computational units, and recording sessions were the primary inferential units.

**Table S3 (TS03).** Nominal analysis configuration and statistical correction families.

**Panel A. Nominal estimator configuration**

| Component | Configuration |
| --- | --- |
| Input and windowing | Processed PPG; 60-s non-overlapping windows; 596 Awake + 305 Drowsy = 901. |
| Embedding | $\tau=0.16$ s; $m=8$; $\tau_{\mathrm{samples}}=\mathrm{round}(\tau f_s)$ (4/8 samples at 25/50 Hz). |
| Simplex Projection | $k=m+1=9$; Euclidean distance; normalized exponential weights; leave-one-out prediction; temporal exclusion $W=1.0$ s; 18 physical-time horizons from 0.04 to 4.00 s, converted using $\mathrm{round}(T_p f_s)$. Mean CC and Mean NRMSE are the means over horizons within each window. |
| RQA | Euclidean distance; per-window threshold targeting $\mathrm{RR}=0.02$; exclusion $W=(m-1)\tau_{\mathrm{samples}}$; $l_{\min}=v_{\min}=2$. Outputs: DET, $L_{\mathrm{mean}}$, LAM, TT. DET describes diagonal recurrence-line organization. |
| Rosenstein LLE | Nearest admissible Euclidean neighbor; spectral-mean-period temporal exclusion; maximum follow time 5 s; fit interval 0.80–1.30 s; ≥50 initial pairs; ≥30 pairs per fit point; ≥3 fit points; finite fit; $R^2\geq0.90$. Units: s$^{-1}$. |
| PPS | $M=39$ surrogates per tested window; tested noisy pseudoperiodic null; two-sided finite-sample rank test. |
| Aggregation and effects | Session-state medians of valid window metrics; paired $\Delta_i=\mathrm{Drowsy}_i-\mathrm{Awake}_i$; report the median paired difference. Simplex aggregation follows the within-window horizon means above. |
| Primary statistics | Two-sided Wilcoxon signed-rank test; matched-pairs rank-biserial correlation; 20,000 paired-session bootstrap resamples; percentile 95% CI for the median paired difference; BH-FDR once across the seven nominal 60-s metrics. |

**Panel B. Statistical families**

| Analysis family | Multiplicity reporting |
| --- | --- |
| Primary RQ2 | BH across 7 nominal 60-s metrics, once |
| Label sensitivity | BH across 4 headline metrics within each alternative rule |
| Delay/dimension sensitivity | BH across 4 headline metrics within each setting |
| RQA RR/Theiler sensitivity | Raw p only |
| LLE sensitivity | Raw p only |
| Window-length robustness | Raw p only |
| Repeated-session sensitivity | BH across 7 metrics per hypothetical matching |
| Symbolic dynamics | BH across 3 metrics per duration |
| PPS window-level rank tests | Unadjusted |
| PPS session-level gap family | BH across 12 tests: 6 metrics × 2 states |

BH denotes Benjamini–Hochberg FDR adjustment. The seven nominal metrics are Mean CC, Mean NRMSE, DET, Lmean, LAM, TT, and LLE. The four headline metrics are Mean CC, Mean NRMSE, DET, and LLE. The PPS session-level gap family contains the six non-LLE metrics in each state. Setting-specific families are not pooled across settings.

## S4. Phase-space reconstruction: AMI and FNN

Average Mutual Information (AMI) was computed separately for each processed 60-s window using KSG estimator 1 with k = 3, Chebyshev distance in joint space, and natural-log units (nats). Candidate delays ranged from one sample to round(fs × 1.0 s) samples. The selected delay was the first strict interior local minimum; no endpoint fallback was used. All 901 nominal windows yielded a selected delay (Table S4A).

The median selected delay was approximately 0.160 s for Awake windows (Q25–Q75: 0.120–0.260 s) and 0.120 s for Drowsy windows (0.120–0.160 s). The median of the 20 session medians supported the operational common delay τ = 0.16 s; 14/20 session medians lay within 0.16 ± 0.04 s. The same delay was used for both states, without optimizing it for a state contrast. It was not treated as a universal or state-specific optimum.

False Nearest Neighbors (FNN) were evaluated over dimensions 1–10 using Euclidean nearest neighbors and Kennel-style criteria. A neighbor was classified as false when the additional-coordinate separation divided by the m-dimensional distance Rm exceeded 15, or when the full (m + 1)-dimensional distance divided by the signal standard deviation exceeded 2. Self-matches and zero or near-zero distances were excluded; no temporal exclusion was applied in this diagnostic.

For the nominal delay, median FNN across the 20 session curves was 0.900% at m = 7, 0.886% at m = 8, and 1.008% at m = 9 (Table S4B). The common dimension m = 8 was selected from this low-FNN plateau. At m = 8, the median FNN was 0.593%, 0.886%, and 1.284% for delays of 0.12, 0.16, and 0.20 s, respectively; 19/20, 11/20, and 7/20 session curves were below 1% (Table S4C). Thus, the nominal choice did not require every session to satisfy FNN < 1%, and m = 8 was not a uniquely optimal dimension. These reconstruction diagnostics provide descriptive support for a common operational embedding; they are not inferential evidence of chaos.

**Table S4 (TS04).** AMI and FNN evidence supporting the common reconstruction parameters.

**Panel A. AMI-selected delays**

| State | Windows | Median τ (s) | Q25 (s) | Q75 (s) | Successful selections |
| --- | --- | --- | --- | --- | --- |
| Awake | 596 | 0.160 | 0.120 | 0.260 | 596/596 |
| Drowsy | 305 | 0.120 | 0.120 | 0.160 | 305/305 |

**Panel B. FNN by dimension at τ = 0.16 s**

| Dimension | Median FNN (%) | Q25 (%) | Q75 (%) |
| --- | --- | --- | --- |
| 7 | 0.900 | 0.679 | 1.155 |
| 8 | 0.886 | 0.613 | 1.132 |
| 9 | 1.008 | 0.666 | 1.298 |

**Panel C. Delay sensitivity at m = 8**

| τ (s) | Median FNN (%) | Session curves <1% |
| --- | --- | --- |
| 0.12 | 0.593 | 19/20 |
| 0.16 | 0.886 | 11/20 |
| 0.20 | 1.284 | 7/20 |

Panel A summarizes selected delays across windows within each state; success is selected-delay count/eligible-window count. Panels B and C summarize session curves formed by taking median FNN across windows at each dimension within each session. Medians and quartiles are then taken across 20 sessions; the <1% count is a session count. FNN values are percentages, not proportions.

### Figure S2 (FS02) — placeholder

**Intended panels:** (A) AMI-selected delay evidence; (B) Awake FNN curves; (C) Drowsy FNN curves. Combine the three existing source panels.

**Exact existing sources (project-relative):**

- A: `phase1/outputs/phase_space/figures/phase_space_ami_60s_processed.pdf`.
- B: `phase1/outputs/phase_space/figures/phase_space_fnn_60s_processed_awake.pdf`.
- C: `phase1/outputs/phase_space/figures/phase_space_fnn_60s_processed_drowsy.pdf`.

**Draft publication caption.** Phase-space reconstruction evidence for processed 60-s PPG windows. (A) AMI-selected delay evidence supporting the common operational delay τ = 0.16 s. (B–C) FNN curves for Awake and Drowsy, respectively, supporting the common dimension m = 8 in a low-FNN region. The same reconstruction parameters were used for both states. These diagnostics describe reconstruction behavior and do not establish a universal optimum.
