# GSI: testable hypotheses, not conclusions

## Core message
GSI is credible only if its claims are decomposed into representation, normalization, transfer, robustness, and cost hypotheses.

## Slide content

Let

$$
GSI_t=\bar V_{H,t}-\bar V_{T,t},
\qquad
\Delta GSI_t=GSI_t-GSI_{BOL}.
$$

| Hypothesis | Falsifiable evidence |
|---|---|
| H1 — Sufficiency | One scalar approaches stronger multi-feature baselines |
| H2 — BOL effect | $\Delta GSI$ reduces cross-cell dispersion and error vs raw GSI |
| H3 — Frozen transfer | Source-selected Head/Tail works on held-out/external cells |
| H4 — Low adaptation | Competitive error at $K=0$ or small target-cycle $K$ |
| H5 — Stability | Broad basin under region, noise, and sampling perturbations |
| H6 — Low total cost | End-to-end cost is lower on identical hardware |

## Evidence from literature

- Qin 2024; Petkovski 2024; Yao & Chen 2025 — motivate H2–H4.
- Wen 2022; Jenu 2022; Chen et al. 2025 — motivate window and operating-condition sensitivity in H5.
- Yao & Chen 2025; Chen et al. 2025 — motivate an end-to-end, hardware-aware H6.
- Naha 2020; Chen et al. 2024 — motivate the one-versus-many representation test in H1.

## Gap / limitation

None of these hypotheses is established by the literature notes or by the GSI formulation alone.

## Link to GSI

Together, H1–H6 define the exact evidence needed before using the proposed GSI positioning.

## Source traceability

- `Naha_2020.md`, `Kang_2024.md` → multi-feature baselines and robustness questions.
- `Qin_2024.md`, `Petkovski_2024.md` → reference normalization and window transfer.
- `Chen_2025.md` → frozen-feature and target-cycle adaptation experiments.
- `Wen_2022.md`, `Jenu_2022.md`, `Junran_Chen_2025.md` → regional sensitivity.

## Presenter notes

- Mỗi dòng là một hypothesis có thể bị bác bỏ.
- H1 phải so với baseline mạnh, không chỉ so raw voltage.
- H2 cần cả representation metrics và prediction metrics.
- H3/H4 tách rõ frozen transfer khỏi few-shot adaptation.
- H6 bao gồm discovery cost, không chỉ LR inference.
