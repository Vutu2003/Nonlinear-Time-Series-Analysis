## Four-duration window-size robustness

The 60-s analysis remains primary; 30, 120, and 180 s are sensitivity analyses.

Metrics preserving the predefined effect direction at all four durations: Mean_CC, Mean_NRMSE, DET, LLE.
Metrics not preserving it at all four durations: none.

- Mean_CC: 30-s median Delta=-0.0147 versus 60-s=-0.0339 (absolute magnitude smaller; ratio=0.434); same expected sign across all durations in 12/20 common sessions.
- Mean_NRMSE: 30-s median Delta=0.0203 versus 60-s=0.0294 (absolute magnitude smaller; ratio=0.689); same expected sign across all durations in 13/20 common sessions.
- DET: 30-s median Delta=-0.0169 versus 60-s=-0.0186 (absolute magnitude smaller; ratio=0.906); same expected sign across all durations in 12/20 common sessions.
- LLE: 30-s median Delta=-0.0325 versus 60-s=-0.0376 (absolute magnitude smaller; ratio=0.865); same expected sign across all durations in 15/20 common sessions.

The widest absolute bootstrap interval occurred for Mean_CC at 30 s (width=0.0673 on that metric's native scale).

Direction and magnitude are reported independently of statistical significance. Raw robustness p-values are descriptive and were not added to the primary BH-FDR family.
