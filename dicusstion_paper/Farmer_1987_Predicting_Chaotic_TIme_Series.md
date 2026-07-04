### 1. Nền tảng Không gian: Tọa độ trễ (Delay Coordinates)
Để thoát khỏi sự phụ thuộc vào phương trình gốc, thuật toán bắt đầu bằng việc chuyển đổi chuỗi thời gian vô hướng 1D thành các vector trong không gian đa chiều.

Vector trạng thái tại thời điểm $t$ được định nghĩa bằng phương pháp tọa độ trễ:
$$
x(t) = (x(t), x(t-\tau), \dots, x(t-(d-1)\tau))
$$
* **Trong đó:** $x(t)$ là dữ liệu gốc, $\tau$ là thời gian trễ (delay time), và $d$ là số chiều không gian nhúng (embedding dimension).
* **Điều kiện cốt lõi:** Để bảo toàn cấu trúc hình học của hệ thống, không gian nhúng phải thỏa mãn $d \ge D$, với $D$ là số chiều thực sự của tập hút (attractor dimension).

---

### 2. Thiết lập Bài toán Dự báo & Metric Không gian
Mục tiêu là tìm một hàm ánh xạ $f_T$ mô tả sự tiến hóa của hệ thống từ hiện tại $x(t)$ tới tương lai $x(t+T)$:
$$
x(t+T) = f_T(x(t))
$$
Vì dữ liệu là hỗn loạn, hàm $f_T$ chắc chắn là phi tuyến. Thay vì tìm một hàm khổng lồ $F_T$ để xấp xỉ toàn cục, thuật toán sử dụng phép xấp xỉ cục bộ dựa trên khoảng cách.

Thuật toán áp đặt một độ đo (metric) $||\dots||$ lên không gian trạng thái. Nó sẽ tìm $k$ láng giềng gần nhất (nearest neighbors) của trạng thái hiện tại $x(t)$. Đó là các điểm $x(t')$ trong quá khứ ($t' < t$) sao cho khoảng cách sau đạt giá trị nhỏ nhất:
$$
||x(t) - x(t')||
$$

---

### 3. Hai Cấp độ "Học" Cục bộ (Local Predictors)
Sau khi tìm được $k$ láng giềng, hệ thống coi mỗi láng giềng $x(t')$ là một điểm ở tập xác định (domain) và trạng thái tương lai của nó $x(t'+T)$ là điểm tương ứng ở tập giá trị (range).

**A. Xấp xỉ Bậc 0 (Zeroth-order approximation / Nearest Neighbor)**
Đây là phương pháp đơn giản nhất, hoạt động với $k = 1$ láng giềng duy nhất.
$$
x_{pred}(t, T) = x(t'+T)
$$
* **Ý nghĩa:** Trực tiếp lấy giá trị tương lai của láng giềng gần nhất làm kết quả dự báo cho thời điểm hiện tại.

**B. Xấp xỉ Bậc 1 (First-order / Local Linear approximation)**
Phương pháp này chọn $k$ láng giềng sao cho $k > d$ (thường lớn hơn để đảm bảo tính ổn định). Hệ thống sẽ khớp một đa thức tuyến tính vào các cặp điểm $(x(t'), x(t'+T))$ thông qua bình phương tối thiểu (least squares).
$$
x_{pred}(t, T) = a_0 + \sum_{i=1}^{d} a_i x_i(t)
$$
* **Giải pháp ma trận:** Bài báo sử dụng kỹ thuật Phân tích giá trị suy biến (Singular-Value Decomposition - SVD) để tìm bộ hệ số $a_i$ nhằm tối thiểu hóa sai số trong vùng không gian cục bộ này.

---

### 4. Hệ thống Đánh giá Hiệu năng (Error Metric)
Để biết thuật toán dự báo tốt đến đâu, bài báo thiết lập chỉ số Sai số bình phương trung bình chuẩn hóa (Normalized Error - $E$).

* **Sai số dự báo (Root-mean-square error):**
$$
\sigma_{\Delta}(T) = \langle [x_{pred}(t, T) - x(t+T)]^2 \rangle^{1/2}
$$

* **Độ lệch chuẩn của dữ liệu gốc:**
$$
\sigma_x = \langle (x - \langle x \rangle)^2 \rangle^{1/2}
$$

* **Sai số Chuẩn hóa (Normalized Error):**
$$
E = \frac{\sigma_{\Delta}(T)}{\sigma_x}
$$
* **Đọc kết quả:** Nếu $E = 0$, dự báo hoàn hảo 100%. Nếu $E = 1$, thuật toán hoàn toàn vô dụng (kết quả không tốt hơn việc lấy giá trị trung bình của toàn bộ dữ liệu).

---

### 5. Định lý Giới hạn Dự báo (The Error Estimate Formula)
Đây là công thức toán học quan trọng nhất (Phương trình 2 trong bài báo), lượng hóa sự bất khả thi của việc dự báo dài hạn trong hệ hỗn loạn khi ở điều kiện lý tưởng (khoảng cách điểm dữ liệu lớn hơn mức nhiễu):
$$
E \approx C e^{(m+1)kT} N^{-(m+1)/D}
$$

* **Sự phân kỳ hàm mũ ($e^{(m+1)kT}$):** Sai số tăng theo hàm mũ dựa trên thời gian dự báo $T$ và hệ số $k$. (Khi dùng xấp xỉ bậc $m=0$, $k$ chính là số mũ Lyapunov lớn nhất; với các bậc khác, $k$ là metric entropy).
* **Sự bù đắp của dữ liệu ($N^{-(m+1)/D}$):** Sai số giảm xuống khi lượng điểm dữ liệu $N$ tăng lên, nhưng sự cải thiện này bị suy giảm nặng nề bởi số chiều của tập hút $D$.
* **Các tham số khác:** $m$ là bậc xấp xỉ (0 hoặc 1) và $C$ là một hằng số.