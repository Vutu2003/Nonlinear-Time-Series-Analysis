````markdown
# Step 2A — Dataset-Wide Filter Evaluation Design

## 1. Goal

Đánh giá định lượng tác động của bộ lọc Butterworth zero-phase trên toàn bộ dataset trước khi freeze preprocessing parameters.

Filter đang test:

```text
Bandpass: 0.5–8 Hz
Order: 2
Zero-phase: filtfilt
````

Mỗi session phải dùng sampling rate được ước lượng riêng từ `Time (s)`.

---

## 2. Cell 1 — Load toàn bộ sessions

Thực hiện:

* đọc tất cả CSV bằng `load_session()`;
* lấy:

  * `Time (s)`;
  * `IR Value raw`;
  * `Label`;
* ước lượng `fs` từ median `dt`.

Hiển thị bảng:

| Session | Samples | Duration | Estimated fs |
| ------- | ------: | -------: | -----------: |

Mục tiêu: xác nhận input trước filtering.

---

## 3. Cell 2 — Apply filter toàn dataset

Với từng session:

```text
Raw PPG
→ optical inversion
→ zero-phase Butterworth bandpass
→ filtered PPG
```

Không thay đổi label hoặc time axis.

Kiểm tra:

* input/output có cùng số samples;
* không sinh NaN/Inf.

Hiển thị bảng lỗi nếu có.

---

## 4. Cell 3 — PSD metrics per session

Dùng Welch PSD cho tín hiệu trước và sau filter.

Tính cho từng session:

* in-band power: `0.5–8 Hz`;
* low-frequency power: `< 0.5 Hz`;
* high-frequency power: `> 8 Hz`;
* in-band retention;
* low-frequency ratio;
* high-frequency ratio.

Bảng kết quả:

| Session | In-band retention | Low-frequency ratio | High-frequency ratio |
| ------- | ----------------: | ------------------: | -------------------: |

---

## 5. Cell 4 — Dataset-level spectral summary

Tổng hợp các metric filter trên toàn dataset:

* median;
* IQR;
* min;
* max.

Hiển thị:

```text
In-band retention
Low-frequency suppression
High-frequency suppression
```

### Plot

Distribution plot cho ba metric trên.

Mục tiêu:

* xác định filter có hoạt động nhất quán giữa các session hay không;
* phát hiện session outlier.

---

## 6. Cell 5 — PSD before vs after

Chọn một số session đại diện:

* session 50 Hz;
* một session 25 Hz điển hình;
* session có spectral metric bất thường nhất nếu có.

Vẽ PSD before/after.

Mỗi plot cần đánh dấu:

```text
0.5 Hz
8 Hz
```

Mục tiêu: xác nhận trực quan kết quả định lượng.

---

## 7. Cell 6 — Peak-count consistency

Dùng cùng một diagnostic peak detector cho tín hiệu trước và sau filter.

Tính theo session:

* peaks before;
* peaks after;
* peak-count difference;
* peak-count change (%).

Bảng:

| Session | Peaks before | Peaks after | Change (%) |
| ------- | -----------: | ----------: | ---------: |

Lưu ý: peak detector này chỉ dùng để đánh giá filter, chưa phải detector chính thức cho PPI.

---

## 8. Cell 7 — Peak-timing consistency

Match peak trước và sau filter trong tolerance cố định.

Tính:

* matched peaks;
* match rate (%);
* median absolute timing shift (ms);
* maximum timing shift (ms).

Bảng:

| Session | Match rate | Median shift | Maximum shift |
| ------- | ---------: | -----------: | ------------: |

---

## 9. Cell 8 — Dataset-level peak summary

Tổng hợp:

* peak-count change;
* peak match rate;
* median timing shift.

Hiển thị:

* median;
* IQR;
* min;
* max.

### Plot

Tạo distribution plots cho:

```text
Peak-count change (%)
Peak match rate (%)
Median timing shift (ms)
```

Mục tiêu: xác định filter có làm thay đổi pulse detection một cách hệ thống hay không.

---

## 10. Cell 9 — Outlier identification

Xác định các session có:

* in-band retention thấp bất thường;
* high/low-frequency suppression khác biệt mạnh;
* peak-count change lớn;
* peak match rate thấp;
* timing shift lớn.

Hiển thị bảng các session cần kiểm tra thủ công.

Không tự động loại session ở bước này.

---

## 11. Cell 10 — Representative waveform inspection

Với các session:

* điển hình;
* spectral outlier;
* peak-consistency outlier;

chọn cùng một đoạn ngắn, ví dụ `10–30 s`.

Vẽ subplot `2 × 1`:

```text
Before filtering
After filtering
```

Có thể overlay detected peaks để kiểm tra:

* pulse morphology;
* peak preservation;
* ringing;
* extra local maxima.

---

## 12. Cell 11 — Sampling-rate comparison

So sánh filter metrics giữa:

```text
50 Hz session
vs
25 Hz sessions
```

Các metric:

* in-band retention;
* low/high-frequency ratio;
* peak-count change;
* peak match rate.

Mục tiêu: kiểm tra cùng filter parameters có hoạt động tương đương giữa các sampling rates hay không.

---

## 13. Cell 12 — Final filter summary

Tạo một bảng tổng hợp cuối cùng:

| Metric                   | Median | IQR | Min | Max |
| ------------------------ | -----: | --: | --: | --: |
| In-band retention        |        |     |     |     |
| Low-frequency ratio      |        |     |     |     |
| High-frequency ratio     |        |     |     |     |
| Peak-count change (%)    |        |     |     |     |
| Peak match rate (%)      |        |     |     |     |
| Median timing shift (ms) |        |     |     |     |

Kèm:

* số session không có lỗi filtering;
* số spectral outliers;
* số peak-consistency outliers.

---

## 14. Decision Criteria

Filter chưa được freeze chỉ dựa trên waveform đẹp.

Đánh giá cuối cùng phải xem đồng thời:

1. **Spectral preservation**

   * phần lớn năng lượng `0.5–8 Hz` được giữ.

2. **Out-of-band suppression**

   * baseline và high-frequency components giảm rõ.

3. **Peak preservation**

   * peak-count không thay đổi bất thường.

4. **Timing preservation**

   * matched peaks có timing shift nhỏ.

5. **Cross-session consistency**

   * hiệu ứng filter không phụ thuộc mạnh vào một vài session.

6. **Sampling-rate robustness**

   * filter hoạt động hợp lý ở cả `25 Hz` và `50 Hz`.

---

## 15. Expected Final Output

Notebook phải trả lời được:

> Bộ lọc `0.5–8 Hz`, Butterworth order 2, zero-phase có loại được thành phần ngoài dải trong khi vẫn bảo toàn waveform và timing của PPG một cách nhất quán trên toàn dataset hay không?

Nếu không, các tham số `lowcut`, `highcut` hoặc `order` phải được kiểm tra lại trước khi sang SQI và segmentation.

```
```
