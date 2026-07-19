# Phương pháp Cao (1997): Xác định Chiều nhúng Tối thiểu

So với các nghiên cứu khác (như thuật toán FNN của Kennel 1992 vốn phụ thuộc vào các ngưỡng chủ quan $R_{tol}$ và $A_{tol}$), Liyang Cao đã đề xuất một kiến trúc tính toán hoàn toàn tự động. Phương pháp này dựa trên việc đo lường sự thay đổi khoảng cách trung bình của các quỹ đạo thay vì đếm số lượng láng giềng giả.

---

## 1. Không gian Pha và Chuẩn Khoảng cách

*   **Vectơ tọa độ trễ:** Điểm dữ liệu thứ $i$ trong không gian $d$ chiều được định nghĩa theo định lý Takens:
    $$y_i(d)=(x_i,x_{i+\tau},...,x_{i+(d-1)\tau})$$
*   **Chuẩn Maximum:** Để tăng tốc độ tính toán, Cao đo khoảng cách giữa hai điểm $k$ và $l$ trong không gian $m$ chiều bằng độ lệch lớn nhất trên các trục tọa độ (thay vì chuẩn Euclid):
    $$||y_k(m)-y_l(m)||=\max_{0\le j\le m-1}|x_{k+j\tau}-x_{l+j\tau}|$$

---

## 2. Chỉ số $E_1(d)$: Đại lượng Bão hòa Không gian

Mục tiêu của $E_1$ là tìm ra thời điểm mà việc tăng thêm chiều không gian không còn làm các nếp gấp của quỹ đạo bị kéo giãn thêm nữa.

**Bước 2.1: Đo tỷ lệ kéo giãn cục bộ**
Với mỗi điểm $y_i(d)$, tìm láng giềng gần nhất của nó là $y_{n(i,d)}(d)$. Khi nâng lên không gian $d+1$, sự kéo giãn khoảng cách giữa hai điểm này được tính bằng tỷ số:
$$a(i,d)=\frac{||y_i(d+1)-y_{n(i,d)}(d+1)||}{||y_i(d)-y_{n(i,d)}(d)||}$$
*(Lưu ý: Chỉ số láng giềng $n(i,d)$ được xác định ở chiều $d$, và dùng chung cho cả tử số lẫn mẫu số).*

**Bước 2.2: Sức căng trung bình toàn hệ thống**
Tính giá trị trung bình của toàn bộ các tỷ lệ kéo giãn trên toàn quỹ đạo:
$$E(d)=\frac{1}{N-d\tau}\sum_{i=1}^{N-d\tau}a(i,d)$$

**Bước 2.3: Chỉ số $E_1$**
Lập tỷ số giữa sức căng trung bình của hai không gian liên tiếp:
$$E_1(d)=\frac{E(d+1)}{E(d)}$$
*   **Ý nghĩa Toán học:** Khi không gian đạt đủ độ rộng (vượt qua chiều nhúng tối thiểu), bộ hút đã được bung mở hoàn toàn. Sức căng trung bình $E(d)$ sẽ ngừng thay đổi, kéo theo $E_1(d)$ tiến tới bão hòa (đi ngang) và tiệm cận giá trị **1.0**.

---

## 3. Chỉ số $E_2(d)$: Radar Nhận diện Nhiễu (Noise)

Do dữ liệu thực tế có giới hạn về số lượng mẫu ($N$), chỉ số $E_1(d)$ của một tín hiệu ngẫu nhiên thuần túy đôi khi vẫn báo bão hòa giả tạo. $E_2(d)$ được thiết kế như một lớp khiên độc lập để lọc bỏ các tín hiệu rác này.

**Bước 3.1: Khoảng cách tuyệt đối trên trục tương lai**
Thay vì đo toàn bộ không gian, đại lượng này chỉ đo sự chênh lệch khoảng cách trên **trục tọa độ mới được thêm vào** (tọa độ thứ $d+1$):
$$E^*(d)=\frac{1}{N-d\tau}\sum_{i=1}^{N-d\tau}|x_{i+d\tau}-x_{n(i,d)+d\tau}|$$

**Bước 3.2: Chỉ số $E_2$**
Tỷ lệ sự biến thiên của đại lượng này giữa hai không gian:
$$E_2(d)=\frac{E^*(d+1)}{E^*(d)}$$
*   **Ý nghĩa Toán học:** 
    *   **Nếu là tín hiệu động lực học (Chaos):** Các giá trị tương lai bị ràng buộc bởi quá khứ. Khoảng cách này phải phụ thuộc vào cấu trúc không gian, nên $E_2(d)$ sẽ thay đổi và **chắc chắn tồn tại các điểm $E_2(d) \ne 1$**.
    *   **Nếu là nhiễu ngẫu nhiên (White/Colored Noise):** Giá trị tương lai hoàn toàn vô trật tự và độc lập. Sự chênh lệch trên trục mới chỉ là sự dao động ngẫu nhiên không đổi. Do đó, $E_2(d)$ sẽ luôn xấp xỉ bằng **1.0** ở mọi chiều $d$.

---

## 4. Tiêu chí Phán quyết (Decision Rule)

Để tự động hóa việc chốt chiều nhúng tối thiểu ($m$), thuật toán cần đồng thời kiểm tra cả hai điều kiện trên biểu đồ:

1.  **Dò tín hiệu hợp lệ:** Kiểm tra đường cong $E_2(d)$. Nếu nó dao động và khác 1 ở các chiều thấp, tín hiệu được xác nhận là chứa động lực học (không phải nhiễu thuần túy).
2.  **Chốt chiều nhúng $m$:** Quan sát đường cong $E_1(d)$. Tìm giá trị $d_0$ đầu tiên mà tại đó $E_1(d)$ bắt đầu đi ngang (bão hòa) và không thay đổi đáng kể khi tiếp tục tăng $d$. Chiều nhúng tối thiểu của hệ thống sẽ là $m=d_0+1$.
3.  

# Đánh giá Phương pháp Cao (1997) và Kiến trúc Hệ thống Thực chiến

Bản tổng hợp này đúc kết các đặc tính cốt lõi của phương pháp Cao (1997) thông qua 4 kịch bản thực nghiệm số học, làm tiền đề để xây dựng luồng xử lý (pipeline) cho các bài toán phân tích tín hiệu y sinh phức tạp (như trích xuất đặc trưng nhịp tim PPG để nhận diện trạng thái mệt mỏi của người lái xe).

---

## I. NHỮNG ĐỘT PHÁ LÝ THUYẾT (Ưu điểm)

1. **Khách quan & Tự động hóa hoàn toàn:**
   * Khai tử hoàn toàn các tham số ngưỡng chủ quan ($R_{tol}, A_{tol}$) của phương pháp FNN (Kennel, 1992).
   * Máy tính có thể tự động chốt chiều nhúng $m$ khi đại lượng sức căng trung bình $E_1(d)$ bão hòa và đi ngang.
2. **Radar chống nhiễu xuất sắc ($E_2$):**
   * Đại lượng $E_2$ tạo ra ranh giới rõ ràng: Dao động mạnh với hệ hỗn mang (Chaos) và bám chặt mốc $1.0$ với nhiễu ngẫu nhiên (White Noise).
   * Hoạt động như một chốt chặn hiệu quả để lọc bỏ các đoạn tín hiệu rác trước khi đưa vào phân tích chuyên sâu.

---

## II. "GÓT CHÂN ACHILLES" KHI THỰC CHIẾN (Nhược điểm)

1. **Sụp đổ trước Nhiễu pha trộn (Low SNR):**
   * Nếu tín hiệu gốc bị trộn nhiễu (VD: nhiễu quang học, rung lắc cơ học 15dB), phép toán "trung bình cộng" của Cao bị sai lệch hoàn toàn. $E_1$ mất khả năng bão hòa và $E_2$ bị "mù" (báo sai thành nhiễu ngẫu nhiên).
2. **Hiện tượng "Không gian rỗng" ở Cửa sổ siêu ngắn:**
   * Khi kích thước mẫu quá nhỏ (VD: $N=250$ điểm, tương đương 5s tín hiệu ở 50Hz), khoảng cách láng giềng bị kéo giãn sai lệch. Thuật toán mất độ chính xác, $E_1$ bão hòa chậm và $E_2$ mất tính ổn định. Đòi hỏi $N \ge 1000$.
3. **Lệ thuộc tuyệt đối vào Time Delay ($\tau$):**
   * Thuật toán bị đánh lừa hoàn toàn nếu mớm sai $\tau$. Nếu $\tau$ quá nhỏ (Oversampling), hệ thống bị bóp méo, $E_1$ chốt sai $m$ và $E_2$ nhận diện nhầm thành nhiễu.

---

## III. KIẾN TRÚC PIPELINE BẮT BUỘC CHO TÍN HIỆU THỰC TẾ

Để hệ thống AI chạy ổn định theo thời gian thực mà không bị sụp đổ bởi các nhược điểm trên, luồng xử lý dữ liệu bắt buộc phải tuân thủ 4 bước:

* **Bước 1 (Tiền xử lý DSP):** Tín hiệu thô phải đi qua bộ lọc (VD: Butterworth Bandpass) để cạo sạch nhiễu nền và nhiễu cử động. Đây là khiên chắn bảo vệ thuật toán Cao.
* **Bước 2 (Thiết kế Cửa sổ Trượt):** Kích thước cửa sổ cắt tín hiệu phải đủ dài (15 - 20 giây) để đảm bảo lượng dữ liệu $N \ge 1000$ điểm, cung cấp đủ chu kỳ động lực học.
* **Bước 3 (Chốt $\tau$ Tối ưu):** Bắt buộc chạy qua thuật toán Thông tin tương hỗ (Mutual Information / KSG) để tìm chính xác độ trễ pha $\tau$.
* **Bước 4 (Triển khai Cao Method):** Sau khi đã có dữ liệu sạch, đủ dài và $\tau$ chuẩn, hàm toán học của Cao mới được kích hoạt để tự động xuất ra chiều nhúng $m$ chuẩn xác nhất cho mạng Neural Network.