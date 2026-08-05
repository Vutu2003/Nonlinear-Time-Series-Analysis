# Paper Metadata
* **Title:** Embeddings and delays as derived from quantification of recurrence plots
* **Authors:** Joseph P. Zbilut and Charles L. Webber Jr.
* **Year:** 1992
* **Keywords:** Recurrence plots, embeddings, delays, dynamical time series, quantification
  
# 1. Why

## Research Question (Câu hỏi nghiên cứu)
* Làm thế nào để lượng hóa các đặc trưng của Recurrence Plot (RP) nhằm tìm ra chiều nhúng (embedding dimension) và thời gian trễ (time delay) tối ưu?
* Có thể dùng sự "mở ra" (topological unfolding) định lượng của RP để xác nhận tính tất định của một hệ thống thay vì ngẫu nhiên không?

## Motivation (Động lực nghiên cứu)
* **Thách thức dữ liệu thực tế:** Dữ liệu thực (đặc biệt trong sinh học) thường ngắn, nhiễu và thiếu tính dừng.
* **Giới hạn của thị giác:** Đánh giá RP bằng mắt rất chủ quan và khó tái lập khi mật độ điểm lặp cao.
* **Nhu cầu định lượng:** Cần nâng cấp RP từ công cụ chẩn đoán định tính sang đo lường định lượng để dễ so sánh và tự động hóa.
* **Tối ưu tham số:** Cần cơ sở khách quan để lựa chọn các tham số tái dựng không gian pha.

## Previous Methods (Các phương pháp tiền nhiệm)
* **RP của Eckmann (1987):** Đề xuất RP trực quan dùng bán kính lân cận thích nghi; phát hiện đường chéo liên hệ với số mũ Lyapunov.
* **Hạn chế:** Phụ thuộc hoàn toàn vào mắt người. Việc thiếu cơ sở toán học để đo đếm các cấu trúc hình học làm giới hạn khả năng ứng dụng và tự động hóa của RP.

# 2. What

## Core Insight (Thấu hiểu cốt lõi)
*   **Khắc phục giới hạn thị giác:** Đột phá lớn nhất là chuyển Recurrence Plot (RP) từ một công cụ quan sát định tính (dễ chủ quan, khó tái lập) sang công cụ đo lường định lượng[cite: 2].
*   **Lượng hóa 2 đặc trưng cơ bản:** Đề xuất tính toán **Percent Recurrence (%REC)** (mật độ điểm) và **Percent Line (%LINE)** (tỷ lệ điểm tạo thành đoạn thẳng) thay vì chỉ "nhìn" các texture[cite: 2].
*   **Đánh giá tham số khách quan:** Theo dõi sự biến thiên của %REC và %LINE theo chiều nhúng và độ trễ để quan sát quá trình "mở ra" (topological unfolding) của attractor, giúp chọn tham số nhúng chính xác hơn[cite: 2].
*   **Xác nhận tính tất định:** Cung cấp bằng chứng định lượng giúp phân biệt hệ động lực xác định thấp chiều với tín hiệu ngẫu nhiên[cite: 2].

## Mathematical Foundation (Cơ sở Toán học)

**1. Tái dựng quỹ đạo & Tính ma trận khoảng cách**
Tập hợp các vectơ trạng thái $x(1), x(2), ..., x(N)$ trong không gian $\mathbb{R}^d$[cite: 2]. Tính khoảng cách Euclid cho mọi cặp điểm:
$$D(i,j)=\|x(i)-x(j)\|$$

**2. Bán kính ngưỡng cố định (Fixed Radius Threshold)**
Điểm hồi quy tại $(i,j)$ được đánh dấu nếu:
$$\|x(i)-x(j)\| \le r$$
Điểm khác biệt quan trọng: $r$ được **cố định** cho toàn bộ không gian pha thay vì thay đổi thích nghi như phương pháp cũ (thường chọn $r \le 10\%$ khoảng cách trung bình chuẩn hóa của phép nhúng đầu tiên)[cite: 2].

**3. Percent Recurrence (%REC)**
Đại diện cho *mật độ sự kiện hồi quy* (mức độ hệ quay lại trạng thái cũ). Được chuẩn hóa theo nửa tam giác trên (bỏ đường chéo chính)[cite: 2]:
$$\%REC = 100 \times \frac{N_r}{N(N-1)/2}$$
Trong đó, $N_r$ là tổng số điểm hồi quy[cite: 2].

**4. Percent Line (%LINE)**
Đại diện cho *mức độ tổ chức tất định* (các quỹ đạo tiến hóa giống nhau). Một đoạn thẳng cấu thành từ $\ge 2$ điểm liên tiếp song song với đường chéo chính[cite: 2]:
$$\%LINE = 100 \times \frac{N_l}{N_r}$$
Trong đó, $N_l$ là số điểm tham gia vào các đoạn thẳng[cite: 2].

# 3. How

## Algorithm & Mathematical Formulation

Quy trình lượng hóa Recurrence Plot (RP) được thực hiện qua chuỗi biến đổi toán học sau:

1.  **Phase Space Reconstruction:** Từ chuỗi thời gian $u(t)$, tái dựng các vectơ trạng thái $x_i = (u_i, u_{i+\tau}, \dots, u_{i+(d-1)\tau}) \in \mathbb{R}^d$[cite: 2].
2.  **Distance Matrix:** Tính khoảng cách Euclid cho mọi cặp trạng thái $D(i,j) = \|x_i - x_j\|_2$[cite: 2].
3.  **Recurrence Matrix:** Áp dụng ngưỡng bán kính cố định $r$ để tạo ma trận nhị phân $R(i,j) = \Theta(r - D(i,j))$[cite: 2].
4.  **Quantification:** 
    *   Loại bỏ đường chéo chính (Line of Identity - LOI)[cite: 2].
    *   Tính $\%REC = 100 \times \frac{N_r}{N(N-1)/2}$ (với $N_r$ là tổng điểm lặp)[cite: 2].
    *   Xác định các đoạn thẳng (tập hợp $\ge 2$ điểm liên tiếp song song đường chéo chính)[cite: 2]. Tính $\%LINE = 100 \times \frac{N_l}{N_r}$ (với $N_l$ là số điểm thuộc đoạn thẳng)[cite: 2].
5.  **Response Surface:** Quét qua một lưới các giá trị $(d, \tau)$ để xây dựng hàm $f(d, \tau) = (\%REC, \%LINE)$ nhằm quan sát quá trình "mở ra" (topological unfolding) của hệ thống[cite: 2].

## End-to-End Pipeline

Dữ liệu thô $\rightarrow$ Tái dựng không gian pha $\rightarrow$ Ma trận khoảng cách $\rightarrow$ Nhị phân hóa (Fixed Radius) $\rightarrow$ Lượng hóa (%REC, %LINE) $\rightarrow$ Vẽ đường cong phản hồi (Response Curves) $\rightarrow$ Đánh giá & Chọn tham số $d, \tau$[cite: 2].

## Implementation Notes

*   **Bán kính (Fixed Radius):** Sử dụng ngưỡng $r$ cố định (khác với Eckmann 1987). Đề xuất $r < 0.1 \times \bar{D}$ (với $\bar{D}$ là khoảng cách trung bình chuẩn hóa của phép nhúng đầu tiên)[cite: 2].
*   **Chuẩn khoảng cách:** Sử dụng khoảng cách Euclid ($L_2$)[cite: 2].
*   **Định nghĩa đoạn thẳng:** Chỉ tính khi chiều dài $L \ge 2$[cite: 2].
*   **Loại bỏ LOI:** Bắt buộc loại bỏ đường chéo chính $i=j$ khi tính toán các chỉ số để tránh sai lệch[cite: 2].
*   **Parameter Sweep:** Cần quét qua nhiều cặp tham số $(d, \tau)$ để thấy được bức tranh tổng thể về động lực học của hệ[cite: 2].
*   

# 4. Validation

## Assumptions (Các giả định)
* **Tính bảo toàn topology:** Dựa trên định lý Takens, phương pháp trễ thời gian bảo toàn cấu trúc topo của attractor, nên các mối quan hệ hồi quy phản ánh đúng động lực học thực tế.
* **Ý nghĩa hình học:** Các điểm và đoạn thẳng trên Recurrence Plot (RP) không ngẫu nhiên mà đại diện cho đặc tính động lực học của hệ thống.
* **Khả năng quan sát "Topological Unfolding":** Nếu %REC và %LINE phản ánh đúng topology, chúng sẽ biến thiên có quy luật theo $d$ và $\tau$, từ đó giúp định vị cấu hình nhúng tối ưu.

## Experiments (Các thực nghiệm kiểm chứng)

### Experimental Design
* Khảo sát trên lưới tham số: chiều nhúng $d \in [1, 6]$, độ trễ $\tau \in [1, 20]$. 
* Dữ liệu: 2000 điểm (đã loại bỏ transients).
* 4 hệ thống thử nghiệm:
  1. **Hệ Lorenz** (Liên tục, $D_f \approx 2.6$)
  2. **Hệ Mackey-Glass** (Liên tục, $D_f \approx 2.13$)
  3. **Bản đồ Hénon** (Rời rạc, $D_f \approx 1.26$)
  4. **Dữ liệu ngẫu nhiên** (Phân bố đều)

### Experimental Results & Validation Summary
* **Hệ liên tục (Lorenz & Mackey-Glass):** Cả %REC và %LINE đều biến thiên có hệ thống, xuất hiện cực trị rõ ràng thể hiện quá trình "mở ra" của attractor. Giá trị $\tau$ thu được khớp với cực tiểu đầu tiên của hàm tự tương quan.
* **Hệ rời rạc (Hénon Map - Khám phá quan trọng nhất):** %REC thất bại trong việc thể hiện unfolding (kết quả phẳng, giống dữ liệu ngẫu nhiên). Ngược lại, **%LINE** hiển thị cực đại cực kỳ sắc nét tại chính xác cấu hình $d=2, \tau=1$. Điều này khẳng định các đoạn thẳng (%LINE) chứa đựng thông tin động lực học cốt lõi mạnh mẽ hơn nhiều so với các điểm lặp đơn lẻ.
* **Dữ liệu ngẫu nhiên:** %REC và %LINE gần như phẳng và không thay đổi trên toàn bộ lưới tham số, tạo sự tương phản tuyệt đối để phân biệt với các hệ tất định.

## Limitations (Các giới hạn)
* **Sự kém nhạy của %REC:** Thiếu độ nhạy với quá trình unfolding ở một số hệ động lực, đặc biệt là hệ rời rạc.
* **Đòi hỏi khắt khe về dữ liệu:** Dễ sinh ra kết quả giả (spurious results) nếu chuỗi thời gian quá ngắn, nhiễu cao, hoặc không đảm bảo tính dừng.
* **Chưa tối ưu chuẩn khoảng cách:** Việc mặc định sử dụng chuẩn khoảng cách Euclid ($L_2$) có thể chưa phải là giải pháp toán học tối ưu nhất cho mọi hệ.
* **Thiếu cơ sở lý thuyết cho bán kính $r$:** Giá trị $r$ ảnh hưởng trực tiếp đến kết quả lượng hóa, nhưng bài báo chưa xây dựng được nguyên tắc lựa chọn tổng quát mà chỉ dừng ở mức kinh nghiệm thực nghiệm ($r < 10\%$ khoảng cách trung bình chuẩn hóa).

# 5. My Research

## Research Ideas (Ý tưởng nghiên cứu)

Dựa trên nền tảng lượng hóa của Zbilut & Webber (1992), có ba hướng triển khai chính cho luận văn:

*   **Theo dõi động lực học tín hiệu sinh học theo thời gian:** Áp dụng cửa sổ trượt (Sliding Window) để tính liên tục %REC và %LINE. Phương pháp này giúp giám sát sự thay đổi cấu trúc động lực học, từ đó phát hiện các chuyển pha sinh lý (ví dụ: mệt mỏi, buồn ngủ) từ tín hiệu sinh học như PPG, ECG.
*   **Tự động lựa chọn tham số tái dựng:** Thay thế các phương pháp truyền thống (FNN, Mutual Information) bằng cách sử dụng trực tiếp Response Curves của %REC và %LINE để định vị cấu hình nhúng ($d, \tau$) tối ưu thông qua quá trình "mở ra" (topological unfolding) của attractor.
*   **Mở rộng sang các chỉ số RQA hiện đại:** Lấy %REC và %LINE làm bước đệm để tiến tới áp dụng bộ chỉ số Recurrence Quantification Analysis (RQA) toàn diện hơn, bao gồm Determinism (DET), Longest Diagonal Line (Lmax), Shannon Entropy (ENTR), Laminarity (LAM), và Trapping Time (TT).

## Knowledge Contribution (Đóng góp tri thức / Đóng góp cho luận văn)

*   **Khai sinh tư duy lượng hóa Recurrence Plot:** Thực hiện bước chuyển dịch mang tính lịch sử từ diễn giải trực quan bằng mắt (Visual Interpretation) sang phân tích định lượng bằng máy tính (Quantitative Analysis), khai sinh ra nền tảng của RQA.
*   **Thiết lập hai đại lượng tiên phong:** Định nghĩa hai chỉ số nền móng: %REC (đo lường mật độ sự kiện hồi quy) và %LINE (đo lường mức độ tổ chức thành các quỹ đạo tiến hóa tương tự).
*   **Chuẩn hóa thuật toán Recurrence Matrix:** Cải tiến phương pháp của Eckmann (1987) bằng cách áp dụng bán kính cố định (Fixed Radius) và chuẩn khoảng cách Euclid, giúp đơn giản hóa tính toán và đảm bảo tính đối xứng tuyệt đối cho ma trận.
*   **Khẳng định giá trị động lực học của đường chéo:** Chứng minh sự vượt trội của %LINE so với %REC trong việc phản ánh quá trình unfolding (đặc biệt qua hệ Hénon). Phát hiện cốt lõi: một điểm lặp đơn lẻ chỉ là trạng thái lặp lại, nhưng một chuỗi điểm tạo thành đường chéo mang theo quy luật tiến hóa của hệ (tiền đề cho chỉ số Determinism - DET sau này).

## My Takeaways (Những điều tôi kế thừa)

1.  **Lượng hóa triệt để:** Không sử dụng Recurrence Plot như một bức tranh trực quan, mà phải xử lý nó như một ma trận toán học có thể đo lường.
2.  **Tập trung vào đường chéo:** Ưu tiên khai thác các cấu trúc đường chéo vì chúng lưu trữ trực tiếp quy luật tiến hóa của hệ động lực học.
3.  **Chuẩn hóa ma trận:** Bắt buộc sử dụng bán kính ngưỡng cố định (Fixed Radius) để đảm bảo tính đối xứng cho ma trận hồi quy.
4.  **Phân tích theo thời gian:** Ứng dụng lượng hóa RP như một công cụ giám sát sự biến thiên của hệ thống theo thời gian thực, vượt ra khỏi bài toán tìm kiếm tham số nhúng ban đầu.

## Paper Contribution (Một câu tóm tắt)

Nếu đóng góp của Eckmann (1987) là:
> **"Recurrence Plot giúp chúng ta nhìn thấy động lực học."**

Thì di sản vĩ đại nhất của Zbilut & Webber (1992) được tóm gọn lại là:
> **"Nếu các texture của Recurrence Plot mang ý nghĩa vật lý, thì chúng phải được chuyển thành những đại lượng có thể đo lường."**