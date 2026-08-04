# Paper Metadata
* **Title**: Multiscale entropy analysis of biological signals
* **Authors**: Madalena Costa, Ary L. Goldberger, and C.-K. Peng
* **Year**: 2005
* **Keywords**: Multiscale entropy (MSE), biological signals, complexity, sample entropy

# 1. Why: Sự ra đời của Multiscale Entropy (Costa et al., 2005)

## 1.1. Research Questions
*   **Định nghĩa lại Complexity:** Làm thế nào để xây dựng một thước đo phản ánh đúng bản chất của độ phức tạp sinh lý, thay vì chỉ đo lường mức độ ngẫu nhiên?
*   **Vượt qua bẫy Single-scale:** Làm thế nào để tạo ra một thuật toán đạt giá trị tối thiểu ở cả hai cực đoan: hoàn toàn trật tự (perfectly predictable) và hoàn toàn ngẫu nhiên (uncorrelated random)?

## 1.2. Underlying Philosophy (Triết lý cốt lõi)
Sự chuyển dịch từ "Model-based" sang "Data-driven dynamics":
*   Không giả định cơ bản chất tất định (No deterministic assumption).
*   Không giả định cơ bản chất ngẫu nhiên (No stochastic assumption).
*   Không sử dụng mô hình tham số (No parametric model).
$\rightarrow$ **Mục tiêu:** So sánh trực tiếp độ phức tạp (Directly compare complexity) dựa trên sự phong phú của cấu trúc động lực học.

## 1.3. Motivation (Động lực nghiên cứu)
*   **Bản chất đa quy mô (Multiscale Nature):** Các hệ sinh học được điều hòa bởi mạng lưới tương tác đa tầng. Dao động sinh lý chứa đựng thông tin động lực học, không phải là nhiễu rác.
*   **Giả thuyết "Mất độ phức tạp" (Loss of Complexity Hypothesis):** Khả năng thích ứng của hệ sinh lý suy giảm do lão hóa/bệnh tật, dẫn đến sự suy sập thông tin trên nhiều thang đo.
*   **Thất bại của các phép đo cũ (Failure of Existing Measures):** Các thước đo truyền thống gán giá trị cao nhất cho nhiễu trắng và tín hiệu bệnh lý, đi ngược lại thực tế y sinh.
*   **Yêu cầu thực tiễn (Practical Complexity Measure):** Khoa học cần một thước đo hoạt động hiệu quả, ổn định trên các tín hiệu sinh lý có độ dài hữu hạn và chứa nhiễu (finite noisy physiologic signals).

## 1.4. Previous Methods & Limitations
*   **Trường phái Tất định (Định lý Takens):** Định lý Takens không sai, nhưng các *giả định* của nó (dữ liệu vô hạn, không có nhiễu, động lực học trơn) hoàn toàn sụp đổ trong môi trường sinh lý thực tế.
*   **Trường phái Ngẫu nhiên (Stochastic):** Thuộc tính thống kê không đồng nhất với cơ chế động lực học cốt lõi (Statistical properties $\neq$ Underlying mechanism).
*   **KS & ER Entropy:** ER entropy tiến tới vô cực đối với dữ liệu thực nghiệm, bởi vì một lượng nhiễu quan sát (observational noise) nhỏ tùy ý cũng có thể tạo ra vô số quỹ đạo phân biệt.
*   **ApEn & SampEn đơn dải:** Mắc kẹt ở góc nhìn *Single-scale*. Bỏ qua cấu trúc ở các thang thời gian lớn, dẫn đến việc đánh giá sai nhiễu trắng là phức tạp nhất.
*   **Đa thang đo của Zhang:** Đúng về mặt lý thuyết thông tin (Information theoretic) nhưng không khả thi trong thực tiễn (Not practical) do đòi hỏi lượng dữ liệu khổng lồ và không nhiễu.

## 1.5. Ứng dụng thực tiễn (Inference cho PPG)
*   Sự buồn ngủ làm suy giảm tương tác của mạng lưới ANS, dẫn đến sự suy sập cấu trúc đa quy mô của tín hiệu tim mạch. 
*   Trên tín hiệu PPG thực tế, nhiễu chuyển động (motion artifacts) sẽ làm biến dạng các ước lượng entropy (distort entropy estimates). Do đó, sự kết hợp giữa thuật toán ổn định và chiến lược tiền xử lý đúng đắn là bắt buộc.

---

**Kết luận:**
> Costa không phát minh ra một entropy mới; ông thay đổi câu hỏi nghiên cứu. Thay vì hỏi "chuỗi này ngẫu nhiên đến mức nào?", ông hỏi "cấu trúc động lực học của hệ được duy trì như thế nào trên nhiều thang thời gian?". Chính sự thay đổi câu hỏi này dẫn đến sự ra đời của Multiscale Entropy.


# 2. Thực nghiệm Lâm sàng: Động lực học Tim mạch (Costa et al., 2005)

## 2.1. Cơ sở dữ liệu và Tiền xử lý
*   **Healthy (72 subjects):** 128 Hz.
*   **CHF (43 subjects):** NYHA Class I-IV, 128-250 Hz.
*   **AF (9 subjects):** 250 Hz, đại diện cho loạn nhịp hỗn loạn.
*   **Tiền xử lý:** Lọc kỹ artifacts, tuy nhiên việc giữ lại các nhịp ngoại vị (PVCs) không làm thay đổi bản chất động lực học.

## 2.2. Hệ quy chiếu Thang đo (Scale Definition)
*   Costa không chọn mốc tùy ý mà dựa vào sinh lý học: **Scale 5** xấp xỉ một chu kỳ hô hấp trung bình.
*   **Scale nhỏ ($\le 5$):** Bị chi phối bởi dao động hô hấp và nhiễu.
*   **Scale lớn ($> 5$):** Phản ánh mạng lưới tương tác sinh lý nội tại.

## 2.3. Giải mã Động lực học 3 nhóm bệnh lý (Figure 5)
*   **Khỏe mạnh (Healthy):** Duy trì entropy cao xuyên suốt các thang đo. Phép coarse-graining đóng vai trò như bộ lọc triệt tiêu các dao động tuần hoàn (hô hấp - RSA), giúp hệ thống hiển lộ các tương tác dài hạn (long-range interaction).
*   **Suy tim sung huyết (CHF):** Tỉ số tín hiệu trên nhiễu (SNR) cực thấp. Sự biến mất của các thành phần nhiễu ngẫu nhiên ở các scale đầu tiên dẫn đến sự sụt giảm entropy cục bộ.
*   **Rung nhĩ (AF):** Đồ thị giảm đơn điệu hệt như nhiễu trắng. Dù mang tính ngẫu nhiên (randomness) cực đại ở scale 1, AF hoàn toàn thiếu vắng tính phức tạp cấu trúc (complexity) ở scale lớn.
*   **Chiến thắng của MSE:** Tại Scale 1: $AF > Healthy$ (Đánh giá sai lệch). Tại Scale lớn: $Healthy > AF$ (Trúng đích sinh học). Khỏe mạnh không thắng ở một điểm, mà thắng ở toàn bộ quỹ đạo duy trì độ phức tạp.

## 2.4. Khả năng Thích ứng Động (Dynamic Adaptability - Figure 6 & 7)
Mục tiêu cốt lõi của Costa khi phân tích Chu kỳ Thức/Ngủ không phải là xem "entropy tăng hay giảm", mà là đo lường **Khả năng tái tổ chức động lực học**:
*   **Khỏe mạnh:** Thay đổi hoàn toàn hình thái đường cong MSE giữa Thức và Ngủ, chứng tỏ khả năng linh hoạt thích ứng với môi trường.
*   **CHF:** Mất hoàn toàn khả năng định chuẩn lại (reorganize). Đường cong chỉ dịch chuyển song song trị số (shift), cấu trúc động lực học hoàn toàn đóng băng.

## 2.5. Ứng dụng Kỹ thuật & Trích xuất Đặc trưng (Figure 8)
*   Costa chuyển từ phân tích đồ thị (curve) sang bài toán phân loại (classification/ML). 
*   Đặc trưng trích xuất: Tổng diện tích dưới đường cong (Area/AUC) cho dải ngắn hạn và dài hạn, cho phép phân tách hoàn hảo nhóm Healthy và CHF.

---

> **Phát hiện quan trọng nhất của phần thực nghiệm (Core Experimental Finding)**
>
> Thông tin chẩn đoán không nằm ở một giá trị entropy đơn lẻ.
> 
> Nó nằm trong toàn bộ quá trình tiến hóa của entropy theo các thang thời gian.
> 
> Do đó, MSE phải được xem như một **"dynamic signature"** (chữ ký động lực học) của hệ sinh lý, chứ không phải một chỉ số vô hướng đơn điểm.

---

### Khung Tư duy Hệ thống NTSA (NTSA Systemic Framework)
Toàn bộ hành trình từ Fraser đến Costa định hình một framework phân tích nhất quán:
1.  **Fraser (Phase Space):** Trả lời câu hỏi *"Ở đâu?"* (Where are the dynamics?)
2.  **Richman (Sample Entropy):** Trả lời câu hỏi *"Đo cái gì?"* (How do we estimate unpredictability locally?)
3.  **Costa (Multiscale):** Trả lời câu hỏi *"Đo trên bao nhiêu quy mô?"* (Across which temporal scales to evaluate full complexity?)


# 5. Triết lý Thiết kế Thực nghiệm: Methodological Principle

## 5.1. Vấn đề cốt lõi: Transition destroys stationarity
*   **Giới hạn của dữ liệu liên tục:** Thuật toán MSE yêu cầu tính dừng (stationarity) tương đối trong đoạn dữ liệu được phân tích. Các giai đoạn chuyển pha (Ví dụ: Wake $\rightarrow$ Sleep, hoặc Alert $\rightarrow$ Microsleep) chứa sự thay đổi đồng thời của nhiều cơ chế sinh lý (ANS, nhịp thở, v.v.), tạo ra hệ phi dừng (nonstationary).
*   **Rủi ro hỗn hợp (Mixed Dynamics):** Nếu tính MSE xuyên suốt một giai đoạn chuyển tiếp, sự thay đổi của entropy sẽ bị lẫn lộn giữa *bản chất của trạng thái mới* và *nhiễu do quá trình chuyển đổi*.

## 5.2. Giải pháp: Isolate Canonical States
*   Thay vì phân tích toàn bộ chuỗi dài, Costa cắt lấy **đoạn đại diện điển hình nhất** (Canonical Wake vs. Canonical Sleep).
*   **Mục đích:** Cách ly (isolate) hoàn toàn động lực học nội tại của các trạng thái sinh lý ổn định (State A vs. State B), loại bỏ các biến số gây nhiễu từ giai đoạn chuyển tiếp.

## 5.3. Chiến lược Áp dụng cho Nghiên cứu PPG-based Drowsiness
Dựa trên triết lý này, dự án hoàn toàn có thể được cấu trúc thành lộ trình 2 giai đoạn (2 papers) cực kỳ chặt chẽ về mặt khoa học:

*   **Phase 1 (Khám phá Động lực học): Characterize Canonical States**
    *   **Dữ liệu:** Lấy các đoạn thuần túy (VD: 15 phút hoàn toàn Alert vs. 15 phút Severe Drowsy). Bỏ qua giai đoạn chuyển tiếp.
    *   **Mục tiêu:** Trả lời câu hỏi "What changes?". Tìm kiếm các *dynamic signatures* tối ưu (MSE, DFA, Recurrence) mà không cần bận tâm đến Machine Learning hay xử lý online.
    *   **Justification:** *“Following the experimental philosophy of Costa et al., we intentionally excluded transition periods and analyzed only representative alert and drowsy epochs. This design isolates the intrinsic dynamics...”*

*   **Phase 2 (Ứng dụng Kỹ thuật): Real-time Transition Detection**
    *   **Dữ liệu:** Dữ liệu liên tục theo thời gian thực (Continuous monitoring).
    *   **Mục tiêu:** Khi đã nắm trong tay các "signature" tối ưu từ Phase 1, bài toán lúc này chuyển sang: Sử dụng cửa sổ trượt (Sliding Window) để trả lời câu hỏi *"How early can we detect the transition?"* phục vụ cảnh báo sớm.
*   

# 6. Tóm tắt: Các Giả định và Hạn chế của MSE

## 1. Assumptions (Các giả định cốt lõi)
*   **Tính dừng (Stationarity):** Chuỗi thời gian không được chứa các xu hướng vĩ mô (trends) hay biến động nền để đảm bảo độ ổn định thống kê của thuật toán.
*   **Tính nhất quán của dải dung sai ($r$):** Tham số $r$ phải được tính từ độ lệch chuẩn (SD) của chuỗi gốc (tại scale 1) và **cố định cho mọi scale**. Điều này đảm bảo sự thay đổi phương sai phản ánh đúng động lực học tự nhiên, không phải do sai lệch thước đo.
*   **Độ dài dữ liệu ($N$):** Chuỗi đầu vào phải đủ lớn để các chuỗi con sau khi rút gọn (coarse-graining) vẫn duy trì độ tin cậy thống kê.
*   **Sự hội tụ thuật toán:** Giả định sai số nội tại của thuật toán là cực nhỏ (dưới 1% với $m=2, r=0.15$), do đó các biến thiên quan sát được là hệ quả của cơ chế sinh học hoặc sai số thực nghiệm.

## 2. Limitations (Các hạn chế kỹ thuật)
*   **Phụ thuộc vào độ dài dữ liệu:** Chuỗi ngắn làm tăng đột biến sai số (đặc biệt với nhiễu $1/f$, sai số lên tới 12% ở $N=1000$), phá vỡ tính nhất quán của phép đo.
*   **Nhạy cảm với xu hướng phi dừng:** Xu hướng trôi dốc làm hỏng việc tính toán SD và dung sai $r$. Tuy nhiên, áp dụng các bộ lọc khử xu hướng (detrending) lại mang rủi ro tiêu diệt cấu trúc đa thang đo bản chất của tín hiệu.
*   **Giới hạn đánh giá ở trạng thái căng thẳng:** MSE đo lường tối ưu ở điều kiện tự do (free-running). Dưới các tác nhân gây căng thẳng, không gian trạng thái bị thu hẹp dẫn đến độ phức tạp giảm sút biểu kiến.
*   **Nhiễu giả tạo trên chuỗi rời rạc:** Phép coarse-graining trên dữ liệu rời rạc (ví dụ: DNA) sinh ra hiệu ứng nhiễu răng cưa, bắt buộc phải có bước xử lý chuyển đổi liên tục hoặc chọn lọc scale khắt khe.
*   

# 7. My Research: Ứng dụng MSE cho PPG-based Drowsiness Detection

## 7.1. Research Ideas (Ý tưởng Nghiên cứu)
*   **Xác định "Lộ trình Động lực học" (Dynamical Routes):** Dùng đồ thị MSE để giải mã tín hiệu PPG khi buồn ngủ sẽ chuyển dịch theo kịch bản nào:
    *   *Route 1 (Đều đặn hóa):* Ức chế thần kinh làm nhịp tim trở nên đều đặn, đơn điệu.
    *   *Route 2 (Hỗn loạn hóa):* Xung đột giữa vi giấc ngủ (microsleep) và các pha giật mình (micro-arousals) tạo ra nhiễu ngẫu nhiên, vô hướng.
*   **Lượng hóa Sự suy giảm Thích ứng (Reduced Adaptive Capacity):** Biến sự sụt giảm của quỹ đạo MSE thành thước đo trực tiếp, theo thời gian thực đánh giá mức độ suy thoái khả năng phản xạ và điều hòa của hệ thần kinh tự chủ (ANS).

## 7.2. Knowledge Contributions (Đóng góp Tri thức)
*   **Phá vỡ giới hạn Entropy Đơn thang đo:** Bác bỏ phương pháp đánh giá "độ đều đặn" thô sơ (ApEn/SampEn tại scale 1). Chứng minh thông tin chẩn đoán cốt lõi nằm ở cấu trúc liên kết đa quy mô của PPG.
*   **Mở rộng Thuyết "Complexity-Loss":** Tiên phong chứng minh sự sụp đổ độ phức tạp không chỉ xuất hiện ở bệnh lý/lão hóa mãn tính, mà còn xảy ra ở một trạng thái nhận thức chuyển tiếp, tạm thời (transient cognitive state) như sự mệt mỏi/thiếu ngủ.
*   **Nâng tầm Tín hiệu PPG:** Hợp thức hóa PPG không chỉ là dao động cơ học để đếm nhịp tim, mà là một hệ thống mang cấu trúc thông tin phân tầng sinh học tinh vi.
*   

# 8. Cẩm nang Thực chiến Xử lý PPG: Tính Robustness của MSE (Appendix B)

Phần này không liệt kê thuật toán theo hướng "hiện tượng $\rightarrow$ giải pháp", mà phân tích theo triết lý "nguyên nhân $\rightarrow$ cơ chế $\rightarrow$ hệ quả" để hiểu rõ *tại sao* mỗi quyết định trong pipeline lại được đưa ra. 

## 8.1. Độ dài dữ liệu ($N$)
*   **Core Insight:** Chuỗi coarse-grained không phải là một đoạn cắt ngắn (subset) của chuỗi gốc. Nó là chuỗi tổng hợp (aggregation) chứa thông tin tích lũy của toàn bộ tín hiệu. $\rightarrow$ Vì vậy, MSE ít nhạy cảm với việc giảm chiều dài dữ liệu hơn là thuật toán SampEn đơn thuần.
*   **Practical Guideline:** Dữ liệu ngắn làm sai số thống kê tăng nhanh (đặc biệt với tín hiệu có tương quan dài hạn như $1/f$). Tuy nhiên, nhờ cơ chế bảo toàn thông tin của coarse-graining, bạn chỉ cần duy trì độ dài cửa sổ khoảng $N = 1000 - 2000$ điểm (15-30 phút PPG) là đủ để giữ vững tính nhất quán tương đối của đồ thị đến scale $\tau = 10$.

## 8.2. Nhiễu trắng chồng chập (White Noise / ADC Noise)
*   **Core Insight:** Nhiễu trắng ngẫu nhiên chỉ thống trị ở các scale nhỏ. Phép toán coarse-graining thực chất hoạt động như một bộ lọc thông thấp (low-pass filter) tự nhiên. $\rightarrow$ Khi scale tăng, ảnh hưởng của white noise giảm nhanh hơn rất nhiều so với ảnh hưởng của các tương quan dài hạn (động lực học bản chất).
*   **Practical Guideline:** Nếu tín hiệu PPG có SNR (tỷ lệ tín hiệu/nhiễu) thấp, hãy ưu tiên trích xuất đặc trưng và phân tích ở các scale lớn, nơi nhiễu cao tần đã được coarse-graining làm suy giảm đáng kể.

## 8.3. Điểm dị thường (Outliers / Motion Artifacts)
*   **Core Insight:** Outlier (như nhiễu chuyển động biên độ lớn) *không* trực tiếp phá hỏng cấu trúc động lực học cốt lõi của chuỗi. Outlier chỉ phá hỏng việc ước lượng độ lệch chuẩn (SD), từ đó làm phình to tham số dung sai $r$. $\rightarrow$ Hệ quả là làm sai lệch hoàn toàn thống kê so khớp (matching statistics), kéo sụt đồ thị MSE một cách giả tạo.
*   **The Trick (Costa Trick):** Không cần các thuật toán tái tạo/nội suy phức tạp, chỉ cần:
    1.  Lọc ngưỡng (Artifact Detection) để tạo ra chuỗi sạch tạm thời.
    2.  Estimate $r$ từ chuỗi sạch này ($r_{clean} = 0.15 \times SD_{clean}$).
    3.  **Run MSE on Original Signal:** Áp dụng tham số $r_{clean}$ để chạy MSE trên *chính chuỗi PPG thô ban đầu*. Đồ thị sẽ tự hội tụ chuẩn xác.

## 8.4. Tần số lấy mẫu hữu hạn (Sampling Frequency)
*   **Core Insight:** Sai số định vị thời gian (do tần số lấy mẫu thấp tạo ra) thực chất chỉ nằm ở hai đầu mút của cửa sổ coarse-graining. Khi tính trung bình, sai số này được chia đều cho $\tau$. $\rightarrow$ Scale $\tau$ càng lớn, thuật toán càng ít nhạy cảm với giới hạn của tần số lấy mẫu.
*   **Practical Guideline:** Sai số định vị sẽ khiến SampEn bị đánh giá thấp ở scale 1, nhưng độ chính xác sẽ tự động hội tụ và bù đắp ở các scale tiếp theo.

---

## 8.5. Robustness Summary
Costa không chứng minh MSE hoàn toàn miễn nhiễm với nhiễu. Ông chứng minh một bức tranh thực tế hơn rất nhiều:
*   **Noise** chỉ ảnh hưởng ở scale nhỏ.
*   **Outlier** chủ yếu làm sai tham số $r$.
*   **Sampling frequency** ảnh hưởng ít dần theo scale.
*   **Coarse-graining** bảo toàn nhiều thông tin hơn việc chỉ cắt ngắn tín hiệu.
$\rightarrow$ **Kết luận:** MSE là một framework có khả năng chống chịu (robust) cực tốt, hoàn toàn phù hợp để triển khai trên các điều kiện đo lường không lý tưởng của thiết bị đeo thực tế (wearables).

---

## 8.6. Pipeline Xử lý PPG Thực chiến

Dựa trên các insight trên, kiến trúc xử lý tín hiệu hoàn chỉnh cho dự án được thiết kế như sau:

```text
[Raw PPG] 
   │
   ├──> Artifact Detection (Only estimate SD_clean)
   │
   ├──> Estimate r (r = 0.15 * SD_clean)
   │
   ├──> Run MSE on ORIGINAL SIGNAL (using estimated r)
   │
   ├──> Multiscale Curve (Bỏ qua nhiễu ở các scale nhỏ)
   │
   ├──> Dynamic Features (AUC, Slope, Plateau tại các scale lớn)
   │
   └──> Statistical Analysis / ML Classifier