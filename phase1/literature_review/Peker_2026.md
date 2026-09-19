# Peker et al. (2026) — Key Notes

## Vai trò
Introduction P1–P2; hỗ trợ P4.

## Key claims
- Drowsiness đi kèm thay đổi ANS, với xu hướng tăng parasympathetic influence và giảm sympathetic effectiveness.
- HR/HRV phản ánh autonomic state và mức alertness.
- PPG đo blood-volume changes và có thể cung cấp thông tin liên quan đến ANS.
- Mối liên hệ trực tiếp giữa blood-volume changes và drowsiness vẫn chưa được xác lập đầy đủ.
- ECG/PPG cũng có thể gián tiếp phản ánh respiration.
- Các nghiên cứu physiological drowsiness dùng window rất đa dạng: 2 s, 30 s, 1 min, 2 min, 5 min.

## Studies liên quan
- **Awais et al. [39]:** ECG HRV (LF, HF, LF/HF) + EEG → SVM.
- **Fujiwara et al. [49]:** ECG HRV; 30-s epochs; phát hiện pre-N1.
- **Lee et al. [134]:** wearable ECG + PPG → RRI → recurrence plots → CNN.
  - Quan trọng: recurrence được dùng như representation cho classification, không phải để phân tích dynamics/RQA.
- **Huang & Deng [135]:** PPG + EDA + respiration; 2-s slices → PCA + ANN.

## Gap liên quan nghiên cứu

Phần lớn các nghiên cứu physiological hiện nay đi theo hướng:

```text
ECG / PPG
→ HR / HRV / statistical or transformed features
→ ML / DL
→ drowsiness classification
````

Ngay cả recurrence plot cũng chủ yếu được dùng như đầu vào cho classifier.

**Khoảng trống:** vẫn chưa rõ các đặc tính động lực học phi tuyến nội tại của PPG thay đổi như thế nào khi trạng thái chuyển từ Awake sang Drowsy.

## Claim boundary

Không suy diễn trực tiếp:

```text
PPG → sympathetic / parasympathetic activity
```

Review cũng thừa nhận mối liên hệ trực tiếp giữa blood-volume changes và drowsiness vẫn cần được nghiên cứu thêm.

```

