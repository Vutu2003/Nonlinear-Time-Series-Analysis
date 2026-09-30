# TASK
Create the definitive frozen scientific source-of-truth file for Manuscript Version 2.

Project root:

`writing_manuscript/`

Output file:

`step_writing/01_master_canonical_sheet.md`

The target manuscript is:

**Ultra-Short PPG Dynamics Across the Wakefulness-to-Drowsiness Transition: A Nonlinear Time-Series Analysis**

Target journal:

**Chaos, Solitons & Fractals**

This file will become the single canonical scientific reference used for all later manuscript writing.

---

# 1. SOURCE HIERARCHY

Use only materials available inside the project.

Priority order:

1. latest finalized reports and frozen results available in the project
2. `step_writing/` finalized reports, if any already exist
3. `doc/manuscript_version1.pdf`
4. older or legacy values only for historical comparison

If two sources disagree:

- DO NOT silently reconcile them
- DO NOT average values
- DO NOT guess which is correct
- identify the conflict explicitly
- use the latest finalized/frozen result as canonical
- record the superseded value in a dedicated conflict/change log

Never invent missing methodological details.

Never use external literature or web search for this task.

---

# 2. PURPOSE OF THE FILE

The output is NOT a manuscript draft.

It is a compact but comprehensive scientific specification containing:

- frozen dataset facts
- protocol
- preprocessing
- quality control
- phase-space reconstruction
- Simplex Projection configuration
- RQA configuration
- Rosenstein LLE configuration
- PPS surrogate testing
- aggregation rules
- statistical framework
- canonical numerical results
- robustness/sensitivity results
- repeated-session dependence sensitivity
- symbolic analysis
- limitations
- claim boundaries
- forbidden claims
- manuscript-relevant interpretation rules

Every later manuscript section must be traceable to this file.

---

# 3. REQUIRED STRUCTURE

Create the following sections.

# Master Canonical Sheet — Manuscript Version 2

## 1. Study identity

Include:

- working title
- target journal
- central scientific question
- current manuscript status
- experimental scope status

State explicitly that the experimental scope is frozen unless a genuine error is discovered.

---

## 2. Dataset and protocol

Record exactly:

- number of recording sessions
- number of participants
- sex distribution
- age
- total recording duration
- Awake duration
- Drowsy duration
- sensor
- acquisition hardware
- labeling approach
- postprandial protocol
- PSG availability
- participant–session linkage status

Important:

If participant–session linkage is unavailable, state this exactly and do not infer any missing mapping.

---

## 3. Preprocessing and signal-quality control

Record:

- filter type
- filter order
- passband
- zero-phase implementation
- primary window length
- robustness window lengths
- SQI definition
- artifact rules
- quasi-stationarity definition
- subwindow lengths
- thresholds
- rejection rule

Be exact about quasi-stationarity:

- variance stability only
- do not introduce mean stability if it is not in the source

Include equations only if they help prevent ambiguity.

---

## 4. Phase-space reconstruction

Record:

- embedding method
- delay-selection method
- dimension-selection method
- frozen delay
- frozen embedding dimension
- sample conversion rule
- rationale for using a common reconstruction for Awake and Drowsy

Also record sensitivity grid for:

- delay
- dimension

Then summarize which metrics were stable and which were sensitive.

Important:

If DET is sensitive to embedding delay, state this explicitly.

Do not describe all metrics as parameter-invariant.

---

## 5. Simplex Projection

Record:

- embedding parameters
- number of neighbors
- distance metric
- weighting
- validation scheme
- Theiler window
- prediction horizons
- window-level aggregation
- session-state aggregation
- final metrics

The aggregation logic must be written exactly as:

1. compute CC and NRMSE at each prediction horizon within each valid window
2. average across horizons to obtain window-level Mean CC and Mean NRMSE
3. take the median across valid windows within each session × state

Do not use any older or ambiguous aggregation wording.

Record Simplex-specific verification/sensitivity results.

---

## 6. Recurrence Quantification Analysis

Record:

- recurrence distance
- target recurrence rate
- window-specific epsilon
- Theiler window
- l_min
- v_min
- metrics:
  - DET
  - Lmean
  - LAM
  - TT

Record interpretation boundaries:

- DET describes diagonal recurrence organization
- DET is not physical determinism

Record sensitivity to:

- recurrence rate
- RQA Theiler window
- embedding delay
- embedding dimension

Explicitly distinguish:

- robustness to RR/Theiler
- sensitivity to embedding delay

---

## 7. Largest Lyapunov Exponent

Record:

- estimator
- embedding
- neighbor rule
- Theiler rule
- fit interval
- follow time
- R² threshold
- minimum pair criteria
- validity criteria
- valid-window fraction

Record sensitivity to:

- fit interval
- R² threshold
- Theiler perturbation
- embedding parameters

Interpretation boundary:

LLE must be described as a finite-data local trajectory divergence descriptor, not proof of deterministic chaos.

---

## 8. PPS surrogate testing

Record:

- surrogate type
- null hypothesis
- number of surrogates per window
- finite-sample two-sided rank test
- minimum attainable p-value
- metrics tested
- observed directional pattern relative to PPS

Mandatory claim boundary:

Rejecting the PPS null does not prove deterministic chaos.

Canonical interpretation:

Observed PPG contains temporal/dynamical organization not fully reproduced by the tested noisy pseudoperiodic null.

---

## 9. Statistical framework

Record:

- computational unit
- inferential unit used in the primary analysis
- definition of:
  \[
  \Delta = \mathrm{Drowsy} - \mathrm{Awake}
  \]
- session-state aggregation
- primary effect summary
- Wilcoxon signed-rank test
- matched-pairs rank-biserial correlation
- bootstrap confidence interval
- number of bootstrap resamples
- BH-FDR
- exact primary hypothesis family

State clearly:

Primary inferential family = seven nominal 60-s metrics.

Sensitivity analyses are robustness analyses, not an expanded confirmatory hypothesis family.

---

## 10. Canonical primary 60-s results

Build one definitive table for all seven metrics.

Use the latest frozen canonical values.

Columns:

- Metric
- Median Δ
- 95% CI
- r_rb
- p
- q_BH
- evidence status

Evidence status should use only these categories:

- headline
- secondary
- unsupported trend

Do NOT create qualitative rankings such as “strong”, “weak”, “best”.

Important:

The corrected window-first Mean CC and Mean NRMSE values must replace any legacy values from Version 1.

If the latest canonical source gives:

- Mean CC = -0.027705
- Mean NRMSE = +0.031855

use those values.

Do not reuse superseded values such as -0.0339 or +0.0294 unless explicitly listed in the conflict/change log.

---

## 11. Headline findings

Freeze the four headline effects:

- Mean CC ↓
- Mean NRMSE ↑
- DET ↓
- LLE ↓

Interpret them as:

- finite-horizon forecastability ↓
- diagonal recurrence organization ↓
- local trajectory divergence ↓

Do not summarize these results using:

- more chaos
- less chaos
- greater complexity
- lower complexity

Record the central nonlinear interpretation:

Finite-horizon forecastability and local trajectory divergence are different dynamical properties.

Therefore:

forecastability ↓ and LLE ↓ are not inherently contradictory.

---

## 12. Window-length robustness

Record:

- 30 s
- 60 s
- 120 s
- 180 s

For each headline metric, state whether direction is preserved.

Canonical interpretation:

60 s is a practical compromise between temporal localization and estimator stability in this dataset.

Do not call 60 s universally optimal.

---

## 13. Label sensitivity

Record:

- T30
- T60
- S3
- S5

For each rule summarize:

- session count
- direction preservation
- q-support
- bootstrap CI behavior

Canonical interpretation:

Findings are not primarily driven by transition-adjacent windows or short state episodes within the tested label definitions.

Do not claim label uncertainty was eliminated.

---

## 14. NTSA parameter sensitivity

Summarize separately for:

- Simplex
- RQA
- LLE
- phase-space reconstruction

Explicitly record:

- Mean CC robustness
- Mean NRMSE robustness
- LLE robustness
- DET sensitivity to embedding delay

Canonical wording:

robust within the tested parameter range

not:

parameter-independent

---

## 15. Unknown repeated-session dependence sensitivity

Record the final frozen repeated-session sensitivity analysis.

Context:

- 20 sessions
- 10 participants
- true participant–session linkage unavailable
- hypothetical two-session clustering only

Record:

- number of possible perfect matchings
- number sampled
- number unique
- headline metric direction preservation
- sampled median Δ*
- 2.5–97.5% hypothetical pairing distribution
- magnitude ratios
- q-support frequencies
- Monte-Carlo convergence
- conservative/adversarial local-search findings

Freeze the interpretation:

The directions of the principal Awake–Drowsy effects were preserved across all 100,000 sampled hypothetical two-session clusterings, while effect magnitude and inferential support varied after aggregation to ten hypothetical clusters.

Mandatory limitation:

This does NOT demonstrate statistical independence.

This does NOT recover participant identity.

This does NOT establish participant-level inference.

This does NOT estimate true within-participant correlation.

---

## 16. Symbolic analysis

Record:

- 0V
- 1V
- 2V

Freeze current interpretation:

- 0V ↑
- 2V ↓
- 1V ≈ 0 / inconsistent

Status:

supportive / exploratory evidence only.

Interpretation boundary:

Compatible with altered cardiac autonomic modulation.

Not direct evidence of sympathetic or parasympathetic activity.

---

## 17. Evidence hierarchy

Create exactly three levels.

### Primary / headline evidence
- Mean CC
- Mean NRMSE
- DET
- LLE

### Secondary evidence
- Lmean
- LAM
- TT

### Supportive / exploratory evidence
- symbolic dynamics

Record that DET remains a headline metric but must be described as reconstruction-sensitive, particularly to embedding delay.

---

## 18. Limitations

Create a definitive list including:

- small cohort
- healthy young adults
- no PSG
- Drowsy cannot be equated with N1/NREM
- peripheral PPG only
- postprandial protocol
- participant–session linkage unavailable
- true within-participant correlation cannot be estimated
- finite-data dependence
- parameter dependence
- no multimodal validation
- no external validation
- PPS tests one specific null
- LLE is not proof of chaos

Do not soften or omit these.

---

## 19. Claim boundaries

Create a table with:

| Topic | Allowed wording | Forbidden wording |

Include at least:

- PPS
- LLE
- DET
- autonomic interpretation
- window length
- parameter robustness
- causality
- participant/session dependence
- Drowsy vs sleep stage

Examples:

Allowed:
“associated with”

Forbidden:
“caused”

Allowed:
“reduced local trajectory divergence”

Forbidden:
“less chaos”

Allowed:
“robust within the tested parameter range”

Forbidden:
“parameter-independent”

Allowed:
“sensitivity to unknown repeated-session dependence”

Forbidden:
“statistical independence was demonstrated”

---

## 20. Canonical terminology

Freeze exact preferred terms:

- Awake
- Drowsy
- wakefulness-to-drowsiness transition
- declining vigilance
- finite-horizon forecastability
- recurrence organization
- diagonal recurrence organization
- local trajectory divergence
- hypothetical two-session clustering
- unknown repeated-session dependence
- participant–session linkage
- session-level inference
- supportive symbolic analysis

Flag terms that should be avoided or minimized.

---

## 21. Main-text vs Supplementary candidates

Do not decide final layout yet, but classify each analysis as:

- likely main text
- likely supplementary
- undecided

Candidates:

- primary 60-s effects
- PPS
- window-length robustness
- label sensitivity
- parameter sensitivity
- repeated-session dependence
- symbolic analysis
- detailed estimator verification
- convergence/adversarial search

This is only a preparation for Step 2.

---

## 22. Conflict and superseded-value log

Create a dedicated table:

| Item | Legacy value/wording | Canonical value/wording | Source reason |

At minimum check:

- Mean CC legacy vs corrected
- Mean NRMSE legacy vs corrected
- aggregation wording
- any participant/session wording
- any claims that became more conservative after sensitivity analyses

Do not hide historical inconsistencies.

---

## 23. Final validation checklist

Before writing the output, verify:

- no canonical number conflicts remain unresolved
- corrected Mean CC / Mean NRMSE are used
- Δ convention is consistent
- all headline signs are correct
- primary inferential family is exactly seven nominal 60-s metrics
- repeated-session sensitivity is not called independence testing
- DET sensitivity is retained
- PPS rejection is not called proof of chaos
- LLE is not called proof of chaos
- symbolic analysis is not treated as direct autonomic measurement
- 60 s is not called optimal
- causal language is avoided
- missing participant–session linkage is explicit

---

# 4. STYLE

Write in compact academic English.

This is a technical source-of-truth document, not polished manuscript prose.

Prefer:

- tables
- concise bullets
- equations
- explicit frozen statements

Avoid:

- long narrative paragraphs
- speculation
- literature review
- rhetorical writing
- reviewer persuasion
- new interpretation

---

# 5. FINAL OUTPUT

Write only:

`step_writing/01_master_canonical_sheet.md`

Do not modify:

- `doc/manuscript_version1.pdf`
- any existing raw result files
- any experimental code
- any manuscript draft

At the end of the file add:

## Freeze status

State:

> This file is the canonical scientific source of truth for Manuscript Version 2. Numerical values, methodological settings, and claim boundaries should not be changed during manuscript writing unless a verified upstream error is identified.

Then stop.