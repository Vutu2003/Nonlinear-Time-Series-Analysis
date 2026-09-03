# Literature landscape: three design directions

## Core message
The literature extracts SOH information from partial curves by trading among representation size, adaptation, and auxiliary information.

## Slide content

| Direction | Examples | What buys robustness |
|---|---|---|
| Local handcrafted features | Naha; Wen; Jenu; Li | Multiple points, selected intervals, derivatives/integrals |
| Geometric/reference features | Qin; Petkovski; Yao & Chen | Relative geometry, early-cycle reference, pattern distance |
| Rich fusion/modeling | Chen 2024; Chen 2025 | Multiple features, deep sequence model, operation history |

**Common pattern**

$$
\text{partial observation}
\rightarrow
\text{region/feature design}
\rightarrow
\text{mapping or adaptation}
$$

**Open axis:** can robustness be retained while collapsing the representation to one frozen scalar?

## Evidence from literature

- Naha 2020; Wen 2022; Jenu 2022; Li 2024 — local/interval partial-profile indicators.
- Qin 2024; Petkovski 2024; Yao & Chen 2025 — geometric or reference-based pipelines.
- Chen et al. 2024; Chen et al. 2025 — multi-feature or multi-modal deep modeling.

## Gap / limitation

No reviewed note demonstrates the full combination of one fixed capacity-defined scalar, BOL normalization, low target adaptation, and frozen cross-dataset evaluation.

## Link to GSI

GSI explores the deliberately sparse corner of the design space rather than assuming richer representations are always required.

## Source traceability

- `Naha_2020.md`, `Wen_2022.md`, `Jenu_2022.md`, `Li_2024.md` → local handcrafted direction.
- `Qin_2024.md`, `Petkovski_2024.md`, `Chen_2025.md` → geometry/reference direction.
- `Kang_2024.md`, `Junran_Chen_2025.md` → rich-model/fusion direction.

## Presenter notes

- Đây là bản đồ theo theme, không phải một slide cho từng paper.
- Các hướng khác nhau đều có lý do thực dụng, nhưng robustness thường đi kèm thêm feature, search, history hoặc adaptation.
- GSI chọn kiểm tra góc cực tối giản của không gian thiết kế.
- “Một scalar” chỉ có ý nghĩa nếu không đánh đổi quá nhiều accuracy và transfer.
