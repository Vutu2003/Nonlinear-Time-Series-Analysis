Được. Với mục tiêu mới, Phase này nên **dừng hoàn toàn ở dataset/label verification trên processed CSV**, không tính lại CC/NRMSE/DET/LLE và không cần bất kỳ fixed NTSA parameter nào ở notebook này.

Bạn có thể thay phần hướng dẫn cũ bằng nguyên khối markdown dưới đây cho Codex.

````markdown
# Verification Phase A — Label & Processed Dataset Verification Only

## 0. Scope

Notebook này chỉ thực hiện verification trên processed dataset CSV hiện tại.

Processed CSV có cấu trúc dạng:

```text
Time (s), IR Value raw, PPG processed, Label
````

Notebook này KHÔNG thực hiện:

* phase-space reconstruction
* Simplex Projection
* RQA
* LLE
* surrogate testing
* statistical comparison của CC / NRMSE / DET / LLE
* recomputation bất kỳ NTSA metric nào

NTSA sensitivity analysis sẽ được thực hiện ở notebook/experiment riêng sau khi Label & Dataset Verification hoàn tất.

Mục tiêu của notebook này là:

1. xác minh tính toàn vẹn của processed dataset
2. xác minh cấu trúc và temporal alignment của label
3. tái dựng các contiguous Awake/Drowsy segments
4. xác định chính xác các transition
5. định lượng mức độ label fragmentation / oscillation
6. xây dựng các conservative label masks cho các experiment sau
7. định lượng lượng dữ liệu còn lại dưới từng sensitivity rule
8. tạo các output có thể dùng trực tiếp cho NTSA verification ở bước sau

Không được chỉnh sửa, làm mượt hoặc tái gán label.

---

# 1. General implementation constraints

* Implement exactly the verification design below.
* Do not modify the scientific logic or thresholds unless explicitly instructed.
* Do not infer missing scientific parameters.
* Do not run any NTSA method.
* Do not modify `PPG processed`.
* Do not relabel Awake/Drowsy data.
* Do not smooth the label timeline.
* Do not use majority voting to replace short label segments.
* Do not automatically exclude sessions 09 or 13.
* Keep every exclusion decision traceable.
* Save intermediate audit tables.
* The notebook must run reproducibly from top to bottom.
* Process files session-by-session when practical to minimize memory usage.
* Avoid unnecessary DataFrame copies.
* Log warnings rather than silently repairing suspicious data.
* If a structural problem is detected, report it explicitly.

---

# 2. Configuration

The notebook must begin with one configuration cell.

User will manually provide:

```python
INPUT_DIR = ...
OUTPUT_DIR = ...
```

Optional:

```python
FILE_PATTERN = "*.csv"
```

Label mapping must also be explicitly defined by the user.

Example:

```python
LABEL_MAP = {
    0: "Awake",
    1: "Drowsy"
}
```

Do not assume the mapping if it has not been provided.

Define:

```python
TRANSITION_EXCLUSION_SEC = [30, 60]
OPTIONAL_TRANSITION_EXCLUSION_SEC = 90

MIN_SEGMENT_DURATION_SEC = [180, 300]
```

The 90-second transition exclusion is optional and should only be evaluated descriptively if sufficient data remain.

---

# 3. Expected processed dataset structure

Required columns:

```text
Time (s)
IR Value raw
PPG processed
Label
```

For each input file, verify these columns exist.

Do not rename columns silently.

If a required column is missing:

* flag the session as failed
* report the missing columns
* continue with other sessions if possible

---

# 4. Experiment A0 — Processed dataset integrity audit

## Objective

Verify that each processed CSV is structurally valid before performing any label sensitivity analysis.

## Checks per session

### 4.1. Basic structure

Record:

* file name
* inferred session ID
* inferred subject ID if available from filename or metadata
* number of rows
* first timestamp
* last timestamp
* recording duration

### 4.2. Timestamp integrity

Check:

* `Time (s)` is numeric
* no NaN timestamps
* timestamps are strictly increasing
* number of duplicate timestamps
* time differences:

```python
dt = Time.diff()
```

Report:

* minimum dt
* median dt
* maximum dt
* estimated sampling frequency:

```text
fs_est = 1 / median(dt)
```

### 4.3. Temporal gaps

Detect unusually large gaps relative to expected sampling interval.

Suggested descriptive criterion:

```text
gap if dt > 1.5 × median_dt
```

Also report more severe gaps separately:

```text
dt > 2 × median_dt
dt > 5 × median_dt
```

Do not automatically interpolate these gaps.

### 4.4. Signal integrity

For both:

```text
IR Value raw
PPG processed
```

report:

* NaN count
* Inf count
* finite sample count
* min
* median
* max
* standard deviation

Do not judge physiological validity here.

This step is only structural integrity verification.

### 4.5. Label integrity

Report:

* unique label values
* number of missing labels
* number of invalid labels
* number of samples per label
* duration per label

Invalid label means any value not present in `LABEL_MAP`.

## Output

Create:

```text
dataset_integrity_summary.csv
```

Suggested columns:

```text
subject
session
file
n_rows
duration_s
time_start
time_end
median_dt
estimated_fs
duplicate_timestamps
n_temporal_gaps
n_severe_gaps
raw_nan
raw_inf
processed_nan
processed_inf
label_nan
invalid_label_count
n_awake_samples
n_drowsy_samples
awake_duration_s
drowsy_duration_s
integrity_pass
notes
```

---

# 5. Experiment A1 — Raw-to-processed lineage audit within processed CSV

## Objective

Verify that the processed dataset preserves a coherent sample-level structure between:

```text
Time
IR Value raw
PPG processed
Label
```

This notebook does not need the original external raw CSV unless separately provided.

Because the processed dataset already contains both raw and processed PPG columns, verify:

* both signal columns have exactly the same row count
* both are aligned to the same timestamps
* labels are defined on the same rows
* no rows contain a signal value without a corresponding timestamp/label

Create descriptive checks for:

```text
finite raw AND finite processed
finite raw AND missing processed
missing raw AND finite processed
```

Do not evaluate whether the filter itself is correct.

Do not recompute preprocessing.

## Output

Add lineage-related fields to:

```text
dataset_integrity_summary.csv
```

and optionally create:

```text
processed_lineage_audit.csv
```

---

# 6. Experiment A2 — Reconstruct contiguous label segments

## Objective

Reconstruct the exact temporal organization of Awake and Drowsy labels.

A new segment begins when:

```text
Label[t] != Label[t-1]
```

or when a sufficiently large temporal gap interrupts continuity.

Do not merge same-state regions across a temporal gap.

For every contiguous segment compute:

* subject
* session
* segment_id
* numeric label
* mapped state
* start time
* end time
* duration
* number of samples
* estimated sampling frequency within segment

## Transition definition

Define transition time as:

> timestamp of the first sample carrying the new label.

Example:

```text
Awake → Drowsy
```

Transition time equals the timestamp of the first Drowsy sample.

## Output

Create:

```text
label_segments.csv
```

with columns:

```text
subject
session
segment_id
label
state
start_s
end_s
duration_s
duration_min
n_samples
```

---

# 7. Experiment A3 — Identify state transitions

## Objective

Generate an explicit table of all Awake ↔ Drowsy transitions.

For each transition report:

```text
subject
session
transition_id
from_label
to_label
from_state
to_state
transition_time_s
previous_segment_duration_s
next_segment_duration_s
```

Only count actual state changes.

Do not treat:

```text
Awake → temporal gap → Awake
```

as an Awake–Drowsy transition.

## Output

Create:

```text
label_transitions.csv
```

---

# 8. Experiment A4 — Session-level label structure audit

## Objective

Describe how stable or fragmented the label timeline is in each session.

For every session calculate:

```text
n_awake_segments
n_drowsy_segments
n_total_segments
n_transitions
total_awake_duration_s
total_drowsy_duration_s
median_segment_duration_s
mean_segment_duration_s
min_segment_duration_s
max_segment_duration_s
```

Also report:

```text
n_segments_lt_60s
n_segments_lt_180s
n_segments_lt_300s
```

Separately for Awake and Drowsy if practical.

## Output

Create:

```text
label_session_summary.csv
```

---

# 9. Experiment A5 — Label oscillation / fragmentation audit

## Objective

Identify rapid Awake–Drowsy reversals without changing the labels.

Detect patterns:

```text
Awake → Drowsy → Awake
```

and

```text
Drowsy → Awake → Drowsy
```

For each three-segment pattern record:

* duration of middle segment
* duration from first transition to second transition
* states involved

Create descriptive flags:

```text
middle_segment_lt_60s
middle_segment_lt_180s
middle_segment_lt_300s
```

These are descriptive only.

Do not:

* remove the segment
* relabel it
* merge surrounding states

## Output

Create:

```text
label_oscillation_audit.csv
```

Suggested fields:

```text
subject
session
pattern_id
state_before
middle_state
state_after
first_transition_s
second_transition_s
middle_segment_duration_s
lt_60s
lt_180s
lt_300s
```

---

# 10. Experiment A6 — Transition-distance annotation

## Objective

Annotate every sample with its proximity to the nearest Awake–Drowsy transition.

For every sample compute:

```text
distance_to_nearest_transition_s
```

Also create boolean flags:

```text
within_transition_30s
within_transition_60s
within_transition_90s
```

A sample is flagged if:

```text
abs(time - nearest_transition_time) <= threshold
```

Do not remove samples at this stage.

This step creates reusable masks for later NTSA experiments.

## Important

If a session has no transitions:

```text
distance_to_nearest_transition_s = NaN
within_transition_* = False
```

## Output

Do not necessarily export every annotated full-resolution CSV unless storage is acceptable.

Prefer one of these approaches:

1. save one compact annotated file per session
2. or save intervals/masks needed to reproduce filtering later

Recommended reusable output:

```text
transition_exclusion_intervals.csv
```

with:

```text
subject
session
transition_id
transition_time_s
exclude_30_start
exclude_30_end
exclude_60_start
exclude_60_end
exclude_90_start
exclude_90_end
```

---

# 11. Experiment A7 — Conservative transition-boundary data retention

## Objective

Quantify how much processed data would remain if regions near state transitions were excluded.

Evaluate:

```text
Primary:
all valid samples

Sensitivity T30:
exclude samples within ±30 s of any transition

Sensitivity T60:
exclude samples within ±60 s of any transition

Optional T90:
exclude samples within ±90 s of any transition
```

This notebook only measures retained data.

Do not calculate NTSA metrics.

For each session and each rule report:

```text
total_samples_before
total_samples_after
retained_fraction
awake_samples_before
awake_samples_after
drowsy_samples_before
drowsy_samples_after
awake_duration_after
drowsy_duration_after
```

## Important

If transition intervals overlap, take their union.

Do not double-count excluded samples.

## Outputs

Create:

```text
transition_retention_by_session.csv
transition_retention_overall.csv
```

---

# 12. Experiment A8 — Minimum state-segment duration retention

## Objective

Quantify how much data remain when only sustained state segments are retained.

Define:

```text
S0 = all valid segments
S3 = only segments with duration >= 180 s
S5 = only segments with duration >= 300 s
```

For each session and each rule report:

```text
n_segments_before
n_segments_after
awake_segments_before
awake_segments_after
drowsy_segments_before
drowsy_segments_after
awake_samples_after
drowsy_samples_after
awake_duration_after
drowsy_duration_after
```

A segment failing the duration threshold is excluded entirely.

Do not:

* trim the segment
* relabel it
* merge it with adjacent segments

## Outputs

Create:

```text
segment_duration_retention_by_session.csv
segment_duration_retention_overall.csv
```

---

# 13. Experiment A9 — Future 60-s NTSA window feasibility

## Objective

Estimate how much usable data remain for the future primary 60-s NTSA analysis without computing any NTSA metric.

This is only a feasibility / dataset-retention analysis.

For every contiguous retained state interval, calculate how many non-overlapping 60-s windows could be formed:

```text
n_60s_windows = floor(segment_duration_s / 60)
```

Important:

* windows must stay within one contiguous state segment
* disconnected segments of the same state must never be concatenated
* leftover samples shorter than 60 s are ignored
* do not calculate any metric

Evaluate separately for:

```text
Primary
T30
T60
S3
S5
```

For transition exclusion rules, first subtract transition-exclusion regions from the original segments and reconstruct the remaining contiguous intervals before calculating possible 60-s windows.

For each session report:

```text
possible_awake_60s_windows
possible_drowsy_60s_windows
has_both_states
```

## Outputs

Create:

```text
future_60s_window_feasibility_by_session.csv
future_60s_window_feasibility_overall.csv
```

This output will be used later to decide whether each conservative label condition provides enough paired Awake–Drowsy data for NTSA analysis.

---

# 14. Experiment A10 — Diagnostic analysis for sessions 09 and 13

## Objective

Determine whether sessions 09 and 13 have unusual label structure compared with the rest of the dataset.

Do not exclude them.

Compare:

```text
n_transitions
median_segment_duration
minimum_segment_duration
n_segments_lt_180s
n_segments_lt_300s
fraction_samples_within_30s_transition
fraction_samples_within_60s_transition
future Awake 60-s windows
future Drowsy 60-s windows
```

Report sessions 09 and 13 alongside the distribution of the other sessions.

Do not run hypothesis tests unless explicitly requested.

This is a descriptive diagnostic only.

## Output

Create:

```text
session_09_13_label_diagnostics.csv
```

---

# 15. Required visualizations

## Figure 1 — Label timeline across sessions

For every session display a horizontal timeline of:

```text
Awake
Drowsy
```

with transition boundaries visible.

Purpose:

* inspect fragmentation
* identify repeated transitions
* visualize short segments

Save:

```text
label_timeline_all_sessions.png
```

---

## Figure 2 — Segment duration distribution

Display distribution of contiguous segment duration:

* overall
* Awake
* Drowsy

Include reference lines at:

```text
60 s
180 s
300 s
```

Save:

```text
segment_duration_distribution.png
```

---

## Figure 3 — Transition count per session

Display:

```text
number of Awake↔Drowsy transitions
```

for each session.

Save:

```text
transition_count_by_session.png
```

---

## Figure 4 — Data retention under conservative label rules

Show retained data fraction under:

```text
Primary
±30 s
±60 s
≥3 min
≥5 min
```

Prefer separate Awake and Drowsy summaries.

Save:

```text
label_rule_data_retention.png
```

---

## Figure 5 — Future 60-s window retention

Show number or percentage of possible future 60-s windows under:

```text
Primary
±30 s
±60 s
≥3 min
≥5 min
```

Separate Awake and Drowsy.

Save:

```text
future_60s_window_retention.png
```

---

# 16. Master label-verification summary

Create one final table:

```text
label_verification_summary.csv
```

Suggested columns:

```text
session
integrity_pass
n_transitions
n_awake_segments
n_drowsy_segments
median_segment_duration_s
n_segments_lt_180s
n_segments_lt_300s
primary_awake_duration_s
primary_drowsy_duration_s
t30_awake_retained_fraction
t30_drowsy_retained_fraction
t60_awake_retained_fraction
t60_drowsy_retained_fraction
s3_awake_retained_fraction
s3_drowsy_retained_fraction
s5_awake_retained_fraction
s5_drowsy_retained_fraction
primary_awake_60s_windows
primary_drowsy_60s_windows
t30_awake_60s_windows
t30_drowsy_60s_windows
t60_awake_60s_windows
t60_drowsy_60s_windows
s3_awake_60s_windows
s3_drowsy_60s_windows
s5_awake_60s_windows
s5_drowsy_60s_windows
notes
```

---

# 17. Final notebook report

At the end of the notebook print a concise report containing:

## Dataset integrity

```text
Number of sessions:
Sessions passing structural integrity:
Sessions with warnings:
Estimated sampling frequencies:
Missing/invalid labels:
```

## Label structure

```text
Total number of segments:
Total transitions:
Median segment duration:
Shortest segment:
Longest segment:
```

## Fragmentation

```text
Segments < 60 s:
Segments < 3 min:
Segments < 5 min:
Rapid reversal patterns:
```

## Retention

```text
Data retained after ±30 s:
Data retained after ±60 s:
Data retained with segment >=3 min:
Data retained with segment >=5 min:
```

Report separately for Awake and Drowsy.

## Future 60-s feasibility

Report:

```text
number of sessions retaining >=1 Awake 60-s window
number of sessions retaining >=1 Drowsy 60-s window
number of sessions retaining both
```

for each rule:

```text
Primary
±30 s
±60 s
≥3 min
≥5 min
```

---

# 18. Interpretation rules

This notebook does not determine whether the scientific Awake–Drowsy NTSA findings are robust.

It only determines whether the dataset and label structure support later robustness experiments.

Possible conclusions:

## Dataset verification passes

If:

* timestamps are structurally valid
* labels contain only expected states
* processed signal is aligned with timestamp and label
* no unexplained sample-level corruption exists

then report:

> The processed dataset preserves a coherent temporal, signal, and label structure suitable for downstream label-sensitivity analyses.

## Label sensitivity datasets are feasible

If conservative rules retain sufficient data in both states across most sessions:

> Conservative label subsets can be constructed without eliminating the majority of paired Awake–Drowsy information.

## Strong data loss

If a rule removes substantial data:

> This sensitivity condition represents a strict subset and should be interpreted with the corresponding reduction in available data and future statistical power.

Do not interpret loss of data as evidence against the labels.

---

# 19. Scientific boundaries

The following claims are NOT allowed from this notebook:

```text
The labels are objectively correct.
The labels are camera-validated.
Short segments are mislabeled.
Transition regions are incorrect.
Awake/Drowsy differences are robust.
Drowsiness changes nonlinear dynamics.
```

Those claims require evidence outside this dataset or the later NTSA analysis.

The correct scope is:

> This verification characterizes the structural integrity, temporal organization, transition structure, fragmentation, and conservative data-retention properties of the existing Awake/Drowsy labels.

---

# 20. Required output structure

Use the user-specified output directory.

Recommended structure:

```text
01_label_dataset_verification/
│
├── audit/
│   ├── dataset_integrity_summary.csv
│   ├── processed_lineage_audit.csv
│   ├── label_segments.csv
│   ├── label_transitions.csv
│   ├── label_session_summary.csv
│   └── label_oscillation_audit.csv
│
├── masks/
│   └── transition_exclusion_intervals.csv
│
├── retention/
│   ├── transition_retention_by_session.csv
│   ├── transition_retention_overall.csv
│   ├── segment_duration_retention_by_session.csv
│   └── segment_duration_retention_overall.csv
│
├── feasibility/
│   ├── future_60s_window_feasibility_by_session.csv
│   └── future_60s_window_feasibility_overall.csv
│
├── diagnostics/
│   └── session_09_13_label_diagnostics.csv
│
├── figures/
│   ├── label_timeline_all_sessions.png
│   ├── segment_duration_distribution.png
│   ├── transition_count_by_session.png
│   ├── label_rule_data_retention.png
│   └── future_60s_window_retention.png
│
└── summary/
    └── label_verification_summary.csv
```

---

# 21. Computational constraints

This verification should be lightweight.

* Do not calculate recurrence matrices.
* Do not perform phase-space embedding.
* Do not run Simplex Projection.
* Do not estimate LLE.
* Do not generate PPS surrogates.
* Do not bootstrap NTSA statistics.
* Process individual CSV files sequentially where practical.
* Avoid retaining multiple full copies of the dataset in memory.
* Store compact interval tables rather than exporting unnecessary full-resolution copies.
* Use vectorized NumPy/Pandas operations for timestamp and label masks.
* Save outputs incrementally.

This notebook should require substantially less CPU and RAM than the later NTSA experiments.

---

# 22. End goal

At completion, this notebook must provide three things:

1. Evidence that the processed dataset is structurally coherent.
2. A complete audit of the existing Awake/Drowsy label timeline.
3. Reproducible conservative label masks/subsets that can later be used in a separate NTSA verification notebook.

The later NTSA notebook will use these predefined conditions:

```text
Primary
T30 = transition exclusion ±30 s
T60 = transition exclusion ±60 s
S3  = state segments >=3 min
S5  = state segments >=5 min
```

without redefining the label rules after seeing NTSA results.

```

Tôi đặc biệt thêm **A9 — Future 60-s NTSA window feasibility** vì nó cho bạn biết trước mỗi rule còn bao nhiêu cửa sổ Awake/Drowsy có thể dùng, nhưng vẫn hoàn toàn không chạy NTSA. Nhờ vậy bạn có thể **freeze `Primary / T30 / T60 / S3 / S5` từ label data trước khi nhìn kết quả nonlinear**, đây là cách kiểm soát thực nghiệm sạch hơn rất nhiều.
```
