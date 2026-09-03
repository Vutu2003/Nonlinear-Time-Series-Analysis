# “Generalization” is not one protocol

## Core message
The reviewed evidence ranges from same-cell forecasting to adapted target-domain transfer, while frozen feature-and-mapping transfer remains the strongest unresolved test.

## Slide content

| Level | What is held fixed? | Example in notes |
|---|---|---|
| Within-cell temporal | Same cell; later cycles held out | Li 2024 (NASA) |
| Unseen-cell | Cell identity held out | Petkovski 2024; Chen 2025 |
| Feature-level transfer | Extractor/geometry frozen | Rarely isolated |
| Mapping-level invariance | Same feature-to-SOH map | Not established across domains |
| Model-level adaptation | Source model updated on target labels | Qin 2024; Yao & Chen 2025 |
| Framework applicability | Pipeline re-tuned per domain | Yao & Chen 2025; Chen 2024 |
| Frozen cross-dataset transfer | Feature + map fixed externally | Not demonstrated in reviewed notes |

$$
\text{framework reusable}
\neq
\text{representation transferable}
$$

## Evidence from literature

- Li 2024; Petkovski 2024; Qin 2024; Yao & Chen 2025; Chen et al. 2024; Chen et al. 2025; Wen 2022.

## Gap / limitation

Cross-chemistry or cross-dataset applicability often includes window re-selection, target labels, fine-tuning, or dataset-specific training, so it does not prove a frozen GSI–SOH mapping.

## Link to GSI

Report nested LOCO, frozen external transfer, and an explicit target-cycle adaptation curve $K=0,1,3,5,10,20,\ldots$.

## Source traceability

- `Li_2024.md` → NASA temporal split and limited Oxford cross-cell transfer.
- `Petkovski_2024.md` → 109 train/validation cells and 15 unseen test cells.
- `Qin_2024.md` → online OSELM updates.
- `Chen_2025.md` → target-cell fine-tuning and framework-level applicability.
- `Kang_2024.md`, `Junran_Chen_2025.md` → dataset-wise tests without frozen cross-dataset proof.
- `Wen_2022.md` → external informativeness but changed feature–SOH behavior.

## Presenter notes

- Khi report kết quả phải gọi đúng tên protocol, không dùng “generalization” chung chung.
- Held-out cell trong cùng dataset là bằng chứng tốt nhưng chưa phải frozen external transfer.
- Fine-tuning chứng minh khả năng adaptation, không chứng minh zero-shot invariance.
- Với GSI, geometry và mapping phải được freeze trước khi nhìn target labels.
