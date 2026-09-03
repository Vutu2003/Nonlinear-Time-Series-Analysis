# How much partial-curve geometry is enough?

## Core message

The literature shows that partial-curve geometry is informative, but it remains unclear how little information is sufficient for robust cross-cell transfer.

## Slide content

**Literature-gap audit for GSI**

> How much geometric information from a partial-discharge voltage–capacity trajectory is sufficient for reliable cross-cell SOH estimation?

$$
\text{minimal representation}
+
\text{BOL referencing}
+
\text{frozen transfer evaluation}
$$

## Evidence from literature

- Naha 2020 — multiple finite voltage differences can encode degradation information.
- Qin 2024 — low-dimensional geometry is useful, but combined with initial scaling and online adaptation.
- Petkovski 2024 — reference-subtracted partial curves support unseen-cell SOH estimation using curve statistics and SVR.
- Yao & Chen 2025 — reference-pattern geometry supports cross-domain estimation, but requires domain-specific selection and target fine-tuning.
- Chen 2025 — partial voltage profiles can exhibit SOH mismatch across cells, motivating more robust representations.

## Gap / limitation

Existing studies demonstrate that partial-curve and reference-based features are useful, but do not isolate whether a **single fixed, BOL-referenced scalar** is sufficient for:

- unseen-cell generalization;
- frozen feature transfer;
- external-dataset evaluation without feature re-selection.

## Link to GSI

GSI is therefore positioned as a **sufficient-representation hypothesis**:

> Can one fixed geometric descriptor preserve enough aging information while reducing feature complexity and transfer burden?

## Source traceability

- `Naha_2020.md` → finite ΔV features.
- `Qin_2024.md` → relative geometry, initial scaling, online adaptation.
- `Petkovski_2024.md` → reference-cycle subtraction and unseen-cell testing.
- `Yao_2025.md` → Shapelet/reference-pattern selection and target fine-tuning.
- `Chen_2025.md` → voltage–SOH mismatch across cells.
- `report_schedule.md` → central GSI positioning.

## Presenter notes

- Literature đã chứng minh partial-curve geometry có chứa thông tin aging; đó không phải novelty của GSI.
- Câu hỏi chưa được isolate rõ là mức representation tối thiểu nào vẫn đủ để transfer tốt.
- GSI kiểm tra một trường hợp cực đoan: một scalar cố định, BOL-referenced, model đơn giản.
- “Reliable transfer” phải tách thành unseen-cell generalization, frozen feature transfer và external-dataset evaluation.