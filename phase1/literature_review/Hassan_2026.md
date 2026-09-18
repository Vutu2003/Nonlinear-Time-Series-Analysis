# Hassan et al. (2026) — Key Notes

## Vai trò
Dùng cho **Introduction Paragraph 1–2**:
- significance của drowsiness
- taxonomy detection methods
- physiological/PPG monitoring
- current PPG-drowsiness paradigm
- labeling limitation

## Key claims

- Drowsiness là một **gradual physiological transition** từ wakefulness về phía sleep, không xuất hiện tức thời.
- Drowsiness khác fatigue về bản chất sinh lý, dù đều làm giảm vigilance/performance.
- Detection methods gồm:
  - subjective
  - vehicle-based
  - behavioral/vision-based
  - physiological
  - multimodal
- PPG được sử dụng khá nhiều, gồm:
  - wearable wrist PPG
  - steering wheel-mounted PPG
  - rPPG/IPPG
  - PPG-derived HR/HRV
- Xu hướng hiện tại chủ yếu là:

```text
PPG → physiological features / HRV → ML/DL → drowsiness detection/classification
````

* KSS thường được dùng để hỗ trợ labeling, nhưng drowsiness là quá trình liên tục trong khi label thường được rời rạc hóa thành `Alert/Drowsy` → có thể gây label uncertainty.

## PPG studies được review trích dẫn

| Tên nghiên cứu / Tác giảNămMô tả ngắn gọn phương pháp |      |                                                                                                                                                                                                                                     |
| ----------------------------------------------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kundinger và cộng sự**                              | 2020 | Thu tín hiệu PPG bằng vòng đeo tay Empatica E4 để trích xuất các đặc trưng biến thiên nhịp tim (HRV) miền thời gian/tần số; phân loại trạng thái tỉnh táo - buồn ngủ bằng các thuật toán ML truyền thống (KNN, Random Forest, SVM). |
| **Amidei và cộng sự**                                 | 2021 | Đánh giá thực nghiệm và kiểm chứng độ tin cậy của dữ liệu quang thể tích đồ (PPG) trong bài toán phát hiện trạng thái buồn ngủ của tài xế.                                                                                          |
| **Bi và cộng sự**                                     | 2023 | Sử dụng kỹ thuật Imaging PPG (IPPG/rPPG không tiếp xúc) trích xuất sóng xung huyết mạch từ video khuôn mặt, áp dụng tách nguồn mù (BSS) và lọc dải thông để tính chỉ số HRV (LF/HF, SD1/SD2) phân loại mệt mỏi.                     |
| **Cao và cộng sự (FDWatch)**                          | 2023 | Đeo cổ tay thu tín hiệu PPG bước sóng kép (trích xuất nhịp ngáp và HRV) kết hợp cảm biến gia tốc và nhịp sinh học; dùng mạng BPNN tính độ tin cậy và lý thuyết bằng chứng Dempster-Shafer để tổng hợp quyết định.                   |
| **Kong và cộng sự (RPPMT-CNN-BiLSTM)**                | 2024 | Tích hợp Remote PPG (rPPG qua camera hồng ngoại) trích xuất nhịp tim với đặc trưng thị giác PERCLOS; sử dụng chuỗi mô hình 1D-CNN và BiLSTM để học động lực học thời gian thực.                                                     |
| **Lu và cộng sự**                                     | 2024 | Dung hợp đa mô hình kết hợp tín hiệu sinh lý PPG với đặc trưng khuôn mặt và tư thế đầu, phân loại bằng mô hình học chuỗi LSTM.                                                                                                      |
| **Siyang và cộng sự**                                 | 2024 | Kết hợp tín hiệu rPPG trích xuất từ camera với các đặc trưng khuôn mặt trong các điều kiện chiếu sáng thay đổi, xử lý bằng mạng Bi-LSTM tích hợp hàm mất mát đa nhiệm (Multi-Loss).                                                 |
| **Tsai và cộng sự**                                   | 2024 | Thu trích xuất các chỉ số HRV (SDNN, RMSSD, nHF) từ PPG đeo cổ tay ở tài xế xe buýt thực tế; kết hợp mô hình trung bình động có trọng số động (DWMA) và mạng LSTM để dự đoán hành vi lái xe bất thường.                             |

## Main insight cho research gap

Current literature chủ yếu hỏi:

> Can PPG-derived features detect/classify drowsiness?

Nghiên cứu này hỏi:

> How do PPG dynamics reorganize from Awake to Drowsy?

## Claim boundary

Không dùng review này để claim:

* PPG trực tiếp đo sympathetic/vagal activity
* drowsiness làm thay đổi nonlinear dynamics
* nonlinear features tốt hơn conventional features

```

