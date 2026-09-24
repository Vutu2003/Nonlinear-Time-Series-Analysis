# Paper 11 — Vaussenat et al. (2026)
## Early Drowsiness Detection via HRV Derivative Analysis

## Method

- 25 participants, 49 driving-simulator sessions.
- Non-contact capacitive ECG từ seat backrest.
- RR intervals được dùng để tính:
  - conventional HRV metrics
  - first derivative `dRRI/dt`
  - second derivative `d²RRI/dt²`
- Features được tính trên **30 s windows, 50% overlap**.
- Ground truth classification dựa trên **crash proximity**, độc lập với HRV features.
- Drowsiness labels mô tả dựa trên behavioral indicators:
  - PERCLOS
  - yawning
  - blink
  - posture

---

## Main idea

Paper xem early drowsiness như một **dynamic transition**, không phải static physiological state.

```text
conventional HRV
→ autonomic state

HRV derivatives
→ transition dynamics
````

Trong đó:

```text
1st derivative
→ velocity / direction of cardiac change

2nd derivative
→ acceleration / transition onset
```

---

## Main findings

* HRV derivatives alone có discriminative power thấp:

  * 1st derivative AUC ≈ 0.549
  * 2nd derivative AUC ≈ 0.568
  * derivatives combined AUC ≈ 0.573
* Khi kết hợp với conventional HRV:

```text
AUC ≈ 0.863
```

→ derivatives chủ yếu cung cấp **complementary transition information**.

HRV-based detection xuất hiện:

```text
~5.8 min trước PERCLOS
~6.8 min trước crash
```

→ cardiac physiological changes có thể xuất hiện trước overt behavioral manifestations.

---

## Physiological interpretation

Authors diễn giải drowsiness onset như một gradual autonomic shift:

```text
sympathetic dominance
→ parasympathetic dominance
```

với:

```text
RRI ↑
HR ↓
RMSSD ↑
HF ↑
```

First derivative phản ánh hướng thay đổi của cardiac rhythm, còn second derivative được xem như marker của transition onset.

Tuy nhiên đây vẫn là **HRV-based physiological interpretation**, không phải direct measurement của sympathetic/vagal neural activity.

---

## Relevance to current study

Paper rất gần với current phenomenon:

```text
Alert / Awake
→ early Drowsiness transition
```

và support mạnh rằng:

> Drowsiness nên được xem như một **time-varying physiological transition**, không chỉ hai static classes.

Điều này phù hợp với current dataset:

```text
Awake ↔ Drowsy ↔ Awake ↔ Drowsy
```

và với việc dùng short windows để capture transition dynamics.

---

## Important contrast with current symbolic result

Vaussenat:

```text
Drowsiness
→ parasympathetic dominance ↑
→ sympathetic dominance ↓
```

Current symbolic analysis:

```text
0V ↑
2V ↓
```

theo Guzzetti / Porta framework:

```text
→ compatible with sympathetic modulation ↑
and/or vagal modulation ↓
```

Hai interpretations không hoàn toàn cùng chiều.

Điều này gợi ý rằng current Awake–Drowsy regime có thể không phải một simple monotonic sympathovagal shift, mà là một **unstable autonomic reorganization**.

---

## Short-window relevance

Paper dùng:

```text
30 s windows
50% overlap
```

để giữ temporal resolution của transition.

Authors cũng thừa nhận 30 s không đủ chuẩn cho reliable LF-HRV estimation.

→ support quan trọng rằng:

> short windows có thể cần thiết để capture transition dynamics, dù estimator reliability phải được cân bằng với temporal resolution.

---

## Discussion role

### Physiological foundation

Strong direct reference cho idea:

```text
early drowsiness
→ dynamic cardiovascular/autonomic transition
```

### Transition-based interpretation

Support việc current study tập trung vào **dynamical changes**, thay vì static feature differences.

### Short-window justification

Cung cấp precedent rằng short windows có thể phù hợp khi mục tiêu là capture onset / transition.

### Complementary-metrics principle

Derivatives alone không đủ mạnh nhưng bổ sung thông tin khi kết hợp với HRV.

Điều này phù hợp với current framework:

```text
Simplex
RQA
LLE
Symbolic RR
```

→ complementary views of the same transition.

### Claim boundary

Không nên dùng paper để claim:

```text
Drowsiness = parasympathetic dominance
Light drowsiness = N1
HRV derivative = direct ANS measurement
current study detects drowsiness earlier than behavior
```

---

## Main takeaway

> **Vaussenat et al. cung cấp direct support rằng early drowsiness là một dynamic autonomic/cardiovascular transition và rằng short-term cardiac changes có thể xuất hiện trước behavioral manifestations. Paper đặc biệt quan trọng để support transition-based physiological interpretation của current study, nhưng sympathovagal direction vẫn nên được xem là literature-based interpretation chứ không phải direct neural evidence.**

```

