### Paper Metadata
*   **Title:** Recurrence-plot-based measures of complexity and their application to heart-rate-variability data
*   **Authors:** Norbert Marwan, Niels Wessel, Udo Meyerfeldt, Alexander Schirdewan, and Jürgen Kurths
*   **Year:** 2002
*   **Keywords:** recurrence plots, measures of complexity, heart-rate variability (HRV), logistic map, laminar states, chaos-chaos transitions

# 1. Why

## Research Question
Làm thế nào để phát hiện và lượng hóa các trạng thái phiến (laminar states) cùng các bước chuyển pha hỗn loạn - hỗn loạn (chaos-chaos transitions) trên các chuỗi dữ liệu thực nghiệm ngắn và phi dừng?

## Motivation
*   **Bản chất hệ thống phức tạp:** Các hệ tự nhiên liên tục chuyển pha giữa các trạng thái tuần hoàn, laminar và hỗn loạn. Hiểu được các chuyển pha này là chìa khóa để giải mã cơ chế vận hành của hệ thống.
*   **Nghịch lý dữ liệu thực nghiệm:** Dữ liệu thực tế thường rất ngắn, làm vô hiệu hóa các phương pháp phân tích phi tuyến truyền thống và có thể dẫn đến cạm bẫy khoa học nếu áp dụng thiếu phê phán.
*   **Khai thác triệt để ngôn ngữ hình học của RP:** Các cấu trúc hình học khác nhau trong Biểu đồ hồi quy (RP) phản ánh những khía cạnh động lực học khác nhau. Việc RP không chỉ có đường chéo mà còn có các đường dọc/ngang đặt ra nhu cầu phải khai thác toàn diện các cấu trúc này.
*   **Khoảng trống của RQA truyền thống:** RQA cổ điển hoạt động xuất sắc trong việc dùng đường chéo để phát hiện điểm phân nhánh, nhưng thông tin chứa trong các cấu trúc dọc lại chưa được khai thác. Điều này khiến RQA truyền thống không thể nhận diện các trạng thái laminar và chuyển pha chaos-chaos.
*   **Tiềm năng ứng dụng sinh lý học:** Việc hiểu rõ động lực học thông qua các phép đo mới cho phép ứng dụng vào dữ liệu biến thiên nhịp tim (HRV), mở ra khả năng nhận diện các pha laminar để dự báo sớm những cơn loạn nhịp tim đe dọa tính mạng.

## Previous Methods
*   **Phân tích tuyến tính:** Thường không đủ năng lực để mô tả các quá trình phi tuyến phức tạp.
*   **Phi tuyến cổ điển (Lyapunov, Fractal Dimensions):** Vấp phải rào cản do "lời nguyền số chiều" và yêu cầu chuỗi quan sát phải cực kỳ dài.
*   **Động lực học ký hiệu (Symbolic Dynamics):** Các phương pháp (như Renyi entropies) tỏ ra hiệu quả trong việc mô phỏng dữ liệu tự nhiên nhưng mang một lăng kính tiếp cận khác.
*   **RQA truyền thống (Webber & Zbilut):** Vượt qua được rào cản dữ liệu ngắn và phát hiện tốt các chuyển pha dựa trên đường chéo, nhưng thất bại trong việc phát hiện chuyển pha chaos-chaos do bỏ qua các cấu trúc dọc.

#  2. Measures of Complexity: Ý nghĩa Toán học và Vật lý Phi tuyến

Đóng góp cốt lõi của Marwan (2002) không chỉ là đề xuất các công thức mới, mà là việc tái định nghĩa cách chúng ta "đọc" hình học không gian pha bằng một đối tượng thống kê trung tâm mới, tạo tiền đề toán học vững chắc cho việc nghiên cứu động lực học chuyển pha (transition dynamics) trong các tín hiệu sinh lý phi dừng.

#### 2.1. Đối tượng thống kê trung tâm: $P(v)$
Giống như Webber (1994) thống kê chiều dài đường chéo thành phân bố $P(l)$ để đại diện cho toàn bộ cấu trúc tiến hóa, Marwan (2002) xây dựng $P(v)$ làm phân bố xác suất chiều dài các đường dọc. $P(v)$ không còn là mô tả của một trạng thái đơn lẻ, mà là một **đối tượng thống kê mô tả toàn bộ mức độ lưu trú (persistence) của hệ thống**. 

Để trích xuất $P(v)$, phương pháp lọc các điểm hồi quy cô lập để giữ lại cấu trúc dọc thực sự ($s_i$):
$$s_i := \{\vec{x}_l \in S_i : (R_{i,l} \cdot R_{i,l+1}) + (R_{i,l} \cdot R_{i,l-1}) > 0\}$$

Mọi chỉ số (LAM, TT, $V_{max}$) thực chất chỉ là các hàm phiếm (functional) được trích xuất từ phân bố $P(v)$ này.

#### 2.2. Hệ thống ba chỉ số cấu trúc dọc
Ba chỉ số của Marwan giải quyết ba câu hỏi hoàn toàn độc lập về động lực học lưu trú của hệ thống:

*   **Laminarity ($\Lambda$)**: Đo lường xác suất $P$ để một recurrence point thuộc về một trạng thái laminar hợp lệ ($v \ge v_{min}$). Về mặt vật lý, nó cho biết hệ thống có thường xuyên rơi vào trạng thái bế tắc (laminar) hay không.
    $$\Lambda := \frac{\sum_{v=v_{min}}^N vP(v)}{\sum_{v=1}^N vP(v)}$$

*   **Trapping Time ($T$)**: Là kỳ vọng toán học $E[v]$ (trung bình cộng có trọng số) của phân bố $P(v)$. Nó đại diện cho thời gian trung bình mỗi lần hệ thống bị "bẫy" lại tại một trạng thái không gian pha trước khi thoát ra.
    $$T := \frac{\sum_{v=v_{min}}^N vP(v)}{\sum_{v=v_{min}}^N P(v)}$$

*   **Maximal Vertical ($V_{max}$)**: Là maximum order statistic của phân bố $P(v)$. Đại lượng cực kỳ nhạy bén này đo lường pha laminar dài nhất từng xuất hiện (longest residence), lý tưởng để phân tích hiện tượng gián đoạn (intermittency).
    $$V_{max} = \max(\{v_l; l=1, 2, \dots, L\})$$

#### 2.3. Triết lý đối ngẫu: Chuyển dịch mô hình (Paradigm Shift)
Việc Marwan (2002) bổ sung các cấu trúc dọc đã biến Recurrence Plot thành một không gian hoàn thiện, kết hợp hoàn hảo giữa hai lăng kính trực giao: nghiên cứu sự tiến hóa và nghiên cứu sự lưu trú. Sự đối ngẫu này chính là nền tảng cốt lõi để phân tích "Động lực học của các Đặc trưng" (Dynamics of Dynamics) khi áp dụng cửa sổ trượt.

| | Webber (1994) | Marwan (2002) |
| :--- | :--- | :--- |
| **Động lực học** | Dynamics of Evolution (Sự tiến hóa) | Dynamics of Residence (Sự lưu trú) |
| **Đối tượng thống kê** | Phân bố đường chéo $P(l)$ | Phân bố đường dọc $P(v)$ |
| **Functional** | `%DET`, `ENT`, $L_{max}$ | $\Lambda$, $T$, $V_{max}$ |
| **Bản chất đo lường**| Sự lặp lại của quỹ đạo tiến hóa. | Sự lưu trú / mắc kẹt của trạng thái. |
| **Câu hỏi triết học** | *Nếu hệ quay lại trạng thái cũ, tương lai có lặp lại không?* | *Khi hệ đến một trạng thái, nó ở lại bao lâu trước khi thay đổi?* |



# 3. How

**Triết lý cốt lõi:** Đóng góp cốt lõi của Marwan et al. (2002) không nằm ở việc thay đổi quy trình xây dựng Recurrence Plot, mà ở việc thay đổi đối tượng hình học được thống kê từ các cấu trúc đường chéo sang các cấu trúc đường dọc, qua đó mở rộng RQA từ phân tích evolution sang phân tích persistence[cite: 1].

## 3.1 Algorithm
Thuật toán kế thừa quy trình xây dựng RP của Webber & Zbilut (1994)[cite: 1]:
1.  **Phase-space Reconstruction:** Xây dựng vector trạng thái từ chuỗi thời gian đơn biến.
2.  **Recurrence Plot:** Tính ma trận khoảng cách và nhị phân hóa bằng ngưỡng $\varepsilon$[cite: 1].
3.  **Vertical Line Extraction:** Trích xuất tất cả các đường dọc liên tiếp trên từng cột của RP để thu được tập độ dài $v$[cite: 1]. Các chỉ số Laminarity và Trapping Time chỉ sử dụng các đường có $v \ge v_{min}$[cite: 1].
4.  **Distribution $P(v)$:** Xây dựng $P(v)$ là phân bố chiều dài của toàn bộ các cấu trúc dọc trong RP[cite: 1].
5.  **Quantification:** Lần lượt tính ba chỉ số cấu trúc dọc: Laminarity ($\Lambda$), Trapping Time ($T$) và Maximal Vertical Length ($V_{max}$)[cite: 1].

## 3.2 Mathematical Formulation

**Phase-space reconstruction:**
$$\mathbf{x}_i = [u_i, u_{i+\tau}, \ldots, u_{i+(m-1)\tau}]$$

**Recurrence Plot:**
$$R_{i,j} = \Theta(\varepsilon - \Vert{}\mathbf{x}_i - \mathbf{x}_j\Vert{})$$

**Vertical Line Distribution ($P(v)$):**
Đường dọc độ dài $v$ là chuỗi liên tiếp $R_{i,j}=1$ trên cùng một cột[cite: 1]. $P(v)$ thống kê toàn bộ phân bố chiều dài này[cite: 1].

**Laminarity ($\Lambda$):**
Tỷ lệ recurrence points thuộc các vertical structures có ý nghĩa[cite: 1]:
$$\Lambda = \frac{\sum_{v=v_{min}}^{N} vP(v)}{\sum_{v=1}^{N} vP(v)}$$

**Trapping Time ($T$):**
Kỳ vọng toán học (expected value) của chiều dài đường dọc[cite: 1]:
$$T = \frac{\sum_{v=v_{min}}^{N} vP(v)}{\sum_{v=v_{min}}^{N} P(v)}$$

**Maximal Vertical Length ($V_{max}$):**
Giá trị cực đại của phân bố $P(v)$, tương ứng với pha laminar dài nhất[cite: 1]:
$$V_{max} = \max(v)$$

## 3.3 End-to-End Pipeline
The only conceptual change nằm ở bước trích xuất hình học:


Raw Time Series
       │
       ▼
Phase-space Reconstruction
       │
       ▼
Distance Matrix
       │
       ▼
Recurrence Matrix
       │
       ▼
Geometry Extraction
       │
       ├────────► Diagonal Structures (Webber, 1994)
       │                │
       │                ▼
       │              P(l)
       │                │
       │                ▼
       │        DET • ENT • Lmax
       │
       └────────► Vertical Structures (Marwan, 2002)
                        │
                        ▼
                      P(v)
                        │
                        ▼
                LAM • TT • Vmax



## 3.4 Computational Complexity

Độ phức tạp giữ nguyên so với RQA cổ điển:

* **Time Complexity:** $O(N^2m)$ (Chi phối bởi bước tính Distance Matrix).
* **Space Complexity:** $O(N^2)$ (Lưu trữ Distance/Recurrence Matrix).

## 3.5 Implementation Notes

* **Tái sử dụng Framework:** Vertical scan có thể tái sử dụng toàn bộ framework của Diagonal scan chỉ bằng cách thay đổi hướng quét (transpose matrix hoặc quét theo cột).
* **Thuật toán đếm:** Sử dụng RLE (Run-Length Encoding) hoặc `np.diff` dọc theo các cột để đếm chiều dài hiệu quả.
* **Data Type Safety:** Ép kiểu Recurrence Matrix (`bool` hoặc `uint8`) về `int32` trước khi dùng `np.diff` để tránh lỗi underflow và đảm bảo phát hiện chính xác các điểm bắt đầu/kết thúc.
* **Guard Clauses:** Phải xử lý trường hợp biên bằng cách trả về $0.0$ nếu không có đường dọc nào đạt $v \ge v_{min}$ để ngăn lỗi `ZeroDivisionError` khi tính $\Lambda$ và $T$.


# 4. Experiments

## - Setups
*   **Benchmark Ground Truth:** Sử dụng bản đồ Logistic ($x_{n+1} = a x_n(1 - x_n)$) làm hệ quy chiếu toán học có đáp án lý thuyết đã biết để kiểm chứng khả năng phát hiện chuyển pha của các chỉ số RQA mới.
*   **Dải tham số:** Khảo sát $a \in [3.5, 4.0]$ với $\Delta a = 0.0005$; loại bỏ 1000 bước lặp đầu tiên (transients) để quỹ đạo thực sự ổn định.
*   **Không gian pha:** Thiết lập chiều nhúng $m=1$ (do Logistic map vốn là hệ động lực một chiều), độ trễ $\tau=1$, và ngưỡng bán kính $\epsilon=0.1\sigma$.

## - Results
*   **Phân tích trực quan (Hình 2):**
        *   Trạng thái tuần hoàn ($a=3.830$): RP được chi phối bởi các đường chéo đều đặn; các cấu trúc dọc gần như không xuất hiện.
        *   Trạng thái laminar/gộp băng ($a=3.679$): RP bị chiếm giữ bởi các khối đen đặc kéo dài theo chiều dọc và ngang, minh họa rõ nét sự lưu trú.
        *   Trạng thái hỗn loạn hoàn toàn ($a=4.000$): RP đồng nhất, chứa chủ yếu điểm cô lập, vắng bóng các cấu trúc vạch.
*   **Phân tích định lượng (Hình 3):**
        *   **RQA truyền thống:** Các chỉ số $\Delta$ và $L_{max}$ tạo đỉnh ở các cửa sổ tuần hoàn nhưng hoàn toàn phẳng lặng (bị "mù") tại các giao điểm siêu quỹ đạo (chaos-chaos transitions).
        *   **RQA đề xuất:** Các chỉ số $\Lambda$, $T$, và $V_{max}$ triệt tiêu tại các pha tuần hoàn do không tồn tại trạng thái laminar, nhưng bứt phá tạo thành các đỉnh sắc nét trùng khớp tuyệt đối với các mốc chuyển pha hỗn loạn - hỗn loạn.
        *   **Hiện tượng nhảy băng:** Tại vùng $a < 3.678$, quỹ đạo phải nhảy liên tục giữa hai băng hỗn loạn khiến hệ không thể lưu trú, dẫn đến $T$ và $V_{max}$ triệt tiêu về 0.

## - Discussion
*   **Mở rộng không gian thông tin:** Đóng góp quan trọng nhất của phương pháp không nằm ở việc thay thế các chỉ số cũ, mà ở việc khai phá một chiều thông tin động lực học hoàn toàn mới bị bỏ ngỏ trong RQA cổ điển.
*   **Bổ sung thay vì cạnh tranh:** Bài báo không chứng minh $\Lambda > DET$. Thực chất, $DET$ đo lường khả năng dự báo (Predictability), còn $\Lambda$ đo lường khả năng lưu trú (Persistence). Chúng là hai thước đo trực giao và bổ trợ hoàn hảo cho nhau.
*   **Mã hóa động lực học qua hình học:** Hình học của RP không chỉ là biểu diễn trực quan, mà bản thân các hình thái khác nhau (chéo, dọc) đã trực tiếp mã hóa các cơ chế động lực khác biệt của hệ thống.
*   **Paradigm Shift:** Thực nghiệm chứng minh việc chuyển đổi đối tượng thống kê từ phân bố đường chéo $P(l)$ sang phân bố đường dọc $P(v)$ đã mở rộng trọn vẹn lăng kính của RQA từ cơ chế tiến hóa (evolution) sang cơ chế lưu trú (laminarity) của hệ động lực.

## - Clinical Application (HRV & VT Prediction)
*   **Thiết lập thực nghiệm:** Phân tích dữ liệu biến thiên nhịp tim (HRV) gồm 1000 nhịp từ máy khử rung tim (ICD) của bệnh nhân suy tim, so sánh giữa trạng thái kiểm soát (Control) và ngay trước cơn loạn nhịp thất (Before VT), với $m=6, \tau=1, \epsilon=110$ ms[cite: 1].
*   **Biểu hiện trực quan (Hình 4):**
    *   *Trạng thái Control:* Nhịp tim biến thiên linh hoạt (600-900 ms), RP thông thoáng với các khối đen nhỏ ($V_{max} = 117$), thể hiện cơ chế "hỗn loạn lành mạnh" và không bị mắc kẹt[cite: 1].
    *   *Trạng thái Before VT:* Nhịp tim suy giảm biến thiên, đập phẳng lặng đơn điệu[cite: 1]. RP bị thống trị bởi các khối chữ nhật đen khổng lồ ($V_{max} = 242$), chứng tỏ quỹ đạo bị "bẫy" vào các pha laminar kéo dài do mất đi sự phức tạp động lực học trước khi sụp đổ[cite: 1].
*   **Sức mạnh thống kê (Bảng I):** Trong khi RQA chéo ($L_{max}$) thất bại trong việc phân biệt hai nhóm ở chiều nhúng thấp ($p > 0.05$ tại $m=3$), RQA dọc ($V_{max}$) bộc lộ độ nhạy bén vượt trội với mức ý nghĩa thống kê cực kỳ mạnh mẽ (**, $p < 0.01$) tại các chiều nhúng cao ($m=6, 9, 12$)[cite: 1].
*   **Mở rộng phân tích chuyển pha sinh lý:** Bản chất của sự xuất hiện các khối chữ nhật đen là chỉ báo vật lý cho sự suy kiệt cơ chế tự điều hòa[cite: 1]. Quá trình chuyển pha hỗn loạn - hỗn loạn này mang cơ chế tương đồng với sự dịch chuyển từ trạng thái tỉnh táo sang buồn ngủ, khi hệ thần kinh tự chủ bị ức chế[cite: 1]. Bằng cách áp dụng cửa sổ trượt trực tiếp lên chuỗi tín hiệu quang thể tích (PPG), sự đột biến của các chỉ số cấu trúc dọc như Laminarity và Trapping Time sẽ đóng vai trò như một bộ kích hoạt (trigger) nhạy bén, cho phép phát hiện sớm các pha laminar sinh lý để cảnh báo trạng thái ngủ gật thời gian thực[cite: 1].