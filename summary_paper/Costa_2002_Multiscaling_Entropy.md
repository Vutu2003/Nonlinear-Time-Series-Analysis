# Paper Metadata

*   **Title:** Multiscale Entropy Analysis of Complex Physiologic Time Series
*   **Authors:** Madalena Costa, Ary L. Goldberger, and C.-K. Peng
*   **Year:** 2002
*   **Keywords:** Multiscale entropy (MSE), physiologic time series, complexity, heart rate, sample entropy (SampEn)
*   
# 1. Why (Theo lăng kính Complexity của Costa et al., 2002)

### 1.1. Research Question (Câu hỏi nghiên cứu)
*   Làm thế nào để lượng hóa chính xác độ phức tạp nội tại (intrinsic complexity) của các chuỗi thời gian sinh lý học trên nhiều thang đo thời gian khác nhau, thay vì chỉ đơn thuần ước lượng mức độ bất định (unpredictability/randomness) của dữ liệu tại một thang đo duy nhất?

### 1.2. Biological Motivation (Động lực Sinh học)
*   **Trạng thái khỏe mạnh (Healthy dynamics):** Hệ thống sinh lý khỏe mạnh không tuần hoàn tuyệt đối cũng không ngẫu nhiên hoàn toàn, mà sở hữu khả năng điều hòa đa thang đo (multiscale regulation) và thích ứng cao, thể hiện qua mức độ phức tạp lớn.
*   **Lão hóa và Bệnh tật (Aging and Disease):** Các trạng thái này gây ra sự phá vỡ liên tục của các tương quan dài hạn và làm giảm khả năng thích nghi của cơ thể. Sự suy giảm này được định nghĩa là sự "mất đi độ phức tạp" (loss of complexity). Do đó, cần một thước đo định lượng được sự suy giảm này để phục vụ chẩn đoán.

### 1.3. Mathematical/Methodological Motivation (Động lực Toán học & Phương pháp)
*   **Nghịch lý của Entropy truyền thống:** Các thước đo entropy truyền thống định lượng mức độ ngẫu nhiên (randomness/disorder), trong đó entropy đạt cực đại ở các hệ thống hoàn toàn ngẫu nhiên.
*   **Randomness $\neq$ Complexity:** Một hệ thống bệnh lý (ví dụ: rung nhĩ) có thể tạo ra các dao động nhiễu loạn cao (giống nhiễu trắng), dẫn đến giá trị entropy cực cao. Tuy nhiên, sự hỗn loạn này không đại diện cho sự phức tạp mang tính cấu trúc và thích nghi của một hệ thống sinh lý khỏe mạnh (vốn có cấu trúc nhiễu $1/f$).
*   Sự thiếu hụt của phân tích đơn thang đo (single-scale paradox) chính là nguyên nhân dẫn đến việc đánh giá sai lệch bản chất động lực học, đòi hỏi sự ra đời của một khung phân tích đa thang đo (multiscale framework).

### 1.4. Previous Methods & Limitations (Các phương pháp trước đây và giới hạn)
*   **Kolmogorov-Sinai (KS) Entropy:** Được thiết kế về mặt lý thuyết cho các dữ liệu tiến tới vô hạn ($n \rightarrow \infty$) và không có nhiễu. Do đó, nó không khả dụng khi áp dụng vào các tín hiệu sinh lý thực tế vốn luôn có độ dài hữu hạn và chứa nhiễu.
*   **ApEn / SampEn (Single-scale):** Các thuật toán này không sai, nhưng việc chỉ đánh giá ở thang đo 1 (Scale = 1) là **không đủ** (insufficient). Do chỉ phản ánh sự bất định của điểm dữ liệu tiếp theo dựa trên lịch sử quá khứ gần nhất, chúng bỏ qua cấu trúc ở các thang đo dài hơn, dẫn đến việc không thể phân tách rõ ràng nhóm khỏe mạnh và nhóm bệnh lý ở thang đo nhỏ.
*   **Zhang's Multiscale Entropy:** Phương pháp này đã chú ý đến tính đa thang đo, nhưng do sử dụng entropy Shannon, nó đòi hỏi quá trình biểu tượng hóa (symbolization), yêu cầu lượng dữ liệu khổng lồ và gần như không có nhiễu. Điều kiện này hoàn toàn không phù hợp với các tín hiệu sinh lý học liên tục và ngắn.
*   
# 2. What (Bản chất và Cơ sở Toán học của MSE)

### 2.1. Core Insight (Nhận thức cốt lõi)
*   **Nguồn gốc đa thang đo của độ phức tạp sinh lý:** Sự phức tạp (complexity) không tự sinh ra từ một cấu trúc đơn lẻ. Nó là kết quả của sự tương tác và phối hợp liên tục giữa nhiều cơ chế điều hòa (multiple regulatory mechanisms) hoạt động trên các thang đo thời gian khác nhau (ví dụ: nhịp tim $\rightarrow$ nhịp thở $\rightarrow$ phản xạ áp thụ quan $\rightarrow$ hệ thần kinh tự chủ $\rightarrow$ nội tiết tố $\rightarrow$ nhịp sinh học).
*   **Định vị lại vai trò của Entropy đơn thang đo:** Các thuật toán entropy truyền thống không "sai" hay bị đánh lừa; chúng đo lường cực kỳ chính xác đại lượng mà chúng được thiết kế để đo (sự bất định/randomness). Tuy nhiên, đại lượng đó không đồng nhất với độ phức tạp. 
*   **Sự ổn định đa tỷ lệ của hệ thống khỏe mạnh:** Hệ sinh lý khỏe mạnh không có mức entropy "phẳng" tuyệt đối, mà duy trì mức entropy tương đối cao và giảm rất chậm qua nhiều thang đo. Điều này minh chứng cho sự tồn tại của các tương quan dài hạn (long-range correlations) và khả năng thích nghi bền bỉ.
*   **Sự hội tụ của Bệnh lý ở "Mất độ phức tạp" (Loss of Complexity):** Cả hai trạng thái bệnh lý cực đoan—dù là quá trật tự (suy tim - CHF) hay quá ngẫu nhiên (rung nhĩ - AF)—cuối cùng đều dẫn đến sự suy giảm độ phức tạp. Độ phức tạp không nằm ở sự trật tự (Order) hay sự hỗn loạn (Disorder), mà nằm ở "sự biến thiên có cấu trúc" (Structured Variability).

### 2.2. Mathematical Foundation (Cơ sở Toán học)
Phương pháp Multiscale Entropy (MSE) lượng hóa độ phức tạp thông qua hai bước vận hành toán học cốt lõi:

*   **Bước 1: Phép biến đổi khử nhiễu thô đa tỷ lệ (Coarse-Graining procedure)**
*   Từ chuỗi thời gian gốc gồm $N$ phần tử $\{x_1, \dots, x_N\}$, thuật toán xây dựng các chuỗi làm thô $\{y^{(\tau)}\}$ dựa theo hệ số thang đo $\tau$.
*   Giá trị mỗi phần tử trong chuỗi mới là trung bình cộng của các điểm dữ liệu gốc trong một cửa sổ không chồng lấp có độ dài bằng $\tau$:
$$y^{(\tau)}_j = \frac{1}{\tau} \sum_{i=(j-1)\tau+1}^{j\tau} x_i \quad \text{với } 1 \le j \le \frac{N}{\tau}$$

*   **Bước 2: Xây dựng đường cong MSE (MSE Curve)**
*   Đầu ra của phân tích MSE không phải là một giá trị vô hướng (scalar) đơn lẻ, mà là một hàm số biểu diễn SampEn theo hệ số tỷ lệ $\tau$ (từ $\tau=1$ đến $\tau=max$).
*   **Thiết lập tham số quyết định (Cố định $r$):** Costa thiết lập dung sai $r = 0.15 \times \text{SD}$ (với SD là độ lệch chuẩn của nguyên bản chuỗi dữ liệu gốc). Nếu tính lại SD cho từng thang đo, phép biến đổi sẽ làm thay đổi cả tín hiệu lẫn ngưỡng (threshold). Việc cố định $r$ loại bỏ hoàn toàn biến nhiễu này, đảm bảo mọi biến thiên của entropy đều xuất phát thuần túy từ sự thay đổi của thang đo thời gian.

*   **Bước 3: Cơ chế giải thích bằng mô hình toán học (Nhiễu)**
*   **Nhiễu $1/f$ (Fractality):** Nhờ đặc tính fractal và cấu trúc tự đồng dạng đa tỷ lệ, các đặc trưng thống kê của tín hiệu gần như bất biến qua các phép biến đổi thang đo (Scale $\rightarrow$ Signal statistics $\rightarrow$ Almost invariant). Do đó, quỹ đạo SampEn duy trì ổn định.
*   **Nhiễu trắng (White noise):** Do hoàn toàn thiếu vắng các tương quan dài hạn, phép biến đổi làm thô (trung bình hóa) khiến phương sai Gauss thu hẹp nhanh chóng. Nói cách khác, coarse-graining đã "giết chết" tính ngẫu nhiên, khiến quỹ đạo SampEn của nhiễu trắng tụt dốc mạnh theo $\tau$.

### 2.3. Operational Definition of Complexity (Định nghĩa vận hành của Độ phức tạp)
Thông qua MSE, Costa đã thay đổi hoàn toàn hệ quy chiếu về độ phức tạp: Complexity không phải là một giá trị entropy vô hướng tại một thang đo, mà là cách entropy tiến hóa (entropy trajectories) dọc theo trục tỷ lệ.

*   **Hệ thống ngẫu nhiên / Bệnh lý cực đoan:** Bắt đầu với mức entropy cực cao ở Scale 1, suy giảm rõ rệt ở Scale 2, rơi tự do ở Scale 5 và tiến gần về 0 ở Scale 20.
*   **Hệ thống khỏe mạnh:** Dù khởi điểm ở Scale 1 có thể thấp hơn tín hiệu nhiễu, quỹ đạo này vẫn duy trì ổn định ở mức cao khi đi qua Scale 5, Scale 10 và Scale 20.
*   **Tổng kết:** Cốt lõi của phương pháp Costa không nằm ở việc so sánh hai giá trị tĩnh, mà ở việc đối chiếu hai quỹ đạo tiến hóa. Khả năng duy trì thông tin qua các lăng kính thời gian khác nhau chính là thước đo định lượng tối thượng cho khái niệm "Độ phức tạp".
*   

# 3. How (Phương pháp và Triển khai thuật toán MSE)

### 3.1. Algorithm (Thuật toán chi tiết)
Thuật toán Multiscale Entropy (MSE) biến đổi tín hiệu qua hai giai đoạn cốt lõi để tạo ra một "hồ sơ động lực học" thay vì một giá trị vô hướng.

*   **Giai đoạn 1: Khử nhiễu thô đa tỷ lệ (Coarse-Graining)**
*   Từ chuỗi gốc $\{x_1, \dots, x_N\}$, xây dựng chuỗi mới $\{y^{(\tau)}\}$ theo hệ số tỷ lệ $\tau$:
$$y^{(\tau)}_j = \frac{1}{\tau} \sum_{i=(j-1)\tau+1}^{j\tau} x_i \quad \text{với } 1 \le j \le \left\lfloor \frac{N}{\tau} \right\rfloor$$
*   **Lưu ý cốt lõi:** Coarse-graining KHÔNG phải là bộ lọc trung bình trượt (moving average filter). Nó là phép tái lấy mẫu (resampling) bằng các cửa sổ **không chồng lấp** nhằm tạo ra một hệ quan sát hoàn toàn mới ở thang thời gian $\tau$.

*   **Giai đoạn 2: Trích xuất hồ sơ Entropy (Entropy Profile)**
*   MSE không tạo ra một loại entropy mới. Đầu ra của MSE là một tập hợp các cặp giá trị (Profile/Curve) ánh xạ từ thang đo sang giá trị SampEn tương ứng: $\tau \rightarrow \text{SampEn}$.
*   Cố định $m=2$ và dung sai $r = 0.15 \times \text{SD}$ (với SD là độ lệch chuẩn nguyên bản của chuỗi gốc).

---

### 3.2. End-to-End Pipeline
**Tín hiệu thô** $\rightarrow$ **Tiền xử lý (loại bỏ nhiễu/outlier)** $\rightarrow$ **Coarse-Graining (chia Scale)** $\rightarrow$ **SampEn (Cố định $r$)** $\rightarrow$ **Đồ thị MSE (Dynamic Signature)**

---

### 3.3. Implementation Notes (Lưu ý kỹ thuật then chốt)

*   **Bẫy triệt tiêu ngưỡng (The Standard Deviation Trap):** Tuyệt đối cố định $r$ theo chuỗi gốc. Lấy ví dụ với nhiễu trắng, khi tăng thang đo (làm mượt), phương sai sẽ giảm mạnh. Nếu liên tục tính lại $r = 0.15 \times \text{SD}_{new}$ cho mỗi chuỗi mới, ngưỡng $r$ cũng sẽ co nhỏ theo. Hai hiệu ứng (tín hiệu mượt hơn + ngưỡng khắt khe hơn) sẽ triệt tiêu lẫn nhau, làm hỏng hoàn toàn mục tiêu đánh giá cấu trúc của tín hiệu.
*   **Giới hạn độ dài dữ liệu:** Costa (2002) dùng chuỗi gốc rất dài ($N=30.000$) để đảm bảo số lượng mẫu ở scale $\tau=20$ vẫn đủ lớn cho SampEn hoạt động ổn định. Với dữ liệu thực tế ngắn hơn, các nghiên cứu sau này rút ra kinh nghiệm thực hành: phải đảm bảo $N/\tau_{max} \ge 100 \sim 200$ điểm.
*   **Triết lý giải mã (Decoding Philosophy):** Độ phức tạp (Complexity) được mã hóa trong toàn bộ hình thái của đường cong, không nằm ở bất kỳ điểm đơn lẻ nào. Dù nhiễu trắng có entropy ở Scale 1 cao hơn tín hiệu khỏe mạnh, sự sụt giảm nhanh chóng của quỹ đạo nhiễu trắng mới là minh chứng cho sự thiếu hụt độ phức tạp.

---

### 3.4. Computational & System Design (Tối ưu hóa tính toán)

*   **Độ phức tạp hội tụ (Computational Complexity):** SampEn có độ phức tạp $O(N^2)$. Tuy nhiên, chi phí tính toán cho MSE không phải là $20 \times O(N^2)$. Khi $\tau$ tăng, độ dài chuỗi giảm còn $N/\tau$. Do đó, tổng thời gian tính toán tỷ lệ với:
$$\sum_{\tau=1}^{\tau_{max}} O\left(\frac{N^2}{\tau^2}\right)$$
*   Vì chuỗi $\sum \frac{1}{\tau^2}$ hội tụ, tổng chi phí tính toán thực tế của toàn bộ quy trình MSE lớn hơn SampEn đơn thang đo không quá nhiều.
*   **Chiến lược tối ưu hóa (Optimizations):** Tùy thuộc vào phần cứng và kích thước dữ liệu, lập trình viên không nên dùng vòng lặp thuần. Các lựa chọn thay thế mạnh mẽ bao gồm: NumPy Vectorization (Broadcasting), Numba JIT, KD-Tree/Ball-tree, hoặc tăng tốc tính toán song song bằng GPU.
*   
# 4. Validation (Kiểm chứng Thống kê và Thực nghiệm)

### 4.1. Assumptions (Các giả định nền tảng)
MSE tựa trên hai tầng giả định tách biệt: một thuộc về lý thuyết sinh học, một thuộc về kỹ thuật thuật toán.

**Giả định Sinh học (Biological Assumptions)**
*   **Thuyết độ phức tạp sinh lý (Physiological Complexity Theory):** Các hệ thống sinh học khỏe mạnh sở hữu động lực học thích ứng đa thang đo (multiscale adaptive dynamics). Sự phức tạp này không đồng nhất với tính ngẫu nhiên hay sự trật tự, mà là sự phối hợp của nhiều cơ chế điều hòa. Lão hóa và bệnh lý phá vỡ cấu trúc này, dẫn đến "mất độ phức tạp".

**Giả định Thuật toán (Algorithmic Assumptions)**
*   **Cố định thước đo (Fixed $r$):** Dung sai $r$ phải được giữ nguyên bằng $0.15 \times \text{SD}$ của chuỗi gốc trên mọi thang đo. Nếu thay đổi $r$ ở mỗi scale, ta đang đồng thời thay đổi cả "đối tượng quan sát" (chuỗi đã làm thô) lẫn "thước đo" (ngưỡng tương đồng).
*   **Kích thước mẫu đủ lớn (Sufficient Sample Size):** Costa không nhấn mạnh vào tính dừng (stationarity) mà đặt nặng việc độ dài dữ liệu phải đủ lớn để SampEn hoạt động ổn định sau khi bị chia nhỏ qua phép coarse-graining.

### 4.2. Experiments (Thực nghiệm và Cơ chế Vật lý)
*   **Thực nghiệm 1: Nhiễu trắng vs. Nhiễu $1/f$ (Mô hình Toán học)**
Tại thang đo nhỏ, nhiễu trắng có entropy cao nhất. Tuy nhiên ở thang đo lớn, entropy sụt giảm về 0 vì phép làm thô (coarse-graining) đã trung bình hóa và triệt tiêu hoàn toàn tính ngẫu nhiên vô hướng. Ngược lại, nhiễu $1/f$ giữ nguyên mức entropy do duy trì được tương quan dài hạn (long-range correlations) và cấu trúc fractal.
*   **Thực nghiệm 2: Bệnh lý Tim mạch (AF vs. CHF vs. Khỏe mạnh)**
Bệnh nhân Rung nhĩ (AF) quá ngẫu nhiên: entropy cực cao ở quy mô nhỏ, nhưng sụt giảm mạnh ở quy mô lớn vì cấu trúc đã bị phá vỡ, không còn thông tin để đo. Ngược lại, người khỏe mạnh duy trì cấu trúc đa thang đo, giúp đường MSE ổn định. Điều này khẳng định triết lý: "Độ phức tạp là sự duy trì cấu trúc qua nhiều thang đo".
*   **Thực nghiệm 3: Đánh giá Lão hóa**
Lão hóa không làm giảm entropy ở mọi thang đo, mà làm giảm **độ phức tạp đa thang đo** (multiscale complexity profile). Sự phân tách giữa người trẻ và người già thể hiện rõ nhất ở các thang đo lớn, chứng minh công cụ đơn thang đo sẽ bỏ sót sự suy giảm sinh lý này.
*   **Thực nghiệm 4: Dữ liệu thay thế (Surrogate Data)**
Việc xáo trộn ngẫu nhiên chuỗi nhịp tim giữ nguyên phân phối biên độ (histogram) nhưng phá hủy tương quan pha (phase correlations). Khi đó, quỹ đạo MSE sụp đổ giống hệt nhiễu trắng. Điều này chứng minh MSE thực chất đang đo lường "tương quan dài hạn", không phải đo phân phối thống kê.

### 4.3. Limitations (Giới hạn của phương pháp)
*   **Sự bào mòn dữ liệu (Data Length Shrinkage):** Khác với các thuật toán khác, MSE có hai nguồn gây thất thoát thông tin: phép coarse-graining làm giảm số lượng phần tử $N$, dẫn đến thuật toán SampEn cạn kiệt các cặp vector khớp nhau ($A, B \rightarrow 0$), gây sai số lớn ở các thang đo cao.
*   **Hiệu ứng dây chuyền của nhiễu ngoại lai (Outlier Chain Reaction):** Đỉnh nhiễu đột ngột $\rightarrow$ SD tăng vọt $\rightarrow$ ngưỡng $r$ bị phình to $\rightarrow$ hầu hết các vector đều được xem là "khớp nhau" $\rightarrow$ Entropy bị đánh tụt xuống một cách giả tạo. Tiền xử lý tín hiệu thô là bắt buộc.
*   **Ngụy biện đơn điểm (Single-point Fallacy):** Tại một thang đo lớn, bệnh nhân CHF và AF có thể cho ra cùng một giá trị entropy. MSE là một đường cong (curve), không phải một điểm. Việc đánh giá độ phức tạp dựa trên một giá trị entropy đơn lẻ là vô nghĩa.
*   **Tính bất thuận nghịch (Irreversibility):** Phép làm thô bằng trung bình hóa làm mất vĩnh viễn thông tin cục bộ (đánh đổi độ phân giải lấy thang đo). Giới hạn này chính là động lực ra đời của các biến thể tối ưu hơn sau này như Composite MSE (CMSE) hay Refined Composite MSE (RCMSE).

### 4.4. Key Takeaways
*   Complexity không thể đánh giá bằng một điểm ở một thang đo đơn lẻ.
*   Hệ thống khỏe mạnh luôn sở hữu cấu trúc thích ứng đa thang đo (multiscale structure).
*   Nhiễu trắng ngẫu nhiên chỉ thể hiện sự "phức tạp giả tạo" ở thang đo nhỏ.
*   Đường cong (MSE profile) mới là đối tượng phân tích tối thượng, không phải các con số rời rạc.
*   MSE thực chất đo lường khả năng duy trì tốc độ tạo thông tin (information generation rate) khi độ phân giải thời gian thay đổi.
*   

# 5. My Research (Định hướng Nghiên cứu & Đóng góp Khoa học)

Thay vì coi NTSA là đích đến, nghiên cứu này sử dụng MSE như một lăng kính để giải mã sự thay đổi động lực học của hệ tuần hoàn. Lộ trình được chia thành 2 giai đoạn rõ rệt để tránh loãng mục tiêu (scope creep).

### 5.1. Phase 1 / Paper 1: Khám phá Cơ chế Sinh lý học (Physiology Focus)
**Mục tiêu:** Phân tích sự biến đổi độ phức tạp của tín hiệu PPG trong quá trình chuyển hế ý thức, không sử dụng Machine Learning.

*   **Đánh giá Macro-dynamics (Chuỗi PRV):** Phân tích sự suy giảm năng lực điều hòa đa thang đo (multiscale regulation) của hệ thần kinh tự chủ. Khi buồn ngủ, sự rút lui của thần kinh giao cảm dự kiến sẽ làm sụp đổ cấu trúc liên kết dài hạn của chuỗi PRV, kéo theo sự sụt giảm của quỹ đạo MSE ở các thang đo trung bình và lớn.
*   **Đánh giá Micro-dynamics (Raw PPG Waveform):** Khắc phục định kiến về tính tuần hoàn (periodicity). Mặc dù chu kỳ tim có tính tuần hoàn mạnh, sự biến điệu mạch máu ngoại vi (peripheral vascular modulation) do giãn mạch khi buồn ngủ sẽ làm thay đổi hình thái và biên độ sóng qua nhiều thang đo thời gian. MSE đo lường chính sự thay đổi cấu trúc vi mô này.
*   **Đóng góp 1 - Tính mới (Transient Complexity Loss):** Các nghiên cứu kinh điển của Costa tập trung vào bệnh lý mãn tính (suy tim, lão hóa). Nghiên cứu này mở rộng thuyết độ phức tạp sinh lý vào một trạng thái sinh lý mang tính thuận nghịch tạm thời (reversible physiological state) là cơn buồn ngủ.
*   **Đóng góp 2 - Cơ chế điều hòa (Which scales are affected?):** Trả lời câu hỏi trọng tâm: Sự buồn ngủ làm đứt gãy động lực học ở thang đo thời gian nào? (Ví dụ: Scale 1-3 không đổi, nhưng Scale 4-8 sụt giảm mạnh). Điều này chỉ ra chính xác điểm mù trong hệ thống phản hồi sinh lý.
*   **Đóng góp 3 - Phương pháp học (Noise Suppression):** Bác bỏ ngụy biện dùng MSE lọc "motion artifacts" (vì nhiễu chuyển động thường là dải tần thấp, biên độ cao). Thay vào đó, chứng minh phép coarse-graining giúp triệt tiêu các thăng giáng ngẫu nhiên vi mô (fine-scale random fluctuations), cho phép các động lực học đa thang đo bền vững (persistent multiscale dynamics) lộ diện rõ nét.

### 5.2. Phase 2 / Paper 2: Ứng dụng & Triển khai Kỹ thuật (Application Focus)
**Mục tiêu:** Trích xuất đặc trưng từ MSE Profile để xây dựng bộ phân loại liên tục (Continuous Online Detection).

*   **Đặc trưng Hình học (MSE Profile as ML Features):** Từ bỏ việc coi MSE là một "con số" tại một thang đo rời rạc. Trích xuất trực tiếp các đặc trưng từ toàn bộ đường cong (Curve) như: Diện tích dưới đường cong (AUC) cho động lực học nhanh và Độ dốc (Slope) cho động lực học dài hạn, làm đầu vào cho Classifier.
*   **Tối ưu hóa Phần cứng (Optimal Scale Factor):** Xác định các thang đo mang tính quyết định (nơi khoảng cách giữa trạng thái Tỉnh và Ngủ là lớn nhất). Việc chỉ tính toán SampEn tại 1-2 thang đo tối ưu này sẽ giảm thiểu khối lượng tính toán, tạo tiền đề đưa thuật toán vào các thiết bị Wearables cảnh báo thời gian thực.