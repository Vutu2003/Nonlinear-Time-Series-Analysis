# Protocol Freeze v1

## 1. research_questions

### RQ1 — Existence
**Do PPG signals acquired during awake and drowsy states exhibit statistically significant deterministic nonlinear dynamics beyond noisy pseudoperiodicity?**

### RQ2 — State-Dependent Nonlinear Dynamics
**Does the nonlinear dynamical organization of PPG change significantly between awake and drowsy states?**

### RQ3 — Raw PPG vs PPI
**Are state-dependent nonlinear changes primarily expressed in the raw PPG waveform, in pulse-to-pulse interval dynamics, or in both?**

---

## 2. dataset_roles

- **Primary dataset:** dữ liệu của nhóm.
- 25 sessions, từ 10 participants.
- Sampling rate: `fs = 50 Hz`.
- Mỗi session thường > 30 phút.
- Hoàn thành toàn bộ pipeline trên primary dataset trước.

External stage:
1. Ưu tiên tìm public dataset có **PPG + drowsiness** để independent replication.
2. Nếu không có dataset phù hợp, dùng **CLAS** cho physiological-state generalization, không gọi là drowsiness validation.

---

## 3. label_rules

- Sử dụng nguyên trạng labels đã có trong các file CSV.
- Không relabel dựa trên kết quả NTSA.
- Primary analysis chỉ dùng các đoạn được gán rõ:
  - `Awake`
  - `Drowsy`
- Các label khác/không rõ nếu có sẽ bị loại khỏi primary analysis và được ghi vào exclusion log.
- Label được xem là fixed external input.

---

## 4. analysis_units

Primary analysis unit:

`recording session`

Có 25 sessions nhưng subject-session mapping không còn khả dụng.

Do đó:

- xử lý 25 sessions như session-level observational units;
- không coi windows là independent samples;
- không tuyên bố có 25 independent subjects;
- manuscript phải nêu rõ dataset gồm 25 sessions từ 10 participants nhưng không còn participant mapping.

Nếu một state có nhiều windows trong cùng session:

`windows -> session × state summary`

Ưu tiên aggregate bằng median và IQR/MAD.

---

## 5. window_policy

Các duration chính:

`T = {60, 180, 300} s`

Trong đó:

- `300 s`: reference window;
- `180 s`: intermediate duration;
- `60 s`: candidate wearable window.

Không mặc định 60 s là đủ.

Đánh giá độ ổn định theo:

- prediction error;
- surrogate decision;
- Lyapunov estimate;
- estimator variance;
- preservation of Awake–Drowsy effect.

Có thể thêm quasi-stationarity gate trước NTSA.

Thuật toán và threshold stationarity phải được freeze trước main experiment.

---

## 6. preprocessing_policy

Pipeline:

`Raw PPG`
`-> optical inversion`
`-> signal audit`
`-> zero-phase Butterworth bandpass`
`-> SQI / artifact rejection`
`-> Raw PPG + PPI`

### Optical inversion

`x'(t) = -x(t)`

Dùng để chuẩn hóa hướng waveform trước peak detection.

### Filtering

Sử dụng:

**zero-phase Butterworth bandpass**

Các thông số cần freeze trước main experiment:

- low cutoff;
- high cutoff;
- filter order;
- boundary handling.

Với `fs = 50 Hz`, Nyquist = `25 Hz`, nên không sử dụng hard-coded 50 Hz notch.

### SQI

SQI đóng vai trò quality gate, ưu tiên loại bad windows thay vì cố sửa tín hiệu.

Candidate checks:

- clipping;
- missing samples;
- abnormal amplitude;
- pulse morphology;
- peak detection confidence;
- PPI plausibility.

Mọi rejected window phải có rejection reason.

### PPI

Pipeline:

`PPG -> peak detection -> peak timestamps -> PPI sequence`

Giữ PPI theo beat index, không interpolate sang uniform time nếu không cần thiết.

---

## 7. surrogate_nulls

### Raw PPG

Surrogate:

`PPS`

Null hypothesis:

Raw PPG có thể được giải thích bởi noisy pseudoperiodicity mà không cần additional deterministic nonlinear structure.

### PPI

Surrogate:

`IAAFT`

Null hypothesis:

PPI có thể được giải thích bởi linear correlated stochastic dynamics với gần cùng amplitude distribution và power spectrum.

Không dùng PPS cho PPI.

---

## 8. primary_secondary_outcomes

### Primary

#### CV-NRMSE

Primary nonlinear prediction metric:

`CV-NRMSE`

Lower NRMSE = better predictability.

Temporal validation phải dùng blocked/contiguous split, không random K-fold.

#### Surrogate contrast

`ΔE = median(E_surrogate) - E_original`

Nếu:

`ΔE > 0`

thì original signal predictable hơn surrogate ensemble.

#### Surrogate hypothesis test

Lưu:

- surrogate rank;
- one-sided p-value;
- reject / not reject.

### Secondary

- maximum Lyapunov exponent `λmax`;
- prediction correlation;
- embedding delay `τ`;
- embedding dimension `m`;
- FNN behavior.

Không dùng `λmax > 0` riêng lẻ để claim chaos.

---

## 9. statistics_plan

Hierarchy:

`window -> session × state -> dataset-level inference`

Không dùng số lượng windows làm sample size.

Nếu cùng session có Awake và Drowsy:

`ΔY_i = Y_i,Drowsy - Y_i,Awake`

Các outcome chính:

- CV-NRMSE;
- ΔE;
- λmax.

Population reporting ưu tiên:

- session-level points;
- paired lines nếu phù hợp;
- effect size;
- confidence interval;
- p-value.

Statistical test cụ thể phải freeze trước final primary analysis.

Nếu có nhiều tests giữa state × representation × duration, cần multiplicity correction hoặc hierarchical testing strategy.

Do mất subject mapping, không thể model participant-level random effects. Đây phải được xem là limitation của study.

---

## 10. critical_gates

### Gate A — Labels
Không thay đổi Awake/Drowsy labels theo NTSA results.

### Gate B — Signal quality
Chỉ window vượt QC mới được đưa vào NTSA.

### Gate C — Stationarity
Nếu dùng stationarity gate, threshold phải freeze trước main experiment.

### Gate D — Synthetic validation
Core NTSA phải được kiểm tra trước trên:

- periodic;
- noisy pseudoperiodic;
- chaotic;
- stochastic / colored-noise signals.

### Gate E — Window validity
Không assume 60 s đủ; phải so với 300 s reference.

### Gate F — Surrogate
- Raw PPG -> PPS
- PPI -> IAAFT

### Gate G — No pseudoreplication
Window count không phải population sample size.

### Gate H — No single-metric chaos claim
Evidence phải dựa trên convergence của:

- valid embedding;
- nonlinear prediction;
- surrogate testing;
- Lyapunov;
- robustness analysis.

### Gate I — Raw PPG vs PPI
So sánh state effect trong từng representation, không so absolute metric một cách máy móc.

### Gate J — External validation
Chỉ dataset có PPG + drowsiness mới gọi là drowsiness replication.

---

## 11. reproducibility_rules

Phải ghi lại toàn bộ:

- random seeds;
- software/library versions;
- configuration files;
- exclusion logs;
- parameter search ranges;
- selected parameters;
- experiment outputs;
- code commit/version.

Không hard-code experiment parameters trong notebooks.

Các config tối thiểu gồm:

- sampling rate;
- filter parameters;
- SQI thresholds;
- stationarity thresholds;
- window durations;
- MI settings;
- FNN settings;
- Theiler window;
- predictor settings;
- Lyapunov settings;
- surrogate method/count;
- statistical thresholds.

Mỗi experiment run nên lưu:

- run ID;
- dataset version;
- config;
- seed;
- code commit;
- included/excluded windows;
- selected embedding parameters;
- NRMSE;
- surrogate statistics;
- Lyapunov estimates;
- final statistical summaries.

Core scientific algorithms phải nằm trong reusable source modules, không chỉ trong notebook.

---

## Still to Freeze Before Main Experiment

Các mục sau cần chốt ở Protocol v1.1:

- Butterworth cutoff + order;
- SQI algorithm + thresholds;
- quasi-stationarity method;
- window overlap;
- peak detector + PPI artifact rules;
- MI estimator + delay-selection rule;
- FNN thresholds;
- maximum embedding dimension;
- Theiler window;
- nonlinear predictor;
- prediction horizons;
- Lyapunov estimator;
- number of PPS/IAAFT surrogates;
- exact statistical tests;
- multiple-comparison strategy.