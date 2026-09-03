# Why this literature audit matters

## Core message
A broad “simple geometric feature” novelty claim would overlap substantially with established partial-profile methods.

## Slide content

**Already demonstrated**

- Partial charge/discharge profiles can support SOH estimation.
- Finite $\Delta V$, curve geometry/distance, and reference comparisons already exist.
- Derivative-free and lightweight partial-profile indicators already exist.

**Therefore, GSI must be judged on**

$$
\boxed{
\text{minimality}
+\text{frozen transferability}
+\text{low adaptation burden}
+\text{measured end-to-end cost}
}
$$

## Evidence from literature

- Naha 2020; Chen et al. 2024 — finite voltage differences are already used.
- Qin 2024; Yao & Chen 2025 — geometric/distance features are already used.
- Petkovski 2024 — early-cycle reference subtraction is already used.
- Jenu 2022 — integrated voltage is derivative-free and intended for practical partial charging.

## Gap / limitation

Prior-art overlap rules out novelty arguments based on any one primitive alone, while the combined question of one fixed scalar, strict transfer, and quantified total cost remains insufficiently established.

## Link to GSI

The audit turns GSI from a feature-naming exercise into a falsifiable representation-and-validation problem.

## Source traceability

- `Naha_2020.md` → nine local finite $\Delta V$ features.
- `Kang_2024.md` → fixed-time voltage difference among four features.
- `Qin_2024.md` → three relative geometric features and self-scaling.
- `Chen_2025.md` → Shapelet distance and reference-pattern selection.
- `Petkovski_2024.md` → $Q_k(V)-Q_{10}(V)$.
- `Jenu_2022.md` → derivative-free integrated voltage.

## Presenter notes

- Slide này đặt “novelty boundary” trước khi nói về GSI.
- Không nên claim “first geometric”, “first reference-based”, hay “first lightweight”.
- Giá trị tiềm năng nằm ở tổ hợp representation tối giản và protocol transfer nghiêm ngặt.
- Mọi claim cuối cùng phải phụ thuộc vào kết quả validation, không vào tên feature.
