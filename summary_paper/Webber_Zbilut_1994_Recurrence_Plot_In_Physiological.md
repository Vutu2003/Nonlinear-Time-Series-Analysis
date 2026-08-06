### Paper Metadata
*   **Title:** Dynamical assessment of physiological systems and states using recurrence plot strategies
*   **Authors:** Charles L. Webber, Jr., and Joseph P. Zbilut
*   **Year:** 1994
*   **Keywords:** complex systems; nonlinear dynamics; chaos; determinism; noise; stochasticity; respiration; muscle fatigue; rat
*   

# 1. Why

## Research Question
Làm thế nào để sử dụng các cấu trúc hồi quy (Recurrence Structures) nhằm định lượng và theo dõi sự thay đổi trạng thái của các hệ sinh lý, đặc biệt khi dữ liệu thực nghiệm ngắn và không dừng (non-stationary)?

## Motivation
*   **Bản chất hệ sinh lý:** Là các hệ động lực phức tạp, phi tuyến và liên tục biến đổi. Quan sát chuỗi thời gian 1D truyền thống không đủ để bộc lộ bản chất hệ thống.
*   **Nghịch lý dữ liệu (Stationarity Dilemma):** Cắt chuỗi dữ liệu ngắn để giữ tính dừng sẽ làm giảm độ phân giải; dùng chuỗi dài để tăng chính xác thì dữ liệu lại mất tính dừng.
*   **Hạn chế của công cụ hiện hành:** Phân tích tuyến tính bỏ qua các đặc trưng phi tuyến. Phân tích phi tuyến kinh điển đòi hỏi dữ liệu dài, lý tưởng và có tính dừng cao.
*   **Tiềm năng của Recurrence Plot (RP):** Là công cụ có thể vượt qua ràng buộc về tính dừng và kích thước dữ liệu để phân tích trực tiếp sự biến đổi của hệ sinh lý.

## Previous Methods
*   **Phân tích tuyến tính (Spectral, Coherence):** Phù hợp với hệ tuyến tính tĩnh nhưng thất bại khi mô tả các thay đổi trạng thái phi tuyến.
*   **Phi tuyến cổ điển (Correlation Dimension, Lyapunov):** Yêu cầu quá khắt khe về dữ liệu (phải dài, dừng, ít nhiễu), không khả thi với dữ liệu sinh lý thực tế.
*   **RP nguyên thủy (Eckmann, 1987):** Phát hiện tốt cấu trúc hồi quy nhưng chỉ dừng ở mức quan sát định tính (nhìn bằng mắt).
*   **RQA sơ khai (Zbilut & Webber, 1992):** Đã cung cấp chỉ số định lượng (%REC, %LINE) nhưng là các giá trị tĩnh tính trên toàn chuỗi, chưa cho phép theo dõi sự dịch chuyển động lực học theo thời gian.
*   

# 2. What

## Core Insight

Nghiên cứu năm 1994 nâng cấp Biểu đồ hồi quy (Recurrence Plot - RP) từ một công cụ quan sát định tính thành một hệ thống phân tích định lượng toàn diện, trực tiếp phản ánh trạng thái động lực học của chuỗi thời gian[cite: 1]. 

Thay vì chỉ dựa vào `%recurrence` và `%line segments` như công trình 1992, Webber & Zbilut chính thức hóa hệ thống 5 biến đặc trưng:
*   **%recurrence:** Mật độ các điểm hồi quy trong không gian pha[cite: 1].
*   **%determinism:** Tỷ lệ các điểm hồi quy liên kết thành đoạn thẳng chéo, thể hiện cấu trúc tất định[cite: 1].
*   **Entropy:** Shannon entropy của phân bố độ dài các đoạn chéo, đo lường độ phức tạp toán học của hệ thống[cite: 1].
*   **Ratio:** Tỷ lệ giữa `%determinism` và `%recurrence`, cực kỳ nhạy cảm với các pha chuyển đổi trạng thái sinh lý[cite: 1].
*   **Trend:** Tốc độ nhạt dần của mật độ hồi quy khi ra xa đường chéo chính, dùng để định lượng tính không dừng (drift)[cite: 1].
*   
Các chỉ số này không đại diện cho năm đại lượng độc lập mà phản ánh năm khía cạnh bổ sung của cùng một hệ động lực học:

| Metric | Dynamical Interpretation | Câu hỏi mà chỉ số trả lời |
|---------|--------------------------|---------------------------|
| **%recurrence** | Mật độ các trạng thái quay trở lại trong không gian pha | Hệ có thường xuyên quay lại các trạng thái trước đó không? |
| **%determinism** | Mức độ tổ chức của các quỹ đạo hồi quy thông qua các đoạn chéo | Các lần hồi quy có tuân theo quy luật động lực học hay chỉ xuất hiện ngẫu nhiên? |
| **Entropy** | Độ đa dạng của phân bố độ dài các đoạn chéo | Hệ có bao nhiêu kiểu tiến hóa động lực học khác nhau? |
| **Ratio** | Mức độ cấu trúc của các điểm hồi quy (DET/REC) | Trong các trạng thái hồi quy, bao nhiêu trạng thái thực sự mang tính xác định? |
| **Trend** | Sự thay đổi mật độ hồi quy theo thời gian | Cấu trúc động lực học của hệ có đang biến đổi (drift) hay vẫn duy trì ổn định? |

Nhìn dưới góc độ động lực học, năm chỉ số này tạo thành một hệ thống mô tả nhiều tầng của cùng một quá trình sinh lý. `%recurrence` phản ánh **mức độ quay trở lại** (recurrence density), `%determinism` phản ánh **mức độ tổ chức của quỹ đạo** (trajectory organization), `Entropy` phản ánh **độ phức tạp của cấu trúc động lực học**, `Ratio` đánh giá **mức độ cấu trúc của các trạng thái hồi quy**, trong khi `Trend` mô tả **sự tiến hóa theo thời gian của toàn bộ cấu trúc động lực học**. Thay vì quan sát trực tiếp tín hiệu sinh lý, Webber & Zbilut sử dụng bộ chỉ số này để quan sát trạng thái và sự biến đổi của chính hệ động lực học ẩn phía sau tín hiệu.

Bộ công cụ này giải quyết các rào cản của phương pháp phi tuyến truyền thống, cho phép phân biệt chính xác các trạng thái sinh lý và theo dõi diễn biến động lực học liên tục qua kỹ thuật cửa sổ trượt (sliding window) trên các tập dữ liệu ngắn và không dừng[cite: 1].

---

## Mathematical Foundation

Kế thừa trực tiếp nền tảng đồ thị từ Eckmann (1987) và phương pháp lượng hóa sơ khởi từ Zbilut & Webber (1992), quy trình toán học được hệ thống hóa như sau:

### 1. Tái cấu trúc không gian pha (Phase-space reconstruction)
Từ chuỗi thời gian đơn biến $u(t)$, các hệ biến thay thế (surrogate variables) được khôi phục thông qua phép nhúng trễ[cite: 1]:

$$\mathbf{x}_i = [u_i, u_{i+\tau}, \dots, u_{i+(d-1)\tau}]$$

Với $d$ là số chiều nhúng (embedding dimension) và $\tau$ là độ trễ thời gian (time delay).

### 2. Ma trận hồi quy (Recurrence Plot)
Khoảng cách không gian (Euclid) giữa mọi cặp vectơ trạng thái được tính toán và nhị phân hóa bằng hàm bước Heaviside $\Theta$ kết hợp một ngưỡng bán kính $r$ cố định:

$$R_{ij} = \Theta(r - \|\mathbf{x}_i - \mathbf{x}_j\|)$$

Trong đó:
*   $R_{ij} = 1$: Hai trạng thái tiệm cận và tạo thành điểm hồi quy.
*   $R_{ij} = 0$: Không hồi quy.

### 3. Định lượng bằng cửa sổ trượt (Sliding Window Quantification)
Hệ 5 đại lượng (%REC, %DET, Entropy, Ratio, Trend) được trích xuất trực tiếp từ hình thái phân bố của ma trận $R_{ij}$. Điểm đột phá là các phép toán này không chỉ tính tĩnh trên toàn chuỗi mà được quét lặp lại qua các cửa sổ (epoch) di chuyển dọc theo tín hiệu[cite: 1]. Cấu trúc này tạo ra các chuỗi tham số theo thời gian, cho phép theo dõi sát sao sự tiến hóa của động lực học hệ thống[cite: 1].


# 3. How

## 3.1 Algorithm
1. **Windowing:** Cắt tín hiệu $u(t)$ thành các epoch qua cửa sổ (kích thước $W$, bước dịch $S$).
2. **Embedding:** Dựng không gian pha $\mathbf{x}_i$ bằng phép nhúng trễ ($d$, $\tau$).
3. **RP Matrix:** Lập ma trận hồi quy nhị phân $R_{i,j}$ dựa trên ngưỡng bán kính $r$.
4. **Diagonal Scan:** Quét nửa trên ma trận (trừ đường chéo chính - LOI) tìm đoạn chéo $l \ge l_{min}$.
5. **Quantification:** Tính 5 biến định lượng (%REC, %DET, Entropy, Ratio, Trend).
6. **Sliding:** Tịnh tiến cửa sổ đi $S$ bước và lặp lại.

## 3.2 Dynamic Quantification Principle
Lượng hóa liên tục qua cửa sổ trượt biến các chỉ số tĩnh thành chuỗi thời gian ($REC(t), DET(t)...$), cho phép theo dõi động lực học sinh lý và phát hiện chuyển pha.

## 3.3 Mathematical Formulation
*   **State Vectors:** $\mathbf{x}_i = [u_i, u_{i+\tau}, \dots, u_{i+(d-1)\tau}]$
*   **RP Matrix:** $R_{i,j} = \Theta \left( r - \|\mathbf{x}_i - \mathbf{x}_j\|_2 \right)$
*   **%REC:** Mật độ điểm hồi quy (trừ LOI).
*   **%DET:** Tỷ lệ điểm hồi quy tạo thành đoạn chéo ($l \ge 2$).
*   **Entropy:** $-\sum P_i(l) \log_2 P_i(l)$. (*Lưu ý: Đo hàm lượng thông tin của phân bố độ dài đoạn chéo, không phải độ phức tạp tín hiệu*).
*   **Ratio:** $\text{\%DET} / \text{\%REC}$.
*   **Trend:** Độ dốc tuyến tính của sự suy giảm mật độ hồi quy khi ra xa LOI.

## 3.4 Pipeline
`Signal` $\to$ `Sliding Window` $\to$ `RP` $\to$ `5 Quantitative Variables` $\to$ `Metric Time Series` $\to$ `Transition Detection`

## 3.5 Complexity
*   **Time:** $\mathcal{O}\left( \frac{N_t}{S} \cdot d \cdot W^2 \right)$
*   **Space:** $O(W^2)$ (hoặc $O(W)$ nếu tối ưu mảng).

## 3.6 Implementation Notes
*   **Parameter Consistency:** $r, d, \tau, l_{min}$ **bắt buộc** cố định qua mọi cửa sổ để đảm bảo biến động phản ánh sinh lý, không phải do nhiễu tham số.
*   **Underflow Bug:** Chuyển trạng thái `uint8` gây tràn số. Bắt buộc ép sang `np.int32` trước khi dùng `np.diff()`.
*   **Padding Biên:** Pad thêm $0$ vào hai đầu mảng đường chéo trước tính sai phân để không sót đoạn viền.
*   **Guard Clauses:** Trả về $0.0$ nếu phân đoạn tĩnh (số điểm = 0) để tránh lỗi chia 0 cho %DET và Ratio.
*   **Overlap Trade-off:** $S=1$ cho độ phân giải cực đại; $S=10-20$ cho ứng dụng thời gian thực/chip nhúng để giảm tải tính toán.
*   

# 4. Validation

## 4.1 Assumptions (Giả định nền tảng)
*   **Nonstationarity:** Tín hiệu sinh lý vốn không dừng (drift, chuyển pha), phá vỡ giả định tĩnh của các phương pháp truyền thống.
*   **Local Dynamics:** Động lực học cục bộ (tính qua cửa sổ trượt tạo các hàm $REC(t), DET(t)...$) bộc lộ chuyển pha rõ hơn là một giá trị trung bình toàn cục.
*   **Takens' Theorem:** Phép nhúng trễ trên một chuỗi đơn biến là đủ để tái dựng toàn bộ động lực học của hệ thống.
*   **Geometric Recurrence:** Hình thái của RP (mật độ, cấu trúc đường chéo) là ảnh xạ trực tiếp của tính tất định và độ phức tạp hệ thống.
*   **Parameter Consistency:** Bắt buộc cố định các tham số ($d, \tau, r, l_{min}$) trên mọi cửa sổ để đảm bảo biến thiên đo được là do sinh lý, không phải do nhiễu thuật toán.

## 4.2 Limitations (Giới hạn)
*   **Multidimensionality:** Không có biến RQA nào độc lập mô tả được hệ thống; phải diễn giải đồng thời cả 5 biến.
*   **Parameter Sensitivity:** Kết quả lượng hóa cực kỳ nhạy cảm với việc lựa chọn $d, \tau, r, l_{min}$.
*   **Empirical Interpretation:** Chỉ số RQA không có diễn giải vật lý tuyệt đối (ví dụ: ENT thấp không hẳn là "đơn giản"), ý nghĩa phụ thuộc hoàn toàn vào bối cảnh hệ thống.
*   **Exploratory Metrics:** Tại thời điểm 1994, Trend và Entropy mới ở dạng sơ khởi, cần nghiên cứu sâu hơn.
*   **Complementary Tool:** RQA là công cụ bổ trợ cung cấp thêm góc nhìn, không sinh ra để thay thế các phương pháp phân tích chuỗi thời gian hiện có.
*   

# 5. My Research

## 5.1 Research Ideas
*   **Transition Dynamics (Thay vì Phân loại tĩnh):** Không chỉ gán nhãn trạng thái (ví dụ: Awake/Drowsy/Fatigue), mà dùng chuỗi $RQA(t)$ để định lượng chính **quá trình chuyển pha** (thời điểm bắt đầu, tốc độ, thời lượng và độ ổn định sau chuyển pha).
*   **Dynamics of Dynamics (Động lực học bậc cao):** Biến đặc trưng tĩnh thành hàm thời gian ($DET \to DET(t)$). Đối tượng nghiên cứu được nâng cấp thành *động lực học của các đặc trưng RQA*, nhằm khai thác các tập tính bậc cao: dao động, chu kỳ, sự thích nghi và phục hồi.

## 5.2 Knowledge Contribution
*   **Tiến hóa thay vì Trạng thái:** Giá trị cốt lõi là việc chuyển đổi đặc trưng tĩnh thành chuỗi thời gian liên tục. 
*   **Nguyên lý Phổ quát:** *"Hệ động lực không chỉ được đặc trưng bởi các pattern của nó, mà bởi cách các pattern đó tiến hóa theo thời gian."* Nguyên lý này có thể mở rộng áp dụng cho mọi hệ phi tuyến, vượt khỏi giới hạn của dữ liệu sinh lý.