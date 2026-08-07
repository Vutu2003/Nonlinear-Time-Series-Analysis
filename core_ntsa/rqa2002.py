"""
============================================================
Recurrence Quantification Analysis (RQA) - Marwan et al. (2002)
============================================================

This module provides a minimal, faithful end-to-end implementation of the 
extended Recurrence Quantification Analysis (RQA) methodology introduced by 
Marwan et al. (2002).

Unlike the classic Webber & Zbilut (1994) framework that exclusively analyzes 
diagonal structures to quantify system predictability (evolution), this module 
introduces a paradigm shift by shifting the statistical object of interest to 
vertical structures in order to quantify laminarity (persistence).

It implements the three core vertical descriptors proposed in 2002:
    • Laminarity (LAM)
    • Trapping Time (TT)
    • Maximal Vertical Length (V_max)

To maintain historical and mathematical fidelity, the architecture explicitly 
branches into two orthogonal quantification paths (Diagonal vs. Vertical) 
derived from the same underlying geometric reservoir.

Data Flow & Conceptual Diagram:
------------------------------------------------------------
[Raw Time Series]
       │
       ▼
 ┌────────────────────────────────────────────────────────┐
 │ MODULE 1: PHASE SPACE RECONSTRUCTION                   │
 │ (Takens' Time Delay Embedding)                         │
 └─────────────────────────┬──────────────────────────────┘
                           │
 ┌─────────────────────────┴──────────────────────────────┐
 │ MODULE 2: RECURRENCE MATRIX                            │
 │ (Distance Matrix -> Heaviside Thresholding)            │
 └─────────────────────────┬──────────────────────────────┘
                           │
         ┌─────────────────┴─────────────────┐
         │ (Paradigm Branching)              │
         ▼                                   ▼
 ┌────────────────────┐              ┌────────────────────┐
 │ MODULE 3           │              │ MODULE 4           │
 │ DIAGONAL SCAN      │              │ VERTICAL SCAN      │
 │ (Webber 1994)      │              │ (Marwan 2002)      │
 ├────────────────────┤              ├────────────────────┤
 │ Extract: P(l)      │              │ Extract: P(v)      │
 │ Metrics:           │              │ Metrics:           │
 │ - DET              │              │ - LAM              │
 │ - L_mean           │              │ - TT               │
 │ - L_max            │              │ - V_max            │
 └───────┬────────────┘              └───────┬────────────┘
         │                                   │
 ┌───────┴────────────┐              ┌───────┴────────────┐
 │ MODULE 5           │              │ MODULE 5           │
 │ WebberResult       │              │ MarwanResult       │
 │ run_webber2002()   │              │ run_marwan2002()   │
 └────────────────────┘              └────────────────────┘

The module provides two wrappers, `run_webber2002()` and `run_marwan2002()`, 
allowing researchers to directly reproduce the comparative experiments 
(Evolution vs. Persistence) presented in Figure 3 of the original paper.
"""


