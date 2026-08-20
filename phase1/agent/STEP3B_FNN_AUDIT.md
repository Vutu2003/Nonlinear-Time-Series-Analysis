````markdown
# Experimental Design — FNN on Full PPG Dataset

## Mục tiêu

Ước lượng embedding dimension `m` bằng FNN trên từng analysis window, nhưng tổ chức tính toán độc lập theo:

```text
60 s → 120 s → 180 s
````

Sau đó mới tổng hợp để đánh giá ảnh hưởng của:

```text
Session × State × Representation × Window size
```

---

## 1. Cấu hình chính

```text
R_tol = 15
A_tol = 2
FNN threshold = 1%
max_m = 10
```

Fixed embedding delay theo representation:

```text
Raw PPG:
tau = round(0.20 * fs)
25 Hz → 5 samples
50 Hz → 10 samples

Processed PPG:
tau = round(0.16 * fs)
25 Hz → 4 samples
50 Hz → 8 samples
```

Chỉ dùng window pass quasi-stationarity của representation tương ứng.

---

## 2. Chạy riêng theo window size

Tạo ba section/cell độc lập:

```text
Experiment A → tất cả 60-s windows
Experiment B → tất cả 120-s windows
Experiment C → tất cả 180-s windows
```

Trong mỗi section:

1. Duyệt từng session.
2. Load Raw và Processed riêng.
3. Với từng window, chạy FNN độc lập.
4. Không gộp nhiều window thành một signal.
5. Lưu kết quả trước khi chuyển sang window size tiếp theo.

---

## 3. Window-level output

Một hàng cho mỗi `window × representation`:

```text
session
window_id
window_size_s
label
representation
fs
tau_samples
max_m
selected_m
min_fnn_percent
valid_count_at_selected_m
m_found
```

Giữ toàn bộ FNN curve và valid-neighbor counts ở cấu trúc riêng nếu cần diagnostic.

Nếu không đạt `FNN <= 1%` trước `max_m`:

```text
selected_m = None
m_found = False
```

Không tự động dùng `max_m`.

---

## 4. Coverage analysis

Cho mỗi:

```text
window_size × state × representation
```

báo:

```text
N windows
N selected_m found
N None
success rate
```

Kiểm tra failure có tập trung ở:

* Raw/Processed;
* Awake/Drowsy;
* 60/120/180 s;
* session cụ thể.

---

## 5. Distribution của selected m

Theo:

```text
60/120/180
× Awake/Drowsy
× Raw/Processed
```

báo:

```text
N
median m
IQR
min
max
mode
```

Plot distribution/count của `selected_m`.

Mục tiêu: xác định `m` có tập trung quanh một vùng hẹp hay không.

---

## 6. Session-level aggregation

Trong mỗi:

```text
session × window_size × state × representation
```

tính:

```text
n_windows
median_m
IQR_m
mode_m
m_found_rate
```

Session là observational unit chính; không dùng toàn bộ window như independent samples cho inference Awake–Drowsy.

---

## 7. Awake vs Drowsy

Với session có đủ hai state, so sánh:

```text
median_m_Drowsy - median_m_Awake
```

riêng cho:

```text
60/120/180 × Raw/Processed
```

Báo:

```text
paired N
median delta
IQR delta
% higher / equal / lower
```

Mục tiêu: kiểm tra embedding dimension có state-dependent hay không.

---

## 8. Raw vs Processed

Ưu tiên paired analysis trên cùng analysis window khi cả hai representation đều hợp lệ.

Báo:

```text
agreement of selected_m
median difference
IQR difference
% exact agreement
% within ±1 dimension
```

Mục tiêu: xác định preprocessing làm thay đổi required embedding dimension đến mức nào.

---

## 9. Window-size stability

Ở session level, so sánh:

```text
60 vs 120
60 vs 180
120 vs 180
```

cho cùng state và representation.

Báo:

```text
median absolute difference
agreement
correlation nếu phù hợp
```

Đặc biệt đánh giá 60 s có cho `m` tương đương 120/180 s hay không.

---

## 10. Diagnostic FNN curves

Chọn có hệ thống một số window:

```text
m thấp
m trung vị
m cao
selected_m=None
Raw vs Processed khác nhau
Awake vs Drowsy khác nhau
```

Plot:

```text
FNN (%) vs embedding dimension
```

kèm đường `1%`.

Mục tiêu: xác nhận automatic decision phù hợp với hình dạng FNN curve.

---

## 11. Sensitivity cohort

Không cần chạy sensitivity trên toàn dataset.

Chọn stratified cohort theo:

```text
session × size × state × representation
```

Thử:

```text
R_tol = 10, 15, 20
A_tol = 1.5, 2.0, 2.5
FNN threshold = 0.5%, 1%, 2%
```

Nếu dùng Theiler exclusion, đánh giá riêng:

```text
theiler = 0
theiler = tau
theiler = 2*tau
```

Báo:

```text
selected_m agreement
median |delta m|
m_found rate
```

---

## 12. Final decision về fixed m

Sau khi có toàn bộ distribution, đánh giá:

```text
Raw PPG → m_fixed_raw ?
Processed PPG → m_fixed_processed ?
```

Không chọn `m` theo Awake/Drowsy.

Fixed `m` nên:

* nằm trong vùng được FNN hỗ trợ ở phần lớn window/session;
* tránh under-embedding;
* ổn định giữa 60/120/180 s;
* ít nhạy với threshold hợp lý;
* giữ cùng embedding configuration giữa Awake và Drowsy.

Window-specific `selected_m` được giữ làm validation/sensitivity reference.

---

## Output

```text
results/fnn/
├── fnn_60_results.csv
├── fnn_120_results.csv
├── fnn_180_results.csv
├── fnn_window_results.csv
└── fnn_session_summary.csv
```

---

## Ready to freeze

FNN strategy sẵn sàng freeze nếu:

* phần lớn window tìm được `m`;
* distribution của `m` có vùng tập trung rõ;
* không có strong Awake–Drowsy selection bias;
* kết quả ổn định giữa 60/120/180 s;
* sensitivity không làm `m` thay đổi mạnh;
* fixed `m` theo representation có thể được biện luận từ dữ liệu thay vì chọn tùy ý.

```
```
