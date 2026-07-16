# PIPELINE THUẬT TOÁN HIGUCHI (HFD)

**Đầu vào (Input):** Một chuỗi thời gian 1D hữu hạn gồm $N$ điểm dữ liệu đo đạc cách đều nhau: $X(1), X(2), \dots, X(N)$.

## Bước 1: Phân rã chuỗi thời gian (Decomposition)  --> Thay đổi độ dài "thước đo" k bằng cách lấy mẫu tín hiệu với các bước nhảy khác nhau.
Thay vì xử lý toàn bộ chuỗi một lúc, ta dùng một "cây thước" có độ dài $k$ (bước nhảy thời gian) để trích xuất ra các chuỗi con.
* **Thao tác:** Với một bước nhảy $k$ cố định, ta tạo ra $k$ chuỗi con riêng biệt bằng cách thay đổi điểm bắt đầu $m$ (với $m=1, 2, \dots, k$).
* **Công thức chuỗi con $X_k^m$:** $X_k^m = \{ X(m), X(m+k), X(m+2k), \dots, X(m + \lfloor \frac{N-m}{k} \rfloor \cdot k) \}$
* **Insight:** Việc dịch pha điểm bắt đầu $m$ giúp thuật toán "vắt kiệt" mọi thông tin từ tập dữ liệu hữu hạn mà không bỏ sót điểm nào.

## Bước 2: Đo chiều dài và Chuẩn hóa (Measurement & Normalization) --> Với mỗi k, ước lượng chiều dài của đồ thị tín hiệu và chuẩn hóa để các phép đo ở các thang đo khác nhau có thể so sánh được.
Tính chiều dài $L_m(k)$ cho từng chuỗi con vừa tạo ở Bước 1.
* **Thao tác:** Tính tổng sai phân tuyệt đối giữa các điểm liên tiếp trong chuỗi con, sau đó nhân với một hệ số bù đắp.
* **Công thức:** $L_m(k) = \frac{1}{k} \left\{ \sum_{i=1}^{\lfloor \frac{N-m}{k} \rfloor} |X(m+ik) - X(m+(i-1)k)| \right\} \cdot \frac{N-1}{\lfloor \frac{N-m}{k} \rfloor \cdot k}$
* **Insight:** Phần tử $\frac{N-1}{\lfloor \frac{N-m}{k} \rfloor \cdot k}$ chính là hệ số chuẩn hóa. Khi bước nhảy $k$ lớn, chuỗi con thường không chạm đúng đến điểm $N$ cuối cùng. Hệ số này phóng đại chiều dài lên để bù đắp cho phần dữ liệu bị hụt, đảm bảo chiều dài ở các mức $k$ khác nhau có thể so sánh công bằng.

## Bước 3: Lấy trung bình tập hợp (Ensemble Average) --> Trung bình hóa các phép đo từ các điểm bắt đầu khác nhau nhằm giảm sai lệch do pha lấy mẫu.
Tổng hợp kết quả của mức $k$ hiện tại.
* **Thao tác:** Tính giá trị trung bình $\langle L(k) \rangle$ của toàn bộ $k$ giá trị chiều dài $L_m(k)$ vừa thu được ở Bước 2.
* **Insight:** Bước này tự động triệt tiêu các dao động nhiễu ngẫu nhiên mà không cần phải cần đến điều kiện $N \to \infty$ hay nhúng không gian pha như Box-counting.

## Bước 4: Lặp lại và Xây dựng đồ thị (Iteration & Power Law) --> Khảo sát quy luật biến thiên của chiều dài trung bình theo thang đo. Nếu tín hiệu có tính fractal thì ⟨L(k)⟩ tuân theo định luật lũy thừa.
* **Thao tác:** Lặp lại Bước 1 đến Bước 3 cho các giá trị $k$ tăng dần (ví dụ: $k=1, 2, 3, 4, \dots, k_{max}$).
* **Quy luật:** Nếu tín hiệu là fractal, chiều dài trung bình sẽ tuân theo định luật lũy thừa: 
  $$\langle L(k) \rangle \propto k^{-D}$$

## Bước 5: Truy xuất Số chiều Fractal (Output Extraction) --> Hồi quy tuyến tính trên đồ thị log–log để ước lượng số chiều fractal từ hệ số góc.
* **Thao tác:** Vẽ đồ thị phân tán với trục hoành là $\log k$ và trục tung là $\log \langle L(k) \rangle$.
* **Kết quả:** Dùng phương pháp bình phương tối thiểu (least-square) để khớp một đường thẳng đi qua các điểm. Hệ số góc (slope) của đường thẳng này chính là $-D$ (âm của Số chiều phân dạng).