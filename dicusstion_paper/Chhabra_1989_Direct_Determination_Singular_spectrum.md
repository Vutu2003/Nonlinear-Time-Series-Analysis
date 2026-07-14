### 1. Động Lực Nghiên Cứu (Motivation)
Việc xác định phổ kỳ dị $f(\alpha)$ từ dữ liệu thực nghiệm (đặc biệt ở các hệ hỗn loạn chiều thấp chưa rõ động lực học cơ sở) từng đối mặt với hai rào cản chí mạng:
* **Sự sụp đổ của Phép biến đổi Legendre:** Phương pháp cũ (Halsey, 1986) tính $f(\alpha)$ gián tiếp qua đạo hàm số trị từ $D_q$. Với dữ liệu nhiễu, thuật toán buộc phải "làm trơn" (smoothing) tín hiệu, dẫn đến sinh ra các dải sai số giả tạo và xóa sổ các hiện tượng đứt gãy vật lý cốt lõi (như sự chuyển pha).
* **Sai số từ các phương pháp trực tiếp thô sơ:** Các kỹ thuật log-log đương thời nhầm lẫn giữa số chiều Hausdorff và Box-counting. Chúng thất bại trong việc xử lý hiệu chỉnh logarit kích thước, khiến kết quả bị đánh giá hụt (undershoot) nghiêm trọng tại vùng đỉnh $D_0$.

---

### 2. Thiết kế Thuật toán Chhabra-Jensen (Step-by-Step)
Tác giả đề xuất một phương pháp tính trực tiếp (canonical method) dựa trên nền tảng Lý thuyết Thông tin (Shannon) và Lý thuyết Đo lường (Billingsley), loại bỏ hoàn toàn đạo hàm Legendre:

* **Bước 1: Tính xác suất thô $P_i(L)$**
Bủa lưới gồm các ô kích thước $L$ lên tập hỗ trợ (support) và tính xác suất tích lũy $P_i(L)$ rơi vào từng ô $i$.
* **Bước 2: Xây dựng hệ xác suất chuẩn hóa $p_i(q, L)$**
Thay vì tính tổng thô bạo gây tràn bộ nhớ khi $q < 0$, tác giả "chuẩn hóa" xác suất để giới hạn mọi giá trị luôn nằm trong khoảng an toàn:
$$p_i(q,L)=\frac{[P_i(L)]^q}{\sum_j [P_j(L)]^q}$$
* **Bước 3: Giải mã phổ mật độ $f(q)$ bằng Entropy**
Dựa trên định lý Billingsley, tính trực tiếp số chiều $f(q)$ qua tỷ lệ thay đổi giữa Entropy chuẩn hóa và logarit kích thước ô:
$$f(q)=\lim_{L \to 0}\frac{\sum_i p_i(q,L)\log[p_i(q,L)]}{\log L}$$
* **Bước 4: Trích xuất trực tiếp sức mạnh kỳ dị $\alpha(q)$**
Tính giá trị trung bình của sức mạnh kỳ dị bằng cách dùng hệ xác suất chuẩn hóa làm trọng số cho xác suất gốc:
$$\alpha(q)=\lim_{L \to 0}\frac{\sum_i p_i(q,L)\log[P_i(L)]}{\log L}$$
* **Bước 5: Lách qua Legendre bằng Hồi quy tuyến tính**
Quét tham số $q$ từ âm sang dương. Tại mỗi giá trị $q$, vẽ đồ thị các tử số (ở Bước 3 và 4) theo trục hoành $\log L$. Hệ số góc (slope) của các đường hồi quy tuyến tính này sẽ trả về chính xác tọa độ trực tiếp của $f(q)$ và $\alpha(q)$ để dựng thành đồ thị hình nắp chuông $f(\alpha)$.

---

### 3. Kết Luận (Conclusion)
Thuật toán Chhabra & Jensen (1989) thiết lập một tiêu chuẩn vàng thực chiến cho phổ kỳ dị đa phân dạng với 3 đột phá:
* **Bảo toàn vật lý:** Cắt bỏ hoàn toàn phép đạo hàm Legendre và khâu làm trơn dữ liệu, giữ nguyên vẹn mọi đứt gãy tự nhiên của hệ thống.
* **Ổn định thống kê:** Giải quyết triệt để bài toán bùng nổ giá trị và nhiễu do lấy mẫu kém ở các vùng dữ liệu kỳ dị cực đoan.
* **Độ chính xác tuyệt đối:** Chạm mốc hoàn hảo tại đỉnh nắp chuông ($D_0$) ngay cả trên dữ liệu chuỗi 1D nhiễu động (nơi các phương pháp cũ bị sai lệch tới 20%).