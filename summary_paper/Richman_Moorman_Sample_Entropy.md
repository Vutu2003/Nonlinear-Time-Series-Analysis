# Richman & Moorman, 2000: Physiological time-series analysis using approximate entropy and sample entropy

# ABSTRACT

* **Vấn đề của ApEn**: Các phương pháp ước lượng entropy truyền thống không phù hợp với dữ liệu y sinh ngắn và nhiễu[cite: 1]. Thuật toán Approximate Entropy (ApEn) dù được dùng nhiều trên lâm sàng nhưng lại cho ra các kết quả thống kê thiếu nhất quán[cite: 1].
* **Giải pháp đề xuất**: Nghiên cứu phát triển một thước đo độ phức tạp mới mang tên Sample Entropy (SampEn) để khắc phục các nhược điểm của ApEn[cite: 1]. 
* **Phương pháp kiểm chứng**: Hai thuật toán được so sánh trực tiếp thông qua việc phân tích các bộ số ngẫu nhiên[cite: 1]. Tác giả cũng đánh giá thêm Cross-ApEn và Cross-SampEn để đo lường độ tương đồng giữa hai chuỗi tín hiệu tim mạch[cite: 1].
* **Kết quả & Ý nghĩa**: SampEn cho kết quả bám sát với lý thuyết toán học hơn hẳn ApEn trên một dải điều kiện rộng[cite: 1]. Độ chính xác cao giúp SampEn trở thành công cụ tối ưu để phân tích các chuỗi thời gian y sinh[cite: 1].
  
# Tóm tắt: Động lực của SampEn & Điểm yếu của ApEn

*   **Tử huyệt của ApEn:** Việc cố tình đếm "tự so sánh" (self-matching) để lấp liếm lỗi $\ln(0)$ tạo ra thiên lệch (bias) chí mạng: khiến kết quả phụ thuộc nặng nề vào chiều dài dữ liệu và đánh mất hoàn toàn "tính nhất quán tương đối" (relative consistency)[cite: 1].
*   **Giải pháp của SampEn:** Cắt bỏ hoàn toàn thao tác "tự so sánh"[cite: 1]. Thay đổi cốt lõi này mang lại ba đột phá: thuật toán chạy nhanh gấp đôi, độc lập với độ dài bản ghi và khôi phục sự nhất quán tuyệt đối[cite: 1].
*   **Mặt trận phân tích đa biến (Cross-Entropy):** Cross-ApEn dễ sai lệch do phải dùng các "chiến lược hiệu chỉnh" khiên cưỡng để tránh lỗi $\ln(0)$[cite: 1]. Cross-SampEn giải quyết triệt để rủi ro này bằng cách lấy tổng số lần khớp trên toàn bộ dữ liệu trước khi tính logarit, đảm bảo thuật toán luôn ổn định chỉ với một điểm khớp duy nhất[cite: 1].
*   

# Tóm tắt Phân tích Toán học: Cội nguồn Thất bại của ApEn

*   **Bản chất & Sai lệch độ dài:** ApEn vận hành bằng cách đếm số láng giềng của từng vector mẫu (template-wise) tại không gian chiều $m$ và $m+1$[cite: 1]. Tuy nhiên, sự bất đồng bộ toán học về số lượng vector (có $N-m+1$ mẫu ở chiều $m$ nhưng chỉ có $N-m$ mẫu ở chiều $m+1$) đã gây ra sai số nhỏ ban đầu đối với dữ liệu[cite: 1].
*   **Tử huyệt "Tự so sánh" (Self-matching):** Để lách lỗi $\ln(0)$ khi tính logarit độc lập cho từng vector, thuật toán buộc phải đếm cả chính nó, biến phép tính xác suất thực $A_i/B_i$ thành $(A_i+1)/(B_i+1)$[cite: 1]. "Khối u" này tạo ra một thiên lệch (bias) nghiêm trọng, đánh lừa hệ thống rằng dữ liệu luôn trật tự và quy luật hơn bản chất thực[cite: 1].
*   **Lỗ hổng kiến trúc không thể vãn hồi:** Việc gỡ bỏ thao tác "tự so sánh" là bất khả thi, bởi chỉ cần một điểm dị thường (outlier) không có láng giềng, toàn bộ thuật toán ApEn sẽ lập tức sụp đổ vì $\ln(0)$[cite: 1]. Việc cố gắng dùng các hệ số xấp xỉ để bù trừ cũng được chứng minh là vô ích[cite: 1].

**Kết luận:** Sai lầm chí mạng của ApEn nằm ở kiến trúc *tính logarit trước cho từng vector rồi mới lấy trung bình*[cite: 1]. Nhận định này đóng vai trò dọn đường hoàn hảo cho SampEn: Thay đổi trình tự bằng cách *gom tổng láng giềng trên toàn cục dữ liệu rồi mới tính logarit*, từ đó cắt bỏ triệt để "tự so sánh" mà không làm sụp đổ phương trình[cite: 1].

# Sample Entropy Algorithm

### Bước 1: Khởi tạo các vector mẫu (Template vectors)

Từ chuỗi dữ liệu gốc $N$ điểm $u(1), u(2), \dots, u(N)$, tạo ra các vector có chiều dài $m$:
$$x_m(i) = [u(i), u(i+1), \dots, u(i+m-1)]$$

*   **Điều kiện giới hạn:** Chỉ lấy các vector với chỉ số $i$ chạy từ $1$ đến $N-m$. Việc cắt bỏ phần đuôi này đảm bảo mọi vector $x_m(i)$ đều có thể được kéo dài thêm 1 điểm dữ liệu hợp lệ để trở thành vector $x_{m+1}(i)$.
*   **Lý giải so với ApEn (Đồng bộ hóa chiều dài):** ApEn khởi tạo $N-m+1$ vector cho không gian chiều $m$ nhưng lại chỉ có $N-m$ vector cho chiều $m+1$, tạo ra một sự chênh lệch toán học. SampEn khắc phục triệt để lỗi này bằng cách đồng bộ hóa tập mẫu, ép cả hai chiều phải sử dụng chung một số lượng vector là $N-m$.

### Bước 2: Tính tổng láng giềng ở không gian chiều $m$ (Đại lượng $B^m$)

Khoảng cách giữa 2 vector $x_m(i)$ và $x_m(j)$ được xác định bằng khoảng cách Chebyshev (độ chênh lệch lớn nhất giữa các cặp phần tử tương ứng):
$$d[x_m(i), x_m(j)] = \max_{0 \le k \le m-1} (|u(i+k) - u(j+k)|)$$

*   **Nguyên tắc đếm:** Đối với mỗi vector $x_m(i)$, đếm số lượng vector $x_m(j)$ thỏa mãn khoảng cách $d \le r$. Tỷ lệ vector khớp (láng giềng) được tính bằng:
$$B_i^m(r) = \frac{1}{N-m-1} \times (\text{số lượng } j \text{ thỏa mãn } d \le r \text{ với } j \neq i)$$
*   **Xác suất toàn cục:** Xác suất khớp ở chiều $m$ trên toàn chuỗi là trung bình cộng của các $B_i^m(r)$:
$$B^m(r) = \frac{1}{N-m} \sum_{i=1}^{N-m} B_i^m(r)$$
*   **Lý giải so với ApEn (Loại bỏ Tự so sánh):** Đây là điểm phân thủy mấu chốt. ApEn cho phép $j$ chạy từ $1$ đến $N-m+1$ bao gồm cả $j = i$ (tự so sánh với chính nó) để tránh lỗi xác suất bằng $0$. SampEn áp đặt quy tắc $j \neq i$ khắt khe, chấp nhận rủi ro $B_i^m(r) = 0$ để bảo vệ tính trung thực của cấu trúc dữ liệu, không tạo ra các điểm khớp ảo.

### Bước 3: Tính tổng láng giềng ở không gian chiều $m+1$ (Đại lượng $A^m$)

Tăng chiều nhúng lên $m+1$ và thực hiện quá trình đếm tương tự đối với các vector $x_{m+1}(i)$ và $x_{m+1}(j)$.

*   **Tỷ lệ vector khớp:**
$$A_i^m(r) = \frac{1}{N-m-1} \times (\text{số lượng } j \text{ thỏa mãn } d \le r \text{ với } j \neq i)$$
*   **Xác suất toàn cục:** 
$$A^m(r) = \frac{1}{N-m} \sum_{i=1}^{N-m} A_i^m(r)$$

### Bước 4: Tính toán giá trị Sample Entropy cuối cùng

Thống kê thực nghiệm Sample Entropy cho chuỗi $N$ điểm dữ liệu được định nghĩa là logarit âm của tỷ số giữa hai xác suất toàn cục vừa tìm được:
$$SampEn(m, r, N) = -\ln \left( \frac{A^m(r)}{B^m(r)} \right)$$

*   **Dạng công thức rút gọn ứng dụng lập trình:** Bằng cách triệt tiêu các mẫu số chung $(N-m-1)$ và $(N-m)$, nếu gọi $A$ là tổng số cặp khớp ở chiều $m+1$ và $B$ là tổng số cặp khớp ở chiều $m$ trên toàn bộ hệ thống, ta có phương trình tối giản:
$$SampEn(m, r, N) = -\ln \left( \frac{A}{B} \right)$$
*   **Lý giải so với ApEn (Thay đổi kiến trúc Logarit):** Thay vì tính logarit cho từng phân số nhỏ $\ln(A_i/B_i)$ rồi mới cộng lại như ApEn (dễ dẫn đến thảm họa $\ln(0)$ nếu một vector không có láng giềng), SampEn gom tổng tất cả $A_i$ và $B_i$ trên toàn bộ dữ liệu trước rồi mới thực hiện phép tính $\ln(A/B)$. Chỉ cần toàn bộ chuỗi có ít nhất một cặp vector khớp nhau ở chiều $m+1$ ($A \ge 1$), thuật toán SampEn sẽ hoạt động ổn định và chính xác mà không cần nhờ đến "khối u tự so sánh".
*   

#  Sự tiến hóa từ ApEn $\to$ SampEn

Sự chuyển đổi từ ApEn sang SampEn không nằm ở việc "bỏ self-match", mà là một cuộc cách mạng về **hàm ước lượng (estimator)** dưới lăng kính của Lý thuyết Thông tin và Thống kê.

#### 1. Sự dịch chuyển Mô hình: State-centric vs. Pair-centric

*   **ApEn (State-centric - Lấy trạng thái làm trung tâm):** 
    Tập trung vào từng vector. Ước lượng xác suất cục bộ, tính lượng thông tin cục bộ, rồi lấy trung bình.
    $$ \text{Local Probability } (C_i) \xrightarrow{\text{log}} \text{Local Information} \xrightarrow{\text{Average}} \text{Average Information } (E[-\log C_i]) $$
*   **SampEn (Pair-centric - Lấy cặp làm trung tâm):** 
    Coi mỗi cặp so khớp là một quan sát (pooling). Ước lượng một xác suất chung toàn cục, rồi tính lượng thông tin của toàn hệ thống.
    $$ \text{Global Probability } (A/B) \xrightarrow{\text{log}} \text{Global Information } (-\log(A/B)) $$

#### 2. Self-match: Chướng ngại vật và Hệ quả

Sự biến mất của tự so sánh (self-match) trong SampEn không phải là điểm xuất phát, mà là **hệ quả tất yếu** của việc thay đổi cấu trúc logarit:

*   **ApEn:** Bắt buộc tính $\log(C_i)$ cho từng trạng thái $\to$ $C_i$ không được phép bằng 0 $\to$ **Buộc phải giữ self-match** để tránh thảm họa $\log(0)$.
*   **SampEn:** Đếm toàn bộ số cặp khớp ($A$ và $B$) rồi mới tính $\log(A/B)$ $\to$ Không còn giới hạn $C_i > 0$ cho từng vector $\to$ **Self-match tự nhiên bị loại bỏ** vì không còn giá trị bảo vệ hàm logarit.

#### 3. Kết luận Cốt lõi (Key Takeaways)

> **"Richman không thay đổi định nghĩa complexity của Pincus. Richman thay đổi cách ước lượng xác suất."**

Chỉ một sự thay đổi về đơn vị quan sát (từ State sang Pair) đã giải quyết triệt để mọi yếu điểm toán học:
*   Bỏ self-match một cách tự nhiên.
*   Loại bỏ hoàn toàn tính toán logarit cục bộ.
*   Gộp (pooling) toàn bộ dữ liệu giúp trung hòa nhiễu ngẫu nhiên.
*   Tạo ra một estimator phương sai thấp, ít thiên lệch và ổn định tuyệt đối trên các chuỗi dữ liệu ngắn.

*Ghi chú: Góc nhìn "Pair-centric" này chính là nền tảng thống nhất để lý giải tính hợp lý của toàn bộ họ Entropy thế hệ sau như Cross-SampEn, FuzzyEn, hay Distribution Entropy.*