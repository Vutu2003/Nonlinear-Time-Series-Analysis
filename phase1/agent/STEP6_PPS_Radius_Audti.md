````markdown
# End-to-End Experiment — PPS Radius Calibration per Session

## 1. Mục tiêu

Xây dựng một pipeline end-to-end chạy độc lập cho từng session để thu thập dữ liệu phục vụ calibration `rho*` trên toàn bộ 20 sessions.

Mỗi lần chạy chỉ cần truyền:

```text
session_id = n
````

Pipeline tự động:

```text
load eligible windows
→ optimize rho cho từng window
→ compute geometry-normalized rho
→ aggregate theo representation × state
→ lưu CSV theo session
→ lưu 4 figure diagnostic theo session
```

Giai đoạn check đầu tiên:

```text
session_id = 1
```

Không sinh PPS ensemble cuối.
Không chạy surrogate hypothesis test.
Không chạy Simplex/RQA.

---

# 2. Frozen configuration

```text
Representations:
- Processed
- Raw

States:
- Awake
- Drowsy

Window sizes:
- 60 s
- 120 s
- 180 s
```

Pool cả 3 window sizes khi tạo summary theo state/representation, nhưng vẫn lưu `window_size` trong CSV để audit sau này.

Reconstruction:

```text
m = 8

Processed:
tau = 0.16 s = 8 samples at 50 Hz

Raw:
tau = 0.20 s = 10 samples at 50 Hz
```

Eligibility:

```text
Processed:
stationary = True

Raw:
stationary = False
```

PPS rho optimization:

```text
segment_length = 2
count_mode = "at_least"

Processed rho grid:
5 → 200
21 log-spaced points

Raw rho grid:
5 -> 400
21 log-spaced points

trials = 3
```

Dùng deterministic seed theo:

```text
session
representation
state
window_size
window_id
```

để rerun cho kết quả reproducible.

---

# 3. Yêu cầu code

Viết một script/pipeline end-to-end có entry point tương tự:

```python
run_session(session_id)
```

Ví dụ:

```python
run_session(1)
```

Không cần chỉnh code khi chuyển session.

Pipeline phải:

```text
- tự load dữ liệu đúng session;
- tự xử lý Raw/Processed;
- tự xử lý Awake/Drowsy;
- tự xử lý 60/120/180 s;
- tự optimize rho;
- tự tạo summary;
- tự lưu CSV;
- tự lưu 4 figures.
```

Không lưu surrogate waveform hoặc PPS indices.

---

# 4. TASK 1 — Load session

Input:

```text
session_id
```

Load toàn bộ eligible windows của session.

Tạo metadata:

```text
session
representation
state
window_size
window_id
sampling_rate
N
tau_samples
```

Validate:

```text
NaN = 0
Inf = 0
N sufficient for embedding
```

In summary counts:

```text
representation × state × window_size
```

---

# 5. TASK 2 — Optimize rho per window

Với từng window:

1. chọn `tau` theo representation;
2. chọn rho grid theo representation;
3. chạy `optimize_rho(...)`.

Thu:

```text
rho_star
peak_C2
peak_C2_sd
boundary_flag
```

Không generate surrogate sau khi đã tìm `rho_star`.

---

# 6. TASK 3 — Compute geometry scale

Cho từng window, từ reconstructed phase space tính:

```text
median_NN_distance
attractor_diameter
```

Sau đó:

$$
c_i
===

# \rho_{NN,i}

\frac{\rho_i^*}
{d_{\mathrm{NN,med},i}}
$$

và:

$$
\rho_{D,i}
==========

\frac{\rho_i^*}
{D_i}
$$

Giữ `rho_NN` là normalized metric chính.

---

# 7. TASK 4 — Create per-window result dataframe

Mỗi row tương ứng một window.

CSV cần các cột:

```text
session
representation
state
window_size
window_id
N
sampling_rate
tau_samples

rho_star
median_NN_distance
rho_NN

attractor_diameter
rho_D

peak_C2
peak_C2_sd
boundary_flag
```

Không cần lưu:

```text
signal
embedding matrix
PPS waveform
PPS indices
full C2 curve
```

---

# 8. TASK 5 — Save session CSV

Tên file:

```text
pps_radius_session_01.csv
```

Ví dụ session 10:

```text
pps_radius_session_10.csv
```

Lưu một CSV duy nhất cho mỗi session.

Nếu file đã tồn tại:

```text
không overwrite âm thầm
```

hoặc yêu cầu explicit overwrite flag.

---

# 9. TASK 6 — Aggregate within session

Pool:

```text
60 + 120 + 180 s
```

theo 4 nhóm:

```text
Processed Awake
Processed Drowsy
Raw Awake
Raw Drowsy
```

Cho mỗi group tính:

```text
N
median rho*
Q1 rho*
Q3 rho*
IQR rho*

median rho_NN
Q1 rho_NN
Q3 rho_NN
IQR rho_NN
```

Chỉ dùng aggregation này cho visualization.

CSV gốc vẫn giữ window-level data.

---

# 10. TASK 7 — Figure 1: Processed absolute rho

Vẽ:

```text
Processed — Absolute PPS radius
```

X-axis:

```text
Awake
Drowsy
```

Y-axis:

```text
rho*
```

Hiển thị:

```text
individual window points
median
IQR
```

Pool 60/120/180 s.

Title phải chứa session:

```text
Session 1 — Processed absolute PPS radius
```

Lưu:

```text
session_01_processed_rho_absolute.png
```

---

# 11. TASK 8 — Figure 2: Raw absolute rho

Tương tự Figure 1.

Title:

```text
Session 1 — Raw absolute PPS radius
```

Lưu:

```text
session_01_raw_rho_absolute.png
```

---

# 12. TASK 9 — Figure 3: Processed geometry-normalized rho

Vẽ:

$$
c_i=
\frac{\rho_i^*}
{d_{\mathrm{NN,med},i}}
$$

Title:

```text
Session 1 — Processed geometry-normalized PPS radius
```

X-axis:

```text
Awake
Drowsy
```

Y-axis:

```text
c = rho* / median NN distance
```

Hiển thị:

```text
individual window points
median
IQR
```

Lưu:

```text
session_01_processed_rho_normalized.png
```

---

# 13. TASK 10 — Figure 4: Raw geometry-normalized rho

Tương tự Figure 3.

Lưu:

```text
session_01_raw_rho_normalized.png
```

---

# 14. TASK 11 — Console summary

Sau khi chạy xong một session, in một summary ngắn:

```text
Session: 1
Total windows: ...

Boundary optima:
N / total

Processed Awake:
N
median rho*
median rho_NN

Processed Drowsy:
N
median rho*
median rho_NN

Raw Awake:
N
median rho*
median rho_NN

Raw Drowsy:
N
median rho*
median rho_NN
```

Cuối cùng in:

```text
CSV saved:
...

Figures saved:
...
```

---

# 15. Folder structure

Gợi ý:

```text
results/
└── pps_radius_calibration/
    ├── csv/
    │   ├── pps_radius_session_01.csv
    │   ├── pps_radius_session_02.csv
    │   └── ...
    │
    └── figures/
        ├── session_01_processed_rho_absolute.png
        ├── session_01_raw_rho_absolute.png
        ├── session_01_processed_rho_normalized.png
        ├── session_01_raw_rho_normalized.png
        └── ...
```

---

# 16. Session 1 validation criteria

Trước khi chạy Session 2–20, kiểm tra Session 1:

```text
[ ] đúng số eligible windows

[ ] Processed dùng stationary=True

[ ] Raw dùng stationary=False

[ ] tau Processed = 8 samples

[ ] tau Raw = 10 samples

[ ] rho grids đúng representation

[ ] boundary fraction thấp

[ ] CSV có một row/window

[ ] rho_NN = rho_star / median_NN_distance

[ ] 4 figures được tạo đúng

[ ] figures pool 60/120/180 s

[ ] không sinh/lưu PPS waveform

[ ] rerun cùng seed cho cùng rho*
```

Nếu Session 1 PASS, giữ nguyên pipeline cho Session 2–20.

---

# 17. Cách chạy

Mục tiêu cuối cùng là chỉ cần:

```python
run_session(1)
```

sau đó:

```python
run_session(2)
run_session(3)
...
run_session(20)
```

hoặc từ command line:

```bash
python run_pps_radius.py --session 1
```

Sau khi Session 1 được kiểm tra thành công, không thay đổi scientific configuration giữa các session.

---

# 18. Không làm trong pipeline này

```text
Không optimize fine rho grid lần hai.

Không generate 10/39 PPS ensemble.

Không lưu PPS waveform.

Không chạy Simplex.

Không chạy RQA.

Không tính surrogate p-value.

Không quyết định frozen c trong từng session.

Không aggregate across sessions ở script này.
```

Cross-session aggregation sẽ là một script/notebook riêng sau khi đủ 20 CSV.

---

# Expected output cho mỗi lần chạy

```text
INPUT
session_id = n

OUTPUT
1 CSV:
pps_radius_session_nn.csv

4 figures:
processed absolute rho
raw absolute rho
processed normalized rho
raw normalized rho
```

Pipeline này chỉ có một nhiệm vụ:

> thu thập nhất quán window-level `rho*` và geometry-normalized radius cho từng session để sau đó đánh giá sự ổn định trên toàn bộ 20 sessions.

```
```
