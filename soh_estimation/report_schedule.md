# Slide Report: Literature Gap for GSI

## 1. Opening message
**Current SOH literature is moving toward practical partial-curve estimation, but most solutions gain robustness by adding complexity.**

GSI đi hướng ngược lại:

$$
\text{minimal geometry}
+
\text{BOL normalization}
+
\text{simple mapping}
$$

---

## 2. Literature landscape từ 9 papers

### Theme 1 — Partial voltage/discharge data is practical
Nhiều paper dùng partial charge/discharge curve để tránh full-cycle testing.

**Gap còn lại:**  
partial window rất nhạy; vùng chọn feature có thể quyết định accuracy.

**Implication for GSI:**  
Head/Tail window phải được chứng minh ổn định, không phải chỉ là correlation optimum.

---

### Theme 2 — Geometric / distance features đã xuất hiện
Qin, Yao, Petkovski đều dùng các dạng geometric/distance/reference features.

**Gap còn lại:**  
đa số cần nhiều feature, curve statistics, Shapelet search, hoặc model adaptation.

**Implication for GSI:**  
Novelty không nên là “geometric feature”, mà là:

$$
\text{one fixed scalar descriptor}
$$

---

### Theme 3 — Reference normalization không hoàn toàn mới
Qin dùng self-scaling; Petkovski dùng reference-cycle curve subtraction; Yao dùng RefShapelet.

**Gap còn lại:**  
chưa chứng minh rõ một reference-normalized scalar có thể giảm cell-specific mismatch đủ mạnh.

**Implication for GSI:**  
ΔGSI phải chứng minh bằng:
- raw GSI vs ΔGSI;
- trajectory collapse;
- inter-cell dispersion reduction;
- LOCO gain.

---

### Theme 4 — Generalization thường là adaptation
Nhiều paper nói “generalization”, nhưng thực tế là:
- target fine-tuning;
- domain-specific feature selection;
- model update;
- train/test trong cùng dataset.

**Gap còn lại:**  
feature-level transferability và frozen mapping chưa được chứng minh đủ mạnh.

**Implication for GSI:**  
Claim mạnh nhất nên là:

$$
\text{frozen Head/Tail}
\rightarrow
\text{unseen-cell / external transfer}
$$

---

### Theme 5 — Complexity thường bị đánh giá thiếu
Một số paper có latency/model size, nhưng nhiều paper chỉ claim “low complexity”.

**Gap còn lại:**  
thiếu end-to-end benchmark gồm feature discovery, extraction, calibration, inference.

**Implication for GSI:**  
GSI nên report:
- feature extraction time;
- LR inference time;
- model size;
- memory;
- window-search cost.

---

## 3. Central gap for GSI

> Existing studies show that partial-curve SOH estimation is feasible, but robust transfer often requires complex feature engineering, reference-pattern search, multi-modal data, nonlinear models, or target-domain adaptation.

GSI đặt câu hỏi khác:

> Can a fixed, BOL-normalized, ultra-low-dimensional geometric descriptor retain enough aging information for accurate and transferable SOH estimation?

---

## 4. Strongest positioning of GSI

GSI không cần thắng bằng “first”.

GSI nên thắng bằng:

$$
\boxed{
\text{minimal representation}
+
\text{frozen transferability}
+
\text{low adaptation burden}
+
\text{quantified low cost}
}
$$

---

## 5. Suggested slide structure

1. **Why this literature audit matters**
2. **9-paper landscape: what has already been done**
3. **Partial-curve features are useful but window-sensitive**
4. **Reference/geometric features are not new**
5. **Generalization claims often rely on adaptation**
6. **Computational cost is inconsistently quantified**
7. **Remaining gap: minimal transferable representation**
8. **GSI hypothesis**
9. **Validation plan to convince reviewers**
10. **Take-home message for prof/partner**

---

## 6. Final take-home slide

**GSI contribution should be framed as:**

> A compact, reference-normalized geometric SOH descriptor that aims to reduce feature re-selection, target-cell adaptation, and computational burden while preserving cross-cell predictive accuracy.