# Paper 5 — Rolink et al. (2015)
## Recurrence Quantification Analysis Across Sleep Stages

## Method

- Dataset lớn: **313 healthy subjects**, >2300 h PSG.
- So sánh **Wake, NREM, REM**.
- Áp dụng RQA trên:
  - ECG
  - respiratory effort
  - heart rate
  - cross-RQA giữa các signals
- Các metrics chính gồm:
  - REC
  - DET
  - L / Lmax
  - ENTR
  - LAM
  - TT
  - recurrence-time metrics

RQA parameters:
- `m = 4`
- delay theo mutual information
- threshold `ε` subject-specific để `REC ≈ 10%`

---

## Main findings

- RQA features có thể phân biệt **Wake vs Sleep**, đặc biệt tốt với cardiac và respiratory signals.
- Trong **NREM**, cardiac và respiratory dynamics nhìn chung **regular hơn**.
- Các differences được phản ánh bởi các metrics như:
  - DET
  - LAM
  - ENTR
  - recurrence times
- REM thường gần Wake hoặc NREM tùy feature, nên discrimination kém hơn.

---

## Physiological interpretation

Paper support rằng:

> Sleep-state changes đi kèm **reorganization of cardio-respiratory dynamics**.

Đặc biệt:

```text
NREM
→ more regular cardiac / respiratory activity
→ altered recurrence structure
````

Tuy nhiên paper không map trực tiếp:

```text
DET / LAM / TT
→ sympathetic / parasympathetic activity
```

---

## Relevance to current study

Rất gần với phần RQA của nghiên cứu hiện tại:

```text
Rolink:
cardiac waveform / HR
→ RQA
→ recurrence differences across Wake / Sleep

Current study:
PPG waveform
→ RQA
→ recurrence differences across Awake / Drowsy
```

Điểm quan trọng:

* Rolink support mạnh rằng **recurrence organization is state-dependent**.
* Nhưng họ gộp `N1 + N2 + N3 = NREM`.

Do đó:

```text
Rolink NREM
≠ current Drowsiness
```

Current dataset gần với:

```text
Awake ↔ Drowsiness
```

hơn là:

```text
Wake → stable NREM
```

---

## Relation to current RQA findings

Current study:

```text
DET ↓
LAM ↑ tendency
TT ↑ tendency
```

Có thể diễn giải như:

```text
less diagonal recurrence organization
+
greater local / laminar persistence
```

Rolink giúp support ý nghĩa của các recurrence structures này, nhưng **không trực tiếp giải thích direction** của drowsiness.

---

## Discussion role

### RQ2 — RQA

Đây là một reference quan trọng để support:

> Sleep-related physiological states are associated with measurable changes in cardiovascular recurrence organization.

### Claim boundary

Không nên dùng paper này để claim:

```text
Drowsiness = NREM
DET ↓ = less physiological determinism
LAM / TT ↑ = specific ANS shift
```

---

## Main takeaway

> **Rolink et al. cung cấp direct evidence rằng recurrence structure của cardio-respiratory dynamics thay đổi theo sleep/wake state. Paper rất quan trọng cho physiological relevance của RQA, nhưng không giải thích trực tiếp direction của DET/LAM/TT trong unstable Awake–Drowsy transition.**

```
