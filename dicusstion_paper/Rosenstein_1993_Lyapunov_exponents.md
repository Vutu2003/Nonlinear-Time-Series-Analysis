### THUẬT TOÁN ROSENSTEIN (1993) TÍNH SỐ MŨ LYAPUNOV LỚN NHẤT (LLE - $\lambda_1$)

**Đầu vào:** Chuỗi thời gian $1D$ gồm $N$ điểm $\{x_1, x_2, \dots, x_N\}$, chu kỳ lấy mẫu $\Delta t$.

#### Bước 1: Tái cấu trúc không gian pha
Mở rộng chuỗi $1D$ thành quỹ đạo trong không gian $m$ chiều.

* **Vector trạng thái:**
$$X_i = (x_i, x_{i+J}, \dots, x_{i+(m-1)J})$$

* **Ma trận quỹ đạo ($M \times m$):**
$$\mathbf{X} = (X_1, X_2, \dots, X_M)^T$$

* **Tham số:** * $m$: Số chiều nhúng.
  * $J$: Độ trễ thời gian (ước lượng qua hàm tự tương quan giảm đến $1 - 1/e$).
  * $M$: Số lượng vector, $M = N - (m - 1)J$.

#### Bước 2: Tìm láng giềng gần nhất (Ràng buộc Theiler)
Với mỗi điểm $X_j$, tìm láng giềng gần nhất $X_{\hat{j}}$.

* **Khoảng cách ban đầu:**
$$d_j(0) = \min_{X_{\hat{j}}} \| X_j - X_{\hat{j}} \|$$

* **Ràng buộc thời gian (Theiler window):**
$$|j - \hat{j}| > w$$
*(Trong đó $w$ là chu kỳ trung bình, nghịch đảo của tần số trung bình từ phổ năng lượng).*

#### Bước 3: Đo lường phân kỳ và Trung bình hóa Logarit
Theo dõi sự phân kỳ của các cặp điểm theo hàm mũ: $d_j(i) \approx d_j(0) e^{\lambda_1 (i \Delta t)}$.

* **Tuyến tính hóa:**
$$\ln d_j(i) \approx \ln d_j(0) + \lambda_1 (i \Delta t)$$

* **Lấy trung bình toàn cục:** Tính trung bình logarit cho tất cả $M$ cặp điểm tại mỗi bước $i$ để triệt tiêu nhiễu:
$$y(i) = \frac{1}{\Delta t} \langle \ln d_j(i) \rangle$$
*(Với $\langle \dots \rangle$ là giá trị trung bình trên toàn bộ chỉ số $j$).*

#### Bước 4: Ước lượng LLE ($\lambda_1$)
* **Đồ thị:** Vẽ hàm $y(i)$ theo thời gian thực $i \Delta t$.
* **Trích xuất:** Áp dụng hồi quy bình phương tối thiểu (Least-squares fit) lên **vùng tuyến tính** (linear region) của đồ thị. Hệ số góc (slope) chính là giá trị Số mũ Lyapunov lớn nhất $\lambda_1$.