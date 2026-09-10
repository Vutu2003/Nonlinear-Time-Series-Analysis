# Verification Plan — PPG Dynamics Across Awake–Drowsy

## Mục tiêu chung

Mục tiêu của verification phase không phải tìm thêm metric mới hay cố làm cho nhiều kết quả đạt significance hơn.

Mục tiêu là kiểm tra xem các finding chính:

- CC ↓
- NRMSE ↑
- DET ↓
- LLE ↓

có còn giữ được khi thay đổi những giả định quan trọng nhất của pipeline hay không.

Ba nguồn bất định cần kiểm tra:

1. Label uncertainty
2. Statistical dependence giữa các session cùng subject
3. NTSA parameter dependence

Nguyên tắc chung:

> Một finding được xem là robust nếu hướng thay đổi, độ lớn hiệu ứng và tính nhất quán vẫn được duy trì dưới các thiết lập hợp lý khác nhau, ngay cả khi p-value hoặc CI thay đổi.

Không sử dụng significance như tiêu chí duy nhất để quyết định robustness.

---

# 1. Verification A — Label Reliability / Label Robustness

## 1.1. Câu hỏi khoa học

Các khác biệt Awake–Drowsy có phụ thuộc quá mạnh vào bộ label hiện có hay không?

Dataset hiện tại chỉ cung cấp:

- PPG
- label Awake/Drowsy
- có thể có KSS/raw score tùy file

Không có raw camera recordings để tái đánh giá label độc lập.

Do đó không thể claim:

> Camera independently validated the labels.

Thay vào đó, mục tiêu là:

> Kiểm tra tính ổn định của các finding khi áp dụng các quy tắc label bảo thủ hơn.

---

## 1.2. Audit lại label structure

Trước khi chạy sensitivity analysis, cần tạo một bảng mô tả đầy đủ label structure.

### Cần xác định

- label hiện tại là binary Awake/Drowsy hay có raw KSS?
- KSS được ghi trực tiếp trong CSV hay chỉ label đã quy đổi?
- label đổi theo sample, beat, epoch hay đoạn thời gian?
- thời lượng trung bình của mỗi contiguous state segment
- số lần chuyển state trong mỗi session
- có isolated segment rất ngắn không?
- có A → D → A hoặc D → A → D trong thời gian rất ngắn không?

### Output

Tạo một bảng:

| subject | session | state | segment_start | segment_end | duration | n_windows |
|---|---|---|---|---|---|---|

Và một bảng summary:

| session | n_awake_segments | n_drowsy_segments | median_awake_duration | median_drowsy_duration | n_transitions |
|---|---:|---:|---:|---:|---:|

Mục tiêu:

> hiểu cấu trúc label trước khi thiết kế sensitivity rule.

---

## 1.3. Trường hợp có raw KSS score

Nếu raw KSS có sẵn, giữ một labeling scheme làm primary và tạo một hoặc nhiều stricter schemes.

Ví dụ:

### Primary scheme

Giữ đúng rule hiện tại của dataset.

### Strict scheme

- Awake: chỉ giữ KSS thấp rõ ràng
- Drowsy: chỉ giữ KSS cao rõ ràng
- loại vùng KSS trung gian

Không lựa chọn threshold dựa trên NTSA result.

Threshold phải được xác định từ:

- protocol dataset
- literature KSS
- hoặc rule đã định trước

### Rerun

Chỉ rerun bốn headline metrics:

- CC
- NRMSE
- DET
- LLE

### So sánh

Với mỗi metric:

| metric | primary Δ | strict Δ | direction preserved | 95% CI | q |
|---|---:|---:|---|---|---|

Primary quantity:

$$
\Delta = \mathrm{Drowsy} - \mathrm{Awake}
$$

### Tiêu chí robustness

Ưu tiên theo thứ tự:

1. giữ cùng direction
2. magnitude không collapse
3. session/subject consistency còn tương tự
4. CI vẫn centered cùng phía
5. significance chỉ là secondary

---

## 1.4. Trường hợp chỉ có binary label

Nếu không có raw KSS, không được tạo artificial KSS thresholds.

Thay vào đó dùng các sensitivity analyses sau.

---

## 1.4.1. Transition-boundary exclusion

### Ý tưởng

Window nằm sát ranh giới Awake ↔ Drowsy có khả năng chứa mixed physiological state hoặc label uncertainty cao hơn.

### Thiết kế

Primary:

> dùng toàn bộ valid labeled windows.

Sensitivity A:

> loại các window nằm trong ±30 s quanh state transition.

Sensitivity B:

> loại các window nằm trong ±60 s quanh state transition.

Có thể thêm ±90 s nếu data density vẫn đủ, nhưng không cần quá nhiều mức.

### Implementation

Một window bị loại nếu:

$$
\operatorname{distance}(\text{window},\text{transition}) < T
$$

với:

$$
T \in \{30\,\mathrm{s}, 60\,\mathrm{s}\}
$$

### Rerun

Rerun:

- CC
- NRMSE
- DET
- LLE

Sau đó aggregate lại đúng pipeline primary:

window → median per session × state → paired Awake–Drowsy comparison.

### Kết quả cần báo

| metric | primary | ±30 s excluded | ±60 s excluded | direction stable |
|---|---:|---:|---:|---|

### Diễn giải nếu pass

> Finding không phụ thuộc chủ yếu vào những window gần ranh giới trạng thái.

---

## 1.4.2. Minimum state-segment duration

### Ý tưởng

Các state segment quá ngắn có thể là label không ổn định hoặc transition fragment.

### Thiết kế

Primary:

> tất cả valid segments.

Sensitivity:

- chỉ giữ state segment ≥ 3 min
- chỉ giữ state segment ≥ 5 min

Chỉ dùng thresholds nếu vẫn còn đủ paired sessions.

### Mục tiêu

Kiểm tra xem finding có giữ trong các đoạn Awake/Drowsy kéo dài và ổn định hơn không.

### Output

| metric | primary | segment ≥3 min | segment ≥5 min |
|---|---:|---:|---:|

Không bắt buộc mọi analysis phải significance.

---

## 1.4.3. Window-purity check

Nếu segmentation cho phép xác định tỷ lệ label trong từng window, yêu cầu:

$$
\mathrm{purity} = \frac{\text{samples in dominant state}}{\text{samples in window}}
$$

Primary:

- current rule

Sensitivity:

- \mathrm{purity} = 100%
- hoặc ≥95%

Nếu window đã được tạo riêng trong từng contiguous state segment thì mục này có thể không cần.

---

## 1.5. Label robustness figure

Tạo một figure đơn giản cho 4 headline metrics.

Có thể dùng forest plot:

- y-axis: CC, NRMSE, DET, LLE
- x-axis: paired median effect
- series:
  - Primary
  - Boundary-excluded
  - Long-segment subset

Mục tiêu figure:

> cho thấy direction preservation, không phải significance hunting.

---

## 1.6. Label robustness conclusion

Một finding được xem là label-robust nếu:

- direction không đảo dưới các conservative subsets
- effect size vẫn cùng order of magnitude
- kết quả không biến mất chỉ khi loại boundary windows

Claim an toàn:

> The principal Awake–Drowsy effects remained directionally stable under conservative label-related sensitivity analyses.

Không claim:

> Labels were externally validated.

---

# 2. Verification B — Subject-Level Dependence

## 2.1. Câu hỏi khoa học

20 sessions đến từ 10 subjects.

Do đó cần kiểm tra:

> Kết luận có còn giữ khi inference tôn trọng repeated measurements trong cùng subject hay không?

Cấu trúc:

$$
10\,\text{subjects} \times 2\,\text{sessions} \approx 20\,\text{sessions}
$$

Hai session cùng subject không được mặc nhiên coi là independent participants.

---

## 2.2. Primary session-level analysis

Giữ analysis hiện tại làm primary descriptive/inferential framework:

Trong mỗi session:

$$
\Delta_{ij} = \mathrm{Drowsy}_{ij} - \mathrm{Awake}_{ij}
$$

Sau đó báo:

- median Δ
- bootstrap 95% CI
- Wilcoxon signed-rank
- rank-biserial effect size
- direction count
- BH-FDR

Không xóa analysis này.

---

## 2.3. Subject-level aggregation

### Mục tiêu

Biến mỗi subject thành một đơn vị độc lập.

Với subject $i$:

$$
\Delta_i^{\mathrm{subject}}
=
\operatorname{median}\left(\Delta_{i,1}, \Delta_{i,2}\right)
$$

Nếu chỉ có một valid session ở subject nào đó thì cần ghi rõ và xác định rule trước.

### Output

N = 10 subjects.

Cho mỗi metric báo:

- median subject-level Δ
- bootstrap CI
- Wilcoxon signed-rank
- direction count

### Quan trọng

Không kỳ vọng power giống N=20.

Với N=10, p-value có thể lớn hơn dù direction rất ổn định.

Do đó đánh giá theo:

1. direction
2. magnitude
3. subject consistency
4. CI
5. p-value

### Bảng

| metric | session-level Δ | subject-level Δ | subject direction count | direction preserved |
|---|---:|---:|---:|---|

---

## 2.4. Cluster bootstrap

### Mục tiêu

Giữ toàn bộ session nhưng bootstrap ở level subject.

### Procedure

Mỗi bootstrap replicate:

1. sample 10 subjects with replacement
2. khi một subject được chọn, lấy toàn bộ session của subject đó
3. tính paired effect theo pipeline
4. lưu group-level statistic

Lặp:

$$
B \in \{10{,}000,\ 20{,}000\}
$$

### Output

Cluster-aware bootstrap CI cho:

- CC
- NRMSE
- DET
- LLE

### Ý nghĩa

Điều này giữ correlation structure giữa các session của cùng subject.

---

## 2.5. Mixed-effects model

### Mục tiêu

Kiểm tra state effect khi accounting for subject-specific baseline.

Model cơ bản:

$$
Y = \beta_0 + \beta_1\,\mathrm{State} + u_{\mathrm{subject}} + \epsilon
$$

Trong đó:

$$
u_{\mathrm{subject}} \sim \mathcal{N}(0,\sigma^2_u)
$$

State:

- Awake
- Drowsy

### Optional: meal/session type

Nếu metadata rõ:

$$
Y =
\beta_0
+
\beta_1\,\mathrm{State}
+
\beta_2\,\mathrm{Meal}
+
u_{\mathrm{subject}}
+
\epsilon
$$

với Meal:

- lunch
- dinner

Có thể thêm:

$$
\mathrm{State} \times \mathrm{Meal}
$$

chỉ khi thật sự cần.

Với N=10 subjects, tránh model quá phức tạp.

### Output

Cho mỗi metric:

- β_State
- CI
- p-value
- direction

### Mục tiêu

Không cần mixed model trở thành primary.

Dùng như sensitivity analysis.

---

## 2.6. Lunch vs Dinner consistency

### Câu hỏi

Finding có chỉ xuất hiện ở một loại session hay không?

Tách:

$$
\Delta_{\mathrm{lunch}}
$$

và:

$$
\Delta_{\mathrm{dinner}}
$$

Cho 4 headline metrics.

### Báo

- median effect
- direction
- subject consistency

### Không cần

Không nhất thiết hypothesis-test mạnh vì sample nhỏ.

### Interpretation

Nếu cùng direction:

> effect không bị giới hạn ở một thời điểm ghi duy nhất.

Nếu khác:

> đây là source of physiological/session variability cần Discussion.

---

## 2.7. Subject-level robustness criteria

Một finding được xem là robust nếu:

- session-level và subject-level cùng direction
- cluster bootstrap không cho thấy effect đảo chiều rõ
- mixed model β_State cùng direction
- lunch/dinner không cho pattern hoàn toàn đối nghịch

Không yêu cầu tất cả p < 0.05.

---

# 3. Verification C — NTSA Parameter Robustness

## 3.1. Câu hỏi khoa học

Kết quả có chỉ xuất hiện tại:

$$
\tau = 0.16\,\mathrm{s},\quad m=8
$$

hay giữ trên một vùng parameter hợp lý?

Mục tiêu không phải chứng minh $\tau=0.16$ và $m=8$ là optimum tuyệt đối.

Mục tiêu:

> chứng minh finding không phụ thuộc vào một parameter choice duy nhất.

---

## 3.2. Freeze nominal configuration

Nominal:

$$
\tau = 0.16\,\mathrm{s}
$$

$$
m = 8
$$

Giữ đây là primary setting.

Lý do:

- AMI supports delay region quanh 0.16 s
- FNN đã plateau ở vùng m cao
- m=8 là common conservative embedding dimension

---

## 3.3. Embedding parameter grid

### Recommended grid

$$
\tau \in \{0.12,\ 0.16,\ 0.20\}\,\mathrm{s}
$$

$$
m \in \{6,\ 8,\ 10\}
$$

Tổng:

$$
3\times3=9
$$

configurations.

Nếu compute cost lớn, có thể dùng:

$$
m \in \{7,8,9\}
$$

nhưng 6/8/10 cho robustness range rộng hơn.

### Important

Convert delay từ seconds sang samples theo từng session:

$$
\tau_{\mathrm{samples}}
=
\operatorname{round}\left(\tau_{\mathrm{seconds}} \times f_s\right)
$$

Không dùng cùng sample delay cho 25 Hz và 50 Hz.

---

## 3.4. Metrics rerun

Trước tiên chỉ rerun primary supported metrics:

- CC
- NRMSE
- DET
- LLE

Không cần rerun toàn bộ secondary metrics ngay.

---

## 3.5. Embedding robustness outputs

Với mỗi $(\tau,m)$:

1. compute all window metrics
2. median per session × state
3. paired Awake–Drowsy Δ
4. compute:
   - median Δ
   - CI
   - r_rb
   - direction count
   - p/q nếu cần

### Figure

Một heatmap cho mỗi metric:

- x-axis = τ
- y-axis = m
- cell value = median paired Δ

Optional:

- cell border nếu CI excludes zero
- symbol nếu BH-FDR supported

Nhưng màu chính phải biểu diễn effect direction/magnitude, không phải p-value.

### Robustness target

Ví dụ:

CC:

$$
\Delta < 0
$$

NRMSE:

$$
\Delta > 0
$$

DET:

$$
\Delta < 0
$$

LLE:

$$
\Delta < 0
$$

trên phần lớn hoặc toàn bộ grid.

---

## 3.6. Embedding robustness criteria

Không dùng:

> 9/9 phải p<0.05

Thay vào đó:

Strong robustness:

- 9/9 same direction

Moderate robustness:

- 7–8/9 same direction
- remaining cells weak/near zero nhưng không đảo mạnh

Concern:

- nhiều parameter combinations đảo direction
- effect chỉ tồn tại ở nominal point

---

# 4. Verification D — RQA-Specific Robustness

## 4.1. Câu hỏi

DET↓ có phụ thuộc vào một recurrence definition cụ thể hay không?

RQA phụ thuộc nhiều hơn chỉ $\tau,m$.

Cần audit:

- norm
- threshold strategy
- recurrence rate
- Theiler window
- l_min
- v_min

---

## 4.2. Freeze nominal RQA configuration

Ghi đầy đủ:

- embedding dimension
- delay
- distance norm
- fixed epsilon hay fixed recurrence rate
- Theiler window
- l_min
- v_min

Đây phải là một reproducibility table.

---

## 4.3. Recurrence threshold sensitivity

Nếu dùng fixed recurrence rate:

ví dụ:

$$
\mathrm{RR} \in \{2.5\%,5\%,7.5\%\}
$$

Hoặc dùng range hợp lý quanh nominal.

Nếu dùng fixed epsilon:

thử ± một mức hợp lý quanh nominal.

### Rerun

Primary:

- DET

Secondary:

- Lmean
- LAM
- TT

### Mục tiêu

DET↓ giữ direction qua recurrence settings.

---

## 4.4. Theiler window sensitivity

Nominal:

$$
w
$$

Sensitivity:

$$
w_{\mathrm{low}},\quad w,\quad w_{\mathrm{high}}
$$

Các giá trị phải có rationale theo autocorrelation / temporal neighborhood.

Không dùng arbitrary range quá rộng.

### Mục tiêu

DET↓ không phải artifact do temporal autocorrelation gần line of identity.

---

## 4.5. Minimum line-length sensitivity

Vary:

$$
l_{\min}
$$

và nếu cần:

$$
v_{\min}
$$

Theo one-factor-at-a-time.

Không cần full Cartesian product.

---

# 5. Verification E — LLE-Specific Robustness

## 5.1. Câu hỏi

LLE↓ có phụ thuộc vào adaptive fit rule hay QC criterion hay không?

---

## 5.2. Primary LLE setup

Ghi rõ:

- Rosenstein method
- embedding settings
- neighborhood definition
- Theiler window nếu có
- candidate fitting range
- minimum fit length
- linear-region selection rule
- R² threshold

---

## 5.3. QC sensitivity

Primary:

$$
R^2 \ge 0.90
$$

Sensitivity:

$$
R^2 \ge 0.95
$$

Bạn đã có analysis này.

Rerun:

- paired Δ
- CI
- r_rb
- direction count

---

## 5.4. Fit-range sensitivity

Test ít nhất một alternative rule.

Ví dụ:

### Primary

Adaptive region with highest R².

### Sensitivity

- stricter minimum fit length
- exclude very early divergence points
- exclude late saturation region
- hoặc use a predefined plausible fit interval

Mục tiêu:

> LLE↓ không phải sản phẩm của việc chọn fit interval tối ưu nhất cho từng window.

---

# 6. Verification F — Prediction-Specific Robustness

## 6.1. Câu hỏi

CC↓ / NRMSE↑ có phụ thuộc vào một prediction horizon cụ thể hay không?

---

## 6.2. Check horizon dependence

Với từng prediction horizon:

- compute Awake–Drowsy effect
- xem direction

Nếu final metric là mean across horizons, ghi rõ:

$$
\overline{\mathrm{CC}} = \operatorname{mean}\left(\mathrm{CC}(h_1),\ldots,\mathrm{CC}(h_k)\right)
$$

$$
\overline{\mathrm{NRMSE}} = \operatorname{mean}\left(\mathrm{NRMSE}(h_1),\ldots,\mathrm{NRMSE}(h_k)\right)
$$

### Mục tiêu

CC↓ và NRMSE↑ không chỉ xuất hiện tại một horizon đơn lẻ.

---

# 7. Verification G — Window-Length Robustness

Phần này đã có nhưng cần đưa vào verification framework chung.

Windows:

- 30 s
- 60 s
- 120 s
- 180 s

60 s = primary.

30/120/180 = sensitivity.

Primary metrics:

- CC
- NRMSE
- DET
- LLE

### Mục tiêu

Kiểm tra:

> conclusion có phụ thuộc vào đúng một segmentation length hay không?

### Interpretation

30 s:

- same direction
- higher variance

60 s:

- primary trade-off

120–180 s:

- robustness

Không yêu cầu identical absolute metric values.

---

# 8. Verification Master Table

Sau khi chạy xong, tạo một bảng tổng hợp:

| Finding | Label robustness | Subject-level | Embedding robustness | Method-specific robustness | Window robustness |
|---|---|---|---|---|---|
| CC ↓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| NRMSE ↑ | ✓ | ✓ | ✓ | ✓ | ✓ |
| DET ↓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| LLE ↓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Có thể dùng:

- ✓ robust
- ~ partial
- ✕ inconsistent

Không dùng p-value làm criterion duy nhất.

---

# 9. Verification Decision Rules

## Green — có thể freeze result

Nếu:

- strict/conservative labels giữ same direction
- subject-level analysis giữ same direction
- parameter grid giữ effect trên phần lớn vùng hợp lý
- RQA/LLE method sensitivity không đảo result
- window robustness giữ direction

→ freeze result và chuyển sang manuscript.

---

## Yellow — cần investigation

Nếu:

- effect magnitude giảm mạnh nhưng vẫn same direction
- significance biến mất do reduced N
- một vài parameter cells gần zero
- một session/subject ảnh hưởng đáng kể

→ investigate nhưng không nhất thiết bác bỏ finding.

---

## Red — cần xem lại conclusion

Nếu:

- strict label analysis đảo direction
- subject-level result trái ngược session-level
- parameter robustness cho nhiều direction reversal
- DET hoặc LLE chỉ tồn tại ở đúng nominal setting
- effect bị chi phối bởi 1–2 subject

→ không freeze claim hiện tại.

---

# 10. Thứ tự thực nghiệm đề xuất

## Phase 1 — Data / Label Verification

1. audit label structure
2. transition-boundary analysis
3. minimum segment duration
4. rerun 4 headline metrics

Output:
- label summary table
- robustness table

---

## Phase 2 — Statistical Independence

1. subject-level aggregation
2. cluster bootstrap
3. mixed-effects sensitivity
4. lunch vs dinner consistency

Output:
- session vs subject comparison
- cluster-aware CI
- mixed-model state effect

---

## Phase 3 — Embedding Robustness

1. τ grid
2. m grid
3. rerun CC / NRMSE / DET / LLE
4. build heatmaps

Output:
- 4 parameter robustness heatmaps
- summary direction table

---

## Phase 4 — Method-Specific Robustness

RQA:
- recurrence threshold/rate
- Theiler window
- line-length parameters

LLE:
- R² criterion
- fit-selection rule

Prediction:
- horizon consistency

---

## Phase 5 — Final Verification Summary

Create:

1. master robustness table
2. concise verification figure
3. final frozen result table
4. Methods wording
5. Limitation wording
6. claim boundary

---

# 11. Statistical Questions Phải Tự Trả Lời Được

Trước manuscript submission phải trả lời chắc chắn:

### Median

- Tại sao dùng median?
- Median của gì?
- Median session × state khác median paired Δ như thế nào?

### Bootstrap

- resampling unit là gì?
- bootstrap window, session hay subject?
- percentile CI nghĩa là gì?
- bootstrap có xử lý dependence không?

### Wilcoxon signed-rank

- dữ liệu paired ở đâu?
- test thực sự dùng signed ranks như thế nào?
- null hypothesis là gì?
- khác paired t-test ra sao?
- khác sign test ra sao?

### Rank-biserial effect size

- dấu biểu diễn gì?
- magnitude biểu diễn gì?
- liên hệ với Wilcoxon ra sao?

### BH-FDR

- family of hypotheses gồm những metric nào?
- raw p khác q-value thế nào?
- FDR khác Bonferroni/FWER thế nào?
- tại sao CI exclude zero nhưng q vẫn >0.05?

### Repeated measurements

- tại sao 20 sessions không đồng nghĩa 20 independent subjects?
- cluster bootstrap xử lý gì?
- mixed model xử lý gì?

### PPS rank test

- tại sao 39 surrogates?
- vì sao p_min = 0.05 trong two-sided test?
- original rank được tính như thế nào?
- reject PPS null thực sự cho phép claim gì?

---

# 12. Claim Boundaries Sau Verification

Nếu verification pass:

Có thể claim:

> In this cohort, the Awake–Drowsy transition was consistently associated with reduced forecastability, reduced diagonal recurrence organization, and reduced local trajectory divergence in short-window PPG dynamics.

Có thể claim:

> These findings were robust to multiple reasonable analysis choices.

Không claim:

> The labels represent objective ground truth.

Không claim:

> The findings generalize to all populations.

Không claim:

> Drowsiness causes a universal chaotic transition.

Không claim:

> PPS proves deterministic chaos.

---

# 13. Verification Philosophy

Verification không nhằm làm cho tất cả kết quả trở thành significant.

Mục tiêu quan trọng hơn là:

$$
\text{same scientific conclusion}
$$

dưới:

$$
\text{different reasonable assumptions}
$$

Nếu effect direction, magnitude và consistency được giữ, trong khi p-value dao động do sample size hoặc variance, finding vẫn có thể được xem là robust.

Nguyên tắc chốt:

> Robustness of the scientific conclusion is more important than robustness of a single p-value.