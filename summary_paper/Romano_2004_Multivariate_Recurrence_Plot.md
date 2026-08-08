# Paper Metadata
* **Title:** Multivariate recurrence plots
* **Authors:** M. Carmen Romano, Marco Thiel, Jürgen Kurths, Werner von Bloh
* **Year:** 2004
* **Keywords:** Multivariate recurrence plots, Joint Rényi entropy, Phase synchronization, Nonlinear dynamics, Time series analysis


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