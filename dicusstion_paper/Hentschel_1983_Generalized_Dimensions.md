# Generalized dimensions

Để các công thức hoạt động, ta bủa một lưới không gian gồm các ô có kích thước $b$ lên một Attractor chứa $N$ điểm dữ liệu [1]:
* **$M(b)$**: Số lượng các ô thực sự có chứa dữ liệu [1].
* **$p_k$**: Xác suất điểm rơi vào ô thứ $k$ (tính bằng số điểm trong ô $k$ chia cho $N$) [1].

**Điều kiện sống còn:** Cả 3 đại lượng cốt lõi đều phải lấy giới hạn đồng thời $\lim_{b \to 0}$ và $\lim_{N \to \infty}$ [2]. Trong thực tiễn, kích thước ô $b$ phải rất nhỏ so với thang đo toàn cục, nhưng hệ thống phải có đủ lượng dữ liệu khổng lồ ($N$) để mỗi ô lưới không bị rơi vào tình trạng rỗng hay chỉ có một vài điểm [3].

### 1. $D_0$: Số chiều Tự đồng dạng / Phân dạng (Capacity / Fractal Dimension)
* **Công thức:** 
  $D_0 = - \lim_{b \to 0} \lim_{N \to \infty} \frac{\log M(b)}{\log b}$ [2]
* **Ý nghĩa:** Đo lường "khung xương hình học" thô của hệ thống. Thuật toán cào bằng mọi thứ: Nó chỉ đếm xem một ô có dữ liệu hay không, phớt lờ hoàn toàn việc ô đó chứa 1 điểm hay 1 triệu điểm. Nó đại diện cho góc nhìn hình học thuần túy.

### 2. $D_1$: Số chiều Thông tin (Information Dimension)
* **Công thức:** Lấy nền tảng từ Entropy Shannon $S(b) = - \sum p_k \log p_k$ [2]: 
  $D_1 = - \lim_{b \to 0} \lim_{N \to \infty} \frac{S(b)}{\log b}$ [2]
* **Ý nghĩa:** Đại diện cho góc nhìn mật độ (xác suất đơn). Bằng cách tính xác suất $p_k$, nó đo lường lượng thông tin cần thiết để xác định trạng thái của hệ thống. Nó bắt đầu phân biệt được vùng dữ liệu tập trung dày đặc và vùng thưa thớt.

### 3. $D_2$: Số mũ Tương quan (Correlation Dimension)
* **Công thức:** Dựa trên tích phân tương quan $C(b)$ (đếm số cặp điểm có khoảng cách nhỏ hơn $b$) [4]: 
  $D_2 = \lim_{b \to 0} \lim_{N \to \infty} \frac{\log C(b)}{\log b}$ [2]
* **Ý nghĩa:** Đại diện cho sự tương tác cặp (Pairs). Khác với $D_1$ chỉ xét từng điểm đơn lẻ rơi vào ô, $D_2$ đánh giá xác suất để hai điểm ngẫu nhiên bất kỳ trên quỹ đạo tiến lại gần nhau trong khoảng cách $b$.

### 4. Công thức Tổng quát $D_q$ & Các bậc cao hơn
Thay vì tính riêng lẻ, bài báo đã chứng minh tất cả được quy về một dạng tổng quát cho mọi $q > 0$ [5], [6]:
* **Công thức:** 
  $D_q = \frac{1}{q-1} \lim_{b \to 0} \frac{\log \sum p_i^q}{\log b}$ [7]
* **Ý nghĩa:** Khi $q = 3, 4, \dots$, các số chiều này đo lường sự tương quan không gian của các cụm 3 điểm (triplets), 4 điểm (quadruplets)... lặp lại trong hệ thống [6]. Tập hợp vô hạn các số chiều $D_q$ này tạo thành một "hồ sơ đặc tả vật lý" hoàn chỉnh cho Attractor [8].

### TÍNH CHẤT ĐỈNH CAO: Bất đẳng thức Đa phân dạng
Tất cả các số chiều này bị ràng buộc bởi một định lý giải tích tuyệt đẹp [9]: 
$D_0 \ge D_1 \ge D_2 \ge \dots \ge D_\infty$ [10]

* **Dấu "=" xảy ra khi:** Hệ thống đồng nhất tuyệt đối (homogeneous), tức là dữ liệu rải đều tăm tắp [9], [11].
* **Dấu ">" (Sự chênh lệch):** Là bằng chứng định lượng cho tính chất phi tuyến và không đồng nhất. Khoảng cách giữa các $D$ càng lớn, mức độ dao động về mật độ dữ liệu (từ cực kỳ đặc đến cực kỳ thưa) của Attractor càng dữ dội [12].

# Hạn chế thực tiễn khi tính toán họ số chiều tổng quát $D_q$

Khi bước từ lý thuyết giải tích hoàn hảo xuống tính toán trên chuỗi thời gian thực tế, các tác giả đã thừa nhận 4 rào cản chí mạng sau [1, 2]:

### 1. Sự "Độc tôn" của Số mũ tương quan ($D_2$)
Mặc dù có vô hạn các số chiều $D_q$, tác giả thừa nhận rằng $D_2$ (Correlation exponent, $\nu$) là đại lượng **duy nhất dễ dàng tính toán** từ một chuỗi thời gian thực tế [1]. 

### 2. Sự kém hiệu quả của thuật toán Box-Counting
Để tính toán toàn bộ dải phổ $D_q$ (bao gồm $D_0$ và $D_1$) từ một tập dữ liệu, thuật toán bủa lưới (Box-counting) là bắt buộc. Tuy nhiên, nó được khẳng định là **kém hiệu quả (inefficient) hơn rất nhiều** so với các thuật toán chuyên biệt dùng để tính riêng $D_2$ [1]. 

### 3. Nghịch lý giới hạn kích thước ô và lượng dữ liệu
Toán học yêu cầu kích thước ô $b \to 0$ và số điểm dữ liệu $N \to \infty$ [2]. Trong thực tiễn, điều này sinh ra một nghịch lý ép kiểu:
* Kích thước ô $b$ phải cực kỳ nhỏ so với tỷ lệ toàn cục.
* Nhưng nó vẫn **phải đủ lớn để đảm bảo chứa một số lượng điểm dữ liệu lớn** bên trong [2].
Với các chuỗi dữ liệu y sinh học ngắn và nhiễu (như PPG), việc tìm ra một ô lưới thỏa mãn cả hai điều kiện này là cực kỳ khó khăn.

### 4. Thiếu vắng "Nhóm biến đổi tái chuẩn hóa" cho dữ liệu thực
Trên các hệ lý thuyết (như Feigenbaum), các thông số xác suất và tỷ lệ chia tỷ xích có thể được tính bằng phương trình giải tích chính xác (rescaling transformation group). Nhưng với dữ liệu thực tế, các thông số này không được biết trước [1]. Người ta buộc phải dùng các phương pháp ước lượng số trị (numerical estimates), điều này luôn đi kèm với sai số hệ thống khổng lồ [1].