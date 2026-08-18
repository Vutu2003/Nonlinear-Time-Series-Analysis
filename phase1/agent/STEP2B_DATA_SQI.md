````markdown
# STEP 2B — Dataset-Wide SQI Evaluation Design

## Mục tiêu

Áp dụng `detect_motion_artifacts()` trên toàn bộ processed dataset để:

- đánh giá tính ổn định của SQI giữa các session;
- định lượng motion artifact trong dataset;
- kiểm tra artifact có lệch theo `Awake/Drowsy` hay không;
- xác định SQI có đủ bằng chứng để freeze trước segmentation.

Cấu hình chính:

```text
window_s = 5.0
threshold = 3.5
````

---

## Cell 1 — Load processed dataset

* Đọc toàn bộ CSV trong `data_processed/dhdata`.
* Với mỗi session lấy:

  * `Time (s)`
  * `PPG processed`
  * `Label`
* Ước lượng `fs` từ `Time (s)`.
* Chạy `detect_motion_artifacts()`.

Output:

| Session | Samples | Duration (s) | fs (Hz) | SQI status |
| ------- | ------: | -----------: | ------: | ---------- |

Kiểm tra:

* mask cùng chiều dài signal;
* boolean;
* không runtime error.

---

## Cell 2 — Artifact summary per session

Gộp các SQI window liên tiếp bị flag thành artifact event.

Với mỗi session tính:

* số artifact event;
* tổng artifact duration;
* artifact duration (%);
* longest artifact;
* số artifact window.

Output:

| Session | Events | Artifact windows | Duration (s) | Duration (%) | Longest (s) |
| ------- | -----: | ---------------: | -----------: | -----------: | ----------: |

---

## Cell 3 — Dataset-level artifact distribution

Tổng hợp toàn dataset:

* total artifact events;
* median / IQR artifact duration (%);
* min / max artifact duration (%);
* số session không có artifact;
* số session có artifact.

Plot:

* distribution của artifact duration (%);
* artifact event count theo session.

Mục tiêu:

* xác định SQI có flag quá nhiều hoặc quá ít dữ liệu;
* tìm session outlier.

---

## Cell 4 — Awake vs Drowsy artifact burden

Dùng `Label` để tính riêng:

* thời lượng Awake/Drowsy;
* artifact duration Awake/Drowsy;
* artifact percentage trong từng state;
* số artifact event trong từng state.

Output:

| Session | Awake artifact (%) | Drowsy artifact (%) | Awake events | Drowsy events |
| ------- | -----------------: | ------------------: | -----------: | ------------: |

Dataset summary:

| State | Total duration | Artifact duration | Artifact (%) |
| ----- | -------------: | ----------------: | -----------: |

Mục tiêu:

* kiểm tra SQI có systematic state bias hay không.

Không diễn giải artifact difference như một hiệu ứng sinh lý.

---

## Cell 5 — Feature-level diagnostic

Tính lại theo từng full 5-s window:

* robust amplitude `A`;
* roughness `R`;
* `z_A`;
* `z_R`;
* artifact flag.

Tổng hợp:

* tỷ lệ artifact do `A` vượt threshold;
* tỷ lệ do `R`;
* tỷ lệ do cả hai.

Plot:

* scatter `z_A` vs `z_R`;
* highlight artifact windows;
* threshold lines tại `3.5`.

Mục tiêu:

* hiểu feature nào đang điều khiển SQI trên dataset.

---

## Cell 6 — Automatic outlier selection

Tự động chọn:

* top 3 session có artifact duration (%) cao nhất;
* top 3 artifact window có `z_A` cao nhất;
* top 3 artifact window có `z_R` cao nhất.

Không hard-code session.

Output:

* danh sách session/window được chọn cho visual inspection.

---

## Cell 7 — Targeted visual inspection

Với các window được chọn:

* plot `PPG processed`;
* highlight chính xác artifact interval;
* thêm một đoạn trước/sau artifact để có context;
* hiển thị:

  * session;
  * interval;
  * label;
  * `z_A`;
  * `z_R`.

Mục tiêu:

* xác nhận các flag tương ứng với waveform abnormality thực tế;
* kiểm tra false-positive rõ ràng.

---

## Cell 8 — Sampling-rate comparison

So sánh descriptively giữa:

```text
~25 Hz
~50 Hz
```

Metrics:

* artifact duration (%);
* artifact event count;
* `z_A`;
* `z_R`.

Không thực hiện statistical inference vì nhóm 50 Hz chỉ có rất ít session.

Mục tiêu:

* kiểm tra SQI không có hành vi bất thường do sampling rate.

---

## Cell 9 — Parameter sensitivity toàn dataset

So sánh:

```text
window_s = 3, 5, 10 s
threshold = 3.0, 3.5, 4.0
```

Với mỗi cấu hình tính:

* total artifact events;
* median artifact duration (%);
* số session có artifact;
* overlap với mask của cấu hình chính `5 s / 3.5`.

Ưu tiên dùng mask overlap, ví dụ Jaccard:

```text
intersection / union
```

Output:

| Window | Threshold | Events | Median artifact (%) | Sessions flagged | Mask overlap |
| -----: | --------: | -----: | ------------------: | ---------------: | -----------: |

Mục tiêu:

* kiểm tra detection không phụ thuộc quá mạnh vào lựa chọn tham số.

---

## Cell 10 — Segmentation impact

Với các window mục tiêu:

```text
60 / 120 / 180 / 240 / 300 s
```

Đếm số candidate analysis window sẽ bị reject nếu:

```text
artifact_mask[start:end].any() == True
```

Output:

| Window length | Candidate | Rejected by SQI | Retained | Retention (%) |
| ------------: | --------: | --------------: | -------: | ------------: |

Mục tiêu:

* đánh giá SQI có làm mất quá nhiều dữ liệu cho NTSA hay không.

---

## Cell 11 — Final SQI summary

Tạo bảng tóm tắt:

* artifact prevalence;
* Awake/Drowsy artifact burden;
* feature contribution;
* session outliers;
* parameter stability;
* expected segmentation retention.

## Ready-to-freeze criteria

SQI có thể freeze nếu:

* artifact visually tương ứng với waveform abnormality;
* artifact burden nhìn chung thấp và hợp lý;
* không có systematic Awake/Drowsy bias rõ ràng do detector;
* không có sampling-rate behavior bất thường;
* kết quả tương đối ổn định quanh `5 s / 3.5`;
* segmentation vẫn giữ đủ dữ liệu cho các window NTSA;
* detector chỉ flag/reject, không sửa hoặc nội suy tín hiệu.

Nếu đạt các tiêu chí trên:

```text
SQI = robust amplitude + roughness
window = 5 s
threshold = 3.5
→ ready to freeze
```

```
```
