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

Romano et al. (2004) mở rộng recurrence analysis từ **recurrence của từng hệ riêng lẻ** sang **joint recurrence của nhiều hệ**.

Thay vì so sánh trực tiếp hai trajectory như CRP:

$$\mathbf{x}_i \approx \mathbf{y}_j$$

MRP kiểm tra xem tại cùng cặp thời điểm $(i,j)$, mỗi hệ có recurrence trong **phase space riêng của nó** hay không:

$$\mathbf{x}_i \approx \mathbf{x}_j$$

và đồng thời

$$\mathbf{y}_i \approx \mathbf{y}_j.$$

Do đó:

$$\boxed{JR^{x,y}_{ij}=R^x_{ij}R^y_{ij}}$$

Một joint recurrence xuất hiện khi **cả hai hệ cùng quay trở lại neighborhood của chính chúng tại cùng cặp thời điểm**.

> **Core idea:** MRP không đo hai hệ có ở gần nhau hay không; nó đo liệu các recurrence events của chúng có xảy ra đồng thời hay không.

---

## Mathematical Foundation

Điểm xuất phát là second-order Rényi information:

$$H_2(x)=-\log\sum_m p_m^2.$$

Xác suất

$$\sum_m p_m^2$$

có thể được ước lượng bằng recurrence probability:

$$\frac{1}{N^2}\sum_{i,j}R^x_{ij}.$$

Với hai hệ, joint Rényi information được ước lượng từ **joint recurrence probability**:

$$\hat H_2(x,y)=-\log\left[\frac{1}{N^2}\sum_{i,j}R^x_{ij}R^y_{ij}\right].$$

Từ đó Romano định nghĩa joint recurrence matrix:

$$\boxed{JR^{x,y}_{ij}=\Theta(\epsilon_x-\|\mathbf{x}_i-\mathbf{x}_j\|)\Theta(\epsilon_y-\|\mathbf{y}_i-\mathbf{y}_j\|)}$$

Hai hệ có thể có:

$$d_x\neq d_y,\qquad\epsilon_x\neq\epsilon_y,$$

vì mỗi recurrence được xác định trong phase space riêng trước khi được kết hợp.

Flow toán học cốt lõi:

$$\boxed{\text{Rényi information}\rightarrow\text{recurrence probability}\rightarrow\text{joint recurrence probability}\rightarrow\text{MRP/JRP}}$$