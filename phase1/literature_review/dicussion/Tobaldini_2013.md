# Paper 2 — Tobaldini et al. (2013)

## Physiological Foundation

- Wake → sleep là một **complex physiological transition** có sự tham gia của nhiều cơ chế điều hòa:
  - sympathetic / parasympathetic modulation
  - baroreflex / chemoreflex
  - respiration
  - central oscillators
  - hormonal regulation

- Trong **drowsiness / sleep onset**:
  - alpha rhythm giảm
  - theta rhythm bắt đầu xuất hiện
  - autonomic cardiovascular regulation bắt đầu thay đổi

- Cardiovascular dynamics vì vậy được tạo bởi nhiều interacting control mechanisms ở nhiều time scales.

> Điều này cung cấp physiological foundation rằng PPG dynamics có thể chứa cấu trúc phức tạp hơn một simple periodic / pseudoperiodic process.

---

## Relevance to current study

Dataset hiện tại phù hợp hơn với:

```text
Awake ↔ Drowsiness ↔ Awake ↔ Drowsiness
````

hơn là:

```text
Awake → N1 → N2 → N3
```

Do đó drowsiness nên được xem như một **unstable transitional regime near sleep onset**, không phải established NREM sleep.

Các findings của NREM như:

```text
HR ↓
BP ↓
MSNA ↓
parasympathetic modulation ↑
```

chỉ nên dùng như **broader physiological context**, không phải direct evidence cho drowsiness trong dataset.

---

## Role in Discussion

### RQ1 — Null test

Paper này hỗ trợ khá tốt:

> Cardiovascular dynamics được hình thành bởi nhiều interacting regulatory mechanisms, nên việc observed PPG dynamics vượt quá một noisy pseudoperiodic null có physiological plausibility.

### RQ2 — Awake vs Drowsy

Paper chỉ hỗ trợ ở mức high-level:

> Awake → Drowsy có thể liên quan đến reorganization của autonomic cardiovascular control trong wake-to-sleep transition.

Nhưng chưa giải thích trực tiếp direction của:

```text
CC ↓
NRMSE ↑
DET ↓
LLE ↓
LAM / TT ↑ tendency
```

→ cần metric-specific literature.

---

## Claim boundary

Không nên suy ra trực tiếp:

```text
Drowsiness = NREM
Drowsiness = N1
PPG metric change = sympathetic/vagal change
```

Cách diễn giải phù hợp hơn:

> Drowsiness represents a transitional physiological regime near sleep onset, in which cardiovascular autonomic regulation is being reorganized.




