# Report Slide Story — Version 0

## Slide 1 — Scientific Problem

**Drowsiness as a transition in ultra-short PPG dynamics**

* PPG thường được dùng để extract features cho classification.
* Nghiên cứu này hỏi một câu khác:

  > **PPG dynamics thay đổi như thế nào khi trạng thái chuyển từ Awake sang Drowsy?**

**Takeaway:** Drowsiness được xem như một **physiological dynamical transition**, không chỉ là classification label.

---

## Slide 2 — Core Literature Progression

### Sviridova 2015

PPG chứa structured nonlinear dynamical organization.

### Sviridova 2018

PPG gần periodic → cần PPS để kiểm tra liệu observed dynamics có chỉ là noisy pseudoperiodicity.

### Sviridova 2022

Dynamical characteristics có thể được nghiên cứu từ finite/short recordings, nhưng phụ thuộc metric.

```text
Nature of dynamics
        ↓
Appropriate null model
        ↓
Temporal feasibility
```

**Takeaway:** Prior work establishes the foundation for studying PPG as a nonlinear dynamical system.

---

## Slide 3 — Research Gap

Prior work chủ yếu hỏi:

> **PPG dynamics là gì?**

Câu hỏi còn thiếu:

```text
Awake ─────────→ Drowsy
        ?

How does the dynamical regime change?
```

**Gap:** State-dependent reorganization của PPG dynamics trong drowsiness vẫn chưa được characterize đầy đủ.

---

## Slide 4 — Conceptual Shift

### Conventional view

```text
PPG
↓
features
↓
classifier
↓
Awake / Drowsy
```

### This study

```text
Awake dynamical regime
↓
physiological transition
↓
Drowsy dynamical regime
```

**Takeaway:**
**From state classification to state-dependent dynamical reorganization.**

---

## Slide 5 — Research Questions

### RQ1 — Dynamical foundation

> Does ultra-short PPG exhibit dynamical organization beyond a noisy pseudoperiodic process?

### RQ2 — State transition

> How does drowsiness reorganize this validated dynamical regime?

Logic:

```text
Establish nontrivial dynamics
        ↓
Study state-dependent modulation
```

---

## Slide 6 — Analytical Framework

```text
PPG windows
    ↓
State-space reconstruction
    ↓
Prediction → forecastability
RQA        → recurrence organization
LLE        → local divergence
    ↓
PPS validation
    ↓
Awake vs Drowsy
    ↓
Window-size robustness
```

Symbolic dynamics:
→ complementary physiological interpretation.

**Takeaway:** Prediction, RQA and LLE are complementary views of the **same dynamical transition**.

---

## Slide 7 — Why PPS?

PPG is strongly oscillatory.

```text
Structured waveform
≠
proof of meaningful nonlinear organization
```

A noisy pseudoperiodic process can also appear highly structured.

**Question:**

> Does observed PPG organization exceed what a noisy pseudoperiodic process can reproduce?

---

## Slide 8 — RQ1 Result

Original PPG vs PPS:

```text
Prediction
CC ↑
NRMSE ↓
→ forecastability ↑

Recurrence
DET ↑
Lmean ↑
→ diagonal organization ↑

Local divergence
LLE ↑
→ trajectory divergence ↑

LAM / TT ↓
→ laminar trapping ↓
```

Pattern is highly coherent across Awake, Drowsy and sessions.

**Takeaway:**

> Both states contain dynamical organization beyond the tested noisy pseudoperiodic null.

---

## Slide 9 — RQ2 Main Finding

### Drowsiness

```text
CC ↓
NRMSE ↑
→ forecastability ↓

DET ↓
→ diagonal recurrence organization ↓

LLE ↓
→ local trajectory divergence ↓
```

Supportive tendencies:

```text
Lmean ↓
LAM ↑
TT ↑
→ possible increased laminarity
```

**Takeaway:**

> **Drowsiness systematically reorganizes short-window PPG dynamics.**

---

## Slide 10 — What Kind of Dynamical Transition?

Observed simultaneously:

```text
forecastability ↓
local divergence ↓
diagonal organization ↓
laminarity ↑ tendency
```

Therefore the result should **not** be reduced to:

```text
more chaos ↔ less chaos
```

Preferred interpretation:

> **Drowsiness produces a different dynamical organization: less locally divergent, less predictably organized and with weaker diagonal recurrence structure.**

**Keyword:**

### Dynamical reorganization

---

## Slide 11 — Why 60 Seconds Matters

Primary scale:

```text
60 s
```

Robustness:

```text
60 s → 120 s → 180 s
```

Main effects retain the same direction across window sizes.

**Takeaway:**

> The Awake–Drowsy dynamical transition is already observable at the 60-s scale and is not critically dependent on window length.

---

## Slide 12 — Inter-session Heterogeneity

Most sessions follow the population direction, but several show coordinated reverse responses.

Important:

* no clear common QC failure,
* removing strongest reverse sessions makes effects stronger,
* they do not generate the population result.

**Takeaway:**

> **Heterogeneity attenuates the group effect rather than creating it.**

Possible interpretation:
→ individual physiological/state-response heterogeneity.

---

## Slide 13 — Physiological Interpretation

Symbolic pattern:

```text
0V ↑
2V ↓
1V ~ unchanged
```

Evidence weaker than main nonlinear findings.

Interpretation:

> Directionally compatible with altered autonomic cardiovascular modulation during drowsiness.

**Role:** supporting physiological interpretation, not primary evidence.

---

## Slide 14 — Main Contributions

### Scientific

Drowsiness is investigated as a transition between PPG dynamical regimes.

### Integrative

Prediction + recurrence + local divergence characterize the transition coherently.

### Temporal

The reorganization is observable in very short 60-s windows and remains robust at 120–180 s.

### Methodological foundation

The compared dynamics are first challenged against a noisy pseudoperiodic null.

**Novelty is not a new nonlinear metric.**

> **Novelty lies in characterizing physiological-state-dependent reorganization of PPG dynamics.**

---

## Slide 15 — Final Story

```text
Prior work
↓
PPG contains nonlinear dynamics
↓
requires pseudoperiodic null testing
↓
can be studied from finite recordings
↓
OPEN QUESTION
↓
What happens during Awake → Drowsy?
↓
RQ1: dynamics exceed PPS
↓
RQ2: Drowsiness
    forecastability ↓
    diagonal organization ↓
    local divergence ↓
    laminarity ↑ tendency
↓
robust from 60–180 s
↓
state-dependent dynamical reorganization
```

### Final message

> **Drowsiness is associated not merely with changes in isolated PPG features, but with a reproducible reorganization of short-window PPG dynamics across forecastability, recurrence organization and local trajectory divergence.**
