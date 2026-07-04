### THUẬT TOÁN KANTZ (1994) TÍNH SỐ MŨ LYAPUNOV LỚN NHẤT (LLE - $\lambda_{max}$)

**Đầu vào:** Một chuỗi dữ liệu thời gian vô hướng đo lường cách đều nhau: $\{x_t\}, t = 1, \dots, T$.

#### Bước 1: Tái cấu trúc không gian và Tìm "Quần thể" hàng xóm
Thay vì tìm một điểm gần nhất, Kantz gom tất cả các điểm nằm trong một vùng không gian nhỏ.

* **Tạo vector trễ (Delay vectors):** Chuyển chuỗi 1D thành các điểm trong không gian nhúng $m$ chiều:
  $$\mathbf{x}_t = (x_{t-m+1}, \dots, x_t)$$
* **Xác định vùng lân cận ($\epsilon$-neighbourhood):** Tại mỗi điểm tham chiếu $\mathbf{x}_t$, tìm tất cả các vector $\mathbf{x}_i$ nằm gọn trong một bán kính $\epsilon$. Tập hợp các điểm hàng xóm này được ký hiệu là $\mathcal{U}_t$.

#### Bước 2: Đo khoảng cách vô hướng (1D) theo thời gian
Thay vì đo khoảng cách đa chiều, Kantz chỉ chiếu khoảng cách đó lên một tọa độ 1D duy nhất sau một khoảng thời gian $\tau$.

* **Công thức (2.2):**
  $$\text{dist}(\mathbf{x}_t, \mathbf{x}_i; \tau) = |x_{t+\tau} - x_{i+\tau}|$$
  *(Trong đó, khoảng cách này bị biến điệu bởi góc chiếu không gian pha $|\cos \phi|$).*

#### Bước 3: Thiết lập Hàm $S(\tau)$ - Trung bình 2 lớp
Đây là công thức trung tâm của thuật toán nhằm mục đích làm phẳng các dao động do góc chiếu và triệt tiêu nhiễu.

* **Công thức (2.3):**
  $$S(\tau) = \frac{1}{T} \sum_{t=1}^T \ln \left( \frac{1}{|\mathcal{U}_t|} \sum_{i \in \mathcal{U}_t} \text{dist}(\mathbf{x}_t, \mathbf{x}_i; \tau) \right)$$
* **Lớp 1 (Bên trong):** Lấy trung bình khoảng cách của toàn bộ quần thể hàng xóm $\mathcal{U}_t$.
* **Lớp 2 (Bên ngoài):** Lấy logarit, sau đó tiếp tục lấy trung bình dọc theo toàn bộ thời gian $T$.

#### Bước 4: Biến đổi toán học để Cô lập LLE và Triệt tiêu nhiễu
Để chứng minh $S(\tau)$ có thể tìm ra LLE trong môi trường có nhiễu đo lường, Kantz phân rã phần bên trong của hàm $S(\tau)$ bằng cách thêm vào thành phần nhiễu cộng gộp $\sigma_{i, \tau}$ và nguyên lý phân kỳ hàm mũ $\Delta_{i, \tau} = \Delta_{i, \tau-1} e^{\lambda_{t+\tau}}$.

* **Công thức (2.4) - Khai triển bên trong logarit:**
  $$\ln \left[ \langle \text{dist}(\mathbf{x}_t, \mathbf{x}_i; \tau) \rangle_{i \in \mathcal{U}_t} \right] = \ln \left( \frac{1}{|\mathcal{U}_t|} \sum_{i \in \mathcal{U}_t} \left| \Delta_{i, \tau-1} e^{\lambda_{t+\tau}} \cos(\phi_{t+\tau}) + \sigma_{i, \tau} \right| \right)$$
* **Công thức (2.5) - Tuyến tính hóa bằng xấp xỉ Taylor:** Giả sử nhiễu nhỏ hơn tín hiệu, phương trình được tách thành các phép cộng:
  $$\approx \lambda_{t+\tau} + \ln( \langle \Delta_{i, \tau-1} \rangle_{\mathcal{U}_t} ) + \ln |\cos(\phi_{t+\tau})| + \frac{\langle \sigma_{i, \tau} \rangle_{\mathcal{U}_t}}{\langle \text{dist}(\mathbf{x}_t, \mathbf{x}_i; \tau) \rangle_{\mathcal{U}_t}}$$
  > *Tại đây, Số mũ Lyapunov cục bộ $\lambda_{t+\tau}$ đã được cô lập. Do nhiễu $\sigma_{i, \tau}$ là ngẫu nhiên, khi bị lấy trung bình trên toàn bộ hàng xóm (tử số $\langle \sigma \rangle$), nó sẽ triệt tiêu và tiến về $0$.*

#### Bước 5: Đạo hàm theo thời gian $\tau$ để trích xuất Độ dốc
Để tìm ra LLE toàn cục ($\lambda$), Kantz lấy sự thay đổi của khoảng cách giữa bước $\tau$ và $\tau-1$ rồi lấy trung bình theo thời gian $t$. Các thành phần khoảng cách $\Delta$ và góc $\phi$ tự triệt tiêu nhau trong phép trừ.

* **Công thức (2.6):**
  $$s(\tau) = \langle \ln \langle \text{dist}(\dots; \tau) \rangle - \ln \langle \text{dist}(\dots; \tau-1) \rangle \rangle_t$$
  $$\approx \lambda + \left\langle \frac{\langle \sigma_{i, \tau} \rangle}{\langle \text{dist}(\dots; \tau) \rangle} \right\rangle_t - \left\langle \frac{\langle \sigma_{i, \tau-1} \rangle}{\langle \text{dist}(\dots; \tau-1) \rangle} \right\rangle_t$$
  *(Vì các phân số chứa nhiễu ở cuối cùng chỉ là đại lượng bậc 2 so với mức nhiễu, tác động của chúng là hoàn toàn có thể bỏ qua. Phương trình đạo hàm được rút gọn thành $s(\tau) \approx \lambda$).*

#### Bước 6: Chốt kết quả bằng Đồ thị (Thực hành)
Dựa trên kết quả toán học $s(\tau) \approx \lambda$ ở Bước 5, hàm số $S(\tau)$ bắt buộc phải có dạng tuyến tính:
$$S(\tau) \approx \lambda \cdot \tau + C$$

* **Thao tác thực tế:** Máy tính sẽ vẽ hàm $S(\tau)$ theo các giá trị thời gian $\tau$ với nhiều tham số chiều nhúng $m$ và bán kính $\epsilon$ khác nhau.
* **Kết luận:** Tìm một vùng tuyến tính (scaling region) nơi các đường cong này song song với nhau. Hệ số góc (slope) của vùng đó chính là Số mũ Lyapunov lớn nhất $\lambda_{max}$.