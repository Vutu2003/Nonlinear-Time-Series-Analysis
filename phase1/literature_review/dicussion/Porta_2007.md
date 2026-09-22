# Paper 3 — Porta et al. (2007)

## Method

- Phân tích **short-term RR interval dynamics** (~240–350 beats).
- Dùng **local nonlinear prediction** trên reconstructed phase space.
- Đánh giá:
  - **predictability / complexity**
  - **nonlinearity** bằng surrogate testing.
- Surrogates: FT, AAFT, IAAFT-1, IAAFT-2.

Nguyên lý:

```text
similar past states
→ similar future evolution
→ prediction quality reflects dynamical predictability
````

---

## Main findings

* Different prediction methods cho absolute values khác nhau nhưng **physiological changes được detect khá nhất quán**.
* Sympathetic activation và complete vagal blockade:

```text
predictability ↑
regularity ↑
complexity ↓
```

* Short-term RR dynamics lúc nghỉ chủ yếu **linear**.
* Autonomic imbalance không tự động làm nonlinear components tăng.
* **Complexity / predictability ≠ nonlinearity**.

---

## Physiological interpretation

Cardiovascular dynamics sinh ra từ nhiều interacting mechanisms:

```text
sympathetic / parasympathetic regulation
baroreflex
respiration
vasomotor oscillations
feedback loops
```

Thay đổi autonomic regulation có thể làm thay đổi **predictability / complexity**, nhưng không thể suy trực tiếp:

```text
predictability change
→ more/less chaos
```

---

## Relevance to current study

Rất gần về methodological logic:

```text
Porta:
RR → local nonlinear prediction → predictability

Current study:
PPG → Simplex Projection → CC / NRMSE
```

Do đó:

```text
CC ↓ / NRMSE ↑
→ reduced finite-horizon forecastability
```

không nên diễn giải là:

```text
more chaos
```

Ngoài ra, pattern của Porta:

```text
sympathetic activation → predictability ↑
```

khác với:

```text
Drowsy → predictability ↓
```

→ Awake–Drowsy change khó giải thích bằng một simple sympathetic shift.

---

## Discussion role

### RQ1

* Hỗ trợ tách rõ:

  * nonlinearity
  * complexity
  * predictability
* Surrogate rejection phải được diễn giải theo **specific null hypothesis**.

### RQ2

* Là reference quan trọng để diễn giải `CC↓ / NRMSE↑` như **reduced forecastability**.
* Cung cấp bridge:

```text
physiological/autonomic perturbation
→ altered cardiovascular dynamics
→ altered short-term predictability
```

---

## Main takeaway

> **Porta et al. cung cấp methodological foundation mạnh cho việc dùng local prediction để đặc trưng short-term cardiovascular dynamics, đồng thời cho thấy predictability/complexity và nonlinearity là các properties khác nhau.**

