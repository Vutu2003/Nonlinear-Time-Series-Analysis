# Paper Metadata
* **Title**: Ordinal analysis of time series
* **Authors**: K. Keller, M. Sinn
* **Year**: 2005
* **Keywords**: Time series; Complexity; Ordinal patterns; Permutation entropy

# 1. Why

## Research Question

Làm thế nào để biểu diễn và khai thác **toàn bộ thông tin ordinal** của một chuỗi thời gian, thay vì nén cấu trúc ordinal xuống một giá trị entropy duy nhất?

## Motivation

Bandt–Pompe cho thấy có thể phân tích time series một cách robust bằng cách sử dụng **quan hệ thứ tự tương đối** thay cho giá trị biên độ tuyệt đối:

$$
x_t
\rightarrow
\text{ordinal patterns}
$$

Tuy nhiên, cấu trúc ordinal chứa nhiều thông tin hơn một scalar complexity measure.

Keller & Sinn hướng tới một representation có thể:

- giữ lại ordinal state tại mỗi thời điểm;
- được tính toán hiệu quả;
- hỗ trợ các phân tích sâu hơn ngoài entropy.

Ý tưởng cốt lõi:

$$
\boxed{
\text{Giữ lại ordinal structure trước}
\rightarrow
\text{quantify sau}
}
$$

## Previous Methods

### Bandt–Pompe Permutation Entropy

Pipeline:

$$
x_t
\rightarrow
\pi_t
\rightarrow
p(\pi)
\rightarrow
H
$$

Permutation Entropy tóm tắt distribution của ordinal patterns bằng:

$$
H
=
-\sum_{\pi}p(\pi)\log p(\pi)
$$

Đây là một complexity measure hữu ích, nhưng chỉ cung cấp **một chi tiết của ordinal structure**.

Bước nén:

$$
p(\pi)
\rightarrow
H
$$

làm mất nhiều thông tin về cấu trúc cụ thể của các ordinal patterns.

Vì vậy Keller & Sinn chuyển từ:

$$
\boxed{
\text{ordinal structure}
\rightarrow
\text{scalar complexity}
}
$$

sang:

$$
\boxed{
\text{ordinal structure}
\rightarrow
\text{richer ordinal representation}
}
$$

# 2. What

## Core Insight

Keller & Sinn không nén ordinal structure trực tiếp thành một scalar như Permutation Entropy, mà xây dựng một **ordinal representation mới** cho time series.

Tại mỗi thời điểm $t$:

$$
(x_t,x_{t-\tau},...,x_{t-d\tau})
\rightarrow
\pi_d^\tau(t)
$$

Ordinal pattern sau đó được mã hóa thành inversion vector:

$$
\pi_d^\tau(t)
\leftrightarrow
(i_1^\tau(t),...,i_d^\tau(t))
$$

và cuối cùng thành một giá trị:

$$
\bar n_d^\tau(t)\in[0,1]
$$

Toàn bộ time series được biến đổi thành:

$$
(x_t)
\rightarrow
(\bar n_d^\tau(t))
$$

Ý tưởng cốt lõi:

$$
\boxed{
\text{Ordinal patterns}
\rightarrow
\text{numerical ordinal representation}
}
$$

thay vì:

$$
\boxed{
\text{Ordinal patterns}
\rightarrow
\text{entropy scalar}
}
$$

---

## Mathematical Foundation

### 1. Ordinal Pattern

Với order $d$ và delay $\tau$, tại thời điểm $t$ xét:

$$
x_t,x_{t-\tau},...,x_{t-d\tau}
$$

Ordinal pattern:

$$
\pi_d^\tau(t)=(r_0,r_1,...,r_d)
$$

thỏa:

$$
x_{t-r_0\tau}
\ge
x_{t-r_1\tau}
\ge
...
\ge
x_{t-r_d\tau}
$$

Có tổng cộng:

$$
(d+1)!
$$

ordinal patterns.

### 2. Inversion Representation

Mỗi pattern được mã hóa bởi:

$$
i_l^\tau(t)
=
\#
\left\{
r\in\{0,...,l-1\}
\mid
x_{t-r\tau}\le x_{t-l\tau}
\right\}
$$

với:

$$
i_l\in\{0,...,l\}
$$

Vector:

$$
(i_1,...,i_d)
$$

mã hóa duy nhất ordinal pattern nên không làm mất ordinal information.

### 3. Ordinal Number

Inversion vector được ánh xạ bijective thành:

$$
n_d^\tau(t)
=
\sum_{l=1}^{d}
i_l^\tau(t)
\frac{(d+1)!}{(l+1)!}
$$

với:

$$
n_d^\tau(t)\in\{0,...,(d+1)!-1\}
$$

### 4. Ordinal Transformation

Chuẩn hóa ordinal number về $[0,1]$:

$$
\bar n_d^\tau(t)
=
\frac{n_d^\tau(t)}{(d+1)!}
=
\sum_{l=1}^{d}
\frac{i_l^\tau(t)}{(l+1)!}
$$

Từ đó thu được ordinal-transformed time series:

$$
\boxed{
(x_t)
\rightarrow
(\bar n_d^\tau(t))
}
$$

Khi $d$ tăng, transformation chứa nhiều ordinal information hơn; về mặt lý thuyết:

$$
d\rightarrow\infty
$$

cho phép biểu diễn toàn bộ **ordinal information** của time series.

# 3. How

## 3.1 Algorithm

Với time series $(x_t)$, order $d$ và delay $\tau$:

1. Tại mỗi thời điểm $t$, lấy delayed window:

$$
(x_t,x_{t-\tau},...,x_{t-d\tau})
$$

2. Xác định ordinal pattern:

$$
\pi_d^\tau(t)
$$

3. Tính inversion vector:

$$
(i_1^\tau(t),...,i_d^\tau(t))
$$

với:

$$
i_l^\tau(t)
=
\#
\left\{
r\in\{0,...,l-1\}
\mid
x_{t-r\tau}\le x_{t-l\tau}
\right\}
$$

4. Mã hóa inversion vector thành ordinal number:

$$
n_d^\tau(t)
=
\sum_{l=1}^{d}
i_l^\tau(t)
\frac{(d+1)!}{(l+1)!}
$$

5. Chuẩn hóa về $[0,1]$:

$$
\bar n_d^\tau(t)
=
\frac{n_d^\tau(t)}{(d+1)!}
$$

6. Lặp lại theo thời gian để tạo ordinal-transformed series:

$$
(\bar n_d^\tau(t))_t
$$

---

## 3.2 Mathematical Formulation

### Ordinal Pattern

$$
\pi_d^\tau(t)=(r_0,...,r_d)
$$

sao cho:

$$
x_{t-r_0\tau}
\ge
x_{t-r_1\tau}
\ge
...
\ge
x_{t-r_d\tau}
$$

Số possible patterns:

$$
(d+1)!
$$

### Inversion Coding

Mỗi ordinal pattern được biểu diễn duy nhất bởi:

$$
(i_1,...,i_d)
$$

với:

$$
i_l\in\{0,...,l\}
$$

Do đó:

$$
\pi_d^\tau(t)
\leftrightarrow
(i_1^\tau(t),...,i_d^\tau(t))
$$

là một lossless recoding trên ordinal level.

### Ordinal Transformation

$$
\boxed{
\bar n_d^\tau(t)
=
\sum_{l=1}^{d}
\frac{i_l^\tau(t)}{(l+1)!}
\in[0,1]
}
$$

Khi $d$ tăng, representation chứa nhiều ordinal information hơn.

---

## 3.3 End-to-End Pipeline

$$
(x_t)
$$

$$
\downarrow
$$

$$
(x_t,x_{t-\tau},...,x_{t-d\tau})
$$

$$
\downarrow
$$

$$
\pi_d^\tau(t)
$$

$$
\downarrow
$$

$$
(i_1^\tau(t),...,i_d^\tau(t))
$$

$$
\downarrow
$$

$$
n_d^\tau(t)
$$

$$
\downarrow
$$

$$
\boxed{
\bar n_d^\tau(t)\in[0,1]
}
$$

Lặp theo $t$:

$$
\boxed{
(x_t)
\rightarrow
(\bar n_d^\tau(t))
}
$$

Kết quả là một time series mới biểu diễn ordinal structure của signal.

---

## 3.4 Computational Complexity

Keller & Sinn khai thác overlap giữa các delayed windows để cập nhật inversion counts thay vì tính lại toàn bộ từ đầu.

Recurrence:

$$
i_l^\tau(t)
=
\begin{cases}
i_{l-1}^\tau(t-\tau)+1,
& x_t\le x_{t-l\tau} \\
i_{l-1}^\tau(t-\tau),
& \text{otherwise}
\end{cases}
$$

Với time series dài $L$ và order $d$:

$$
\boxed{
O(Ld)
}
$$

Authors ước lượng ordinal transformation cần khoảng:

$$
5dL
$$

logic-arithmetic operations.

---

## 3.5 Implementation Notes

- $d+1$: số samples trong một ordinal window.
- $\tau$: khoảng cách giữa các samples bên trong window.
- Temporal span:

$$
d\tau
$$

samples, hoặc:

$$
d\tau\Delta t
$$

theo thời gian thực.

- Hai consecutive windows overlap mạnh nên nên dùng incremental update.
- Tie cần một deterministic rule để mỗi window ánh xạ duy nhất tới một ordinal pattern.
- Không cần lưu permutation nếu mục tiêu cuối là ordinal transformation; inversion vector có thể được tính trực tiếp.
- Chuẩn hóa về $[0,1]$ giúp các ordinal representations ở different orders nằm trên cùng một numerical range.
- Ordinal transformation giữ ordinal information, không khôi phục absolute amplitude information.