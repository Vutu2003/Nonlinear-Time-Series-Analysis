Mình đề xuất notebook full dataset chỉ cần **9 cell chính**, đủ để chạy, QC, aggregate đúng hierarchy, lưu output chuẩn để phân tích sau, và tạo đúng các figure publication-ready cho RQ2.

## Cell 1 — Setup và frozen protocol

Khai báo rõ toàn bộ protocol:

```text
m = 8

Processed:
tau = 0.16 s

Raw:
tau = 0.20 s

Theiler:
W = (m - 1) * tau_samples

Distance:
Euclidean

Fixed RR:
target_rr = 0.02

Line cutoffs:
l_min = 2
v_min = 2

Metrics:
DET, Lmean, ENTR, Lmax, LAM, TT, Vmax
```

Load metadata/full dataset và các eligibility rules:

```text
Processed:
SQI + Processed stationarity

Raw:
SQI only
no stationarity filtering
```

**Output inline:** protocol summary + số session.

---

## Cell 2 — Coverage trước khi chạy

Tổng hợp số eligible windows theo:

```text
session
× representation
× state
× window_size
```

Kiểm tra paired Awake–Drowsy availability.

**Output inline:** coverage table + số paired sessions cho từng `representation × window_size`.

Nếu coverage bất thường thì dừng trước RQA.

---

## Cell 3 — Full window-level RQA

Chạy `run_rqa()` trên toàn bộ eligible windows.

Mỗi window lưu:

```text
session
representation
state
window_size
window_id
fs
tau_samples
theiler_samples

epsilon
target_rr
achieved_rr

DET
Lmean
ENTR
Lmax
LAM
TT
Vmax

n_diagonal_lines
n_vertical_lines
```

**Lưu file:**

```text
rqa_window_level.csv
```

Đây là master output thấp nhất, không aggregate.

---

## Cell 4 — Full-dataset QC

Kiểm tra:

* NaN / Inf;
* invalid metrics;
* `abs(achieved_rr - 0.02)`;
* zero diagonal support;
* zero vertical support;
* DET/LAM ngoài `[0,1]`;
* `Lmax < Lmean`;
* `Vmax < TT`.

Tóm tắt theo representation/window size.

**Lưu file:**

```text
rqa_qc_summary.csv
```

Không tạo publication figure ở cell này.

---

## Cell 5 — Session-level aggregation

Aggregate windows theo:

[
Session
\times Representation
\times State
\times WindowSize
]

Cho từng metric tính:

```text
mean
std
median
n_windows
```

Output schema nên là **wide table**, ví dụ:

```text
session
representation
state
window_size
n_windows

DET_mean
DET_std
DET_median

Lmean_mean
Lmean_std
Lmean_median

ENTR_mean
ENTR_std
ENTR_median

Lmax_mean
Lmax_std
Lmax_median

LAM_mean
LAM_std
LAM_median

TT_mean
TT_std
TT_median

Vmax_mean
Vmax_std
Vmax_median
```

**Lưu file:**

```text
rqa_session_state_summary.csv
```

Đây là bảng chính để đánh giá within-session robustness.

---

## Cell 6 — Paired Awake–Drowsy contrasts

Từ **session means**, chỉ giữ các session có paired Awake/Drowsy cho cùng:

```text
representation
window_size
```

Tính:

[
\Delta q
========

q_{Drowsy}-q_{Awake}
]

cho 7 metrics.

Schema:

```text
session
representation
window_size
n_awake_windows
n_drowsy_windows

delta_DET
delta_Lmean
delta_ENTR
delta_Lmax
delta_LAM
delta_TT
delta_Vmax
```

**Lưu file:**

```text
rqa_session_paired_deltas.csv
```

Đây là file trực tiếp nhất cho RQ2.

---

## Cell 7 — Across-session RQ2 summary

Aggregate `delta` qua sessions theo:

```text
representation
× window_size
× metric
```

Tính:

```text
n_paired_sessions
mean_delta
std_delta
median_delta
q25_delta
q75_delta
n_delta_positive
fraction_delta_positive
```

Có thể thêm:

```text
min_delta
max_delta
```

nếu muốn QC.

Schema long-table:

| representation | window_size | metric | n_paired_sessions | mean_delta | std_delta | median_delta | q25_delta | q75_delta | n_delta_positive | fraction_delta_positive |
| -------------- | ----------: | ------ | ----------------: | ---------: | --------: | -----------: | --------: | --------: | ---------------: | ----------------------: |

**Lưu file:**

```text
rqa_rq2_summary.csv
```

Đây sẽ là **main numerical output cho RQ2**.

---

## Cell 8 — Publication-ready figures cho RQ2

Chỉ lưu các figure thực sự cần cho paper.

Mình đề xuất đúng **2 loại figure**.

### Figure 1 — Awake vs Drowsy RQA profiles

Cho từng representation:

* rows hoặc panels theo `60 / 120 / 180 s`;
* metric-level comparison Awake vs Drowsy;
* dùng session-level means, không pooled windows;
* hiển thị central tendency + uncertainty across sessions.

Có thể tổ chức 7 metrics thành:

```text
Diagonal family:
DET, Lmean, ENTR, Lmax

Vertical family:
LAM, TT, Vmax
```

Nếu 7 metric trong một figure quá dày thì tách thành:

```text
Figure RQA-A: diagonal metrics
Figure RQA-B: vertical metrics
```

### Figure 2 — Paired session delta

Plot:

[
\Delta = Drowsy-Awake
]

cho từng metric, tách Raw/Processed và 60/120/180 s.

Ưu tiên dạng:

* paired-session dot distribution / strip;
* zero reference line;
* mean/median overlay.

Figure này rất mạnh cho RQ2 vì thể hiện:

* direction;
* across-session variability;
* sign consistency.

**Chỉ lưu các figure publication-ready**, ví dụ:

```text
fig_rqa_diagonal_rq2.png
fig_rqa_vertical_rq2.png
fig_rqa_paired_deltas_rq2.png
```

Có thể lưu thêm PDF/SVG nếu workflow paper cần vector.

Không lưu exploratory plots.

---

## Cell 9 — Final run summary

Print concise status:

```text
Total windows processed
Processed windows
Raw windows

Invalid outputs
Max achieved-RR error
Zero diagonal support
Zero vertical support

Paired sessions:
Processed 60/120/180
Raw 60/120/180
```

Sau đó display `rqa_rq2_summary` toàn bộ.

Không thực hiện inferential test ở notebook này nếu mục tiêu hiện tại vẫn là tạo **descriptive NTSA evidence cho RQ2**.

---

# Output files cần Codex lưu

Mình sẽ freeze đúng 5 data outputs:

```text
1. rqa_window_level.csv
2. rqa_qc_summary.csv
3. rqa_session_state_summary.csv
4. rqa_session_paired_deltas.csv
5. rqa_rq2_summary.csv
```

Ý nghĩa hierarchy:

```text
rqa_window_level
        ↓
repeated realizations

rqa_session_state_summary
        ↓
Session × State × Window Size × Representation

rqa_session_paired_deltas
        ↓
Drowsy - Awake within session

rqa_rq2_summary
        ↓
across-session descriptive RQ2 evidence
```

## Note trực tiếp cho Codex

```text
Use the frozen RQA protocol exactly as specified.

Do not change:
- m
- representation-specific tau
- Theiler rule
- target RR
- l_min
- v_min
- distance metric
- eligibility rules

The statistical/inference unit is session.
Never pool windows across sessions as independent observations.

Use window-level results only to compute within-session summaries.

Save only the specified CSV outputs and publication-ready RQ2 figures.
Do not save exploratory or QC figures.

All saved tables must contain explicit column names, no implicit MultiIndex,
and be directly reloadable for later statistical analysis.

Use Drowsy - Awake consistently for all delta metrics.
```

Với cấu trúc này, sau full run bạn chỉ cần gửi mình **QC summary + session-state table + paired-delta table + RQ2 summary**, là chúng ta có thể đánh giá ngay RQA đã cung cấp evidence cho RQ2 mạnh đến đâu và Raw/Processed khác nhau thế nào.
