### RQ2 — Multiplicity-controlled Awake–Drowsy state effects

Seven predefined primary metrics were evaluated across 20 paired sessions
using 60-s Processed PPG:

- Prediction: Mean_CC, Mean_NRMSE
- RQA: DET, Lmean, LAM, TT
- Local divergence: LLE

Raw paired Wilcoxon p-values were jointly corrected using the
Benjamini–Hochberg false discovery rate procedure across the seven tests.

#### BH-FDR supported findings

- **Mean_CC**: median Delta=-0.0339, 95% CI [-0.0595, -0.0043], r_rb=-0.581, q_BH=0.0376; 15/20 lower in Drowsy.
- **Mean_NRMSE**: median Delta=0.0294, 95% CI [0.0047, 0.0530], r_rb=0.667, q_BH=0.0255; 15/20 higher in Drowsy.
- **DET**: median Delta=-0.0186, 95% CI [-0.0364, -0.0069], r_rb=-0.581, q_BH=0.0376; 15/20 lower in Drowsy.
- **LLE**: median Delta=-0.0376, 95% CI [-0.0537, -0.0230], r_rb=-0.810, q_BH=0.0050; 16/20 lower in Drowsy.

#### Directionally consistent but weaker findings

- **Lmean**: median Delta=-0.0630, 95% CI [-0.1247, -0.0139], r_rb=-0.486, q_BH=0.0816; 16/20 lower in Drowsy.
- **LAM**: median Delta=0.0165, 95% CI [-0.0044, 0.0635], r_rb=0.381, q_BH=0.1667; 13/20 higher in Drowsy.
- **TT**: median Delta=0.0095, 95% CI [-0.0034, 0.0160], r_rb=0.333, q_BH=0.2024; 14/20 higher in Drowsy.

#### Integrated interpretation

Drowsiness showed lower forecastability, with lower Mean_CC and higher Mean_NRMSE. Lower DET supported reduced diagonal recurrence organization. Lower LLE supported reduced local trajectory divergence.

All effect magnitudes are median paired Delta = Drowsy - Awake, with
bootstrap 95% confidence intervals, matched-pairs rank-biserial effect
sizes, and session-level direction counts. BH-FDR controls multiplicity
and does not replace effect-size or uncertainty reporting.
