# GSI literature-gap deck — Summary

## Central question

> How much geometric information from a partial-discharge voltage–capacity trajectory is actually required for reliable cross-cell SOH estimation?

## Narrative arc

1. Partial charge/discharge profiles are already a practical and information-rich basis for SOH estimation.
2. Their usefulness is region-dependent; a good result at one window does not establish a transferable representation.
3. Finite voltage differences, geometric/distance features, early-cycle referencing, and reference-pattern comparisons all have prior art.
4. The unresolved issue is therefore not whether geometry can encode aging, but whether one fixed, BOL-referenced scalar retains enough information under strict transfer.
5. Literature uses “generalization” for materially different protocols, ranging from later cycles of the same cell to target-domain fine-tuning.
6. Physical interpretation also has levels: correlation and trajectory-level explanations do not constitute mechanistic identification.
7. Computational claims must include feature discovery and adaptation, not inference latency alone.
8. GSI should be tested as a minimal-representation hypothesis, not presented as an already validated solution.

## Proposed GSI positioning

GSI is a physically motivated, mechanism-unproven hypothesis built around:

- one capacity-defined Head–Tail voltage descriptor;
- BOL-referenced normalization;
- feature geometry selected on source training data and then frozen;
- a simple mapping with zero/few-shot target calibration;
- quantified end-to-end cost, including feature discovery.

## Claims to avoid

- “First geometric SOH feature.”
- “First reference-normalized SOH feature.”
- “First lightweight/derivative-free partial-profile method.”
- “Generalizes” without naming the exact validation level.
- “GSI measures LLI/LAM/SEI” without direct diagnostic evidence.
- “Low cost” based only on final prediction latency.

## Evidence base

Primary evidence: `report_schedule.md` and the nine per-paper notes in `soh_estimation/`.

- `Naha_2020.md`
- `Wen_2022.md`
- `Jenu_2022.md`
- `Qin_2024.md`
- `Li_2024.md`
- `Petkovski_2024.md`
- `Kang_2024.md` (Chen et al., 2024)
- `Chen_2025.md` (Yao & Chen, 2025)
- `Junran_Chen_2025.md` (Chen et al., Applied Energy 2025)

Uncertainty and scope in these notes are preserved; no claim in this deck was added from memory of the original papers.
