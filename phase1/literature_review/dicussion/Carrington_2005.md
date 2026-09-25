# Paper 13 — Carrington et al. (2005)
## Thay đổi chức năng tim mạch trong giai đoạn sleep onset ở người trẻ

## Phương pháp

- 21 healthy young adults.
- Theo dõi từ **1 giờ trước lights out** đến hết first NREM period.
- Đo liên tục:
  - ECG / HR
  - systolic BP / diastolic BP
  - baroreflex activity
  - EEG / EOG / EMG để xác định sleep-wake state
- Sleep onset được chia thành 5 phase:

```text
Phase 1
→ relaxed presleep wakefulness

Phase 2
→ lights out → trước Stage 1

Phase 3
→ Stage 1 + repeated arousals

Phase 4
→ Stage 1/2 + repeated arousals

Phase 5
→ stable NREM after last arousal
```

Phases 3–4 được xem là giai đoạn **sleep–wake state instability**.

---

## Kết quả chính

Từ wakefulness đến stable sleep:

```text
SBP ↓ ~12 mmHg
DBP ↓ ~7 mmHg
HR ↓ ~6.6 bpm
```

Nhưng quá trình giảm **không monotonic**.

Đặc biệt:

```text
after lights out
→ BP / HR bắt đầu giảm

during unstable Stage 1–2 with arousals
→ decline bị chậm / gián đoạn

stable sleep
→ BP / HR tiếp tục giảm và ổn định
```

---

## Vai trò của arousal

Có 435 spontaneous arousals trong phases 3–4.

Mỗi arousal gây:

```text
BP ↑ transiently
HR ↑ transiently
```

và peak response có thể quay gần về mức wakefulness.

Quan trọng hơn:

> repeated arousals không chỉ tạo transient spikes mà còn **retard underlying cardiovascular decline** trong quá trình sleep onset.

Số arousals nhiều hơn liên quan đến:
- sleep onset latency dài hơn
- BP / HR giảm ít hơn
- tốc độ giảm BP / HR chậm hơn

---

## Physiological interpretation

Paper cho thấy sleep onset là một **multi-phase cardiovascular transition**, không phải sự chuyển trạng thái tức thời.

Pattern tổng thể:

```text
wake-like cardiovascular regulation
↓
initial decline after lights out
↓
unstable sleep-onset period with repeated arousals
↕
temporary cardiovascular reactivation
↓
stable sleep
→ lower BP / HR
```

Tác giả cũng thấy baroreflex activity nhìn chung không giảm trong khi BP và HR giảm.

Do đó họ hypothesize rằng quá trình sleep onset có thể liên quan đến:

> **downward resetting of cardiovascular/baroreflex regulation**

hơn là đơn giản loss of regulatory sensitivity.

Cơ chế cụ thể của baroreflex resetting vẫn chưa được chứng minh trực tiếp.

---

## Điểm đặc biệt quan trọng

Cardiovascular changes bắt đầu:

```text
sau lights out
nhưng
trước EEG-defined Stage 1 sleep
```

Do đó:

> physiological transition có thể bắt đầu trước formal electrophysiological sleep onset.

Điều này củng cố việc không nên đồng nhất:

```text
physiological drowsiness transition
=
PSG-defined N1
```

---

## Liên quan đến nghiên cứu hiện tại

Current dataset:

```text
Awake ↔ Drowsy ↔ Awake ↔ Drowsy
```

Carrington cho thấy sleep-onset period cũng có:

```text
sleep-driving processes
↔ repeated arousals
↔ wake-like cardiovascular reactivation
```

Do đó rất phù hợp với cách xem Drowsiness như một:

> **unstable regulatory regime**

thay vì một static sleep state.

---

## Liên hệ với current NTSA findings

Paper không trực tiếp đo:

```text
CC / NRMSE
DET / LAM / TT
LLE
```

nhưng cung cấp physiological mechanism hợp lý cho:

```text
unstable cardiovascular regulation
+
repeated arousal-driven perturbations
→ less stable short-term trajectory evolution
```

Điều này có thể tạo physiological context cho:

```text
CC ↓
NRMSE ↑
```

tức **reduced finite-horizon forecastability**.

Đây vẫn là inference của current study, không phải direct finding của Carrington.

---

## Liên hệ với Symbolic Analysis

Overall sleep-onset trajectory trong paper hướng tới:

```text
HR ↓
BP ↓
stable sleep physiology
```

nhưng repeated arousals tạo:

```text
HR ↑ transiently
BP ↑ transiently
```

Do đó early sleep onset có thể chứa **mixed autonomic influences**, thay vì một simple monotonic sympathovagal shift.

Điều này giúp contextualize current pattern:

```text
0V ↑
2V ↓
```

mà không cần ép nó phải giống hoàn toàn established stable-sleep physiology.

---

## Liên hệ với Shinar et al. (2006)

```text
Shinar
→ wake–sleep transition có vigilance fluctuations

Carrington
→ arousals trong transition làm thay đổi cardiovascular trajectory
```

Hai paper bổ sung nhau rất tốt:

> **State instability không chỉ tồn tại về EEG/vigilance mà còn có measurable cardiovascular consequences.**

---

## Role in Discussion

### Physiological backbone

Strong reference cho việc:

> **sleep onset là một multi-phase physiological transition.**

### Unstable transition

Support trực tiếp rằng:

```text
Stage 1 / early Stage 2
+ repeated arousals
→ unstable cardiovascular regulation
```

### Prediction interpretation

Cung cấp physiological rationale cho hypothesis rằng unstable transition có thể làm **finite-horizon predictability giảm**.

### ANS / cardiovascular interpretation

Support cách diễn giải drowsiness như:

> **reorganization of cardiovascular control**

thay vì chỉ:

```text
sympathetic ↓
parasympathetic ↑
```

### Claim boundary

Không nên suy ra:

```text
Drowsiness = Stage 1 / Stage 2
arousal directly explains CC↓ / NRMSE↑
baroreflex resetting đã được chứng minh hoàn toàn
current PPG metrics trực tiếp đo autonomic activity
```

---

## Main takeaway

> **Carrington et al. cho thấy sleep onset là một quá trình tim mạch đa phase, trong đó BP và HR không giảm một cách monotonic mà bị gián đoạn bởi repeated arousals. Những arousals này tạo transient wake-like cardiovascular reactivation và làm chậm quá trình settling vào stable sleep. Paper cung cấp strong physiological support cho việc xem Awake–Drowsy trong nghiên cứu hiện tại như một unstable regulatory transition và tạo mechanistic context hợp lý cho reduced short-term forecastability.**
