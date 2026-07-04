# Thuật toán False Nearest Neighbors (FNN)
**Nguồn:** *Determining embedding dimension for phase-space reconstruction using a geometrical construction* - Matthew B. Kennel (1992)

Thuật toán FNN được sử dụng để tìm số chiều nhúng tối thiểu $d_E$ (embedding dimension) nhằm bung mở hoàn toàn bộ hút của một hệ động lực từ chuỗi thời gian vô hướng 1D, dựa trên Định lý nhúng Takens.

---

## I. Bảng Chú thích Ký hiệu (Notations)

* **$N$**: Tổng số điểm dữ liệu của chuỗi thời gian.
* **$x(n)$**: Chuỗi thời gian vô hướng gốc thu được từ cảm biến ($n = 1, 2, ..., N$).
* **$T$**: Độ trễ thời gian (Time delay $\tau$).
* **$d$**: Chiều nhúng hiện tại đang được kiểm tra ($d=1, 2, 3...$).
* **$y(n)$**: Vectơ tọa độ của điểm dữ liệu thứ $n$ trong không gian $d$ chiều.
* **$y^{(r)}(n)$**: Láng giềng gần thứ $r$ của điểm $y(n)$. Trong tính toán thực tế, ta thường chỉ xét láng giềng gần nhất ($r=1$).
* **$R_d(n, r)$**: Khoảng cách Euclid từ điểm thứ $n$ đến láng giềng thứ $r$ của nó ở không gian $d$ chiều.

---

## II. Luồng Thực thi và Phương trình Toán học

### Bước 1: Khởi tạo kích thước toàn cục của hệ thống
Trước khi vào vòng lặp xét không gian, cần tính "kích thước vật lý" (bán kính hiệu dụng) của toàn bộ hệ thống $R_A$ để làm lớp giáp chống nhiễu.

**1. Tính Trọng tâm (Mean):**
$$\overline{x}=\frac{1}{N}\sum_{n=1}^{N}x(n)$$
> *Ý nghĩa:* Điểm cân bằng nằm chính giữa đám mây dữ liệu.

**2. Tính Kích thước Bộ hút (Variance/RMS size):**
$$R_{A}^{2}=\frac{1}{N}\sum_{n=1}^{N}[x(n)-\overline{x}]^{2}$$
> *Ý nghĩa:* Độ lệch chuẩn của toàn bộ dữ liệu, đại diện cho độ phình to tối đa của các quỹ đạo hệ thống.

---

### Bước 2: Vòng lặp xét Không gian (Bắt đầu từ $d=1$)

**1. Trải tọa độ không gian pha (Multivariate vectors):**
Cắt chuỗi 1D thành các vectơ tọa độ $d$ chiều theo định lý Takens (Phương trình 1):
$$y(n)=(x(n),x(n+T),...,x(n+(d-1)T))$$

**2. Tìm láng giềng và tính bình phương khoảng cách ($R_d$):**
Dùng thuật toán tìm kiếm (VD: KD-Tree) để tìm láng giềng thứ $r$ cho mọi điểm $n$. Tính bình phương khoảng cách giữa chúng ở không gian $d$ chiều (Phương trình 2):
$$R_{d}^{2}(n,r)=\sum_{k=0}^{d-1}[x(n+kT)-x^{(r)}(n+kT)]^{2}$$

---

### Bước 3: Phép thử nâng chiều ($d \rightarrow d+1$)
Ép cặp điểm $(y(n), y^{(r)}(n))$ lên không gian $d+1$ bằng cách thêm tọa độ ở nhịp trễ tiếp theo: $x(n+dT)$. 

Tính bình phương khoảng cách ở chiều không gian mới (Phương trình 3):
$$R_{d+1}^{2}(n,r)=R_{d}^{2}(n,r)+[x(n+dT)-x^{(r)}(n+dT)]^{2}$$
> *Ý nghĩa:* Khoảng cách mới = Khoảng cách cũ + Độ chênh lệch thuần túy do trục tọa độ mới tạo ra.

---

### Bước 4: Phán quyết Láng giềng giả (False Neighbor)
Một điểm sẽ bị gắn cờ là "Láng giềng giả" nếu nó trượt **một trong hai** tiêu chí sau đây:

**Tiêu chí 1: Sự kéo giãn tương đối (Relative Stretch)**
Kiểm tra xem tỷ lệ gia tăng khoảng cách khi chuyển sang chiều $d+1$ có vượt quá ngưỡng cho phép hay không (Phương trình 4):
$$\left[ \frac{R_{d+1}^{2}(n,r)-R_{d}^{2}(n,r)}{R_{d}^{2}(n,r)} \right]^{1/2} = \frac{|x(n+Td)-x^{(r)}(n+Td)|}{R_{d}(n,r)} > R_{tol}$$
> *Ý nghĩa:* Nếu phần giãn ra trên trục mới lớn gấp nhiều lần khoảng cách ban đầu ($R_{tol} \ge 10$), sự gần gũi ở chiều $d$ chỉ là ảo ảnh do phép chiếu.

**Tiêu chí 2: Kích thước tuyệt đối (Absolute Size)**
Lớp giáp chống nhiễu ngẫu nhiên. So sánh khoảng cách ở chiều mới với kích thước tổng thể của hệ thống (Phương trình 5):
$$\frac{R_{d+1}(n)}{R_{A}} > A_{tol}$$
> *Ý nghĩa:* Nếu ở chiều $d+1$, khoảng cách giữa hai láng giềng giãn ra to bằng khoảng $A_{tol}$ lần (thường $A_{tol} = 2.0$) bán kính toàn cục $R_A$, đây là hai điểm nhiễu bị ném văng ra xa chứ không tuân theo động lực học.

---

### Bước 5: Thống kê và Điều kiện dừng

**1. Tính tỷ lệ FNN:**
$$\text{Tỷ lệ FNN (\%)} = \frac{\text{Số lượng Láng giềng giả}}{\text{Tổng số điểm hợp lệ}} \times 100\%$$

**2. Quy tắc cuốn chiếu:**
* Nếu tỷ lệ FNN vẫn ở mức cao: Tăng $d = d+1$ và lặp lại từ Bước 2.
* **Điểm dừng (Xác định $m$):** Vòng lặp kết thúc khi Tỷ lệ FNN rớt xuống $\approx 0\%$ (với dữ liệu sạch) hoặc tạo thành một đường "cao nguyên" nằm ngang, không thể giảm thêm (với dữ liệu thực có nhiễu). Giá trị $d$ tại điểm bão hòa này chính là **Chiều nhúng tối thiểu ($m$)**.

# 📌 TỔNG KẾT: BÀI BÁO FNN (MATTHEW KENNEL, 1992)

## 1. Đóng góp cốt lõi (Ưu điểm)
* **Chẩn đoán định lượng:** Biến việc tìm chiều nhúng $d_E$ từ chỗ "nhìn bằng mắt" sang một thang đo tỷ lệ phần trăm (0% - 100%) rõ ràng, giúp tiết kiệm tài nguyên tính toán cho các khâu phía sau.
* **Tấm khiên chống nhiễu ($A_{tol}$):** Là một trong những thuật toán tiên phong phân biệt được *Hỗn mang tất định* (số chiều hữu hạn - tỷ lệ FNN rớt về 0) và *Nhiễu ngẫu nhiên* (số chiều vô hạn - tỷ lệ FNN treo ở mức cao).
* **Minh chứng "Hiện tượng Cao nguyên":** Khi tín hiệu pha nhiễu, tỷ lệ FNN không về 0% mà tạo thành một bình nguyên (plateau) đi ngang. Chiều nhúng tối ưu được chọn tại "điểm uốn" của đồ thị.

## 2. Hạn chế thực tiễn (Điểm nghẽn tự động hóa)
* **Ràng buộc chặt chẽ với Time Delay ($\tau$):** Thuật toán sẽ sụp đổ (báo cáo sai số chiều) nếu nạp sai giá trị $\tau$ (quá nhỏ gây hiệu ứng đường chéo, quá lớn làm vỡ tương quan). Bắt buộc phải kết hợp với Mutual Information (KSG).
* **Phụ thuộc vào Ngưỡng kinh nghiệm:** Bắt người dùng phải tự tinh chỉnh thủ công các tham số $R_{tol}$ (10-15) và $A_{tol}$ (2.0). Điều này khiến việc đưa thuật toán vào một pipeline AI tự động chạy Real-time là cực kỳ rủi ro.

---

# 🚀 MỞ RỘNG: SỰ TIẾN HÓA CỦA CÁC THUẬT TOÁN TÌM CHIỀU NHÚNG

Sau rào cản về "Ngưỡng cắt cứng nhắc" của Kennel, cộng đồng Động lực học phi tuyến (NTSA) đã có những bước tiến vượt bậc để tự động hóa hoàn toàn bài toán này:

### 1. Cao's Method (Liyang Cao, 1997) - "Tiêu chuẩn Vàng" thực chiến
Đây là bản nâng cấp trực tiếp và triệt để nhất từ FNN của Kennel, giải quyết 100% bài toán tự động hóa:
* **Không cần tham số:** Khử hoàn toàn $R_{tol}$ và $A_{tol}$.
* **Đại lượng bão hòa ($E_1$):** Chuyển từ "Đếm số lượng điểm" sang đo "Sự bão hòa của khoảng cách trung bình". Máy tính chỉ cần dò điểm đi ngang của đường cong $E_1$ để chốt $m$.
* **Radar dò nhiễu ($E_2$):** Bổ sung một chỉ số riêng biệt, tiến về 1 nếu là tín hiệu hỗn mang thật, và dao động hỗn loạn nếu là nhiễu thuần túy.

### 2. Phân tích Dữ liệu Topo (Topological Data Analysis - TDA)
Ở các thập kỷ sau, toán học Topo hiện đại can thiệp sâu hơn bằng công cụ **Persistent Homology** (Homology bền vững). Thay vì đếm láng giềng, người ta theo dõi sự hình thành và biến mất của các "lỗ hổng" (holes) trong dữ liệu khi tăng bán kính quét. Thuật toán này lỳ lợm với nhiễu y sinh học (như PPG, EEG) đến mức không cần quan tâm đến các nếp gấp cục bộ.

### 3. False Nearest Strands (FNS - Kennamer, 1998)
Một biến thể dành riêng cho dữ liệu cực ngắn. Thay vì xét từng điểm (points) như FNN, FNS xét sự đan chéo của **cả một đoạn quỹ đạo** (strands). Nó chống chịu cực tốt với hiệu ứng "Oversampling" (lấy mẫu quá dày) ở các cảm biến hiện đại.

### 4. Học Sâu Hỗn mang (Chaos-Informed Deep Learning - Hiện tại)
Trong các kiến trúc AI Real-time đương đại, người ta không còn tìm $m$ một cách tường minh nữa. Các mạng Convolutional Neural Networks 1D (CNN-1D) kết hợp với Cơ chế chú ý (Attention) được thiết kế để tự động nội suy và trích xuất các đặc trưng topo ở nhiều chiều không gian ẩn (latent spaces) khác nhau thẳng từ tín hiệu 1D gốc. Tuy nhiên, việc hiểu bản chất $m$ từ Kennel và Cao vẫn là nền tảng bắt buộc để kỹ sư thiết kế hàm Loss function và cấu trúc mạng cho hợp lý.