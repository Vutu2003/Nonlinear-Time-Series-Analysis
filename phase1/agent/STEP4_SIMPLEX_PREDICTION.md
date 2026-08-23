````markdown
# Final Simplex Prediction Experiment — Processed → Raw → Cross-Representation

## Frozen Protocol

```text
m = 8

tau:
    Processed = 0.16 s
    Raw       = 0.20 s

Simplex:
    k = m + 1 = 9
    Euclidean distance
    exponential weighting
    leave-one-out state prediction

Theiler window:
    W = 1 s

Prediction horizon:
    Hmax = 4 s
    common physical-time grid

Outputs:
    CC(h)
    NRMSE(h)

Window sizes:
    60 / 120 / 180 s
````

No further parameter tuning.

Statistical hierarchy:

```text
Window
→ Session × State × Window Size
→ Across-session comparison
```

Primary RQ2 focus:

> Does nonlinear prediction behavior differ between Awake and Drowsy?

---

# Part A — Processed PPG

## Cell 1 — Load + Coverage

Load all eligible Processed windows.

Summarize:

```text
Session × State × Window Size → n_windows
```

---

## Cell 2 — Run Frozen Prediction

For every:

```text
Session
× State
× Window Size
× Window
× Horizon
```

compute:

```text
CC(h)
NRMSE(h)
valid_fraction
```

Keep detailed results in memory only.

---

## Cell 3 — Session-Level Aggregation

Aggregate windows within:

```text
Session × State × Window Size × Horizon
```

Calculate:

```text
mean / SD
median / IQR
n_windows
```

Then compute RQ2 difference curves:

```text
Delta_CC(h)
    = CC_Drowsy(h) - CC_Awake(h)

Delta_NRMSE(h)
    = NRMSE_Drowsy(h) - NRMSE_Awake(h)
```

---

## Cell 4 — Processed Final Outputs

Save only summary CSV:

```text
processed_simplex_summary.csv
```

Include:

```text
session
state
window_size
horizon
central_CC
variability_CC
central_NRMSE
variability_NRMSE
n_windows
```

Save publication-ready figures only:

```text
processed_awake_vs_drowsy.png
processed_state_difference.png
```

Figures should show:

```text
60 / 120 / 180 s
CC(h) and NRMSE(h)
Awake vs Drowsy
session-level / across-session variability
```

---

# Part B — Raw PPG

## Cell 5 — Load + Coverage

Load Raw PPG using the final Raw eligibility policy.

Summarize:

```text
Session × State × Window Size → n_windows
```

Record missing/low-support combinations.

---

## Cell 6 — Run Frozen Prediction + Aggregate

Repeat exactly the Processed pipeline using:

```text
tau_raw = 0.20 s
```

All other parameters remain identical.

Calculate:

```text
CC(h)
NRMSE(h)

Delta_CC(h)
Delta_NRMSE(h)
```

---

## Cell 7 — Raw Final Outputs

Save only:

```text
raw_simplex_summary.csv
```

Publication-ready figures:

```text
raw_awake_vs_drowsy.png
raw_state_difference.png
```

Do not save intermediate/window-level files unless required for debugging.

---

# Part C — Cross-Representation Comparison

## Cell 8 — Merge Session-Level Results

Merge Processed and Raw using:

```text
Session
× State
× Window Size
× Horizon
```

Use only comparable session/state/window-size combinations.

---

## Cell 9 — Compare State Effects Between Representations

Primary comparison:

```text
Delta_CC_Raw(h)
vs
Delta_CC_Processed(h)

Delta_NRMSE_Raw(h)
vs
Delta_NRMSE_Processed(h)
```

Evaluate:

```text
- direction of Awake–Drowsy difference
- magnitude of difference
- horizon dependence
- window-size robustness
- consistency across sessions
```

Do not pool windows across sessions.

---

## Cell 10 — Final Cross-Representation Outputs

Save one summary CSV:

```text
simplex_raw_vs_processed_summary.csv
```

Save publication-ready figures:

```text
simplex_rq2_awake_vs_drowsy.png
simplex_raw_vs_processed_state_effect.png
```

Priority figure for RQ2:

```text
Raw and Processed
× 60 / 120 / 180 s
× Delta_CC(h) / Delta_NRMSE(h)
```

The figure should make the Awake–Drowsy state effect and its consistency across representations immediately visible.

---

# Output Policy

Keep only final summary results.

## CSV

```text
processed_simplex_summary.csv
raw_simplex_summary.csv
simplex_raw_vs_processed_summary.csv
```

## Publication Figures

```text
processed_awake_vs_drowsy.png
processed_state_difference.png

raw_awake_vs_drowsy.png
raw_state_difference.png

simplex_rq2_awake_vs_drowsy.png
simplex_raw_vs_processed_state_effect.png
```

Do not save:

```text
per-window CSVs
per-session CSVs
per-horizon files
debug plots
temporary figures
duplicate results
```

---

# Final Analysis Logic

```text
Processed PPG
→ Awake vs Drowsy
→ session-level state difference

Raw PPG
→ Awake vs Drowsy
→ session-level state difference

Processed + Raw
→ compare state-difference curves
→ evaluate representation dependence
```

Scientific interpretation:

```text
CC(h), NRMSE(h)
    → nonlinear predictability profile

Awake vs Drowsy
    → RQ2: state-dependent dynamical organization

Raw vs Processed state effects
    → localization of representation-dependent changes
```

Surrogate testing and RQ1 inference remain deferred.

```
```
