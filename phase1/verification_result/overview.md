````markdown
# Verification Plan — PPG Dynamics Across Awake–Drowsy

## Mục tiêu chung

Verification phase nhằm kiểm tra xem các finding chính của nghiên cứu:

- CC ↓
- NRMSE ↑
- DET ↓
- LLE ↓

có còn giữ được khi thay đổi các giả định hợp lý của pipeline hay không.

Ba nguồn bất định chính cần kiểm tra:

1. Label uncertainty
2. NTSA parameter dependence
3. Statistical dependence giữa các session cùng subject

Thứ tự ưu tiên được sắp xếp theo mức độ liên quan trực tiếp tới concern hiện tại của nghiên cứu:

```text
Label uncertainty
        ↓
NTSA parameter robustness
        ↓
Method-specific robustness
        ↓
Window-length robustness
        ↓
Subject-level strict sensitivity
````

Nguyên tắc chung:

> Verification không nhằm làm cho tất cả kết quả trở nên statistically significant, mà nhằm kiểm tra xem kết luận khoa học có ổn định dưới các giả định hợp lý khác nhau hay không.

---

# 1. Verification A — Label Uncertainty

## 1.1. Mục tiêu

Kiểm tra xem các khác biệt Awake–Drowsy có phụ thuộc quá mạnh vào bộ label hiện tại hay không.

Dataset hiện tại chỉ có:

* PPG
* Awake/Drowsy label
* không có raw camera data để tái đánh giá độc lập

Do đó không thể trực tiếp xác nhận camera-based validation.

Mục tiêu phù hợp hơn là:

> Kiểm tra tính ổn định của các finding khi áp dụng các cách chọn label bảo thủ hơn.

---

## 1.2. Audit cấu trúc label

Trước sensitivity analysis, cần kiểm tra:

* label là binary Awake/Drowsy hay có raw KSS
* label được cập nhật theo đơn vị thời gian nào
* số lần Awake ↔ Drowsy transition trong từng session
* thời lượng từng contiguous state segment
* có segment rất ngắn hoặc label oscillation bất thường hay không
* vị trí chính xác của các state transition

### Output

Tạo bảng:

| subject | session | state | start | end | duration |
| ------- | ------- | ----- | ----- | --- | -------- |

và summary:

| session | n_awake_segments | n_drowsy_segments | n_transitions | median_state_duration |
| ------- | ---------------: | ----------------: | ------------: | --------------------: |

---

## 1.3. Transition-boundary exclusion

### Giả thuyết

Các window nằm sát ranh giới Awake–Drowsy có khả năng chứa trạng thái sinh lý pha trộn hoặc label uncertainty cao hơn.

### Thiết kế

Primary:

> sử dụng toàn bộ valid windows như hiện tại.

Sensitivity 1:

> loại window nằm trong ±30 s quanh state transition.

Sensitivity 2:

> loại window nằm trong ±60 s quanh state transition.

Có thể thêm ±90 s nếu số lượng dữ liệu vẫn đủ, nhưng không bắt buộc.

### Pipeline

```text
Original labels
→ identify transition points
→ remove boundary windows
→ recompute session × state medians
→ paired Awake–Drowsy comparison
```

### Metrics

Chỉ rerun 4 headline metrics:

* CC
* NRMSE
* DET
* LLE

### Output

| Metric | Primary Δ | ±30 s | ±60 s | Direction preserved |
| ------ | --------: | ----: | ----: | ------------------- |
| CC     |           |       |       |                     |
| NRMSE  |           |       |       |                     |
| DET    |           |       |       |                     |
| LLE    |           |       |       |                     |

---

## 1.4. Minimum state-segment duration

### Giả thuyết

Các state segment rất ngắn có thể phản ánh transition fragment hoặc label kém ổn định hơn.

### Thiết kế

Primary:

> tất cả valid segments.

Sensitivity:

* chỉ giữ segment ≥ 3 phút
* chỉ giữ segment ≥ 5 phút

Chỉ sử dụng threshold nếu vẫn còn đủ paired Awake–Drowsy session.

### Mục tiêu

Kiểm tra xem các finding có giữ khi chỉ dùng những state segment kéo dài và ổn định hơn hay không.

---

## 1.5. Tiêu chí đánh giá label robustness

Không sử dụng p-value như tiêu chí duy nhất.

Ưu tiên:

1. direction preservation
2. effect magnitude
3. session consistency
4. CI location
5. statistical significance

### Strong support

```text
CC ↓
NRMSE ↑
DET ↓
LLE ↓
```

giữ nguyên dưới primary và conservative label subsets.

### Concern

* effect đảo direction
* effect chỉ tồn tại khi giữ boundary windows
* effect collapse gần zero sau conservative filtering

---

## 1.6. Claim nếu verification pass

> Các khác biệt Awake–Drowsy chính vẫn giữ cùng hướng khi loại các window gần ranh giới trạng thái và khi chỉ giữ các đoạn trạng thái kéo dài hơn.

Không claim:

> Label là ground truth khách quan.

---

# 2. Verification B — NTSA Parameter Dependence

## 2.1. Mục tiêu

Kiểm tra xem các finding có chỉ xuất hiện tại một bộ tham số NTSA cụ thể hay không.

Primary configuration hiện tại:

$$
\tau = 0.16s,\quad m = 8
$$

Mục tiêu không phải chứng minh đây là optimum duy nhất.

Mục tiêu là:

> Chứng minh conclusion ổn định trên một vùng parameter hợp lý được hỗ trợ bởi AMI và FNN.

---

# 2.2. Embedding parameter robustness

## Nominal setting

$$
\tau = 0.16s
$$

$$
m = 8
$$

## Sensitivity grid

$$
\tau \in \{0.12,\ 0.16,\ 0.20\}\ s
$$

$$
m \in \{6,\ 8,\ 10\}
$$

Tổng:

$$
3 \times 3 = 9
$$

configurations.

Delay phải được quy đổi từ seconds sang samples theo từng sampling frequency:

$$
\tau_{samples}
=
round(\tau_{seconds}\times f_s)
$$

---

## 2.3. Metrics rerun

Chỉ rerun primary supported metrics:

* CC
* NRMSE
* DET
* LLE

Pipeline giữ nguyên:

```text
Window
→ metric
→ median per session × state
→ paired Drowsy − Awake
→ statistical summary
```

---

## 2.4. Output

Với mỗi \((\tau,m)\), tính:

* median paired Δ
* bootstrap 95% CI
* rank-biserial effect size
* direction count
* p/q nếu cần

### Visualization

Một heatmap cho mỗi metric:

```text
x-axis = τ
y-axis = m
cell value = median paired Δ
```

Màu thể hiện:

* direction
* magnitude

Không dùng màu chủ yếu để thể hiện p-value.

---

## 2.5. Tiêu chí đánh giá embedding robustness

### Strong robustness

* 9/9 configurations giữ cùng direction

### Moderate robustness

* 7–8/9 giữ direction
* các setting còn lại gần zero nhưng không đảo mạnh

### Concern

* nhiều setting đảo direction
* finding chỉ tồn tại ở đúng \(\tau=0.16, m=8\)

---

# 3. Verification C — Method-Specific Robustness

Sau khi embedding robustness ổn định, kiểm tra các parameter riêng của từng phương pháp.

---

# 3.1. RQA robustness

## Parameters cần audit

* distance norm
* recurrence threshold strategy
* fixed recurrence rate hay fixed epsilon
* Theiler window
* \(l_{min}\)
* \(v_{min}\)

Trước hết freeze nominal RQA configuration.

---

## 3.1.1. Recurrence threshold sensitivity

Nếu dùng fixed recurrence rate:

ví dụ:

$$
RR \in \{2.5\%,\ 5\%,\ 7.5\%\}
$$

hoặc một range phù hợp quanh nominal setting.

Rerun:

Primary:

* DET

Secondary:

* Lmean
* LAM
* TT

Mục tiêu:

> DET ↓ không phụ thuộc vào đúng một recurrence threshold.

---

## 3.1.2. Theiler window sensitivity

Nominal:

$$
w
$$

Sensitivity:

$$
w_{low},\quad w,\quad w_{high}
$$

Giá trị phải có methodological rationale.

Mục tiêu:

> RQA result không bị tạo chủ yếu bởi temporal autocorrelation gần line of identity.

---

## 3.1.3. Minimum line-length sensitivity

Kiểm tra:

$$
l_{min}
$$

và nếu cần:

$$
v_{min}
$$

Theo one-factor-at-a-time.

Không cần full Cartesian grid.

---

# 3.2. LLE robustness

## Parameters cần audit

* embedding setting
* neighbor search
* Theiler window nếu có
* candidate fit region
* minimum fit length
* adaptive fit rule
* \(R^2\) QC threshold

---

## 3.2.1. QC sensitivity

Primary:

$$
R^2 \ge 0.90
$$

Sensitivity:

$$
R^2 \ge 0.95
$$

So sánh:

* median Δ
* CI
* effect size
* direction count

---

## 3.2.2. Fit-range sensitivity

Primary:

> adaptive linear region selected by highest \(R^2\)

Sensitivity:

* stricter minimum fit length
* loại early transient
* loại late saturation
* hoặc dùng predefined plausible fit range

Mục tiêu:

> LLE ↓ không phải artifact của adaptive fit selection.

---

# 3.3. Prediction robustness

Kiểm tra xem:

$$
CC\downarrow,\quad NRMSE\uparrow
$$

có giữ trên prediction horizons hay không.

Nếu final metric là mean across horizons, cần ghi rõ range horizon được sử dụng.

Mục tiêu:

> effect không chỉ xuất hiện ở một prediction horizon duy nhất.

---

# 4. Verification D — Window-Length Robustness

Phần này đã có nhưng được đưa vào verification framework chung.

Window lengths:

* 30 s
* 60 s
* 120 s
* 180 s

Role:

```text
30 s   → short-window stress test
60 s   → primary
120 s  → robustness
180 s  → robustness
```

Primary metrics:

* CC
* NRMSE
* DET
* LLE

Mục tiêu:

> conclusion không phụ thuộc nghiêm trọng vào một segmentation length duy nhất.

Không yêu cầu absolute metric values giống nhau.

Quan trọng hơn là:

* direction
* effect magnitude
* uncertainty

---

# 5. Verification E — Strict Subject-Level Sensitivity

## 5.1. Vai trò

Đây là verification strict nhất và được thực hiện sau cùng.

Primary study design vẫn sử dụng:

> 20 session-level Awake–Drowsy contrasts.

Strict sensitivity hỏi thêm:

> Nếu accounting for việc 20 sessions đến từ 10 subjects, conclusion có còn giữ hay không?

Mục tiêu không phải thay thế session-level primary analysis.

---

## 5.2. Subject-level aggregation

Với subject \(i\):

$$
\Delta_i^{subject}
=
median(
\Delta_{i,session1},
\Delta_{i,session2}
)
$$

Sau aggregation:

$$
n=10
$$

subjects.

Rerun:

* CC
* NRMSE
* DET
* LLE

Báo:

* median subject-level Δ
* bootstrap CI
* direction count
* Wilcoxon signed-rank nếu phù hợp

### Lưu ý

Do N giảm từ 20 xuống 10:

> significance có thể giảm dù scientific direction vẫn ổn định.

Do đó ưu tiên:

1. direction
2. magnitude
3. subject consistency
4. CI
5. p-value

---

## 5.3. Cluster bootstrap

Bootstrap ở subject level.

Mỗi replicate:

```text
sample 10 subjects with replacement
→ retain all sessions of selected subject
→ recompute group effect
```

Lặp:

$$
B = 10,000 - 20,000
$$

Mục tiêu:

> giữ within-subject dependency structure.

---

## 5.4. Optional mixed-effects sensitivity

Nếu cần thêm rigor:

$$
Y =
\beta_0
+
\beta_1 State
+
u_{subject}
+
\epsilon
$$

Optional:

$$
Y =
\beta_0
+
\beta_1 State
+
\beta_2 Meal
+
u_{subject}
+
\epsilon
$$

Không làm model quá phức tạp do chỉ có 10 subjects.

Mixed model chỉ là sensitivity, không bắt buộc trở thành primary analysis.

---

# 6. Verification Master Matrix

Sau khi hoàn thành, tạo bảng tổng hợp:

| Finding | Label robustness | Embedding robustness | Method-specific robustness | Window robustness | Subject-level strict sensitivity |
| ------- | ---------------- | -------------------- | -------------------------- | ----------------- | -------------------------------- |
| CC ↓    |                  |                      |                            |                   |                                  |
| NRMSE ↑ |                  |                      |                            |                   |                                  |
| DET ↓   |                  |                      |                            |                   |                                  |
| LLE ↓   |                  |                      |                            |                   |                                  |

Quy ước:

* ✓ robust
* ~ partial
* ✕ inconsistent

Không quyết định chỉ dựa trên significance.

---

# 7. Decision Rules

## GREEN — Freeze finding

Finding có thể được giữ làm core result nếu:

* direction ổn định dưới label sensitivity
* direction ổn định trên parameter region hợp lý
* method-specific sensitivity không đảo conclusion
* window-size robustness giữ direction
* strict subject-level sensitivity không cho kết quả đối nghịch

---

## YELLOW — Giữ nhưng hạ claim

Nếu:

* direction giữ nhưng effect magnitude giảm
* CI rộng hơn
* significance mất ở stricter analysis
* một số parameter setting gần zero

Khi đó dùng wording:

> directionally consistent but sensitive to analysis conditions

---

## RED — Reconsider finding

Nếu:

* conservative label analysis đảo direction
* parameter changes làm direction đảo nhiều lần
* effect chỉ tồn tại ở nominal setting
* strict subject-level analysis cho conclusion đối nghịch
* result bị chi phối bởi rất ít session/subject

Khi đó cần sửa hoặc loại finding khỏi core conclusion.

---

# 8. Recommended Execution Order

## Phase 1 — Label Verification

1. audit label structure
2. transition-boundary exclusion
3. minimum segment duration
4. rerun CC / NRMSE / DET / LLE

---

## Phase 2 — Embedding Robustness

1. define \(\tau\) grid
2. define \(m\) grid
3. rerun 4 headline metrics
4. build robustness heatmaps

---

## Phase 3 — Method-Specific Robustness

RQA:

* recurrence setting
* Theiler window
* line-length parameters

LLE:

* R² threshold
* fit-range rule

Prediction:

* horizon consistency

---

## Phase 4 — Window Robustness

Consolidate existing:

* 30 s
* 60 s
* 120 s
* 180 s

---

## Phase 5 — Strict Subject-Level Sensitivity

1. subject-level aggregation
2. cluster bootstrap
3. optional mixed-effects model
4. compare with session-level primary result

---

# 9. Final Verification Question

Sau cùng, mỗi finding phải trả lời được:

> Nếu thay đổi một giả định hợp lý của analysis, scientific conclusion có còn giữ không?

Mục tiêu cuối cùng không phải:

$$
p < 0.05
$$

ở mọi analysis.

Mục tiêu là:

$$
\boxed{
\text{Stable direction}
+
\text{Comparable effect}
+
\text{Cross-analysis consistency}
}
$$

Nguyên tắc chốt:

> Robustness of the scientific conclusion is more important than robustness of a single p-value.

```
```
