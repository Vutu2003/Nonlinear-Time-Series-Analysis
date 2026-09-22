# Paper 7 — Calderón-Juárez et al. (2023)
## Revisiting nonlinearity of heart rate variability in healthy aging

## Method

- Dataset lớn: **1026 healthy subjects**, 18–92 tuổi.
- Phân tích **5-min HRV từ ECG**.
- Dùng RQA:
  - `DET`
  - `LAM`
- Kết hợp **surrogate data testing** bằng wavelet-based surrogates để kiểm tra nonlinear information.
- RQA dùng:
  - FAN với recurrence density cố định 7%
  - delay từ mutual information
  - embedding dimension từ FNN

### Statistics

- mean ± SD
- ANOVA + Bonferroni
- logistic regression
- OR + **95% CI**

→ philosophy thống kê khá gần nghiên cứu hiện tại ở điểm:
`effect/direction + uncertainty + multiple-comparison control`

---

## Main findings

- Tỷ lệ HRV series được xác định là nonlinear giảm theo tuổi.
- BMI và HR cao hơn liên quan đến khả năng xuất hiện nonlinear information thấp hơn.
- Female sex liên quan đến tỷ lệ nonlinear HRV cao hơn.
- DET và LAM thay đổi theo age/sex, nhưng metric value không được xem là proof trực tiếp của complexity loss.

---

## Physiological interpretation

Nonlinear HRV được xem là kết quả của tương tác liên tục giữa:

```text
sympathetic
parasympathetic
neuroendocrine system
intrinsic cardiac nervous system
central control pathways
````

→ nonlinear organization có thể phản ánh **multisystem cardiovascular regulation**.

Authors cũng nhấn mạnh rằng cơ chế sinh học cụ thể phía sau các nonlinear changes vẫn chưa thể xác định trực tiếp.

---

## Relevance to current study

Paper rất quan trọng để tách:

```text
RQA metric value
≠
proof of nonlinearity
```

và:

```text
surrogate testing
→ evidence for nonlinear information

DET / LAM comparison
→ description of recurrence organization
```

Điều này phù hợp trực tiếp với:

```text
RQ1:
PPS surrogate rejection

RQ2:
DET / LAM changes
```

---

## Relation to current findings

Current study:

```text
DET ↓
LAM ↑ tendency
```

Paper này giúp giữ claim boundary:

```text
DET ↓
≠ less complexity
≠ less determinism
≠ less chaos

LAM ↑
≠ more/less nonlinear
```

RQA metrics nên được diễn giải như **changes in recurrence geometry**, không phải scalar measure của toàn bộ system complexity.

---

## Discussion role

### RQ1

Strong support cho việc dùng **surrogate testing** để kiểm tra nonlinear organization.

### RQ2

Support việc xem `DET` và `LAM` như các descriptive dynamical properties khác nhau.

### Physiological foundation

Support rằng nonlinear cardiovascular dynamics có thể sinh ra từ **interacting regulatory systems**.

### Statistical reporting

Supporting precedent cho:

* confidence intervals
* effect-oriented reporting
* multiple-comparison correction

Nhưng không phải direct justification cho bootstrap median CI của nghiên cứu hiện tại.

---

## Main takeaway

> **Calderón-Juárez et al. củng cố distinction giữa nonlinearity testing và RQA metric interpretation: surrogate testing dùng để xác nhận nonlinear information, còn DET/LAM chỉ mô tả các khía cạnh khác nhau của recurrence organization. Đây là reference rất mạnh cho claim boundaries của nghiên cứu hiện tại.**

```
