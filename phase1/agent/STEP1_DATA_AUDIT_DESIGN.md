# Step 1 — Data Audit & Dataset Characterization Design

## 1. Goal

Implement a reusable core pipeline to audit and characterize all primary PPG CSV sessions before preprocessing or NTSA.

Step 1 must answer:

* Are all files structurally valid?
* Is sampling consistent with `fs = 50 Hz`?
* Are there missing, duplicated, or corrupted values?
* How long is each recording?
* How much Awake/Drowsy data exists?
* How are labels distributed into continuous state segments?
* Which sessions can support `60 / 180 / 300 s` analyses?
* What is the overall composition of the dataset?

This step performs **data inspection only**.

Do not implement:

* filtering;
* inversion;
* SQI;
* motion-artifact correction;
* stationarity tests;
* peak detection;
* PPI extraction;
* NTSA.

---

# 2. Dataset Assumptions

Primary dataset directory:

```text
dataset/dhdata/
```

Expected sampling frequency:

```text
fs = 50 Hz
expected_dt = 0.02 s
```

Frozen label mapping:

```text
0 -> Awake
1 -> Drowsy
```

Expected relevant columns:

```text
Time (real)
IR Value raw
Time (s)
Label
IR Value filtered
```

Known optional/empty column:

```text
Unnamed: 2
```

Primary scientific signal:

```text
IR Value raw
```

Canonical time axis:

```text
Time (s)
```

---

# 3. Proposed Core Structure

```text
src/
└── dataloader/
    ├── __init__.py
    ├── loader.py
    ├── schema.py
    ├── audit.py
    ├── segments.py
    ├── inventory.py
    └── models.py

tests/
└── dataloader/
    ├── test_loader.py
    ├── test_schema.py
    ├── test_audit.py
    ├── test_segments.py
    └── test_inventory.py
```

Generated files:

```text
outputs/
└── data_audit/
    ├── dataset_inventory.csv
    ├── dataset_summary.json
    └── sessions/
        ├── session_001.json
        ├── session_002.json
        └── ...
```

---

# 4. Module Responsibilities

## 4.1 `schema.py`

Define dataset constants and schema expectations.

Example responsibilities:

```text
REQUIRED_COLUMNS
OPTIONAL_COLUMNS
EXPECTED_FS
EXPECTED_DT
LABEL_MAP
WINDOW_DURATIONS
```

Recommended values:

```text
EXPECTED_FS = 50.0
EXPECTED_DT = 0.02

LABEL_MAP = {
    0: "Awake",
    1: "Drowsy",
}

WINDOW_DURATIONS = [60, 180, 300]
```

Do not hard-code these values elsewhere.

---

## 4.2 `loader.py`

Responsibilities:

1. Load one CSV.
2. Validate that file is readable.
3. Normalize simple column formatting if necessary.
4. Preserve original data.
5. Return a DataFrame plus file metadata.

Core API:

```python
load_session(path)
```

Expected behavior:

```text
CSV path
    ↓
read file
    ↓
basic structural validation
    ↓
return session dataframe
```

The loader must not:

* filter PPG;
* modify labels;
* interpolate samples;
* remove suspicious samples silently.

---

## 4.3 `audit.py`

Perform session-level acquisition audit.

Core API:

```python
audit_session(df, session_id, file_name)
```

Audit categories:

### Structural

Calculate:

```text
n_rows
n_columns
column_names
empty_columns
duplicate_rows
```

### Missing values

For every column:

```text
null_count
null_percentage
```

Also check:

```text
NaN
+inf
-inf
```

for numeric fields.

### Time axis

Using:

```text
Time (s)
```

calculate:

```text
start_time_s
end_time_s
duration_s

dt_min
dt_max
dt_mean
dt_median
dt_std

estimated_fs
```

Check:

```text
duplicate timestamps
non-monotonic timestamps
negative dt
zero dt
large time gaps
```

Estimated sampling frequency:

```text
estimated_fs = 1 / median(dt)
```

### Raw PPG descriptive statistics

For:

```text
IR Value raw
```

calculate:

```text
count
min
max
range
mean
median
std
q1
q3
iqr
n_unique
```

No physiological quality interpretation is performed here.

### Filtered PPG descriptive statistics

If:

```text
IR Value filtered
```

exists, calculate the same descriptive statistics.

This column is descriptive only and is not the primary analysis input.

---

# 5. Label Audit

For `Label`, calculate:

```text
unique_labels
invalid_labels
null_labels
```

Allowed labels:

```text
0
1
```

Map them to:

```text
Awake
Drowsy
```

For each state calculate:

```text
sample_count
sample_percentage
duration_s
```

Do not infer labels from PPG morphology.

Do not correct labels automatically.

---

# 6. Continuous State Segmentation

Implement in:

```text
segments.py
```

Core API:

```python
extract_label_segments(time_s, labels)
```

A new segment starts whenever:

```text
Label[i] != Label[i-1]
```

Each segment record should contain:

```text
segment_id
label
state
start_index
end_index
start_time_s
end_time_s
n_samples
duration_s
```

For every session calculate:

```text
n_segments
n_transitions

n_awake_segments
n_drowsy_segments

longest_awake_segment_s
longest_drowsy_segment_s

median_awake_segment_s
median_drowsy_segment_s
```

---

# 7. Window Availability Audit

This stage does not create analysis windows.

It only determines whether continuous state segments are long enough.

Durations:

```text
60 s
180 s
300 s
```

For each state and duration calculate:

```text
awake_ge_60
awake_ge_180
awake_ge_300

drowsy_ge_60
drowsy_ge_180
drowsy_ge_300
```

These values indicate whether at least one continuous segment is long enough.

Also calculate:

```text
paired_60
paired_180
paired_300
```

Definition:

```text
paired_T =
    Awake contains segment >= T
    AND
    Drowsy contains segment >= T
```

Optionally calculate the number of eligible continuous segments:

```text
n_awake_segments_ge_60
n_awake_segments_ge_180
n_awake_segments_ge_300

n_drowsy_segments_ge_60
n_drowsy_segments_ge_180
n_drowsy_segments_ge_300
```

Do not concatenate disconnected segments to satisfy a duration requirement.

---

# 8. Session Audit Status

Each session should receive:

```text
PASS
WARNING
FAIL
```

## FAIL

Use when core analysis input cannot be trusted/read.

Examples:

```text
CSV cannot be read
required column missing
Time (s) completely invalid
IR Value raw completely missing
Label completely missing
```

## WARNING

Use when data can still be characterized but an anomaly exists.

Examples:

```text
unexpected column
empty column
some null values
sampling irregularity
time gap
duplicate timestamp
invalid labels mixed with valid labels
unexpected estimated sampling rate
```

## PASS

No critical structural or acquisition anomaly detected.

All warnings and failures must include explicit reasons.

Example:

```json
{
  "status": "WARNING",
  "issues": [
    "Empty column: Unnamed: 2",
    "3 duplicated timestamps"
  ]
}
```

---

# 9. Per-Session Output

Each session must produce one machine-readable audit record.

Example fields:

```text
session_id
file_name
status
issues

n_rows
n_columns
duration_s

estimated_fs
dt_median
dt_std
n_duplicate_timestamps
n_non_monotonic_timestamps
n_time_gaps

raw_min
raw_max
raw_mean
raw_median
raw_std
raw_q1
raw_q3

awake_samples
awake_duration_s
awake_percentage

drowsy_samples
drowsy_duration_s
drowsy_percentage

n_transitions
n_segments

longest_awake_segment_s
longest_drowsy_segment_s

awake_ge_60
awake_ge_180
awake_ge_300

drowsy_ge_60
drowsy_ge_180
drowsy_ge_300

paired_60
paired_180
paired_300
```

Detailed segment information should be stored in the corresponding session JSON.

---

# 10. Dataset-Level Inventory

Implement in:

```text
inventory.py
```

Core API:

```python
audit_dataset(dataset_dir, output_dir)
```

Pipeline:

```text
discover CSV files
        ↓
load each session
        ↓
audit session
        ↓
extract continuous label segments
        ↓
calculate duration eligibility
        ↓
combine session records
        ↓
dataset_inventory.csv
        ↓
dataset_summary.json
```

Each row of:

```text
dataset_inventory.csv
```

represents exactly one recording session.

---

# 11. Dataset-Level Summary

Generate overall statistics:

```text
total_sessions
total_samples
total_recording_duration_s
total_recording_hours

sessions_pass
sessions_warning
sessions_fail

sampling_rate_min
sampling_rate_max
sampling_rate_median

session_duration_min
session_duration_max
session_duration_median

total_awake_duration_s
total_drowsy_duration_s

awake_percentage
drowsy_percentage

total_state_transitions

sessions_with_awake
sessions_with_drowsy
sessions_with_both_states

sessions_paired_60
sessions_paired_180
sessions_paired_300

sessions_with_missing_values
sessions_with_time_gaps
sessions_with_invalid_labels
```

---

# 12. Required Test Cases

## TC-01 — Valid CSV

Input:

```text
correct columns
50 Hz timeline
no missing values
labels 0 and 1
```

Expected:

```text
loader succeeds
audit completes
estimated fs ≈ 50 Hz
status PASS or WARNING only for known optional issues
```

---

## TC-02 — Missing Required Column

Remove:

```text
IR Value raw
```

Expected:

```text
status FAIL
explicit missing-column reason
no silent fallback
```

---

## TC-03 — Empty Optional Column

Input contains:

```text
Unnamed: 2
```

with 100% null values.

Expected:

```text
empty column detected
audit still completes
```

---

## TC-04 — Null Raw PPG Values

Inject NaN into:

```text
IR Value raw
```

Expected:

```text
null count detected correctly
WARNING
no automatic interpolation
```

---

## TC-05 — Null Labels

Inject missing values into:

```text
Label
```

Expected:

```text
null labels counted
WARNING
```

---

## TC-06 — Invalid Label

Inject:

```text
Label = 2
```

Expected:

```text
invalid label detected
not mapped to Awake/Drowsy
WARNING
```

---

## TC-07 — Duplicate Timestamp

Create:

```text
Time[i] == Time[i-1]
```

Expected:

```text
duplicate timestamp count > 0
zero dt detected
WARNING
```

---

## TC-08 — Non-Monotonic Timestamp

Create:

```text
Time[i] < Time[i-1]
```

Expected:

```text
non-monotonic timestamp detected
WARNING
```

---

## TC-09 — Missing Sampling Interval

At 50 Hz expected:

```text
dt = 0.02 s
```

Create a gap, e.g.:

```text
0.02
0.04
0.06
0.12
```

Expected:

```text
time gap detected
WARNING
```

---

## TC-10 — Incorrect Sampling Frequency

Construct timeline corresponding to:

```text
fs = 25 Hz
```

Expected:

```text
estimated_fs ≈ 25 Hz
sampling-rate mismatch detected
WARNING
```

---

## TC-11 — Label Segmentation

Input:

```text
0 0 0 1 1 0 0 1
```

Expected:

```text
4 continuous segments
3 transitions
```

---

## TC-12 — Single-State Session

All labels:

```text
0
```

Expected:

```text
Awake detected
Drowsy duration = 0
paired_60 = False
paired_180 = False
paired_300 = False
```

---

## TC-13 — Window Eligibility

Segments:

```text
Awake = 350 s
Drowsy = 200 s
```

Expected:

```text
paired_60  = True
paired_180 = True
paired_300 = False
```

---

## TC-14 — Disconnected Segments Must Not Be Combined

Segments:

```text
Drowsy = 170 s
Awake  = 20 s
Drowsy = 170 s
```

Expected:

```text
Drowsy total duration > 300 s
BUT
drowsy_ge_300 = False
```

Disconnected segments must never be concatenated for duration eligibility.

---

## TC-15 — Constant Raw Signal

Input:

```text
IR Value raw = constant
```

Expected:

```text
statistics calculated correctly
n_unique = 1
no crash
```

Signal quality interpretation is outside Step 1.

---

## TC-16 — Empty CSV

Input contains headers but no rows.

Expected:

```text
status FAIL
clear reason
no unhandled exception
```

---

## TC-17 — Completely Invalid File

Input cannot be parsed as CSV.

Expected:

```text
controlled failure
file recorded in dataset audit
remaining sessions continue processing
```

---

## TC-18 — Dataset Batch Robustness

Dataset directory contains:

```text
24 valid files
1 invalid file
```

Expected:

```text
all 25 files appear in audit result
invalid file marked FAIL
batch execution does not stop
```

---

# 13. Numerical Tolerance

Do not rely on exact floating-point equality.

Sampling checks should use configurable tolerances.

Example:

```text
expected fs = 50 Hz
expected dt = 0.02 s
```

Tolerance must be defined centrally in `schema.py`.

Do not hard-code tolerance values throughout the codebase.

---

# 14. Logging Requirements

Every batch audit should log:

```text
run timestamp
dataset path
number of files discovered
files processed
files passed
files warned
files failed
output paths
```

Do not silently discard exceptions.

Each failure must include:

```text
session/file
exception type
human-readable reason
```

---

# 15. Reproducibility

Step 1 should be deterministic.

Running the audit twice on identical files must produce identical:

```text
dataset_inventory.csv
dataset_summary.json
session audit statistics
segment boundaries
```

No random operations are required.

---

# 16. Notebook Role

Notebook is only for manual verification and visualization.

Suggested notebook:

```text
notebook/01_data_audit_validation.ipynb
```

Notebook workflow:

```text
import core API
    ↓
load one sample session
    ↓
display session audit
    ↓
display label segments
    ↓
verify descriptive statistics
    ↓
run full dataset audit
    ↓
inspect dataset_inventory.csv
    ↓
inspect dataset-level summary
```

Do not duplicate audit algorithms inside the notebook.

The notebook must call functions from:

```text
src/dataloader/
```

---

# 17. Acceptance Criteria

Step 1 is complete when:

* [ ] All 25 CSV files can be discovered automatically.
* [ ] Every file receives `PASS`, `WARNING`, or `FAIL`.
* [ ] Missing/null values are reported.
* [ ] Sampling frequency is estimated independently for every session.
* [ ] Timestamp irregularities are detected.
* [ ] Raw PPG descriptive statistics are generated.
* [ ] `0 -> Awake` and `1 -> Drowsy` mapping is applied consistently.
* [ ] Continuous Awake/Drowsy segments are extracted correctly.
* [ ] `60 / 180 / 300 s` eligibility is calculated from continuous segments.
* [ ] Disconnected state segments are never combined for eligibility.
* [ ] One-row-per-session `dataset_inventory.csv` is generated.
* [ ] Detailed per-session JSON reports are generated.
* [ ] `dataset_summary.json` is generated.
* [ ] Invalid files do not terminate the full batch.
* [ ] All unit tests pass.
* [ ] Notebook contains validation only, not core implementation.

---

# 18. Definition of Done

Step 1 output must provide a complete factual description of the primary dataset before any physiological preprocessing.

The final dependency boundary is:

```text
Raw CSV files
      ↓
Data Audit & Characterization
      ↓
Validated Dataset Inventory
      ↓
Step 2+ preprocessing / segmentation
```

No preprocessing decision should alter the outputs produced by Step 1.
