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

# Tóm tắt Mục 4.1: Phân biệt nguồn gốc của Đa phân dạng (Shuffling & Ratio Test)

## 1. Hai nguồn gốc của tính đa phân dạng

Đa phân dạng của một chuỗi thời gian có thể xuất phát từ hai cơ chế độc lập.

### (i) Do phân phối xác suất rộng (Distribution-induced Multifractality)

- Phân phối xác suất có đuôi dày (heavy-tailed distribution).
- Xuất hiện các dao động có biên độ rất lớn.
- Không phụ thuộc vào thứ tự xuất hiện của dữ liệu.

---

### (ii) Do tương quan dài hạn (Correlation-induced Multifractality)

- Các dao động nhỏ và lớn có cấu trúc tương quan khác nhau trên nhiều thang đo.
- Thứ tự xuất hiện của dữ liệu mang thông tin (long-range correlation).
- Đây là nguồn gốc động lực học của multifractality.

---

## 2. Phép thử Xáo trộn (Shuffling Test)

### Ý tưởng

Xáo trộn ngẫu nhiên toàn bộ chuỗi thời gian.

Kết quả:

- Phá hủy hoàn toàn cấu trúc tương quan dài hạn.
- Giữ nguyên phân phối xác suất (PDF).

Do đó:

- Correlation $\rightarrow$ bị loại bỏ.
- Distribution $\rightarrow$ được bảo toàn.

---

## 3. Đánh giá nguồn gốc bằng MF-DFA

Sau khi chạy MF-DFA trên chuỗi đã xáo trộn, thu được số mũ

$$
h_{\mathrm{shuf}}(q)
$$

### Trường hợp 1

$$
h_{\mathrm{shuf}}(q)\approx h(q)
$$

→ Đa phân dạng chủ yếu do **phân phối xác suất rộng**.

---

### Trường hợp 2

$$
h_{\mathrm{shuf}}(q)\approx0.5
$$

→ Sau khi mất tương quan, chuỗi trở thành White Noise.

→ Đa phân dạng chủ yếu do **Long-range Correlation**.

---

### Trường hợp 3 (phổ biến nhất)

$$
0.5<h_{\mathrm{shuf}}(q)<h(q)
$$

→ Đa phân dạng được tạo ra bởi **cả Distribution và Correlation**.

---

## 4. Ratio Test (Correlation-only Scaling)

Để loại bỏ ảnh hưởng của phân phối xác suất và chỉ giữ lại phần scaling do tương quan:

$$
\frac{F_q(s)}{F_q^{\mathrm{shuf}}(s)}
\sim
s^{h_{\mathrm{cor}}(q)}
$$

Trong đó

$$
h_{\mathrm{cor}}(q)
=
h(q)-h_{\mathrm{shuf}}(q)
$$

hay

$$
h(q)
=
h_{\mathrm{shuf}}(q)
+
h_{\mathrm{cor}}(q)
$$

---

## 5. Ý nghĩa của $h_{\mathrm{cor}}(q)$

### Nếu

$$
h_{\mathrm{cor}}(q)\approx0
$$

→ Hầu như không tồn tại Long-range Correlation.

---

### Nếu

$$
h_{\mathrm{cor}}(q)\neq0
$$

→ Hệ thống tồn tại Long-range Correlation.

---

### Nếu

$$
h_{\mathrm{cor}}(q)
$$

phụ thuộc vào $q$

→ Chính cấu trúc tương quan cũng mang tính đa phân dạng (Correlation-induced Multifractality).

---

## Kết luận

MF-DFA chỉ cho biết **chuỗi có đa phân dạng hay không**.

Section 4 bổ sung các phép thử để xác định **nguồn gốc của đa phân dạng**:

- Distribution-induced Multifractality.
- Correlation-induced Multifractality.
- Hoặc sự kết hợp của cả hai.

Đây là bước chuyển từ **đo lường (Measurement)** sang **giải thích cơ chế (Mechanism Identification)**.


### 1. Hiệu ứng kích thước hữu hạn (Finite-size effect) là sai số nội tại của MF-DFA

Ngay cả đối với một chuỗi đơn phân dạng (monofractal) lý tưởng, sự phụ thuộc giả của $h(q)$ vào $q$ vẫn có thể xuất hiện khi chiều dài dữ liệu là hữu hạn [1, 2]. 

*   **Lý thuyết:** Phổ số mũ phải là một hằng số $h(q) = H$ [3].
*   **Thực tế đo đạc:** Với các chuỗi dữ liệu ngắn (ví dụ $N \approx 8192$), các thăng giáng nhỏ thường chịu nhiễu thống kê lớn, dẫn đến hiện tượng đo lố (overshoot) ở các moment âm. Hệ quả là $h(-10)$ luôn lớn hơn một chút so với $h(+10)$ [2].
*   **Bản chất:** Sự chênh lệch này là sai lệch thống kê (statistical bias) tự nhiên của thuật toán trên tập dữ liệu ngắn, hoàn toàn không phải là bằng chứng của đa phân dạng [2].

> **💡 Take-away:** 
> **Tuyệt đối không kết luận tín hiệu có tính đa phân dạng chỉ dựa vào một độ cong nhẹ của đồ thị phổ $h(q)$.**

---

### 2. Xáo trộn dữ liệu (Shuffling) giúp truy vết nguồn gốc đa phân dạng

Phép so sánh phổ đa phân dạng trước và sau khi xáo trộn ngẫu nhiên là chìa khóa phân tích để bóc tách bản chất của hệ thống [4, 5]:

*   **Nếu phổ sụp đổ về mức $h_{shuf}(q) \approx 0.5$:** Toàn bộ cấu trúc đa phân dạng chủ yếu sinh ra từ **"trí nhớ" tương quan dài hạn (long-range correlations)** của hệ thống, và đã bị phá hủy hoàn toàn sau khi xáo trộn [6, 7].
*   **Nếu phổ gần như giữ nguyên hình dáng ($h_{shuf}(q) \approx h(q)$):** Tính đa phân dạng bắt nguồn từ những đột biến trong **phân phối xác suất biên độ rộng (broad probability distribution)**, vì phép xáo trộn không làm thay đổi hàm mật độ phân phối [6, 8].

> **💡 Take-away:** 
> **Shuffling là phép thử bắt buộc và hiệu quả nhất để phân biệt giữa đa phân dạng do tương quan (correlation-induced) và đa phân dạng do phân phối (distribution-induced).**

---

### 3. Luôn đối chiếu với ngưỡng sai số nền (Baseline Comparison)

Kết quả đo lường từ MF-DFA chỉ thực sự có ý nghĩa khoa học khi độ lệch của các chỉ số vượt qua được sai số tự nhiên của chính thuật toán [2]. 

Do đó, trước khi đưa ra kết luận khẳng định, người nghiên cứu bắt buộc phải:
*   Xác định rõ mức độ sai số do hiệu ứng kích thước hữu hạn (finite-size effect) bằng cách sinh ra các chuỗi đơn phân dạng giả lập có cùng độ dài để so sánh [2].
*   Sử dụng các chuỗi đối chứng (shuffled/surrogate series) để thiết lập hệ quy chiếu nền [9].

> **💡 Take-away:** 
> **MF-DFA không chỉ đơn thuần là việc tính ra một giá trị $h(q)$, mà cốt lõi là phải đánh giá được độ tin cậy, tính ngẫu nhiên và biên độ sai số của kết quả đó.**