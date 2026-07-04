# HỆ THỐNG KIỂM ĐỊNH ĐỘNG LỰC HỌC LÕI (CORE DYNAMICS VALIDATOR)
**Triết lý cốt lõi:** *Statistic-Centric & Global Parameter Locking*

---

## GIAI ĐOẠN 1: Khởi Tạo Nền Tảng & Hệ Quy Chiếu
**Mục tiêu:** Cố định "sân chơi" hình học và tạo lập các nhân chứng giả tuân thủ nghiêm ngặt tính chất thống kê tuyến tính của tín hiệu gốc.

1. **Trích xuất Tham số Toàn cục (Global Locking):**
   * Đầu vào là chuỗi tín hiệu đo lường thực tế $x_{orig}$ (cửa sổ ngắn).
   * Sử dụng hàm Average Mutual Information (AMI) để tìm độ trễ thời gian tối ưu $\tau$.
   * Sử dụng hàm False Nearest Neighbors (FNN) để tìm số chiều nhúng tối ưu $m$.
   * **Chốt cứng** cặp tham số $(\tau, m)$ này cho toàn bộ quá trình về sau.

2. **Sinh Dữ liệu Đối chứng (Surrogate Generation):**
   * Sử dụng thuật toán **IAAFT** trên $x_{orig}$ để tạo ra tập hợp $M$ chuỗi surrogate $x_{surr}^{(1)}, \dots, x_{surr}^{(M)}$ (với $M \ge 39$).
   * Đảm bảo các chuỗi giả này giữ nguyên phổ năng lượng (PSD) và phân phối biên độ gốc, chỉ phá hủy các cấu trúc phụ thuộc thời gian phi tuyến.

---

## GIAI ĐOẠN 2: Tái Tạo Không Gian Pha Đồng Bộ
**Mục tiêu:** Ánh xạ dữ liệu từ miền thời gian 1D sang không gian quỹ đạo đa chiều mà không làm sai lệch cấu trúc do nhiễu tham số.

1. Sử dụng duy nhất bộ tham số $(\tau, m)$ đã khóa ở Giai đoạn 1.
2. Nhúng chuỗi $x_{orig}$ thành ma trận quỹ đạo $\mathbf{Y}_{orig}$.
3. Nhúng toàn bộ $M$ chuỗi surrogate thành các ma trận quỹ đạo $\mathbf{Y}_{surr}^{(1)}, \dots, \mathbf{Y}_{surr}^{(M)}$.

---

## GIAI ĐOẠN 3: Tầng Đánh Giá Đa Chiến Lược (Plug-and-Play Predictors)
**Mục tiêu:** Nén toàn bộ năng lực dự báo của một chuỗi thời gian thành MỘT con số vô hướng (Scalar Statistic) thông qua các màng lọc không gian.

Tại mỗi vector trạng thái truy vấn, sử dụng thuật toán KD-Tree tìm $K$ láng giềng gần nhất (Khuyến nghị $K = 5 \sim 10$), kết hợp màng lọc Theiler Window để bỏ qua các điểm lân cận thời gian. Đưa láng giềng vào các "Strategy Modules" độc lập:

1. **Module 1 - Nền tảng (Farmer 0th Order - Local Constant):**
   * Lấy trung bình trực tiếp sự tiến hóa của $K$ láng giềng.
   * Đặc tính: Cực kỳ vững chãi (robust) trước các gai nhiễu (artifacts) của thiết bị đo.

2. **Module 2 - Mũi dò nhạy bén (Farmer 1st Order - Local Linear):**
   * Fit một siêu phẳng tuyến tính cục bộ qua các láng giềng.
   * Đặc tính: Nhạy cảm cao với sự trơn tru của đa tạp (manifold), phát huy sức mạnh tối đa khi tín hiệu ít nhiễu.

3. **Module 3 - Át chủ bài (Sugihara Simplex Projection):**
   * Nội suy dự báo bằng cách gán trọng số giảm dần theo khoảng cách hình học ($w_j \propto \exp(-d_j/d_1)$).
   * Đặc tính: Hoạt động xuất sắc trên dữ liệu ngắn và quỹ đạo cong phức tạp.

4. **Tổng hợp Thống kê (Aggregation):**
   * Với mỗi chuỗi (thật và giả), tính sai số dự báo tuyệt đối $e(i)$ tại mọi điểm.
   * Trích xuất đại lượng đại diện: $T = \text{Median}(e)$ (hoặc $\text{RMSE}$).
   * Đầu ra của mỗi Module là $M+1$ con số: $T_{orig}$ và mảng $\mathbf{T}_{surr}$.

---

## GIAI ĐOẠN 4: Tầng Khai Thác Bổ Trợ (Secondary Evaluators)
**Mục tiêu:** Cung cấp góc nhìn tham chiếu để củng cố lập luận.

1. **Predictive Skill:** Tính hệ số tương quan (Correlation Coefficient - CC) giữa quỹ đạo thực tế và quỹ đạo dự báo.
2. **Lyapunov Exponent ($\lambda_1$):** Sử dụng thuật toán Kantz đo sự phân kỳ quỹ đạo. Đóng vai trò là bằng chứng thứ cấp để kiểm chứng tính hỗn loạn nội tại.

---

## GIAI ĐOẠN 5: Tòa Án Thống Kê Phi Tham Số (One-Sided Rank Test)
**Mục tiêu:** Phán quyết bằng p-value thông qua phép đếm thứ hạng thực nghiệm nguyên thủy, miễn nhiễm với giả định phân phối.

1. **Đối với nhóm đại lượng "Càng nhỏ càng mang tính quyết định" (RMSE, $\lambda_1$):**
   * Đếm số chuỗi giả có giá trị lớn hơn hoặc bằng chuỗi thật: 
     $$C = \sum_{k=1}^M \Theta(T_{surr}^{(k)} - T_{orig})$$

2. **Đối với nhóm đại lượng "Càng lớn càng mang tính quyết định" (CC):**
   * Đếm số chuỗi giả có giá trị nhỏ hơn hoặc bằng chuỗi thật: 
     $$C = \sum_{k=1}^M \Theta(T_{orig} - T_{surr}^{(k)})$$

3. **Xuất p-value:**
   * Tính $p = \frac{1 + C}{M + 1}$. 
   * Nếu $p \le \alpha$ (ví dụ: $\alpha = 0.05$): Bác bỏ giả thuyết tín hiệu là một quá trình ngẫu nhiên tuyến tính. Hệ thống có tính hỗn loạn quyết định tính.

---

## GIAI ĐOẠN 6: Khung Trình Bày Công Bố (Publication Output)
Hệ thống sẽ tổng hợp tự động thành một cấu trúc bảng hiển thị toàn bộ chỉ số đánh giá của Giai đoạn 3 và 4. 

| Statistic (Đại lượng) | $T_{orig}$ | Surrogate Median | p-value | Significance |
| :--- | :--- | :--- | :--- | :--- |
| **Prediction: Bậc 0 (RMSE)** | [Kết quả] | [Kết quả] | [p] | [***] |
| **Prediction: Bậc 1 (RMSE)** | [Kết quả] | [Kết quả] | [p] | [***] |
| **Prediction: Simplex (RMSE)**| [Kết quả] | [Kết quả] | [p] | [***] |
| **Predictive Skill (CC)** | [Kết quả] | [Kết quả] | [p] | [***] |
| **Kantz Lyapunov ($\lambda_1$)** | [Kết quả] | [Kết quả] | [p] | [**] |