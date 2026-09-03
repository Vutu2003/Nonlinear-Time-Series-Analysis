# Remaining gap: sufficient geometry under strict transfer

## Core message
The unresolved question is whether a single fixed partial-curve descriptor can preserve accuracy while reducing feature re-selection, target adaptation, and total cost.

## Slide content

**Established**

- Partial curves contain aging-sensitive information.
- Local geometry, finite differences, references, and nonlinear models can estimate SOH.
- Held-out-cell performance is feasible within a dataset.

**Insufficiently established as a combined result**

$$
\boxed{
\begin{aligned}
&\text{one capacity-defined scalar}\\
&+\text{BOL-referenced normalization}\\
&+\text{source-selected, frozen geometry}\\
&+\text{zero/few-shot target calibration}\\
&+\text{quantified end-to-end cost}
\end{aligned}}
$$

## Evidence from literature

- Naha 2020; Wen 2022; Qin 2024; Petkovski 2024; Yao & Chen 2025; Chen et al. 2025.

## Gap / limitation

This is a gap in combined evidence, not proof that the proposed GSI combination will succeed or that none of its elements has prior art.

## Link to GSI

GSI should be evaluated as the minimal candidate representation that could close this evidence gap.

## Source traceability

- `Naha_2020.md` → minimum-information question after multi-$\Delta V$ representation.
- `Wen_2022.md` → region dependence and changing external mapping.
- `Qin_2024.md` → close geometric/BOL-scaled neighbor with online adaptation.
- `Petkovski_2024.md` → reference features, held-out cells, and window dependence.
- `Chen_2025.md` → domain-specific feature selection and target fine-tuning.
- `Junran_Chen_2025.md` → representation mismatch and auxiliary-data burden.
- `report_schedule.md` → final gap synthesis.

## Presenter notes

- Đây là “gap in evidence”, không phải claim “first”.
- Mỗi thành phần riêng lẻ đều có prior art gần.
- Contribution chỉ mạnh nếu tổ hợp tối giản vẫn giữ được accuracy và transfer.
- Nếu frozen transfer thất bại, kết quả vẫn giúp xác định giới hạn của one-scalar representation.
