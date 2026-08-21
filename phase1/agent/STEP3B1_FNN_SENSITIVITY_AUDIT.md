````markdown
# FNN Decision-Threshold Sensitivity Analysis

## Mục tiêu

Đánh giá ảnh hưởng của **residual-FNN decision threshold** đến embedding dimension được chọn từ các đường cong FNN đã tính trên toàn bộ dataset.

Phần này **không chạy lại thuật toán FNN**.

Các tham số FNN đã được freeze:

- `tau`: cố định theo representation
  - Raw PPG: `tau = 0.20 s`
  - Processed PPG: `tau = 0.16 s`
- `R_tol = 15`
- `A_tol = 2`
- `max_m = 10`
- `theiler = 0`
- nearest neighbor: `r = 1`

Input chính:

```text
fnn_curves.csv
````

Các threshold cần đánh giá:

```text
1%, 2%, 3%, 4%, 5%
```

Với mỗi threshold `θ`, định nghĩa:

```text
selected_m(θ) = dimension đầu tiên sao cho FNN(m) <= θ
```

Nếu không có dimension nào trong `1...10` đạt threshold:

```text
selected_m = NaN
m_found = False
```

Mục tiêu cuối cùng không phải tìm một threshold "tối ưu tuyệt đối", mà xác định **trade-off hợp lý giữa residual FNN, coverage và embedding dimension**, sau đó đánh giá xem có tồn tại một vùng `m` ổn định đủ mạnh để freeze cho downstream NTSA hay không.

---

# Experiment 0 — Data Integrity and FNN Curve Validation

## Task

Đọc `fnn_curves.csv` và xác nhận dataset FNN hiện tại có thể dùng trực tiếp cho threshold analysis.

Kiểm tra:

1. Khóa cửa sổ:

```text
session
window_id
window_size_s
label
representation
```

2. Mỗi cửa sổ phải có dimension:

```text
1, 2, ..., 10
```

3. `fnn_percent`:

   * finite
   * `0 <= fnn_percent <= 100`

4. `valid_count`:

   * positive
   * theo dõi xu hướng giảm khi `m` tăng

5. Không duplicate:

```text
(session, window_id, window_size_s, label, representation, dimension)
```

6. Xác nhận các strata:

```text
window_size_s ∈ {60, 120, 180}
label ∈ {Awake, Drowsy}
representation ∈ {Raw, Processed}
```

7. Báo cáo số unique window × representation.

## Output

Console/table:

```text
n_curve_rows
n_unique_windows
n_sessions
counts by window_size_s
counts by label
counts by representation
missing dimensions
duplicate rows
invalid fnn_percent
invalid valid_count
```

## Đánh giá

PASS nếu:

* tất cả cửa sổ có đầy đủ `m=1...10`;
* không duplicate;
* không có FNN ngoài `[0,100]`;
* không có lỗi metadata nghiêm trọng.

## Nhận xét cần ghi

Nếu PASS:

> FNN curves were complete and internally consistent across all eligible window-representation observations, allowing decision-threshold sensitivity to be performed entirely as post-processing without recomputing nearest neighbors.

---

# Experiment 1 — Derive Threshold-Specific Window Results

## Task

Từ mỗi FNN curve, derive kết quả cho:

```text
threshold_pct = 1, 2, 3, 4, 5
```

Với mỗi:

```text
window × representation × threshold
```

tính:

```text
selected_m
m_found
min_fnn_percent
fnn_at_selected_m
valid_count_at_selected_m
```

Ngoài ra giữ toàn bộ metadata:

```text
session
window_id
window_size_s
label
representation
threshold_pct
```

## Output

Tạo:

```text
fnn_threshold_window_results.csv
```

Mỗi original window-representation sẽ tạo 5 dòng.

## Validation

Kiểm tra logic monotonic:

Nếu:

```text
θ1 < θ2
```

thì với cùng một window:

```text
selected_m(θ2) <= selected_m(θ1)
```

khi cả hai đều found.

Ngoài ra:

```text
m_found(θ)
```

không được chuyển từ `True` sang `False` khi threshold tăng.

## Nhận xét cần ghi

Threshold chỉ thay đổi **decision rule**, không thay đổi FNN curve:

> All threshold-specific embedding dimensions were derived from the same precomputed FNN curves; therefore, differences across thresholds reflect decision-rule sensitivity rather than changes in the underlying nearest-neighbor calculation.

---

# Experiment 2 — Global Threshold–Coverage Trade-off

## Task

Đối với từng threshold:

```text
1%, 2%, 3%, 4%, 5%
```

tính trên toàn bộ dataset:

```text
N
n_m_found
m_found_rate_pct
median_selected_m
IQR_selected_m
mode_selected_m
Q10
Q25
Q50
Q75
Q90
min_selected_m
max_selected_m
```

`selected_m` statistics chỉ tính trên các window `m_found=True`.

Nhưng luôn báo song song `m_found_rate`.

## Output

Table:

```text
threshold_pct
N
n_m_found
m_found_rate_pct
median_m
iqr_m
mode_m
q90_m
```

Figure 1:

```text
Threshold (%) vs m_found_rate (%)
```

Figure 2:

```text
Threshold (%) vs median selected_m
```

Có thể thêm IQR/error bars.

## Đánh giá

Tìm trade-off:

* threshold quá thấp:

  * `m_found_rate` thấp;
  * selected m có thể dồn lên vùng cao;
  * nhiều window không crossing.

* threshold quá cao:

  * coverage cao;
  * nhưng selected m có thể giảm mạnh;
  * criterion trở nên permissive.

Điểm quan tâm là vùng mà:

```text
coverage tăng đáng kể
nhưng median/mode m bắt đầu ổn định
```

## Nhận xét cần ghi

Không chọn threshold chỉ vì có coverage cao nhất.

Cần mô tả:

> Increasing the residual-FNN threshold monotonically increased the proportion of windows for which an embedding dimension could be identified, while generally reducing the selected dimension. The useful operating region was therefore assessed as a trade-off between embedding coverage and residual false-neighbor tolerance.

---

# Experiment 3 — Raw vs Processed Threshold Response

## Task

Lặp Experiment 2 riêng cho:

```text
Raw
Processed
```

Tính theo từng threshold:

```text
m_found_rate
median_m
IQR_m
mode_m
Q90_m
min_fnn_percent
```

## Output

Table:

```text
threshold | representation | N | found_rate | median_m | IQR | mode | Q90
```

Figure:

```text
Threshold → m_found_rate
```

hai curves:

```text
Raw
Processed
```

Figure:

```text
Threshold → median selected_m
```

Raw và Processed riêng.

## Đánh giá

Cần trả lời:

1. Raw có cần threshold cao hơn mới đạt coverage hợp lý không?
2. Processed có saturate coverage sớm hơn Raw không?
3. Median/mode của hai representation có tiến về cùng vùng `m` không?
4. Có threshold nào khiến Raw/Processed divergence mạnh không?

## Nhận xét cần ghi

Không suy diễn rằng Processed "có dynamics đơn giản hơn".

Chỉ nói:

> The two waveform representations differed in residual FNN behavior and threshold-crossing coverage.

Nếu cả hai hội tụ về vùng tương tự:

> Despite different crossing rates, Raw and Processed PPG supported a similar embedding-dimensional region over the central threshold range.

---

# Experiment 4 — Awake vs Drowsy Robustness

## Task

Trong mỗi:

```text
threshold × representation × window_size
```

so sánh:

```text
Awake
Drowsy
```

ở window level mô tả:

```text
m_found_rate
median_m
IQR_m
mode_m
```

Sau đó aggregate ở session level.

Không dùng pooled windows để inference chính.

## Output

Descriptive table:

```text
threshold
window_size_s
representation
label
N
m_found_rate
median_m
IQR_m
mode_m
```

## Session-level aggregation

Với mỗi:

```text
session × threshold × size × state × representation
```

tính:

```text
n_windows
n_m_found
m_found_rate_pct
median_m
iqr_m
mode_m
```

Tạo:

```text
fnn_threshold_session_summary.csv
```

## Paired comparison

Trong mỗi:

```text
threshold × size × representation
```

ghép Awake và Drowsy cùng session.

Tính:

```text
n_paired_sessions
median(Drowsy - Awake)
IQR(delta)
% Drowsy > Awake
% equal
% Drowsy < Awake
```

Có thể dùng paired non-parametric test nếu cần, nhưng mục tiêu chính ở đây là **robustness của embedding selection**, không phải hypothesis testing về trạng thái.

## Đánh giá

Threshold phù hợp không nên tạo ra một pattern kiểu:

```text
Awake → m≈6
Drowsy → m≈9
```

một cách systematic nếu mục tiêu downstream là fixed common embedding configuration.

Nếu state differences nhỏ và không ổn định:

> No systematic state-dependent shift in the embedding dimension was observed across the evaluated residual-FNN thresholds.

Đây là bằng chứng hỗ trợ dùng cùng `m` cho Awake và Drowsy.

---

# Experiment 5 — Window-Length Robustness

## Task

Phân tích riêng:

```text
60 s
120 s
180 s
```

cho mỗi threshold và representation.

Tính:

```text
m_found_rate
median_m
IQR_m
mode_m
Q90_m
```

Sau đó dùng session-level summaries để so sánh:

```text
60 vs 120
60 vs 180
120 vs 180
```

## Output

Table:

```text
threshold
representation
window_size_s
N
m_found_rate
median_m
IQR_m
mode_m
Q90_m
```

Figure:

```text
selected_m vs threshold
```

chia theo:

```text
60 / 120 / 180 s
```

## Đánh giá

Tìm xem window ngắn có:

* coverage thấp hơn;
* selected m thấp/higher bất thường;
* dispersion lớn hơn.

Nếu 60 s gần với 120/180 s:

> Embedding-dimensional estimates were broadly stable across the three analysis-window durations, supporting the feasibility of the shortest 60-s window for subsequent nonlinear analysis.

Không gọi đây là proof nếu khác biệt vẫn tồn tại.

---

# Experiment 6 — Threshold-to-Threshold Agreement

## Task

So sánh selected dimension giữa các threshold liên tiếp:

```text
1 vs 2
2 vs 3
3 vs 4
4 vs 5
```

và so với threshold reference `1%`:

```text
1 vs 2
1 vs 3
1 vs 4
1 vs 5
```

Chỉ tính `Δm` khi cả hai threshold đều found.

Tính:

```text
exact_agreement_pct
within_1_dimension_pct
within_2_dimensions_pct
median_abs_delta_m
IQR_abs_delta_m
```

Đồng thời báo:

```text
newly_found_pct
```

tức số window trước đó không found nhưng found khi tăng threshold.

## Output

Table:

```text
threshold_a
threshold_b
n_comparable
exact_agreement
within_1
within_2
median_abs_delta_m
newly_found
```

Phân tích overall và riêng Raw/Processed.

## Đánh giá

Một vùng threshold ổn định sẽ có:

```text
median |Δm| nhỏ
high within-1 agreement
```

Ví dụ nếu:

```text
2→3
3→4
```

chỉ đổi rất ít selected m trong khi coverage gần saturation, đây là bằng chứng của một stable decision region.

---

# Experiment 7 — Residual-FNN Curve Plateau Analysis

## Mục tiêu

Không phụ thuộc hoàn toàn vào việc curve có crossing threshold hay không.

## Task

Từ `fnn_curves.csv`, với mỗi dimension:

```text
m = 1...10
```

tính theo dataset và strata:

```text
median FNN(m)
IQR FNN(m)
Q25
Q75
Q90
```

Cho:

```text
Overall
Raw / Processed
Awake / Drowsy
60 / 120 / 180
```

## Improvement metric

Tính:

```text
delta_fnn(m) = FNN(m) - FNN(m+1)
```

cho từng window.

Sau đó aggregate:

```text
median_delta_fnn(m)
IQR_delta_fnn(m)
```

## Output

Figure chính:

```text
median FNN% vs embedding dimension
```

với IQR.

Raw và Processed riêng.

Figure phụ:

```text
median ΔFNN(m→m+1) vs m
```

## Đánh giá plateau

Không hard-code plateau bằng một con số tùy ý ngay từ đầu.

Quan sát:

1. FNN giảm mạnh ở dimension thấp.
2. Mức giảm bắt đầu nhỏ đi ở đâu?
3. Sau dimension nào tăng thêm `m` chỉ tạo cải thiện nhỏ?
4. Vùng này có ổn định giữa Raw/Processed và window size không?

Đặc biệt đánh giá:

```text
m = 7
m = 8
m = 9
m = 10
```

Nếu:

```text
FNN(7) → FNN(8): còn cải thiện đáng kể
FNN(8) → FNN(9): cải thiện nhỏ
FNN(9) → FNN(10): rất nhỏ / không nhất quán
```

thì `m≈8` có bằng chứng plateau mạnh.

## Nhận xét cần ghi

Đây là bằng chứng quan trọng để tránh phụ thuộc hoàn toàn vào decision threshold:

> The embedding dimension was not determined solely from threshold crossing. The residual-FNN curves were also examined for a low-FNN plateau, representing the dimensional region beyond which additional coordinates produced little reduction in false nearest neighbors.

---

# Experiment 8 — Threshold Crossing Profile Across Dimension

## Task

Với mỗi threshold `1–5%` và mỗi dimension `1...10`, tính:

```text
percentage of windows with FNN(m) <= threshold
```

Quan trọng:

Đây KHÔNG phải `selected_m`.

Nó trả lời:

> Tại dimension m, bao nhiêu phần trăm window đã có residual FNN thấp hơn threshold?

## Output

Heatmap/table:

```text
dimension × threshold
```

cell:

```text
% windows satisfying FNN <= threshold
```

Làm riêng:

```text
Raw
Processed
```

## Đánh giá

Figure này sẽ trực tiếp cho thấy vùng:

```text
m≈7–8
```

có phải nơi phần lớn curves đạt residual-FNN thấp hay không.

Nó cũng giúp nhận diện:

```text
m=8 → gain lớn
m=9/10 → gain rất nhỏ
```

nếu có.

---

# Experiment 9 — Failure Analysis

## Task

Đối với từng threshold, lấy các window:

```text
m_found=False
```

Phân tích theo:

```text
representation
state
window_size
session
```

Tính:

```text
failure_rate
median min_fnn_percent
Q25/Q75 min_fnn_percent
```

Ngoài ra xác định tại `m=10`:

```text
FNN(10)
```

## Phân loại descriptive

Có thể chia failure thành:

```text
near-threshold:
min_fnn <= threshold + 1%

moderate:
threshold + 1% < min_fnn <= threshold + 5%

far:
min_fnn > threshold + 5%
```

Đây chỉ là diagnostic bins, không phải scientific rule.

## Đánh giá

Cần phân biệt:

### Case A

Window không crossing nhưng:

```text
FNN(m) đã plateau ở 1.5–2.5%
```

→ strict threshold issue.

### Case B

Window không crossing và:

```text
FNN vẫn cao / không ổn định tới m=10
```

→ reconstruction khó xác định từ FNN trong phạm vi hiện tại.

Không force `m=10`.

## Nhận xét cần ghi

> Failure to cross a strict residual-FNN threshold was treated as an informative result rather than automatically assigning the maximum investigated dimension.

---

# Experiment 10 — Session Influence / Pseudoreplication Audit

## Task

Đảm bảo kết luận threshold không bị một vài session dài chi phối.

Với từng threshold:

```text
number of windows per session
fraction of total windows per session
session median selected_m
session m_found_rate
```

Báo:

```text
largest-session contribution
median windows/session
range windows/session
```

## Đánh giá

Window-level distributions dùng để mô tả.

Session-level summaries dùng để kết luận về robustness.

## Nhận xét cần ghi

> Window-level results were used to characterize the distribution of FNN behavior, whereas session-level aggregation was used to prevent sessions containing more valid windows from disproportionately influencing methodological conclusions.

---

# Experiment 11 — Integrated Threshold Trade-off Scorecard

## Task

Không tạo một optimization score tùy ý.

Thay vào đó lập scorecard cho từng threshold:

```text
1%
2%
3%
4%
5%
```

Các tiêu chí:

| Criterion                 | Ý nghĩa                           |
| ------------------------- | --------------------------------- |
| Overall m_found rate      | coverage                          |
| Raw m_found rate          | robustness với waveform nhiễu hơn |
| Processed m_found rate    | coverage processed                |
| Median selected m         | dimensional consequence           |
| IQR selected m            | dispersion                        |
| Q90 selected m            | upper-tail requirement            |
| 60-s consistency          | short-window feasibility          |
| Awake/Drowsy stability    | state comparability               |
| Raw/Processed convergence | representation comparability      |
| Threshold agreement       | sensitivity                       |
| Plateau consistency       | threshold-independent support     |

## Output

Một final decision table.

Ví dụ cấu trúc:

```text
threshold | coverage | median_m | Q90_m | stability | plateau agreement | interpretation
```

Không hard-code "best".

## Đánh giá

Tìm **elbow/trade-off region**:

```text
strict side:
coverage tăng mạnh khi tăng threshold

stable middle:
coverage cải thiện nhưng m thay đổi ít

permissive side:
coverage gần saturation nhưng m tiếp tục bị kéo xuống
```

Threshold cuối nên nằm ở vùng giữa nếu dữ liệu hỗ trợ.

---

# Experiment 12 — Final Fixed-m Evaluation

Chỉ thực hiện sau khi threshold trade-off đã được mô tả đầy đủ.

## Task

Từ:

1. selected-m distributions;
2. threshold sensitivity;
3. session-level stability;
4. Raw/Processed agreement;
5. Awake/Drowsy robustness;
6. window-size robustness;
7. residual-FNN plateau;

xác định một **fixed embedding dimension candidate** cho downstream NTSA.

Không chọn riêng `m` cho:

```text
Awake
Drowsy
```

Nếu có thể, ưu tiên một common `m` cho Raw và Processed.

Nếu representation thực sự yêu cầu dimension khác nhau một cách mạnh và ổn định thì báo riêng, không ép common `m`.

## Candidate evaluation

Đối với mỗi candidate có bằng chứng, ví dụ:

```text
m = 7
m = 8
m = 9
```

báo:

```text
median FNN at m
IQR FNN at m
% <= 1%
% <= 2%
% <= 3%
% <= 4%
% <= 5%
median improvement to next dimension
```

Raw/Processed riêng.

## Tiêu chí chọn fixed m

Ưu tiên dimension:

1. nằm trong low-FNN plateau;
2. không underembed rõ ràng;
3. tăng thêm dimension chỉ giảm residual FNN rất ít;
4. ổn định trên `1–5%`;
5. ổn định giữa 60/120/180 s;
6. không phụ thuộc Awake/Drowsy;
7. hợp lý cho cả Raw và Processed nếu chọn common m;
8. không chọn vì downstream state separation tốt hơn.

## Kết luận cần phân biệt

Không dùng:

```text
"m = X is the true embedding dimension."
```

Không dùng:

```text
"m = X is absolutely optimal."
```

Dùng:

> Within the investigated FNN configuration and residual-FNN decision range, `m = X` provided the most defensible trade-off between residual false-neighbor reduction, threshold-crossing coverage, dimensional stability, and computational parsimony.

Hoặc nếu plateau rõ:

> A common embedding dimension of `m = X` was selected from the stable low-FNN plateau rather than from a single arbitrary residual-FNN threshold.

---

# Required Figures

Tối thiểu tạo các figure sau:

1. `threshold_vs_found_rate.png`

   * overall
   * Raw/Processed

2. `threshold_vs_selected_m.png`

   * median + IQR
   * Raw/Processed

3. `fnn_curve_population.png`

   * median FNN(m) + IQR
   * Raw/Processed

4. `fnn_improvement_curve.png`

   * median `ΔFNN(m→m+1)`

5. `threshold_dimension_heatmap.png`

   * `% windows satisfying FNN(m) <= threshold`

6. `selected_m_by_window_size.png`

   * threshold × 60/120/180

7. `selected_m_by_state.png`

   * Awake/Drowsy, preferably session-level

Không tạo quá nhiều plots nếu chúng không bổ sung thông tin mới.

---

# Required Output Files

```text
results/fnn_threshold/
├── fnn_threshold_window_results.csv
├── fnn_threshold_session_summary.csv
├── fnn_threshold_overall_summary.csv
├── fnn_threshold_representation_summary.csv
├── fnn_threshold_state_summary.csv
├── fnn_threshold_window_size_summary.csv
├── fnn_threshold_agreement.csv
├── fnn_plateau_summary.csv
├── fnn_failure_summary.csv
└── figures/
```

Không sửa `fnn_curves.csv`.

---

# Final Reporting Questions

Notebook cuối cùng phải trả lời rõ các câu hỏi sau.

## Q1

Decision threshold `1–5%` ảnh hưởng mạnh đến `m_found_rate` như thế nào?

## Q2

Threshold ảnh hưởng bao nhiêu đến distribution của `selected_m`?

## Q3

Có tồn tại vùng threshold mà coverage tăng nhưng selected dimension gần như ổn định không?

## Q4

Raw và Processed có cùng hỗ trợ một vùng embedding dimension hay không?

## Q5

Awake và Drowsy có systematic embedding-dimension difference hay không?

## Q6

Kết luận có ổn định giữa cửa sổ `60/120/180 s` hay không?

## Q7

FNN curves có hình thành residual-FNN plateau rõ ràng không?

## Q8

Nếu strict threshold không được crossing, nguyên nhân chủ yếu là residual plateau thấp nhưng > threshold hay FNN vẫn còn cao?

## Q9

Threshold nào cung cấp trade-off hợp lý nhất giữa strictness và coverage?

## Q10

Fixed embedding dimension nào được hỗ trợ mạnh nhất bởi **toàn bộ bằng chứng**, thay vì bởi một threshold đơn lẻ?

---

# Scientific Guardrails

* Không optimize threshold để cố thu được `m=8`.
* Không chọn threshold dựa trên khả năng phân biệt Awake/Drowsy.
* Không xem tất cả windows là observational units độc lập cho inference.
* Không force `selected_m=max_m` khi không crossing.
* Không gọi `selected_m` là intrinsic/true attractor dimension.
* Không diễn giải FNN thấp là bằng chứng chaos.
* Không diễn giải Raw/Processed difference thành khác biệt sinh lý cụ thể nếu chưa có bằng chứng.
* Luôn phân biệt:

  * FNN curve behavior;
  * threshold crossing;
  * final fixed embedding decision.
* Quyết định cuối phải được đưa ra **sau khi xem toàn bộ threshold `1–5%`**, không đặt primary threshold trước khi chạy analysis.

```
```
