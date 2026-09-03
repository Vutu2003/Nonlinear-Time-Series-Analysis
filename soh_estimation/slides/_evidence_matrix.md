# Evidence matrix for the GSI literature-gap deck

## Reading key

- **Yes**: explicitly supported in the paper note.
- **Partial**: present, but only for a narrower protocol or with an important qualification.
- **No evidence**: not demonstrated in the available note; this does not prove the paper never addressed it.
- Generalization categories are kept separate rather than collapsed into one label.

## Method and representation

| Paper note | Partial profile | Main representation | Reference / normalization | Window dependence | Model / added input |
|---|---|---|---|---|---|
| Naha 2020 | Partial charge | 9 capacity-indexed finite $\Delta V$ + $T_{avg}$ | Current/resistance correction, not BOL subtraction | Starting voltage is application-chosen; no systematic region map | ANN |
| Wen 2022 | Shallow partial CC charge/discharge | $\Delta SoC$ across a fixed voltage span | No explicit $HI_t-HI_0$ | Yes; window scanned by correlation | Mainly linear relation in a suitable regime |
| Jenu 2022 | Partial charge | ICA peaks or integrated voltage | No BOL reference reported in note | Yes; IV strongly voltage-range dependent, especially for LFP | ICA needs filtering; IV is derivative-free |
| Qin 2024 | Partial charge | 3 relative geometric features in $(t,V)$ | Initial-value self-scaling $X_i/X_0$ | Yes; IC-peak and shape-constrained region selection | Online OSELM adaptation |
| Li 2024 | Partial discharge | 3 $dV/dt$ interval features | None reported in note | Yes; predefined dataset-specific voltage regions | Smoothing + HPO-OS-ELM |
| Petkovski 2024 | Partial discharge | Statistics of $Q_k(V)-Q_{10}(V)$ + temperature | Reference-cycle curve subtraction | Yes; some high-voltage intervals perform poorly | SVR |
| Chen et al. 2024 | Partial profile under fast charge | 4 handcrafted time/voltage/integral/IC features | None reported in note | Region robustness not established | CNN + CSAM + LSTM + attention |
| Yao & Chen 2025 | Partial curve patterns | Shapelet distance (minED/VMED) | Reference Shapelet; domain-specific supervised selection | Yes; window/step optimized by domain | Fine-tuning + 4-model ensemble |
| Chen et al. 2025 | Partial voltage profile | Multi-modal learned representation | No BOL scalar normalization reported in note | Yes; window position and length matter | Voltage profile + operation histogram, CNN/FNN |

## Generalization taxonomy

| Paper note | Within-cell temporal | Unseen-cell | Feature-level transfer | Mapping-level invariance | Model adaptation | Framework applicability | Frozen cross-dataset |
|---|---:|---:|---:|---:|---:|---:|---:|
| Naha 2020 | Partial | Partial robustness across cells/conditions | No evidence | No evidence | No evidence stated | Partial | No evidence |
| Wen 2022 | Yes | Partial | Partial: regional concept remains informative externally | No: relationship changes between datasets | No evidence stated | Yes | No evidence |
| Jenu 2022 | Yes | No evidence | No evidence | No evidence | No evidence | Partial across C-rates | No evidence |
| Qin 2024 | Yes | Partial | Partial: self-scaled geometry | No | Yes: online OSELM | Yes | No |
| Li 2024 | Yes (NASA) | Partial (Oxford) | No systematic test | No evidence | Sequential learner, but frozen transfer unclear | Partial | No |
| Petkovski 2024 | Yes | Yes: 15 held-out cells | Partial within one dataset | Partial within one dataset | No target fine-tuning reported | Yes | No |
| Chen et al. 2024 | Yes | Partial | No frozen cross-dataset test | No | Models trained/tested per dataset | Yes across datasets | No |
| Yao & Chen 2025 | Yes | Yes after target adaptation | Weak–moderate; selector is domain-specific | No | Yes: labeled target cell fine-tuning | Strong | No |
| Chen et al. 2025 | Yes | Yes within each dataset | No frozen cross-dataset test | No evidence | Dataset-level training | Yes | No |

## Interpretation and computational evidence

| Paper note | Interpretation level supported | Discovery / extraction cost | Training / adaptation | Inference / memory benchmark |
|---|---|---|---|---|
| Naha 2020 | Phenomenological/model-based trajectory explanation; not direct degradation-mode proof | Not quantified systematically | Small ANN; not systematically benchmarked | No quantitative hardware benchmark in note |
| Wen 2022 | IC-supported electrochemical consistency; not direct LLI/LAM proof | Window scan implied; not systematically benchmarked | Simple relation | No quantitative hardware benchmark in note |
| Jenu 2022 | ICA can link peaks to degradation phenomena; IV itself is mainly phenomenological | ICA filtering burden; no end-to-end timing | Not emphasized in note | Qualitative “lightweight” for IV |
| Qin 2024 | IC-informed region plus geometric rationale | Region selection required; no full timing in note | Online model updates | No hardware benchmark in note |
| Li 2024 | Phenomenological | Differentiation + Gaussian smoothing; no full timing | HPO-OS-ELM | “Reduced burden” is qualitative in note |
| Petkovski 2024 | Phenomenological curve-evolution explanation | Interpolation/subtraction/statistics; no timings | SVR | Computational advantage qualitative only |
| Chen et al. 2024 | Phenomenological features; black-box final mapping | Multi-feature extraction; no systematic timing | Deep hybrid training | No latency/FLOPs/memory benchmark in note |
| Yao & Chen 2025 | Interpretable distance, but domain-dependent | Quantified: GP/search/extraction can dominate | About 180 s training/fine-tuning | About 0.016 s testing; ensemble cost context needed |
| Chen et al. 2025 | Phenomenological multi-modal explanation | Multi-source preprocessing/history required | CNN/FNN training | Jetson Nano about 15.6 ms and 1.97 MB |

## Theme-to-source traceability

| Deck theme | Primary supporting note files |
|---|---|
| Partial-profile practicality | `Naha_2020.md`, `Wen_2022.md`, `Jenu_2022.md`, `Li_2024.md`, `Petkovski_2024.md` |
| Window sensitivity | `Wen_2022.md`, `Jenu_2022.md`, `Qin_2024.md`, `Li_2024.md`, `Petkovski_2024.md`, `Junran_Chen_2025.md` |
| Geometric/reference prior art | `Naha_2020.md`, `Qin_2024.md`, `Petkovski_2024.md`, `Chen_2025.md`, `Kang_2024.md` |
| SOH–voltage mismatch | `Junran_Chen_2025.md`, with representation-shift context from `Chen_2025.md` |
| Adaptation versus frozen transfer | `Qin_2024.md`, `Chen_2025.md`, `Petkovski_2024.md`, `Wen_2022.md` |
| Physical-interpretation levels | `Naha_2020.md`, `Wen_2022.md`, `Jenu_2022.md`, `Kang_2024.md` |
| End-to-end computational accounting | `Chen_2025.md`, `Junran_Chen_2025.md`, `Petkovski_2024.md`, `Li_2024.md`, `Kang_2024.md` |
| Remaining minimal-representation gap | `Naha_2020.md`, `Qin_2024.md`, `Petkovski_2024.md`, `Chen_2025.md`, `report_schedule.md` |
