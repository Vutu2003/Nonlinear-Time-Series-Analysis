# Paper 6 — Martín-González et al. (2018)
## RQA for sleep-apnea characterization

## Method

- Phân tích **RR intervals / HRV từ single-lead ECG** trên 2 databases.
- Dùng **RQA** để phân biệt apnea vs non-apnea.
- Sweep đồng thời các RQA parameters:
  - embedding dimension
  - delay
  - recurrence threshold
- So sánh:
  - Fixed Distance
  - FAN (Fixed Amount of Nearest Neighbours)
- Các RQA metrics gồm:
  - DET, L, Lmax, ENTR
  - LAM, TT, Vmax
  - recurrence-time features
  - network-based features

### Parameter finding

Kết quả tốt nhất chủ yếu quanh:

```text
m ≈ 7–8
delay ≈ 4–5
FAN ≈ 5%
````

→ nhấn mạnh rằng **RQA results phụ thuộc mạnh vào parameter selection**.

---

## Main findings

Trong apnea:

```text
LAM ↑
Vmax ↑
DET ↑
Lmax ↑
```

→ recurrence structure trở nên:

```text
more regular
more predictable
more laminar
less complex
```

Vertical và diagonal structures đều chứa information quan trọng.

---

## Physiological interpretation

* Cardiovascular dynamics chịu ảnh hưởng của nhiều interacting mechanisms:

  * ANS
  * respiration
  * baroreflex
  * cardiorespiratory coupling
* Trong apnea, control system được diễn giải là **simplified / more regular**, với nhiều recurrence và laminar states hơn.
* Authors liên hệ điều này với altered autonomic regulation và impaired baroreflex.

Quan trọng:

> RQA metrics không nên được xem như direct measurement của sympathetic / parasympathetic activity.

---

## Relevance to current study

Rất quan trọng cho việc diễn giải:

```text
DET ↓
LAM ↑ tendency
TT ↑ tendency
```

### RQA geometry

```text
DET ↓
→ reduced diagonal recurrence organization

LAM / TT ↑
→ greater local persistence / laminar behavior
```

Hai nhóm metrics phản ánh **different dynamical properties**, nên không cần thay đổi cùng chiều.

Current pattern:

```text
less diagonal organization
+
greater laminar persistence
```

→ phù hợp hơn với **redistribution / reorganization of recurrence structure**
hơn là một simple increase/decrease of "complexity".

---

## Important contrast

Sleep apnea trong paper:

```text
DET ↑ + LAM ↑
→ global regularization / simplification
```

Current Drowsiness:

```text
DET ↓ + LAM/TT ↑ tendency
```

→ Drowsiness không giống simple pathological loss of complexity.

Nó có thể phản ánh một **mixed transitional dynamical regime**.

---

## Methodological relevance

Paper support mạnh rằng:

> RQA conclusions phụ thuộc vào embedding, delay và threshold.

Do đó rất relevant cho:

* frozen RQA parameters
* parameter-dependence verification
* robustness analysis

Ngoài ra, paper dùng **median + quartiles trong boxplots**, là supporting precedent cho việc mô tả heterogeneous RQA distributions, nhưng không phải direct justification cho session-level median aggregation.

---

## Discussion role

### RQ2 — RQA

* Cung cấp interpretation rõ cho diagonal vs vertical structures.
* Hỗ trợ cách diễn giải `DET↓` và `LAM/TT↑` như **different aspects of recurrence organization**.

### Verification / Method

* Strong citation cho việc RQA parameterization cần được kiểm tra cẩn thận.

### Claim boundary

Không nên suy ra:

```text
DET ↓ = less physical determinism
LAM ↑ = specific ANS shift
RQA change = chaos transition
```

---

## Main takeaway

> **Martín-González et al. cho thấy diagonal và vertical recurrence structures phản ánh các khía cạnh khác nhau của cardiovascular dynamics và phụ thuộc mạnh vào RQA parameterization. Điều này hỗ trợ trực tiếp cách diễn giải pattern `DET↓` cùng `LAM/TT↑` của nghiên cứu hiện tại như một reorganization của recurrence geometry, thay vì một thay đổi đơn chiều của complexity.**

```
