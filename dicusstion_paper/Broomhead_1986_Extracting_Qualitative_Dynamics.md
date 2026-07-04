# 📘 BẢN ĐẶC TẢ TOÁN HỌC: MỤC 3.1 - HỆ THỐNG KỲ DỊ (THE SINGULAR SYSTEM)
*Trích xuất từ: Broomhead & King (1986) - Extracting Qualitative Dynamics from Experimental Data*

Mục 3.1 thiết lập nền tảng hình học và thống kê, biến một chuỗi dữ liệu vô hướng 1D thành một toán tử tuyến tính nối liền hai không gian: Thời gian và Trạng thái. Đây là bước "hợp pháp hóa" toán học trước khi gọi thuật toán SVD.

---

### 1. Khởi tạo Không gian Trạng thái (State Space)

**Phát biểu Toán học:**
Cho một chuỗi thời gian vô hướng gồm $N_T$ điểm quan sát: $\{v_1, v_2, \dots, v_{N_T}\}$. 
Sử dụng một cửa sổ quan sát có độ dài $n$ ($n \ll N_T$) trượt dọc theo chuỗi dữ liệu (với độ trễ lấy mẫu $J=1$). Tại mỗi bước trượt $i$, ta thu được một vector cột $x_i \in \mathbb{R}^n$:
$$x_i = (v_i, v_{i+1}, \dots, v_{i+n-1})^T$$
Tổng số vector trạng thái sinh ra là $N = N_T - (n-1)$.

**💡 Giải nghĩa Thực hành (Đám mây điểm):**
* **Vật lý:** Chuỗi $v_i$ là tín hiệu 1D (như PPG) dao động theo thời gian. 
* **Hình học:** Mỗi vector $x_i$ đại diện cho tọa độ của **một điểm duy nhất** trong Không gian Nhúng $n$ chiều ($\mathbb{R}^n$). 
* Quá trình trượt cửa sổ $N$ lần tương đương với việc "rải" $N$ điểm vào không gian, tạo thành một "đám mây điểm" mang hình dáng của đa tạp hỗn mang.

---

### 2. Ma trận Quỹ đạo và Ánh xạ Tuyến tính

**Phát biểu Toán học:**
Tập hợp các vector trạng thái $x_i$ tạo thành Ma trận Quỹ đạo (Trajectory Matrix) $X$ kích thước $N \times n$:
$$X = \frac{1}{\sqrt{N}} \begin{bmatrix} x_1^T \\ x_2^T \\ \vdots \\ x_N^T \end{bmatrix}$$
Ma trận $X$ hoạt động như một ánh xạ tuyến tính nối hai không gian: Không gian Nhúng $\mathbb{R}^n$ và Không gian Thời gian $\mathbb{R}^N$.

**💡 Giải nghĩa Thực hành (Hệ số Chuẩn hóa):**
* Hệ số $\frac{1}{\sqrt{N}}$ không phải là chuẩn hóa biên độ thông thường. Trong đại số tuyến tính, khi ta tính ma trận hiệp phương sai $X^T X$, phép nhân ma trận bản chất là phép cộng dồn $N$ phần tử. 
* Việc nhân trước $N^{-1/2}$ đảm bảo rằng $X^T X$ sẽ tự động chứa hệ số $\frac{1}{N}$. Phép cộng dồn nay biến thành **Phép tính Trung bình (Average)**, giúp ma trận không bị phân kỳ (phình to đến vô cực) khi độ dài chuỗi tín hiệu $N \to \infty$.

---

### 3. Sự giao hoán Không gian - Thời gian (Tính Ergodic)

**Phát biểu Toán học:**
Sử dụng vector cơ sở chuẩn $e_i \in \mathbb{R}^N$ (vector có phần tử thứ $i$ bằng 1, còn lại bằng 0) để trích xuất trạng thái tại một thời điểm cụ thể:
$$x_i^T = \sqrt{N} e_i^T X$$
Mở rộng cho một tổ hợp tuyến tính với vector trọng số $w \in \mathbb{R}^N$:
$$\text{Tổ hợp tuyến tính} = w^T X$$

**💡 Giải nghĩa Thực hành (Bản chất Ergodicity):**
* **Toán tử trích xuất:** $e_i$ đóng vai trò là một "nhãn thời gian". Phép nhân $e_i^T X$ có nghĩa là: *"Hãy chỉ định thời điểm $i$, hệ thống sẽ trả về tọa độ không gian vật lý của bộ hấp dẫn tại thời điểm đó"*.
* **Giả thuyết Ergodic:** Phép tính $w^T X$ gom nhiều hàng của $X$ lại để tính trung bình. Điều này chứng minh sự tương đương tuyệt đối (giao hoán) giữa hai hành động:
    1.  **Trung bình Thời gian (Time-average):** Theo dõi sự thay đổi của tín hiệu dọc theo trục thời gian dài.
    2.  **Trung bình Không gian (Space-average):** Chụp một bức ảnh toàn cảnh của đám mây điểm trên không gian $\mathbb{R}^n$ tại một khoảnh khắc.

---

### 4. Kết luận Đóng gói (The Triple)

**Phát biểu Toán học:**
Hệ thống động lực được đóng gói chính thức thành một cấu trúc bộ ba (the triple):
$$\mathbf{(X, \mathbb{R}^n, \mathbb{R}^N)}$$

**💡 Giải nghĩa Thực hành (Giấy phép Toán học):**
* Phép phân tích SVD chỉ có ý nghĩa vật lý khi và chỉ khi nó được áp dụng lên một toán tử tuyến tính kết nối hai **Không gian Hilbert** (không gian có định nghĩa chặt chẽ về tích vô hướng và khoảng cách).
* Bằng việc định nghĩa rõ ràng tích vô hướng trên $\mathbb{R}^n$ (hình học quỹ đạo) và $\mathbb{R}^N$ (thống kê thời gian), tác giả đã tạo ra một "bản hợp đồng" toán học. 
* **Hệ quả tối hậu:** Mọi trị kỳ dị (Singular values - $\sigma_i$) sinh ra từ SVD ở các mục sau chắc chắn không phải là những con số vô nghĩa, mà chúng chính là đại lượng đo lường **Năng lượng/Phương sai** thực sự của hệ thống hỗn mang.

# 📘 BẢN ĐẶC TẢ TOÁN HỌC: MỤC 3.2 - SỰ ĐỘC LẬP VÀ TÍNH TRỰC GIAO (INDEPENDENCE & ORTHOGONALITY)
*Trích xuất từ: Broomhead & King (1986) - Extracting Qualitative Dynamics from Experimental Data*

Mục 3.2 là bước chuyển đổi hình học cốt lõi: Từ bỏ hệ trục tọa độ trễ thời gian tùy ý (vốn chứa đầy sự trùng lặp) để đi tìm một hệ cơ sở trực giao duy nhất, được chi phối và định hình bởi chính bản chất của dữ liệu.

---

### 1. Ma trận Hiệp phương sai (The Covariance Matrix) - Không gian Nhúng $\mathbb{R}^n$

**Phát biểu Toán học:**
Định nghĩa ma trận $\Xi$ (Kích thước $n \times n$) trên không gian $\mathbb{R}^n$ (Công thức 3.9):
$$\Xi = X^T X = \frac{1}{N} \sum_{i=1}^N x_i x_i^T$$

**💡 Giải nghĩa Thực hành (Đo lường sự dư thừa):**
* Kích thước của $\Xi$ rất nhỏ (ví dụ $50 \times 50$), cực kỳ dễ tính toán đối với máy tính.
* **Bản chất Thống kê:** $\Xi$ chính là Ma trận Hiệp phương sai. Nó chứa giá trị tương quan trung bình theo thời gian (time-averaged correlation) giữa mọi cặp tọa độ trễ nằm trong cửa sổ thời gian $n$. Nếu $\Xi$ có các giá trị ngoài đường chéo lớn, điều đó gào thét rằng: *"Các trục tọa độ trễ của Takens đang chứa thông tin lặp lại của nhau!"*

---

### 2. Khai triển Trị riêng (Eigendecomposition) - Sinh ra Hệ cơ sở mới

**Phát biểu Toán học:**
Giải bài toán trị riêng cho ma trận đối xứng $\Xi$ (Công thức 3.8):
$$\Xi c_i = \sigma_i^2 c_i$$
Toán tử trực giao: Tập hợp các vector riêng $\{c_i\}$ tạo thành một **Hệ cơ sở trực giao hoàn chỉnh** (Complete orthonormal basis) mới cho không gian $\mathbb{R}^n$. 

**💡 Giải nghĩa Thực hành (Đập bỏ sự "Tùy ý"):**
* Thay vì bám víu vào hệ trục $x(t), x(t+\tau)$ một cách mù quáng, thuật toán tự động xoay không gian để tìm ra các trục $c_i$ trực giao (vuông góc 100%) với nhau. 
* Trên hệ trục mới này, mọi sự dư thừa thông tin bị tiêu diệt. Việc sử dụng $\{c_i\}$ chính thức phá hủy hoàn toàn tính "tùy ý" của phương pháp Takens gốc.

---

### 3. Ma trận Cấu trúc (The Structure Matrix) - Không gian Thời gian $\mathbb{R}^N$

**Phát biểu Toán học:**
Định nghĩa ma trận $\Theta$ (Kích thước $N \times N$) trên không gian thời gian $\mathbb{R}^N$:
$$\Theta = X X^T$$
Bài toán trị riêng cho $\Theta$ (Công thức 3.5):
$$\Theta s_i = \sigma_i^2 s_i$$
(Với $\{s_i\}$ là các vector riêng trực giao trong $\mathbb{R}^N$).

**💡 Giải nghĩa Thực hành (Bức tranh Toàn cảnh):**
* Kích thước của $\Theta$ vô cùng khổng lồ (ví dụ $10.000 \times 10.000$ điểm dữ liệu), việc giải trực tiếp bài toán trị riêng cho nó là một thảm họa tính toán (OOM - Out of Memory).
* **Bản chất Thống kê:** Nếu $\Xi$ đo tương quan giữa các *trục không gian*, thì $\Theta$ đo sự tương quan giữa tất cả các *mẫu hình (patterns)* thời gian đã từng xuất hiện dọc theo tín hiệu. 

---

### 4. Mối liên hệ Kép (Ánh xạ qua lại Không gian - Thời gian)

**Phát biểu Toán học:**
Tác giả chứng minh hai không gian $\mathbb{R}^n$ và $\mathbb{R}^N$ liên kết chặt chẽ với nhau thông qua chính các trị số $\sigma_i$:
* Ánh xạ $\mathbb{R}^N \rightarrow \mathbb{R}^n$ (Công thức 3.3): $\quad s_i^T X = \sigma_i c_i^T$
* Ánh xạ $\mathbb{R}^n \rightarrow \mathbb{R}^N$ (Công thức 3.7): $\quad X c_i = \sigma_i s_i$

**💡 Giải nghĩa Thực hành (Nền tảng của SVD):**
* Đây là một cú "hack" toán học tuyệt đẹp! Vì $\Theta$ quá lớn không thể tính được, ta chỉ cần giải $\Xi$ (rất nhỏ) để tìm $c_i$ và $\sigma_i$. Sau đó, dùng công thức $s_i = \frac{1}{\sigma_i} X c_i$ để suy ngược ra $s_i$ của $\Theta$ mà không tốn sức.
* *(Góc nhìn Kỹ sư AI)*: Khung toán học phản xạ chéo này chính là nền tảng nguyên thủy để xây dựng nên phép phân tích SVD: $X = S \Sigma C^T$ mà ta sẽ sử dụng ở Mục 3.3.

---

### 5. Kết luận Hình học: Số chiều Bản chất (Intrinsic Dimensionality)

**Phát biểu Toán học:**
Định lý Hạng (Rank): Toán học chứng minh được:
$$\text{Rank}(\Theta) = \text{Rank}(\Xi) = n' \quad (\text{với } n' \le n)$$
Không gian $\mathbb{R}^n$ (và tương ứng là $\mathbb{R}^N$) bị phân tách làm 2 phần:
1. **Không gian con (Subspace) $n'$ chiều:** Nơi chứa đa tạp (manifold) của quỹ đạo hệ động lực thực sự.
2. **Phần bù trực giao (Orthogonal complement):** Không gian trống rỗng, nơi mọi tín hiệu bị triệt tiêu ($\sigma_i = 0$).

**💡 Giải nghĩa Thực hành (Giới hạn của Hỗn mang):**
* Cho dù bạn cố tình chọn cửa sổ $n=50$ (tạo ra không gian 50 chiều), thì hệ thống cũng tự động nhận ra rằng đám mây điểm quỹ đạo thực chất phẳng lỳ ở 46 chiều, và nó chỉ sống trong một không gian con $n'=4$ chiều mà thôi.
* **Chốt hạ:** Số $n'$ này chính là giới hạn trên (upper bound) của **Số chiều Bản chất (Intrinsic Dimensionality)** mà bộ hấp dẫn thực sự chiếm hữu. Bất kỳ chiều nào vượt ra ngoài $n'$ đều là vô nghĩa (cho đến khi Nhiễu Trắng xuất hiện ở Mục 3.3 và làm đảo lộn giới hạn này).

# 📘 GHI CHÚ MỤC 3.3: PHÂN TÍCH GIÁ TRỊ KỲ DỊ VÀ NHIỄU (SVD AND NOISE)
*Mục này giải quyết bài toán thực tế: Tách bạch Động lực học tất định (Chaos) ra khỏi Nhiễu đo lường ngẫu nhiên (Noise) ngay trên không gian pha.*

---

### 1. Phân tích SVD và Hình học của Quỹ đạo ảo

**Định lý SVD (Công thức 3.12):**
Ma trận quỹ đạo được phân rã thành:
$$X = S \Sigma C^T$$
* $C = (c_1, c_2, \dots, c_n)$: Ma trận vector kỳ dị không gian (các trục tọa độ trực giao).
* $\Sigma = \text{diag}(\sigma_1, \sigma_2, \dots, \sigma_n)$: Ma trận đường chéo chứa các trị kỳ dị giảm dần.

**Năng lượng hình chiếu (Công thức 3.11):**
$$(XC)^T(XC) = \Sigma^2$$

**💡 Ý nghĩa Hình học & Vật lý:**
Đám mây điểm quỹ đạo $X$ tạo thành một khối **Ellipsoid** trong không gian $n$ chiều. 
* $c_i$ xác định **hướng** của các trục chính.
* $\sigma_i^2$ là bình phương hình chiếu trung bình, đại diện cho **năng lượng (phương sai)** của tín hiệu dọc theo trục $c_i$. Trục có $\sigma_i^2$ càng lớn thì dao động hỗn mang trên đó càng mạnh.

---

### 2. Mô hình Nhiễu và Khám phá "Sàn Nhiễu" (The Noise Floor)

**Giả định Nhiễu cộng (White Noise):**
Tín hiệu đo được gồm tín hiệu sạch ($\bar{v}$) và nhiễu trắng ngẫu nhiên ($\xi$):
$$v_j = \bar{v}_j + \xi_j$$

**Sự phân rã Hiệp phương sai:**
Vì nhiễu trắng đẳng hướng và không có tương quan chéo, ma trận hiệp phương sai tổng $\Xi$ tách làm đôi:
$$\Xi = \bar{\Xi} + \langle \xi^2 \rangle \mathbf{I}_n$$
*(Trong đó $\mathbf{I}_n$ là ma trận đơn vị, $\langle \xi^2 \rangle$ là phương sai của nhiễu).*

**Phương trình Sinh tử (Công thức 3.13 - Sự dịch chuyển phổ):**
$$\sigma_i^2 = \bar{\sigma}_i^2 + \langle \xi^2 \rangle$$

**💡 Ý nghĩa Hình học & Vật lý (Khoảnh khắc Eureka):**
* Nhiễu trắng hoạt động như một "đám sương mù hình cầu", cộng thêm một lượng năng lượng $\langle \xi^2 \rangle$ vào **mọi hướng** trong không gian.
* Với hệ động lực có số chiều hữu hạn $d$, từ trục thứ $d+1$ trở đi, tín hiệu gốc không tồn tại ($\bar{\sigma}_i^2 = 0$). 
* Khi đó: $\sigma_i^2 = \langle \xi^2 \rangle$ (với mọi $i > d$). Các trị kỳ dị này bằng nhau chằn chặn, tạo thành một đường chạy ngang trên đồ thị logarit. Đây chính là **Sàn nhiễu (Noise Floor)**.

---

### 3. Phân lập Không gian và Triệt tiêu Nhiễu (Subspace Filtering)

**Toán tử Chiếu và Cắt tỉa (Công thức 3.16):**
Chia không gian làm 2 phần: $P$ (vùng tín hiệu vượt sàn nhiễu) và $Q$ (vùng bị nhiễu thống trị).
$$X = \bar{X} + \Delta X$$
*(Bỏ $\Delta X$, chỉ giữ lại $\bar{X}$)*.

**Đầu ra Thực hành (Công thức 3.19 - Tái tạo đa tạp):**
$$\bar{X} = \sum_{\sigma_i > \text{noise}} (X c_i) c_i^T$$

**💡 Ý nghĩa Kỹ thuật (Chốt chặn cho AI):**
* Thay vì dùng bộ lọc thông dải (Bandpass) cắt theo tần số, đây là quá trình **từ chối nhiễu ngoài dải trên không gian pha**. 
* Phép tính $(X c_i) c_i^T$ lấy quỹ đạo thô chiếu lên các trục sạch ($i \le d$), sau đó xây dựng lại một không gian con hoàn toàn nhẵn bóng.
* **Hệ quả tối hậu:** Dữ liệu $\bar{X}$ (hoặc chuỗi 1D tái tạo từ nó) được giải phóng khỏi các rung động ngẫu nhiên của thiết bị đo. Khi đưa vào mô hình học sâu, AI sẽ bị ép phải học các đặc trưng hỗn mang nội tại ($\bar{\sigma}_i^2$) thay vì học thuộc lòng nhiễu cảm biến ($\langle \xi^2 \rangle$).