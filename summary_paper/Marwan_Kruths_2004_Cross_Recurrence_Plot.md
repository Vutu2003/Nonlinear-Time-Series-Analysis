# Paper Metadata
* **Title:** Nonlinear analysis of bivariate data with cross recurrence plots
* **Authors:** Norbert Marwan, Jürgen Kurths
* **Year:** 2002
* **Keywords:** Data analysis; Correlation test; Cross recurrence plot; Nonlinear dynamics

# WHY
### 1. Research Question
Làm thế nào để định lượng và phát hiện các mối quan hệ động lực học (dynamical interrelations) giữa hai hệ thống thông qua các chuỗi thời gian ngắn, phi dừng và phi tuyến mà chúng sinh ra?

### 2. Motivation
*   **Đặc tính dữ liệu tự nhiên:** Dữ liệu thực tế thu được thường vô cùng phức tạp, phi dừng và có độ dài ngắn do giới hạn số lượng phép đo.
*   **Khoảng trống của RP đơn biến:** Các kỹ thuật RP và RQA truyền thống chỉ khảo sát động lực học nội tại của một hệ thống đơn lẻ, không thể đánh giá trực tiếp mức độ tương đồng hay tương tác giữa hai hệ động lực khác nhau.
*   **Khám phá độ trễ và nhân quả:** Cần một công cụ để nhận diện các kỷ nguyên tương tác phi tuyến, đồng thời xác định các khoảng thời gian trễ (lags) nhằm đề xuất liên kết nhân quả giữa hai hệ thống.

### 3. Previous Methods & Limitations
*   **Phương pháp tuyến tính (Linear correlation):** Chỉ phản ánh sự đồng biến của dữ liệu quan sát, nhưng không đủ khả năng phát hiện các mối quan hệ động lực học phi tuyến ngầm ẩn giữa các hệ thống.
*   **Phương pháp phi tuyến cổ điển (Fractal, Lyapunov, Mutual Information):** Đòi hỏi chuỗi dữ liệu dài; việc áp dụng thiếu phê phán lên các dữ liệu ngắn, phi dừng thường dẫn đến những cạm bẫy (pitfalls) sai lệch nghiêm trọng.
*   **Sự đột phá của RQA trên CRP:** Đóng góp cốt lõi của CRP là việc nhúng hai quá trình vào cùng một không gian pha và **chuyển đổi các thước đo RQA thành các hàm phụ thuộc độ trễ (lag-dependent functions)**. Các chỉ số như $RR(t)$, $DET(t)$ và $L(t)$ dịch chuyển dọc theo các đường chéo để trả lời chính xác câu hỏi: Hai hệ thống có đang cùng trải qua một hành vi động lực học hay không, và nếu có thì chúng lệch nhau bao nhiêu thời gian?
*   

### 2. What

#### Core Insight (Triết lý cốt lõi)
Đột phá của Biểu đồ hồi quy chéo (CRP) là sự dịch chuyển đối tượng nghiên cứu từ *một* quỹ đạo sang *hai* quỹ đạo, dẫn đến một bước ngoặt về mô hình đánh giá (paradigm shift). Triết lý này được cấu trúc theo 3 tầng logic:

*   **Tầng 1 - Từ Self-recurrence sang Cross-recurrence:** Nếu RP trả lời câu hỏi "Một hệ thống có quay lại trạng thái cũ không?", thì CRP trả lời câu hỏi "Hai hệ thống có cùng tiến hóa trong không gian pha không?". Hai chuỗi thời gian được nhúng riêng biệt thành hai quỹ đạo, nhưng được biểu diễn và so sánh chung trong cùng một hệ tọa độ không gian pha.
*   **Tầng 2 - Khái niệm Lag (Độ trễ):** Sự dịch chuyển ra khỏi đường chéo chính (diagonal offset) trong ma trận CRP chính là độ trễ thời gian $t$ giữa hai hệ thống.
*   **Tầng 3 - Lag-dependent RQA (RQA theo độ trễ):** Các thước đo RQA không còn là các giá trị vô hướng (scalar, ví dụ: $DET = 0.81$) tĩnh như trong RP. Thay vào đó, chúng biến thành các hàm số/tín hiệu chạy theo trục độ trễ $t$ (ví dụ: $DET(-50), ..., DET(0), ..., DET(+50)$).

**Sơ đồ Tóm tắt Paradigm Shift:**
*   **RP** $\rightarrow$ **RQA (Scalar)** $\rightarrow$ *Does one system return?*
*   **CRP** $\rightarrow$ **Lag-specific RQA (Function)** $\rightarrow$ *Do two systems evolve together, and at what lag?*

---

#### Mathematical Foundation (Nền tảng toán học)

Nền tảng của CRP được chia thành hai tầng rõ rệt:

**Tầng 1: Đối tượng hình học (Ma trận CRP)**
Là ma trận đối chiếu khoảng cách giữa mọi điểm của quỹ đạo $\vec{x}$ và quỹ đạo $\vec{y}$:
$$CR_{i,j} = \Theta(\epsilon - \|\vec{x}_i - \vec{y}_j\|)$$

**Tầng 2: Đối tượng thống kê ($P_t(l)$) & Các phiếm hàm**
Mọi chỉ số định lượng đều bắt nguồn từ $P_t(l)$ – hàm phân bố tần suất của các đường chéo độ dài $l$ nằm trên đường chéo trễ $t$. Từ đối tượng thống kê này, hệ thống dẫn xuất ra 3 phiếm hàm (functional):

*   **$RR(t)$ (Recurrence Rate):** 
    *   Đo lường xác suất xuất hiện các trạng thái tương đồng giữa hai hệ thống tại độ trễ $t$. 
    *   Về mặt thực tiễn, $RR(t)$ có khả năng kháng cự và ít nhạy cảm với các biến động nhiễu làm đứt gãy đường chéo hơn so với các chỉ số còn lại.
    *   $$RR(t) = \frac{1}{N-t} \sum_{l=1}^{N-t} l P_t(l)$$

*   **$DET(t)$ (Determinism):** 
    *   Đo lường tỷ lệ hai quỹ đạo tiến hóa tương tự nhau trong một khoảng thời gian tại mốc trễ $t$. 
    *   Giá trị $DET(t)$ thấp không hẳn có nghĩa là hệ ngẫu nhiên, mà phản ánh việc hai quỹ đạo không còn đồng bộ. Ngược lại, $DET(t)$ cao bộc lộ hành vi tiến hóa song hành mạnh mẽ.
    *   $$DET(t) = \frac{\sum_{l=l_{min}}^{N-t} l P_t(l)}{\sum_{l=1}^{N-t} l P_t(l)}$$

*   **$L(t)$ (Average Diagonal Line Length):** 
    *   Đại lượng này lượng hóa chính xác *khoảng thời gian duy trì liên tục sự tương đồng động lực học* giữa hai hệ thống.
    *   $$L(t) = \frac{\sum_{l=l_{min}}^{N-t} l P_t(l)}{\sum_{l=l_{min}}^{N-t} P_t(l)}$$
*   

### 3. How

#### 3.1 Algorithm
Quá trình phân tích CRP vận hành theo một luồng trích xuất độ trễ (lag) rất tự nhiên:
1.  **Embedding (Nhúng không gian pha):** Tái dựng hai chuỗi thời gian thành hai quỹ đạo không gian pha $\vec{x}_i$ và $\vec{y}_j$.
2.  **Cross Distance Matrix (Ma trận khoảng cách chéo):** Tính toán khoảng cách giữa mọi cặp điểm thuộc hai quỹ đạo.
3.  **Cross Recurrence Matrix (Ma trận hồi quy chéo):** Nhị phân hóa khoảng cách bằng một ngưỡng $\epsilon$.
4.  **Extract every diagonal (Trích xuất độ trễ):** Khảo sát từng đường chéo song song với đường chéo chính (Line of Identity - LOI); khoảng cách từ một đường chéo tới LOI chính là độ trễ (lag) $t$.
5.  **Compute $P_t(l)$:** Tại mỗi mốc trễ $t$, lập hàm phân bố tần suất của các đường chéo có độ dài $l$.
6.  **Compute Metrics:** Từ $P_t(l)$, tính toán $RR(t)$, $DET(t)$ và $L(t)$.

#### 3.2 Mathematical Formulation
*   **Không gian pha:** $\vec{x}_i = (u_i, u_{i+\tau}, \dots, u_{i+(m-1)\tau})$.
*   **Ma trận CRP:** $CR_{i,j} = \Theta(\epsilon - \|\vec{x}_i - \vec{y}_j\|)$.
*   **Trục độ trễ $t$:** Được định nghĩa là offset (khoảng cách) từ LOI. Về mặt lý thuyết $t \in [-(N-1), \dots, N-1]$. Tuy nhiên, trong thực nghiệm, người ta thường chỉ khảo sát một khoảng trễ hữu hạn $t \in [-T, T]$ quanh LOI.
*   **Các phiếm hàm theo độ trễ:**
    *   $$RR(t) = \frac{1}{N-t}\sum_{l=1}^{N-t}lP_t(l)$$
    *   $$DET(t) = \frac{\sum_{l=l_{min}}^{N-t}lP_t(l)}{\sum_{l=1}^{N-t}lP_t(l)}$$
    *   $$L(t) = \frac{\sum_{l=l_{min}}^{N-t}lP_t(l)}{\sum_{l=l_{min}}^{N-t}P_t(l)}$$

#### 3.3 End-to-End Pipeline
1.  **Tiền xử lý:** Nếu hai chuỗi có cùng độ dài và cùng thang đo thời gian (time scale), CRP sẽ trở thành ma trận vuông, rất thuận tiện cho việc diễn giải hình học.
2.  **Khởi tạo:** Thuật toán FNN tìm chiều nhúng $m$, hàm MI tìm độ trễ $\tau$.
3.  **Quét RQA Thuận:** Dựng ma trận CRP và xuất ra bộ ba response curves $RR_+(t)$, $DET_+(t)$, $L_+(t)$.
4.  **Quét RQA Nghịch:** Đảo dấu chuỗi thứ hai (nhân $-1$) và quét lại để xuất ra $RR_-(t)$, $DET_-(t)$, $L_-(t)$. Việc đảo dấu biến mối quan hệ nghịch pha thành đồng pha trong không gian pha, nhờ đó vẫn có thể sử dụng cùng một bộ chỉ số dựa trên đường chéo.
5.  **Gợi ý nhân quả:** Quan sát cực đại trên đồ thị để định vị khoảng trễ (lag), từ đó đề xuất hoặc gợi ý các quan hệ nhân quả (causal links) thay vì mang tính chứng minh tuyệt đối.

#### 3.4 Computational Complexity
*   **Embedding:** $\mathcal{O}(Nm)$.
*   **Distance Matrix:** $\mathcal{O}(N^2m)$.
*   **Lag Scan & Metrics:** $\mathcal{O}(N^2)$.

#### 3.5 Implementation Notes
*   **Kháng nhiễu với $RR(t)$:** Khi nhiễu phủ mạnh làm vỡ vụn các cấu trúc đường chéo dài, $RR(t)$ vẫn hoạt động bền bỉ vì nó chỉ đếm xác suất lặp lại trạng thái.
*   **Xử lý tính phi dừng:** Sử dụng bán kính lân cận biến thiên (điều chỉnh để số lượng láng giềng cố định) giúp duy trì mật độ điểm và đối phó tốt với dữ liệu phi dừng.
*   **Diễn giải $L(t)$:** Nên xem $L(t)$ như một đại lượng đo lường thời gian dự báo trung bình, tránh khiên cưỡng gắn trực tiếp với số mũ Lyapunov đối với tín hiệu thực tế.
*   **Embedding Compatibility (Tính tương thích nhúng):** CRP giả định hai hệ thống được biểu diễn trong cùng một hệ tọa độ phase space (thường dùng chung $m$ và $\tau$). Nếu hai hệ yêu cầu các thông số tối ưu quá khác biệt, việc diễn giải khoảng cách động lực học cần được cân nhắc hết sức cẩn thận.

> **Core Philosophy:** Về bản chất, CRP không thay đổi định nghĩa toán học của các chỉ số RQA cổ điển, mà mở rộng chúng thành các hàm phụ thuộc vào độ trễ thời gian. Chính sự thay đổi từ "một giá trị toàn cục" (scalar) sang "một hàm theo lag" (function) đã cho phép định vị chính xác thời điểm hai hệ thống đạt mức tương đồng động lực học lớn nhất.


