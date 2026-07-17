# Thuật toán DFA (Detrended Fluctuation Analysis)

DFA không trực tiếp đo lường bản thân tín hiệu. Thay vào đó, DFA đo lường **sự thay đổi của năng lượng dao động nội tại khi ta thay đổi lăng kính (thang thời gian) quan sát**. Thuật toán được vận hành qua 5 bước triết học sau:

#### Bước 1: Tạo Profile (Khuếch đại cấu trúc)
*   **Toán học:** $Y(k) = \sum_{i=1}^{k}(x_i - \bar{x})$
*   **Ý nghĩa Vật lý:** Chuyển đổi chuỗi thời gian ban đầu thành một quá trình tích lũy (random walk). Bước này mượn nguyên bản tư tưởng của Hurst: dùng phép tích phân để "bơm phồng" và làm lộ diện các cấu trúc tương quan dài hạn (long-range dependence) vốn bị ẩn giấu rất sâu trong các dao động nhỏ lẻ của chuỗi gốc.

#### Bước 2: Quan sát Đa thang đo (Windowing)
*   **Toán học:** Chia Profile $Y(k)$ thành các cửa sổ không chồng lấn có kích thước $n$.
*   **Ý nghĩa Vật lý:** Thừa nhận bản chất phi dừng (non-stationary) của hệ sinh lý. Hệ thống không dao động quanh một "điểm neo" duy nhất (global mean) từ đầu đến cuối. Khi chia nhỏ thành các khoảng thời gian $n$, chúng ta đang đi tìm các trạng thái **"cân bằng cục bộ" (local equilibrium)** của hệ thống tại từng thời điểm.

#### Bước 3: Triệt tiêu Cân bằng cục bộ (Local Detrending)
*   **Toán học:** Xác định thành phần xu hướng $Y_n(k)$ và trích xuất phần dư $\Delta Y(k) = Y(k) - Y_n(k)$.
*   **Ý nghĩa Vật lý:** Ước lượng và gọt bỏ **thành phần biến thiên chậm (slow-varying component)**. Đa thức bậc $m$ ở đây chỉ đơn thuần là một công cụ toán học để "bắt" lấy cái xu hướng ngoại sinh hoặc độ trôi nền. Sau khi triệt tiêu sự dịch chuyển vĩ mô này, thứ còn sót lại trên tay chúng ta chính là những vi dao động hoàn toàn tinh khiết.

#### Bước 4: Trích xuất Năng lượng dao động nội tại (Fluctuation)
*   **Toán học:** Tính RMS của phần dư: 
    $$F(n) = \sqrt{\frac{1}{N}\sum (\Delta Y)^2}$$
*   **Ý nghĩa Vật lý:** Đây là điểm chia tay triết học với Hurst!
    *   **Hurst hỏi:** *Profile vươn đi xa đến mức nào? (Range)*
    *   **Peng hỏi:** *Sau khi trừ bỏ xu hướng chậm, Profile còn giữ lại bao nhiêu năng lượng dao động nhanh? (Residual energy)*
    Đại lượng $F(n)$ không phải là phương sai thống kê thông thường, mà chính là **biên độ trung bình của phần dao động không thể giải thích được bởi xu hướng cục bộ**. 

#### Bước 5: Khám phá Quy luật Scaling và Trạng thái Sinh lý
*   **Toán học:** Đánh giá mối quan hệ $F(n) \propto n^\alpha$ qua nhiều thang thời gian $n$. Sự phụ thuộc tuyến tính trên đồ thị $\log F(n)$ theo $\log n$ sẽ xác định số mũ $\alpha$ (hệ số góc của đường thẳng).
*   **Ý nghĩa Vật lý (Cảnh quan "Độ gồ ghề"):** Số mũ $\alpha$ mô tả cách các dao động nội tại phát triển và giãn nở, đồng thời đóng vai trò như một chỉ báo về độ gồ ghề (roughness) của chuỗi thời gian (giá trị $\alpha$ càng lớn, tín hiệu càng mượt).
    *   $0 < \alpha < 0.5$: **Tương quan nghịch (Anti-persistence).** Các giá trị lớn và nhỏ có xu hướng luân phiên nhau liên tục để tự triệt tiêu. Một giá trị lớn thường bị theo ngay sau bởi một giá trị nhỏ để kéo hệ thống giật ngược lại (cảnh quan cực kỳ gồ ghề).
    *   $\alpha = 0.5$: **Nhiễu trắng (White noise).** Quá trình hoàn toàn ngẫu nhiên, không có bộ nhớ (hành xử như một bước đi ngẫu nhiên - random walk).
    *   $0.5 < \alpha < 1.0$: **Tương quan dài hạn kiên định (Persistent power-law).** Các dao động ở các thang đo khác nhau có sự liên kết chặt chẽ. Giá trị quá khứ có sức ảnh hưởng mạnh mẽ tới tương lai (khoảng thời gian lớn dễ được nối tiếp bởi khoảng thời gian lớn).
    *   $\alpha = 1.0$: **Nhiễu $1/f$ (Trạng thái khỏe mạnh lý tưởng).** Sự "thỏa hiệp" hoàn hảo giữa tính khó lường của nhiễu trắng và sự trơn tru của nhiễu Brown. Dữ liệu nhịp tim từ người khỏe mạnh thường hội tụ sát mốc này.
    *   $\alpha > 1.0$: **Tương quan phi lũy thừa.** Hệ thống vẫn có tương quan nhưng ngừng tuân theo định luật tỷ lệ lũy thừa chuẩn.
    *   $\alpha = 1.5$: **Nhiễu Brown (Brownian noise).** Tín hiệu cực kỳ mượt mà (kết quả của tích phân nhiễu trắng). Trong y sinh, khi $\alpha$ tiến xa khỏi $1.0$ và tiệm cận về mức này, nó phản ánh một trạng thái bệnh lý nghiêm trọng, nơi hệ thống mất đi tính phức tạp thích nghi và trở nên mượt mà một cách giả tạo.

---

**Triết lý cốt lõi:**
Peng không hề thay đổi tư duy vĩ đại về "Scaling" của Hurst. Đóng góp lịch sử của Peng là định nghĩa lại từ **"Fluctuation" (Sự thăng giáng)**. Thay vì đo biên độ tuyệt đối, Peng đo năng lượng của phần dư. Chính sự tinh chỉnh sắc sảo này đã giúp DFA gạn đục khơi trong, tách rời hoàn hảo bộ nhớ nội tại của hệ thống khỏi những xu hướng ngoại sinh phi dừng.

# BÁO CÁO TỔNG HỢP: BẢN CHẤT ĐỘNG LỰC HỌC VÀ CÁC GIỚI HẠN CỦA THUẬT TOÁN DFA

Thuật toán Detrended Fluctuation Analysis (DFA) được xây dựng dựa trên 3 giả định toán học cốt lõi. Sự thành công hay thất bại của DFA khi áp dụng vào thực tế phụ thuộc hoàn toàn vào việc hệ thống sinh lý có vi phạm các giả định này (đặc biệt là giả định số 3) hay không.

## I. 3 GIẢ ĐỊNH CỐT LÕI CỦA DFA

1. **Sự tồn tại của Profile (Động lực học khuếch đại)**
   * **Toán học:** $Y(k) = \sum_{i=1}^{k}(x_i - \bar{x})$
   * **Bản chất:** Tín hiệu gốc có thể được chuyển đổi thành một quá trình tích lũy (random walk) để bơm phồng và làm bộc lộ các cấu trúc tương quan dài hạn ẩn sâu bên trong các dao động nhỏ lẻ.

2. **Trend chỉ tồn tại cục bộ (Local Trend)**
   * **Toán học:** Xu hướng biến thiên chậm $Y_n(k)$ trong từng cửa sổ nhỏ có thể được xấp xỉ chính xác bằng một đa thức bậc thấp (bậc 1, 2, 3...) và có thể loại bỏ bằng phép trừ $\Delta Y = Y - Y_n$.
   * **Bản chất:** Hệ thống không dao động quanh một điểm neo tĩnh (global mean) mà liên tục thiết lập các trạng thái cân bằng địa phương.

3. **Tính bất biến theo thang đo (Scale-invariance)**
   * **Toán học:** Năng lượng dao động nội tại (RMS của phần dư) phải thỏa mãn quy luật lũy thừa: $F(n) \propto n^\alpha$.
   * **Bản chất:** Hệ thống được chi phối bởi một cơ chế động lực thống nhất trên mọi lăng kính quan sát. Hệ thống không có một "thang đo đặc trưng" (characteristic scale) nào. 

---

## II. SỰ SỤP ĐỔ CỦA GIẢ ĐỊNH SỐ 3 VÀ CÁC KỊCH BẢN

Giả định số 3 là "linh hồn" của DFA. Khi đồ thị $\log F(n)$ bị gãy khúc (crossover) hoặc cong vênh, hệ số $\alpha$ duy nhất mất đi ý nghĩa. Sự sụp đổ này xuất phát từ 7 kịch bản, được chia thành 3 nhóm nguyên nhân chính:

### Nhóm 1: Sự sụp đổ do Bản chất Động lực học (Đa cơ chế)
*Hệ thống không đơn thuần, mà chứa nhiều cơ chế vật lý chồng chéo.*
* **(1) Crossover (Gãy khúc):** Hệ thống có hai cơ chế động lực chi phối ở hai dải thời gian khác nhau (VD: vi mô do hô hấp, vĩ mô do thần kinh tự chủ), tạo ra $\alpha_1$ và $\alpha_2$ riêng biệt.
* **(2) Đa thang đo (Multiple characteristic scales):** Tín hiệu chứa quá nhiều chu kỳ sinh lý chồng lấp (nhịp tim 1Hz, hô hấp 0.25Hz, vận mạch 0.05Hz), khiến $\alpha$ thay đổi liên tục.
* **(3) Đa phân dạng (Multifractal):** Hệ thống không có một scaling duy nhất mà có nhiều scaling cùng tồn tại, đòi hỏi phải dùng MFDFA.
* **(4) Chuyển pha (Phase transition):** Hệ thống trải qua sự thay đổi trạng thái đột ngột (VD: từ thức sang ngủ), làm một $\alpha$ trung bình trên toàn dải trở nên vô nghĩa.

### Nhóm 2: Sự sụp đổ do Nhiễu Tất định (Tính chu kỳ)
*Kẻ thù tự nhiên của phép đo Fractal.*
* **(5) Chu kỳ mạnh (Strong periodicity):** Các sóng tuần hoàn (như nhịp tim cơ học) tạo ra một "thang đo đặc trưng" cứng nhắc $T$. Khi cửa sổ $n$ tiệm cận $T$, quy luật power-law bị phá vỡ, $F(n)$ dao động bão hòa hoặc lượn sóng.

### Nhóm 3: Sự sụp đổ do Giới hạn Kỹ thuật (Công cụ không phù hợp)
*Lỗi từ phía thiết lập thuật toán, không phải do hệ thống.*
* **(6) Tín hiệu quá ngắn:** Nếu $N$ quá nhỏ, số lượng cửa sổ ở dải $n$ lớn sẽ không đủ để tính trung bình thống kê, khiến $F(n)$ dao động nhiễu loạn ở đuôi đồ thị.
* **(7) Trend quá mạnh không khử nổi:** Nếu hệ thống có đường nền cong phức tạp (hàm mũ, bậc 3) nhưng chỉ dùng DFA-1 (khớp đường thẳng), phần dư sẽ bị lỗi. $F(n)$ tăng vọt giả tạo, kéo theo $\alpha$ bị sai lệch.

---

## III. KẾT LUẬN
Sự sụp đổ của đồ thị $\log F(n)$ trong DFA không phải là lỗi thuật toán, mà là **lời khai sinh học** của hệ thống. Chính việc phân tích các điểm gãy (crossover) và sự sai lệch quy luật Scaling sẽ cung cấp manh mối vật lý cực kỳ quý giá về cấu trúc bệnh lý hoặc các cơ chế điều hòa đang ẩn giấu bên trong chuỗi thời gian y sinh.

# BÁO CÁO TỔNG HỢP: NHỮNG HẠN CHẾ CỐT LÕI CỦA THUẬT TOÁN DFA (PENG 1994)

Mặc dù Detrended Fluctuation Analysis (DFA) là một bước tiến lịch sử trong việc đo lường tương quan dài hạn của các hệ thống phi dừng, phiên bản nguyên thủy của Peng (1994) vẫn tồn tại 5 giới hạn nền tảng về mặt toán học và vật lý. Việc nhận thức rõ các giới hạn này là cơ sở để ứng dụng đúng và phát triển các phiên bản DFA bậc cao hoặc đa phân dạng sau này.

## I. TÓM TẮT 5 HẠN CHẾ CỐT LÕI

| Hạn chế | Bản chất |
| :--- | :--- |
| **1. Scale nhỏ** | Quá trình Detrending gây ra sai số (deviation), dẫn đến overfit cục bộ. |
| **2. Chuỗi hữu hạn** | Hiệu ứng Finite-size làm nhiễu đại lượng $F(n)$ ở các thang đo lớn. |
| **3. DFA-1** | Chỉ khử được trend tuyến tính, các trend bậc cao còn sót lại sẽ làm sai lệch kết quả (cần DFA-$m$). |
| **4. Một $\alpha$ duy nhất** | Không mô tả được bản chất khi hệ thống có hiện tượng gãy khúc (crossover) hoặc có nhiều miền scaling. |
| **5. Chỉ mô tả tương quan** | Không thể suy luận ngược ra cơ chế sinh dữ liệu; chỉ đo dao động bậc 2 (không đủ cho hệ đa phân dạng). |

---

# II. PHÂN TÍCH CHI TIẾT CÁC HẠN CHẾ

### 1. Sai số hệ thống ở cửa sổ nhỏ (Small-scale Deviation)
Ở các thang đo quá nhỏ (ví dụ $n < 4$ hoặc $n < 8$), số lượng điểm dữ liệu trong một cửa sổ là quá ít. Quá trình khớp đa thức (polyfit) sẽ bám quá sát vào dữ liệu (overfitting), khiến phần dư (residual) trở nên nhỏ bất thường. Điều này làm cho đồ thị $\log F(n)$ bị méo mó ở đoạn đầu, dẫn đến việc ước lượng số mũ $\alpha$ bị sai lệch. Đây là một giới hạn toán học nội tại của phép hồi quy.

### 2. Hiệu ứng kích thước hữu hạn (Finite-Size Effect)
Đây là giới hạn thống kê chung của các thuật toán phân tích chuỗi thời gian. Khi kích thước cửa sổ $n$ tiến gần đến tổng chiều dài chuỗi $N$ (ví dụ: $N = 5000, n = 1000$), số lượng cửa sổ còn lại để lấy trung bình RMS là rất ít (chỉ còn 5 cửa sổ). Theo luật số lớn, phương sai lúc này sẽ rất cao, làm cho $F(n)$ dao động mạnh và nhiễu loạn ở dải vĩ mô, làm mất đi tính tuyến tính của đồ thị log-log.

### 3. Giới hạn của bộ lọc tuyến tính (Linear Detrending)
Phiên bản DFA nguyên thủy (Peng 1994) sử dụng hồi quy tuyến tính trong mỗi cửa sổ (DFA-1). Phương pháp này chỉ loại bỏ được các xu hướng là đường thẳng. Nếu hệ thống chứa các độ trôi nền phức tạp hơn (bậc hai, bậc ba, hàm mũ), bộ lọc tuyến tính sẽ để sót lại các thành phần xu hướng này trong phần dư. Kết quả là $F(n)$ bị khuếch đại giả tạo. Đây chính là động lực để thuật toán phát triển thành các phiên bản DFA bậc cao (DFA-2, DFA-3,...).

### 4. Giả định quy luật Scaling đơn (Single Scaling Exponent)
Bản thân hiện tượng gãy khúc (crossover) là một **ưu điểm** của DFA khi nó giúp phát hiện sự chuyển giao giữa các cơ chế sinh lý khác nhau (ví dụ: từ hô hấp sang thần kinh tự chủ). Tuy nhiên, **hạn chế của DFA nằm ở chỗ nó giả định tồn tại một quy luật scaling đơn nhất**. Khi hệ thống có crossover hoặc chứa nhiều miền scaling độc lập, việc dùng một số mũ $\alpha$ duy nhất (bằng cách fit một đường thẳng duy nhất qua toàn bộ phổ) để mô tả toàn bộ hệ thống là một sự cưỡng ép toán học và làm mất đi ý nghĩa vật lý thực sự.

### 5. Thiếu cơ sở Cơ chế (Mechanistic) và Giới hạn Đơn phân dạng (Monofractal)
*   **Mô tả thay vì Cơ chế:** DFA chỉ đóng vai trò mô tả (descriptive) việc tồn tại tương quan dài hạn (ví dụ $\alpha \approx 1$), nhưng không thể phân biệt được nguồn gốc vật lý sinh ra nó. Kết quả $\alpha \approx 1$ có thể xuất phát từ quá trình tự hồi quy (autoregressive), fractional Brownian motion, động lực học hỗn loạn (chaos), hay các vòng lặp phản hồi sinh lý (nonlinear feedback).
*   **Giới hạn Đơn phân dạng:** DFA đo lường độ thăng giáng dựa trên căn bậc hai trung bình bình phương (second-order fluctuation). Thước đo này chỉ đủ sức tóm tắt các hệ thống đơn phân dạng. Đối với các hệ thống phức tạp (multifractal) nơi các dao động lớn và nhỏ tuân theo các quy luật scaling khác biệt, một giá trị $\alpha$ là hoàn toàn vô dụng.

---

## III. KẾT LUẬN VÀ LỊCH SỬ TIẾN HÓA

Năm giới hạn trên phản ánh chính xác trục lịch sử tiến hóa của lĩnh vực phân tích chuỗi thời gian phi tuyến:
1.  **Hurst (1951):** Mở đường bằng việc phát hiện sự phụ thuộc dài hạn (long-range dependence) nhưng công cụ R/S quá nhạy cảm và dễ bị đánh lừa bởi xu hướng ngoại sinh (trend).
2.  **Peng (1994):** Khắc phục được điểm yếu của Hurst bằng cơ chế "Local Detrending" để đo lường tương quan dài hạn đáng tin cậy hơn trên dữ liệu phi dừng.
3.  **Kantelhardt và cộng sự (2002):** Nhận diện được giới hạn số 4 và số 5 của Peng, từ đó phát triển **Multifractal DFA (MFDFA)** để xử lý các hệ sinh lý phức tạp, đánh dấu bước chuyển mình từ phân tích đơn phân dạng sang đa phân dạng.
4.  

# Tổng hợp: Thiết kế dữ liệu kiểm soát (Control Sequences) trong Peng (1994)

Để chứng minh tính ưu việt của thuật toán DFA, Peng và cộng sự đã thiết kế hai chuỗi dữ liệu kiểm soát đóng vai trò làm "đáp án chuẩn". Cả hai chuỗi đều có bề ngoài nhấp nhô và "chắp vá" (patchy), nhưng bản chất động lực học bên trong lại hoàn toàn đối lập.

| Đặc điểm | Chuỗi 1: Mô hình "Chắp vá" (Uncorrelated Patch) | Chuỗi 2: Mô hình Tương quan (Correlated Sequence) |
| :--- | :--- | :--- |
| **Mục đích** | Mô phỏng "xu hướng cục bộ" giả tạo do cắt ghép. | Đại diện cho cấu trúc Fractal có trí nhớ dài hạn. |
| **Bản chất** | Lắp ghép (stitching) các đoạn random walk độc lập. | Tương quan theo quy luật lũy thừa (power-law) tự nhiên. |

---

#### 1. Chuỗi kiểm soát 1: Mô hình "Chắp vá" (Không tương quan)
Đây là chuỗi "mồi nhử" được thiết kế để đánh lừa các công cụ đo lường bằng cách tạo ra các xu hướng (trend) giả tạo.

*   **Khởi tạo:** Tạo một chuỗi có tổng chiều dài $N = 100000$ điểm.
*   **Phân mảnh ngẫu nhiên:** Cắt chuỗi này thành $k = 40$ vùng con (subregions) có chiều dài dao động ngẫu nhiên từ 68 đến 11679 điểm.
*   **Gán độ lệch (Bias):** Mỗi vùng con được gán một "độ lệch thành phần" rút ngẫu nhiên từ phân phối chuẩn Gaussian (với trung bình là $0.5$ và độ lệch chuẩn $\sigma = 0.1$).
*   **Hệ quả:** Quá trình cắt ghép này tạo ra một "kích thước đặc trưng" (characteristic length scale) tại mốc $2500$ điểm ($100000 / 40$). Thang đo đặc trưng này chính là nguyên nhân gây ra điểm gãy khúc (crossover) trên đồ thị DFA.

#### 2. Chuỗi kiểm soát 2: Mô hình Tương quan dài hạn (Fractal thực sự)
Chuỗi này có bề ngoài "chắp vá" tương tự Chuỗi 1, nhưng cấu trúc đó sinh ra từ bộ nhớ nội tại chứ không phải do can thiệp cơ học. Peng sử dụng bộ lọc Fourier để tạo ra chuỗi này.

*   **Khởi tạo Nhiễu:** Tạo tập hợp các biến ngẫu nhiên, không tương quan từ một phân phối đều (uniform distribution).
*   **Biến đổi Fourier (FFT):** Chuyển đổi chuỗi từ không gian thời gian sang không gian tần số ($q$-space).
*   **Áp đặt Scaling:** Nhân các giá trị phổ trong không gian $q$ với một hàm tỷ lệ lũy thừa (power) để thiết lập chỉ số tương quan mong muốn (ví dụ $\alpha = 0.61$).
*   **Biến đổi ngược (IFFT):** Đưa dữ liệu trở lại miền thời gian. Kết quả thu được là một chuỗi có cấu trúc trí nhớ dài hạn được nhúng chặt ở mọi thang đo.

> **Ý nghĩa thực nghiệm:** Việc chủ động tạo ra hai chuỗi dữ liệu (một chuỗi chứa trend phi dừng nhân tạo, một chuỗi chứa bộ nhớ Fractal thuần khiết) là phương pháp luận hoàn hảo để kiểm chứng độ sắc bén của thuật toán. DFA đã chứng minh được giá trị lịch sử khi "bóc trần" thành công bản chất của cả hai mô hình này.