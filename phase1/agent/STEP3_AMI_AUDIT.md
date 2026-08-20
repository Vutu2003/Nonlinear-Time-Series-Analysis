````markdown
# Experimental Design — AMI on Full PPG Dataset

## Mục tiêu

Ước lượng time delay `tau` cho từng analysis window bằng:

```text
PPG window
→ AMI(tau) bằng KSG
→ first local minimum
→ tau_window
````

Phân tích theo cấu trúc:

```text
Session
└── Window size: 60 / 120 / 180 s
    └── State: Awake / Drowsy
        └── Representation: Raw / Processed
            └── từng window
```

---

## 1. Cấu hình chính

```text
KSG: k = 3
tau: đơn vị samples
tau_seconds = tau / fs
stationarity_only = True theo từng representation
```

`max_lag` phải được định nghĩa theo **seconds** rồi chuyển sang samples theo `fs` để session 25 Hz và 50 Hz có cùng search range vật lý.

Không thay thế bằng global minimum nếu không tìm thấy first local minimum:

```text
tau = None
```

---

## 2. Sanity check trên một session

Chọn một session có đủ Awake/Drowsy.

Chạy toàn bộ:

```text
60 / 120 / 180 s
× Awake / Drowsy
× Raw / Processed
```

Kiểm tra:

* mọi window trả AMI curve hợp lệ;
* `tau` nằm trong search range;
* Raw/Processed dùng đúng stationarity flag;
* `tau_samples` và `tau_seconds` được lưu đúng.

Plot một số AMI curve đại diện và đánh dấu first local minimum.

---

## 3. Chạy AMI toàn dataset

Với mọi NTSA-ready window, lưu một record:

```text
session
window_id
window_size_s
label
representation
fs
tau_samples
tau_seconds
ami_at_tau
tau_found
```

Không loại bỏ record khi `tau=None`.

---

## 4. Coverage / failure analysis

Tổng hợp theo:

```text
window size × state × representation
```

Báo:

```text
N windows
N tau found
N tau=None
success rate (%)
```

Kiểm tra `tau=None` có tập trung ở state, representation, window size hoặc session cụ thể hay không.

---

## 5. Phân phối tau ở window level

Cho từng:

```text
60 / 120 / 180
× Awake / Drowsy
× Raw / Processed
```

Báo:

```text
N
median tau_seconds
IQR
min
max
```

Dùng `tau_seconds` làm đại lượng chính để so sánh giữa session khác `fs`.

Plot distribution/boxplot để phát hiện outlier hoặc multimodality.

---

## 6. Aggregate về session level

Trong mỗi:

```text
session × window size × state × representation
```

tính:

```text
n_windows
median_tau
IQR_tau
tau_found_rate
```

`median` là summary chính vì `tau` rời rạc và có thể lệch/outlier.

Không coi các window trong cùng session là independent observations.

---

## 7. Awake vs Drowsy

Chỉ dùng session có dữ liệu hợp lệ cho cả hai state tại cùng:

```text
window size × representation
```

So sánh session-level `median_tau_seconds`:

```text
Awake ↔ Drowsy
```

Đánh giá:

* hướng thay đổi;
* độ nhất quán giữa session;
* dependence theo 60/120/180 s.

Mục đích: kiểm tra liệu temporal dependence scale của PPG có thay đổi theo trạng thái.

---

## 8. Raw vs Processed

Trên cùng analysis window, so sánh:

```text
tau_raw ↔ tau_processed
```

Báo:

```text
correlation
median difference
IQR difference
% exact/near agreement
```

Mục đích: đánh giá preprocessing ảnh hưởng tới lựa chọn embedding delay đến mức nào.

Đây là methodological comparison, không phải trực tiếp trả lời RQ Raw PPG vs PPI.

---

## 9. Window-size stability

Trong cùng session/state/representation, so sánh:

```text
60 ↔ 120 ↔ 180 s
```

Đánh giá session-level median tau có ổn định khi tăng window length hay không.

Nếu 60 s cho tau tương đương 120/180 s, đây là bằng chứng hỗ trợ short-window feasibility.

---

## 10. Sensitivity analysis

### KSG neighbor count

```text
k = 2, 3, 4
```

So sánh:

```text
tau agreement
median |Δtau|
tau-found rate
```

### max_lag

Thử một vùng search hợp lý quanh cấu hình chính.

Mục tiêu: first minimum không bị quyết định chủ yếu bởi boundary của search range.

---

## 11. Visual validation

Chọn có hệ thống:

```text
tau thấp
tau trung vị
tau cao
tau=None
Awake vs Drowsy
Raw vs Processed
```

Plot:

```text
AMI vs lag_seconds
```

đánh dấu first local minimum để xác nhận decision rule phù hợp với hình dạng curve.

---

## 12. Output cuối

### Window-level

```text
ami_window_results.csv
```

Một hàng = một window × representation.

### Session-level

```text
ami_session_summary.csv
```

Một hàng =:

```text
session × window_size × state × representation
```

---

## Liên hệ Research Questions

### RQ1 — Existence of nonlinear deterministic dynamics

AMI **không chứng minh determinism/chaos**. Nó cung cấp delay phù hợp để reconstruct phase space cho các kiểm định nonlinear tiếp theo.

### RQ2 — State-dependent nonlinear dynamics

Awake–Drowsy differences trong `tau` có thể cho thấy thay đổi về temporal dependence scale, nhưng chỉ là supporting evidence.

### RQ3 — Representation dependence

Raw–Processed comparison đánh giá độ robust của embedding đối với preprocessing. RQ3 chính thức vẫn cần so sánh **Raw PPG với PPI** ở các phân tích downstream.

---

## Ready to freeze AMI strategy

Freeze nếu:

* first minimum được tìm thấy ở phần lớn window;
* AMI curve visually hợp lý;
* `tau` ổn định với `k=2–4`;
* không phụ thuộc mạnh vào `max_lag`;
* không có failure bias rõ theo Awake/Drowsy;
* session-level tau ổn định hợp lý giữa 60/120/180 s;
* khác biệt Raw/Processed được định lượng và giải thích rõ.

```
```
