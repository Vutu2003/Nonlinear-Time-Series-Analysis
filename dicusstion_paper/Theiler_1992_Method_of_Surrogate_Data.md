# THUẬT TOÁN AAFT (Amplitude Adjusted Fourier Transform)
*Tác giả: Theiler (1992)*



**Đầu vào:** Chuỗi thời gian thực nghiệm $x_t$ với $t = 0, 1, \dots, N-1$.
* Gọi $x_{(k)}$ là phần tử nhỏ thứ $k$ (sau khi sắp xếp tăng dần) của chuỗi $x_t$.
* Gọi $R(v)$ là hàm trả về thứ hạng (rank) của giá trị $v$ trong tập hợp của nó.

---

## Bước 1: Khởi tạo Gaussian
Tạo một chuỗi nhiễu trắng độ dài $N$ tuân theo phân phối chuẩn tắc:
$$r_t \sim \mathcal{N}(0, 1)$$
Gọi $r_{(k)}$ là phần tử nhỏ thứ $k$ của chuỗi $r_t$ sau khi sắp xếp.

## Bước 2: Ánh xạ thứ hạng thuận (Forward Rank-ordering)
Tạo chuỗi dữ liệu mới $y_t$ mang phân phối Gaussian nhưng giữ nguyên trật tự thời gian (động lực học) của $x_t$ bằng phép gán:
$$y_t = r_{(R(x_t))}$$

## Bước 3: Ngẫu nhiên hóa pha (Phase Randomization)
* **3.1. Phân tích phổ (DFT):**
  $$Y_k = \sum_{t=0}^{N-1} y_t e^{-i 2\pi k t / N} = |Y_k| e^{i \theta_k}$$
* **3.2. Xáo trộn pha:** Nhân với góc pha ngẫu nhiên $\phi_k \sim \mathcal{U}[0, 2\pi)$ (áp dụng điều kiện đối xứng $\phi_k = -\phi_{N-k}$ để đảm bảo miền thời gian là số thực):
  $$\tilde{Y}_k = |Y_k| e^{i \phi_k}$$
* **3.3. Tái tạo miền thời gian (IDFT):**
  $$y'_t = \frac{1}{N} \sum_{k=0}^{N-1} \tilde{Y}_k e^{i 2\pi k t / N}$$

## Bước 4: Ánh xạ thứ hạng nghịch (Inverse Rank-ordering)
Kéo chuỗi Surrogate $y'_t$ (đang có biên độ Gaussian) trở về phân phối biên độ thực nghiệm ban đầu. Thu được chuỗi đối chứng cuối cùng $x^{surr}_t$:
$$x^{surr}_t = x_{(R(y'_t))}$$

---
**Kết luận:** Chuỗi dữ liệu thay thế $x^{surr}_t$ bảo toàn chính xác 100% phân phối biên độ của chuỗi gốc $x_t$ (nhờ Bước 4) và xấp xỉ bảo toàn phổ năng lượng tuyến tính sinh ra từ Bước 3.