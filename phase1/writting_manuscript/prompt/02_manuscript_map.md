# TASK
Create the definitive argument-driven manuscript map for Manuscript Version 2.

Project root:

`writing_manuscript/`

Canonical scientific source:

`step_writing/01_master_canonical_sheet.md`

Historical baseline manuscript:

`doc/manuscript_version1.pdf`

Output file:

`step_writing/02_manuscript_map.md`

Target journal:

**Chaos, Solitons & Fractals**

---

# 1. SOURCE RULES

Use:

1. `step_writing/01_master_canonical_sheet.md` as the scientific source of truth
2. `doc/manuscript_version1.pdf` only as a structural/content baseline

If Version 1 conflicts with the canonical sheet:

- follow the canonical sheet
- do not copy the conflicting V1 value or wording
- do not attempt to reconcile it independently

Do not introduce new experiments.

Do not modify frozen numerical results.

Do not perform external literature research.

Do not write the final manuscript prose yet.

---

# 2. PURPOSE

The output must be an **argument map**, not a simple table of contents.

The map must define:

- the central scientific thesis
- RQ1
- RQ2
- evidence hierarchy
- narrative sequence
- section purpose
- exact scientific role of each result
- allowed claim
- forbidden overclaim
- main-text vs supplementary placement
- logical transitions between sections
- final reader takeaway

The manuscript should read as a coherent nonlinear-dynamics study, not as a collection of methods.

---

# 3. CENTRAL THESIS

Use the canonical thesis as the organizing principle.

Preferred direction:

> The wakefulness-to-drowsiness transition is associated with a coordinated reorganization of short-window PPG dynamics across finite-horizon forecastability, recurrence organization, and local trajectory divergence, rather than a simple shift along a single “more chaos–less chaos” axis.

Do not reduce the paper to:

> We applied Simplex Projection, RQA and LLE to PPG.

The three methods must be framed as complementary views of one dynamical phenomenon.

---

# 4. RESEARCH QUESTIONS

Freeze the manuscript around two research questions.

## RQ1
Does short-window PPG in Awake and Drowsy contain temporal/dynamical organization beyond that reproduced by the tested noisy pseudoperiodic null?

Evidence:

- PPS surrogate testing

Claim boundary:

PPS rejection does not prove deterministic chaos.

## RQ2
How does drowsiness alter complementary dynamical properties of short-window PPG?

Evidence:

- Mean CC
- Mean NRMSE
- DET
- LLE
- secondary RQA metrics

Interpretive dimensions:

- finite-horizon forecastability
- recurrence organization
- local trajectory divergence

---

# 5. EVIDENCE HIERARCHY

Use exactly:

## Primary / headline
- Mean CC
- Mean NRMSE
- DET
- LLE

## Secondary
- Lmean
- LAM
- TT

## Supportive / exploratory
- symbolic dynamics

DET remains headline but must be marked as reconstruction-sensitive, especially to embedding delay.

---

# 6. REQUIRED OUTPUT STRUCTURE

Create:

# Manuscript Map — Version 2

## 1. One-paragraph manuscript identity

Summarize:

- scientific problem
- gap
- contribution
- central thesis
- what makes the study more than a method-application paper

---

## 2. Core scientific logic

Build a compact causal/narrative chain such as:

1. drowsiness is a transitional physiological regime
2. PPG is commonly reduced to conventional features
3. PPG itself contains structured nonlinear/pseudoperiodic dynamics
4. this dynamical reorganization is under-characterized during Awake→Drowsy
5. a single nonlinear descriptor is insufficient
6. complementary prediction/recurrence/divergence analyses are required
7. surrogate testing establishes organization beyond the tested null
8. paired analysis identifies the direction of reorganization
9. robustness analyses show which findings are stable and which are parameter-sensitive
10. repeated-session sensitivity bounds the remaining inferential concern
11. symbolic analysis provides only supportive physiological context

This logic should govern the whole paper.

---

## 3. Introduction map

Design the Introduction as 5–7 paragraphs.

For each paragraph provide:

- purpose
- key content
- evidence/literature role
- transition to next paragraph
- claims to avoid

Suggested logic:

### Paragraph 1
Drowsiness as a physiological transition and importance of physiological monitoring.

### Paragraph 2
PPG in drowsiness literature is mostly used as conventional features or classifier input.

### Paragraph 3
PPG is itself a nonlinear pseudoperiodic dynamical signal.

### Paragraph 4
Gap:
- direct dynamical reorganization during Awake→Drowsy is under-characterized
- single nonlinear descriptors are insufficient
- short-window reliability is unresolved

### Paragraph 5
Rationale for complementary framework:
- prediction
- recurrence
- divergence

### Paragraph 6
RQ1 and RQ2.

### Paragraph 7
Contribution statement.

Do not write final prose.

---

## 4. Materials and Methods map

Define the final subsection architecture.

Recommended:

### 4.1 Dataset and experimental protocol
### 4.2 PPG preprocessing
### 4.3 Segmentation and quality control
### 4.4 Phase-space reconstruction
### 4.5 Nonlinear time-series analysis
#### 4.5.1 Simplex Projection
#### 4.5.2 RQA
#### 4.5.3 Rosenstein LLE
### 4.6 Pseudoperiodic surrogate testing
### 4.7 Statistical analysis
### 4.8 Sensitivity and robustness analyses

For each subsection state:

- what must remain in main Methods
- what textbook explanation can be removed
- what can move to Supplementary
- exact reproducibility-critical details
- claim/wording cautions

Important:

Methods should answer “what exactly was done”, not teach the general method.

---

## 5. Results map

This is the most important section.

Use evidence hierarchy, not algorithm order.

Recommended sequence:

### 5.1 Dataset and quality-control summary

Role:
brief setup only.

### 5.2 RQ1 — Dynamical organization beyond the noisy pseudoperiodic null

Evidence:
PPS.

Required takeaway:
Both Awake and Drowsy PPG contain organization not fully reproduced by the tested PPS null.

Forbidden takeaway:
deterministic chaos is proven.

### 5.3 RQ2 — Primary Awake–Drowsy dynamical reorganization

Lead with:

- Mean CC ↓
- Mean NRMSE ↑
- DET ↓
- LLE ↓

Then secondary metrics:

- Lmean
- LAM
- TT

Required takeaway:
coordinated multidimensional reorganization.

### 5.4 Robustness across window lengths

Required role:
establish finite-window stability and uncertainty.

### 5.5 Label-definition and NTSA-parameter sensitivity

Required role:
show robustness is method-specific.

Important:
explicitly preserve DET embedding-delay sensitivity.

### 5.6 Sensitivity to unknown repeated-session dependence

Required role:
address missing participant–session linkage.

Key message:
directions preserved across hypothetical clusterings, but effect magnitude and inferential support vary.

Forbidden message:
sessions are statistically independent.

### 5.7 Supportive symbolic analysis

Keep short.

Status:
supportive/exploratory only.

For every Results subsection provide:

- scientific question
- evidence shown
- minimum statistics needed
- likely figure/table
- one-sentence takeaway
- what interpretation should be deferred to Discussion

---

## 6. Discussion map

Design Discussion around arguments, not repetition of Results.

Recommended architecture:

### 6.1 Coordinated reorganization of PPG dynamics

Integrate:

- forecastability ↓
- recurrence organization altered
- local divergence ↓

Main claim:
multidimensional reorganization.

### 6.2 Why forecastability ↓ and LLE ↓ are not contradictory

This must be a central nonlinear-dynamics argument.

Explain conceptually:

- Simplex = finite-horizon prediction from neighboring states
- LLE = local trajectory divergence within a specific fitting scale
- therefore they need not move in opposite directions

Do not reduce this to “more/less chaos”.

### 6.3 Robustness and finite-window dynamics

Integrate:

- window length
- labels
- embedding
- estimator settings
- repeated-session dependence

Critical nuance:

Robustness is metric-specific, not universal.

DET is reconstruction-sensitive.

### 6.4 Physiological interpretation

Frame around:

- wake-to-sleep transition
- declining vigilance
- autonomic/cardiovascular regulation
- transitional regulatory regime

Use symbolic analysis only as supportive context.

Do not claim direct sympathetic or parasympathetic measurement.

Do not claim causal mechanisms.

### 6.5 Practical implications

Discuss:

- feasibility of short-window dynamical characterization
- possible future nonlinear descriptors
- no classifier was built
- no real-time detection performance was demonstrated

### 6.6 Limitations

Must include all canonical limitations.

Participant–session linkage limitation must be explicit.

For each Discussion subsection provide:

- core argument
- evidence feeding it
- relevant prior-work role
- exact claim boundary
- takeaway

---

## 7. Conclusion map

Define the final Conclusion logic in 3–5 sentences.

It should contain only:

- RQ1 answer
- RQ2 answer
- central multidimensional reorganization message
- short future-facing statement

No new claims.

No detailed sensitivity statistics.

---

## 8. Abstract map

Design the final Abstract only structurally.

Use:

1. background/gap
2. objective
3. data/method
4. RQ1 result
5. primary RQ2 results
6. robustness nuance
7. central conclusion

State which exact results are important enough for the Abstract.

Avoid overloading with q-values.

---

## 9. Figure plan

Create a main-paper figure plan.

For each proposed figure provide:

- figure number
- scientific role
- panels
- evidence level
- main-text justification
- whether an existing V1 figure can be reused/reworked

Preferred direction:

### Figure 1
Study / analysis pipeline

### Figure 2
Phase-space reconstruction or compact reconstruction validation

### Figure 3
PPS evidence

### Figure 4
Primary Awake–Drowsy effects

### Figure 5
Window-length robustness

### Figure 6
Compact robustness/sensitivity summary only if necessary

Avoid too many method-demonstration figures.

---

## 10. Table plan

Define likely main tables.

Candidates:

- dataset/QC summary
- frozen nominal configuration
- primary seven-metric results
- compact sensitivity summary

For each table state:

- main vs supplementary
- whether it duplicates a figure
- whether it is essential for reproducibility

---

## 11. Supplementary architecture

Design Supplementary sections for:

- full label sensitivity
- phase-space sensitivity
- Simplex verification
- RQA verification
- LLE verification
- repeated-session dependence details
- Monte-Carlo convergence
- adversarial/local-search analysis
- detailed symbolic results
- extra method demonstrations

The Supplementary should defend reproducibility and reviewer scrutiny without overwhelming the main paper.

---

## 12. Main text vs Supplementary decision table

Create:

| Analysis / evidence | Main text | Supplementary | Reason |

Include all major analyses.

---

## 13. Claim-boundary map

Create:

| Manuscript topic | Main allowed claim | Required caveat | Forbidden overclaim |

Include:

- PPS
- Simplex
- DET
- LLE
- autonomic interpretation
- 60-s window
- parameter robustness
- label sensitivity
- repeated-session dependence
- causal interpretation

---

## 14. Section-to-section transition map

Write one sentence describing the logical transition between:

- Introduction → Methods
- Methods → Results
- RQ1 → RQ2
- primary results → robustness
- robustness → symbolic support
- Results → Discussion
- dynamical interpretation → physiology
- physiology → limitations
- Discussion → Conclusion

The goal is to prevent the manuscript from feeling fragmented.

---

## 15. Reviewer-facing contribution map

Without writing reviewer-response prose, identify the strongest defensible contributions:

- conceptual contribution
- nonlinear-dynamics contribution
- methodological rigor
- short-window contribution
- robustness contribution

Also identify the main vulnerabilities:

- small cohort
- no PSG
- missing participant–session linkage
- postprandial design
- no external validation
- finite-data and parameter dependence

Do not score or rank them.

---

## 16. Final manuscript identity check

At the end, answer:

After reading only the title, abstract, main figures and conclusion, what should a reviewer understand this paper to be about?

Target identity:

> A study identifying coordinated multidimensional reorganization of short-window PPG dynamics across the wakefulness-to-drowsiness transition, supported by surrogate testing and extensive robustness analyses.

Avoid the identity:

> A small PPG study applying RQA, Simplex and Lyapunov exponents.

---

# 7. IMPORTANT DESIGN RULES

The manuscript map must preserve the following principles.

1. Scientific story > method order.
2. Primary evidence > secondary evidence > supportive evidence.
3. Robustness should support the story, not dominate it.
4. Sensitivity analyses do not erase limitations.
5. Statistical significance should not replace effect-direction and effect-magnitude interpretation.
6. DET sensitivity must remain visible.
7. Repeated-session sensitivity must not be presented as proof of independence.
8. Symbolic analysis must not compete with the main Simplex–RQA–LLE story.
9. The Discussion must interpret, not repeat Results.
10. The final manuscript must feel like a CSF nonlinear-dynamics paper, not a thesis chapter.

---

# 8. STYLE

Write in concise academic English.

Use:

- headings
- compact tables
- bullets
- short explanatory paragraphs

Do not write full manuscript paragraphs except where a one-sentence takeaway is explicitly requested.

Do not rewrite the Introduction, Methods, Results or Discussion yet.

This is an architecture document.

---

# 9. FINAL VALIDATION

Before finalizing, check that:

- all scientific content agrees with `01_master_canonical_sheet.md`
- no frozen number is altered
- corrected Mean CC / Mean NRMSE are assumed
- no statistical independence claim appears
- DET sensitivity remains explicit
- PPS rejection is not equated with deterministic chaos
- LLE is not equated with chaos
- symbolic results remain supportive
- 60 s is described as a practical compromise
- main/supplementary hierarchy is clear
- Results flow answers RQ1 then RQ2
- Discussion centers the forecastability–LLE nuance
- central thesis is visible throughout

---

# 10. FINAL OUTPUT

Write only:

`step_writing/02_manuscript_map.md`

Do not modify:

- `step_writing/01_master_canonical_sheet.md`
- `doc/manuscript_version1.pdf`
- any manuscript drafts
- any result files
- any experimental code

At the end add:

## Freeze status

State:

> This manuscript map defines the narrative architecture, evidence hierarchy, section roles, and claim boundaries for Manuscript Version 2. Subsequent writing should follow this map unless a deliberate manuscript-level revision is explicitly approved.

Then stop.