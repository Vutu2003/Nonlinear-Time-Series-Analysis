# Integrated RQ2 Conclusion — Simplex Projection + RQA

### 1. Tổng hợp bằng chứng

Hai phương pháp nonlinear độc lập cung cấp bằng chứng bổ sung cho RQ2:

```text
Simplex Projection
→ local temporal evolution / forecastability

RQA
→ recurrence geometry / trajectory organization / laminar persistence
````

Cả hai đều sử dụng `session` làm đơn vị inference và cho thấy Awake–Drowsy differences phụ thuộc mạnh vào signal representation.

---

### 2. Processed PPG

Simplex Projection cho:

```text
CC ↓ trong Drowsy
NRMSE ↑ trong Drowsy
```

tại cả `60 / 120 / 180 s`, với toàn bộ 6 primary contrasts đạt BH-FDR support.

RQA đồng thời cho:

```text
DET ↓ trong Drowsy
```

tại cả `60 / 120 / 180 s`, cùng với xu hướng tăng laminar organization.

Hai kết quả hội tụ về interpretation:

> **Drowsiness is associated with reduced local trajectory coherence and reduced nonlinear forecastability in Processed PPG dynamics.**

---

### 3. Raw PPG

Simplex Projection cho state effect yếu và kém nhất quán hơn, không có primary contrast nào đạt BH-FDR support.

Ngược lại, RQA cho statistical support rõ hơn ở:

```text
Lmean ↑
Lmax ↑
LAM ↑
TT ↑
Vmax ↑
```

tùy window size.

Điều này cho thấy Raw PPG có thể bảo tồn các dynamical features liên quan nhiều hơn đến:

```text
recurrence persistence
long-line structures
laminar / trapping dynamics
```

thay vì local forecastability.

---

### 4. Representation dependence

Cả Simplex và RQA đều cho cross-representation differences có statistical support.

Do đó finding trung tâm của RQ2 là:

> **Preprocessing changes the observable expression of state-dependent nonlinear PPG dynamics.**

Raw và Processed không nhất thiết là hai representations cạnh tranh nhau mà có thể phản ánh các mặt bổ sung của cùng state transition:

```text
Processed
→ local predictability / trajectory coherence

Raw
→ recurrence persistence / laminar organization
```

---

### 5. Window-length robustness

Các state-dependent patterns chính được bảo tồn về hướng trên:

```text
60 s
120 s
180 s
```

ở cả Simplex Projection và RQA.

Do chưa pre-specify equivalence margin, không kết luận các window sizes là equivalent hoặc non-inferior.

Tuy nhiên, kết quả hỗ trợ một engineering insight:

> **The principal nonlinear state signatures are already observable in 60-s windows, suggesting limited additional dynamical information from extending the analysis window to 120–180 s relative to the added latency and computational cost.**

---

### 6. Integrated contribution cho RQ2

Kết quả hiện tại hỗ trợ kết luận:

> **Drowsiness is associated with a systematic and representation-dependent reorganization of reconstructed PPG dynamics. Processed PPG exhibits reduced local forecastability and reduced diagonal trajectory organization, whereas Raw PPG shows stronger changes in recurrence persistence and laminar structure. These complementary effects are directionally robust across 60–180 s analysis windows.**

Điều này cho thấy Awake và Drowsy khác nhau không chỉ ở một nonlinear metric riêng lẻ, mà ở nhiều khía cạnh bổ sung của reconstructed dynamics.

---

### 7. Giới hạn diễn giải

Các kết quả RQ2 hiện hỗ trợ:

```text
state-dependent nonlinear dynamical differences
representation-dependent dynamical reorganization
window-length robustness
```

Nhưng chưa cho phép kết luận:

```text
determinism
chaos
chaos-to-chaos transition
```

Các claim này cần được đánh giá bằng surrogate testing trong RQ1.

---

### 8. Trạng thái hiện tại

```text
Phase-space reconstruction       CLOSED
Simplex Projection RQ2           CLOSED
RQA RQ2                          CLOSED

Integrated RQ2 evidence          COMPLETE
Representation dependence       SUPPORTED
60–180 s directional robustness SUPPORTED

RQ1 surrogate testing            NEXT
Determinism / chaos claim        NOT YET ALLOWED
```

```

