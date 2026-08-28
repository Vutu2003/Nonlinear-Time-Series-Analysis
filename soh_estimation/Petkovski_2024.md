# Petkovski et al., Energies 2024 — Core Notes & Gap for GSI

## 1. Scope
Đề xuất phương pháp ước lượng SOH từ dữ liệu partial discharge bằng:

partial/full discharge Q(V)
→ reference cycle 10
→ difference curve
→ handcrafted features + temperature
→ SVR
→ SOH.

Ba feature chính:
- Ftr1: log-variance của difference curve;
- Ftr2: log-minimum của difference curve;
- Ftr3: cumulative temperature.

Dataset: 124 cell LFP Toyota–MIT–Stanford. :contentReference[oaicite:0]{index=0}

---

## 2. Research gap của chính nghiên cứu
Paper xuất phát từ hai vấn đề:

1. Full discharge data khó có trong thực tế vì battery thường không được discharge hết toàn bộ voltage range.
2. Cần một SOH estimator có:
   - accuracy tốt;
   - computational burden thấp hơn deep learning;
   - khả năng dùng partial discharge data.

Ngoài ra, hiệu quả của feature có thể thay đổi theo voltage interval nên cần đánh giá rõ window dependence. :contentReference[oaicite:1]{index=1}

## 3. Research question
Có thể diễn giải RQ chính là:

> Có thể dùng các feature đơn giản được xây từ partial discharge capacity curves để ước lượng SOH chính xác bằng SVR hay không?

RQ phụ:

> Feature nào và voltage interval nào duy trì được SOH information tốt nhất khi chuyển từ full discharge sang partial discharge?

---

## 4. Main results
- Full voltage range 2–3.4 V:
  - mean test R² ≈ 0.962.
- Partial voltage ranges:
  - phần lớn đạt mean test R² ≈ 0.939–0.973.
- Một số vùng điện áp cao như 3.15–3.4 V và 3.25–3.4 V cho kết quả kém.
- 109 cell train/validation, 15 unseen cells dùng test. :contentReference[oaicite:2]{index=2}

---

# Gap còn lại liên quan đến GSI

## Gap 1 — Reference-based feature không còn mới
Petkovski đã dùng:

Q_k(V) - Q_10(V)

để biểu diễn degradation relative to an early reference cycle.

Do đó, novelty của GSI không nên dựa vào:
- “dùng reference cycle”;
- “dùng difference feature”.

GSI cần nhấn mạnh vào:
- ultra-low-dimensional geometry;
- fixed Head–Tail representation;
- ΔGSI để giảm cell-specific offset;
- khả năng transfer mà không cần nhiều curve statistics.

---

## Gap 2 — Representation vẫn tương đối phức tạp
Petkovski cần:
- toàn bộ partial Q(V) curve;
- interpolation;
- curve subtraction;
- variance/minimum statistics;
- cumulative temperature;
- SVR.

GSI chỉ cần:

V_H, V_T
→ GSI
→ ΔGSI
→ linear regression.

→ GSI có tiềm năng giảm feature dimensionality, preprocessing và model complexity.

---

## Gap 3 — Window dependence rõ rệt
Paper cho thấy feature effectiveness thay đổi mạnh theo voltage interval.

Một feature tốt ở full range có thể thất bại ở partial range.

Điều này cho thấy:

feature quality
≠
independent of region.

GSI cần chứng minh:
- Head/Tail region nằm trong một stable sensitivity basin;
- geometry được chọn trên source data rồi freeze;
- không cần re-select window trên target cell/dataset.

---

## Gap 4 — Generalization mới ở mức unseen-cell trong cùng dataset
Petkovski có legitimate held-out-cell testing:

109 cells
→ train/validation

15 unseen cells
→ test.

Nhưng chưa chứng minh:
- cross-dataset transfer;
- cross-chemistry transfer;
- frozen feature geometry across domains.

GSI nên nhắm:

nested LOCO
+ frozen Head/Tail
+ external dataset transfer.

---

## Gap 5 — Outlier cells vẫn gây failure
Hai test cells T4 và T13 có R² thấp hơn rõ rệt vì degradation trajectory khác phần lớn training cells.

Điều này cho thấy:

good average unseen-cell performance
≠
robustness to atypical degradation trajectories.

GSI nên kiểm tra:
- cell-wise error distribution;
- worst-case cells;
- whether ΔGSI reduces inter-cell trajectory dispersion.

---

## Gap 6 — Physical interpretation còn yếu
Petkovski giải thích feature chủ yếu dựa trên thay đổi của Q(V) curve theo aging.

Chưa có:
- ICA/DVA validation;
- degradation-mode attribution;
- direct physical diagnostics.

GSI có thể mạnh hơn nếu Head/Tail regions được support bởi ICA/DVA evolution.

---

## Gap 7 — Computational cost mới chỉ được claim định tính
Paper chọn SVR vì cho rằng có trade-off tốt giữa:
- accuracy;
- applicability;
- computational burden;
- interpretability.

Nhưng không có benchmark rõ về:
- latency;
- memory;
- model size;
- embedded hardware.

GSI nên benchmark end-to-end để chứng minh lợi thế của one-scalar + LR.

---

# Core contrast với GSI

Petkovski:

partial Q(V)
+ reference curve subtraction
+ statistical features
+ temperature
+ SVR

GSI:

partial Q–V geometry
+ BOL normalization
+ one scalar
+ linear regression.

Câu hỏi còn mở mà GSI có thể trả lời:

> Liệu một descriptor hình học cực kỳ tối giản, được cố định và reference-normalized, có thể giữ đủ aging information để generalize sang unseen cells/datasets mà không cần curve statistics, temperature feature hay nonlinear SVR hay không?