# 📝 GHI CHÚ NHANH: SỰ THẤT BẠI CỦA FRASER (BINNING) & SỨC MẠNH CỦA KL (k-NN)

## 1. Tử huyệt của Fraser 1986 (Phương pháp Chia lưới - Binning)
Bản chất của Fraser là chia không gian thành các ô vuông (quadtree) và đếm số điểm rơi vào đó. Nó vấp phải 3 nhược điểm chí mạng:
* **Nghịch lý kích thước lưới (Grid-size Paradox):** Chọn ô quá to sẽ làm phẳng đi các cấu trúc phi tuyến (mất nếp gấp của hệ động lực). Chọn ô quá nhỏ thì các thăng giáng nhiễu ngẫu nhiên sẽ chiếm quyền, làm ô bị trống rỗng hoặc sai lệch xác suất.
* **Lời nguyền số chiều (Curse of Dimensionality):** Khi tính toán ở không gian nhiều chiều, số lượng ô lưới tăng theo hàm mũ ($2^D$). Dữ liệu bị "bốc hơi" vào các không gian trống, kiểm định $\chi^2$ hoàn toàn tê liệt vì không đủ số mẫu kỳ vọng.
* **Sai số lượng tử hóa (Discretization Bias):** Việc ép một quỹ đạo liên tục vào các hộp rời rạc sinh ra một lượng sai số hệ thống cố hữu. Khi tính MI ($H(X) + H(Y) - H(X,Y)$), các sai số này không tự triệt tiêu.

## 2. Sự lật đổ của KL 1987 (Phương pháp k-NN)
KL giải quyết toàn bộ các nhược điểm trên bằng cách vứt bỏ tấm lưới cố định:
* **Độ phân giải thích ứng (Adaptive Resolution):** Cố định số điểm đếm ($k$), để khoảng cách ($\epsilon$) tự co giãn. Vùng mật độ cao $\epsilon$ tự thu nhỏ để lấy chi tiết sắc nét; vùng đuôi loãng $\epsilon$ tự phình to để gom đủ dữ liệu.
* **Miễn nhiễm với "Lời nguyền số chiều":** k-NN tính toán dựa trên khoảng cách (distance metric), nên dù ở không gian nhiều chiều, nó vẫn luôn tìm được láng giềng mà không bị rỗng dữ liệu.
* **Giải phẫu sai số bằng Giải tích:** Chấp nhận khoảng cách là biến ngẫu nhiên và dùng hàm Digamma $\psi$ để bù trừ hoàn hảo sai số thống kê vi mô.

**👉 CHỐT LẠI:** Fraser cố gắng xấp xỉ không gian bằng một chiếc lưới thô cứng, còn KL xấp xỉ không gian bằng những "bong bóng" mềm dẻo nương theo đúng hình dáng thực tế của tập dữ liệu.


# 📘 SỔ TAY TOÁN HỌC CHUYÊN SÂU: ƯỚC LƯỢNG ENTROPY KOZACHENKO-LEONENKO (KL 1987) & BƯỚC ĐỆM TỚI KSG (2004)

**Mục tiêu:** Hiểu tận gốc cách KL (1987) dùng giải tích thuần túy để tính Shannon Entropy từ khoảng cách k-NN, và lý do tại sao nó thất bại khi tính Thông tin tương hỗ (MI), buộc KSG (2004) phải ra đời.

---

## PHẦN 1: GIẢI PHẪU TOÁN HỌC NGHIÊM NGẶT (Eq. 13 $\rightarrow$ 20)

Trái tim của phần này nằm ở việc chứng minh: *Làm thế nào hàm Digamma ($\psi$) lại xuất hiện để sửa sai tuyệt đối cho hàm logarit?*

### Bước 1: Rời rạc hóa Tích phân bằng Luật Số Lớn (Eq. 13 $\rightarrow$ 14)
* **Lý thuyết:** Entropy liên tục là kỳ vọng của hàm $-\log \mu(x)$ đối với phân bố $\mu(x)$:
  $$H(X) = \mathbb{E}_{x \sim \mu} [-\log \mu(x)] = - \int_{\mathbb{R}^d} \mu(x) \log \mu(x) dx \quad \text{(13)}$$
* **Thực hành (Thống kê):** Xấp xỉ không chệch bằng trung bình mẫu trên $N$ điểm dữ liệu:
  $$\hat{H}(X) = - \frac{1}{N} \sum_{i=1}^N \log \hat{\mu}(x_i) \quad \text{(14)}$$
  $\rightarrow$ **Nhiệm vụ:** Tìm ước lượng thống kê $\hat{\mu}(x_i)$ sao cho $\mathbb{E}[\log \hat{\mu}(x_i)] = \log \mu(x_i)$.

### Bước 2: Thiết lập Phân bố Xác suất Vi mô (Eq. 15 $\rightarrow$ 16)
Thay vì tìm $\mu(x_i)$ trực tiếp, xét biến ngẫu nhiên là khối lượng xác suất $p_i(\epsilon)$ lọt vào quả cầu $B(x_i, \epsilon/2)$: $p_i(\epsilon) = \int_{B} \mu(x) dx$.
Xác suất để điểm láng giềng thứ $k$ rơi chính xác lên vỏ quả cầu là một bài toán Tổ hợp:
* Có $k-1$ điểm bên trong: $p_i^{k-1}$
* Có $1$ điểm trên biên: $dp_i(\epsilon)$
* Có $N-k-1$ điểm bên ngoài: $(1-p_i)^{N-k-1}$



Phương trình vi phân tổng hợp:
$$P_k(\epsilon) d\epsilon = k \binom{N-1}{k} p_i^{k-1} (1-p_i)^{N-k-1} dp_i(\epsilon) \quad \text{(15, 16)}$$
$\rightarrow$ **Nhận xét:** Đổi biến sang không gian $p$, đây chính xác là **Phân bố Beta** với $\alpha = k, \beta = N-k$.

### Bước 3: Đột phá Giải tích - Kỳ vọng của Logarit (Eq. 17) 🌟
Đây là bước vĩ đại nhất. Tính kỳ vọng của biến ngẫu nhiên $\log p_i$:
$$\mathbb{E}[\log p_i] = \int_0^1 \log(p) \cdot f_{Beta}(p; k, N-k) dp$$
Sử dụng **Hàm Beta Euler** $B(\alpha, \beta)$, lấy đạo hàm riêng theo $\alpha$ hai vế. Ký hiệu hàm Digamma là $\psi(x) = \frac{\Gamma'(x)}{\Gamma(x)}$, giải tích hàm sinh ra kết quả chính xác tuyệt đối (không xấp xỉ):
$$\mathbb{E}[\log p_i] = \psi(k) - \psi(N) \quad \text{(17)}$$
*(Hàm $\psi$ đã tự động triệt tiêu sai số hệ thống sinh ra khi lấy logarit của một biến ngẫu nhiên).*

### Bước 4: Chấp nhận Xấp xỉ Hình học (Eq. 18)
Giả định ở giới hạn vi mô ($N$ đủ lớn), quả cầu $\epsilon$ rất nhỏ, mật độ $\mu(x_i)$ bên trong gần như không đổi. 
$$p_i(\epsilon) \approx c_d \epsilon^d \mu(x_i) \quad \text{(18)}$$
*(Khối lượng = Thể tích $\times$ Mật độ).*

### Bước 5 & 6: Cô lập Mật độ & Hoàn thiện (Eq. 19 $\rightarrow$ 20)
Lấy logarit (18) và thế (17) vào, cô lập được $\log \mu(x_i)$. Đưa ngược lại vào (14) và chuyển Kỳ vọng lý thuyết thành Trung bình mẫu thực nghiệm, ta thu được:
$$\hat{H}(X) = - \psi(k) + \psi(N) + \log(c_d) + \frac{d}{N} \sum_{i=1}^N \log \epsilon_i \quad \text{(20)}$$

---

## PHẦN 2: NÚT THẮT CỦA KL VÀ ĐỘNG LỰC CẢI TIẾN CỦA KSG (2004)

Thuật toán KL (1987) là một kiệt tác cho Entropy 1 chiều. Tuy nhiên, khi áp dụng để tính toán Thông tin tương hỗ (Mutual Information) đa chiều: $I(X,Y) = H(X) + H(Y) - H(X,Y)$, phương pháp này bộc lộ một "tử huyệt".

### 1. Sự bất đồng nhất của khoảng cách $\epsilon$ (Geometric Bias)
Nếu áp dụng ngây thơ KL 3 lần độc lập:
* Tính $H(X,Y)$ ở không gian 2D $\rightarrow$ Vòng tròn láng giềng phải mở rất to $\rightarrow \epsilon_{xy}$ lớn.
* Tính $H(X)$ trên trục 1D $\rightarrow$ Dữ liệu bị ép xẹp, láng giềng rất gần $\rightarrow \epsilon_x$ nhỏ.
* Tính $H(Y)$ trên trục 1D $\rightarrow \epsilon_y$ nhỏ.

Mặc dù hàm $\psi$ đã triệt tiêu sai số thống kê vi mô, nhưng việc dùng các khoảng cách vật lý có độ lớn chênh lệch nhau này tạo ra một **sai số hình học khổng lồ**. Khi thực hiện phép cộng trừ, các sai số này **không tự triệt tiêu**.

### 2. Ý nghĩa thực tiễn & Sự can thiệp của KSG
Khi xử lý các chuỗi tín hiệu sinh lý có tính phi dừng cao (như việc trích xuất đặc trưng phi tuyến từ tín hiệu PPG để phát hiện độ thức tỉnh/buồn ngủ của tài xế), việc áp dụng ngây thơ công thức KL sẽ tạo ra các điểm cực tiểu giả (false minimums). Đặc biệt khi đối chiếu các mô hình hiện đại trên các tập dữ liệu thực nghiệm tiêu chuẩn (như áp dụng hệ thống đo lường này lên phiên bản 2025 của PhysDrive), sai số hệ thống chưa bị triệt tiêu của KL sẽ bị khuếch đại, làm sai lệch hoàn toàn việc chọn độ trễ $\tau$.



**Đột phá của KSG (2004) - Thuật toán 1:**
Để tiêu diệt triệt để sai số này, Kraskov, Stögbauer và Grassberger đã thay đổi hoàn toàn luật chơi:
* Dùng **Chuẩn Cực Đại (Maximum Norm)** để biến quả cầu láng giềng ở không gian tổng thành một **Hình Vuông**.
* Đóng băng khoảng cách $\epsilon$ của hình vuông đó, chiếu nó xuống trục $X$ và trục $Y$.
* Thay vì đi tìm $\epsilon$ mới, thuật toán chỉ việc **đếm số điểm $n_x, n_y$** lọt vào cái bóng của hình vuông đó.
* **Kết quả:** Phép chiếu hình học này ép hệ thống phải sử dụng chung một thang đo $\epsilon$. Khi cộng trừ Entropy, biến số $\epsilon$ bị triệt tiêu hoàn toàn, để lại một công thức đo lường MI thuần khiết không sai số!

# 📐 BẢN LƯỢC DỊCH TOÁN HỌC: BỘ ƯỚC LƯỢNG $I^{(1)}$ CỦA KSG (MỤC II.B)

**Mục tiêu:** Xây dựng công cụ tính MI $I(X,Y) = H(X) + H(Y) - H(X,Y)$ miễn nhiễm với sai số lượng tử hóa.

### Bước 1: Ước lượng Không gian Tổng (Phương trình 21)
Áp dụng bộ ước lượng KL cho không gian kết hợp $Z = (X,Y)$ bằng **chuẩn cực đại (Max-norm)**. 
Đặc tính của chuẩn này biến "quả cầu láng giềng" thành một hình hộp vuông, cho phép tách hằng số thể tích: $c_d = c_{d_X} c_{d_Y}$. Khoảng cách đến láng giềng thứ $k$ là $\epsilon(i)/2$.
$$\hat{H}(X,Y) = -\psi(k) + \psi(N) + \log(c_{d_X} c_{d_Y}) + \frac{d_X+d_Y}{N} \sum_{i=1}^N \log \epsilon(i) \quad \text{(21)}$$

### Bước 2: Chỉ điểm "Nghịch lý Sai số Biên" (Bottleneck)
Nếu tiếp tục áp dụng máy móc KL để tính $\hat{H}(X)$ và $\hat{H}(Y)$ độc lập với cùng tham số $k$:
* Không gian tổng $Z$ thưa thớt hơn $\rightarrow$ $\epsilon_Z$ mở rộng rất lớn.
* Không gian biên $X, Y$ đặc hơn $\rightarrow$ $\epsilon_X, \epsilon_Y$ co lại rất nhỏ.

**Hệ quả:** Sai số hệ thống của KL tỷ lệ thuận với $\epsilon$. Vì $\epsilon_Z \neq \epsilon_X \neq \epsilon_Y$, các sai số này lệch pha nhau và **không thể tự triệt tiêu** khi thực hiện phép trừ $H(X) + H(Y) - H(X,Y)$.

### Bước 3: Phép chiếu Hình học - Đóng băng Thang đo (Phương trình 22)
KSG đảo ngược tư duy: **Thay vì cố định $k$ và thả nổi $\epsilon$, hãy đóng băng $\epsilon$ và thả nổi $k$ trên các không gian biên.**
* Lấy ranh giới hộp vuông $\epsilon(i)$ từ không gian $Z$, chiếu thẳng đứng xuống trục $X$ và trục $Y$.
* Đếm số điểm dữ liệu nằm nghiêm ngặt bên trong các bóng chiếu này $\rightarrow$ thu được các biến đếm $n_x(i)$ và $n_y(i)$.
* Lúc này, khoảng cách $\epsilon(i)/2$ đóng vai trò là láng giềng thứ $n_x(i)+1$ trên trục $X$. Áp dụng lại KL:
$$\hat{H}(X) = -\frac{1}{N} \sum_{i=1}^N \psi(n_x(i) + 1) + \psi(N) + \log c_{d_X} + \frac{d_X}{N} \sum_{i=1}^N \log \epsilon(i) \quad \text{(22)}$$

### Bước 4: Sự triệt tiêu Giải tích Tuyệt đối (Khởi sinh Phương trình 8)
Thực hiện phép trừ $I^{(1)} = \hat{H}(X) + \hat{H}(Y) - \hat{H}(X,Y)$ với các biểu thức vừa thiết lập. 

Phép màu đại số xuất hiện:
1.  **Triệt tiêu Hằng số:** $\log(c_{d_X}) + \log(c_{d_Y}) - \log(c_{d_X} c_{d_Y}) = 0$.
2.  **Triệt tiêu Khoảng cách (Trọng tâm):** Lượng $\frac{d_X}{N}\sum\log\epsilon(i)$ cộng $\frac{d_Y}{N}\sum\log\epsilon(i)$ triệt tiêu chính xác 100% với lượng $\frac{d_X+d_Y}{N}\sum\log\epsilon(i)$ của không gian tổng.

Biến số vật lý hoàn toàn bốc hơi, bộ ước lượng chỉ còn lại các hàm bù trừ thống kê:
$$I^{(1)}(X,Y) = \psi(k) - \langle \psi(n_x + 1) + \psi(n_y + 1) \rangle + \psi(N)$$

### Bước 5: Tổng quát hóa Đa chiều (Phương trình 23)
Nhờ sự đơn giản hóa khốc liệt sau khi loại bỏ được biến số khoảng cách, việc mở rộng thuật toán lên $m$ chiều $(X_1, ..., X_m)$ trở nên hệ thống:
$$I^{(1)}(X_1, ..., X_m) = \psi(k) + (m - 1)\psi(N) - \langle \psi(n_{x_1}) + ... + \psi(n_{x_m}) \rangle \quad \text{(23)}$$

---
**💡 ĐÚC KẾT TRIẾT LÝ KSG:**
Thay vì đo đạc các khoảng cách lệch pha nhau, KSG dùng chung một kích thước hộp vuông (đồng bộ hóa ranh giới chiếu). Thao tác hình học này ép hệ thống giải tích phải ép mọi sai số (bias) triệt tiêu lẫn nhau. Kết quả là một bộ đo lường chỉ cần "vẽ hộp và đếm điểm", cực kỳ mượt mà, miễn nhiễm với nhiễu và lý tưởng cho các tín hiệu phi dừng phức tạp.

# 📐 BẢN LƯỢC DỊCH TOÁN HỌC: BỘ ƯỚC LƯỢNG $I^{(2)}$ CỦA KSG (MỤC II.C)

**Mục tiêu:** Khắc phục sai số hệ thống của Thuật toán 1 tại các trục biên bằng cách chuyển từ "Hộp vuông" (Hyper-cube) sang "Khối chữ nhật" (Hyper-rectangle).

### 1. Động lực: "Lỗ hổng" của Hộp vuông $I^{(1)}$
* **Nghịch lý độ khít:** Thuật toán 1 dùng một khoảng cách $\epsilon(i)$ duy nhất. Ranh giới này chạm chính xác vào điểm láng giềng trong không gian tổng $Z$, nhưng khi chiếu xuống các trục biên ($X, Y$), ranh giới $\epsilon(i)$ thường "rộng" hơn khoảng cách thực tế đến các điểm dữ liệu ngoài cùng trong bóng chiếu.
* **Hậu quả:** Việc dùng $\epsilon$ chung khiến phương trình KL áp dụng cho các trục biên chỉ là một phép xấp xỉ lỏng lẻo. Ở không gian chiều cao, sự chênh lệch này khuếch đại thành sai số hệ thống (systematic bias).
* **Giải pháp $I^{(2)}$:** KSG ép ranh giới phải "khít" hoàn toàn. Đo chính xác khoảng cách $\epsilon_x$ và $\epsilon_y$ đến các điểm láng giềng trên từng trục, tạo thành một khối chữ nhật.

### 2. Thiết lập Xác suất Khối chữ nhật (Phương trình 24 - 26)
Việc sử dụng khối chữ nhật phá vỡ tính đối xứng của chuẩn cực đại, tạo ra các kịch bản hình học khác nhau:
* **Trường hợp (b):** 1 điểm duy nhất nằm ở góc quyết định cả 2 ranh giới $\epsilon_x, \epsilon_y$. (Xác suất $P_k^{(b)}$).
* **Trường hợp (c):** 2 điểm nằm trên 2 cạnh vuông góc khác nhau cùng định cỡ khối chữ nhật. (Xác suất $P_k^{(c)}$).

Hàm phân bố láng giềng lúc này là tổng tổ hợp:
$$P_k(\epsilon_x,\epsilon_y) = P_k^{(b)} + P_k^{(c)} \quad \text{(24)}$$
*(Chú ý: KSG sử dụng $q_i$ làm khối lượng của hình chữ nhật, và kẹp thêm $p_i$ - khối lượng của hình vuông bao ngoài - để duy trì điều kiện chuẩn cực đại).*

### 3. Đột phá Giải tích: Hệ số phạt $-1/k$ (Phương trình 27 & 9)
Khi lấy tích phân giải tích hàm xác suất phức hợp trên để tìm kỳ vọng của $\log(q_i)$, sự phân rã hình học sinh ra một hệ số bù trừ mới:
$$E(\log q_i) = \psi(k) - \frac{1}{k} - \psi(N) \quad \text{(27)}$$

Đưa kỳ vọng này vào phép tính $H(X) + H(Y) - H(X,Y)$, ta thu được Thuật toán 2:
$$I^{(2)}(X,Y) = \psi(k) - \frac{1}{k} - \langle \psi(n_x) + \psi(n_y) \rangle + \psi(N) \quad \text{(9)}$$
*(Lưu ý: Biến đếm $n_x, n_y$ không còn cộng $1$ như $I^{(1)}$ vì ranh giới lúc này đã ép khít chính xác vào các điểm láng giềng).*

### 4. Tổng quát hóa Đa chiều (Phương trình 28 - 30)
Trong không gian $m$ chiều $(X_1, ..., X_m)$, số kịch bản hình học bùng nổ. KSG dùng thủ thuật đồng nhất tỷ lệ tích phân (hệ số $k^{m-1}$) để bỏ qua việc đếm tổ hợp, đi thẳng đến kỳ vọng tổng quát với đại lượng phạt tỷ lệ thuận với số chiều:
$$I^{(2)}(X_1, ..., X_m) = \psi(k) - \frac{m-1}{k} + (m-1)\psi(N) - \langle \psi(n_{x_1}) + ... + \psi(n_{x_m}) \rangle \quad \text{(30)}$$

### 5. Sự thỏa hiệp Hình học (Cheating Slightly)
KSG thể hiện sự nghiêm cẩn học thuật khi chỉ ra một "điểm mù" của $I^{(2)}$:
* **Vấn đề:** Có những vùng không gian nằm ngoài khối chữ nhật $\epsilon_x \times \epsilon_y$, nhưng lại nằm lọt trong bóng chiếu dọc/ngang của khối vuông bao ngoài. Nhờ chuẩn cực đại, ta biết chắc chắn các vùng này rỗng.
* **Lẽ ra:** Phải trừ các vùng rỗng này ra khỏi tích phân Entropy biên để tăng độ chính xác.
* **Thỏa hiệp:** KSG lờ đi bước này để giữ cho phương trình toán học khả thi. Họ chứng minh bằng giải tích rằng sai số do sự thỏa hiệp này tạo ra tỷ lệ với $O(1/n_x)$ và $O(1/n_y)$, nghĩa là nó sẽ tự động tiêu biến về 0 ở các tập dữ liệu đủ lớn ($N \to \infty$).

---
**💡 ĐÚC KẾT SỰ KHÁC BIỆT:**
Nếu $I^{(1)}$ hi sinh độ khít của ranh giới (chịu xấp xỉ ở trục biên) để giữ phương trình đơn giản, thì $I^{(2)}$ hi sinh sự đơn giản của phương trình (phải sinh ra hệ số phạt $-(m-1)/k$) để ép ranh giới hình học khít tuyệt đối trên mọi chiều không gian. Trong thực hành, $I^{(2)}$ là lựa chọn sắc bén hơn khi làm việc với các hệ thống đa chiều có sự phân bố mật độ cực kỳ bất đối xứng.

# 🚀 BẢN GHI CHÚ: SỰ TIẾN HÓA CỦA CÁC THUẬT TOÁN ƯỚC LƯỢNG THÔNG TIN TƯƠNG HỖ (SAU KSG 2004)

Mặc dù KSG (2004) đã thiết lập tiêu chuẩn vàng trong việc sử dụng chuẩn cực đại (max-norm) để triệt tiêu sai số k-NN, sự bùng nổ của Dữ liệu lớn và Học sâu (Deep Learning) đã thúc đẩy giới khoa học tạo ra các thế hệ thuật toán mới để vượt qua giới hạn về số chiều và tốc độ tính toán.

## 1. Nhóm Cải tiến Thống kê Nền tảng (Vá lỗi KSG)
Nhóm này vẫn trung thành với triết lý k-NN nhưng xử lý các "điểm mù" về hình học mà KSG chưa giải quyết triệt để:
* **LNC (Local Non-uniformity Correction - Gao et al., 2015):** * *Vấn đề:* KSG giả định mật độ dữ liệu bên trong khối láng giềng $\epsilon$ là đồng đều. Nếu dữ liệu có tương quan phi tuyến mạnh (tạo thành một đa tạp hẹp), giả định này sụp đổ.
    * *Giải pháp:* LNC dùng PCA (Phân tích thành phần chính) ngay tại từng vùng cục bộ để xoay trục và chuẩn hóa thể tích, giúp KSG chính xác trở lại trên các cấu trúc dữ liệu bị bóp méo cực độ.
* **EDGE (Ensemble Estimators - Noshad et al., 2019):** Kết hợp lý thuyết đồ thị và kỹ thuật băm (hashing) để giảm phương sai khi phải đối mặt với dữ liệu có số chiều cao nhưng số lượng mẫu (sample size) lại quá ít.

## 2. Kỷ nguyên Học sâu: Mutual Information Neural Estimators (MINE)
Khi không gian ẩn (latent space) lên tới hàng nghìn chiều, các thuật toán dựa trên khoảng cách (như KSG) bị tê liệt bởi "Lời nguyền số chiều". Neural Networks bước vào cuộc chơi:
* **MINE (Belghazi et al., 2018):** Thay vì đếm điểm láng giềng, MINE dùng một Mạng Neural để tối đa hóa cận dưới (lower bound) của Thông tin tương hỗ dựa trên biểu diễn Donsker-Varadhan.
    * *Ưu điểm:* Tính được MI cho ảnh, chuỗi thời gian n-chiều; có khả năng tính vi phân (differentiable) để đưa trực tiếp vào hàm Loss.
* **InfoNCE & SMILE:** Các biến thể cải tiến cận dưới của MI, hiện đang là "trái tim" của trào lưu Học tự giám sát (Contrastive Learning - ví dụ như cách mô hình CLIP của OpenAI đối chiếu ảnh và text).

## 3. Tối ưu Hiệu năng cho Chuỗi Thời Gian / Dữ Liệu Lớn
Khi phân tích tín hiệu sinh lý (PPG, ECG) với hàng triệu điểm dữ liệu:
* **Cấu trúc dữ liệu không gian (cKDTree / BallTree):** Phế bỏ việc tính toán ma trận khoảng cách thủ công $O(N^2)$, đẩy độ phức tạp thuật toán xuống mức $O(N \log N)$.
* **JIDT / IDTxl:** Các thư viện mã nguồn mở chuyên dụng cho Transfer Entropy và Động lực học mạng. Chúng sử dụng lõi KSG nhưng được viết bằng C++ / Cython để hỗ trợ tính toán song song (Parallel Computing) cực nhanh.

---
> 💡 **BÀI HỌC RÚT RA (TAKEAWAY): CÓ NÊN BỎ RƠI KSG?**
>
> **KHÔNG.** Dù MINE hay InfoNCE rất mạnh cho Deep Learning, **KSG (Thuật toán 1) vẫn là Tiêu chuẩn vàng** trong Phân tích Động lực học Phi tuyến (Nonlinear Dynamics) truyền thống — đặc biệt là bài toán **Tìm độ trễ thời gian $\tau$** và **Tái tạo không gian pha**.
> 
> *Lý do:* KSG không cần huấn luyện (training-free), không phụ thuộc hyperparameter (chỉ cần chọn $k$), và có sự "lỳ lợm" (robustness) tuyệt đối trước nhiễu phi dừng — điều kiện tiên quyết để bung mở các bộ hút hỗn mang (chaos attractors) một cách chính xác nhất.
>
> # 🛠️ BẢN CÔ ĐỌNG: CẨM NANG TRIỂN KHAI THỰC TẾ THUẬT TOÁN KSG (MỤC III.A)

Mục III.A cung cấp 4 thủ thuật "sống còn" để chuyển hóa toán học KSG thành mã nguồn chạy được trên dữ liệu thực tế:

### 1. Biến đổi Hình học (Transformations)
* **Cơ sở lý thuyết:** MI bất biến dưới các phép biến đổi đồng phôi (bóp méo trơn tru), trong khi Entropy thì không.
* **Thực hành:** * Luôn **chuẩn hóa phương sai** về 1.
  * Nếu phân bố dữ liệu quá lệch hoặc có điểm kỳ dị (như hệ động lực $G$-exponential), việc dùng **phép biến đổi logarit** ($x' = \log x$) sẽ làm mịn phân bố, triệt tiêu sai số khổng lồ của thuật toán nguyên bản.

### 2. Tối ưu Nút thắt Cổ chai (Fast Neighbor Search)
Thuật toán k-NN là gánh nặng CPU lớn nhất. Có 3 cấp độ thiết kế:
* **Vét cạn $\mathcal{O}(N^2)$:** Tính mọi khoảng cách. Chỉ dùng cho đồ chơi ($N \le 300$).
* **Sắp xếp (Quicksort):** Sắp xếp tọa độ để thu hẹp vùng tìm kiếm cục bộ. Chạy ổn với vài nghìn điểm.
* **Chia lưới (Grids/Boxes):** Đỉnh cao tối ưu. Chia không gian thành lưới 1D (cỡ $1/N$) và 2D (cỡ $\sqrt{k/N}$). Phương pháp này biến KSG thành một thuật toán siêu tốc, ngang ngửa các công cụ binning tốt nhất thời bấy giờ.

### 3. "Tuyệt chiêu" Chống Trùng lặp (Degeneracy)
* **Vấn đề chí mạng:** Dữ liệu vật lý số hóa (ADC 12/16-bit) tạo ra vô số điểm trùng giá trị tuyệt đối. Khoảng cách bằng 0 khiến biến đếm láng giềng ($n_x, n_y$) tê liệt và đếm sai.
* **Giải pháp KSG:** Cộng thẳng một lượng **nhiễu ngẫu nhiên siêu nhỏ** ($< 10^{-10}$ với biến double) vào toàn bộ dữ liệu. Nó bẻ gãy các điểm trùng lặp một cách nhân tạo để hệ thống đếm hoạt động trơn tru mà không làm xước bản chất động lực học của tín hiệu.

### 4. Chuẩn hóa Mật độ bằng Xếp hạng (Rank Ordering)
* **Kỹ thuật:** Thay vì dùng giá trị thực, dùng thứ hạng (rank) của điểm dữ liệu. Việc này ép một đám mây điểm hỗn loạn thành một phân bố đồng đều (uniform density) hoàn hảo.
* **Đánh giá:** Rất hiệu quả. KSG vẫn tính ra MI cực kỳ chính xác (bằng 0 nếu độc lập tuyệt đối), với **điều kiện bắt buộc** là vẫn phải kết hợp "tuyệt chiêu nhiễu $10^{-10}$" để xử lý các điểm có cùng thứ hạng.

---
> 💡 **ĐÚC KẾT CHO PIPELINE XỬ LÝ TÍN HIỆU (VD: PPG):**
> Để một bộ mã nguồn KSG không bao giờ sụp đổ khi nhận dữ liệu thực: **(1)** Chuẩn hóa/Logarit hóa $\rightarrow$ **(2)** Dùng cấu trúc không gian (như `cKDTree`) thay vì vòng lặp $\rightarrow$ **(3) Lệnh bắt buộc:** `data += np.random.normal(scale=1e-10, size=data.shape)`.