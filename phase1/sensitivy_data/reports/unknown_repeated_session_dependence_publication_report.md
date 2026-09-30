# Phân tích độ nhạy đối với sự phụ thuộc giữa các phiên đo lặp lại chưa xác định

*Báo cáo định hướng công bố cho nghiên cứu “Ultra-Short PPG Dynamics Across the Wakefulness-to-Drowsiness Transition: A Nonlinear Time-Series Analysis” (tạp chí dự kiến: Chaos, Solitons & Fractals).* Trong toàn bộ báo cáo, chênh lệch ghép cặp được định nghĩa là \(\Delta=\mathrm{Drowsy}-\mathrm{Awake}\). Các số liệu lấy từ [phân tích độ nhạy đã đóng băng](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_results.md); [hồ sơ phương pháp](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_method.md) và [manifest](../../sensitivy_data/unknown_repeated_session_dependence_v1/manifest.json) cung cấp thông tin để tái lập.

## 1. Động cơ và vấn đề suy luận thống kê

Nghiên cứu gồm 20 phiên đo của 10 người trưởng thành trẻ, khỏe mạnh; theo thiết kế thu nhận ban đầu, mỗi người có hai phiên. Tuy nhiên, hiện không còn thông tin liên kết người tham gia với phiên đo. Mỗi phiên cung cấp một cặp giá trị Awake và Drowsy, nhưng xem cả 20 phiên là các đơn vị suy luận độc lập có thể đánh giá thấp độ bất định nếu hai phiên của cùng một người có tương quan. Nguy cơ lặp đơn vị quan sát trong suy luận này đòi hỏi một phân tích độ nhạy. Phân tích xem xét liệu chiều và độ lớn của các hiệu ứng chính có duy trì khi gộp phiên thành những *cụm hai phiên giả định* hay không; nó không xác định các cặp thực tế và không ước lượng tương quan giữa các phiên của cùng một người.

## 2. Thiết kế phân tích độ nhạy

Hai mươi phiên, được sắp theo mã số tăng dần, được phân thành mười cụm hai phiên giả định không chồng lấn. Trong mỗi cụm, hai chênh lệch ở cấp phiên được lấy trung bình số học: \(\Delta_k^*=(\Delta_i+\Delta_j)/2\). Thuật toán hoán vị với seed định trước lấy mẫu có hoàn lại 100.000 cách ghép cặp hoàn hảo từ 654.729.075 cách có thể; 99.990 cách là duy nhất (tỷ lệ lặp 0,010000%). Mọi lần rút, kể cả các cách ghép trùng, đều được giữ trong thống kê tổng hợp. Với từng cách ghép và từng metric trong bảy metric, phân tích tính trung vị của mười giá trị \(\Delta_k^*\), số cụm có chiều hiệu ứng kỳ vọng, tương quan rank-biserial cho dữ liệu ghép cặp (\(r_{rb}\)), giá trị \(p\) của kiểm định Wilcoxon signed-rank hai phía dạng exact và giá trị \(q_{BH}\) điều chỉnh Benjamini–Hochberg đồng thời trên bảy metric. Giá trị có trị tuyệt đối không quá \(10^{-12}\) được coi là 0; các trị tuyệt đối khác 0 bị trùng nhận thứ hạng trung bình. Không thực hiện bootstrap lồng trong mỗi lần ghép cặp.

Các phân vị 2,5–97,5% phản ánh sự biến thiên **giữa các cách ghép giả định**. Chúng không phải khoảng tin cậy bootstrap hay khoảng tin cậy của hiệu ứng ở cấp người tham gia. Mười cụm là cấu trúc giả định cho phân tích độ nhạy, không phải các nhóm người tham gia đã được quan sát.

## 3. Kiểm chứng kết quả gốc

Trước khi tạo bất kỳ cách ghép giả định nào, đầu vào canonical gồm 20 phiên đã tái hiện các kết quả Wilcoxon signed-rank chính sau hiệu chỉnh và phép điều chỉnh BH trên bảy metric. Mean CC và Mean NRMSE dùng cách gộp Simplex bắt đầu từ *window*: CC hoặc NRMSE được tính ở từng prediction horizon trong mỗi window; 18 giá trị horizon được lấy trung bình để có giá trị của window; sau đó lấy trung vị các window hợp lệ trong từng phiên và trạng thái. Các kết quả đã sửa này thay thế giá trị prediction cũ, vốn được tính bằng cách lấy trung bình các trung vị window riêng theo từng horizon. Năm metric còn lại giữ định nghĩa đã thẩm định ở cấp phiên cho nhánh P0, Processed, cửa sổ 60 giây. [Đầu vào canonical](../../sensitivy_data/unknown_repeated_session_dependence_v1/canonical_20_session_7metric_P0_60s_v1.csv) có SHA-256 `3cdc90d0bf214244fcced56a44a692bd941432352837fe285d31be0c9f375286`.

| Metric | Trung vị \(\Delta\), n=20 | \(p\) hai phía | \(r_{rb}\) | \(q_{BH}\) |
| --- | ---: | ---: | ---: | ---: |
| **Mean CC** | −0.027705 | 0.02664185 | −0.561905 | 0.04662323 |
| **Mean NRMSE** | +0.031855 | 0.01531219 | +0.609524 | 0.04662323 |
| **DET** | −0.018645 | 0.02148438 | −0.580952 | 0.04662323 |
| Lmean | −0.062991 | 0.05825806 | −0.485714 | 0.08156128 |
| LAM | +0.016509 | 0.14290619 | +0.380952 | 0.16672389 |
| TT | +0.009515 | 0.20244980 | +0.333333 | 0.20244980 |
| **LLE** (s⁻¹) | −0.037570 | 0.00070763 | −0.809524 | 0.00495338 |

Bốn metric in đậm là các kết quả trọng tâm được xác định trước; Lmean, LAM và TT được trình bày ở mức mô tả bổ trợ.

## 4. Kết quả ghép cặp ngẫu nhiên

Cả bốn metric trọng tâm đều giữ chiều Awake-to-Drowsy kỳ vọng trong mọi cách ghép giả định đã lấy mẫu: Mean CC, DET và LLE giảm, còn Mean NRMSE tăng. Không trung vị nào trong 100.000 lần ghép của bốn metric này đạt hoặc vượt qua 0 sang chiều ngược lại. Độ lớn hiệu ứng thay đổi theo cách ghép; mức hỗ trợ suy luận sau điều chỉnh BH xuất hiện ít thường xuyên hơn ở Mean CC, Mean NRMSE và DET so với LLE.

| Metric trọng tâm | Trung vị \(\Delta\) gốc | Trung vị \(\Delta^*\) | Phân bố theo cách ghép, 2,5–97,5% | Giữ chiều kỳ vọng | Trung vị \(r_{rb}\) | Tỷ lệ \(q_{BH}<0.05\) |
| --- | ---: | ---: | --- | ---: | ---: | ---: |
| Mean CC | −0.027705 | −0.024205 | [−0.035921, −0.014749] | 100.000% | −0.709 | 19.36% |
| Mean NRMSE | +0.031855 | +0.026313 | [+0.018469, +0.034258] | 100.000% | +0.745 | 27.82% |
| DET | −0.018645 | −0.018069 | [−0.025544, −0.010024] | 100.000% | −0.709 | 22.59% |
| LLE (s⁻¹) | −0.037570 | −0.035608 | [−0.044613, −0.026557] | 100.000% | −0.964 | 79.69% |

Ba metric còn lại vẫn thuộc cùng tập bảy kiểm định. Trung vị \(\Delta^*\) lần lượt là −0.065674 với Lmean, +0.022726 với LAM và +0.007641 với TT; tỷ lệ giữ cùng dấu với trung vị n=20 tương ứng là 100.000%, 99.630% và 99.246%. [Bảng tổng hợp đủ bảy metric](../../sensitivy_data/unknown_repeated_session_dependence_v1/random_pairing_summary_v1.csv) lưu phân bố hiệu ứng, \(r_{rb}\), số cụm cùng chiều và mức hỗ trợ thống kê.

## 5. Độ ổn định của chiều và độ lớn hiệu ứng

Một cụm giả định chỉ được tính là cùng chiều kỳ vọng khi giá trị \(\Delta_k^*\) sau định hướng dấu lớn hơn \(10^{-12}\); trung vị nằm trong khoảng ±\(10^{-12}\) quanh 0 không được tính là giữ chiều. Dù trung vị giữ chiều ở mọi cách ghép được lấy mẫu, một số cụm riêng lẻ vẫn có thể ngược chiều hiệu ứng trọng tâm. Số cụm cùng chiều, theo thứ tự tối thiểu / phân vị 2,5% / trung vị / tối đa, là 5/6/8/10 với Mean CC, 6/7/8/9 với Mean NRMSE, 6/6/8/10 với DET và 7/8/9/10 với LLE.

Để so sánh độ lớn một cách mô tả, đặt \(R_{\mathrm{mag}}=|\mathrm{median}(\Delta^*)|/|\mathrm{median}(\Delta)_{n=20}|\). Các phân vị 2,5% / trung vị / 97,5% của tỷ số này là 0.532/0.874/1.297 đối với Mean CC; 0.580/0.826/1.075 đối với Mean NRMSE; 0.538/0.969/1.370 đối với DET; và 0.707/0.948/1.187 đối với LLE. Trong bốn metric trọng tâm, Mean CC và Mean NRMSE giảm độ lớn điển hình nhiều nhất. Tuy vậy, các phân bố được lấy mẫu không có tỷ trọng đáng kể tập trung gần 0 và không có trung vị trọng tâm nào đảo dấu. Những tỷ số này mô tả phân bố theo cách ghép, không phải khoảng tin cậy thống kê. Vì thế, các phát hiện trọng tâm **ổn định về chiều trong mô hình ghép cụm giả định đã khảo sát**, nhưng độ lớn không bất biến.

## 6. Mức hỗ trợ suy luận với mười cụm giả định

Tỷ lệ cách ghép có \(p<0.05\) chưa điều chỉnh lần lượt là 53.35%, 80.33%, 64.03% và 100.00% đối với Mean CC, Mean NRMSE, DET và LLE. Sau điều chỉnh BH trên cùng bảy metric như phân tích gốc, tỷ lệ có \(q_{BH}<0.05\) tương ứng là 19.36%, 27.82%, 22.59% và 79.69%. Tỷ lệ hỗ trợ sau điều chỉnh thấp hơn ở ba metric đầu cho thấy kết luận về ý nghĩa thống kê ở n=20 kém ổn định hơn khi gộp thành mười đơn vị giả định; điều này **không** có nghĩa hiệu ứng biến mất hoặc đảo chiều. Việc gộp làm thay đổi cả vector hiệu ứng lẫn số đơn vị suy luận hiệu dụng; cỡ mẫu nhỏ hơn có thể làm giảm lực kiểm định. Khi thiếu liên kết thật giữa người tham gia và phiên đo, các tỷ lệ này không định lượng được tác động thực tế của sự phụ thuộc giữa các phiên lên giá trị \(p\) ban đầu. Do đó, chiều và độ lớn hiệu ứng là bằng chứng chính của phân tích độ nhạy; mức hỗ trợ suy luận là bằng chứng thứ cấp.

## 7. Tìm kiếm cách ghép bảo thủ

Một phép tìm kiếm riêng, xác định trước, dùng 100 điểm bắt đầu và ở mỗi bước đánh giá 90 phép đổi cặp. Với từng metric trọng tâm, bốn mục tiêu được tối ưu độc lập: trung vị cùng chiều kỳ vọng yếu nhất, \(r_{rb}\) cùng chiều yếu nhất, số cụm cùng chiều ít nhất và mức hỗ trợ Wilcoxon exact yếu nhất. Các cách ghép có trung vị yếu nhất được tìm thấy cho \(\Delta^*\) bằng −0.003904 (Mean CC), +0.012076 (Mean NRMSE), −0.004709 (DET) và −0.019763 (LLE). Tất cả vẫn giữ chiều kỳ vọng, dù một số hiệu ứng suy giảm rõ và có mức hỗ trợ suy luận yếu hơn. Đây là **kết quả tìm kiếm cực trị cục bộ**, không phải cực trị toàn cục đã được chứng minh hoặc cách ghép người tham gia thực tế. Phép tìm kiếm giúp nhận diện khả năng suy yếu của kết quả, nhưng không chứng minh tính ổn định trong trường hợp bất lợi nhất. Cách ghép và thông tin chẩn đoán của cả 16 lần tìm kiếm nằm trong [bảng kết quả bảo thủ](../../sensitivy_data/unknown_repeated_session_dependence_v1/adversarial_best_found_v1.csv).

## 8. Độ ổn định Monte Carlo

Số lần lấy mẫu cuối cùng, 100.000, đã được xác định trước; độ hội tụ được đánh giá mô tả trên các tiền tố của cùng chuỗi mẫu. Từ 50.000 đến 100.000 cách ghép, tỷ lệ giữ chiều và trung vị \(r_{rb}\) của cả bốn metric trọng tâm không đổi. Mức thay đổi tuyệt đối lớn nhất của trung vị hiệu ứng là 0.00002273, của phân vị đầu mút phân bố là 0.00009067, và của tỷ lệ hỗ trợ BH là 0.116 điểm phần trăm. Các thay đổi nhỏ này cho thấy những thống kê Monte Carlo được báo cáo đã ổn định ở mức mô tả; không sử dụng quy tắc dừng thích nghi.

## 9. Diễn giải tổng hợp

Trong mô hình mười cụm hai phiên giả định đã khảo sát, chiều của các kết luận Awake–Drowsy chính không phụ thuộc mạnh vào một cách phân cặp cụ thể trong mẫu: trung vị của cả bốn metric trọng tâm giữ dấu đã định trước qua 100.000 cách ghép. Độ lớn hiệu ứng thay đổi, đặc biệt với Mean CC và Mean NRMSE; vì vậy không thể diễn giải kết quả như sự bất biến trước việc gộp cụm.

Cần phân biệt độ ổn định của hiệu ứng với mức hỗ trợ thống kê. Khi chuyển từ 20 đơn vị phiên đo sang mười đơn vị cụm giả định, mức hỗ trợ BH xuất hiện ít thường xuyên hơn đối với Mean CC, Mean NRMSE và DET, trong khi LLE được hỗ trợ nhất quán hơn. Như vậy, bằng chứng ở cấp phiên về chiều hiệu ứng ổn định hơn, trong mô hình độ nhạy này, so với quyết định suy luận dựa trên ngưỡng \(p\) hoặc \(q\). Thí nghiệm không chứng minh 20 phiên đo độc lập thống kê, cũng không xác nhận các giá trị \(p\) gốc vẫn hợp lệ dưới cấu trúc phụ thuộc thực tế chưa biết.

Do thiếu liên kết giữa người tham gia và phiên đo, không thể ước lượng tương quan thực tế giữa các phiên của cùng một người, và suy luận thống kê thật sự ở cấp người tham gia vẫn chưa thể thực hiện. Phân tích này kiểm tra có cấu trúc mức biến thiên của các kết luận ở cấp phiên giữa nhiều cách ghép giả định; nó không thay thế mô hình sử dụng mã định danh người tham gia đã biết.

## 10. Đoạn văn có thể dùng cho bản thảo

### 10.1 Đoạn Phương pháp

“Để đánh giá độ nhạy đối với sự phụ thuộc chưa xác định giữa các phiên đo lặp lại, chúng tôi dùng 20 chênh lệch Awake–Drowsy ở cấp phiên làm đầu vào cho các phân hoạch giả định thành mười cụm hai phiên. Với seed xác định trước, chúng tôi lấy mẫu có hoàn lại 100.000 cách ghép cặp hoàn hảo và lấy trung bình hai chênh lệch phiên trong mỗi cụm. Ở từng cách ghép và từng metric trong bảy metric chính, chúng tôi tính trung vị của mười chênh lệch cụm, tương quan rank-biserial cho dữ liệu ghép cặp, giá trị \(p\) Wilcoxon signed-rank hai phía dạng exact và giá trị \(q\) điều chỉnh Benjamini–Hochberg trên bảy metric. Các phân vị theo cách ghép mô tả độ nhạy đối với việc phân cụm giả định, không phải khoảng tin cậy ở cấp người tham gia.”

### 10.2 Đoạn Kết quả

“Qua 100.000 cách ghép giả định thành cụm hai phiên, trung vị hiệu ứng của Mean CC, Mean NRMSE, DET và LLE giữ chiều đã định trước trong mọi cách ghép. Trung vị hiệu ứng theo các cách ghép lần lượt là −0.024205, +0.026313, −0.018069 và −0.035608 s⁻¹; các khoảng phân vị 2,5–97,5% tương ứng của phân bố cách ghép đều không chứa 0. Độ lớn hiệu ứng thay đổi; tỷ lệ cách ghép có hỗ trợ sau điều chỉnh BH trên bảy metric (\(q<0.05\)) lần lượt là 19.36%, 27.82%, 22.59% và 79.69%. Như vậy, sau khi gộp thành mười cụm giả định, chiều hiệu ứng ổn định hơn mức hỗ trợ suy luận dựa trên ngưỡng.”

### 10.3 Đoạn Thảo luận / Giới hạn

“Chiều của các hiệu ứng Awake–Drowsy chính ổn định trong mô hình ghép cụm hai phiên giả định đã khảo sát, dù độ lớn hiệu ứng và mức hỗ trợ thống kê thay đổi. Đặc biệt, tỷ lệ hỗ trợ sau điều chỉnh thấp hơn ở Mean CC, Mean NRMSE và DET có thể liên quan đến số đơn vị suy luận hiệu dụng nhỏ hơn cũng như sự khác biệt giữa các cách ghép giả định; không nên diễn giải đó là hiệu ứng đảo chiều. Vì liên kết thật giữa người tham gia và phiên đo không còn, không thể ước lượng tương quan giữa các phiên của cùng một người. Phân tích độ nhạy này không khôi phục danh tính người tham gia và không thay thế suy luận thống kê ở cấp người tham gia.”

## 11. Đề xuất vị trí trong bản thảo

**Bản thảo chính.** Trình bày ngắn gọn vấn đề suy luận, tỷ lệ giữ chiều của bốn metric trọng tâm, trung vị và các phân vị của phân bố theo cách ghép, cùng tỷ lệ hỗ trợ BH trong một đoạn Kết quả hoặc bảng ngắn. Nêu rõ các khoảng được báo cáo là phân bố qua những cách ghép giả định.

**Tài liệu bổ sung.** Cung cấp bảng kết quả đầy đủ của bảy metric; phân bố tỷ số độ lớn và số cụm cùng chiều; các tiền tố dùng kiểm tra hội tụ; cả bốn mục tiêu tìm kiếm bảo thủ cho mỗi metric trọng tâm, kèm cách ghép và thông tin chẩn đoán tìm kiếm; thuật toán đã đóng băng, nguồn gốc đầu vào canonical và manifest SHA-256.

## 12. Kết luận cuối cùng

Chiều của các hiệu ứng Awake–Drowsy chính không phụ thuộc vào cách ghép cụm hai phiên giả định cụ thể trong 100.000 cách ghép đã lấy mẫu; tuy nhiên, độ lớn hiệu ứng và mức hỗ trợ suy luận thay đổi khi gộp thành mười cụm. Vì liên kết thật giữa người tham gia và phiên đo vẫn không có, đây là kết quả đánh giá độ nhạy, không phải bằng chứng về tính độc lập thống kê hay suy luận ở cấp người tham gia.
