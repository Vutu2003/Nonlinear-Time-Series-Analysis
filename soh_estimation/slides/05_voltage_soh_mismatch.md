# Same SOH does not guarantee the same voltage trajectory

## Core message
Cell-to-cell voltage-profile mismatch at the same SOH is a representation-level obstacle, not merely a regression-model problem.

## Slide content

$$
SOH_a=SOH_b
\nRightarrow
V_a(Q)=V_b(Q)
$$

**Observed challenge**

- Partial voltage/IC curves can differ across cells at comparable SOH.
- A voltage-only mapping may therefore mix aging information with cell-specific offsets or trajectory deformation.

**Literature response:** Chen 2025 adds accumulated operation histograms to the partial profile.

**GSI hypothesis:** BOL referencing may reduce—rather than assume away—the mismatch inside the representation.

## Evidence from literature

- Chen et al. 2025 — explicit SOH–voltage mismatch and multi-modal compensation.
- Yao & Chen 2025 — feature shift, mapping shift, and model mismatch are not fully isolated across domains.
- Petkovski 2024 — atypical degradation trajectories produce weak cell-wise results despite good averages.

## Gap / limitation

The notes do not establish that BOL subtraction alone removes the mismatch, and a single reference measurement may also propagate reference noise.

## Link to GSI

Test whether $\Delta GSI$ reduces intercept spread and trajectory dispersion, while comparing one-cycle BOL against a $K$-cycle averaged reference.

## Source traceability

- `Junran_Chen_2025.md` → same-SOH voltage/IC mismatch and histogram fusion.
- `Chen_2025.md` → distinction among feature, mapping, and model shifts.
- `Petkovski_2024.md` → outlier test-cell trajectories.
- `Kang_2024.md` → possible propagation of BOL-reference noise and $K$-cycle reference idea.

## Presenter notes

- Đây là lý do representation cần được đánh giá trước model.
- Chen giải quyết bằng thêm nguồn dữ liệu lịch sử; GSI thử một hướng nhẹ hơn là within-cell reference.
- Không được nói $\Delta GSI$ đã giải quyết mismatch trước khi có dispersion và LOCO evidence.
- Cần test reference trung bình vì lỗi ở BOL có thể đi theo toàn bộ trajectory.
