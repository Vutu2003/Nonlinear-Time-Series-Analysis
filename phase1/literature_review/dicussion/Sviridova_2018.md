# Paper 10 — Sviridova et al. (2022)
## Photoplethysmogram Recording Length: Defining Minimal Length Requirement from Dynamical Characteristics

## Method

- Phân tích trực tiếp **NIR PPG waveform** ở healthy subjects.
- 30 recordings, mỗi recording 5 phút, sampling rate `409.6 Hz`.
- Dùng **time-delay reconstruction + RQA**.
- Parameters:
  - `m = 4`
  - `τ`: khi autocorrelation giảm dưới `1/e`
  - `ε = 10%` kích thước reconstructed attractor
- RQA metrics:
  - `DET`
  - `Lmax`
  - `L`
  - `ENTR`
- Đánh giá estimation error khi giảm recording length.
- Kiểm tra thêm trên noisy Rössler system và PPG đã subsample.

---

## Main findings

Khả năng estimate RQA phụ thuộc mạnh vào từng metric.

Với PPG, để error < 1%:

```text
DET   ≈ 2.4 s
ENTR  ≈ 17 s
L     ≈ 105 s
Lmax  ≈ 120 s
````

→ `DET` rất robust với short recordings.

→ các diagonal-length metrics như `L` và đặc biệt `Lmax` cần data dài hơn nhiều.

Sampling-rate reduction từ `409.6 → 204.8 → 102.4 Hz` chỉ làm thay đổi nhỏ minimum-length estimates trong dataset này.

---

## Relevance to current study

Đây là một trong những paper gần nhất về:

```text
PPG waveform
+
phase-space reconstruction
+
RQA
+
short recording length
```

Current study sử dụng:

```text
30 / 60 / 120 / 180 s windows
```

Do đó paper support mạnh rằng **short-window PPG RQA là khả thi**, nhưng độ ổn định phụ thuộc metric.

Đặc biệt:

```text
DET
→ expected to be relatively robust even for short windows

L / diagonal-length measures
→ more sensitive to window length
```

Điều này phù hợp với current findings:

```text
DET ↓
→ stable across window durations

Lmean ↓
→ weaker / less statistically stable
```

---

## Methodological relevance

Paper nhấn mạnh:

> recording length là một parameter quan trọng của nonlinear time-series analysis.

Do đó hỗ trợ trực tiếp việc current study:

* kiểm tra `30 / 60 / 120 / 180 s`
* chọn `60 s` như practical compromise
* không giả định tất cả NTSA metrics có cùng minimum data requirement

Paper cũng cảnh báo rằng **filtering có thể thay đổi nonlinear dynamical characteristics của PPG**, nên preprocessing cần được kiểm soát và giữ nhất quán.

---

## Physiological / dynamical interpretation

Paper chủ yếu là methodological, không nghiên cứu Awake–Drowsy physiology.

Nó support rằng PPG waveform chứa measurable dynamical structure có thể được đặc trưng bằng phase-space / recurrence analysis.

Tuy nhiên authors dùng các claim khá mạnh như:

```text
PPG dynamics → deterministic chaos
DET > 0.9 → sign of determinism
1/Lmax → trajectory divergence
```

Các claim này không nên transfer trực tiếp vào current manuscript.

Current study nên giữ interpretation thận trọng hơn:

```text
DET
→ diagonal recurrence organization

L
→ average diagonal persistence

LLE
→ local trajectory divergence

surrogate testing
→ evidence relative to a specified null
```

---

## Role in Discussion

### Short-window justification

Strong reference cho việc **ultra-short PPG dynamics có thể được estimated bằng RQA**, đặc biệt với `DET`.

### Window-length robustness

Rất relevant để giải thích vì sao:

```text
DET
→ stable across short windows

Lmean
→ potentially more duration-sensitive
```

### Methodological precedent

Một trong các nghiên cứu gần nhất sử dụng:

```text
raw PPG waveform → reconstructed dynamics → RQA
```

### Claim boundary

Không dùng paper để claim:

```text
PPG is definitively chaotic
DET > 0.9 proves physical determinism
60 s is universally sufficient for every NTSA metric
```

Kết quả của họ áp dụng cho specific NIR PPG, acquisition setting và RQA parameterization.

---

## Main takeaway

> **Sviridova et al. cung cấp strong methodological support cho việc phân tích nonlinear dynamics trên short PPG waveform. Quan trọng nhất, paper cho thấy minimum recording length phụ thuộc mạnh vào từng dynamical metric: DET ổn định rất sớm, trong khi diagonal-length measures cần recordings dài hơn đáng kể.**

```

