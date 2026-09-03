# Partial profiles work—but the window is part of the method

## Core message
Across the reviewed studies, SOH information is unevenly distributed along the voltage trajectory and feature quality depends on the observed region.

## Slide content

| Evidence | Window dependence observed |
|---|---|
| Wen 2022 | $\Delta SoC$ window selected by SOH correlation |
| Jenu 2022 | Integrated voltage strongly range-sensitive for LFP |
| Qin 2024 | IC peak + curve-shape constraints define the interval |
| Li 2024 | Dataset-specific discharge voltage regions |
| Petkovski 2024 | Several high-voltage windows degrade performance |
| Chen 2025 | Partial-window position and length affect accuracy |

$$
\text{good feature at one window}
\not\Rightarrow
\text{stable transferable representation}
$$

**Required GSI evidence:** a broad stability basin under voltage-region and Head/Tail perturbations.

## Evidence from literature

- Wen 2022; Jenu 2022; Qin 2024; Li 2024; Petkovski 2024; Chen et al. 2025.

## Gap / limitation

Correlation-optimal or dataset-specific windows do not show that the selected geometry remains stable after moving to an unseen cell or dataset.

## Link to GSI

Select Head/Tail only inside each training fold, map the local error surface, then freeze both positions before testing the held-out target.

## Source traceability

- `Wen_2022.md` → window scan and nested leakage warning.
- `Jenu_2022.md` → IV voltage-range sensitivity.
- `Qin_2024.md` → adaptive IC/shape-based interval.
- `Li_2024.md` → NASA/Oxford regions and smoothing.
- `Petkovski_2024.md` → partial-window performance variation.
- `Junran_Chen_2025.md` → position/length sensitivity.

## Presenter notes

- Partial-profile practicality đã được support khá rộng.
- Nhưng “partial” không đủ mô tả method; vị trí và độ dài window là hyperparameter quan trọng.
- Với GSI, cần tìm basin rộng thay vì một điểm optimum sắc nhọn.
- Toàn bộ window search phải nằm trong training fold để tránh leakage.
