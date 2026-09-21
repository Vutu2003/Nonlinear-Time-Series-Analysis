# Chen_2025

# Yao & Chen, Energy 2025 — Gap & Contrast với GSI

## 1. Research motivation

Paper nhắm tới hai vấn đề:

$$
\text{interpretability}
+
\text{cross-chemistry / cross-condition applicability}
$$

Existing SOH features/models thường được phát triển dưới chemistry hoặc operating condition cụ thể nên có thể suy giảm performance khi domain thay đổi.

Paper đề xuất:

$$
\text{Shapelet distance feature}
+
\text{transfer learning}
+
\text{dynamic model weighting}
$$

để thích nghi với target domain.

---

## 2. Research-gap nuance

Claim:

> interpretable features may not generalize well across chemistry/conditions.

Nhưng cần phân biệt:

$$
\text{feature shift}
+
\text{mapping shift}
+
\text{model mismatch}
$$

Paper không isolate hoàn toàn ba nguồn lỗi này.

Do đó evidence phù hợp hơn với:

> Existing feature–model pipelines remain domain-dependent.

Không nên diễn giải mạnh thành:

> Interpretable features themselves are intrinsically non-transferable.

---

## 3. Generalization trong paper thực chất là gì?

### Feature-level transferability
Evidence: **yếu–trung bình**

Feature extractor không hoàn toàn frozen:
- sliding-window length/step được optimize theo từng domain;
- RefShapelet được chọn bằng:

$$
RefShapelet=
\arg\max |PCC(DF,SOH)|
$$

=> cần labeled data và domain-specific feature selection.

### Mapping-level invariance
**Không được chứng minh.**

Model source không được dùng nguyên trạng:

$$
\text{source pre-training}
\rightarrow
\text{target fine-tuning}
$$

### Model-level transfer
**Có evidence**, nhưng là transfer learning với labeled target data.

### Framework-level adaptability
Đây là claim được support mạnh nhất:

> cùng một Shapelet + TL framework có thể được re-adapt cho nhiều chemistry/condition.

---

## 4. Target-domain adaptation burden

Training protocol:

$$
\text{source domain}
\rightarrow
\text{pre-train}
\rightarrow
\text{first target-domain battery}
\rightarrow
\text{fine-tune}
\rightarrow
\text{test remaining cells}
$$

Do đó:

$$
\boxed{\text{không phải zero-shot transfer}}
$$

Paper cần aging data của ít nhất một target battery.

Nhưng paper không trả lời:

> Cần tối thiểu bao nhiêu target cycles để đạt accuracy tốt?

Đây là gap application quan trọng cho GSI.

---

## 5. Feature representation vẫn domain-dependent

Hai distance features:

- minED
- VMED

không có một feature consistently tốt nhất trên mọi domain.

$$
\text{minED better in some cases}
$$

$$
\text{VMED better in others}
$$

VMED còn suy giảm khi aging trajectory không dịch chủ yếu theo vertical direction.

Insight:

$$
\boxed{
\text{geometric aging deformation itself may depend on chemistry/condition}
}
$$

Do đó:

> same distance-feature concept không đồng nghĩa với one universally stable representation.

---

## 6. Computational burden

Paper có quantitative computational benchmark.

Model-level:
- DWM-TL training/fine-tuning ≈ 180 s;
- testing rất nhanh ≈ 0.016 s.

Nhưng feature pipeline mới là phần nặng:

$$
\text{GP optimization}
+
\text{sliding-window search}
+
\text{RefShapelet selection}
+
\text{distance calculation}
$$

Example:

- minED GP optimization: ≈ 6 h 23 min;
- VMED GP optimization: ≈ 14 min;
- minED feature extraction: ≈ 5 min 46 s;
- VMED feature extraction: ≈ 18 s.

Insight:

$$
\text{feature-development cost}
\gg
\text{final inference cost}
$$

=> Computational efficiency phải benchmark end-to-end, không chỉ prediction latency.

---

## 7. Contrast trực tiếp với GSI

### Yao & Chen

$$
\text{domain-specific window optimization}
+
\text{supervised RefShapelet selection}
+
\text{distance feature}
+
\text{target-domain fine-tuning}
+
\text{4-model ensemble}
$$

### GSI hypothesis

$$
\text{source-selected fixed Head/Tail}
+
\text{single scalar}
+
\text{BOL normalization}
+
\text{linear mapping}
+
\text{zero/few-shot target adaptation}
$$

Core contrast:

$$
\boxed{
\text{Yao: adapt feature + adapt model}
}
$$

vs.

$$
\boxed{
\text{GSI: stabilize representation to minimize adaptation}
}
$$

---

## 8. Motivation cho experiment GSI

### A. Frozen feature transfer

$$
\text{select Head/Tail on source}
\rightarrow
\text{freeze geometry}
\rightarrow
\text{apply to unseen target}
$$

Nếu tốt:

> chứng minh feature-level transferability thực sự.

Nếu reselect Head/Tail trên target:

> chỉ chứng minh framework applicability.

### B. Target-cycle adaptation burden

Sweep:

$$
K=0,1,3,5,10,20,\ldots
$$

với $K$ = số labeled target cycles dùng calibration.

Report:

$$
RMSE(K),\ MAE(K),\ R^2(K)
$$

và:

$$
K_{95}
=
\min K:
\text{performance reaches 95\% of adapted optimum}
$$

Potential contribution:

> GSI requires substantially less target-domain calibration than adaptive feature/model frameworks.

### C. One-representation test

Kiểm tra cùng một frozen Head/Tail geometry trên:
- unseen cells;
- external dataset;
- different conditions nếu có.

Mục tiêu:

$$
\text{one descriptor}
\rightarrow
\text{multiple domains}
$$

thay vì cần minED/VMED hoặc domain-specific feature tuning.

### D. End-to-end computational benchmark

Bao gồm:
- Head/Tail discovery cost;
- feature extraction latency;
- calibration cost;
- LR inference;
- memory/model size.

Không chỉ report inference latency.

---

## 9. Gap còn lại mà GSI có thể khai thác

> Whether a single, fixed, capacity-defined geometric descriptor can preserve sufficient aging information across unseen cells while substantially reducing feature re-selection and target-domain adaptation remains insufficiently established.

Potential stronger contribution:

> BOL normalization of a fixed Head–Tail descriptor reduces cell-specific offsets sufficiently to enable accurate SOH estimation with minimal target-cell calibration.

---

## Verdict for GSI

- Raw geometric-feature threat: **High**
- Reference/distance concept threat: **Moderate–High**
- ΔGSI exact-formulation threat: **Moderate**
- Feature-transferability threat: **Moderate**
- Model-generalization threat: **Low–Moderate**
- Adaptation-framework threat: **High**
- Complexity benchmark relevance: **Very High**

Main lesson:

$$
\boxed{
\text{GSI không cần thắng bằng feature novelty;}
\\
\text{GSI cần thắng bằng representation stability + low adaptation burden + simplicity.}
}
$$

---

# Jenu_2022

## Jenu et al., 2022 — Partial Charging SOH Estimation

### Research gap

ICA có khả năng phân tích degradation tốt nhưng:

- thường cần low C-rate;
- nhạy với measurement noise;
- cần filtering;
- khó áp dụng online trong điều kiện thực tế.

=> Nghiên cứu kiểm tra ICA và Integrated Voltage (IV) trên partial charging ở C/3, 1C, 2C. :contentReference[oaicite:0]{index=0}

### Phương pháp

#### ICA

$$
IC=\frac{dQ}{dV}
$$

Theo dõi peak height / area / position.

Physical interpretation:

$$
\text{IC peak evolution}
\leftrightarrow
\text{electrochemical degradation}
$$

Peak decrease được liên hệ với LLI/LAM; peak shift có thể liên quan tới tăng resistance. :contentReference[oaicite:1]{index=1}

Nhược điểm:

$$
\text{differentiation}
\rightarrow
\text{noise amplification}
\rightarrow
\text{filtering required}
$$

:contentReference[oaicite:2]{index=2}

#### Integrated Voltage

$$
IV=\int_{t_1}^{t_2}V(t)\,dt
$$

trên predefined voltage range.

Ưu điểm:
- derivative-free;
- đơn giản;
- không cần heavy computation;
- phù hợp partial charging/BMS. :contentReference[oaicite:3]{index=3}

### Kết quả chính

- ICA accuracy giảm rõ khi C-rate tăng.
- Với LFP, ICA bắt đầu scatter từ khoảng 1C.
- IV ít nhạy với C-rate hơn, RMSE < 2% tới 2C.
- IV vẫn phụ thuộc mạnh vào voltage-range selection, đặc biệt với LFP. :contentReference[oaicite:4]{index=4}

### Liên hệ với GSI

Jenu:

$$
\text{ICA: derivative + filtering}
$$

hoặc

$$
\text{IV: integration trên predefined voltage range}
$$

GSI:

$$
\text{regional averaging}
+
\text{finite }\Delta V
+
\text{derivative-free}
+
1\text{ scalar}
$$

### Motivation tiềm năng cho GSI

Kiểm tra liệu GSI có thể:

- ít nhạy noise hơn ICA;
- ít phụ thuộc exact voltage range hơn IV;
- giữ accuracy ở higher C-rate;
- cung cấp physical interpretation thông qua ICA/DVA;
- đạt complexity thấp với representation tối giản.

### Lưu ý novelty

Không nên claim:

> first derivative-free / lightweight partial-voltage SOH method

vì IV đã có.

Potential distinction của GSI nằm ở:

$$
\boxed{
\text{capacity-defined geometry}
+
\Delta GSI
+
\text{robustness}
+
\text{generalization}
+
\text{minimal representation}
}
$$

---

# Junran_Chen_2025

# Chen et al., Applied Energy 2025 — Liên hệ với GSI

## Ý chính
- Đề xuất multi-modal fusion:
  partial voltage profile + histogram vận hành → SOH.
- Mục tiêu: bù nhược điểm của từng nguồn dữ liệu.
- Kết quả tốt nhất: RMSPE 0.74%, giảm lỗi tới ~42%, và cần ít training cells hơn histogram-only khoảng 60%.

## Gap liên quan đến GSI

1. **SOH–voltage mismatch**
   - Cùng SOH nhưng voltage/IC curve giữa các cell có thể khác nhau.
   - Chen xử lý bằng cách thêm histogram.
   - GSI hướng tới giảm mismatch ngay trong voltage representation bằng ΔGSI/BOL normalization.

2. **Phụ thuộc nhiều nguồn dữ liệu**
   - Chen cần partial profile + accumulated histogram history.
   - GSI chỉ cần partial-discharge trajectory + BOL reference.
   - → GSI có tiềm năng giảm data/history/storage burden.

3. **Window sensitivity**
   - Chen cho thấy vị trí và độ dài partial window ảnh hưởng mạnh đến accuracy.
   - GSI cần chứng minh Head/Tail region ổn định và transferable khi freeze sang unseen cells/dataset.

4. **Generalization**
   - Chen có unseen-cell testing trong từng dataset.
   - Chưa chứng minh frozen cross-dataset/cross-chemistry transfer.
   - GSI nên nhắm strict LOCO + frozen feature geometry + external transfer.

5. **Physical interpretation**
   - Chen chủ yếu giải thích ở mức phenomenological; final CNN/FNN vẫn khó diễn giải.
   - GSI có thể mạnh hơn nếu Head/Tail regions được support bằng ICA/DVA.

6. **Computational cost**
   - Chen đã benchmark trên Jetson Nano (~15.6 ms, ~1.97 MB).
   - GSI cần benchmark end-to-end để chứng minh lợi thế của one-scalar + linear regression.

---

# Kang_2024

# Chen et al., 2024 — Research Gap & Research Question

# Research gap

Các phương pháp SOH hiện tại còn gặp:

- dữ liệu pin nhiễu / thiếu / không chính xác;
- feature selection và dimensionality reduction có thể tốn tài nguyên tính toán;
- khó đồng thời học được short-term patterns và long-term dependencies;
- accuracy và robustness dưới fast-charging vẫn còn hạn chế.

Ngoài ra:
- direct methods cần thiết bị / điều kiện đo phức tạp;
- model-based methods cần prior knowledge và parameter estimation khó.

### Research question

> Có thể cải thiện SOH estimation dưới fast-charging bằng cách kết hợp
> nhiều health features với một hybrid deep model có khả năng học cả
> local patterns và long-term dependencies hay không?

### Giải pháp đề xuất

$$
\text{4 handcrafted features}
+
\text{1D-CNN}
+
\text{CSAM}
+
\text{LSTM}
+
\text{Multi-head Attention}
\rightarrow
\text{TFMN}
$$

Mục tiêu chính:

$$
\boxed{\text{tăng accuracy + robustness dưới fast charging}}
$$

### Liên hệ với GSI

Chen đi theo hướng:

$$
\text{complex battery dynamics}
\rightarrow
\text{multi-feature + complex model}
$$

GSI có thể đặt câu hỏi ngược lại:

$$
\boxed{
\text{Có thể đạt accuracy/robustness tương đương bằng một scalar feature + model đơn giản không?}
}
$$

## Chen et al., 2024 — Feature Extraction & Liên hệ với GSI

### 4 health features

1. Khoảng thời gian tại cùng khoảng điện áp:

$$
\Delta V=\text{const.}
\rightarrow
T_i=t_{i,end}-t_{i,start}
$$

2. Độ chênh điện áp tại cùng khoảng thời gian:

$$
\Delta t=\text{const.}
\rightarrow
\Delta V_i=V_{i,start}-V_{i,end}
$$

3. Tích phân biến thiên điện áp:

$$
C_n=\int_{T_n}^{T_{n+1}}V(t)dt-V_n\Delta T_n
$$

4. Vị trí đỉnh IC:

$$
Q_{peak}=\arg\max\left(\frac{dQ}{dV}\right)
$$

Các feature có $|r|\approx0.86-0.94$ với SOH trên các cell đại diện. :contentReference[oaicite:0]{index=0}

### Liên hệ với GSI

Chen:

$$
\text{nhiều descriptor của trajectory}
\rightarrow
\text{deep feature fusion}
$$

GSI:

$$
\text{một regional }\Delta V\text{ theo capacity}
\rightarrow
\text{model đơn giản}
$$

Đặc biệt:

$$
\boxed{
\text{Chen: fixed }\Delta t \rightarrow \Delta V
}
$$

vs.

$$
\boxed{
\text{GSI: Head/Tail theo capacity} \rightarrow \Delta V
}
$$

=> Primitive $\Delta V$ không mới; khác biệt nằm ở cách định nghĩa region/coordinate và mức độ tối giản.

### Motivation tiềm năng cho GSI

> Có thực sự cần nhiều handcrafted features + deep model để khai thác aging trajectory,
> hay một scalar geometric descriptor đã đủ?

Tiềm năng claim:

$$
\boxed{
\text{representation tối giản}
+
\text{chi phí tính toán thấp}
+
\text{accuracy/robustness tương đương}
}
$$

## Robustness experiment tiềm năng cho GSI

### 1. Nhiễu điện áp

Thêm noise vào raw voltage:

$$
V'(Q)=V(Q)+\epsilon
$$

với nhiều mức noise, sau đó đánh giá:

- sai lệch của $GSI$ và $\Delta GSI$;
- $R^2$, RMSE, MAE của SOH estimation.

Chen 2024 chỉ kiểm tra prediction dưới noise 50/100/150 mV; GSI có thể đánh giá thêm trực tiếp độ ổn định của feature. :contentReference[oaicite:0]{index=0}

### 2. Tiềm năng chống nhiễu của GSI

GSI dùng trung bình trong Head/Tail:

$$
V_H=\frac{V_{H1}+V_{H2}}{2},
\qquad
V_T=\frac{V_{T1}+V_{T2}}{2}
$$

nên có hypothesis:

$$
\text{regional averaging}
\rightarrow
\text{giảm random measurement noise}
$$

Cần kiểm chứng bằng thực nghiệm.

### 3. Robustness của $\Delta GSI$

$$
\Delta GSI_t=GSI_t-GSI_0
$$

Tiềm năng:

$$
\text{loại bỏ static cell/bias offset}
\rightarrow
\text{trajectory ổn định hơn}
$$

Tuy nhiên noise tại $GSI_0$ có thể truyền sang mọi cycle.

=> Test thêm reference trung bình:

$$
GSI_{ref}=\frac{1}{K}\sum_{k=1}^{K}GSI_k
$$

thay vì chỉ dùng cycle đầu.

### 4. Sampling robustness

Downsample dữ liệu:

$$
1\,Hz
\rightarrow
0.5
\rightarrow
0.2
\rightarrow
0.1\,Hz
$$

và kiểm tra feature/performance degradation.

### 5. Region robustness

Perturb:

- voltage region;
- Head/Tail positions.

Mục tiêu tìm:

$$
\boxed{\text{broad stable region}}
$$

thay vì một sharp optimum.

### Potential claim

Nếu GSI/$\Delta GSI$ duy trì ổn định dưới noise, downsampling và region perturbation:

$$
\boxed{
\text{simple averaging}
+
\text{reference normalization}
\rightarrow
\text{robust low-dimensional SOH feature}
}
$$

Đặc biệt nên tách:

$$
\text{feature robustness}
\rightarrow
\text{prediction robustness}
$$

thay vì chỉ báo cáo prediction error như Chen.

## Chen et al., 2024 — Gaps tiềm năng cho GSI

### 1. Generalization

Chen sử dụng nhiều datasets nhưng chủ yếu train/test riêng trong từng dataset.

=> Chưa chứng minh rõ:

$$
\text{feature/model transferability across datasets}
$$

Tiềm năng GSI:

$$
\boxed{
GSI/\Delta GSI
\text{ duy trì quan hệ ổn định với SOH giữa các cell/dataset}
}
$$

### 2. Computational cost

TFMN gồm:

$$
\text{1D-CNN + CSAM + LSTM + Attention}
$$

nhưng không định lượng rõ:

- inference time;
- parameter count;
- FLOPs/MACs;
- memory footprint.

=> GSI có thể chứng minh trực tiếp:

$$
\boxed{\text{accuracy–complexity trade-off}}
$$

với scalar feature + linear model.

### 3. Physical interpretation

Chen có giải thích feature ở mức phenomenological, nhưng chưa xây dựng
mechanistic linkage rõ ràng; TFMN vẫn mang tính black-box.

=> GSI có thể tăng interpretability bằng:

$$
\text{ICA/DVA}
\leftrightarrow
\text{local }V(Q)\text{ evolution}
\leftrightarrow
GSI/\Delta GSI
$$

### 4. Robustness

Chen chủ yếu kiểm tra noise robustness của prediction.

=> GSI có thể mở rộng thành:

$$
\boxed{
\text{noise}
+
\text{sampling}
+
\text{region sensitivity}
}
$$

và tách:

$$
\text{feature robustness}
\rightarrow
\text{prediction robustness}
$$

---

# Li_2024

## Li et al., 2024 — Interval Voltage Features

### Research gap

Các phương pháp dùng toàn bộ charge/discharge profile:

- tốn thời gian;
- khó đáp ứng real-time;
- không phù hợp đánh giá SOH nhanh trong ứng dụng thực tế.

=> Đề xuất dùng partial discharge region để trích feature. :contentReference[oaicite:0]{index=0}

### Phương pháp

Phân tích:

$$
\frac{dV}{dt}
$$

trên discharge profile và chọn một voltage region có aging sensitivity cao.

NASA:

$$
2.9-3.4\,V
$$

Oxford:

$$
2.8-3.5\,V
$$

Ba features:

$$
HF_1=\int \frac{dV}{dt}dV
$$

$$
HF_2=\text{mean}\left(\frac{dV}{dt}\right)
$$

$$
HF_3=
\left|
\left.\frac{dV}{dt}\right|_{V_{high}}
-
\left.\frac{dV}{dt}\right|_{V_{low}}
\right|
$$

:contentReference[oaicite:1]{index=1}

Oxford cần Gaussian smoothing do $dV/dt$ rất noisy. :contentReference[oaicite:2]{index=2}

### Modeling

$$
3\,HF
\rightarrow
HPO\text{-}OS\text{-}ELM
\rightarrow
SOH
$$

OS-ELM được chọn vì sequential learning và giảm computational burden;
HPO tối ưu weights/bias để tăng accuracy. :contentReference[oaicite:3]{index=3}

### Generalization

NASA:

$$
70\%\text{ đầu mỗi cell}
\rightarrow
30\%\text{ cuối cùng cell}
$$

=> chủ yếu same-cell temporal prediction.

Oxford:

$$
\text{train Cell1}
\rightarrow
\text{test Cell3/7/8}
$$

=> có cross-cell transfer nhưng chưa systematic LOCO / cross-dataset transfer. :contentReference[oaicite:4]{index=4}

### Liên hệ với GSI

Li:

$$
\text{partial discharge}
+
dV/dt
+
\text{smoothing}
+
3\,features
+
ML
$$

GSI:

$$
\text{partial discharge}
+
\text{derivative-free regional }\Delta V
+
1\,scalar
+
\text{linear model}
$$

=> Regional partial-discharge feature không mới.

### Gaps tiềm năng cho GSI

- **Derivative/noise:** Li cần differentiation + smoothing.
- **Complexity:** có nói giảm computational burden nhưng chưa benchmark rõ runtime/FLOPs/memory.
- **Generalization:** chưa strict LOCO/cross-dataset feature-transfer analysis.
- **Physical interpretation:** chủ yếu phenomenological, chưa có mechanistic linkage trực tiếp.

### Potential GSI angle

$$
\boxed{
\text{derivative-free}
+
\text{minimal representation}
+
\text{noise robustness}
+
\text{strict generalization}
+
\text{quantified low computational cost}
}
$$

---

# Naha_2020

## Research gap

Các phương pháp SOH trước đó vẫn gặp nhiều hạn chế khi triển khai online trong BMS:

- một số phương pháp cần lượng training data lớn và phải bao phủ toàn bộ SOH range;
- một số cần full charge/discharge profile;
- một số cần probing signal hoặc special test;
- một số sử dụng cycle number;
- model-based methods phụ thuộc vào battery model và model parameters;
- một số phương pháp chỉ phù hợp cho offline estimation.

Trong thực tế, battery usage thường tạo ra partial và random charge/discharge data,
do đó full profile không phải lúc nào cũng có sẵn.

=> Gap chính: thiếu một phương pháp SOH estimation có thể hoạt động online,
chính xác, sử dụng normal partial charging data và có training-data requirement vừa phải.

## Research question

Có thể estimate SOH chính xác từ một đoạn partial charging ngắn trong điều kiện sử dụng bình thường,
mà không cần full charge/discharge profile, cycle number, absolute SOC hoặc lượng training data rất lớn hay không?

Sub-question 1:
Có thể xây dựng một health-sensitive feature từ các thay đổi cục bộ của charging voltage curve hay không?

Sub-question 2:
Có thể train estimator cho SOH range rộng chỉ từ khoảng 400 cycles đầu tiên,
thay vì cần dữ liệu aging toàn vòng đời hay không?

## Design of feature vector

### Core idea

Naha et al. giả định một simplified battery model:

$$
R_i = R_f + \Delta R_{sei}
$$

và xây dựng điện áp hiệu chỉnh:

$$
v_{sei}(k)=v(k)-R_fi(k)
$$

để giảm ảnh hưởng của CC charging rate lên voltage feature.

### Physical rationale

Authors quan sát voltage–SOC curve thay đổi khi SOH giảm.

Họ diễn giải:

$$
\text{LAM / LLI}
\rightarrow
\text{horizontal shrinkage}
$$

$$
\text{internal resistance increase}
\rightarrow
\text{vertical shrinkage}
$$

Do đó voltage trajectory được xem là chứa aging information.

### Feature construction

Một điểm bắt đầu $v_{sei,0}$ được cố định.

Các điểm tiếp theo được chọn sau mỗi Coulomb-count increment:

$$
\Delta Q_c = 1.5\%C_{\max}
$$

Tổng cộng 10 điểm $v_{sei}$ được lấy.

Sau đó:

$$
\Delta v_{sei,k}
=
v_{sei,k}-v_{sei,k-1}
$$

với:

$$
k=1,\ldots,9
$$

Feature vector là:

$$
\mathbf{x}
=
[
\Delta v_{sei,1},
\ldots,
\Delta v_{sei,9},
T_{avg}
]
$$

### Relation to GSI

Naha:

$$
\text{capacity-indexed voltage samples}
\rightarrow
\text{multiple successive }\Delta V
$$

GSI:

$$
\text{capacity-defined Head/Tail regions}
\rightarrow
\text{single regional }\Delta V
$$

=> Hai phương pháp khai thác cùng family thông tin hình học của voltage trajectory,
nhưng Naha giữ nhiều local finite differences trong khi GSI nén thành một scalar.

### Important implication for GSI

Naha chủ động hiệu chỉnh voltage bằng $R_fi$ để giảm ảnh hưởng của charging rate.

GSI dùng raw terminal voltage, vì vậy cần kiểm tra:

- C-rate/current sensitivity;
- resistance/polarization contribution;
- whether observed GSI evolution is truly aging-related or partly operating-condition dependent.

### Physical clue

Paper gợi ý chain:

$$
\text{battery aging}
\rightarrow
\text{LAM / LLI / resistance increase}
\rightarrow
\text{voltage-curve evolution}
\rightarrow
\Delta v_{sei}\text{ evolution}
$$

Tuy nhiên đây chủ yếu là model/literature-based interpretation,
không phải direct measurement of degradation modes.

# Diễn giải vật lý: Aging và sự thay đổi của Voltage Trajectory

### Quan sát chính

Naha et al. quan sát rằng đường cong voltage–SOC thay đổi có hệ thống khi SOH giảm.

Paper mô tả sự thay đổi này theo hai hướng chính:

$$
\text{horizontal shrinkage}
$$

và:

$$
\text{vertical shrinkage}
$$

### Horizontal change

Authors liên hệ sự co lại theo trục SOC/capacity với:

$$
\text{loss of active material}
$$

và:

$$
\text{loss of lithium inventory}
$$

Ý nghĩa hình học là khi battery mất khả năng lưu trữ điện tích,
usable capacity range giảm và voltage trajectory bị nén theo phương ngang.

Có thể biểu diễn khái niệm:

$$
\text{capacity-related degradation}
\rightarrow
\text{change in horizontal extent of }V(Q)
$$

### Vertical change

Authors liên hệ sự thay đổi theo trục voltage với sự gia tăng internal resistance.

Simplified model:

$$
R_i = R_f + \Delta R_{sei}
$$

trong đó:

- $R_f$ là phần resistance được giả định không đổi theo aging;
- $\Delta R_{sei}$ là phần resistance tăng thêm liên quan đến SEI growth.

Do terminal voltage phụ thuộc vào current và resistance, resistance growth làm
voltage trajectory thay đổi theo phương điện áp.

Conceptually:

$$
\text{resistance growth}
\rightarrow
\text{vertical modification of }V(Q)
$$

### Combined interpretation

Naha cung cấp một cách diễn giải tổng quát:

$$
\text{battery aging}
\rightarrow
\begin{cases}
\text{capacity-related changes}\\
\text{resistance-related changes}
\end{cases}
\rightarrow
\text{evolution of voltage trajectory}
$$

Do đó, các đại lượng hình học được trích xuất từ voltage trajectory có thể
thay đổi theo SOH.

### Connection to finite voltage differences

Khi shape và position của voltage trajectory thay đổi theo aging,
voltage separation giữa các vị trí trên curve cũng thay đổi.

Do đó:

$$
\text{voltage-trajectory evolution}
\rightarrow
\text{change in finite }\Delta V
$$

Đây là physical motivation cho việc Naha sử dụng:

$$
\Delta v_{sei,k}
=
v_{sei,k}-v_{sei,k-1}
$$

làm health-sensitive features.

### Relevance to GSI

GSI cũng là một finite regional voltage difference:

$$
GSI = V_H-V_T
$$

Do đó có thể xây dựng chain diễn giải:

$$
\text{aging}
\rightarrow
\text{capacity/resistance-related changes}
\rightarrow
\text{evolution of }V(Q)
\rightarrow
\text{change in regional voltage geometry}
\rightarrow
\text{change in GSI}
$$

### Safe interpretation for GSI

GSI nên được diễn giải là một descriptor hình học nhạy với
aging-induced evolution của voltage–capacity trajectory.

Một cách nói an toàn:

> Battery aging alters the voltage trajectory through combined
> capacity-related and resistive effects. GSI is therefore interpreted
> as a compact geometric descriptor sensitive to this trajectory evolution.

### Điều chưa thể kết luận

Naha không cung cấp direct evidence rằng một finite voltage difference cụ thể
có thể tách riêng hoặc định lượng:

$$
LLI
$$

$$
LAM
$$

$$
SEI\ growth
$$

hoặc các degradation modes khác.

Vì vậy, hiện chưa nên claim:

$$
GSI \equiv LLI
$$

hoặc:

$$
GSI \equiv LAM
$$

hoặc:

$$
GSI \equiv SEI\ growth
$$

### Kết luận hiện tại

Thông tin quan trọng nhất lấy từ Naha là:

$$
\boxed{
\text{aging}
\rightarrow
\text{voltage-trajectory evolution}
\rightarrow
\text{finite-}\Delta V\text{ evolution}
}
$$

Đây là một mechanistic clue hữu ích để biện luận vì sao GSI có thể
nhạy với SOH, nhưng chưa phải bằng chứng cho một degradation mechanism
cụ thể phía sau GSI.


# Gap hiện tại khi so sánh Naha 2020 với GSI

Naha đã chứng minh rằng partial charging voltage trajectory chứa
aging-sensitive information và có thể được biểu diễn bằng nhiều
incremental voltage differences:

$$
\mathbf{x}
=
[
\Delta v_{sei,1},
\dots,
\Delta v_{sei,9},
T_{avg}
]
$$

Sau đó ANN được sử dụng để học mapping giữa feature vector và SOH.

Tuy nhiên, vẫn chưa rõ liệu có cần giữ nhiều local voltage-difference
features như vậy hay không.

GSI đặt câu hỏi:

$$
\text{How much voltage-trajectory information is actually required for SOH estimation?}
$$

Thay vì nhiều local $\Delta V$, GSI nén partial voltage trajectory thành
một regional voltage separation duy nhất:

$$
GSI = V_H - V_T
$$

### Research gap

Existing partial-voltage approaches retain multiple local features and
may require nonlinear estimators, while the minimum amount of geometric
information required from the voltage trajectory remains unclear.

### Research question

Liệu một single regional geometric descriptor của partial voltage
trajectory có đủ để estimate SOH chính xác và generalize giữa các cell
hay không?

### Working hypothesis

Một Head–Tail voltage separation được lựa chọn phù hợp có thể giữ lại
đủ aging-sensitive information để estimate SOH, trong khi giảm mạnh:

- feature dimensionality;
- preprocessing;
- model complexity;
- computational/storage requirement.

### Điều cần chứng minh thực nghiệm

GSI chỉ có giá trị contribution nếu chứng minh được trade-off:

$$
\text{comparable accuracy}
+
\text{much lower complexity}
+
\text{strong cross-cell generalization}
$$

so với các multi-$\Delta V$ baselines như Naha-style features.

# Partial-region sensitivity: gap từ Naha 2020

Naha sử dụng một fixed starting voltage $v_{sei,0}$ và từ đó lấy
10 voltage points cách nhau:

$$
\Delta Q_c = 1.5\%C_{\max}
$$

Authors cho biết vị trí $v_{sei,0}$ có thể được chọn tùy application.

Tuy nhiên, paper không thực hiện systematic sensitivity analysis đối với
vị trí của partial charging region.

Không có so sánh kiểu:

$$
\text{different starting regions}
\rightarrow
\text{different SOH performance}
$$

Robustness được kiểm tra chủ yếu theo:
- cell;
- temperature;
- charging C-rate;
- nominal capacity.

### Implication for GSI

Một experiment quan trọng là kiểm tra sensitivity của GSI đối với
Head/Tail window location.

Câu hỏi:

$$
\text{GSI có chỉ hoạt động tại một narrowly tuned region hay không?}
$$

Desired evidence:

$$
\text{broad stable region}
\rightarrow
\text{robust trajectory-based descriptor}
$$

thay vì:

$$
\text{single sharp optimum}
\rightarrow
\text{possible dataset-specific window tuning}
$$

Potential contribution:

> Systematic evaluation of regional sensitivity and robustness of a
> partial-voltage trajectory descriptor.

---

# Petkovski_2024

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

---

# Qin_2024

# Qin & Zhao, Energy 2024 — Targeted Audit

## Motivation

Các feature/model SOH được xây dựng dưới điều kiện cố định có thể mất hiệu lực khi:

- chỉ có dữ liệu partial charging;
- battery type, temperature, charging mode hoặc application thay đổi;
- dữ liệu aging của target domain còn hạn chế.

Bài toán cốt lõi:

$$
\text{partial observation}
+
\text{domain shift}
\rightarrow
\text{giảm khả năng áp dụng của feature/model}
$$

---

## Research Gap

### Gap 1 — Chọn vùng feature

Các phương pháp partial-charging vẫn thường cần một voltage interval phù hợp được xác định trước.

$$
\text{arbitrary partial interval}
\not\Rightarrow
\text{effective aging feature}
$$

Việc chọn interval tốt thường cần dữ liệu aging đầy đủ.

### Gap 2 — Khả năng thích nghi giữa các application

Feature và mapping SOH học từ một application có thể không còn phù hợp ở application khác.

Các hướng hiện có như:
- multi-domain training;
- transfer learning / fine-tuning;

vẫn cần dữ liệu aging của target domain.

---

## Insight chính

Thay vì chọn feature window hoàn toàn bằng correlation:

$$
\text{IC peak}
\rightarrow
\text{aging-sensitive voltage region}
\rightarrow
\text{curve-shape constraint}
$$

Sau đó xây các relative geometric features để giảm phụ thuộc vào vị trí tuyệt đối của partial charging segment.

Đối với domain shift:

$$
\text{initial-reference scaling}
+
\text{online adaptation}
$$

được dùng thay vì giả định một frozen model có thể dùng chung cho mọi application.

---

## Method

### 1. Adaptive voltage-region determination

Rough region:
- xây IC curve;
- xác định IC peak;
- voltage interval phải chứa voltage tại IC peak.

Final region:
- voltage curve trong interval phải gần dạng straight line hoặc arc;
- shape được đánh giá thông qua biến thiên slope/derivative.

### 2. Geometric aging features

Trên mặt phẳng $(t,V)$:

$$
l_1=
\sqrt{(t_b-t_a)^2+(V_b-V_a)^2}
$$

$$
l_2=
\frac{|V_b-V_a|}{|t_b-t_a|}
$$

$$
l_3=
\frac{|t_b-t_a|}
{\sqrt{(t_b-t_a)^2+(V_b-V_a)^2}}
$$

Ý tưởng:

> sử dụng relative geometry thay vì absolute curve coordinates.

### 3. Feature self-scaling

$$
X_{n,k}=\frac{X_{i,k}}{X_{i,0}}
$$

Mục tiêu:
- giảm khác biệt về feature scale giữa các battery applications.

### 4. SOH adaptation

$$
\text{self-scaled features}
\rightarrow
\text{OSELM online update}
\rightarrow
SOH
$$

Model được cập nhật liên tục bằng dữ liệu của target battery.

---

## Relevance / Threat với GSI

### Conceptual overlap mạnh

Cả hai đều theo hướng:

$$
\text{partial trajectory}
\rightarrow
\text{low-dimensional geometric feature}
\rightarrow
\text{practical SOH estimation}
$$

Qin cũng dùng initial-reference normalization:

$$
X_t/X_0
$$

nên làm yếu novelty claim rộng dựa riêng trên BOL normalization.

### Khác biệt chính

Qin:

$$
(t,V)
+
\text{multiple geometric features}
+
X_t/X_0
+
\text{online OSELM adaptation}
$$

GSI:

$$
(Q,V)
+
\text{single Head--Tail }\Delta V
+
(GSI_t-GSI_0)
+
\text{linear mapping}
$$

---

## Gap / Cơ hội còn lại cho GSI

GSI không nên claim novelty từ:
- geometric partial-curve feature;
- reference normalization đơn thuần;
- lightweight feature construction đơn thuần.

Cơ hội mạnh nhất:

> Một single capacity-defined Head–Tail descriptor mà BOL normalization có thể giảm cell-specific offset đủ mạnh để hỗ trợ cross-cell SOH estimation với rất ít hoặc không cần target-cell adaptation.

Bằng chứng cần bổ sung:

1. Leakage-free Head/Tail selection.
2. Giải thích rõ và thuyết phục cách chọn Head/Tail.
3. Region-sensitivity / stable-basin analysis.
4. ICA/DVA-supported interpretation.
5. GSI vs ΔGSI ablation.
6. Định lượng số target-cell cycles cần để recalibrate.
7. Quantified computational cost.

## Verdict

- Raw GSI threat: **Moderate–High**
- ΔGSI threat: **Moderate**
- Generalization threat: **Moderate**
- Complexity threat: **Low**
- Physical-interpretation relevance: **High**
- Vai trò với GSI: **closest conceptual / methodological neighbor quan trọng**

---

# Wen_2022

# Research gap

Các phương pháp SOH hiện có vẫn gặp hạn chế cho quick/on-site estimation:

- direct capacity measurement cần full charge/discharge và tốn thời gian;
- EIS khó triển khai field test và nhạy với noise;
- physics-based methods có model complexity cao;
- deep-learning/data-driven methods có computational cost cao và feature khó diễn giải;
- ICA/regional derivative methods cần filtering và thường bị giới hạn ở low C-rate;
- nhiều data-driven methods phụ thuộc mạnh vào data volume/characteristics và khó xử lý battery-wise differences.

=> Gap chính:

Thiếu một phương pháp SOH đơn giản, nhanh, không phá hủy và có thể áp dụng
trên shallow partial charge/discharge data với high fidelity.

## Research question

Có thể sử dụng một regional feature đơn giản từ partial CC voltage-time curve
để estimate SOH chính xác mà không cần full profile, derivative-heavy processing
hoặc high-complexity model hay không?

Sub-question:

Có tồn tại một suitable voltage region mà incremental SoC có quan hệ ổn định,
gần tuyến tính với SOH hay không?

Ngoài SOH estimation, các đặc trưng của quan hệ này có thể giúp phân biệt
remaining-life tendency giữa các batteries có cùng SOH hay không?

#  SoH–ΔSoC evolution during discharging

### Core idea

Wen chọn một voltage window:

$$
(V_s,\Delta V)
$$

trên CC discharge curve.

Thời gian để voltage đi qua window là:

$$
\Delta t
$$

và vì discharge ở constant current:

$$
\Delta SoC=C\Delta t
$$

Do đó:

$$
\text{fixed }\Delta V
\rightarrow
\text{measure }\Delta SoC
$$

### Window selection

Authors scan nhiều tổ hợp:

$$
(V_s,\Delta V)
$$

và dùng Spearman correlation giữa $\Delta SoC$ và SoH để tìm
aging-sensitive voltage region.

Điều này cho thấy:

$$
\text{SOH information is region-dependent}
$$

trên voltage trajectory.

### Physical interpretation

Authors dùng IC curve:

$$
dSoC/dV
$$

để liên hệ sự thay đổi của $\Delta SoC$ với sự thay đổi của
electrochemical reaction features.

IC peak intensity và position thay đổi theo cycling, đồng thời với
sự thay đổi của quan hệ SoH–$\Delta SoC$.

=> Đây là physical bridge, không phải direct identification của LLI/LAM.

### Relation to GSI

Wen:

$$
\text{fixed voltage span}
\rightarrow
\text{horizontal capacity span } \Delta SoC
$$

GSI:

$$
\text{fixed capacity regions}
\rightarrow
\text{vertical voltage span } \Delta V
$$

Hai phương pháp đều khai thác local geometry của voltage trajectory,
nhưng theo hai hướng khác nhau.

### Key implication for GSI

1. Aging information không phân bố đồng đều trên voltage curve.
2. Window/region selection là một phần quan trọng của method.
3. GSI nên có region-sensitivity analysis để chứng minh robustness.
4. ICA có thể được dùng như một bridge vật lý để giải thích tại sao
   regional voltage geometry thay đổi theo aging.

# Physical interpretation bằng IC trong Wen 2022

### Vai trò của IC

IC không phải feature chính để estimate SOH.

Feature chính vẫn là:

$$
\Delta SoC = C\Delta t
$$

trong một voltage window cố định.

IC được dùng như một **physical interpretation bridge** để kiểm tra xem sự thay đổi của
regional feature có đi cùng sự thay đổi của các đặc trưng điện hóa trên voltage curve hay không.

### Quan sát từ IC

Wen sử dụng:

$$
\frac{dSoC}{dV}
$$

và quan sát theo cycling:

- IC peak intensity giảm;
- IC peak position dịch chuyển;
- một số peak có thể biến mất ở degradation stage muộn hơn.

Các thay đổi này xuất hiện đồng thời với sự thay đổi của quan hệ:

$$
SoH \leftrightarrow \Delta SoC
$$

Đặc biệt, khi IC peaks thay đổi mạnh hơn, quan hệ SoH–$\Delta SoC$
cũng chuyển từ gần tuyến tính sang nonlinear. :contentReference[oaicite:0]{index=0}

### Cách diễn giải vật lý

Có thể tóm tắt logic của Wen như sau:

$$
\text{battery aging}
\rightarrow
\text{electrochemical reaction characteristics evolve}
$$

$$
\Downarrow
$$

$$
\text{IC peak evolution}
\leftrightarrow
\text{voltage-trajectory evolution}
$$

$$
\Downarrow
$$

$$
\Delta SoC\text{ trong fixed voltage window thay đổi}
$$

IC vì vậy cung cấp evidence rằng regional voltage feature có liên hệ với
aging-induced electrochemical evolution, chứ không chỉ là empirical correlation.

### Giới hạn

Wen không trực tiếp chứng minh:

$$
\Delta SoC \equiv LLI
$$

hoặc:

$$
\Delta SoC \equiv LAM
$$

hoặc một degradation mode cụ thể.

Do đó IC ở đây là **supporting physical interpretation**, không phải
direct degradation-mode identification.

## Tiềm năng áp dụng cho GSI

GSI đo regional voltage geometry:

$$
GSI = V_H - V_T
$$

Một hướng physical interpretation tiềm năng là kiểm tra xem vùng Head–Tail
có đồng thời chứa các IC/DVA features thay đổi theo aging hay không.

Nếu quan sát được:

$$
\text{IC/DVA evolution trong cùng region}
$$

đồng thời với:

$$
\text{GSI evolution}
$$

thì có thể xây dựng chain:

$$
\text{aging}
\rightarrow
\text{electrochemical evolution}
\rightarrow
\text{local voltage-trajectory evolution}
\rightarrow
\text{GSI evolution}
$$

### Safe claim cho GSI

> IC/DVA analysis có thể được dùng để hỗ trợ rằng vùng Head–Tail được chọn là
> một aging-sensitive electrochemical region của voltage trajectory.

Không nên claim rằng GSI trực tiếp đo LLI, LAM hoặc một degradation mechanism cụ thể
nếu chưa có diagnostic evidence mạnh hơn.

# Kế hoạch thực nghiệm cho Physical Interpretation của GSI

### Mục tiêu

Không cần chứng minh GSI trực tiếp đo LLI/LAM/SEI.

Mục tiêu thực tế hơn:

> Kiểm tra liệu sự thay đổi của GSI có đồng thời với sự thay đổi của các
> đặc trưng electrochemical trên cùng vùng voltage trajectory hay không.

### 1. Theo dõi GSI theo aging

Với mỗi cycle:

$$
GSI_t = V_{H,t}-V_{T,t}
$$

và nếu dùng differential form:

$$
\Delta GSI_t = GSI_t-GSI_0
$$

Plot:

$$
GSI,\Delta GSI \text{ vs. cycle / SOH}
$$

để xác nhận trajectory evolution.

### 2. Tính ICA/DVA trên cùng dữ liệu

Từ voltage-capacity curve:

$$
IC = \frac{dQ}{dV}
$$

hoặc:

$$
DVA = \frac{dV}{dQ}
$$

Theo dõi theo aging:

- peak position;
- peak amplitude;
- peak area;
- peak disappearance/appearance;
- local slope evolution.

### 3. Đặt Head–Tail region lên ICA/DVA

Xác định Head và Tail của GSI nằm ở đâu so với:

- IC peaks;
- IC valleys;
- DVA features;
- plateau-transition regions.

Mục tiêu là kiểm tra:

$$
\text{GSI-selected region}
\leftrightarrow
\text{aging-sensitive ICA/DVA region}
$$

### 4. Phân tích sự đồng biến

So sánh:

$$
GSI_t
$$

với các ICA/DVA features theo cycle/SOH.

Ví dụ:

$$
GSI_t \leftrightarrow IC\ peak\ position
$$

$$
GSI_t \leftrightarrow IC\ peak\ amplitude
$$

$$
GSI_t \leftrightarrow local\ DVA\ evolution
$$

Có thể dùng correlation và visualization để xem chúng có thay đổi
đồng thời theo aging hay không.

### 5. Region sensitivity map

Dịch Head/Tail windows dọc voltage-capacity trajectory và tính:

$$
\rho(GSI,SOH)
$$

hoặc prediction error cho từng region.

Sau đó so sánh bản đồ này với ICA/DVA evolution.

Nếu vùng GSI tốt nhất trùng với vùng ICA/DVA thay đổi mạnh theo aging,
đây sẽ là physical evidence mạnh hơn việc chỉ tối ưu correlation.

### 6. Kiểm tra resistance / polarization effect

Nếu có dữ liệu ở nhiều C-rate, so sánh:

$$
GSI(C_1),GSI(C_2),...
$$

để xác định GSI nhạy bao nhiêu với current-induced polarization.

Mục tiêu là phân biệt sơ bộ:

$$
\text{aging-related trajectory evolution}
$$

với:

$$
\text{operating-condition-induced voltage shift}
$$

### 7. Expected physical interpretation

Nếu kết quả phù hợp, có thể xây dựng chain:

$$
\text{battery aging}
\rightarrow
\text{electrochemical evolution visible in ICA/DVA}
\rightarrow
\text{local }V(Q)\text{ geometry evolution}
\rightarrow
\text{GSI evolution}
$$

### Safe claim

> GSI captures geometric changes in an aging-sensitive region of the
> voltage-capacity trajectory, whose evolution is consistent with
> changes observed in ICA/DVA characteristics.

### Không nên claim nếu chưa có diagnostic bổ sung

$$
GSI \equiv LLI
$$

$$
GSI \equiv LAM
$$

$$
GSI \equiv SEI\ growth
$$

Muốn đi tới degradation-mode identification mạnh hơn sẽ cần additional
diagnostics như half-cell fitting, EIS, reference-electrode data hoặc
post-mortem analysis.


# Robustness experiment: Voltage region và Head/Tail sensitivity

### Mục tiêu

Kiểm tra GSI có phụ thuộc mạnh vào exact region/window được chọn hay không.

### Level 1 — Voltage-region sensitivity

Thay đổi vùng voltage quan sát:

$$
[V_{\min},V_{\max}]
\rightarrow
[V_{\min}+\delta_1,V_{\max}+\delta_2]
$$

Với mỗi region:
- xác định lại Head/Tail;
- tính GSI;
- đánh giá $R^2$, RMSE, MAE trên cùng protocol.

### Level 2 — Head/Tail sensitivity

Trong một voltage region cố định, perturb vị trí Head/Tail:

$$
(Q_H,Q_T)
\rightarrow
(Q_H+\delta_H,Q_T+\delta_T)
$$

và đánh giá lại performance.

### Evidence mong muốn

Không chỉ có một sharp optimum mà tồn tại:

$$
\boxed{\text{broad stable region with similar performance}}
$$

Điều này hỗ trợ claim:

> GSI không phụ thuộc mạnh vào một exact predefined voltage/window location,
> mà khai thác một vùng aging-sensitive tương đối ổn định của voltage trajectory.

### Quan trọng

Window/region selection phải được thực hiện chỉ trên training cells trong mỗi outer LOCO fold:

$$
\text{train cells}
\rightarrow
\text{select region/Head-Tail}
\rightarrow
\text{freeze}
\rightarrow
\text{test held-out cell}
$$

để tránh feature-selection leakage.

# Experiment: Generalization và BOL-reference effect

### Mục tiêu

Kiểm tra liệu $\Delta GSI$ có làm quan hệ feature–SOH ổn định hơn giữa các cell và dataset hay không.

### 1. Within-cell analysis

Với từng cell, plot:

$$
GSI \text{ vs. SOH}
$$

và:

$$
\Delta GSI \text{ vs. SOH}
$$

So sánh:
- slope;
- intercept;
- linearity;
- residual/error.

### 2. Cross-cell analysis

Overlay tất cả cells trong cùng dataset.

Kiểm tra liệu raw GSI có:

$$
\text{cell-specific offset / trajectory shift}
$$

và sau BOL subtraction:

$$
\Delta GSI = GSI_t-GSI_0
$$

các trajectories có collapse gần hơn về một common relationship hay không.

### 3. Cross-dataset analysis

Lặp lại trên:
- in-house dataset;
- external dataset.

So sánh mức độ ổn định của:

$$
GSI\text{–SOH}
$$

và:

$$
\Delta GSI\text{–SOH}
$$

giữa hai dataset.

### 4. Strict generalization test

Trong mỗi validation fold:

$$
\text{train cells}
\rightarrow
\text{select/freeze region + Head/Tail + model}
\rightarrow
\text{held-out cell}
$$

External dataset không được dùng target SOH để tune lại feature/window.

### Evidence mong muốn

Nếu:

$$
\Delta GSI
$$

giảm:
- inter-cell intercept shift;
- trajectory dispersion;
- cross-dataset mapping variation;

và đồng thời cải thiện LOCO/external error,

thì có thể support hypothesis:

> BOL referencing suppresses cell-specific baseline variation and improves
> transferability of the GSI–SOH relationship across unseen cells.


# Gaps và Motivation cho GSI sau Naha 2020 + Wen 2022

### 1. Minimal representation

Prior works đã chứng minh partial voltage trajectory chứa aging information:

- Naha: nhiều local $\Delta V$ + temperature + ANN.
- Wen: một regional $\Delta SoC$ + linear relation.

=> Gap còn lại:

$$
\text{Có thể nén aging-sensitive trajectory xuống một single capacity-defined voltage descriptor hay không?}
$$

GSI hypothesis:

$$
GSI = V_H - V_T
$$

có thể giữ đủ SOH information với representation tối giản hơn.

---

### 2. Computational cost

Naha và Wen đều nhấn mạnh tính practical/online/on-site, nhưng chưa có
systematic quantitative benchmark về:

- inference time;
- memory;
- FLOPs/MACs;
- hardware cost.

Naha dùng ANN nhỏ; Wen dùng linear relation. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

=> GSI có thể định lượng trực tiếp:

$$
\text{accuracy} \;-\; \text{computational complexity}
$$

đặc biệt cho deployment trên BMS.

---

### 3. Cross-cell / cross-dataset generalization

Wen cho thấy regional $\Delta SoC$ vẫn informative trên external A123 dataset,
nhưng exact SOH–$\Delta SoC$ behavior thay đổi:

$$
\text{LISHEN: mainly linear for } SOH>0.75
$$

$$
\text{A123: nonlinear early stage, then linear}
$$

:contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

=> Gap:

$$
\text{feature generalizes}
\neq
\text{mapping is invariant}
$$

GSI nên kiểm tra:

$$
GSI\text{–SOH}
\quad \text{vs.} \quad
\Delta GSI\text{–SOH}
$$

trên từng cell và từng dataset.

---

### 4. BOL-reference normalization

Naha và Wen chưa sử dụng dạng:

$$
HI_t-HI_0
$$

như một explicit within-cell normalization.

=> Hypothesis tiềm năng:

$$
\Delta GSI_t = GSI_t-GSI_0
$$

có thể giảm cell-specific offset và làm degradation trajectories
collapse về một common relationship tốt hơn.

---

### 5. Regional robustness

Wen scan nhiều voltage windows và cho thấy SOH information phụ thuộc region;
Naha cũng cần một fixed starting voltage. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5}

=> GSI cần kiểm tra:

- voltage-region sensitivity;
- Head/Tail sensitivity;
- broad stable region vs. sharp optimum.

Mục tiêu:

$$
\text{robust regional descriptor}
>
\text{dataset-specific tuned window}
$$

---

### 6. Physical interpretation

Naha cung cấp chain:

$$
\text{capacity/resistance-related aging}
\rightarrow
\text{voltage-trajectory evolution}
$$

Wen dùng ICA để cho thấy regional feature evolution đi cùng
IC peak evolution. :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

=> Motivation cho GSI:

$$
\text{aging}
\rightarrow
\text{electrochemical evolution}
\rightarrow
\text{local }V(Q)\text{ evolution}
\rightarrow
GSI\text{ evolution}
$$

GSI có thể dùng ICA/DVA để support physical interpretation,
nhưng không claim trực tiếp LLI/LAM/SEI nếu chưa có diagnostic evidence.

---

## Working contribution hypothesis

GSI không nên được định vị là một completely new voltage-difference idea.

Tiềm năng contribution nằm ở tổ hợp:

$$
\boxed{
\text{minimal capacity-defined descriptor}
+
\text{BOL normalization}
+
\text{regional robustness}
+
\text{strict cross-cell/external generalization}
+
\text{quantified low computational cost}
}
$$