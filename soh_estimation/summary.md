| ID | First author | Year | Full title | Journal | DOI | PDF filename |
|---|---|---|---|---|---|---|
| Naha_2020 | Arunava Naha | 2020 | An Incremental Voltage Difference Based Technique for Online State of Health Estimation of Li-ion Batteries | Scientific Reports | 10.1038/s41598-020-66424-9 | [naha2020.pdf](paper/naha2020.pdf) |
| Wen_2022 | Jici Wen | 2022 | Linear correlation between state-of-health and incremental state-of-charge in Li-ion batteries and its application to SoH evaluation | Electrochimica Acta | 10.1016/j.electacta.2022.141300 | [wen2022.pdf](paper/wen2022.pdf) |
| Petkovski_2024 | Emil Petkovski | 2024 | State of Health Estimation Procedure for Lithium-Ion Batteries Using Partial Discharge Data and Support Vector Regression | Energies | 10.3390/en17010206 | [petkovski2024.pdf](paper/petkovski2024.pdf) |
| Qin_2024 | Pengliang Qin | 2024 | Enhancing data-driven-based state of health estimation for diverse battery applications through effective feature construction | Energy | 10.1016/j.energy.2024.133156 | [qin2024.pdf](paper/qin2024.pdf) |
| Chen_2025 | Junran Chen | 2025 | Battery state-of-health estimation using CNNs with transfer learning and multi-modal fusion of partial voltage profiles and histogram data | Applied Energy | 10.1016/j.apenergy.2025.125923 | [chen2025.pdf](paper/chen2025.pdf) |
| Yao_2025 | Xing-Yan Yao | 2025 | Battery state of health estimation with interpretable distance feature and dynamic weight model across-chemistry and working conditions | Energy | 10.1016/j.energy.2025.137175 | [yao2025.pdf](paper/yao2025.pdf) |

**Source and reading conventions.** This document uses only the six supplied PDFs, including their figures, tables, and captions. Page numbers refer to PDF pages, which match the printed article page numbers. Source locations accompany technical details and results. Percentages retain the authors' metric definitions: relative percentage error, absolute SOH error, and dimensionless R² are not interchangeable. Plot heights have not been converted into invented precise values. Supplementary files cited by the PDFs but not supplied were not consulted.

**Internal GSI planning.** The six PDFs do not define the manuscript's GSI method. Section 13 therefore identifies supported comparison axes and suggested experiments, rather than asserting an unverified GSI formulation or novelty. Suggestions in Sections 13 and comparison D are planning recommendations, not experiments reported by the cited papers.

# Naha_2020

## 1. Bibliographic information

- Full title: An Incremental Voltage Difference Based Technique for Online State of Health Estimation of Li-ion Batteries.
- Authors: Arunava Naha; Seongho Han; Samarth Agarwal; Arijit Guha; Ashish Khandelwal; Piyush Tagade; Krishnan S. Hariharan; Subramanya Mayya Kolake; Jongmoon Yoon; Bookeun Oh.
- Journal: Scientific Reports.
- Year: 2020.
- Volume / issue / article number: 10 / issue not explicitly reported / 9526.
- DOI: 10.1038/s41598-020-66424-9. (p. 1.)

## 2. Research objective

- Estimate SOH online from short partial charging segments using finite differences of resistance-corrected voltage and average temperature.
- Generate training features over a broader SOH range by extrapolating voltage curves from early cycling data.
- Evaluate separate test cells under different temperatures, charging rates, and nominal capacities with the same electrochemistry. (pp. 3–6.)

## 3. Battery data and experimental setting

- Battery chemistry: LCO cathode / graphite anode, both battery types.
- Cell format / nominal capacity: Pouch cells; Type-1 maximum capacity 3.0 Ah; Type-2 maximum capacity 3.5 Ah; nominal voltage described as 3.85–4.4 V.
- Number of cells: 18 total: 10 Type-1 and 8 Type-2; 2 Type-1 training cells and 16 separate test cells.
- Dataset name/source: Authors' laboratory cycling experiments; no public dataset name explicitly reported.
- Charge/discharge protocol: CC–CV charge, CV at 4.4 V, CC discharge; 0.2C probing charge/discharge after each 50 or 125 normal cycles supplies reference capacity.
- Temperature: 25 °C and 45 °C chambers.
- C-rate: Normal CC charge 0.8C, 1.0C, or 1.2C; normal discharge 1.0C or 1.2C; probing 0.2C. Training charge rate 0.8C.
- Full or partial profile: Full cycles for calibration and early-life extrapolation; partial charging for estimation, approximately 15 min, described generally as 10–20 min.
- Charge or discharge: Charging features; discharge capacity from probing cycles supplies SOH labels.
- Observed voltage/capacity/time region: Ten corrected-voltage points with adjacent coulomb-count increments of 1.5% of rated capacity; starting corrected voltage fixed for the application. 3.7 V is an example, not an explicitly documented common test window.
- Sampling rate, if reported: 0.8C data sampled every 1 min; 1.2C every 10 s; cubic-polynomial upsampling to 1 s. Sampling at 1.0C: Not explicitly reported. (pp. 3–7; Tables 2–3.)

## 4. Input data

- Terminal voltage, current, battery temperature, sampling time, and rated capacity.
- First-cycle fixed internal resistance from the discharge-to-rest voltage/current transition.
- Early cycling/probing data for offline voltage extrapolation; corrected partial charging voltage and average charging temperature for deployed estimation. Previous SOH and cycle count are not estimator inputs. (pp. 3–6, 9.)

## 5. Feature / representation construction

Using the first-cycle resistance \(R_f\), construct

\[
v_{\mathrm{sei}}(k)=v(k)-R_f i(k),\qquad
R_f=\frac{v(\mathrm{eod})-v(\mathrm{sor})}{i(\mathrm{eod})}.
\]

Select ten points on the corrected voltage versus coulomb-count coordinate, starting at a fixed \(v_{\mathrm{sei},0}\), with

\[
\Delta Q_c=\sum i(k)T_s=0.015C_{\max},\quad
\Delta v_{\mathrm{sei},j}=v_{\mathrm{sei},j}-v_{\mathrm{sei},j-1},\quad
\mathbf{x}=[\Delta v_{\mathrm{sei},1},\ldots,\Delta v_{\mathrm{sei},9},T_{\mathrm{avg}}].
\]

The final vector has ten components: nine finite voltage differences and temperature. These are capacity-indexed finite differences, not an ICA/DVA derivative or a single scalar. The resistance correction uses an initial-state parameter; adjacent-point subtraction is not subtraction of an entire BOL curve. SOH labels and sampling increments use rated-capacity normalization. (pp. 3–5, Eqs. 1–8.)

For offline augmentation, fit a first-cycle OCV–SOC polynomial and a least-squares relation \(\Delta R_{\mathrm{sei}}=\widehat P_c\Delta Q_{\mathrm{loss}}\) from the first 400 cycles. Use these to synthesize corrected-voltage curves at lower SOH. The actual training procedure extrapolates 100%–75% SOH in 500 equal steps, although the introductory description emphasizes 100%–80%. (p. 5; pp. 9–10, Eqs. 19–31.)

## 6. Feature/window selection

- Fixed application-dependent starting corrected voltage, followed by predefined equal coulomb-count increments. An available IC peak is suggested as an alternative start.
- No correlation scan or supervised window optimization explicitly reported.
- Offline extrapolation and ANN training use the two training cells; test-cell first-cycle resistance and rated capacity are used for normalization/correction, not reported target-label fine-tuning. Exact start voltage used in every test case: Not explicitly reported. (pp. 4–6.)

## 7. Estimation model

- Model / estimator: ANN implemented in scikit-learn; ten input nodes, one hidden layer of 100 nodes, one output; logistic activation.
- Model inputs: Nine corrected finite voltage differences and average temperature.
- Output: SOH.
- Online/offline learning: One-time offline training; cyclewise online inference. Online weight learning is not reported.
- Fine-tuning or adaptation: No retraining for the 3.5 Ah test cells of the same electrochemistry; new-chemistry training is discussed, not demonstrated as cross-chemistry transfer.
- Hyperparameter optimization: Architecture selected after trials balancing accuracy and computation; no formal optimization protocol reported.
- Ensemble, if any: None reported. kNN, linear regression, SVM regression, and RF were tried, but only ANN results are presented. (pp. 3, 5–6.)

## 8. Validation protocol

Training uses the first 400 measured cycles of one Type-1 cell at each temperature, followed by synthetic full-range SOH features. Measured early-life SOH is approximately 100%–96%; synthetic training extends to 75%. Testing uses physically distinct cells, rather than later cycles of the training cells. (pp. 5–6; Table 3, p. 8.)

| Role | Type | Cells | CC charge | Chamber |
|---|---|---:|---|---|
| Training | Type-1 | 1 | 0.8C | 45 °C |
| Training | Type-1 | 1 | 0.8C | 25 °C |
| Testing | Type-1 | 3 | 0.8C | 45 °C |
| Testing | Type-1 | 3 | 0.8C | 25 °C |
| Testing | Type-1 | 1 | 1.0C | 45 °C |
| Testing | Type-1 | 1 | 1.2C | 45 °C |
| Testing | Type-2 | 4 | 0.8C | 45 °C |
| Testing | Type-2 | 4 | 0.8C | 25 °C |

This is held-out cross-cell testing with initial resistance calibration, including rate and same-chemistry capacity changes. The two higher-rate Type-1 cases reach approximately 85% SOH according to the text; the ordinary Type-1 cases cover approximately 100%–90%. No separate validation-cell set, LOCO, k-fold protocol, or cross-dataset experiment is explicitly reported.

## 9. Quantitative results

The authors define absolute error as \(AE=|SOH_t-SOH_e|/SOH_t\), so their percentage MAE is a mean relative absolute error, rather than an unnormalized SOH difference. (p. 6, Eq. 9.)

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| All 16 test cells; conditions in Table 3 | Two distinct training cells; held-out cells | MAE | <1% in every test case | p. 6 and Fig. 4, p. 7; per-cell precise values are not printed |
| All 16 test cells | Same setup | SD of absolute error | Below 0.7 except one case | p. 6 wording; Fig. 4 labels SD in % |
| All 16 test cells | Same setup | Maximum absolute error, MaxE | <1.5% except one case | p. 6; no exact value supplied for the exception |
| Type-1, 0.8C, 25/45 °C | Six held-out cells | Case-specific MAE / SD / MaxE | Not explicitly reported / not found in the paper. | Bars in Fig. 4; aggregate bounds above apply |
| Type-1, 1.0C or 1.2C, 45 °C | One held-out cell per rate | Case-specific MAE / SD / MaxE | Not explicitly reported / not found in the paper. | The visible exception is the 1.0C, 45 °C case; do not digitize its height as an exact value |
| Type-2, 3.5 Ah, 0.8C, 25/45 °C | Eight held-out cells; trained on 3.0 Ah | Case-specific MAE / SD / MaxE | Not explicitly reported / not found in the paper. | Same-chemistry capacity transfer; Fig. 4 |
| Voltage extrapolation, not SOH prediction | Measured versus extrapolated curves | Mean square error | <1% | p. 10; retain authors' metric wording |

R², RMSE, and additional baseline error values: Not explicitly reported / not found in the paper.

## 10. Robustness / sensitivity results

- Separate cells at 25/45 °C, 0.8/1.0/1.2C charge, and 3.0/3.5 Ah capacities are evaluated; the per-case MAE remains <1% (pp. 6–8).
- Corrected voltage is intended to reduce charging-rate effects. Only the listed rates are demonstrated; no arbitrary-rate guarantee is established.
- Noise injection, window scans, and downsampling sensitivity: Not explicitly reported / not found in the paper.

## 11. Physical interpretation / explainability

The simplified OCV-plus-resistance model separates fixed resistance from aging-related SEI resistance. The authors attribute horizontal curve contraction to active-material/lithium-inventory loss and vertical evolution to resistance increase, and use a literature-derived SEI resistance–capacity-loss relation for extrapolation. Internal resistance and capacity are measured; SEI growth and particular degradation modes are model/literature interpretations, not direct postmortem evidence. No SHAP or separate DVA analysis is reported. (pp. 3–4, 7–10.)

## 12. Computational information

- Abstract: complexity \(O(n^4)\), without a clearly defined \(n\) there.
- Testing-stage expression: \(O(n_{\mathrm{layer}}\,n_{\mathrm{neurons}}^3)\) (p. 6); retain separately rather than reconciling the two expressions.
- Training-data acquisition: approximately 45 days for 400 cycles; this is laboratory acquisition time, not ANN training runtime (pp. 3, 6).
- ANN architecture is reported; feature-extraction runtime, training runtime, inference latency, memory/model size, parameter count, FLOPs/MACs, and measured embedded deployment: Not explicitly reported / not found in the paper.

## 13. Direct relevance to GSI

- Strong comparison axis: partial charging and explicitly finite, capacity-indexed ΔV features.
- Initial-state information is already used through first-cycle resistance correction; this differs technically from reference-curve subtraction. The feature vector is derivative-free but has ten components, rather than one scalar.
- No geometric distance representation or target-label adaptation is reported; the ANN and electrochemical extrapolation are separate processing stages to compare with the manuscript's actual GSI implementation.
- Can motivate unseen-cell testing, BOL-reference ablation, rate/temperature robustness, and a measured computational benchmark; no GSI novelty claim follows from this comparison.

## 14. One-sentence Related Work summary

Naha et al. extracted nine capacity-indexed finite differences of resistance-corrected voltage from partial charging profiles, combined them with average temperature, and used an ANN for SOH estimation, achieving MAE below 1% on 16 held-out LCO/graphite cells spanning two temperatures, three charging rates, and two capacities.

# Wen_2022

## 1. Bibliographic information

- Full title: Linear correlation between state-of-health and incremental state-of-charge in Li-ion batteries and its application to SoH evaluation.
- Authors: Jici Wen; Qingrong Zou; Chunguang Chen; Yujie Wei.
- Journal: Electrochimica Acta.
- Year: 2022.
- Volume / issue / article number: 434 / issue not explicitly reported / 141300.
- DOI: 10.1016/j.electacta.2022.141300. (p. 1.)

## 2. Research objective

- Construct a scalar incremental SOC from a sliding voltage window of CC charging/discharging data and examine its linear relation to SOH.
- Use the fitted slope and extrapolated value at SOH = 1 for sequential SOH evaluation and comparison of cycling performance.
- Validate the relation across cell types and rates using laboratory and two external datasets. (pp. 2–8.)

## 3. Battery data and experimental setting

- Battery chemistry: Laboratory LISHEN and external A123: LFP/graphite. External Kokam: mixed lithium cobalt oxide and lithium nickel cobalt oxide positive electrode / graphite negative electrode.
- Cell format / nominal capacity: LISHEN 18650 cylindrical, 1.5 Ah; Kokam SLPB 533459H pouch, 0.74 Ah; A123 1.1 Ah, format not explicitly reported.
- Number of cells: 48 LISHEN (six groups of eight); 8 Kokam; 45 A123. Cycle-life analysis uses 32 of the LISHEN cells.
- Dataset name/source: Authors' experiments; Birkl/Oxford-related Kokam data, references 59–60; Attia et al. A123 data, reference 63.
- Charge/discharge protocol: LISHEN CC–CV charge to 4.0 V, CV cutoff 0.05C, CC discharge to 2.0 V. Kokam dynamic aging: 2C CC charge and Artemis urban discharge, mean discharge current 1.36 A; 1C charge/discharge characterization after each 100 dynamic cycles. A123: 4C CC discharge to 2 V, followed by CV to 1/50C cutoff.
- Temperature: LISHEN 25 °C; Kokam 40 °C; A123: Not explicitly reported.
- C-rate: LISHEN charge/discharge pairs 1.0/3.0C, 1.5/3.0C, 2.0/3.0C, 2.5/3.0C, 2.0/2.0C, and 2.5/2.5C. Table 1 mislabels the abbreviation of the 2.0/2.0C group as “2.0C-3.0D”; the protocol column gives 2.0C discharge. Kokam characterization 1C; A123 analyzed at 4C discharge.
- Full or partial profile: Full cycling/characterization for reference SOH; shallow partial CC segments for the feature.
- Charge or discharge: Both examined; principal LISHEN fitting/prediction and A123 fitting use discharge; Kokam validation uses charge.
- Observed voltage/capacity/time region: LISHEN examples \(V_s=3.3\) V, ΔV = 0.3 V; charging 3.3–3.6 V, discharging 3.3–3.0 V. Kokam charging \(V_s=3.8\) V, ΔV = 0.2 V. A123 discharge \(V_s=3.3\) V, ΔV = 0.3 V.
- Sampling rate, if reported: Laboratory LISHEN 1 Hz; external datasets: Not explicitly reported. (pp. 2–3, Table 1; pp. 5–8.)

## 4. Input data

- CC voltage–time curves and known CC rate.
- Voltage-window traversal time Δt, converted to ΔSOC.
- Reference capacity/rated capacity for SOH labels; per-cell initial calibration and later calibration points for the linear predictor. (pp. 1, 3–8.)

## 5. Feature / representation construction

In the \((t,V)\) coordinate, measure the time to traverse a window beginning at \(V_s\) with width ΔV, and convert it to one scalar:

\[
\Delta SOC=C\Delta t,\qquad
SOH=1+k\left(\Delta SOC-\Delta SOC^1\right).
\]

Here \(C\) is the CC rate and Δt uses the corresponding time unit; \(\Delta SOC^1\) is the extrapolated ΔSOC at SOH = 1. Several plots use \(1-\Delta SOC\), but Eq. 2 defines the model in ΔSOC. Window ΔV is a finite voltage interval; the feature is its SOC increment, not a vector of finite voltage differences. The deployed feature does not require differentiation. ICA, \(dSOC/dV\), is separately used to interpret evolution and identify a linear-aging regime. No whole-curve reference subtraction or feature interpolation/filter specification is reported. (pp. 3–7, Eq. 2.)

## 6. Feature/window selection

- Scan window start \(V_s\) and width ΔV using the Spearman correlation of ΔSOC with measured SOH; examples appear in Figs. 2b and 3b (pp. 3–5).
- The correlation definition uses the battery-specific total number of cycles, so this analysis uses labeled cycling histories; a strictly training-only window-selection protocol is not explicitly reported.
- For LISHEN discharge, define the end of the fitted linear regime using an IC Peak 1 voltage-position offset of 0.3% from its initial position (p. 7).
- Kokam uses a dataset-specific 0.2 V charging window; A123 applies the 0.3 V discharge window. This is validation of a relation across datasets, not evidence that a fitted source estimator is transferred without recalibration.

## 7. Estimation model

- Model / estimator: Per-cell linear SOH–ΔSOC relation with slope \(k\) and extrapolated \(\Delta SOC^1\).
- Model inputs: Scalar ΔSOC.
- Output: SOH; slope/intercept-related indices also characterize cycling performance.
- Online/offline learning: Linear fitting and sequential shallow-profile evaluation; the conclusion describes initial two to three full cycles for calibration.
- Fine-tuning or adaptation: In the 48-cell prediction demonstration, \(k\) is corrected once after SOH decreases by up to 0.04.
- Hyperparameter optimization: Spearman window analysis; no separate machine-learning optimizer reported.
- Ensemble, if any: None reported. (pp. 7–9.)

## 8. Validation protocol

- **LISHEN fitting:** Linear-region fits evaluated on the same 48 cells' measured aging trajectories, principally SOH >0.75. This is fit quality, not unseen-cell error.
- **LISHEN prediction:** Predictions for those 48 cells using calibrated \(k\) and \(\Delta SOC^1\), with one correction of \(k\) at a SOH decrease up to 0.04. The paper does not give a conventional train/test fraction or a precise calibration/test cycle partition.
- **Kokam:** Validate the SOH–ΔSOC evolution pattern on eight external pouch cells, using their 1C characterization curves and a different window.
- **A123:** Fit/check linearity on 45 external cells at 4C discharge. The initial region SOH >0.93 is nonlinear; subsequent evolution is approximately linear to SOH = 0.7.
- Counts of separate training/validation/test cells, LOCO, and k-fold: Not explicitly reported / not found in the paper. Multiple datasets establish applicability of the relation, not a frozen-model cross-dataset transfer experiment. (pp. 5–9, Figs. 4–7.)

## 9. Quantitative results

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| 48 LISHEN cells, six rate groups | Same-cell linear-regime fitting | Maximum Error (ME) | 0.4%–1.4% | p. 8, Fig. 5d |
| 48 LISHEN cells, fitting | Same trajectories | MAE | Authors say the MAEs are “smaller by 0.5%” | Ambiguous wording: not safely convertible to MAE <0.5% |
| 48 LISHEN cells, sequential prediction | Per-cell calibration plus one \(k\) correction | ME | 0.5%–2% | p. 8, Fig. 6g; later paragraph gives 0.4%–2% for the same 48-cell prediction context |
| 48 LISHEN cells, sequential prediction | Same setup | MAE | Within 0.7% | p. 8, Fig. 6g |
| 45 A123 LFP/graphite cells | Linear-regime fitting after initially nonlinear aging | ME | 0.4%–2.0% | p. 8, Fig. 7c |
| 45 A123 cells, fitting | Same setup | MAE | Authors say the MAE is “smaller by 0.5%” | Preserve wording; do not interpret as an unambiguous upper bound |
| 8 Kokam pouch cells | Charging-curve evolution validation | Quantitative SOH error metric | Not explicitly reported / not found in the paper. | Figs. 4a–b, pp. 5–7 |

The paper defines ME as \(\max_i(y_i-\widehat y_i)\), without an absolute-value sign, while defining MAE with an absolute value (p. 7). Retain “ME” rather than silently relabeling it maximum absolute error. RMSE and R²: Not explicitly reported / not found in the paper.

## 10. Robustness / sensitivity results

- Tested charge/discharge rates and cell types are listed above; the 48-cell prediction MAE is within 0.7% (p. 8).
- Window scans show strong/weak and sometimes negative correlations depending on the region; no numeric noise-injection/downsampling benchmark is reported (pp. 3–5).
- LISHEN charge example remains linear to SOH = 0.5; LISHEN discharge has a later nonlinear regime; A123 has an initially nonlinear regime above 0.93 followed by a linear regime to 0.7. These are observed regime differences, not identical accuracy over a universal SOH range (pp. 4–5, 8).
- Temperature robustness is not isolated experimentally from differences in the external datasets.

## 11. Physical interpretation / explainability

ICA peak intensity/position evolution is compared with the onset and end of linear SOH–ΔSOC evolution. The measured discharge IC Peak 1 shift defines the fitted LISHEN regime; A123's Peak 1 disappears in the initial nonlinear stage while Peak 2 decreases in the subsequent linear stage. On 32 LISHEN cells, slope \(k\) correlates positively and \(\Delta SOC^1\) negatively with degradation rate. These are curve/correlation diagnostics, not direct identification of individual material-loss mechanisms. (pp. 4–8, Figs. 2–3, 7–8.)

## 12. Computational information

Only qualitative computational-efficiency claim; no quantitative benchmark found. The conclusion describes assessment in less than a few minutes, which concerns the shallow measurement procedure, not timed feature extraction or inference on specified hardware. Training time, memory, and model-size benchmarks: Not explicitly reported / not found in the paper. (p. 9.)

## 13. Direct relevance to GSI

- Strong comparison axis: a single derivative-free scalar from a partial profile and a finite ΔV window, applicable to both CC charge and discharge.
- Reference-like calibration appears as \(\Delta SOC^1\) at SOH = 1; whole-curve BOL subtraction and a geometric distance feature are not reported.
- The method requires region-dependent linearity and per-cell calibration/correction; these are concrete estimator/validation properties to compare with the actual GSI formulation.
- Can motivate region sensitivity, ICA/DVA interpretation, BOL-reference ablation, and a separately designed unseen-cell experiment; reported per-cell fits alone cannot establish that experiment's outcome.

## 14. One-sentence Related Work summary

Wen et al. derived incremental SOC from sliding finite-voltage windows of partial CC profiles and used a calibrated linear SOH–ΔSOC model for SOH estimation, achieving MAE within 0.7% and maximum error of 0.5%–2% in sequential prediction on 48 LISHEN LFP/graphite cells with one slope correction.

# Petkovski_2024

## 1. Bibliographic information

- Full title: State of Health Estimation Procedure for Lithium-Ion Batteries Using Partial Discharge Data and Support Vector Regression.
- Authors: Emil Petkovski; Iacopo Marri; Loredana Cristaldi; Marco Faifer.
- Journal: Energies.
- Year: 2024, following the volume/citation printed in the PDF. The printed publication date is 30 December 2023.
- Volume / issue / article number: 17 / issue not explicitly stated in the article text / 206.
- DOI: 10.3390/en17010206. (p. 1.)

## 2. Research objective

- Estimate cyclewise SOH using SVR and discharge-capacity/temperature features.
- Compare feature combinations over the full discharge window and ten smaller voltage intervals.
- Evaluate separately held-out cells and explain failures at uninformative voltage windows or atypical degradation trajectories. (pp. 3–12.)

## 3. Battery data and experimental setting

- Battery chemistry: Lithium iron phosphate.
- Cell format / nominal capacity: Commercial cells; 1.1 Ah, 3.3 V nominal. Cell format/model: Not explicitly reported.
- Number of cells: 124.
- Dataset name/source: Toyota Research Institute in cooperation with Stanford and MIT; experimental platform and Severson-related data cited in the PDF.
- Charge/discharge protocol: Two-step fast charge, “C1(Q1)–C2”, with 72 policies; constant-current discharge at 4.4 A.
- Temperature: Chamber 30 °C; cell temperature may vary by up to 10 °C within a cycle and between cells.
- C-rate: Discharge current stated as 4.4 A. Individual charging C-rates are not enumerated; do not import rates from another paper on the same source dataset.
- Full or partial profile: Both full and partial discharge windows.
- Charge or discharge: Discharge-capacity features; cumulative average cycle temperature also used.
- Observed voltage/capacity/time region: Full 2–3.4 V; ten partial windows listed in Section 9.
- Sampling rate, if reported: Not explicitly reported. (p. 3, Section 2; pp. 7–11.)

## 4. Input data

- Discharge capacity as a function of voltage, \(Q_k(V)\).
- Each battery's cycle-10 discharge curve, \(Q_{10}(V)\), as reference.
- Temperature measurements over each cycle and cumulative history of cycle-average temperature. (pp. 5–7.)

## 5. Feature / representation construction

Interpolate reference and current discharge curves onto a common voltage grid and subtract pointwise in the \((V,Q)\) coordinate:

\[
\Delta Q_k(V)=Q_k(V)-Q_{10}(V),\qquad
\overline{\Delta Q_k}=\frac1p\sum_{i=1}^{p}\Delta Q_{k,i}.
\]

The three available features are

\[
\begin{aligned}
Ftr1(k)&=\log_{10}\left|\frac{1}{p-1}\sum_{i=1}^{p}(\Delta Q_{k,i}-\overline{\Delta Q_k})^2\right|,\\
Ftr2(k)&=\log_{10}|\min_i\Delta Q_{k,i}|,\\
Ftr3(k)&=\sum_{c=1}^{k}\overline T_c.
\end{aligned}
\]

Common logarithms are specified in the text; the third feature is the sum of cycle-average temperatures, not merely the current cycle's temperature and not a continuous-time integral. For cycles 1–10 the first two feature values are set equal to those of cycle 11. Interpolation type and number of common-grid points: Not explicitly reported. (pp. 5–7, Eq. 3.)

Feature sets: A = [Ftr1, Ftr2, Ftr3], three dimensions; B = [Ftr1, Ftr3], two dimensions; C = [Ftr2, Ftr3], two dimensions. The chosen full-window model uses B. This is derivative-free, reference-based statistical processing; cycle 10 is an early-life reference, not necessarily exact BOL. (pp. 7–10.)

## 6. Feature/window selection

- Full window and ten predefined partial intervals are evaluated; no optimization of arbitrary continuous window endpoints is described.
- Within each interval, select A/B/C by the highest mean five-fold CV R², then tune that interval's SVR hyperparameters.
- Selection/tuning use only the 109 training/validation cells, not the 15 held-out test cells. Labels are used for the CV objective. Fold grouping by cell versus cycle is not explicitly described. (pp. 7–10.)

## 7. Estimation model

- Model / estimator: Gaussian-kernel SVR.
- Model inputs: Selected two- or three-component feature set.
- Output: SOH after each cycle.
- Online/offline learning: Offline training/tuning; cyclewise estimation. No online weight updates described.
- Fine-tuning or adaptation: No target-domain fine-tuning reported; separate models are fitted for each evaluated interval.
- Hyperparameter optimization: MATLAB 2021b Bayesian optimizer, 60 iterations, RMSE loss; subsequent five-fold CV selects features and hierarchically refines epsilon, box constraint, and kernel scale. Full-window final values: box constraint 0.0055, epsilon 0.0021, kernel scale 1.0.
- Ensemble, if any: None reported. (pp. 7–10, Tables 1–4.)

## 8. Validation protocol

Randomly hold out 15 entire batteries; use all cycles of the other 109 for training/validation. Apply five-fold CV for feature-set selection and hyperparameter refinement within this pool. Final R² is calculated individually across each held-out battery's cycles and then averaged across 15 batteries. Test features still require the test battery's own cycle-10 reference and temperature history. This is unseen-cell testing with local reference acquisition, not zero-calibration deployment or cross-dataset transfer. Exact cell grouping inside the CV folds, separate validation-cell count, and LOCO: Not explicitly reported / not found in the paper. (pp. 7–8, 11–12.)

## 9. Quantitative results

Each row below is a separately tuned interval-specific model. CV and test values are **mean R²**, not RMSE or percentage errors. (Tables 3–5, pp. 10–11.)

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| Full 2–3.4 V; set B | Five-fold CV on 109 cells' data; 15 held-out cells | CV R² / test R² | 0.9761 / 0.9620 | Abstract/text round to 0.976 and 0.962 |
| 3–3.4 V; set B | Same split, own tuned model | CV R² / test R² | 0.9609 / 0.9447 | Partial |
| 3.15–3.4 V; set A | Same split | CV R² / test R² | 0.9042 / 0.8639 | High-voltage failure case |
| 3.25–3.4 V; set A | Same split | CV R² / test R² | 0.8525 / 0.8473 | High-voltage failure case; Table 5 reverses these two high-window column positions relative to Table 4 |
| 3–3.2 V; set B | Same split | CV R² / test R² | 0.9673 / 0.9387 | Partial |
| 3–3.1 V; set C | Same split | CV R² / test R² | 0.9567 / 0.9486 | Partial |
| 3–3.05 V; set C | Same split | CV R² / test R² | 0.9687 / 0.9515 | Narrow partial window |
| 2.8–3 V; set C | Same split | CV R² / test R² | 0.9740 / 0.9579 | Partial |
| 2.9–3 V; set C | Same split | CV R² / test R² | 0.9737 / 0.9576 | Partial |
| 2.4–2.6 V; set A | Same split | CV R² / test R² | 0.9821 / 0.9727 | Partial |
| 2.2–2.4 V; set A | Same split | CV R² / test R² | 0.9818 / 0.9728 | Best test mean |
| Full window, best individual cell T11 | Held-out individual-cell trajectory | R² | 0.9992 | Text rounds to 0.999 |
| Full window, worst individual cell T4 | Held-out individual-cell trajectory | R² | 0.7938 | Text rounds to 0.794 |
| Full window, representative “mode” cell T5 | Held-out individual-cell trajectory | R² | 0.9813 | Text rounds to 0.981 |
| Full window, outlier T13 | Held-out individual-cell trajectory | R² | 0.8234 | Table 5 |

The abstract's 0.939–0.973 partial-window range applies to the successful windows and excludes the two poor high-voltage windows; it is not the range over all ten partial cases. Numerical SOH RMSE, MAE, MAPE, and maximum error: Not explicitly reported / not found in the paper. RMSE is an optimization loss, not a tabulated estimation result.

## 10. Robustness / sensitivity results

- Strong explicit window sensitivity: all ten partial-window test means are preserved above; variance features fail when the difference curve becomes nearly constant below 3.1 V (pp. 8–11).
- For 3–3.05 V, set B feature-selection CV R² = 0.3883, versus set C = 0.9646, illustrating why variance and minimum-difference features cannot be treated as interchangeable (Table 2, p. 10).
- T4 and T13 remain difficult across windows; their full-window R² values are 0.7938 and 0.8234. The authors compare normalized-cycle degradation trajectories to explain this behavior (p. 11, Fig. 9).
- Noise, downsampling, independent temperature sweeps, and discharge-rate sweeps: Not explicitly reported / not found in the paper.

## 11. Physical interpretation / explainability

Reference subtraction represents the change in discharge capacity distribution. High-voltage windows move little charge and change little with aging; low-voltage difference curves have little variance, weakening Ftr1 while retaining information in Ftr2. The outliers have atypical nearly linear/sudden SOH declines. Internal defects or extreme usage are proposed explanations, not diagnosed causes. No direct degradation-mode experiment, ICA/DVA interpretation of the constructed features, or SHAP analysis is reported. (pp. 5, 9, 11.)

## 12. Computational information

Only qualitative computational-efficiency claim; no quantitative benchmark found. The paper reports MATLAB 2021b and a 60-iteration optimization limit due to computational resources, but not measured search/extraction/training/inference time, model memory, parameter count, FLOPs/MACs, or embedded hardware results. (pp. 2–3, 7, 12.)

## 13. Direct relevance to GSI

- Strong comparison axis: partial discharge curves with explicit per-cell early-reference subtraction and derivative-free representations.
- Already uses a reference cycle, but not finite ΔV values as estimator features or a Euclidean curve-distance scalar; two or three statistical/history features enter SVR.
- Local reference acquisition is compatible with held-out-cell evaluation; the reference requirement should be made equally explicit when comparing GSI validation.
- Can motivate BOL-reference ablation, region sensitivity, unseen-cell testing, outlier analysis, and computational benchmarking; cycle-10 reference subtraction alone supports no claim about GSI novelty.

## 14. One-sentence Related Work summary

Petkovski et al. constructed logarithmic statistics of cycle-10-referenced discharge-capacity differences and cumulative cycle-average temperature and used Gaussian-kernel SVR for SOH estimation, achieving mean R² of 0.9620 for the full 2–3.4 V window and 0.9728 for the 2.2–2.4 V window on 15 held-out cells from a 124-cell LFP dataset.

# Qin_2024

## 1. Bibliographic information

- Full title: Enhancing data-driven-based state of health estimation for diverse battery applications through effective feature construction.
- Authors: Pengliang Qin; Linhui Zhao.
- Journal: Energy.
- Year: 2024.
- Volume / issue / article number: 309 / issue not explicitly reported / 133156.
- DOI: 10.1016/j.energy.2024.133156. (p. 1.)

## 2. Research objective

- Determine usable partial charging voltage regions from IC peak location and voltage-curve shape, without requiring a complete aging history for initial region determination.
- Construct geometric features from approximately straight or arc-shaped voltage–time segments.
- Use initial-feature self-scaling and OSELM updates to estimate SOH as a battery's aging pattern changes. (pp. 2–5.)

## 3. Battery data and experimental setting

- Battery chemistry: NASA cells described as NCA; CALCE as LCO; Oxford as a blend of lithium cobalt oxide and lithium nickel cobalt oxide. Studied Cell 60: ternary LiNi1-x-yCoxMyO2/graphite, as printed in Table 2.
- Cell format / nominal capacity: NASA 2 Ah; CALCE 1.1 Ah; Oxford Kokam SLPB 533459H4, 0.74 Ah; Cell 60, 57 Ah. Cell formats: Not explicitly reported in this PDF.
- Number of cells: Six public cells used for feature evaluation—B0005/B0007, CS2-35/CS2-37, Cell 1/Cell 5—and one experimental Cell 60. The experimental pack has 96 cells, but only Cell 60 is studied; the Oxford source contains eight cells, but only two are selected.
- Dataset name/source: NASA Ames Prognostics Center of Excellence, CALCE/University of Maryland, Oxford Battery Degradation Dataset, and authors' 96-cell pack experiment.
- Charge/discharge protocol: Public cells use CC–CV charging. Cell 60 aging uses multi-segment CC charging with future current selected from temperature/voltage and 1C CC discharge; capacity calibrations use CC–CV charge.
- Temperature: Table 1 gives NASA B0005 25 °C and B0007 43 °C, despite the text's general description of NASA at approximately 25 °C; CALCE 23 °C; Oxford 40 °C; experimental pack 25 °C.
- C-rate: Cell 60 discharge 1C. Table 1 gives charging currents rather than C-rates: NASA 1.5 A, CALCE 0.55 A, Oxford 0.74 A. Public discharge C-rates and exact Cell 60 multi-segment charging rates: Not explicitly reported.
- Full or partial profile: Relatively complete CC–CV charging for initial IC/region determination and capacity labels; selected partial charge regions for features, with additional narrower-window tests.
- Charge or discharge: Charging features and charging-capacity SOH labels.
- Observed voltage/capacity/time region: NASA [3.93, 4.2] V; CALCE [3.87, 4.2] V; Oxford [3.8, 4.2] V; Cell 60 [4.055, 4.16] V. Table 1 discharge cutoffs: B0005 2.7 V, B0007 2.2 V, CALCE/Oxford 2.7 V; Cell 60 cutoffs 3.4/4.3 V.
- Sampling rate, if reported: Acquisition sampling frequency: Not explicitly reported. IC processing uses a moving-average sampling step of 20, not a reported 20 Hz acquisition rate. (pp. 5–7, Tables 1–3.)

## 4. Input data

- Charging voltage and time for the geometric features.
- Current and time/capacity for constructing the initial IC curve and reference charging capacity.
- Each feature's own initial value for self-scaling.
- Labeled SOH samples for OSELM initialization and continuing updates; temperature is used in the experimental charging policy, not explicitly included in the three-feature estimator input. (pp. 3–6, 9.)

## 5. Feature / representation construction

Form \((t,U)\) coordinates over a selected interval with endpoints \((t_a,U_a)\), \((t_b,U_b)\). Construct

\[
\begin{aligned}
l_1&=\sqrt{(t_b-t_a)^2+(U_b-U_a)^2},\\
l_2&=\frac{|U_b-U_a|}{|t_b-t_a|},\\
l_3&=\sin\beta=\frac{|t_b-t_a|}{\sqrt{(t_b-t_a)^2+(U_b-U_a)^2}}.
\end{aligned}
\]

These are chord/line-segment length, slope, and sine of the angle to the voltage axis; three constructed features form the representation. Coordinate rescaling before these geometric equations and a fixed number of sampled feature points are not explicitly reported. The method argues that a partial segment of a line or circle can map to its complete shape; experimentally, narrower-window feature values still differ, so exact invariance should not be claimed. (p. 4, Eqs. 7–9; pp. 8–9.)

Separate **normalization** from feature extraction: each feature is divided by its own initial value,

\[
X_{n,k}=\frac{X_{i,k}}{X_{i,0}},
\]

rather than standardized with another domain's mean and standard deviation. This is initial-state feature normalization, not subtraction of a complete BOL curve. ICA is used for region selection, with \(dQ/dU=I\,dt/dU\), moving-average smoothing, and step 20. Endpoint feature evaluation is derivative-free, but the complete region-selection pipeline uses derivatives. (pp. 3–6, Eqs. 1, 5–6, 17.)

## 6. Feature/window selection

- First choose a rough interval containing an IC peak, then refine it to where the voltage curve approximates a line or arc.
- The stated shape checks use small second or third derivatives with threshold δ; a numerical δ is not explicitly reported (p. 4, Eqs. 5–6).
- Region determination uses a relatively complete charge curve for the battery application; it is repeated for each dataset/type, not a frozen common source window.
- The proposed selection rule does not require SOH labels for its peak/shape tests. Subsequent labeled Pearson-correlation evaluations verify the resulting features across aging data; no strict training-only partition of these analyses is given. (pp. 3–4, 6–8.)

## 7. Estimation model

- Model / estimator: Feature self-scaling plus Online Sequential Extreme Learning Machine (OSELM).
- Model inputs: Constructed geometric aging features, self-scaled by their initial values.
- Output: SOH; Eq. 21 gives \(Q_{aged}/Q_N\times100\%\). The prose reverses the usual descriptions of these two symbols; retain the equation without treating that wording as a separate capacity convention.
- Online/offline learning: Initialize ELM output weights via a generalized inverse; recursively update OSELM output weights with incoming labeled samples.
- Fine-tuning or adaptation: Continuing within-battery supervised updates, not a source-pretrained network frozen for a label-free target.
- Hyperparameter optimization: Not explicitly reported; hidden-layer size and activation choice are not specified.
- Ensemble, if any: None reported. (pp. 4–6, Eqs. 14–21; p. 9.)

## 8. Validation protocol

- Features are examined on all seven selected cells; SOH-estimation comparisons concern B0007, CS2-37, Oxford Cell 5, and Cell 60.
- For the proposed method and incremental-learning comparator, the paper says only the battery used for verification is considered; conventional OSELM and no-update comparators use another battery from the same dataset for training. Do not assign the comparators' cross-cell setup to the proposed method.
- The online experiment uses two data samples to determine initial parameters, update step 4, and prediction step 2. These are reported data-step settings, not necessarily four/two raw acquisition samples or a universal number of ordinary cycles.
- Ground-truth capacity/SOH enters supervised model updates, as required by the OSELM equations. This is same-battery sequential adaptation; no independent held-out unseen-cell test of the proposed model is demonstrated.
- Train/test fraction, fixed train/validation/test cell counts, LOCO, and k-fold: Not explicitly reported / not found in the paper. Testing multiple datasets involves dataset-specific region construction and online learning, not a frozen cross-dataset transfer. (pp. 5–6, 9–10.)

## 9. Quantitative results

Pairs below are **MAE / MaxAE**, both in %, as identified by Section 4.3. (Table 8, p. 9.)

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| NASA B0007 | Proposed self-scaled OSELM, same-battery online updates | MAE / MaxAE | 0.4948% / 1.6458% | Table 8 |
| CALCE CS2-37 | Same method | MAE / MaxAE | 0.3552% / 1.9675% | Table 8 |
| Oxford Cell 5 | Same method | MAE / MaxAE | 0.0637% / 0.1683% | Table 8 |
| Experimental Cell 60 | Same method | MAE / MaxAE | 1.4038% / 2.3457% | Table 8 |
| NASA B0007 | Conventional OSELM, other-cell training plus updates | MAE / MaxAE | 2.6018% / 5.7456% | Comparator, not proposed-method output |
| CALCE CS2-37 | Same comparator | MAE / MaxAE | 0.5814% / 3.5831% | Table 8 |
| Oxford Cell 5 | Same comparator | MAE / MaxAE | 0.3703% / 0.7569% | Table 8 |
| Experimental Cell 60 | Same comparator | MAE / MaxAE | 1.5927% / 2.5883% | Table 8 |
| NASA B0007 | Proposed method, one-step / two-step prediction | MAE / MaxAE | 0.49% / 1.65%; 0.53% / 1.20% | Table 9, p. 10 |
| CALCE CS2-37 | Proposed method, one-step / two-step | MAE / MaxAE | 0.36% / 1.97%; 0.33% / 1.63% | Table 9 |
| Oxford Cell 5 | Proposed method, one-step / two-step | MAE / MaxAE | 0.0636% / 0.17%; 0.0665% / 0.18% | Table 9; retain distinct Oxford rounding/value from Table 8 |
| Experimental Cell 60 | Proposed method, one-step / two-step | Printed MAE / MaxAE pair | 1.40% / 0.23%; 1.34% / 2.62% | Table 9's one-step MaxAE is below its MAE and conflicts with Table 8; retain as printed, do not repair |

Table 9 is captioned “SOC online estimation results” although Section 4.3 and Fig. 13 concern SOH. Its Cell 60 one-step pair is internally inconsistent; use Table 8's 1.4038% / 2.3457% for the main manuscript fact. R², RMSE, and MAPE: Not explicitly reported / not found in the paper.

## 10. Robustness / sensitivity results

- Narrower-region tests quantify feature–SOH correlation, not SOH prediction errors. NASA B0007 at [3.98, 4.08] V gives Pearson coefficients 0.9847, −0.9690, 0.9534 for Features 1–3; Cell 60 at [4.065, 4.15] V gives 0.9147, −0.8915, 0.8747 (Table 7, p. 8).
- The authors state effective features persist with a region only 37.04% of the original width and correlation above 95%; this does not hold uniformly for every Cell 60 feature in Table 7. Preserve the reported claim and its table qualification (p. 8).
- Full-window feature correlations for Cell 60 are 0.9125, −0.8928, 0.8791, lower than those of the public examples (Table 6, p. 8).
- One-/two-step SOH errors are listed separately above. No quantitative injected-noise, downsampling, or controlled C-rate/temperature robustness test is reported.

## 11. Physical interpretation / explainability

IC peaks identify voltage regions associated with electrochemical changes; the paper then represents the curve geometrically as a line/arc and chord indicators. Its explanation is based on IC/voltage-shape evolution and feature–SOH correlation. It does not directly measure or partition loss of lithium inventory, active material, or resistance for the proposed features. No SHAP or DVA diagnostic evidence is reported. (pp. 3–4, 7–8.)

## 12. Computational information

Only qualitative computational-efficiency claim; no quantitative benchmark found. Fast/low-complexity ELM and sequential updates are discussed, but feature search/extraction time, update time, inference time, memory, parameter count, and embedded execution are not benchmarked. (pp. 4–5.)

## 13. Direct relevance to GSI

- Strong comparison axes: partial-profile geometry, relative endpoint distances, and initial-feature normalization.
- Already has finite voltage intervals and derivative-free endpoint features; the full pipeline uses ICA and derivative-based window checks, and offers three features rather than an explicitly reduced single scalar.
- Adaptation is supervised same-battery OSELM updating, with region construction repeated for each application; compare this explicitly with any GSI claim of frozen transfer.
- Can motivate geometry comparison, BOL-reference ablation, region sensitivity, ICA/DVA interpretation, and frozen-feature transfer experiments without implying that this paper already demonstrates those GSI outcomes.

## 14. One-sentence Related Work summary

Qin et al. constructed chord length, slope, and angular features from IC-guided partial charging regions, self-scaled them by initial values, and used OSELM for SOH estimation, achieving MAEs of 0.4948%, 0.3552%, 0.0637%, and 1.4038% under same-battery online updating on NASA B0007, CALCE CS2-37, Oxford Cell 5, and a 57 Ah experimental cell, respectively.

# Chen_2025

## 1. Bibliographic information

- Full title: Battery state-of-health estimation using CNNs with transfer learning and multi-modal fusion of partial voltage profiles and histogram data.
- Authors: Junran Chen; Phillip Kollmeyer; Ryan Ahmed; Ali Emadi.
- Journal: Applied Energy.
- Year: 2025.
- Volume / issue / article number: 391 / issue not explicitly reported / 125923.
- DOI: 10.1016/j.apenergy.2025.125923. (p. 1.)

## 2. Research objective

- Combine partial-profile information and cumulative operational-history histograms for SOH estimation.
- Transfer pretrained CNN/FNN representations into a fusion estimator and evaluate their complementarity under restricted training data.
- Quantify profile-window effects, training-data requirements, and inference cost on a PC and edge device. (pp. 7–15.)

## 3. Battery data and experimental setting

- Battery chemistry: McMaster NCA; Stanford LFP.
- Cell format / nominal capacity: McMaster Samsung 30 T, 3 Ah; format not explicitly stated in this PDF. Stanford A123 APR18650M1A, 1.1 Ah; format not separately stated in the text.
- Number of cells: McMaster six; Stanford 124.
- Dataset name/source: McMaster battery aging dataset for 15 min fast charging of Samsung 30 T cells; Stanford/MIT Severson dataset.
- Charge/discharge protocol: McMaster aging between 10% and 80% SOC using five fast-charge policies on six cells (CC applied to two), followed by drive-cycle discharge (UDDS/HWFET/LA92/WLTP); capacity/HPPC characterization at checkpoints. Stanford two-stage “C1(Q1)–C2” fast charging to 80% SOC, then 1C CC–CV completion; 4C discharge to 2.0 V, including a CV stage to C/50.
- Temperature: McMaster 25 °C; Stanford 30 °C.
- C-rate: McMaster CC/CC 2: 2.8C; BC: 5 min 4C then 10 min 2.2C. BCNP 0.1 s: 1.9 s at 4.323C and 0.1 s at −2.162C for 5 min, then 1.9 s at 2.324C and 0.1 s at −1.189C for 10 min. BCNP 1 s uses the same current levels with 1 s positive/negative pulses. BCR uses 1.9 s at 4.323C then 0.1 s rest for 5 min, followed by 1.9 s at 2.324C then 0.1 s rest for 10 min. McMaster feature/label characterization uses 0.5C discharge; Stanford features use 4C discharge.
- Full or partial profile: Approximately 14% SOC partial CC profiles, plus cumulative histograms of broader operation histories. Window-length tests include 7.2%, 28%, and 42%.
- Charge or discharge: **Main evaluated partial profiles are discharge profiles**: 0.5C McMaster and 4C Stanford (Section 4.1, p. 7), despite charging wording in the title, abstract, and some section/caption labels. Histograms aggregate operation history.
- Observed voltage/capacity/time region: 1000 s of a nominal 7200 s McMaster 0.5C discharge; 125 s of a nominal 900 s Stanford 4C discharge; regions near cutoff are excluded to avoid label leakage. SOC-position cases are listed in Section 10. Cells aged to approximately 70% SOH (McMaster) or 80% (Stanford).
- Sampling rate, if reported: Not explicitly reported. The reported time-window lengths must not be converted into an assumed number of input samples. (pp. 4–8, Tables 2–3.)

## 4. Input data

- Partial CC voltage, current, and temperature curves; three CNN channels.
- Cumulative duration histograms over current I, voltage V, temperature T, discharged coulombs since fully charged Q, and Q×I.
- Nominal/fresh capacity and measured discharge capacity for labels. McMaster label uses full 0.5C discharge to 2.5 V; Stanford label uses its 4C discharge including CV completion. HPPC/resistance and IC/DTW analyses diagnose feature ambiguities; they are not extra deployed estimator inputs. (pp. 5–8.)

## 5. Feature / representation construction

**Partial profiles:** Feed three aligned raw channels to a one-dimensional CNN with convolution, ReLU, max pooling, and fully connected layers. Features are learned, rather than hand-constructed finite ΔV, IC peaks, or curve-reference distances. The paper reports time/SOC lengths but not the final sampled profile-vector dimension in the supplied main PDF; detailed architectures are assigned to supplementary Fig. S2. (pp. 7–8.)

**Histograms:** Accumulate operational time in predefined bins. Table 3 uses minimum:step:maximum conventions:

| Histogram variable | McMaster | Stanford |
|---|---|---|
| Current, A | −35:1:35 | −10:0.1:10 |
| Voltage, V | 2.5:0.1:4.2 | 1.5:0.1:4 |
| Temperature, °C | 20:1:45 | 20:1:40 |
| Capacity, Ah | 0:0.03:3 | 0:0.1:1.1 |
| Q×I, Ah A | −105:1:105 | −11:0.1:11 |
| Total reported features | 427 | 560 |
| PCA output features | 12 | 69 |

PCA retains a 99% reconstruction/variance threshold and supplies reduced histogram features to an FNN with dropout 0.2. It is representation reduction, not SOH-supervised feature/window selection. Histogram totals and PCA dimensions are retained as reported, without recalculating bins using an assumed endpoint convention. No BOL curve subtraction or initial-feature normalization is described. (p. 8.)

**Fusion:** Pretrain the partial-profile CNN and histogram FNN separately; remove each last output layer; copy their other parameters into a fusion architecture and combine their representations through a final FNN. The main approach locks pretrained parameters; the histogram branch remains unlocked for McMaster and Stanford four-cell training because its initial predictions are poor. Final concatenated latent dimension: Not explicitly reported / not found in the paper. (pp. 8–9.)

## 6. Feature/window selection

- Empirical comparison of SOC lengths and positions; choose 14% as the accuracy/practicality tradeoff (pp. 10–11, Table 6).
- Exclude the cutoff region to avoid directly revealing capacity/SOH labels. No voltage-window correlation scan, IC-peak selection, or per-target geometric optimization is used.
- Network size and hyperparameters are selected through labeled five-fold CV within the training set. PCA fitting scope and a strict training-only selection procedure for the final SOC length/position are not explicitly documented; do not assert them. (pp. 8–11.)

## 7. Estimation model

- Model / estimator: CNN profile encoder + FNN histogram encoder + FNN multi-modal fusion head.
- Model inputs: Partial V/I/T curves and PCA-transformed cumulative histograms.
- Output: Capacity/SOH; results plot capacity in Ah and report RMSPE/MAPE for SOH accuracy.
- Online/offline learning: Offline neural-network training; proposed periodic inference during operation. No demonstrated continuous online weight update.
- Fine-tuning or adaptation: Transfer from pretrained modality-specific models into the fusion task within each dataset; locked versus unlocked pretraining is compared. This is not McMaster-to-Stanford or NCA-to-LFP source/target transfer.
- Hyperparameter optimization: Five-fold CV and grid/logarithmic network-size search. Batch size 100, initial learning rate 0.0001, validation frequency 3, validation patience 100, learning-rate drop period 1000, factor 0.1; Adam optimizer.
- Ensemble, if any: Learned representation fusion; no separate arithmetic voting ensemble reported. (pp. 8–10, 14, Tables 4, 8.)

## 8. Validation protocol

- **McMaster:** Train on BC, CC, BCR, BCNP 1 s (four cells); test on CC 2 and BCNP 0.1 s (two held-out cells). Training pool contains 192 recorded aging cycles, not 192 cells.
- **Stanford main:** Train on cells #1–#100; test on #101–#124 (24 held-out cells). Training pool contains 73,743 recorded aging cycles.
- **Stanford reduced data:** Train on four selected cells #2, #19, #37, #42 from the 100-cell training pool; additional experiments use 20, 30, and 40 training cells. Do not interpret unused training cells as a newly defined 120-cell test set; Table 5 defines the held-out testing group.
- **Internal CV:** Shuffle training data into five folds and train on four/validate on one. The paper does not state that CV folds are grouped by battery; these folds should not be called LOCO or guaranteed unseen-cell CV.
- All reported primary test results are cross-cell within their respective dataset. There is no demonstrated source-dataset model applied to another dataset without retraining, and no target-test-cell labeled adaptation. Repeated training under different SOC windows is window sensitivity, not fixed-feature cross-domain transfer. (pp. 9–12, 14; Tables 5–7.)

## 9. Quantitative results

Main errors are **RMSPE / MAPE**, both in %. Preserve RMSPE rather than relabeling it RMSE. (Table 7, p. 12.)

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| McMaster, fusion | Four training / two held-out cells | RMSPE / MAPE | 1.36% / 1.04% | Main fusion result |
| McMaster, partial-profile CNN | Same split | RMSPE / MAPE | 2.29% / 1.71% | Single-modality baseline |
| McMaster, histogram FNN | Same split | RMSPE / MAPE | 27.3% / 23.1% | Limited-data failure |
| Stanford, fusion | 100 training / 24 held-out cells | RMSPE / MAPE | 0.74% / 0.50% | Main fusion result |
| Stanford, partial-profile CNN | Same split | RMSPE / MAPE | 2.11% / 1.23% | Single-modality baseline |
| Stanford, histogram FNN | Same split | RMSPE / MAPE | 1.03% / 0.65% | PCA histogram baseline |
| Stanford four-cell case, fusion | Four selected training cells; defined held-out test group | RMSPE / MAPE | 1.40% / 1.05% | Main small-data fusion result |
| Stanford four-cell case, partial CNN | Same setup | RMSPE / MAPE | 2.41% / 1.39% | Baseline |
| Stanford four-cell case, histogram FNN | Same setup | RMSPE / MAPE | 52.05% / 47.47% | Small-data failure |
| McMaster fusion versus partial CNN | Four-cell training | Reported relative improvement | Approximately 40% | p. 13 |
| Stanford fusion versus histogram | 100-cell training | Reported relative improvement | Around 28% | p. 14 |
| Stanford fusion versus partial CNN | Four-cell training | Reported error reduction | Approximately 42% | p. 14 |
| Stanford four-cell fusion versus 100-cell partial CNN | Different training sizes, same dataset | Reported improvement | Approximately 34% | 1.40% versus 2.11% RMSPE; p. 14 |
| Stanford training-size comparison | 40-cell fusion versus 100-cell histogram | RMSPE / reported data reduction | 1.01% versus 1.03%; 60% less training data | Fig. 11 and p. 14; same-accuracy training requirement, not universal reduction |
| Stanford fusion trained from scratch | 100-cell training | RMSPE / MAPE | 0.89% / 0.57% | Table 8 |
| Stanford fusion, locked pretrained branches | Same setup | RMSPE / MAPE | 0.74% / 0.50% | Table 8 |
| Stanford fusion, unlocked pretrained branches | Same setup | RMSPE / MAPE | 0.84% / 0.52% | Table 8; neighboring prose instead says 0.83% RMSPE |

Additional training-size cases from Fig. 11 (p. 14):

| Stanford training cells | Histogram RMSPE | Fusion RMSPE |
|---:|---:|---:|
| 4 | 52.05% | 1.4% |
| 20 | 2.14% | 1.21% |
| 30 | 1.65% | 1.14% |
| 40 | 1.54% | 1.01% |
| 100 | 1.03% | 0.74% |

R², MAE, and numerical maximum-error summary: Not explicitly reported / not found in the paper. Scatterplot ±2%/±5% bands are reference bands, not claims that every estimate lies inside them.

## 10. Robustness / sensitivity results

Table 6 (p. 11) evaluates **partial-profile CNNs**, not the fusion model. Entries are RMSPE / MAPE; separate models are trained and sized for these comparisons.

| SOC location | McMaster | Stanford |
|---|---|---|
| 100%–86% | 2.65% / 2.02% | 4.78% / 2.94% |
| 86%–72% | 2.42% / 1.59% | 1.30% / 0.94% |
| 72%–58% | 2.68% / 2.03% | 1.25% / 0.91% |
| 58%–44% | 2.41% / 1.88% | 0.85% / 0.66% |
| 44%–30% | 1.64% / 1.36% | 1.04% / 0.75% |
| 30%–16% | 1.38% / 1.24% | 1.32% / 0.95% |

| SOC window length, errors across all locations | McMaster | Stanford |
|---|---|---|
| 7.2% | 2.33% / 1.62% | 2.80% / 1.76% |
| 14% | 2.29% / 1.71% | 2.11% / 1.23% |
| 28% | 2.16% / 1.48% | 1.54% / 1.10% |
| 42% | 2.00% / 1.57% | 1.22% / 0.87% |

- Representation ablation: Stanford histogram FNN without PCA gives RMSPE/MAPE 3.56%/1.85%, versus 1.03%/0.65% with PCA (Fig. 6b, p. 10).
- Limited-training-data robustness is quantified in Section 9; it is not a sensor-noise test.
- No quantitative noise injection, sampling/downsampling sensitivity, or independently isolated temperature/C-rate sweep is reported.

## 11. Physical interpretation / explainability

Measured capacity/voltage/IC curves and HPPC resistance expose nonunique relationships between profile shape and SOH. For example, DTW matches a BCR cell at 86.7% SOH to a CC voltage curve at 90.1% SOH and an IC curve at 89.1% SOH. The authors explain this through differing capacity/resistance aging and possible degradation modes; measured resistance supports the mismatch, while specific SEI/lithium-inventory/material-loss allocations remain interpretations. Histogram fusion supplies operational-history information; CNN contributions are not explained with SHAP or a demonstrated feature-attribution method. (pp. 5–6, 12; p. 15 lists interpretability as future work.)

## 12. Computational information

Measured on the Stanford setup; execution time is total test execution time divided by the number of test data points. PC: 2021 Apple MacBook M1; edge: NVIDIA Jetson Nano. (Table 9, p. 15.)

| Model | Model size | PC execution per data point | Jetson Nano execution per data point |
|---|---:|---:|---:|
| Partial-profile CNN | 1.77 MB | 0.15 ms | 14.50 ms |
| Histogram FNN | 0.08 MB | 0.0015 ms | 0.1042 ms |
| Multi-modal fusion | 1.97 MB | 0.31 ms | 15.63 ms |

Histogram FNN with PCA has 19,329 learnable parameters, versus 184,833 without PCA (p. 10). This is not the fusion parameter count. Training/CV used a four-NVIDIA-A100 server, but timed training/search/PCA extraction, total deployment RAM, fusion parameter count, and FLOPs/MACs are not explicitly reported. Architecture details assigned to supplementary Fig. S2 are absent from the supplied PDF.

## 13. Direct relevance to GSI

- Strong comparison axes: partial-profile information, region sensitivity, and reliability under different degradation histories; the main experiments specifically use discharge.
- No hand-built finite ΔV scalar, geometric reference distance, or BOL feature normalization is reported; the representation combines learned multi-channel features and cumulative history.
- Transfer here means pretrained modality encoders reused in a fusion estimator, not frozen cross-chemistry/dataset transfer. Target-test-cell adaptation is not demonstrated.
- Can motivate region sensitivity, unseen-cell evaluation, operational-history comparison, and computational benchmarks; the measured 1.97 MB/15.63 ms fusion model supplies a concrete deployment comparator.

## 14. One-sentence Related Work summary

Chen et al. fused CNN representations of partial discharge voltage/current/temperature profiles with FNN representations of PCA-compressed operational histograms and used a pretrained multi-modal fusion network for SOH estimation, achieving RMSPE/MAPE of 1.36%/1.04% on two held-out McMaster cells and 0.74%/0.50% on 24 held-out Stanford cells.

# Yao_2025

## 1. Bibliographic information

- Full title: Battery state of health estimation with interpretable distance feature and dynamic weight model across-chemistry and working conditions.
- Authors: Xing-Yan Yao; Liwei Chen.
- Journal: Energy.
- Year: 2025.
- Volume / issue / article number: 332 / issue not explicitly reported / 137175.
- DOI: 10.1016/j.energy.2025.137175. (p. 1.)

## 2. Research objective

- Construct interpretable scalar distances between a selected reference Shapelet and CC charging voltage–time segments.
- Compare minimum-distance matching (minED) and matching at the same relative position (VMED).
- Combine four neural estimators using error-dependent weights and target-domain fine-tuning across chemistries and operating conditions. (pp. 5–9.)

## 3. Battery data and experimental setting

- Battery chemistry: XJTU Batch-1 NCM523; Oxford LCO + NCO; Tongji dataset 1 NCA, dataset 2 NCM (table header also spells NMC), dataset 3 NCA + NCM.
- Cell format / nominal capacity: XJTU NCM523 18650, 2 Ah, nominal voltage 3.6 V; Oxford pouch, 0.740 Ah; Tongji NCA and NCM 18650, each 3.5 Ah; Tongji mixed NCA + NCM 18650, 2.5 Ah.
- Number of cells: XJTU full source contains 55 cells in six batches; analyzed Batch-1 has eight. Oxford eight. Tongji total 130: Table 1 lists condition-specific counts below; these are dataset counts, not separately reported test-cell counts.
- Dataset name/source: XJTU, Oxford, and three Tongji University datasets, treated as five datasets.
- Charge/discharge protocol: CC charging voltage–time data supply the Shapelets; Oxford described as CC–CV charge followed by a drive-cycle discharge. Exact CV cutoff-current/rest details for all datasets: Not explicitly reported.
- Temperature: XJTU room temperature; Oxford 40 °C; Tongji 25/35/45 °C by condition.
- C-rate: Condition-specific charge/discharge values below.
- Full or partial profile: Sliding local subsequences extracted from full recorded CC charging histories; the feature is local, but arbitrary incomplete-charge availability is not independently validated.
- Charge or discharge: CC charging features.
- Observed voltage/capacity/time region: Dataset voltage limits below; feature windows use optimized sample lengths/steps rather than one fixed voltage window.
- Sampling rate, if reported: Not explicitly reported. Sliding-window “length” is a sample count, not a duration. (pp. 3, 5, 7–9; Tables 1, 4–5.)

| Dataset | Temperature | Charge/discharge rate | Cells | Voltage limits | Condition label |
|---|---|---|---:|---|---|
| XJTU Batch-1 | Room temperature | 2C / 1C | 8 | 2.5–4.2 V | — |
| Oxford | 40 °C | 1C / 1C in Table 1 | 8 | 2.7–4.2 V | —; prose additionally describes drive-cycle discharge |
| Tongji 1, NCA | 25 °C | 0.25C / 1C | 7 | 2.65–4.2 V | CY25-025_1 |
| Tongji 1, NCA | 25 °C | 0.5C / 1C | 19 | 2.65–4.2 V | CY25-05_1, source domain |
| Tongji 1, NCA | 25 °C | 1C / 1C | 9 | 2.65–4.2 V | CY25-1_1 |
| Tongji 1, NCA | 35 °C | 0.5C / 1C | 3 | 2.65–4.2 V | CY35-05_1 |
| Tongji 1, NCA | 45 °C | 0.5C / 1C | 28 | 2.65–4.2 V | CY45-05_1 |
| Tongji 2, NCM | 25 °C | 0.5C / 1C | 23 | 2.5–4.2 V | CY25-05_1 |
| Tongji 2, NCM | 35 °C | 0.5C / 1C | 4 | 2.5–4.2 V | CY35-05_1 |
| Tongji 2, NCM | 45 °C | 0.5C / 1C | 28 | 2.5–4.2 V | CY45-05_1 |
| Tongji 3, NCA + NCM | 25 °C | 0.5C / 1C | 3 | 2.5–4.2 V | CY25-05_1 |
| Tongji 3, NCA + NCM | 25 °C | 0.5C / 2C | 3 | 2.5–4.2 V | CY25-05_2 |
| Tongji 3, NCA + NCM | 25 °C | 0.5C / 3C **as printed** | 3 | 2.5–4.2 V | CY25-05_4 **as printed** |

The last row's rate and label conflict: the label and later prose suggest 4C, but Table 1 says 3C. Retain both; do not silently choose one. (Table 1, p. 3; pp. 5, 17.)

## 4. Input data

- CC charging voltage and its sampling time, forming two-dimensional \((t,V)\) sequences.
- Labeled SOH for reference-Shapelet/window selection, source training, target fine-tuning, and estimation-error-dependent weighting.
- No current/temperature channel is used to calculate the proposed distances, although the datasets encompass different rates/temperatures. Capacity supplies aging/SOH information, not the two-dimensional Shapelet coordinates. (pp. 5–9.)

## 5. Feature / representation construction

For each cycle, min–max normalize voltage and time using

\[
X_{norm}=\frac{X-\min(X)}{\max(X)-\min(X)},
\]

and divide the two-dimensional time series into candidate Shapelets of length \(l\) and step \(s\). For a candidate reference \(R\), compute a cyclewise distance series:

\[
d_i^{minED}=\min_j ED(R,S_{i,j}),\qquad
d_i^{VMED}=ED(R,S_{i,j_R}),
\]

where VMED matches the subsequence at the same position as the reference. ED is the Euclidean distance over the voltage/time coordinates of equal-length Shapelets. Eq. 3 in the PDF repeats the S1 subscript on both terms of its differences; the verbal definition and matching diagrams identify a distance between two different Shapelets, not a zero self-distance. The compact notation above follows that stated operation rather than reproducing the subscript typo. (pp. 6–8, Eqs. 3–8; Fig. 4.)

Choose the reference whose full distance series has maximum absolute Pearson correlation with labeled SOH:

\[
R=\operatorname*{arg\,max}_{R\in CanShapelets}|PCC(\mathbf d_R,\mathbf{SOH})|.
\]

Each method produces one scalar DF per cycle, not an automatically combined two-feature vector. The reference may come from early **or late** aging; it is not constrained to the BOL cycle. Min–max coordinate normalization is separate from reference selection and distance computation. Differentiation, fixed finite ΔV construction, and ICA/DVA are not needed for these DFs. Input sequence/historical context length used by each neural learner is not explicitly reported. (pp. 6–9.)

## 6. Feature/window selection

- Optimize sliding length and step using **genetic programming (GP)**, as named by the authors; GP here is not Gaussian-process optimization.
- Fitness is Pearson correlation between DF and labeled SOH; select the reference using maximum |PCC|.
- Selection uses labeled source and target training-cell aging data. It is repeated for each chemistry/condition; target references/window parameters are not held frozen from the source.
- The first target cell is used except Tongji dataset 2 CY25-05_1, where cell #5 is selected to provide a more complete aging trajectory.
- Window examples: minED length/step = 5/261 for Tongji 1 CY25-025_1-#1, 600/40 for Oxford Cell1, 680/50 for XJTU 2C_Battery-1; VMED values for the same cases = 126/1, 187/1, 768/10. Final settings differ substantially across domains. (pp. 8–9, Tables 4–5.)

## 7. Estimation model

- Model / estimator: Dynamic Weight Model (DWM), with or without transfer learning (DWM-TL), combining LSTM, GRU, CNN, and Transformer base learners.
- Model inputs: minED or VMED DF representation.
- Output: SOH.
- Online/offline learning: Source pretraining and labeled target fine-tuning; weighting described as dynamic/error-based. A complete online label-acquisition and update schedule is not reported.
- Fine-tuning or adaptation: Freeze each learner's initial layer, retrain later and fully connected layers on labeled target data.
- Hyperparameter optimization: GP optimizes Shapelet windows; five-fold validation chooses the final model. Detailed base-network architectures/hyperparameters are not explicitly reported.
- Ensemble, if any: \(w_i=(1/e_i)/\sum_{j=1}^{4}(1/e_j)\), with target-domain RMSE errors \(e_i\); \(SOH_{DWM}=\sum_i w_iSOH_i\). Evaluation subsets/timing for every weight refresh are not fully specified. (pp. 8–9, Eqs. 9–10.)

## 8. Validation protocol

- **Source:** All NCA cells in Tongji dataset 1 CY25-05_1; Table 1 lists 19 source cells. Source data split 8:2 training/validation; whether this split is temporal, random-cycle, or cellwise is not stated.
- **Targets:** Other Tongji chemistry/condition groups, Oxford, and XJTU. Labeled first-cell data per target condition support feature optimization and fine-tuning; Tongji dataset 2 CY25-05_1 uses cell #5 instead.
- **Cross-cell evaluation:** Figures show estimates for multiple target batteries after training/adaptation on designated target cells. Exact exclusion accounting, separate test-cell count for every condition, and cellwise grouping of the five-fold validation are not explicitly reported. Do not derive an exact test count by subtracting one from each dataset count without a stated evaluation roster.
- **Cross-dataset/cross-chemistry adaptation:** Source-to-target transfer includes target-domain labeled feature construction and model fine-tuning. It is not label-free application to an unseen chemistry, nor frozen-reference transfer.
- Five-fold validation is reported; LOCO and same-cell temporal held-out test boundaries are not specified. No target-label fraction or “first few cycles only” restriction is reported: target training-cell aging trajectories are used. (pp. 8–11, Sections 3.4–4.4.)

## 9. Quantitative results

The PDF contains **two inconsistent series of DWM-TL condition results**. Retain both with provenance. Pairs are **MAE / RMSE**, in %, using the authors' SOH-difference definitions in Eqs. 11–12; they are not RMSPE. Do not average conflicting entries or present abstract minima as a universal result.

**Chemistry/condition and weighting comparisons:** Tables 7–8 and 18–19 (pp. 10–11, 15) report the following. Dataset 1 denotes NCA, dataset 2 NCM, dataset 3 NCA + NCM. Each target uses labeled domain-specific feature selection and fine-tuning.

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| Tongji 1 CY25-025_1 | Adapted target, minED / VMED | MAE / RMSE | 0.706% / 0.833%; 1.781% / 2.047% | Tables 8, 18–19 |
| Tongji 1 CY25-1_1 | Same | MAE / RMSE | 2.145% / 2.516%; 2.765% / 3.635% | Tables 8, 18–19 |
| Tongji 1 CY35-05_1 | Same | MAE / RMSE | 1.425% / 1.875%; 0.597% / 0.791% | Tables 7–8, 18–19 |
| Tongji 1 CY45-05_1 | Same | MAE / RMSE | 3.459% / 4.031%; 1.132% / 1.236% | Tables 7–8, 18–19 |
| Tongji 2 CY25-05_1 | Same; target training cell #5 | MAE / RMSE | 1.713% / 1.866%; 0.929% / 0.985% | Tables 7–8, 18–19 |
| Tongji 2 CY35-05_1 | Adapted target, minED / VMED | MAE / RMSE | 3.313% / 3.619%; 0.527% / 0.695% | Tables 7–8, 18–19 |
| Tongji 2 CY45-05_1 | Same | MAE / RMSE | 1.351% / 1.603%; 2.262% / 2.807% | Tables 7–8, 18–19 |
| Tongji 3 CY25-05_1 | Same | MAE / RMSE | 0.510% / 0.819%; 2.160% / 3.181% | Tables 7–8, 18–19 |
| Tongji 3 CY25-05_2 | Same | MAE / RMSE | 0.425% / 0.703%; 1.527% / 1.950% | Tables 8, 18–19 |
| Tongji 3 CY25-05_4 | Same | MAE / RMSE | 0.592% / 0.777%; 1.196% / 1.781% | Tables 8, 18–19 |

**Base-model transfer comparison:** DWM-TL rows in Tables 13–16 (p. 14). Some values differ from the preceding table despite the same condition/method labels.

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| Tongji 1 CY25-025_1 | Adapted target, minED / VMED | MAE / RMSE | 0.639% / 0.723%; 1.781% / 2.047% | Tables 13, 15 |
| Tongji 1 CY25-1_1 | Same | MAE / RMSE | 2.145% / 2.516%; 2.765% / 3.635% | Tables 13, 15 |
| Tongji 1 CY35-05_1 | Same | MAE / RMSE | 1.115% / 1.623%; 0.597% / 0.791% | minED conflicts with Tables 7–8/18 |
| Tongji 1 CY45-05_1 | Same | MAE / RMSE | 3.426% / 4.011%; 1.132% / 1.236% | Tables 13, 15 |
| Tongji 2 CY25-05_1 | Same; target training cell #5 | MAE / RMSE | 1.713% / 1.866%; 0.929% / 0.985% | Tables 13, 15 |
| Tongji 2 CY35-05_1 | Adapted target, minED / VMED | MAE / RMSE | 3.011% / 3.219%; 0.439% / 0.673% | VMED conflicts with 0.527% / 0.695% in Tables 7–8/19 |
| Tongji 2 CY45-05_1 | Same | MAE / RMSE | 0.965% / 1.109%; 2.262% / 2.807% | Tables 13, 15 |
| Tongji 3 CY25-05_1 | Same | MAE / RMSE | 0.409% / 0.699%; 2.160% / 3.181% | minED pair quoted by the abstract |
| Tongji 3 CY25-05_2 | Same | MAE / RMSE | 0.421% / 0.683%; 1.527% / 1.950% | Table 13 RMSE is below the abstract's stated minED minimum of 0.699% |
| Tongji 3 CY25-05_4 | Same | MAE / RMSE | 0.515% / 0.735%; 1.196% / 1.781% | Tables 13, 15 |
| XJTU Batch-1 | Source transfer + labeled target fine-tuning, minED / VMED | MAE / RMSE | 1.467% / 1.887%; 1.035% / 1.101% | Tables 14, 16 |
| Oxford | Same | MAE / RMSE | 1.797% / 1.902%; 1.159% / 1.301% | Tables 14, 16; minED DWM-TL is not the best Oxford base-model result |

**Without-TL DWM results:** These are distinct experimental cases, not the DWM-TL values above. (Tables 9–12, p. 13.)

| Dataset / case | Validation setup | Metric | Reported value | Notes |
|---|---|---|---|---|
| Tongji 1 CY25-025_1 | DWM without TL, minED / VMED | MAE / RMSE | 0.715% / 0.846%; 1.752% / 2.014% | Tables 9, 11 |
| Tongji 1 CY25-1_1 | Same | MAE / RMSE | 2.208% / 2.584%; 2.565% / 3.289% | Tables 9, 11 |
| Tongji 1 CY35-05_1 | Same | MAE / RMSE | 1.522% / 1.930%; 0.794% / 0.987% | Tables 9, 11 |
| Tongji 1 CY45-05_1 | Same | MAE / RMSE | 3.463% / 4.030%; 0.954% / 1.203% | Tables 9, 11 |
| Tongji 2 CY25-05_1 | Same | MAE / RMSE | 1.714% / 1.869%; 0.930% / 0.998% | Tables 9, 11 |
| Tongji 2 CY35-05_1 | Same | MAE / RMSE | 3.194% / 3.471%; 0.541% / 0.706% | Tables 9, 11 |
| Tongji 2 CY45-05_1 | Same | MAE / RMSE | 1.441% / 1.711%; 2.262% / 2.806% | Tables 9, 11 |
| Tongji 3 CY25-05_1 | Same | MAE / RMSE | 0.530% / 0.835%; 2.179% / 3.202% | Tables 9, 11 |
| Tongji 3 CY25-05_2 | Same | MAE / RMSE | 0.503% / 0.787%; 1.524% / 1.945% | Tables 9, 11 |
| Tongji 3 CY25-05_4 | Same | MAE / RMSE | 0.626% / 0.835%; 1.177% / 1.740% | Tables 9, 11 |
| XJTU Batch-1 | DWM without TL, minED / VMED | MAE / RMSE | 1.471% / 1.889%; 1.143% / 1.298% | Tables 10, 12 |
| Oxford | Same | MAE / RMSE | 1.852% / 2.011%; 1.313% / 1.575% | Tables 10, 12 |

Additional reported comparison summaries:

- Weight-strategy comparison: minED DWM-TL mean MAE/RMSE = 1.564%/1.864%, versus softmax-TL 1.616%/1.920% and simple averaging-TL 1.626%/1.933% over the three Tongji datasets (p. 15, Table 18 context).
- VMED DWM-TL mean MAE/RMSE = 1.488%/1.911% in the weighting comparison (p. 15, Table 19 context).
- The prose reports average MAE/RMSE improvements of 48.33%/48.38% with minED DWM-TL versus DWM; aggregation scope is not clearly reconciled with the displayed tables (p. 14). Preserve as a reported claim, not a recomputed universal improvement.
- The conclusion states 10%–25% improvement using DFs; the exact metric/case mapping is not specified there (p. 17).
- R², MAPE/RMSPE, and numerical maximum-error summary: Not explicitly reported / not found in the paper.

## 10. Robustness / sensitivity results

- The condition-specific errors above explicitly cover changes in temperature, charging rate, discharge rate, chemistry, and dataset **with labeled target adaptation**. They should not be called robustness of a completely frozen estimator.
- VMED helps some NCA/NCM cases but is worse on the mixed-chemistry Tongji 3 cases; minED is not uniformly best either (pp. 11–12, 16–17).
- Feature correlations are not uniformly above 0.95: Table 4 gives XJTU minED |PCC| = 0.9309; Table 5 gives mixed-chemistry CY25-05_1 VMED |PCC| = 0.89874. Table 4 and Table 6 also conflict for Tongji 2 CY25-05_1 minED (0.9848 versus 0.8871). Thus the prose's high-correlation statements need these qualifications (pp. 9–10).
- GP-selected sample windows are reported per domain, but controlled window-width/noise/downsampling sensitivity curves are not explicitly evaluated. A short local Shapelet is not sufficient evidence of arbitrary partial-charge coverage.

## 11. Physical interpretation / explainability

Distances track upward/leftward motion and shortening of CC voltage–time curves during aging. minED quantifies the closest local pattern; VMED reflects change at the same relative segment position. The authors relate differences between these representations to chemistry-dependent curve motion, particularly the mixed NCA + NCM trajectories. This is phenomenological geometric/curve-evolution interpretation; no direct ICA/DVA degradation-mode diagnosis, postmortem attribution, or SHAP explanation is demonstrated. (pp. 6–7, 16–17, Figs. 3, 13–14.)

## 12. Computational information

- **GP window search:** Tongji 1 CY25-025_1-#1, population 20 and generation 1: minED 6 h 23 min 35 s; VMED 14 min 12 s (p. 9).
- **Distance-feature calculation:** Same named battery, fixed length 100/step 20: minED 5 min 46 s, PCC −0.98432; VMED 18 s, PCC 0.99399. This is a different benchmark from GP search (pp. 15–16).
- **Model timing:** Table 17 uses source CY25-05_1 and target CY35-05_1 in Tongji dataset 1. Times are reported training/testing runs, not explicitly per-cycle inference. Do not convert 0.016 s into a claimed per-estimate latency.

| Model | Training time | Testing time | MAE / RMSE in the timing table |
|---|---:|---:|---|
| LSTM | 5.062 s | 0.331 s | 6.439% / 8.360% |
| GRU | 13.181 s | 0.294 s | 4.580% / 5.443% |
| CNN | 5.163 s | 0.045 s | 7.230% / 9.061% |
| Transformer | 7.253 s | 0.186 s | 5.451% / 6.044% |
| DWM | 30.244 s | 0.193 s | 1.522% / 1.930% |
| LSTM-TL | 15.387 s | 1.611 s | 1.304% / 1.905% |
| GRU-TL | 30.946 s | 0.050 s | 1.772% / 2.215% |
| CNN-TL | 13.147 s | 0.022 s | 1.263% / 1.743% |
| Transformer-TL | 144.031 s | 0.182 s | 1.852% / 2.346% |
| DWM-TL | 180.262 s | 0.016 s | 1.425% / 1.875% |

The timing-table DWM-TL pair follows Tables 7–8/18 rather than Table 13's 1.115%/1.623%. Hardware, model size, deployment RAM, parameter count, FLOPs/MACs, and isolated per-sample inference timing: Not explicitly reported / not found in the paper. (p. 15.)

## 13. Direct relevance to GSI

- Strong comparison axes: partial local voltage–time geometry, reference distances, derivative-free construction, and one scalar DF per cycle.
- Reference Shapelets are selected by labeled SOH correlation and may be late-life; they are not fixed BOL references. Coordinate min–max scaling is already present, whereas explicit BOL feature normalization and finite ΔV feature construction are not reported.
- Target feature/window/reference selection and supervised model fine-tuning are already used; these must be distinguished from any GSI experiment with frozen source features.
- Can motivate frozen-feature transfer, BOL-reference ablation, unseen-cell evaluation, cross-condition robustness, and separate search/extraction/inference benchmarks. Key GSI differences require its actual definition; no novelty assertion is supported here.

## 14. One-sentence Related Work summary

Yao et al. constructed scalar minED/VMED distances from SOH-correlated charging voltage–time Shapelets and used an error-weighted LSTM/GRU/CNN/Transformer ensemble with target fine-tuning for SOH estimation, reporting MAE/RMSE of 0.409%/0.699% for minED on Tongji mixed-chemistry CY25-05_1 and 0.439%/0.673% for VMED on Tongji NCM CY35-05_1 in their base-model transfer comparison.

# Cross-paper comparison

## A. Technical comparison table

Results refer to the source locations and qualifications in each paper's Sections 8–12. Feature dimensions are constructed representations, not neural latent dimensions or parameter counts.

| Paper | Partial profile | Charge/discharge | Main feature | Feature dimension | Reference/normalization | Model | Validation type | Best/main reported result | Target adaptation | Physical interpretation | Computational result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Naha_2020 | 10–20 min | Charge | Capacity-indexed corrected finite ΔV + temperature | 10 | First-cycle resistance; rated-capacity scale | ANN, 100 hidden nodes | 2 train / 16 held-out cells; rates/capacities vary | Every test-cell MAE <1%; relative AE definition | No target-label fine-tuning | Simplified OCV/SEI resistance–capacity model | Complexity expressions; no measured inference/memory |
| Wen_2022 | Shallow finite-voltage interval | Both; principal fitting/prediction discharge | ΔSOC = CΔt | 1 | Rated-capacity SOC; extrapolated ΔSOC at SOH = 1 | Per-cell calibrated linear relation | Per-cell fitting/prediction with correction; external-dataset relation checks | 48-cell prediction MAE within 0.7%, ME 0.5%–2% | Per-cell slope correction; no frozen source transfer | ICA evolution and linear-regime boundaries | Qualitative; less-than-few-minutes measurement claim |
| Petkovski_2024 | Full + ten partial windows | Discharge | Log variance/minimum of ΔQ(V), cumulative temperature | 2 or 3 | Own cycle-10 curve subtraction | Gaussian SVR | 109 train/CV / 15 held-out cells; CV grouping unspecified | Full test mean R² 0.9620; best partial 0.9728 | No; interval-specific models trained | Curve change and window informativeness | Qualitative; no timed benchmark |
| Qin_2024 | IC/shape-selected and narrower windows | Charge | Chord length, slope, angular sine | 3 constructed | Initial-feature self-scaling | OSELM | Same-battery supervised sequential updates, four estimation cases | Oxford MAE 0.0637%, MaxAE 0.1683%; Cell 60 1.4038%/2.3457% | Online labeled updates; per-application region choice | IC-guided geometry; no direct mode attribution | Qualitative; no timed benchmark |
| Chen_2025 | ~14% SOC + operation history | Main experiments discharge | Learned V/I/T representation + PCA histograms | 3 profile channels; histograms 12/69 PCs; fused dimension not found | PCA; no reported BOL reference operation | CNN + FNN encoders, FNN fusion | McMaster 4/2 and Stanford 100/24 cell splits; shuffled five-fold internal CV | Fusion RMSPE/MAPE 1.36%/1.04% and 0.74%/0.50% | Modality-to-fusion pretraining; no cross-dataset target adaptation | Measured profile/resistance mismatch; no neural attribution | 1.97 MB; 0.31 ms PC / 15.63 ms Jetson per data point |
| Yao_2025 | Local Shapelets from CC histories | Charge | minED or same-position VMED distance | 1 per method per cycle | Selected early/late reference; min–max coordinates | DWM-TL, four neural learners | Source 8:2; target-cell feature selection/fine-tuning; five-fold grouping unspecified | Tables 13/15: minED 0.409%/0.699%, VMED 0.439%/0.673% MAE/RMSE; conflicting table series retained | Yes; both feature re-selection and model fine-tuning | Phenomenological curve motion | Search 6 h 23 min 35 s vs 14 min 12 s; DWM-TL testing run 0.016 s |

## B. Related Work-ready facts

### Naha_2020

- Technical method: Nine resistance-corrected voltage differences at adjacent 1.5%-rated-capacity increments plus average temperature; synthetic training curves from early cycling (pp. 4–5, 9–10).
- Model: ANN with ten inputs, 100 hidden nodes, one output (p. 5).
- Validation: Two Type-1 training cells; 16 separate LCO/graphite test cells at 25/45 °C, 0.8/1.0/1.2C charge, 3.0/3.5 Ah (Table 3, p. 8).
- Quantitative result: MAE <1% in each test case, using absolute relative error; MaxE <1.5% except one case (p. 6, Fig. 4).

### Wen_2022

- Technical method: Scalar ΔSOC from traversal time in a sliding finite ΔV CC window; Spearman region analysis and ICA-based linear-regime check (pp. 3–7).
- Model: Calibrated linear SOH–ΔSOC relation with slope and value extrapolated to SOH = 1 (Eq. 2, p. 7).
- Validation: Same-cell fitting and calibrated prediction on 48 LISHEN cells, with one slope correction; separate evolution/fitting checks on eight Kokam and 45 A123 cells (pp. 5–8).
- Quantitative result: LISHEN prediction MAE within 0.7%, ME 0.5%–2%; LISHEN fit ME 0.4%–1.4%, A123 fit ME 0.4%–2.0% (p. 8).

### Petkovski_2024

- Technical method: Common-grid interpolation and cycle-10 subtraction of discharge Q(V); logarithmic variance/minimum features plus cumulative average temperature (Eq. 3, p. 7).
- Model: Gaussian SVR; select two-/three-feature combinations and tune separately per window with five-fold CV (pp. 7–10).
- Validation: 109 training/validation cells and 15 whole-cell holdouts from 124 LFP cells; per-cell test R² averaged across holdouts (pp. 7–8, 11).
- Quantitative result: Full-window mean test R² 0.9620; best partial mean 0.9728 at 2.2–2.4 V; unsuccessful high windows 0.8639 at 3.15–3.4 V and 0.8473 at 3.25–3.4 V (Table 5, p. 11).

### Qin_2024

- Technical method: IC/curve-shape-selected partial charging intervals; chord length, slope, and angular sine, divided by their own initial values (pp. 3–5).
- Model: Supervised online sequential ELM updates (pp. 5, 9).
- Validation: Same-battery initialization/adaptation on NASA B0007, CALCE CS2-37, Oxford Cell 5, and Cell 60; two initialization samples, update step 4, prediction step 2 (p. 9).
- Quantitative result: MAE/MaxAE = 0.4948%/1.6458%, 0.3552%/1.9675%, 0.0637%/0.1683%, and 1.4038%/2.3457%, respectively (Table 8, p. 9).

### Chen_2025

- Technical method: Partial discharge V/I/T CNN representations fused with FNN representations of cumulative operational histograms reduced by PCA at a 99% threshold (pp. 7–9).
- Model: Modality-pretrained CNN/FNN encoders with a fusion FNN; principally frozen encoders, with histogram-branch exceptions under limited data (pp. 8–9).
- Validation: Four McMaster training/two held-out cells; 100 Stanford training/24 held-out cells; reduced four-cell Stanford training case (Table 5, p. 9; Table 7, p. 12).
- Quantitative result: Fusion RMSPE/MAPE 1.36%/1.04%, 0.74%/0.50%, and 1.40%/1.05%, respectively; 40-cell fusion RMSPE 1.01% versus 100-cell histogram 1.03%, supporting the reported 60% training-data reduction (pp. 12–14).

### Yao_2025

- Technical method: Normalize CC voltage–time coordinates, optimize reference Shapelets by labeled |PCC|, and compute scalar minED or same-position VMED distances; reselect features per target condition (pp. 6–9).
- Model: RMSE-inversely-weighted LSTM/GRU/CNN/Transformer ensemble with source pretraining and supervised target fine-tuning (pp. 8–9).
- Validation: Tongji NCA CY25-05_1 source, 8:2 source split; labeled target training-cell aging data for adaptation; other Tongji conditions/chemistries, Oxford, and XJTU evaluated; exact condition test rosters/fold grouping not specified (pp. 8–11).
- Quantitative result: Base-model transfer tables report minED MAE/RMSE 0.409%/0.699% on Tongji 3 CY25-05_1 and VMED 0.439%/0.673% on Tongji 2 CY35-05_1; Tables 8/18–19 instead give 0.510%/0.819% and 0.527%/0.695% for those cases (pp. 11, 14–15).

## C. Missing-information checklist

“Not found” below means **Not explicitly reported / not found in the paper.** Presence of a computational-complexity claim is distinguished from presence of a measured benchmark.

| Paper | Quantitative SOH metric | Validation split | Number of cells | Window-selection method | Computational benchmark | Physical interpretation |
|---|---|---|---|---|---|---|
| Naha_2020 | Found: aggregate per-test-cell bounds; exact bar values not found | Cell split found; independent validation/CV not found | Found: 18, including 2/16 split | Fixed start/increments found; actual common test start not found | Measured runtime/memory not found; complexity given | Found: simplified resistance/SEI and curve evolution |
| Wen_2022 | Found for LISHEN/A123; Kokam SOH error metric not found | Conventional train/test ratio and exact calibration/test boundaries not found | Found: 48, 8, 45 | Spearman scan/ICA regime found; training-only isolation not found | Measured runtime/memory not found | Found: ICA evolution and degradation-rate correlations |
| Petkovski_2024 | Found: R²; numerical RMSE/MAE not found | 109/15 found; CV fold grouping not found | Found: 124 | Predefined intervals + labeled CV feature choice found | Measured runtime/memory not found | Found: phenomenological curve/window interpretation; direct mode attribution not found |
| Qin_2024 | Found: MAE/MaxAE; Table 9 Cell 60 pair inconsistent | Sequential update settings found; fixed train/test partition not found | Found: 6 public + 1 studied pack cell; 96 is pack size | IC/shape rule found; threshold δ not found | Measured runtime/memory not found | Found: IC-guided geometry; direct degradation-mode attribution not found |
| Chen_2025 | Found: RMSPE/MAPE | Whole-cell splits found; CV battery grouping not found | Found: 6 and 124 | SOC length/position comparison found; training-only PCA/window-selection scope not found | Found: model MB and per-data-point PC/Jetson times; training time not found | Found: measured resistance/profile mismatch; neural attribution not found |
| Yao_2025 | Found: MAE/RMSE; multiple inconsistent table series | Source 8:2/target training-cell rule found; exact target test rosters/fold grouping not found | Dataset/group counts found; separate test counts not found | Labeled GP/absolute-Pearson-correlation selection per domain found | Found: search/extraction and training/testing runs; hardware/per-sample inference/memory not found | Found: curve-motion/distance interpretation; direct degradation-mode attribution not found |

Additional drafting checks: Wen's ambiguous fitting-MAE wording and printed ME equation; Petkovski's 2024 citation versus December 2023 publication date; Qin's NASA temperature discrepancy and erroneous one-step Cell 60 table pair; Chen's charge/discharge terminology and 0.84%/0.83% fine-tuning discrepancy; Yao's condition-rate mismatch, correlation discrepancies, and conflicting performance tables. None has been resolved using external sources or assumptions.

## D. Suggested 3-paragraph grouping for the manuscript

### Paragraph 1: Simple / regional / partial-profile features

- Papers: Naha_2020 and Wen_2022.
- Technical reason: Both construct compact indicators from a partial CC profile and a finite interval. Naha uses nine capacity-indexed voltage increments plus temperature and an ANN; Wen uses one voltage-window SOC increment and a calibrated linear relation.
- Naha result to mention: MAE <1% across 16 distinct test cells; retain the relative-error definition and the held-out-cell context (p. 6; Table 3).
- Wen result to mention: MAE within 0.7%, ME 0.5%–2% for calibrated 48-cell sequential prediction with one slope correction, rather than calling this held-out-cell accuracy (p. 8).

### Paragraph 2: Geometric / reference-based representations

- Papers: Petkovski_2024 and Qin_2024.
- Technical reason: Petkovski summarizes deviations from an early reference curve; Qin describes partial voltage–time geometry and normalizes each geometric feature by its initial value. Both explicitly separate representation construction from their respective SVR/OSELM estimators.
- Petkovski result to mention: Mean test R² 0.9620 over full discharge and 0.9728 for the best partial window on 15 held-out cells; include high-window failures if discussing region sensitivity (Table 5).
- Qin result to mention: MAE 0.0637% on Oxford Cell 5 and 1.4038% on the experimental 57 Ah cell under labeled online updating, or the complete four-case MAE sequence when space permits (Table 8).

### Paragraph 3: Transfer / multimodal / domain-adaptive representations

- Papers: Chen_2025 and Yao_2025.
- Technical reason: Chen reuses modality-specific pretrained encoders to fuse partial profiles and operational histories; Yao transfers a neural ensemble across conditions/chemistries with labeled target feature re-selection and fine-tuning. These are distinct uses of transfer and should be named separately.
- Chen result to mention: RMSPE 0.74% on 24 held-out Stanford cells and 1.36% on two held-out McMaster cells; optionally the 60% lower training-cell requirement at approximately 1% RMSPE (Tables 5/7; Fig. 11).
- Yao result to mention: Table 13 minED MAE/RMSE 0.409%/0.699% and Table 15 VMED 0.439%/0.673%, with explicit target-label adaptation and table provenance; do not describe these as frozen unseen-domain performance. If manuscript space cannot accommodate the source conflict, use a clearly identified single table/case rather than a universal “best” claim.
