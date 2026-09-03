# Validation plan: freeze first, then transfer

## Core message
A leakage-free nested protocol can separate feature quality, mapping invariance, adaptation burden, robustness, and cost.

## Slide content

**Outer evaluation**

$$
\text{train cells}
\rightarrow
\boxed{\text{select Head/Tail + fit map}}
\rightarrow
\boxed{\text{freeze}}
\rightarrow
\text{held-out cell / external dataset}
$$

**Required experiments**

1. Raw GSI vs $\Delta GSI$ vs multi-feature/reference baselines.
2. Nested LOCO: all feature selection inside each outer fold.
3. Frozen external transfer; no target SOH used for re-selection.
4. Adaptation sweep: $K=0,1,3,5,10,20,\ldots$ labeled target cycles.
5. Stability maps: voltage region × Head/Tail positions.
6. Noise, downsampling, C-rate/current, and reference-noise tests.
7. ICA/DVA co-evolution analysis without mechanism attribution.
8. End-to-end timing, memory, model size, and worst-cell errors.

## Evidence from literature

- Wen 2022 — nested selection logic, stability basin, BOL and external-transfer analyses.
- Yao & Chen 2025 — frozen-feature test, target-cycle sweep, and total-cost benchmark.
- Petkovski 2024 — held-out cells, window dependence, and worst-cell failures.
- Chen et al. 2024; Jenu 2022; Naha 2020 — noise, sampling, rate, and trajectory-interpretation controls.

## Gap / limitation

Cross-chemistry transfer may remain confounded by chemistry, protocol, temperature, and instrumentation unless the dataset design permits these factors to be separated.

## Link to GSI

This protocol identifies which GSI claim survives and whether remaining error comes from the representation, mapping, or target shift.

## Source traceability

- `Wen_2022.md` → nested LOCO, broad basin, GSI/$\Delta GSI$, external test.
- `Chen_2025.md` → $K$-cycle adaptation curve and end-to-end benchmark.
- `Petkovski_2024.md` → unseen-cell and outlier-cell reporting.
- `Kang_2024.md` → noise/downsampling/reference sensitivity.
- `Jenu_2022.md`, `Naha_2020.md` → C-rate and resistance/polarization cautions.

## Presenter notes

- Trình tự quan trọng nhất là select trên train rồi freeze trước test.
- External dataset tuyệt đối không dùng target SOH để chọn lại Head/Tail trong zero-shot test.
- Report phân phối cell-wise và worst case, không chỉ mean error.
- Adaptation curve cho biết chính xác bao nhiêu target labels cần thiết.
- Physical và cost evaluation phải chạy trên cùng representation đã freeze.
