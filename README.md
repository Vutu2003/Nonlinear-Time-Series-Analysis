# Nonlinear Time Series Analysis

> Reading, systematizing, and reproducing foundational algorithms in nonlinear
> time series analysis.

This research and implementation project explores **Nonlinear Time Series
Analysis (NTSA)**. Its main goal is to turn original research papers into
readable, verifiable, and reusable implementations:

1. read and summarize the original method;
2. analyze its assumptions, mathematical formulation, and limitations;
3. design the algorithm and experiments;
4. implement the core scientific code;
5. reproduce the results reported in the paper;
6. evaluate the method on real-world data.

The project prioritizes scientific fidelity, verifiability, and code clarity
over hiding the workflow behind high-level APIs.

## 🧭 Five Main Research Directions

| Research direction | Central question | Representative topics |
|---|---|---|
| 🌀 **Chaos-based Methods / Determinism** | Does the time series reflect deterministic dynamics and sensitivity to initial conditions? | Phase-space reconstruction, embedding, nonlinear prediction, Lyapunov exponents |
| 📐 **Fractal Analysis** | How does the signal exhibit self-similarity and scaling behavior? | Fractal dimensions, DFA, multifractal analysis, singularity spectra |
| 📊 **Entropy-based Methods** | How uncertain, irregular, or complex is the signal? | Approximate Entropy, Sample Entropy, Permutation Entropy, Multiscale Entropy |
| 🔁 **Recurrence Plots** | When does the system return to previously visited states? | Recurrence Plots, RQA, Cross Recurrence Plots, Multivariate Recurrence Plots |
| 🔤 **Symbolic Encoding** | Can the dynamics be represented through symbols or order relations? | Symbolic dynamics, ordinal patterns, ordinal transformations |

These directions are not completely independent. For example, ordinal
patterns are both a symbolic representation and the foundation of Permutation
Entropy.

## 🔬 Research Workflow

```mermaid
flowchart LR
    A[Original paper] --> B[Paper summary]
    B --> C[Limitation analysis]
    B --> D[Algorithm design]
    D --> E[Core NTSA]
    C --> F[Experiment design]
    E --> F
    F --> G[Paper reproduction]
    G --> H[Real-world data evaluation]
    H --> I[Domain-specific applications]
```

Each stage is kept separate so that scientific formulations, implementations,
and experimental choices remain easy to distinguish.

## 📁 Project Structure

| Directory | Purpose |
|---|---|
| [`summary_paper/`](summary_paper/) | Summaries of research papers, including motivation, mathematical foundations, algorithms, experiments, and key conclusions. |
| [`limitations/`](limitations/) | Assumptions, limitations, failure cases, and interpretation risks associated with each method. |
| [`algorithm_design/`](algorithm_design/) | Core algorithm designs created before implementation, including formulas, modules, APIs, dependencies, and scientific invariants. |
| [`experiment_design/`](experiment_design/) | Experimental designs covering data, parameters, baselines, figures, diagnostics, and reproduction criteria. |
| [`core_ntsa/`](core_ntsa/) | Reusable implementations of the core NTSA algorithms. |
| [`paper_replications/`](paper_replications/) | Notebooks and workflows that reproduce experiments, figures, or results from original papers. |
| [`data/`](data/) | Input datasets used for testing and experimentation. |
| [`applied_realistic_data/`](applied_realistic_data/) | Applications of the implemented methods to data with realistic characteristics. |
| [`replications_with_real_dataset/`](replications_with_real_dataset/) | Reproductions and evaluations using real-world datasets instead of simulated data. |
| [`core_ppg/`](core_ppg/) | Core components and pipelines dedicated to photoplethysmography (PPG) signals. |
| [`soh_estimation/`](soh_estimation/) | Research on applying NTSA to State of Health (SOH) estimation. |
| [`test/`](test/) | Notebooks and tests for validating implementations and scientific invariants. |
| `.venv/` | Local Python environment; not part of the research content. |

### Project-level Files

| File | Purpose |
|---|---|
| [`requirements.txt`](requirements.txt) | Dependencies required to reproduce the Python environment. |
| [`standard_note.md`](standard_note.md) | Shared conventions for notes, designs, and implementations. |
| [`README.md`](README.md) | Overview of the repository's goals, scope, and structure. |

## 🧩 Organizational Principles

- **Paper first, code second:** every implementation should be traceable to the
  formulas and assumptions in the original publication.
- **Separate core algorithms from experiments:** reusable algorithms belong in
  `core_ntsa/`, while parameters and plotting belong in experiment notebooks.
- **Correctness first:** clear reference implementations take priority over
  performance optimization.
- **Reproducibility:** paper-specified parameters must be distinguished from
  choices introduced by the reproduction.
- **Scientific validation:** each algorithm should be checked using examples
  from the paper, range invariants, or corresponding mathematical properties.

## 🚀 Getting Started

Create a Python environment and install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

A recommended order for exploring the project is:

```text
summary_paper
    → algorithm_design
    → core_ntsa
    → experiment_design
    → paper_replications
    → replications_with_real_dataset
```

## 📌 Project Status

The project is being developed paper by paper across the five research
directions. Some modules or notebooks may still be in the design, validation,
or reproduction stage. Results should therefore be checked against the
original publications before being used in real-world applications.
