### Khung Thuật toán Cốt lõi: Simplex Projection (Sugihara & May, 1990)

Thuật toán Simplex Projection được áp dụng để dự báo phi tuyến ngắn hạn nhằm trích xuất "chữ ký hỗn loạn" của tín hiệu PPG, với mục tiêu phân biệt trạng thái Tỉnh táo (hỗn loạn tất định) và Buồn ngủ (nhiễu vi mô lấn át). Quy trình thực chiến bao gồm 7 bước (bao gồm cả tiền xử lý) như sau:

#### **Bước 0: Tiền xử lý - Khử xu hướng tuyến tính (First-Differencing)**
Để loại bỏ các tự tương quan tuyến tính chậm (slow trends) sinh ra do nhịp thở hoặc cử động cơ thể, chuỗi tín hiệu gốc $x = \{x_1, x_2, \dots, x_N\}$ được chuyển hóa thành chuỗi sai phân bậc 1 (đặt là $y$):
$$y_t = x_{t+1} - x_t$$
*(Toàn bộ các bước tiếp theo sẽ được thực hiện độc lập trên chuỗi sai phân $y$ có chiều dài $N-1$).*

#### **Bước 1: Tái tạo Không gian Trạng thái (State Space Reconstruction)**
Dựa trên Định lý nhúng Takens, chuỗi 1D được tái tạo thành các vector trạng thái trong không gian $E$ chiều với độ trễ $\tau$:
$$\mathbf{Y}_t = \langle y_t, y_{t-\tau}, y_{t-2\tau}, \dots, y_{t-(E-1)\tau} \rangle$$
Tập hợp các vector này được chia làm hai phần: Tập Thư viện (Library) để tra cứu và Tập Kiểm thử (Predictee) để dự báo.

#### **Bước 2: Truy vấn và Bộ lọc Cửa sổ Theiler (Theiler Window Exclusion)**
Với mỗi điểm truy vấn $\mathbf{Y}_p$ (tại thời điểm $p$) trong tập Kiểm thử, thuật toán tìm kiếm láng giềng trong tập Thư viện. 
**Điều kiện tiên quyết:** Bất kỳ điểm ứng viên $\mathbf{Y}_i$ nào cũng phải thỏa mãn Cửa sổ Theiler ($t_w$) để tránh lỗi "tự tương quan tầm thường" (ngăn việc sử dụng các điểm quá gần về mặt thời gian để dự báo tương lai):
$$|p - i| > t_w$$
Khoảng cách Euclidean từ điểm truy vấn đến các ứng viên hợp lệ được tính bằng:
$$d(\mathbf{Y}_p, \mathbf{Y}_i) = \| \mathbf{Y}_p - \mathbf{Y}_i \|_2$$

#### **Bước 3: Xác định Khối Đa diện (Simplex Identification)**
Sắp xếp các khoảng cách hợp lệ theo thứ tự tăng dần: $d_1 \le d_2 \le \dots \le d_k$.
Thuật toán chọn ra chính xác **$k = E + 1$** láng giềng gần nhất để tạo thành một khối đa diện (Simplex) bao bọc điểm truy vấn. Gọi chỉ số thời gian của $E+1$ láng giềng này là $v_1, v_2, \dots, v_{E+1}$.

#### **Bước 4: Tính Trọng số Suy giảm Hàm mũ (Exponential Weighting)**
Gán trọng số cho từng láng giềng $j \in [1, E+1]$ dựa trên khoảng cách của chúng, sử dụng khoảng cách nhỏ nhất $d_1$ làm hệ số chuẩn hóa:
$$w_j = \exp \left( - \frac{d(\mathbf{Y}_p, \mathbf{Y}_{v_j})}{d_1} \right)$$
*(Trường hợp ngoại lệ: Nếu $d_1 = 0$, nghĩa là tồn tại điểm lịch sử trùng khớp hoàn hảo, thuật toán gán $w_1 = 1$ và $w_{j \ne 1} = 0$).*

Sau đó, chuẩn hóa để tổng trọng số bằng $1$ (đảm bảo tính chất tổ hợp lồi để giới nội nhiễu):
$$W_j = \frac{w_j}{\sum_{m=1}^{E+1} w_m}$$

#### **Bước 5: Phóng chiếu Nội suy (Forward Projection)**
Xác định giá trị thực tế của $E+1$ láng giềng ở $T_p$ bước trong tương lai ($y_{v_j+T_p}$). Giá trị dự báo của điểm truy vấn ở tương lai ($\hat{y}_{p+T_p}$) là trung bình cộng có trọng số của các quỹ đạo lịch sử này:
$$\hat{y}_{p+T_p} = \sum_{j=1}^{E+1} W_j \cdot y_{v_j+T_p}$$

#### **Bước 6: Đánh giá Năng lực Dự báo bằng Hệ số Tương quan ($\rho$)**
Lặp lại các bước trên cho toàn bộ các điểm trong tập Kiểm thử để tạo ra chuỗi dự báo sai phân $\hat{Y}$ và so sánh với chuỗi sai phân thực tế $Y_{true}$. "Chữ ký" của hệ thống được đánh giá bằng Hệ số tương quan Pearson qua các tầm nhìn dự báo $T_p$ khác nhau:
$$\rho(T_p) = \frac{\text{Cov}(\hat{Y}, Y_{true})}{\sigma_{\hat{Y}} \sigma_{Y_{true}}}$$