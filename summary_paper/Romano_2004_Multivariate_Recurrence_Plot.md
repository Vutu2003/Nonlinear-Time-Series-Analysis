# Paper Metadata
* **Title:** Multivariate recurrence plots
* **Authors:** M. Carmen Romano, Marco Thiel, Jürgen Kurths, Werner von Bloh
* **Year:** 2004
* **Keywords:** Multivariate recurrence plots, Joint Rényi entropy, Phase synchronization, Nonlinear dynamics, Time series analysis

# 1. Why

## Research Question

Làm thế nào để xây dựng một phương pháp recurrence cho **multivariate time series** có thể:

- mô tả **joint dynamics** của nhiều hệ tương tác,
- ước lượng các **dynamical invariants** và **information measures** của toàn hệ,
- phát hiện các hiện tượng **complex synchronization**, đặc biệt là phase synchronization và weak coupling,

mà không cần trộn trực tiếp các phase spaces của các hệ thành cùng một không gian so sánh.

---

## Motivation

Các hệ thực nghiệm thường:

- phi tuyến,
- nonstationary,
- có dữ liệu tương đối ngắn,
- và không biết trước phương trình động lực học chi phối.

Do đó cần một phương pháp có thể suy ra thông tin về **predictability, complexity và synchronization** trực tiếp từ time series.

Romano et al. đề xuất MRP dựa trên **joint recurrences**, từ đó có thể ước lượng **joint second-order Rényi entropy $K_2$** và nghiên cứu sự thay đổi của dynamics khi các hệ chuyển sang phase synchronization.

---

## Previous Methods

### RP / RQA

RP mô tả recurrence của một trajectory trong phase space:

$$R_{ij}=\Theta(\epsilon-\|\mathbf{x}_i-\mathbf{x}_j\|).$$

RQA mở rộng RP từ trực quan sang định lượng.

**Giới hạn:** chủ yếu mô tả recurrence của từng hệ riêng lẻ, chưa trực tiếp biểu diễn joint recurrence của nhiều subsystem.

---

### Cross Recurrence Plot (CRP)

CRP so sánh trực tiếp hai trajectory:

$$CR_{ij}=\Theta(\epsilon-\|\mathbf{x}_i-\mathbf{y}_j\|).$$

**Giới hạn đối với bài toán Romano:**

- hai states phải có thể so sánh trực tiếp trong một common phase space,
- thường đòi hỏi phase-space dimensions tương thích,
- không cho phép mỗi subsystem giữ hoàn toàn độc lập phase-space geometry và threshold riêng.

Trong ví dụ hai Rössler oscillators của paper, CRP không phân biệt được rõ trạng thái phase synchronized và non-phase-synchronized.

---

### Lyapunov Exponents

Tổng các Lyapunov exponents dương

$$\sum_{\lambda_i>0}\lambda_i$$

cung cấp thông tin về mức độ chaotic của toàn hệ.

**Giới hạn:**

- thường cần biết equations of motion,
- khó áp dụng trực tiếp khi chỉ có experimental time series,
- với hệ nonhyperbolic, quan hệ giữa $K_2$ và $\sum \lambda_i^+$ không còn là đẳng thức.

Trong paper, ở vùng coupling rất nhỏ

$$\mu \in [0,0.006],$$

$\sum \lambda_i^+$ không làm lộ rõ tip của Arnold tongue, trong khi $K_2$ ước lượng từ MRP vẫn cho thấy cấu trúc này.

---

## Core Gap

Các phương pháp trước đó chưa đồng thời đáp ứng được:

$$\boxed{\text{multivariate dynamics}+\text{separate phase spaces}+\text{data-based invariant estimation}+\text{synchronization analysis}}$$

Romano et al. giải quyết khoảng trống này bằng **joint recurrences**.

# 2. What

## Core Insight

Romano et al. (2004) mở rộng recurrence analysis từ **recurrence của từng hệ** sang **joint recurrence của nhiều hệ**.

Thay vì so sánh trực tiếp hai trajectory như CRP, MRP kiểm tra liệu tại cùng cặp thời điểm `(i, j)`, các hệ có cùng recurrence trong **phase space riêng của chúng** hay không:

$$
JR_{ij}^{x,y} = R_{ij}^{x} R_{ij}^{y}
$$

Trong đó:

$$
R_{ij}^{x}
=
\Theta
\left(
\epsilon_x - \|\mathbf{x}_i-\mathbf{x}_j\|
\right)
$$

$$
R_{ij}^{y}
=
\Theta
\left(
\epsilon_y - \|\mathbf{y}_i-\mathbf{y}_j\|
\right)
$$

Do đó:

$$
JR_{ij}^{x,y}=1
$$

chỉ khi **cả hai hệ cùng recurrence tại `(i, j)`**.

> **Core idea:** MRP không hỏi hai hệ có ở gần nhau hay không; nó hỏi liệu các recurrence events của chúng có xảy ra đồng thời hay không.

Vì mỗi hệ được xét trong phase space riêng nên có thể có:

$$
d_x \neq d_y,
\qquad
\epsilon_x \neq \epsilon_y
$$

---

## Mathematical Foundation

Second-order Rényi information có dạng:

$$
H_2(x)
=
-\log
\left(
\sum_m p_m^2
\right)
$$

Trong recurrence analysis, xác suất này có thể được ước lượng từ recurrence probability:

$$
\sum_m p_m^2
\approx
\frac{1}{N^2}
\sum_{i,j} R_{ij}
$$

Với hai hệ, ta thay recurrence probability bằng **joint recurrence probability**:

$$
\frac{1}{N^2}
\sum_{i,j}
R_{ij}^{x}R_{ij}^{y}
$$

Từ đó joint recurrence matrix `JR` trở thành cơ sở để ước lượng các information measures của toàn coupled system.

### Joint Rényi entropy K2

Romano tiếp tục sử dụng **độ dài các joint diagonal lines** trong MRP.

Nếu xác suất xuất hiện diagonal dài ít nhất `l` là `P(l)`, thì trong scaling region:

$$
\ln P(l)
\approx
-K_2 l \Delta t + C
$$

Do đó `K2` được ước lượng từ độ dốc của `ln P(l)` theo `l`.

- `K2` lớn → diagonal dài mất nhanh → dynamics phức tạp/chaotic hơn.
- `K2` nhỏ → diagonal dài tồn tại nhiều → dynamics regular/predictable hơn.

---

## Algorithm

### Step 1 — Construct individual recurrence plots

Từ hai synchronized time series, xây riêng:

$$
R^x
\qquad \text{và} \qquad
R^y
$$

với threshold riêng:

$$
\epsilon_x,
\qquad
\epsilon_y
$$

### Step 2 — Construct the Multivariate Recurrence Plot

Thực hiện element-wise intersection:

$$
JR^{x,y}
=
R^x \odot R^y
$$

hay:

$$
JR_{ij}^{x,y}
=
R_{ij}^{x}R_{ij}^{y}
$$

### Step 3 — Extract joint diagonal lines

Tìm các chuỗi:

$$
JR_{i,j}
=
JR_{i+1,j+1}
=
\cdots
=
JR_{i+l-1,j+l-1}
=
1
$$

### Step 4 — Estimate K2

Tính distribution của joint diagonal lengths:

$$
P(l)
=
P(\text{diagonal length} \ge l)
$$

sau đó fit vùng tuyến tính của:

$$
\ln P(l)
\quad \text{vs.} \quad
l
$$

để ước lượng `K2`.

### Overall Flow

$$
X,Y
\rightarrow
R^x,R^y
\rightarrow
JR
\rightarrow
\text{Joint Diagonals}
\rightarrow
P(l)
\rightarrow
K_2
$$

# 3. How

## 3.1 Algorithm

Given two synchronized trajectories

$$
X=\{\mathbf{x}_i\}_{i=1}^{N},
\qquad
Y=\{\mathbf{y}_i\}_{i=1}^{N},
$$

construct the individual recurrence matrices:

$$
R_{ij}^{x}
=
\Theta
\left(
\epsilon_x-\|\mathbf{x}_i-\mathbf{x}_j\|
\right),
$$

$$
R_{ij}^{y}
=
\Theta
\left(
\epsilon_y-\|\mathbf{y}_i-\mathbf{y}_j\|
\right).
$$

Then form the Multivariate/Joint Recurrence Plot:

$$
JR_{ij}^{x,y}
=
R_{ij}^{x}R_{ij}^{y}.
$$

A joint recurrence occurs only when both subsystems recur simultaneously at the same pair of times `(i, j)`.

---

## 3.2 Mathematical Formulation

The joint recurrence probability is:

$$
P_{JR}
=
\frac{1}{N^2}
\sum_{i,j=1}^{N}
JR_{ij}^{x,y}.
$$

To estimate the joint second-order Rényi entropy, extract joint diagonal lines and define:

$$
P(l)
=
P(\text{diagonal length} \ge l).
$$

In the scaling region:

$$
\ln P(l)
\approx
-K_2 l \Delta t + C.
$$

Hence:

$$
\widehat{K}_2
\approx
-\frac{\text{slope}}{\Delta t}.
$$

---

## 3.3 End-to-End Pipeline

$$
X,Y
\rightarrow
\text{Phase-space reconstruction}
\rightarrow
R^x,R^y
\rightarrow
JR
\rightarrow
\text{Joint diagonal lengths}
\rightarrow
P(l)
\rightarrow
\widehat{K}_2
$$

Interpretation:

- `JR` captures simultaneous recurrence geometry.
- Joint diagonals capture repeated joint evolution.
- `K2` quantifies the predictability/complexity of the whole coupled system.

---

## 3.4 Computational Complexity

For `N` states per subsystem:

- Distance matrix for each RP: approximately `O(N^2)`.
- Memory for each recurrence matrix: `O(N^2)`.
- Joint matrix construction: `O(N^2)`.
- Diagonal-line extraction: approximately `O(N^2)`.

Therefore, the dominant cost is:

$$
\boxed{O(N^2)}
$$

in both computation and memory.

The paper explicitly notes that computation time increases approximately with `N^2`.

---

## 3.5 Implementation Notes

- The signals must share a common time axis before constructing `JR`.
- Each subsystem may use its own:
  - embedding dimension,
  - phase-space geometry,
  - recurrence threshold.

Thus:

$$
d_x \neq d_y,
\qquad
\epsilon_x \neq \epsilon_y.
$$

- Romano recommends selecting thresholds through recurrence rate rather than using identical absolute thresholds.
- For estimating `K2`, only a suitable linear scaling region of `ln P(l)` versus `l` should be fitted.
- Very long diagonals and very rare events should be excluded to reduce finite-size effects.
- In the paper's automated analysis:
  - `N = 10000`,
  - diagonal lengths above `l_max = 400` were excluded,
  - 40 recurrence-rate levels from `1%` to `95%` were tested.

# 4. Experiment

# 5. Conclusion

## Assumptions

- Các subsystem phải được quan sát trên **cùng một time axis** để `JR_ij` biểu diễn recurrence đồng thời tại cùng cặp thời điểm `(i, j)`.
- Mỗi subsystem được phép có **phase-space dimension và threshold riêng**:

$$
d_x \neq d_y,
\qquad
\epsilon_x \neq \epsilon_y
$$

- Recurrence threshold phải được chọn sao cho phản ánh hợp lý natural measure của từng hệ; paper ưu tiên cách chọn thông qua recurrence rate.
- Ước lượng `K2` giả định tồn tại một **scaling region** đủ rõ trong quan hệ:

$$
\ln P(l) \approx -K_2 l \Delta t + C
$$

- Chuỗi thời gian phải đủ dài để distribution của joint diagonal lines có ý nghĩa thống kê.

---

## Limitations

- Chi phí tính toán và bộ nhớ tăng xấp xỉ:

$$
O(N^2)
$$

nên trở nên nặng với chuỗi dài.

- Kết quả phụ thuộc vào:
  - phase-space reconstruction,
  - recurrence thresholds,
  - lượng dữ liệu,
  - việc chọn scaling region để estimate `K2`.

- MRP yêu cầu **time alignment đã biết trước**; khác với CRP, nó không phù hợp để trực tiếp tìm sự tương ứng giữa hai time axes khác nhau.

- Joint recurrence phản ánh **simultaneous recurrence**, nhưng bản thân một joint recurrence point không chứng minh synchronization hay coupling; cần xem cấu trúc thống kê của toàn MRP.

- Paper chưa đánh giá đầy đủ ảnh hưởng của noise; tác giả xem đây là hướng cần nghiên cứu tiếp.

- Khả năng phân biệt synchronization được chứng minh trên hệ Rössler cụ thể, vì vậy không nên xem kết quả định lượng là phổ quát cho mọi dynamical system.

> **Overall:** MRP cung cấp một cách giữ riêng phase space của từng subsystem nhưng vẫn mô tả joint dynamics của toàn hệ. Điểm mạnh chính là khả năng chuyển joint recurrence geometry thành các information/dynamical measures như `K2`; đổi lại, phương pháp phụ thuộc đáng kể vào preprocessing, threshold selection và chất lượng diagonal statistics.

# 6. My Research

## Research Ideas

MRP mở ra một hướng phù hợp cho bài toán sinh lý đa biến, nơi nhiều subsystem phản ánh các cơ chế điều hòa khác nhau nhưng cùng tiến hóa theo thời gian.

Một hướng tự nhiên là xây dựng joint recurrence giữa các tín hiệu như:

$$
\text{EEG} \leftrightarrow \text{PPG/PRV}
$$

hoặc:

$$
\text{Cardiac} \leftrightarrow \text{Respiratory}
$$

để kiểm tra liệu các subsystem có **recurrence đồng thời** trong quá trình chuyển trạng thái sinh lý hay không.

Thay vì chỉ tính một MRP cho toàn bộ recording, có thể dùng sliding window:

$$
JR_{ij}^{(w)}
$$

và theo dõi các đại lượng như:

$$
RR_{joint}(w),
\qquad
K_2^{joint}(w)
$$

theo thời gian.

Mục tiêu là nghiên cứu:

> sự phối hợp giữa các subsystem thay đổi như thế nào trước, trong và sau một physiological transition.

Một hướng mở rộng khác là kết hợp ba lớp recurrence information:

- **Diagonal RQA:** evolution / predictability
- **Vertical RQA:** persistence / laminarity
- **MRP:** simultaneous recurrence / joint dynamics

từ đó xây dựng một mô tả đa tầng của transition dynamics.

---

## Knowledge Contribution

Đóng góp tiềm năng không chỉ nằm ở việc áp dụng MRP vào dữ liệu sinh lý, mà ở việc chuyển từ phân tích từng signal riêng lẻ sang phân tích **organization của toàn hệ đa biến**.

Có thể hình dung contribution theo flow:

$$
\text{Single-system dynamics}
\rightarrow
\text{Cross-system interrelation}
\rightarrow
\text{Joint-system dynamics}
$$

Cụ thể:

- dùng RP/RQA để mô tả dynamics nội tại của từng subsystem;
- dùng CRP để mô tả lagged dynamical interrelation giữa hai signals;
- dùng MRP để mô tả các recurrence events xảy ra đồng thời trong toàn hệ;
- theo dõi các quantities này theo sliding window để nghiên cứu **dynamical transition** thay vì chỉ phân loại trạng thái tĩnh.

> **Potential contribution:** xây dựng một recurrence-based multivariate framework để mô tả cách các subsystem sinh lý thay đổi từ dynamics tương đối độc lập sang dynamics phối hợp trong quá trình chuyển trạng thái.