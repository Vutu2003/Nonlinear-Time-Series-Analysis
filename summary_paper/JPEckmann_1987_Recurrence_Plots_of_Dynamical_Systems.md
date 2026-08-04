# Paper Metadata
* **Title:** Recurrence Plots of Dynamical Systems
* **Authors:** J.-P. Eckmann, S. Oliffson Kamphorst, and D. Ruelle
* **Year:** 1987
* **Keywords:** Dynamical systems, Time series, Recurrence plots, Fluctuation phenomena, Random processes

# 1. Why (Nguồn gốc và Động lực của Recurrence Plot)

* **Bối cảnh & Phương pháp cũ:** Các phương pháp phi tuyến đương thời (Entropy, Lyapunov, Information Dimension) chủ yếu cung cấp các **chỉ số định lượng toàn cục**. Chúng đòi hỏi các giả định khắt khe (dữ liệu dài, hệ tự trị) và không thể hiện được cấu trúc động lực học theo thời gian.
* **Khoảng trống nghiên cứu:** Thiếu một **công cụ chẩn đoán trực quan** để kiểm tra tính hợp lệ của các giả định lý thuyết trên dữ liệu thực nghiệm (thường ngắn, không dừng, hoặc có tham số trôi chậm).
* **Mục tiêu & Câu hỏi nghiên cứu:** Xây dựng một biểu diễn đồ họa để trực quan hóa sự lặp lại (recurrence) của quỹ đạo trong không gian pha. Mục đích là để nhận biết các tương quan thời gian tinh tế và các thang thời gian đặc trưng.
* **Giá trị mang lại:** Tạo ra một công cụ chẩn đoán giúp:
  * Kiểm tra các giả định trước khi áp dụng các phương pháp định lượng.
  * Bộc lộ các cấu trúc ẩn (dao động chậm, tính không dừng, sự trôi).
  * Cung cấp thông tin động lực học hữu ích ngay cả khi các giả định lý thuyết khắt khe bị vi phạm.

# 2.What (Recurrence Plot - Nội dung, Điểm mới và Nền tảng (Eckmann, 1987))

*   **Core Insight:** RP là công cụ đồ họa chẩn đoán dùng để trực quan hóa sự lặp lại (recurrence) của quỹ đạo. Mục đích chính là kiểm tra các giả định phi tuyến và bộc lộ các cấu trúc động lực học ẩn (trôi tham số, dao động chậm, tính không dừng).
*   **Novelty:** Đột phá bằng việc chuyển từ **định lượng bằng chỉ số toàn cục** (như Entropy, Lyapunov) sang **biểu diễn trực quan** toàn bộ cấu trúc không gian pha.
*   **Đặc trưng hình ảnh:**
    *   *Vĩ mô (Large-scale):* Đồng nhất (hệ tự trị/dừng), Nhạt màu xa đường chéo (hệ trôi tham số), Dải rộng (hệ có dao động chậm).
    *   *Vi mô (Small-scale):* Đường chéo (quỹ đạo tiến hóa song song; độ dài tỷ lệ nghịch với số mũ Lyapunov dương lớn nhất), Bàn cờ (dao động quanh các điểm cân bằng), Trống/Rời rạc (dữ liệu ngẫu nhiên).
*   **Cơ sở Toán học:**
    *   *Tái dựng không gian pha:* Bằng phương pháp trễ thời gian $x(i) = (u_i, u_{i+\tau}, ..., u_{i+(d-1)\tau})$.
    *   *Bán kính thích nghi:* $r(i)$ thay đổi động theo từng trạng thái $x(i)$ (chọn sao cho có khoảng 10 láng giềng) thay vì cố định.
    *   *Điều kiện hồi quy:* Đánh dấu điểm $(i,j)$ nếu $x(j)$ nằm trong bán kính $r(i)$ của $x(i)$.
    *   *Tính đối xứng:* Đồ thị gần đối xứng qua đường chéo $i=j$, nhưng không đối xứng tuyệt đối do $r(i) \neq r(j)$.
*   
# 3. How (Cách thức hoạt động của Recurrence Plot (Eckmann, 1987))

### 3.1. Thuật toán xây dựng (Algorithm)
*   **Tái dựng không gian pha:** Chuyển chuỗi vô hướng thành quỹ đạo không gian $d$-chiều bằng kỹ thuật trễ thời gian: $x(i) = (u_i, u_{i+\tau}, \dots, u_{i+(d-1)\tau})$[cite: 1].
*   **Lân cận thích nghi:** Sử dụng bán kính động $r(i)$ thay đổi theo từng vị trí $x(i)$ sao cho bao chùm được khoảng $10$ điểm láng giềng[cite: 1].
*   **Vẽ RP:** Đánh dấu điểm tại tọa độ $(i,j)$ nếu $x(j)$ cách $x(i)$ một khoảng nhỏ hơn $r(i)$[cite: 1]. Biểu đồ không đối xứng tuyệt đối do $r(i) \neq r(j)$[cite: 1].

### 3.2. Quy trình chẩn đoán (Diagnostic Procedure)
*   Dữ liệu gốc $\rightarrow$ Tái dựng không gian pha $\rightarrow$ Vẽ RP $\rightarrow$ Quan sát vĩ mô (Đồng nhất, Sự trôi, Dao động chậm) $\rightarrow$ Quan sát vi mô (Đường chéo, Bàn cờ) $\rightarrow$ Kết luận tính chất động lực học[cite: 1].

### 3.3. Darkness Histogram
*   Tính mật độ điểm hồi quy theo khoảng cách thời gian $|i-j|$[cite: 1].
*   Công cụ này giúp định lượng hiện tượng trôi tham số (parameter drift) khi mắt người khó phân biệt sự thay đổi độ đậm nhạt trên toàn bộ biểu đồ[cite: 1].

### 3.4. Đặc điểm tính toán & Lưu ý
*   **Đặc điểm:** Phương pháp tiếp cận hoàn toàn dựa trên dữ liệu (data-driven), không cần giả định trước về mô hình, độ phức tạp $O(N^2)$.
*   **Giới hạn (so với hiện đại):** Bài báo gốc chưa đề cập đến cách chọn tối ưu tham số $d$ và $\tau$, chưa định nghĩa RQA hay sử dụng bán kính ngưỡng cố định (fixed threshold).
*   

## 4. Validation: Kiểm chứng Recurrence Plot (Eckmann, 1987)

*   **Chiến lược & Giả định:** Sử dụng các thực nghiệm thay vì chứng minh toán học để kiểm tra hai giả định khắt khe của phân tích phi tuyến: hệ tự trị (không chứa thời gian tường minh) và chuỗi dữ liệu dài[cite: 1].
*   **Thực nghiệm 1 (Hệ Hénon):** Với 20.000 điểm và chiều nhúng $d=8$, cấu trúc biểu đồ đồng nhất (homogeneous) chứng minh khả năng mô tả hệ tự trị và dừng[cite: 1].
*   **Thực nghiệm 2 (Hệ Lorenz có trôi):** Khi thêm 10% drift, đồ thị nhạt dần khi rời xa đường chéo, chứng minh RP nhạy bén với sự thay đổi chậm (parameter drift) của hệ thống[cite: 1].
*   **Thực nghiệm 3 (Dữ liệu Ciliberto):** Với 40.000 điểm thực nghiệm và $d=9$, RP bộc lộ rõ kiểu hình tuần hoàn (periodic typology) là các dao động chậm xếp chồng lên chuyển động hỗn loạn vốn bị che khuất trong chuỗi gốc[cite: 1].
*   **Darkness Histogram:** Công cụ đếm mật độ điểm lặp theo khoảng cách $|i-j|$ được đề xuất để định lượng hiện tượng trôi, khắc phục giới hạn của mắt người trong việc nhận biết các thay đổi sắc độ nhỏ[cite: 1].
*   **Giới hạn:** Phụ thuộc vào quan sát mắt thường[cite: 1]. Việc phân định giữa cấu trúc vĩ mô và vi mô đôi khi khó khăn, điển hình như kết cấu bàn cờ có thể mở rộng ra quy mô lớn[cite: 1].
*   **Kết luận:** RP chứng minh được giá trị cốt lõi là một công cụ chẩn đoán trực quan giúp bộc lộ các cấu trúc thời gian tinh tế, hoạt động hiệu quả ngay cả khi các giả định nền tảng không được thỏa mãn[cite: 1].
*   


## Ghi chú Độc lập: Diễn giải Vật lý các cấu trúc trong Recurrence Plot

### 1. Nguyên lý phân cấp cốt lõi
Ý nghĩa vật lý của RP không nằm ở từng điểm đen (một lần lặp), mà ở cách các sự kiện đó tạo thành các cấu trúc tương quan. 
**Hệ phân cấp diễn giải:**
State $\rightarrow$ Recurrence Event $\rightarrow$ Texture $\rightarrow$ Typology $\rightarrow$ Dynamics

### 2. Ý nghĩa Động lực học & Vật lý của các Cấu trúc (Textures)

| Cấu trúc | Ý nghĩa Toán học | Ý nghĩa Động lực học | Ý nghĩa Vật lý |
| :--- | :--- | :--- | :--- |
| **Single Point** | Hai trạng thái gần nhau ($x_i \approx x_j$). | Một recurrence. | Hệ tình cờ ghé lại một vùng trạng thái. |
| **Diagonal Line** | Hai quỹ đạo tiến hóa song song ($x_{i+k} \approx x_{j+k}$). | Deterministic evolution. | Tính tất định: Hệ lặp lại một *quy luật tiến hóa*. Độ dài tỷ lệ nghịch với Lyapunov exponent. |
| **Vertical / Horizontal Line** | Trạng thái gần như không đổi ($x_i \approx x_j \approx x_{j+1} \dots$). | Trapping. | Hệ bị "mắc kẹt" (laminar, metastable) ở một miền trạng thái. |
| **Checkerboard** | Luân phiên quay lại nhiều vùng. | Structured oscillation. | Dao động có tổ chức quanh các điểm cân bằng. |
| **Homogeneous Field** | Mật độ lặp ổn định. | Stationary dynamics. | Quy luật phân bố xác suất không đổi theo thời gian. |
| **Fading Pattern** | Mật độ lặp giảm theo $|i-j|$. | Parameter drift. | Sự trôi/thay đổi chậm: Quỹ đạo dịch chuyển sang miền mới. |
| **White Bands** | Không có sự kiện lặp. | Regime change. | Chuyển pha, rẽ nhánh (bifurcation), thay đổi động lực học đột ngột. |

### 3. Góc nhìn tổng quát
*   RP không vẽ hình dáng của attractor, mà vẽ **hình học của các sự kiện hồi quy**.
*   Các điểm đen (recurrence event) $\rightarrow$ Đường chéo (evolution event) $\rightarrow$ Vùng đồng nhất (stationary process) $\rightarrow$ Vùng nhạt dần (drifting process).
*   Góc nhìn này là cầu nối Topology $\rightarrow$ Dynamical Systems $\rightarrow$ Statistical Physics, tạo tiền đề để RQA (1992) lượng hóa các cấu trúc này.