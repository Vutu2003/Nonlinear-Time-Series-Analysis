# Unknown repeated-session dependence sensitivity — results

## 1. Executive result

- **Mean_CC:** expected median direction in 100.000% of 100,000 random hypothetical pairings; median Δ*=-0.024205, 2.5–97.5% [-0.035921, -0.014749]; q<0.05 in 19.36%.
- **Mean_NRMSE:** expected median direction in 100.000% of 100,000 random hypothetical pairings; median Δ*=+0.026313, 2.5–97.5% [+0.018469, +0.034258]; q<0.05 in 27.82%.
- **DET:** expected median direction in 100.000% of 100,000 random hypothetical pairings; median Δ*=-0.018069, 2.5–97.5% [-0.025544, -0.010024]; q<0.05 in 22.59%.
- **LLE:** expected median direction in 100.000% of 100,000 random hypothetical pairings; median Δ*=-0.035608, 2.5–97.5% [-0.044613, -0.026557]; q<0.05 in 79.69%.

These are hypothetical two-session clusters, not recovered participant mappings. Direction and magnitude are the primary evidence; p/q support is secondary.

## 2. Input and baseline verification

Canonical input: [`canonical_20_session_7metric_P0_60s_v1.csv`](canonical_20_session_7metric_P0_60s_v1.csv); SHA-256 `3cdc90d0bf214244fcced56a44a692bd941432352837fe285d31be0c9f375286`. Exactly 20 numerically sorted sessions and seven complete paired metrics; baseline validation passed **before any matching was generated**. Source hashes and frozen settings are in [`manifest.json`](manifest.json) and [`protocol.json`](protocol.json).

| Metric | n=20 median Δ | n=20 p | n=20 r_rb | n=20 q_BH |
| --- | ---: | ---: | ---: | ---: |
| Mean_CC | -0.027705 | 0.02664185 | -0.561905 | 0.04662323 |
| Mean_NRMSE | +0.031855 | 0.01531219 | +0.609524 | 0.04662323 |
| DET | -0.018645 | 0.02148438 | -0.580952 | 0.04662323 |
| Lmean | -0.062991 | 0.05825806 | -0.485714 | 0.08156128 |
| LAM | +0.016509 | 0.14290619 | +0.380952 | 0.16672389 |
| TT | +0.009515 | 0.20244980 | +0.333333 | 0.20244980 |
| LLE | -0.037570 | 0.00070763 | -0.809524 | 0.00495338 |

## 3. Random-pairing sensitivity

Generated **100,000** matchings with replacement from the **654,729,075** possible perfect matchings; **99,990 unique**, duplicate fraction **0.010000%**. The complete ordered sequence and 700,000 metric results are in the compressed CSVs. The 2.5–97.5% interval below describes variation across sampled hypothetical matchings; it is not a bootstrap confidence interval for a participant effect.

| Metric | Original n=20 Δ | Median Δ* | Δ* 2.5–97.5% | Same-direction % | Median r_rb | r_rb 2.5–97.5% | p<0.05 % | q<0.05 % |
| --- | ---: | ---: | --- | ---: | ---: | --- | ---: | ---: |
| **Mean_CC** | -0.027705 | -0.024205 | [-0.035921, -0.014749] | 100.000 | -0.709 | [-0.927, -0.564] | 53.35 | 19.36 |
| **Mean_NRMSE** | +0.031855 | +0.026313 | [+0.018469, +0.034258] | 100.000 | +0.745 | [+0.636, +0.927] | 80.33 | 27.82 |
| **DET** | -0.018645 | -0.018069 | [-0.025544, -0.010024] | 100.000 | -0.709 | [-0.964, -0.564] | 64.03 | 22.59 |
| Lmean | -0.062991 | -0.065674 | [-0.100041, -0.033254] | 100.000 | -0.564 | [-0.782, -0.418] | 10.24 | 2.41 |
| LAM | +0.016509 | +0.022726 | [+0.006285, +0.040184] | 99.630 | +0.527 | [+0.345, +0.782] | 9.71 | 2.94 |
| TT | +0.009515 | +0.007641 | [+0.001190, +0.013655] | 99.246 | +0.382 | [+0.236, +0.600] | 0.21 | 0.04 |
| **LLE** | -0.037570 | -0.035608 | [-0.044613, -0.026557] | 100.000 | -0.964 | [-1.000, -0.818] | 100.00 | 79.69 |

For Lmean, LAM and TT, ‘same direction’ is descriptive relative to the observed n=20 median sign; the four predefined headline signs govern primary interpretation. Full min/25th/75th/max and magnitude distributions are in [`random_pairing_summary_v1.csv`](random_pairing_summary_v1.csv).

## 4. Directional robustness of headline metrics

A cluster counts toward the expected direction only when its oriented Δ* exceeds 1e-12; a median within that tolerance of zero does not preserve direction.

| Metric | Expected direction | Preserved % | Direction-count min / 2.5th / median / max | Sampled median crossed/touched zero? |
| --- | --- | ---: | --- | --- |
| Mean_CC | negative | 100.000 | 5 / 6.00 / 8.00 / 10 | No |
| Mean_NRMSE | positive | 100.000 | 6 / 7.00 / 8.00 / 9 | No |
| DET | negative | 100.000 | 6 / 6.00 / 8.00 / 10 | No |
| LLE | negative | 100.000 | 7 / 8.00 / 9.00 / 10 | No |

Full direction-count distribution across the fixed 100,000 matchings (percentages):

| Metric | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Mean_CC | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.028 | 2.561 | 24.553 | 49.223 | 22.794 | 0.841 |
| Mean_NRMSE | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.728 | 15.398 | 51.171 | 32.703 | 0.000 |
| DET | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.790 | 25.460 | 47.833 | 22.060 | 1.857 |
| LLE | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.271 | 13.920 | 55.836 | 29.973 |

## 5. Effect-magnitude stability

Magnitude ratio is |median Δ*| / |original n=20 median Δ|, a descriptive scale comparison. Distribution endpoints and inner quantiles of Δ* are recorded in the summary CSV.

| Metric | Δ* min / 2.5th / median / 97.5th / max | Magnitude ratio 2.5th / median / 97.5th |
| --- | --- | --- |
| Mean_CC | -0.047780 / -0.035921 / -0.024205 / -0.014749 / -0.003904 | 0.532 / 0.874 / 1.297 |
| Mean_NRMSE | +0.012076 / +0.018469 / +0.026313 / +0.034258 / +0.044176 | 0.580 / 0.826 / 1.075 |
| DET | -0.032904 / -0.025544 / -0.018069 / -0.010024 / -0.004709 | 0.538 / 0.969 / 1.370 |
| Lmean | -0.128074 / -0.100041 / -0.065674 / -0.033254 / -0.015260 | 0.528 / 1.043 / 1.588 |
| LAM | -0.007590 / +0.006285 / +0.022726 / +0.040184 / +0.052448 | 0.381 / 1.377 / 2.434 |
| TT | -0.002651 / +0.001190 / +0.007641 / +0.013655 / +0.016808 | 0.130 / 0.803 / 1.435 |
| LLE | -0.052499 / -0.044613 / -0.035608 / -0.026557 / -0.019861 | 0.707 / 0.948 / 1.187 |

Inner quartiles of sampled median effects:

| Metric | 25th percentile Δ* | 75th percentile Δ* |
| --- | ---: | ---: |
| Mean_CC | -0.027743 | -0.020904 |
| Mean_NRMSE | +0.023634 | +0.028469 |
| DET | -0.020786 | -0.015309 |
| Lmean | -0.076721 | -0.055661 |
| LAM | +0.016434 | +0.028936 |
| TT | +0.005375 | +0.009879 |
| LLE | -0.038802 | -0.032291 |

- **Mean_CC:** 0.000% of sampled median effects were zero or opposite to the expected direction; the 2.5th percentile of the magnitude ratio was 0.532. This quantifies observed movement toward zero without imposing a post hoc collapse threshold.
- **Mean_NRMSE:** 0.000% of sampled median effects were zero or opposite to the expected direction; the 2.5th percentile of the magnitude ratio was 0.580. This quantifies observed movement toward zero without imposing a post hoc collapse threshold.
- **DET:** 0.000% of sampled median effects were zero or opposite to the expected direction; the 2.5th percentile of the magnitude ratio was 0.538. This quantifies observed movement toward zero without imposing a post hoc collapse threshold.
- **LLE:** 0.000% of sampled median effects were zero or opposite to the expected direction; the 2.5th percentile of the magnitude ratio was 0.707. This quantifies observed movement toward zero without imposing a post hoc collapse threshold.

Across the four headline metrics, none of the 100,000 sampled medians reached zero; their 2.5th-percentile magnitude ratios ranged from 0.532 to 0.707. Thus attenuation occurs, especially for Mean CC and Mean NRMSE, but the sampled distributions do not show a substantial mass at zero.

## 6. Inferential support under n=10 hypothetical clusters

The p<0.05 and seven-metric BH q<0.05 fractions are shown in Section 3. Lower support fractions at n=10 can reflect reduced effective sample size and do not by themselves imply a reversed effect. Exact two-sided Wilcoxon used the same zero/tie rule for every matching; no nested bootstrap was run.

All-zero hypothetical-cluster vectors: **0** across 700,000 metric-matching evaluations; when present, the frozen convention is p=1 and r_rb=NaN.

## 7. Monte-Carlo convergence

All prefixes use the same prespecified sequence; N=100,000 was not adapted. The full 16-row table including 2.5th/97.5th percentiles and median r_rb is [`convergence_v1.csv`](convergence_v1.csv).

| Metric | Prefix | Sign % | Median Δ* | Δ* 2.5–97.5% | Median r_rb | q<0.05 % |
| --- | ---: | ---: | ---: | --- | ---: | ---: |
| Mean_CC | 1,000 | 100.000 | -0.024453 | [-0.036306, -0.014964] | -0.709 | 20.10 |
| Mean_CC | 10,000 | 100.000 | -0.024202 | [-0.035974, -0.014918] | -0.709 | 19.19 |
| Mean_CC | 50,000 | 100.000 | -0.024205 | [-0.036011, -0.014725] | -0.709 | 19.44 |
| Mean_CC | 100,000 | 100.000 | -0.024205 | [-0.035921, -0.014749] | -0.709 | 19.36 |
| Mean_NRMSE | 1,000 | 100.000 | +0.026313 | [+0.018042, +0.035022] | +0.745 | 29.10 |
| Mean_NRMSE | 10,000 | 100.000 | +0.026320 | [+0.018484, +0.034123] | +0.745 | 27.62 |
| Mean_NRMSE | 50,000 | 100.000 | +0.026326 | [+0.018469, +0.034217] | +0.745 | 27.94 |
| Mean_NRMSE | 100,000 | 100.000 | +0.026313 | [+0.018469, +0.034258] | +0.745 | 27.82 |
| DET | 1,000 | 100.000 | -0.018222 | [-0.025460, -0.009958] | -0.709 | 22.00 |
| DET | 10,000 | 100.000 | -0.018063 | [-0.025460, -0.010126] | -0.709 | 22.24 |
| DET | 50,000 | 100.000 | -0.018092 | [-0.025603, -0.010037] | -0.709 | 22.69 |
| DET | 100,000 | 100.000 | -0.018069 | [-0.025544, -0.010024] | -0.709 | 22.59 |
| LLE | 1,000 | 100.000 | -0.035763 | [-0.044542, -0.026539] | -0.964 | 80.50 |
| LLE | 10,000 | 100.000 | -0.035498 | [-0.044416, -0.026794] | -0.964 | 79.94 |
| LLE | 50,000 | 100.000 | -0.035608 | [-0.044580, -0.026648] | -0.964 | 79.69 |
| LLE | 100,000 | 100.000 | -0.035608 | [-0.044613, -0.026557] | -0.964 | 79.69 |

Change from the 50,000 to 100,000 prefix, reported without a post hoc stopping threshold:

| Metric | Sign-fraction change (percentage points) | Median Δ* absolute change | 2.5th / 97.5th Δ* absolute change | Median r_rb absolute change | q-support change (percentage points) |
| --- | ---: | ---: | --- | ---: | ---: |
| Mean_CC | 0.0000 | 0.00000000 | 0.00008940 / 0.00002461 | 0.000000 | 0.0830 |
| Mean_NRMSE | 0.0000 | 0.00001266 | 0.00000000 / 0.00004182 | 0.000000 | 0.1160 |
| DET | 0.0000 | 0.00002273 | 0.00005999 / 0.00001324 | 0.000000 | 0.1020 |
| LLE | 0.0000 | 0.00000000 | 0.00003294 / 0.00009067 | 0.000000 | 0.0080 |
The headline summaries **stabilized in the 50,000-to-100,000 comparison**: all four sign fractions and median `r_rb` values were unchanged; median-effect changes were at most 0.00002273, endpoint-percentile changes at most 0.00009067, and BH-support changes at most 0.116 percentage points. This is a descriptive convergence judgment, not an adaptive stopping rule; the prespecified 100,000 draw remains the final analysis.

## 8. Conservative/adversarial search

The table reports the **most conservative pairing found** for each prespecified metric/objective by 100-start steepest local search over 90 swaps per step. Each metric was optimized independently. These are discovered local optima, not proven global optima; the pairing is hypothetical. The full CSV includes the objective, starting candidate, number of steps and convergence across starts.

| Metric | Objective | Most conservative median Δ* | Direction count /10 | r_rb | p | q_BH for that matching | Pairing |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| Mean_CC | weakest_median | -0.003904 | 8/10 | -0.600 | 0.105469 | 0.147656 | `[(01,05),(04,11),(06,09),(07,08),(10,12),(13,21),(14,22),(15,23),(17,18),(19,25)]` |
| Mean_CC | weakest_r_rb | -0.024496 | 6/10 | -0.418 | 0.275391 | 0.321289 | `[(01,05),(04,06),(07,10),(08,25),(09,21),(11,18),(12,19),(13,15),(14,22),(17,23)]` |
| Mean_CC | weakest_direction_count | -0.020664 | 5/10 | -0.455 | 0.232422 | 0.325391 | `[(01,06),(04,09),(05,14),(07,25),(08,17),(10,11),(12,18),(13,15),(19,22),(21,23)]` |
| Mean_CC | weakest_wilcoxon_support | -0.024496 | 6/10 | -0.418 | 0.275391 | 0.321289 | `[(01,05),(04,06),(07,10),(08,25),(09,21),(11,18),(12,19),(13,15),(14,22),(17,23)]` |
| Mean_NRMSE | weakest_median | +0.012076 | 8/10 | +0.745 | 0.037109 | 0.129883 | `[(01,09),(04,12),(05,15),(06,07),(08,25),(10,19),(11,21),(13,23),(14,22),(17,18)]` |
| Mean_NRMSE | weakest_r_rb | +0.041490 | 6/10 | +0.455 | 0.232422 | 0.271159 | `[(01,09),(04,13),(05,10),(06,07),(08,25),(11,18),(12,14),(15,23),(17,21),(19,22)]` |
| Mean_NRMSE | weakest_direction_count | +0.026170 | 6/10 | +0.636 | 0.083984 | 0.186849 | `[(01,04),(05,06),(07,12),(08,13),(09,15),(10,11),(14,18),(17,19),(21,23),(22,25)]` |
| Mean_NRMSE | weakest_wilcoxon_support | +0.041490 | 6/10 | +0.455 | 0.232422 | 0.271159 | `[(01,09),(04,13),(05,10),(06,07),(08,25),(11,18),(12,14),(15,23),(17,21),(19,22)]` |
| DET | weakest_median | -0.004709 | 7/10 | -0.636 | 0.083984 | 0.097982 | `[(01,05),(04,06),(07,09),(08,13),(10,18),(11,12),(14,17),(15,23),(19,21),(22,25)]` |
| DET | weakest_r_rb | -0.023852 | 8/10 | -0.418 | 0.275391 | 0.321289 | `[(01,09),(04,12),(05,06),(07,08),(10,17),(11,22),(13,19),(14,15),(18,25),(21,23)]` |
| DET | weakest_direction_count | -0.017355 | 6/10 | -0.564 | 0.130859 | 0.229004 | `[(01,06),(04,08),(05,07),(09,14),(10,22),(11,18),(12,23),(13,17),(15,19),(21,25)]` |
| DET | weakest_wilcoxon_support | -0.023852 | 8/10 | -0.418 | 0.275391 | 0.321289 | `[(01,09),(04,12),(05,06),(07,08),(10,17),(11,22),(13,19),(14,15),(18,25),(21,23)]` |
| LLE | weakest_median | -0.019763 | 10/10 | -1.000 | 0.001953 | 0.013672 | `[(01,04),(05,07),(06,11),(08,09),(10,18),(12,19),(13,23),(14,25),(15,22),(17,21)]` |
| LLE | weakest_r_rb | -0.029994 | 9/10 | -0.745 | 0.037109 | 0.090234 | `[(01,04),(05,07),(06,08),(09,25),(10,12),(11,17),(13,18),(14,23),(15,21),(19,22)]` |
| LLE | weakest_direction_count | -0.043983 | 7/10 | -0.782 | 0.027344 | 0.095703 | `[(01,04),(05,06),(07,23),(08,19),(09,12),(10,11),(13,15),(14,21),(17,25),(18,22)]` |
| LLE | weakest_wilcoxon_support | -0.029994 | 9/10 | -0.745 | 0.037109 | 0.090234 | `[(01,04),(05,07),(06,08),(09,25),(10,12),(11,17),(13,18),(14,23),(15,21),(19,22)]` |

The 100 starts did **not** all converge to one matching. The number of distinct local endpoints was 98–100 across the 16 searches, and only one start reached each retained best matching. This multiplicity is recorded per objective in [`adversarial_best_found_v1.csv`](adversarial_best_found_v1.csv) and per start in [`adversarial_local_search_starts_v1.csv`](adversarial_local_search_starts_v1.csv); it reinforces that these are local-search findings rather than proven global extrema.

## 9. Integrated interpretation

- **Mean_CC:** preserved the expected direction in every sampled matching. Median magnitude ratio 0.874 (2.5–97.5% 0.532–1.297); median r_rb -0.709; q support 19.36%.
- **Mean_NRMSE:** preserved the expected direction in every sampled matching. Median magnitude ratio 0.826 (2.5–97.5% 0.580–1.075); median r_rb +0.745; q support 27.82%.
- **DET:** preserved the expected direction in every sampled matching. Median magnitude ratio 0.969 (2.5–97.5% 0.538–1.370); median r_rb -0.709; q support 22.59%.
- **LLE:** preserved the expected direction in every sampled matching. Median magnitude ratio 0.948 (2.5–97.5% 0.707–1.187); median r_rb -0.964; q support 79.69%.

The conservative searches show additional possible fragility within the specified local-search neighborhood; they do not estimate how likely any particular matching is in the actual dataset.

## 10. Manuscript implication

The corrected window-first Mean CC/Mean NRMSE baseline must replace the legacy prediction numbers. The random and conservative results above can be described as sensitivity to **unknown repeated-session dependence** under hypothetical two-session clustering. Manuscript claims about significance should use the reported support frequencies and should not describe the hypothetical clusters as observed participants.

## 11. Remaining limitation

True participant-session linkage remains unavailable, so actual within-participant correlation cannot be estimated. Hypothetical pairings do not replace cluster-aware inference using identified participants and do not establish participant-level effects. The analysis only measures how the present session-level conclusions change under the prespecified plausible clustering model.

## 12. Final conclusion

**Do the principal Awake–Drowsy conclusions appear dependent on treating all 20 sessions as independent inferential units?** Their **directions did not** depend on that assumption across the 100,000 sampled hypothetical pairings; the size of the effects and statistical support varied under ten-cluster aggregation. Conservative local-search findings above delimit the interpretation without identifying actual participant clusters.
