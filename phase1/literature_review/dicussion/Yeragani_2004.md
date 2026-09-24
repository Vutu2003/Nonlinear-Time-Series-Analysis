# Paper 8 — Yeragani et al. (2004)
## LLE of heart-rate dynamics across frequency bands

## Method

- Phân tích **HR / RR dynamics từ ECG**.
- So sánh:
  - Awake vs Sleep
  - Supine vs Standing
  - Healthy controls vs Panic disorder
- Tính:
  - Minimum Embedding Dimension (MED)
  - Largest Lyapunov Exponent (LLE)
- Dùng **Rosenstein algorithm** để ước lượng LLE.
- Tách HR time series thành:
  - VLF: < 0.04 Hz
  - LF: 0.04–0.15 Hz
  - HF: 0.15–0.5 Hz
- Sau đó tính LLE riêng cho từng band.

---

## Main findings

Ở healthy controls:

```text
Sleep:
UF-LLE ↑
HF-LLE ↑

Standing:
LF-LLE ↑
HF-LLE ↓
````

→ LLE thay đổi theo physiological state và frequency content.

Paper cũng cho thấy:

* LLE phụ thuộc vào **sampling rate**
* data length ảnh hưởng estimation
* preprocessing/filtering có thể ảnh hưởng nonlinear measures

---

## Physiological interpretation

Authors đề xuất:

```text
HF-LLE
→ có thể liên quan vagal modulation

LF-LLE / HF-LLE
→ có thể phản ánh relative sympathovagal interaction
```

Tuy nhiên chính authors nhấn mạnh rằng các mapping này vẫn cần **physiological/pharmacological validation**.

Do đó không nên hiểu:

```text
LLE ↑/↓
→ direct sympathetic/vagal ↑/↓
```

---

## Relevance to current study

Current study:

```text
PPG waveform
→ bandpass 0.5–8 Hz
→ Rosenstein LLE
```

Yeragani:

```text
HR/HRV
→ VLF/LF/HF decomposition
→ band-specific LLE
```

Hai loại frequency band **không tương đương**.

Vì vậy LLE hiện tại nên được diễn giải là:

> **local divergence of PPG waveform dynamics**

không phải direct autonomic-band LLE.

---

## Relation to current finding

Current study:

```text
Drowsy → LLE ↓
```

Yeragani:

```text
Sleep → LLE ↑
```

→ cho thấy LLE direction phụ thuộc physiological context.

Điều này support rằng:

> Drowsiness không nên được đồng nhất với established sleep.

---

## Role in Discussion

### LLE interpretation

Strong reference để support:

```text
LLE
→ local trajectory divergence / sensitivity to nearby states
```

### Physiological sensitivity

Cho thấy LLE thay đổi theo sleep/posture/autonomic perturbation.

### Claim boundary

Không nên suy:

```text
LLE ↓ = less chaos
LLE ↓ = parasympathetic ↑
LLE ↓ = sympathetic ↓
```

### Robustness

Hữu ích để support việc:

* giữ sampling rate nhất quán
* kiểm tra data-length dependence
* thận trọng với preprocessing/filtering

---

## Main takeaway

> **Yeragani et al. cho thấy LLE của cardiovascular dynamics nhạy với physiological state, nhưng direction và physiological meaning phụ thuộc mạnh vào signal representation, frequency content và autonomic context. Vì vậy LLE trong nghiên cứu hiện tại nên được diễn giải như local trajectory divergence, không phải direct marker của sympathetic/vagal activity hay chaos.**

```
