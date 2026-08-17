````markdown
# Step 1 — Data Audit Notebook Analysis Design

## 1. Goal

Use the completed `src/dataloader/` core modules inside `data_audit.ipynb` to characterize the full primary dataset and generate dataset-level results for later Methods, Results, figures, and supplementary material.

The notebook must only call existing core APIs.

Do not duplicate audit or segmentation logic inside the notebook.

---

## 2. Dataset Overview

Report:

- total sessions;
- total samples;
- total recording duration (hours);
- session duration: min / median / max;
- sampling frequency: min / median / max;
- number of sessions containing Awake and Drowsy.

Expected label mapping:

```text
0 -> Awake
1 -> Drowsy
````

---

## 3. Data Quality Report

Summarize across all sessions:

* PASS / WARNING / FAIL counts;
* null / NaN values;
* `inf / -inf`;
* duplicate rows;
* duplicate timestamps;
* non-monotonic timestamps;
* time gaps;
* invalid labels;
* empty columns;
* sampling-rate inconsistencies.

Create a compact session-level quality table:

| Session | Duration | fs | Null | Gaps | Invalid Labels | Status |
| ------- | -------: | -: | ---: | ---: | -------------: | ------ |

---

## 4. Awake–Drowsy Composition

Calculate:

* total Awake duration;
* total Drowsy duration;
* Awake/Drowsy percentage;
* Awake/Drowsy duration per session.

### Plot — State Composition by Session

Create a horizontal stacked bar plot:

```text
x = recording duration
y = session
segments = Awake / Drowsy
```

Purpose:

* show label balance;
* show between-session heterogeneity;
* characterize state composition of the dataset.

---

## 5. Continuous State Segments

Using outputs from `segments.py`, report:

* total state transitions;
* transitions per session;
* number of Awake segments;
* number of Drowsy segments;
* longest Awake segment;
* longest Drowsy segment;
* median continuous Awake duration;
* median continuous Drowsy duration.

### Plot — Continuous Segment Duration

Compare distributions of:

```text
Awake segment duration
Drowsy segment duration
```

This analysis must use contiguous segments only.

Disconnected segments must not be combined.

---

## 6. Window Availability

Evaluate predefined durations:

```text
60 s
180 s
300 s
```

For each duration report:

| Duration | Awake Eligible | Drowsy Eligible | Paired Eligible |
| -------: | -------------: | --------------: | --------------: |
|     60 s |              n |               n |               n |
|    180 s |              n |               n |               n |
|    300 s |              n |               n |               n |

Where:

```text
paired_T =
    at least one Awake segment >= T
    AND
    at least one Drowsy segment >= T
```

### Plot — Session Availability vs Window Duration

```text
x = 60 / 180 / 300 s
y = number of eligible sessions

series:
- Awake
- Drowsy
- Paired
```

This result determines the available session pool for later window-length experiments.

---

## 7. Acquisition Consistency

Report per-session:

* recording duration;
* sample count;
* estimated sampling frequency;
* median sampling interval;
* sampling interval variability.

Optional plots:

### Recording Duration

```text
x = session
y = duration (min)
```

### Sampling Frequency

```text
x = session
y = estimated fs
reference = 50 Hz
```

---

## 8. Raw PPG Descriptive Statistics

Using `IR Value raw`, summarize across sessions:

* median;
* mean;
* standard deviation;
* IQR;
* minimum;
* maximum;
* signal range.

Use these only as acquisition-level descriptive statistics.

Do not interpret them as SQI or physiological quality metrics.

---

## 9. Core Results for Paper Preparation

At minimum, retain the following results from the notebook:

1. **Dataset summary**

   * sessions;
   * total recording hours;
   * sampling frequency;
   * median recording duration;
   * Awake/Drowsy durations.

2. **Data integrity summary**

   * missing values;
   * timestamp problems;
   * invalid labels;
   * audit status.

3. **Awake–Drowsy composition plot**

   * per-session stacked duration.

4. **Continuous-state duration statistics**

   * Awake vs Drowsy segment lengths.

5. **Window availability**

   * eligible Awake, Drowsy, and paired sessions at `60 / 180 / 300 s`.

---

## 10. Notebook Boundary

`data_audit.ipynb` may:

```text
load core outputs
        ↓
aggregate results
        ↓
display tables
        ↓
calculate dataset-level summaries
        ↓
generate plots
        ↓
interpret dataset composition
```

It must not implement:

* CSV parsing logic;
* schema validation;
* label segmentation;
* window eligibility logic;
* filtering;
* SQI;
* stationarity;
* peak detection;
* PPI;
* NTSA.

All core calculations must originate from `src/dataloader/`.

```
```
Có thể thêm một mục riêng ngay sau phần **Core Results for Paper Preparation** như sau:

````markdown
## 10. Publication-Ready Plot Requirements

All figures generated in `data_audit.ipynb` must be publication-ready and reproducible.

### General Style

- Use `matplotlib` as the primary plotting library.
- Use one consistent project-wide plotting style.
- Prefer clear, minimal scientific figures over decorative plots.
- Avoid unnecessary 3D effects, gradients, background decoration, and excessive grid lines.
- Avoid bar charts with `mean ± SEM` when individual/session-level information can be shown directly.
- Use consistent visual encoding for:
  - `Awake`
  - `Drowsy`
  - `Paired`
- The same state encoding must be reused across all later project figures.

### Figure Size

Figures should support standard journal layouts:

- single-column figure;
- double-column figure.

Figure dimensions must be explicitly defined rather than relying on notebook defaults.

### Typography

- Use a publication-safe font consistently.
- Axis labels, tick labels, legends, and annotations must remain readable after journal-size reduction.
- Use consistent font sizes across all figures.
- Avoid oversized titles inside figures.

### Axes and Labels

Every plot must include:

- meaningful axis labels;
- physical units where applicable;
- clearly defined category names;
- readable session identifiers when sessions are shown.

Examples:

```text
Recording duration (min)
Segment duration (s)
Eligible sessions (n)
Sampling frequency (Hz)
````

Avoid ambiguous labels such as:

```text
Value
Score
Index
```

### Statistical Visualization

Whenever possible, preserve the underlying session-level observations.

Prefer:

```text
individual points
paired points/lines
median + IQR
effect estimate + confidence interval
distribution plots
```

over summary-only visualizations.

Do not visually imply that windows are independent population samples.

### Data Integrity

Plots must be generated directly from outputs of the Step-1 core pipeline.

Do not manually:

* edit plotted values;
* remove sessions from plotting cells;
* reorder or filter data without an explicit documented rule.

Any exclusion shown in a figure must be traceable to the audit results.

### Resolution and Export Quality

During notebook development, figures may be displayed inline.

Final publication figures must support:

* raster export at >= 300 dpi;
* vector export where possible (`PDF` or `SVG`);
* tight bounding boxes;
* no clipped labels or legends.

Line plots, scatter plots, and bar-based scientific graphics should preferentially retain a vector version.

### Figure Consistency

All publication candidate figures must use consistent:

* figure width;
* font family;
* font size hierarchy;
* line width;
* marker size;
* state encoding;
* axis styling;
* legend styling.

These settings should eventually be centralized in a project-level plotting style such as:

```text
publication.mplstyle
```

The notebook should not independently redefine figure style in every plotting cell.

---

## 11. Notebook Boundary

`data_audit.ipynb` may:

```text
load core outputs
        ↓
aggregate results
        ↓
display tables
        ↓
calculate dataset-level summaries
        ↓
generate publication-ready plots
        ↓
interpret dataset composition
```

It must not implement:

* CSV parsing logic;
* schema validation;
* label segmentation;
* window eligibility logic;
* filtering;
* SQI;
* stationarity;
* peak detection;
* PPI;
* NTSA.

All core calculations must originate from `src/dataloader/`.

```

Mình đặc biệt khuyên giữ yêu cầu **state encoding nhất quán từ Step 1 cho đến toàn bộ paper**. Nghĩa là một khi `Awake` và `Drowsy` đã có visual identity trong `data_audit.ipynb`, Figure 4–10 sau này không nên tự đổi cách biểu diễn. Điều này sẽ giúp toàn bộ manuscript nhìn như một hệ thống figure thống nhất thay vì các plot độc lập.
```
