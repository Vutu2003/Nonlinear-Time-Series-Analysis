### 1. Đầu vào (Input)
Chuỗi thời gian thực nghiệm gồm $N$ điểm dữ liệu:
$$X = \{x_1, x_2, \dots, x_N\}$$

### 2. Tái cấu trúc không gian pha (Phase Space Reconstruction)
Nhúng chuỗi $X$ vào không gian $d$ chiều bằng độ trễ thời gian $\tau$. Vector trạng thái tại bước $i$ được định nghĩa là:
$$\xi_i = \Big( x_i, x_{i+\tau}, x_{i+2\tau}, \dots, x_{i+(d-1)\tau} \Big)$$
Tổng số vector trạng thái thu được:
$$N_m = N - (d-1)\tau$$

### 3. Tích phân tương quan (Correlation Integral)
Tính xác suất để hai vector trạng thái có khoảng cách không gian nhỏ hơn bán kính $l$, đồng thời loại bỏ các tương quan giả do quán tính thời gian bằng cửa sổ Theiler $w$:
$$C(l, d) = \frac{1}{N_{pairs}} \sum_{i=1}^{N_m} \sum_{j=i+w}^{N_m} \theta \Big( l - \|\xi_i - \xi_j\| \Big)$$
Trong đó:
* Khoảng cách $\|\cdot\|$ thường dùng chuẩn cực đại (Chebyshev norm) hoặc chuẩn Euclid.
* $\theta(x)$ là hàm Heaviside step: $\theta(x) = 1$ khi $x > 0$, ngược lại $\theta(x) = 0$.
* Tổng số cặp vector hợp lệ sau khi áp dụng Theiler window:
$$N_{pairs} = \frac{(N_m - w + 1)(N_m - w)}{2}$$

### 4. Ước lượng số chiều cục bộ (Local Dimension Estimation)
Dựa trên định luật lũy thừa của hệ Fractal $C(l, d) \propto l^{\nu(d)}$, hệ số góc (số chiều tương quan $\nu$) tại chiều nhúng $d$ là đạo hàm trên đồ thị log-log trong vùng tuyến tính (Scaling Region):
$$\nu(d) = \frac{\partial \ln C(l, d)}{\partial \ln l}$$

### 5. Tiêu chuẩn bão hòa (Saturation Rule)
Khảo sát hàm số $\nu(d)$ khi số chiều nhúng $d \to \infty$ ($d = 2, 3, 4, \dots$):

* **Kịch bản 1: Hỗn loạn tất định (Deterministic Chaos)**
  $$\lim_{d \to \infty} \nu(d) = \nu_{sat} \quad (\text{Hằng số})$$
  *(Kết luận: Hệ thống có cấu trúc phi tuyến với số bậc tự do thực tế là $\nu_{sat}$)*

* **Kịch bản 2: Nhiễu ngẫu nhiên (Random Noise)**
  $$\nu(d) \approx d$$
  *(Kết luận: Hệ thống không có cấu trúc giới hạn, lấp đầy mọi không gian được nhúng)*