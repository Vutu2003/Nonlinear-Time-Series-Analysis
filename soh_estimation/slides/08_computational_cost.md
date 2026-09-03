# Low inference latency is not low end-to-end cost

## Core message
Computational efficiency must account for feature discovery, extraction, adaptation, inference, and memory as separate costs.

## Slide content

| Cost layer | What to measure |
|---|---|
| Feature discovery | Window/Head–Tail search time and evaluations |
| Preprocessing / extraction | Interpolation, smoothing, derivatives, per-cycle latency |
| Training / adaptation | Fit time and labeled target cycles |
| Inference | Latency on named hardware |
| Memory / size | Parameters, bytes, working memory |

**Why this matters**

- Yao & Chen 2025: testing is fast, while GP/search/extraction can dominate.
- Chen 2025: a hardware latency/size benchmark is reported.
- Several “low burden” claims in the notes remain qualitative.

$$
C_{total}=C_{discover}+C_{extract}+C_{adapt}+C_{infer}+C_{memory}
$$

## Evidence from literature

- Yao & Chen 2025 — about 0.016 s testing, but up to hours for one optimization path and minutes for some extraction paths.
- Chen et al. 2025 — Jetson Nano benchmark of about 15.6 ms and 1.97 MB.
- Petkovski 2024; Li 2024; Naha 2020; Wen 2022; Chen et al. 2024 — systematic end-to-end hardware accounting is absent from the notes.

## Gap / limitation

The reviewed evidence is not directly comparable because hardware, pipeline boundaries, and one-time versus recurring costs differ.

## Link to GSI

Benchmark GSI and baselines end to end on identical hardware, including nested feature search and target calibration rather than reporting linear-regression latency alone.

## Source traceability

- `Chen_2025.md` → quantified Shapelet discovery/extraction/training/testing costs.
- `Junran_Chen_2025.md` → Jetson Nano latency and model size.
- `Petkovski_2024.md`, `Li_2024.md`, `Naha_2020.md`, `Wen_2022.md`, `Kang_2024.md` → qualitative or incomplete cost evidence.

## Presenter notes

- Inference nhanh không phản ánh chi phí tìm feature hoặc fine-tune.
- Cần tách chi phí one-time và per-cycle nhưng vẫn report cả hai.
- So sánh chỉ hợp lệ khi cùng hardware và cùng ranh giới pipeline.
- GSI phải tính cả Head/Tail discovery, dù final model chỉ là linear regression.
