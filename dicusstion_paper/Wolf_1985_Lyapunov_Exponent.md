### THUẬT TOÁN WOLF (1985) TÍNH SỐ MŨ LYAPUNOV LỚN NHẤT (LLE - $\lambda_1$)

**Đầu vào:** Chuỗi dữ liệu 1D $x = \{x_1, x_2, \dots, x_N\}$, chu kỳ lấy mẫu $dt$.

#### Bước 1: Tái cấu trúc Không gian Pha
"Nhúng" chuỗi 1D vào không gian $m$ chiều bằng phương pháp tọa độ trễ.
* **Véc-tơ không gian trạng thái tại $t_i$:**
  $$X(t_i) = \{x(t_i), x(t_i + \tau), \dots, x(t_i + (m-1)\tau)\}$$
  *(Với $m$ là chiều nhúng, $\tau$ là độ trễ thời gian).*

#### Bước 2: Khởi tạo và Tìm láng giềng đầu tiên
Tìm láng giềng $X_{nn}(t_0)$ gần nhất với điểm mốc $X(t_0)$.
* **Khoảng cách Euclidean:**
  $$d_j = \| X(t_0) - X(t_j) \| = \sqrt{\sum_{k=1}^{m} \left( X_k(t_0) - X_k(t_j) \right)^2}$$
* **Tiêu chuẩn chọn:** Chọn $X(t_j)$ có $d_j$ nhỏ nhất sao cho:
  1. $d_j > \text{SCALMN}$ *(Tránh nhiễu thiết bị đo).*
  2. $|t_0 - t_j| > \text{Mean Period}$ *(Tránh các điểm nằm trên cùng một quỹ đạo thời gian).*
* **Lưu trữ:** Khoảng cách ban đầu $L(t_0) = \| X(t_0) - X_{nn}(t_0) \|$.

#### Bước 3: Tiến hóa theo bước thời gian cố định
Cho cặp điểm trôi về phía trước một khoảng $\Delta t$ (EVOLV).
* **Cập nhật thời gian:** $t_1 = t_0 + \Delta t$
* **Khoảng cách sau tiến hóa:**
  $$L'(t_1) = \| X(t_1) - X_{nn}(t_1) \|$$

#### Bước 4: Quy trình Thay thế Láng giềng (Replacement)
Giữ lại $X(t_1)$, bỏ láng giềng cũ, tìm ứng viên $X_{new}(t_1)$ thỏa mãn cả khoảng cách và góc lệch.
* **Định nghĩa véc-tơ:**
  * Véc-tơ cũ: $\vec{V}_{old} = X(t_1) - X_{nn}(t_1)$
  * Véc-tơ mới: $\vec{V}_{new} = X(t_1) - X_{candidate}$
* **Tính góc lệch $\theta$ (Tích vô hướng):**
  $$\cos(\theta) = \frac{\vec{V}_{old} \cdot \vec{V}_{new}}{\|\vec{V}_{old}\| \times \|\vec{V}_{new}\|}$$
  $$\theta = \arccos \left( |\cos(\theta)| \right)$$
* **Tiêu chuẩn chọn:** Quét không gian tìm $X_{new}(t_1)$ sao cho:
  1. $\text{SCALMN} \le \|\vec{V}_{new}\| \le \text{SCALMX}$
  2. $\theta \le \text{ANGLMX}$ (Nếu có nhiều điểm, ưu tiên $\theta$ nhỏ nhất).
  *(Nếu thất bại: Tăng dần $\text{SCALMX}$, sau đó nới lỏng $\text{ANGLMX}$. Tệ nhất thì giữ nguyên véc-tơ cũ).*
* **Cập nhật:** $L(t_1) = \|\vec{V}_{new}\|$ và thay thế láng giềng mới.

#### Bước 5: Tính tổng Logarit và Trích xuất LLE ($\lambda_1$)
* **Lặp:** Lặp lại quy trình (Tiến hóa $\rightarrow$ Tính Log $\rightarrow$ Thay thế) cho đến điểm cuối mảng.
* **Tính lượng thông tin phân kỳ tại bước $k$:**
  $$\text{Rate}_k = \log_2 \left( \frac{L'(t_k)}{L(t_{k-1})} \right)$$
* **Phương trình chốt LLE ($\lambda_1$):** Lấy tổng lượng phân kỳ chia cho tổng thời gian tiến hóa:
  $$\lambda_1 = \frac{1}{M \cdot \Delta t \cdot dt} \sum_{k=1}^{M} \log_2 \frac{L'(t_k)}{L(t_{k-1})}$$
  *(Đơn vị: bits/second. $M$ là tổng số bước thay thế).*

> **💡 Lưu ý lập trình:** Nút thắt cổ chai (bottleneck) nằm ở Bước 4. Phải sử dụng cấu trúc dữ liệu không gian tối ưu (ví dụ: KD-Tree) thay vì quét tuyến tính toàn bộ ma trận để đảm bảo tốc độ chạy của thuật toán.

### 6 ĐIỂM YẾU CHÍ MẠNG CỦA THUẬT TOÁN WOLF (1985)

* **1. Sai số Hướng (Orientation Errors):**
    * **Bản chất:** Sinh ra từ khâu "Thay thế láng giềng". Máy tính không thể tìm được điểm thay thế nằm thẳng hàng chuẩn xác 100% với véc-tơ cũ.
    * **Hệ quả:** Sai số góc làm "lẫn lộn" các đặc tính từ những hướng không gian khác (như hướng có số mũ bằng 0 hoặc âm). 
    * **Bế tắc (Trade-off):** Luôn phải thỏa hiệp giữa việc chọn véc-tơ ngắn (không vọt khỏi bộ hút) và véc-tơ đúng hướng (giảm sai số góc).

* **2. Lời nguyền Chiều (Curse of Dimensionality):**
    * **Đói dữ liệu:** Yêu cầu mật độ điểm khổng lồ, tăng theo hàm mũ (từ $10^d$ đến $30^d$ điểm với $d$ là số chiều).
    * **Thực tiễn:** Cực kỳ khó áp dụng cho dữ liệu y sinh ngắn như PPG ($d \approx 4-6$) vì thuật toán sẽ thất bại trong việc tìm điểm thay thế.

* **3. Nhạy cảm với Tham số (Parameter Sensitivity):**
    * **Chiều nhúng ($m$):** Nhỏ quá khiến quỹ đạo đè lên nhau (chọn nhầm láng giềng ở xa, gây sai số bùng nổ); lớn quá sẽ tạo không gian thừa cho nhiễu hoành hành.
    * **Thời gian tiến hóa (EVOLV):** Quá dài sẽ làm véc-tơ vọt qua các nếp gấp (đánh giá thấp $\lambda_1$); quá ngắn sẽ làm sai số góc cộng dồn liên tục.

* **4. Giới hạn Nhiễu (Noise Limitations):**
    * Bắt buộc thiết lập ngưỡng khoảng cách tối thiểu (SCALMN) để thuật toán không tính toán lầm trên dao động ngẫu nhiên. Chỉ hoạt động tốt với dữ liệu có độ phân giải tối thiểu $8$ bits có ý nghĩa.

* **5. Bất lực với Số mũ Âm (Negative Exponents):**
    * Chỉ hiệu quả để tìm Số mũ lớn nhất ($\lambda_1$). Các chiều không gian có số mũ âm sẽ co rút cực nhanh, chìm ngay vào dải nhiễu và sinh ra bất ổn định về mặt số học.

* **6. Cảnh báo Cốt lõi từ Tác giả:**
    * Lyapunov là đại lượng đo lường sự phân kỳ **dài hạn**. Việc cố gắng tính toán bằng cách "lấy trung bình các ước lượng phân kỳ cục bộ" là một thủ thuật cực kỳ nguy hiểm và sai lệch.