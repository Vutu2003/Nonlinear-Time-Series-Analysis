### CẢM HỨNG "LẬT NGƯỢC VẤN ĐỀ" VÀ 3 BƯỚC ĐỘT BIẾN CỦA THUẬT TOÁN PPS (Michael Small)

Nhận thấy các phương pháp truyền thống phá hỏng tính liên tục của hệ giả tuần hoàn, Michael Small đã lật ngược thuật toán dự báo S&M: Dùng láng giềng để **mô phỏng hệ thống giả** thay vì dự báo. Ý tưởng này được hiện thực hóa qua 3 bước:

* **Đột biến 1: Chuyển đổi Ngẫu nhiên (Stochastic Shift):** Thay thế phép tính trung bình tất định bằng việc "đổ xúc xắc" chọn láng giềng dựa trên phân phối xác suất hàm mũ $\exp(-d/\rho)$ nhằm tiêm nhiễu vào hệ thống.
* **Đột biến 2: Tối giản bước đi (Simplicity):** Loại bỏ các phương trình toán học phức tạp (như nội suy tuyến tính). Quỹ đạo Surrogate mượn trực tiếp bước tiến thời gian của láng giềng: $s_{i+1} = z_{t+1}$.
* **Đột biến 3: Chuyên biệt hóa Giả thuyết Null:** Tập trung giải quyết một giả thuyết duy nhất: "Quỹ đạo chu kỳ bị chi phối bởi nhiễu không tương quan". Bán kính $\rho$ được dùng để khóa chặt tính chu kỳ vĩ mô, chỉ cho phép nhiễu xáo trộn ở các vi cấu trúc.

# GIẢI THÍCH TOÁN HỌC CHO HÀM MŨ TRONG THIẾT KẾ PPS

Xét xác suất chuyển trạng thái:

$$
P(s_j=z_t\mid s_i)\propto
\exp\left(
-\frac{\lVert z_t-s_i\rVert}{\rho}
\right)
$$

với:

- $s_i$: trạng thái hiện tại trong không gian pha  
- $z_t$: trạng thái ứng viên  
- $\rho$: tham số điều khiển mức nhiễu / độ cục bộ của quá trình lấy mẫu  

Việc lựa chọn nhân hàm mũ không đơn thuần là một quyết định kỹ thuật mà có thể được giải thích từ ba góc nhìn bổ sung.

---

## 1. Góc nhìn thống kê nhiệt: Hạt nhân kiểu Boltzmann

Biểu thức trên có cùng dạng toán học với phân bố Gibbs–Boltzmann:

$$
P(x)\propto e^{-E(x)/(kT)}
$$

Trong PPS:

$$
E(z_t)=\lVert z_t-s_i\rVert
$$

được hiểu như một **chi phí chuyển trạng thái**, còn $\rho$ đóng vai trò tương tự một **thang nhiệt**.

### Các giới hạn quan trọng

- Khi $\rho\rightarrow0$: xác suất tập trung vào các trạng thái rất gần → quỹ đạo gần như tái tạo tín hiệu gốc.
- Khi $\rho\rightarrow\infty$: phân bố tiến gần đồng đều → mất cấu trúc động lực học.

Do đó, $\rho$ điều khiển sự đánh đổi giữa:

- bảo toàn cấu trúc;
- và mức ngẫu nhiên được đưa vào.

> Lưu ý: đây là phép tương đồng toán học với Gibbs–Boltzmann, không phải diễn giải nhiệt động lực học theo nghĩa vật lý nghiêm ngặt.

---

## 2. Góc nhìn hình học: Láng giềng mềm (Soft Neighborhood)

Các phương pháp chọn láng giềng kiểu ngưỡng cứng có dạng:

$$
P=
\begin{cases}
1,& d<r\\
0,& d\ge r
\end{cases}
$$

Cách tiếp cận này tạo ra biên quyết định rời rạc trong không gian pha.

Ngược lại, PPS sử dụng:

$$
w(d)=e^{-d/\rho}
$$

tạo ra một trường trọng số liên tục:

- điểm gần được ưu tiên mạnh;
- điểm xa bị suy giảm xác suất dần dần;
- không tồn tại ranh giới cắt đột ngột.

Nhờ đó quỹ đạo surrogate thay đổi trơn hơn theo hình học của dữ liệu.

---

## 3. Góc nhìn động lực học: Hạn chế chuyển tiếp xa

Trong các hệ giả tuần hoàn, hai trạng thái gần nhau theo khoảng cách Euclide chưa chắc thuộc cùng pha động lực học.

Do:

$$
\frac{P(d+\Delta d)}{P(d)}
=
e^{-\Delta d/\rho}
$$

xác suất giảm theo hàm mũ khi khoảng cách tăng.

Kết quả là:

- bước nhảy lớn trở nên hiếm;
- chuyển tiếp cục bộ được ưu tiên;
- quỹ đạo sinh ra có xu hướng bám theo đa tạp trạng thái thay vì cắt ngang cấu trúc động lực học.

Điều này không bảo đảm bảo toàn pha tuyệt đối, nhưng tạo ra một thiên hướng thống kê ưu tiên tính liên tục của quỹ đạo.

---

## Kết luận

Nhân xác suất mũ trong PPS có thể được xem như một **kernel lấy mẫu kiểu Gibbs dựa trên khoảng cách**.

Vai trò của nó không phải tạo nhiễu thuần túy mà là tạo **ngẫu nhiên có kiểm soát**: đủ để làm suy yếu tương quan vi mô giữa các chu kỳ nhưng vẫn duy trì phần lớn cấu trúc hình học và động lực học của quỹ đạo gốc.


### TỔNG KẾT: BẢN CHẤT "NHÀ GIẢ KIM" CỦA THUẬT TOÁN PPS

Triết lý của Michael Small trong thuật toán PPS không phải là sao chép, mà là tái cấu trúc động lực học thông qua sự cân bằng tinh tế giữa tính tất định và tính ngẫu nhiên.

*   **Vai trò của Hàm mũ $\exp(-d/\rho)$ (Bộ lọc không gian phi tuyến):**
    *   Đóng vai trò là một "lực hấp dẫn xác suất", định nghĩa tầm ảnh hưởng của các điểm lân cận mà không sử dụng ranh giới cứng nhắc.
    *   Phân cấp các láng giềng dựa trên khoảng cách Euclide, cho phép thuật toán ưu tiên sự liên tục của hệ thống trong khi vẫn mở ra cơ hội khám phá toàn bộ không gian pha.

*   **Vai trò của Tham số $\rho$ (Thang điều chuẩn độ dốc):**
    *   $\rho$ là "chiết áp" điều khiển sự cân bằng giữa tính tất định và tính ngẫu nhiên.
    *   **$\rho$ thấp (Độ dốc gắt):** Ưu tiên tuyệt đối các điểm cực gần, ép hệ thống vào trạng thái "đóng băng" (tất định), làm mất tính ngẫu nhiên cần thiết của Surrogate.
    *   **$\rho$ cao (Độ dốc phẳng):** Triệt tiêu mọi sự ưu tiên, biến việc lấy mẫu thành ngẫu nhiên đồng nhất (uniform random), khiến dữ liệu trở thành nhiễu trắng và mất hoàn toàn cấu trúc động lực học.
    *   **$\rho$ tối ưu:** Tạo ra một "vùng láng giềng mềm" (soft neighborhood) vừa đủ thoải để thuật toán vừa bám sát hình thái đa tạp gốc (vĩ mô), vừa đủ linh hoạt để "nhảy" sang các chu kỳ khác, phá vỡ liên kết tất định (vi mô).

*   **Bản chất của Việc chọn ngẫu nhiên ưu tiên (Weighted Random Choice):**
    *   Đây là sự kết hợp giữa **cơ chế lấy mẫu theo phân phối** và **không gian dữ liệu hợp lý**.
    *   "Ưu tiên" giúp Surrogate cam kết với cấu trúc thực tế của hệ động lực học (giữ lại cốt cách), trong khi "ngẫu nhiên" giúp Surrogate xóa bỏ ký ức về trình tự thời gian (phá vỡ tính tất định).
    *   PPS tạo ra dữ liệu giả có "hình hài" giống bản gốc nhưng không chứa các mối liên kết phi tuyến tinh vi, tạo nền tảng hoàn hảo để phân tách các đặc trưng phi tuyến từ tín hiệu PPG.