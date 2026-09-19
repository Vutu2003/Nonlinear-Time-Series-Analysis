# El Sahmarany et al. (2026) — Key Notes

## Vai trò
Supporting review cho **Introduction P1–P2**; chủ yếu dùng để củng cố PPG/ECG literature và lần theo primary studies, không phải backbone chính về physiology. :contentReference[oaicite:0]{index=0}

## Key points
- PPG là phương pháp quang học không xâm lấn để đo pulse wave và blood-volume changes. :contentReference[oaicite:1]{index=1}
- Trong drowsiness monitoring, PPG đã được triển khai dưới nhiều dạng:
  - steering-wheel PPG
  - ear PPG
  - wearable PPG
- Các đặc trưng thường dùng gồm:
  - HR
  - HRV
  - PAT
  - blood-volume-related features
- PPG thường được dùng như một **supporting physiological modality**, do thay đổi có thể nhỏ và tín hiệu dễ bị ảnh hưởng bởi motion và ambient light. :contentReference[oaicite:2]{index=2}
- ECG/HR cũng được dùng phổ biến vì HR và HRV phản ánh thay đổi physiological state liên quan drowsiness. :contentReference[oaicite:3]{index=3}

## Studies đáng chú ý
- **[70] PAT + PPG + ECG**
  - ECG R-peaks + PPG peaks → PAT + HR.
  - Dùng để theo dõi thay đổi trong drowsiness.
  - Hữu ích cho claim rằng PPG-derived cardiovascular features có thể phản ánh drowsiness.

- **[71] ECG/PPG → RRI → Recurrence Plot → CNN**
  - RRI từ ECG và PPG → Bin-RP / Cont-RP / ReLU-RP → CNN.
  - Phân loại Awake/Drowsy.
  - **Rất liên quan:** recurrence được dùng như representation cho classification, không phải để phân tích RQA hay dynamical organization.

- **[69] Steering-wheel PPG**
  - PPG gắn trên vô-lăng.
  - Trích xuất HR và HRV.
  - Hữu ích cho practical motivation về PPG sensing.

- **[74] ECG-HRV drowsiness**
  - HRV features như LF/HF được dùng cho drowsiness classification.
  - Hữu ích để củng cố vai trò của cardiovascular/autonomic features.

- **[30] Early-stage drowsiness using heart-rate variation**
  - Dùng heart-rate variation để phát hiện drowsiness sớm.
  - Có thể hữu ích cho practical motivation về early monitoring.

## Insight cho research gap

Literature tiếp tục cho thấy pipeline phổ biến:

```text
PPG / ECG
→ HR / HRV / PAT / transformed features
→ ML / DL
→ drowsiness classification
````

Ngay cả recurrence plots cũng chủ yếu được dùng như **representation cho classifier**, thay vì để nghiên cứu trực tiếp cấu trúc động lực học của tín hiệu.

**Gap:** vẫn còn thiếu các nghiên cứu trả lời trực tiếp câu hỏi PPG dynamics thay đổi như thế nào khi trạng thái chuyển từ Awake sang Drowsy.

## Claim boundary

* Không dùng review này để claim PPG trực tiếp đo ANS.
* Không dùng để claim PPG độc lập đủ mạnh cho drowsiness detection.
* Review nhấn mạnh rõ limitations do motion, ambient light và mức thay đổi nhỏ của PPG. 

## Primary papers nên follow-up

Ưu tiên đọc theo thứ tự:

```text
[71] → [70] → [69] → [74] → [30]
```

Trong đó **[71] quan trọng nhất** vì gần trực tiếp với hướng recurrence + PPG + drowsiness của nghiên cứu hiện tại.

```

