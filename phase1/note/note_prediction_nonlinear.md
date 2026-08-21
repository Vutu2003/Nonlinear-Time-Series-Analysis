````markdown
# Nonlinear Prediction — Current Design Status

## Frozen / Nearly Frozen

| Component | Status |
|---|---|
| Predictor | **Frozen:** Simplex projection |
| Embedding parameters | **Frozen:** `m`, `τ` from AMI/FNN |
| Number of neighbors | **Nearly frozen:** `k = E + 1` |
| Distance metric | **Nearly frozen:** Euclidean distance |
| Weighting | **Nearly frozen:** standard exponential simplex weighting |
| Train/test strategy | **Frozen:** leave-one-out state-space prediction + temporal exclusion |
| Prediction metrics | **Frozen:** `CC(h)` and `NRMSE(h)` |
| Prediction output | **Frozen conceptually:** prediction-skill curves over horizon, not a single scalar |
| Predictor sensitivity | **Not planned:** simplex justified from literature/methodological rationale |

---

## Open Methodological Decisions

### 1. Theiler Window

Need to determine:

```text
W_Theiler
````

Purpose:

* exclude temporally adjacent states;
* prevent trivial nearest neighbors caused by serial continuity;
* avoid optimistic prediction performance.

Plan:

```text
literature review
→ define candidate W values
→ sensitivity analysis
→ select a defensible fixed W
```

Sensitivity should evaluate the effect of `W` on:

```text
CC(h)
NRMSE(h)
```

The goal is **robustness assessment**, not tuning `W` to maximize prediction skill.

---

### 2. Prediction Horizon

Prediction will be characterized as a function of horizon:

```text
CC(h)
NRMSE(h)
```

rather than at one selected horizon.

Current direction:

```text
h expressed in physical time (seconds)
```

Need to determine:

```text
h-grid
H_max
```

Main objective:

> characterize how prediction skill decays with increasing forecast horizon.

---

### 3. Signal Normalization

Still open.

Need to distinguish between:

```text
signal normalization before embedding / neighbor search
```

and:

```text
prediction-error normalization used in NRMSE
```

Signal normalization may affect phase-space geometry and nearest-neighbor selection, so it must be justified from source literature before freezing.

---

### 4. NRMSE Definition

Need to verify the denominator used for normalization.

General form:

```text
NRMSE = RMSE / normalization_factor
```

Candidate normalization factors may include:

```text
standard deviation
range
mean
other literature-specific definitions
```

The definition must be fixed before real-data inference.

---

## Deferred Until Later

### Surrogate Analysis

Not implemented during the current prediction-development stage.

Planned later, likely after RQA is finalized:

```text
Prediction
+
RQA
+
Surrogate testing
```

---

### Curve-Level Statistical Testing

Future surrogate comparison will use the **prediction curve**, rather than reducing nonlinear prediction immediately to one scalar.

Conceptually:

```text
Original:
CC_original(h)
NRMSE_original(h)

vs.

Surrogates:
CC_surrogate(h)
NRMSE_surrogate(h)
```

Possible future approaches:

```text
rank-based surrogate test
global/curve-wise comparison
functional summary statistics
```

Exact statistical method is **not frozen yet**.

---

# Current Priority

Three main methodological questions remain:

```text
1. Theiler window
2. Prediction horizon / H_max
3. Signal normalization + NRMSE definition
```

Recommended order:

```text
Theiler window
→ prediction horizon
→ normalization / error definition
→ freeze prediction protocol
→ implement final core simplex prediction
```

Rationale:

```text
Theiler window
→ determines valid neighbors

Prediction horizon
→ determines what future dynamics are being predicted

Normalization
→ determines phase-space distance scaling and prediction-error scaling
```

---

# Final Prediction Framework

```text
Reconstructed phase space
        ↓
Simplex projection
        ↓
Leave-one-out state prediction
+ temporal exclusion
        ↓
Prediction across horizon h
        ↓
CC(h) + NRMSE(h)
        ↓
Prediction-skill curves
```

Later:

```text
Prediction curves
+
RQA metrics
        ↓
Surrogate testing
        ↓
RQ1: nonlinear/deterministic dynamical evidence

Awake vs Drowsy comparison
        ↓
RQ2: state-dependent nonlinear organization
```

```
```
