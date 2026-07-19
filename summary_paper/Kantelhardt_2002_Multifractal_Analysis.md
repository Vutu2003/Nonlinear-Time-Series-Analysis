### Bước 1: Tính chuỗi tích lũy (Profile)

*   **Công thức:** 
    $$Y(i) \equiv \sum_{k=1}^i [x_k - \langle x \rangle]$$ 
    *(với $i = 1, \dots, N$)*
*   **Giải thích:** Tính tổng tích lũy của chuỗi dữ liệu gốc $x_k$ sau khi trừ đi giá trị trung bình $\langle x \rangle$ để tạo ra một quỹ đạo dạng "bước đi ngẫu nhiên" (random walk).

---

### Bước 2: Phân mảnh dữ liệu (Windowing)

*   **Tham số tính toán:** Chia chuỗi $Y(i)$ thành các đoạn không chồng lấn có chiều dài $s$, thu được $N_s \equiv \text{int}(N/s)$ đoạn.
*   **Giải thích:** Để tránh bỏ sót phần dữ liệu dư ở cuối (do $N$ thường không chia hết trọn vẹn cho $s$), phép chia đoạn được lặp lại một lần nữa nhưng bắt đầu từ cuối chuỗi ngược lên. Quá trình này mang lại tổng cộng $2N_s$ đoạn, đảm bảo mọi điểm dữ liệu đều được bao phủ.

---

### Bước 3: Khử xu hướng cục bộ (Local Detrending) và Tính phương sai

*   **Công thức:**
    *   Đối với $N_s$ đoạn đi từ đầu chuỗi ($\nu = 1, \dots, N_s$):
        $$F^2(s, \nu) \equiv \frac{1}{s} \sum_{i=1}^s \{Y[(\nu-1)s+i] - y_\nu(i)\}^2$$
    *   Đối với $N_s$ đoạn đi từ cuối chuỗi ($\nu = N_s+1, \dots, 2N_s$):
        $$F^2(s, \nu) \equiv \frac{1}{s} \sum_{i=1}^s \{Y[N-(\nu-N_s)s+i] - y_\nu(i)\}^2$$
*   **Giải thích:** Vẽ một đường đa thức $y_\nu(i)$ (bậc $m$) khớp với từng đoạn để đại diện cho xu hướng cục bộ. Sau đó, tính phương sai cục bộ (trung bình bình phương của các độ lệch) giữa chuỗi tích lũy và đường xu hướng đó nhằm loại bỏ hoàn toàn sự phi dừng (non-stationarity).

---

### Bước 4: Tính hàm thăng giáng bậc $q$ (Cốt lõi Đa phân dạng)

*   **Công thức:** 
    $$F_q(s) \equiv \left\{ \frac{1}{2N_s} \sum_{\nu=1}^{2N_s} [F^2(s, \nu)]^{q/2} \right\}^{1/q}$$
*   **Giải thích:** Lấy trung bình tất cả phương sai của các đoạn theo trọng số bậc $q$ (với $q$ là số thực, $q \neq 0$).
    *   **Khi $q = 2$:** Công thức trở về đúng dạng của thuật toán DFA truyền thống.
    *   **Khi $q > 0$:** Phép toán lũy thừa sẽ khuếch đại và làm nổi bật các đoạn có phương sai (thăng giáng biên độ) lớn.
    *   **Khi $q < 0$:** Phép toán lũy thừa nghịch đảo sẽ khuếch đại và làm nổi bật các đoạn có phương sai (thăng giáng biên độ) nhỏ.

---

### Lưu ý kỹ thuật: Điều kiện kích thước cửa sổ $s > m + 1$ (hay $s \ge m + 2$)

Hàm $F_q(s)$ chỉ được định nghĩa hợp lệ khi kích thước cửa sổ $s$ tuân thủ nghiêm ngặt điều kiện $s > m + 1$ (trong đó $m$ là bậc của đa thức khử xu hướng). Nguyên nhân xuất phát từ giới hạn của **Bậc tự do (Degrees of Freedom)** trong toán thống kê:

*   **Rủi ro khớp hoàn hảo (Perfect Fitting):** Một đa thức bậc $m$ luôn được xác định bởi đúng $m+1$ hệ số. Nếu bạn chọn $s = m+1$ (ví dụ: dùng hàm bậc 1 để khớp qua 2 điểm dữ liệu), đường cong hồi quy sẽ đi qua chính xác $100\%$ các điểm trong cửa sổ đó.
*   **Triệt tiêu phương sai:** Khi đa thức khớp hoàn hảo, sai số phần dư tại mọi điểm đều bằng 0, dẫn đến phương sai cục bộ $F^2(s, \nu) = 0$. Kéo theo đó, hàm thăng giáng tổng thể $F_q(s) = 0$.
*   **Sự sụp đổ của không gian Logarit:** Mục tiêu cuối cùng của thuật toán là vẽ đồ thị phân tích trên hệ trục log-log (giữa $\log(F_q(s))$ và $\log(s)$). Nếu $F_q(s) = 0$, phép tính $\log(0)$ sẽ đưa ra một giới hạn vô nghiệm ($-\infty$), làm gián đoạn toàn bộ quá trình trích xuất số mũ.
*   **Kết luận:** Để thuật toán đo lường được sự thăng giáng thực tế (cần ít nhất 1 bậc tự do), số lượng điểm dữ liệu $s$ trong cửa sổ bắt buộc phải lớn hơn số tham số của đa thức ($m+1$). Do đó, $s \ge m+2$ là ranh giới tối thiểu tuyệt đối về mặt toán học.
*   

**Bước 5: Xác định Số mũ Hurst tổng quát $h(q)$**

*   **Công thức cốt lõi:** $F_q(s) \sim s^{h(q)}$.
*   **Cách tính:** Vẽ đồ thị log-log của hàm $F_q(s)$ theo kích thước cửa sổ $s$ cho từng giá trị của $q$. Độ dốc của đường thẳng thu được chính là số mũ $h(q)$.

**Ý nghĩa vật lý của $q$ và $h(q)$:**
*   **Khi $q > 0$:** Hệ thống tập trung vào các **biến động lớn**. Các biến động này thường gồ ghề hơn, dẫn đến độ dốc $h(q)$ **nhỏ hơn**.
*   **Khi $q < 0$:** Hệ thống tập trung vào các **biến động nhỏ**. Các biến động này thường mượt mà hơn, dẫn đến độ dốc $h(q)$ **lớn hơn**.

**Phân loại trạng thái hệ thống:**
*   **Đơn phân dạng (Monofractal):** Nếu $h(q)$ là một hằng số không phụ thuộc vào $q$.
*   **Đa phân dạng (Multifractal):** Nếu $h(q)$ thay đổi phụ thuộc vào $q$ (nhỏ dần khi $q$ tăng).

**Xử lý ngoại lệ (Kỹ thuật Tích phân kép):**
*   **Vấn đề:** MF-DFA tiêu chuẩn chỉ đo chính xác khi $h(q) > 0$. Nó sẽ bị sai số với các chuỗi tương quan nghịch mạnh ($h(q) \le 0$).
*   **Giải pháp:** Tích phân chuỗi profile thêm một lần nữa: $\tilde{Y}(i) \equiv \sum_{k=1}^i [Y(k) - \langle Y \rangle]$.
*   **Hiệu chỉnh công thức:** Chạy MF-DFA trên chuỗi mới thu được độ dốc $\tilde{h}(q)$. Số mũ thực tế được tính bằng: **$h(q) = \tilde{h}(q) - 1$**.
*   

# Tóm tắt các lưu ý kỹ thuật khi đo độ dốc $h(q)$ (Bước 5)

**1. Cắt bỏ cửa sổ quá lớn ($s > N/4$):**
*   **Vấn đề:** Số lượng phân đoạn quá ít ($N_s < 4$), gây nhiễu thống kê.
*   **Giải pháp:** Loại bỏ vùng $s > N/4$ khi fit đường thẳng hồi quy tuyến tính.

**2. Thận trọng với cửa sổ quá nhỏ ($s \approx 10$):**
*   **Vấn đề:** Bị sai số hệ thống do đa thức bị "overfit" với dữ liệu quá ngắn.
*   **Giải pháp:** Bỏ qua vùng $s \approx 10$ khi đo độ dốc, hoặc dùng phép chia tỷ số (Ratio Test) để khử sai số này.

**3. Điểm neo $h(2)$:**
*   **Ý nghĩa:** Khi $q=2$, công thức trở về DFA truyền thống. Đối với chuỗi dừng, $h(2)$ chính là **chỉ số Hurst $H$ tiêu chuẩn** [1]. Các $h(q)$ khác được gọi là "Số mũ Hurst tổng quát".

**4. Bẫy lỗi "Chia cho 0" tại $q = 0$:**
*   **Vấn đề:** Khi $q=0$, công thức chuẩn $[ \dots ]^{1/q}$ sẽ gây lỗi toán học (1/0) [2, 3].
*   **Giải pháp:** Bắt buộc phải rẽ nhánh code (If/Else). Tại $q=0$, chuyển sang dùng công thức **trung bình logarit** (logarithmic averaging): 
    $F_0(s) \equiv \exp \left\{ \frac{1}{4N_s} \sum_{\nu=1}^{2N_s} \ln [F^2(s, \nu)] \right\}$ [4].

# Tóm tat Mục 4.1: Phân biệt nguồn gốc Đa phân dạng (Shuffling & Ratio Test)

**1. Hai nguồn gốc của Đa phân dạng:**
*   **Loại (i) - Do phân phối (Distribution):** Biên độ dữ liệu có các bước nhảy vọt quá lớn (phân phối rộng).
*   **Loại (ii) - Do tương quan (Correlation):** Dữ liệu có cấu trúc "trí nhớ" hoặc tương quan dài hạn giữa các dao động lớn/nhỏ.

**2. Phép thử Xáo trộn (Shuffling Test):**
*   **Cách làm:** Xáo trộn ngẫu nhiên dữ liệu gốc. Phép toán này **phá hủy hoàn toàn loại (ii)** nhưng **giữ nguyên loại (i)**.
*   **Đánh giá qua số mũ $h_{shuf}(q)$:**
    *   Nếu $h_{shuf}(q) = h(q)$: Đa phân dạng hoàn toàn do biên độ (Loại i).
    *   Nếu $h_{shuf}(q) = 0.5$: Đa phân dạng hoàn toàn do tương quan (Loại ii - Trở về nhiễu trắng).

**3. Kiểm định Tỷ số (Ratio Test) - Bóc tách tương quan:**
*   **Mục đích:** Triệt tiêu nhiễu biên độ, chỉ giữ lại phần đa phân dạng do cấu trúc tương quan/thần kinh.
*   **Công thức đồ thị Tỷ số:** 
    $\frac{F_q(s)}{F_q^{shuf}(s)} \sim s^{h_{cor}(q)}$
*   **Hệ thức cốt lõi:** 
    **$h(q) = h_{shuf}(q) + h_{cor}(q)$**
*   **Kết luận:** Số mũ $h_{cor}(q)$ chính là chỉ số thuần khiết nhất đại diện cho độ mạnh yếu của "trí nhớ" tương quan dài hạn trong hệ thống.
*   
# QUY TRÌNH BÓC TÁCH VÀ KIỂM ĐỊNH TÍN HIỆU PPG (Dựa trên Mục 4)

**Bước 1: Đo lường cơ bản (MF-DFA gốc)**
Chạy thuật toán MF-DFA trên đoạn PPG 5 phút ($N \approx 8192$ điểm) để tính độ rộng phổ $\Delta h_{PPG}$ ban đầu.

**Bước 2: Lọc "ảo giác" dữ liệu ngắn (Mục 4.2)**
Tạo các chuỗi đơn phân dạng giả lập (Surrogate) có cùng độ dài 8192 điểm để đo mức độ sai số thống kê tự nhiên $\Delta h_{error}$.

**Bước 3: Chẩn đoán ý nghĩa thống kê (Significance)**
Nếu $\Delta h_{PPG}$ nhỏ hơn hoặc bằng $\Delta h_{error}$: Độ cong của phổ chỉ là nhiễu ngẫu nhiên. Kết luận nhịp tim đang ở trạng thái đơn phân dạng (mất độ phức tạp/buồn ngủ).

**Bước 4: Chiết xuất đặc trưng thần kinh (Mục 4.1)**
Nếu $\Delta h_{PPG}$ lớn hơn $\Delta h_{error}$ (đa phân dạng thực sự): Tiến hành xáo trộn chuỗi PPG (Shuffling) để phá hủy trí nhớ thời gian của hệ thần kinh.
Tính đồ thị tỷ số: $\frac{F_q(s)}{F_q^{shuf}(s)} \sim s^{h_{cor}(q)}$ nhằm triệt tiêu toàn bộ nhiễu do biên độ hô hấp/cử động.

**Đầu ra:** Chỉ số $h_{cor}(q)$ thu được chính là đặc trưng thuần khiết nhất của hệ thần kinh, sẵn sàng làm input cho Machine Learning.