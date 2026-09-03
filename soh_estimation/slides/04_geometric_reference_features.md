# Geometry and referencing are prior art

## Core message
GSI cannot claim novelty from finite voltage differences, geometric distance, early-cycle referencing, or reference-pattern comparison alone.

## Slide content

| Prior-art primitive | Literature example |
|---|---|
| Capacity-indexed finite $\Delta V$ | Naha 2020 |
| Fixed-time $\Delta V$ | Chen 2024 |
| Relative line/arc geometry | Qin 2024 |
| Initial-value scaling $X_i/X_0$ | Qin 2024 |
| Reference-cycle subtraction $Q_k-Q_{10}$ | Petkovski 2024 |
| Shapelet/reference-pattern distance | Yao & Chen 2025 |

**Defensible GSI distinction to test**

$$
\text{one capacity-defined Head--Tail scalar}
+\text{BOL difference}
+\text{frozen simple mapping}
$$

## Evidence from literature

- Naha 2020; Qin 2024; Petkovski 2024; Chen et al. 2024; Yao & Chen 2025.

## Gap / limitation

The notes leave open whether BOL referencing can suppress cell-specific offsets enough for a single frozen descriptor to transfer without repeated feature selection or model adaptation.

## Link to GSI

Compare raw GSI against $\Delta GSI=GSI_t-GSI_{BOL}$ using trajectory collapse, inter-cell dispersion, LOCO error, and external transfer.

## Source traceability

- `Naha_2020.md` → capacity-indexed local $\Delta V$ vector.
- `Kang_2024.md` → fixed-$\Delta t$ voltage difference.
- `Qin_2024.md` → $(t,V)$ geometry and $X_i/X_0$.
- `Petkovski_2024.md` → reference cycle 10 subtraction.
- `Chen_2025.md` → RefShapelet with minED/VMED.

## Presenter notes

- Slide này chủ động thừa nhận overlap mạnh nhất.
- Novelty không nằm ở từng primitive riêng lẻ.
- Điểm cần kiểm chứng là mức nén thông tin, cách freeze geometry, và adaptation burden.
- Ablation raw GSI versus $\Delta GSI$ là bắt buộc.
