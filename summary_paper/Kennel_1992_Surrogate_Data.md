# PIPELINE TOÁN HỌC: CHUẨN ĐOÁN HỖN LOẠN VÀ TẠO DỮ LIỆU THAY THẾ
*(Phương pháp Surrogate Data - Kennel & Isabelle, 1992)*

## GIAI ĐOẠN 1: Tiền xử lý - Ép Phân phối Gaussian (Histogram Transformation)
**Mục tiêu:** Tránh lỗi "dương tính giả" do khác biệt về hình dáng phân phối xác suất.

* **Đầu vào:** Chuỗi dữ liệu thô $x(n)$ với $n = 1, 2, \dots, N$.
* **Bước 1.1:** Tạo một chuỗi số ngẫu nhiên $g(n)$ có độ dài $N$ tuân theo phân phối chuẩn tắc (Gaussian) $\mathcal{N}(0,1)$.
* **Bước 1.2:** Sắp xếp cả hai chuỗi $x(n)$ và $g(n)$ theo thứ tự độ lớn tăng dần.
* **Bước 1.3:** Ánh xạ 1-1 (rank-based mapping) giá trị của $x(n)$ sang giá trị của $g(n)$ có cùng thứ hạng.
* **Đầu ra:** Một chuỗi dữ liệu mới $x'(n)$ đã mang hình hài phân phối Gaussian nhưng vẫn bảo toàn tuyệt đối động lực học (số mũ Lyapunov, fractal) của chuỗi $x(n)$ ban đầu. *(Từ đây về sau, ta chỉ dùng $x'(n)$ làm "Dữ liệu Thật").*

## GIAI ĐOẠN 2: Tạo Nhóm Đối chứng (Surrogate Data Generation)
**Mục tiêu:** Tạo ra $M$ chuỗi "Dữ liệu Giả" có cùng cấu trúc tự tương quan (nhiễu màu) với chuỗi thật $x'(n)$.

* **Bước 2.1 (Biến đổi Fourier):** Tính DFT của chuỗi thật $x'(n)$:
    $$X(k) = \sum_{j=0}^{N-1} x'(j) \exp\left(\frac{2\pi i j k}{N}\right)$$
* **Bước 2.2 (Ngẫu nhiên hóa Pha):** Tạo $M$ chuỗi phổ giả ($r = 1, \dots, M$) bằng cách nhân với nhiễu Gaussian phức:
    $$X^r(k) = X(k) [\zeta(k) + i\eta(k)]$$
    *(Trong đó $\zeta$ và $\eta$ là số ngẫu nhiên Gaussian độc lập, trung bình $0$, phương sai $1/2$. Để kết quả là số thực, ép điều kiện $\eta(k) = -\eta(N-k)$).*
* **Bước 2.3 (Biến đổi ngược):** Tính IDFT để đưa về miền thời gian:
    $$x^r(n) = \frac{1}{N} \sum_{k=0}^{N-1} X^r(k) \exp\left(\frac{-2\pi i n k}{N}\right)$$
* **Bước 2.4 (Kiểm định Chất lượng):** Chạy bài test Kolmogorov-Smirnov (K-S test) giữa phân phối của $x'(n)$ và $x^r(n)$. Nếu khác biệt quá 95%, vứt bỏ chuỗi giả này và thuật toán sẽ tạo lại chuỗi mới.

## GIAI ĐOẠN 3: Tái cấu trúc Không gian & Chạy Dự báo (The Prediction Algorithm)
**Mục tiêu:** Ép các chuỗi dữ liệu thực hiện chức năng "Dự báo tương lai" để tìm ra Sai số.
*(Lặp lại quy trình này cho cả chuỗi thật $x'(n)$ và $M$ chuỗi giả $x^r(n)$)*

* **Bước 3.1 (Nhúng Không gian trễ):** Tạo các vector $d$ chiều với độ trễ $T$:
    $$y(j) = (x(j), x(j+T), \dots, x(j+(d-1)T))$$
* **Bước 3.2 (Tìm 1 láng giềng):** Tại mỗi điểm truy vấn $y(j)$, dùng thuật toán k-d tree tìm đúng 1 láng giềng gần nhất là $y(il)$.
    *(Màng lọc Theiler: Loại bỏ tất cả láng giềng có $|il - j| < \text{autocorrelation time}$ để tránh lấy các điểm lân cận về mặt thời gian).*
* **Bước 3.3 (Tính Sai số Dự báo):** Dự báo tương lai $\tau$ bước và tính sai số tuyệt đối $e(j)$:
    $$e(j) = |x(il + (d-1)T + \tau) - x(j + (d-1)T + \tau)|$$
* **Đầu ra:** Ta có một tập sai số của dữ liệu thật $e(j)$, và $M$ tập sai số của dữ liệu giả $e^r(j)$.

## GIAI ĐOẠN 4: Làm mỏng Dữ liệu (Decimation)
**Mục tiêu:** Bơm tính "Độc lập thống kê" vào các tập sai số để thỏa mãn điều kiện kiểm định.

* **Bước 4.1:** Tính thời gian tự tương quan (autocorrelation time) của tập sai số $e(j)$.
* **Bước 4.2:** Loại bỏ (decimate) các mẫu sai số nằm quá gần nhau, chỉ giữ lại các điểm cách nhau một khoảng bằng thời gian tự tương quan.

**Đầu ra Giai đoạn 4:**
* **Tập A:** Sai số của dữ liệu thật đã làm mỏng (có kích thước $N_a$).
* **Tập B:** Gộp toàn bộ $M$ tập sai số của dữ liệu giả đã làm mỏng (có kích thước $N_b = M \times N_a$).

---

## GIAI ĐOẠN 5: Tòa án Thống kê & Hiệu chỉnh Mức ý nghĩa (The Statistic & Alpha)
**Mục tiêu:** Tính toán tỷ lệ thắng/thua và chốt hạ bằng con số độ tin cậy.

* **Bước 5.1 (Mann-Whitney Rank-Sum):** Đếm số lần sai số thật ($A$) lớn hơn sai số giả ($B$):
  $$U = \sum_{i=1}^{N_a} \sum_{j=1}^{N_b} \Theta(A_i - B_j)$$
  *(Với $\Theta(x) = 1$ nếu $x > 0$, ngược lại bằng $0$)*

* **Bước 5.2 (Z-score):** Chuẩn hóa $U$ thành biến $z$:
  $$z = \frac{U - N_a N_b / 2}{\sqrt{N_a N_b (N_a + N_b + 1) / 12}}$$

* **Bước 5.3 (Hiệu chỉnh Bonferroni):** Nếu bạn quét vòng lặp qua $K$ cặp tham số ($d, T$) khác nhau, mức ý nghĩa mục tiêu $\alpha$ (ví dụ: $0.01$ cho độ tin cậy $99\%$) phải được chia nhỏ để chống Dương tính giả. Ta tìm ngưỡng $z_0$ mới theo phương trình:
  $$\int_{-\infty}^{z_0} e^{-z^2/2} dz = \frac{\sqrt{2\pi} \alpha}{K}$$

---

## 🏁 QUYẾT ĐỊNH CUỐI CÙNG:
So sánh $z$ tính được (ở **Bước 5.2**) với $z_0$ (ở **Bước 5.3**):

* **Nếu $z < z_0$** (Ví dụ $z < -2.33$ với $\alpha=0.01, K=1$): Bác bỏ $H_0$. Mở tiệc ăn mừng! Tín hiệu PPG của bạn chứa cấu trúc Hỗn loạn Tất định được giấu kín dưới lớp nhiễu.
* **Nếu $z \ge z_0$**: Chấp nhận $H_0$. Thuật toán dự báo không thể hiện sự vượt trội có ý nghĩa thống kê so với nhiễu màu ngẫu nhiên. Hệ thống được coi là Nhiễu (hoặc quá ồn để có thể phân biệt).