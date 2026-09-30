# Bản đồ bản thảo — Version 2

**Thẩm quyền nguồn và phạm vi.** [Manuscript Version 1](../doc/manuscript_version1.pdf) là nguồn có thẩm quyền cho mọi kết quả số, bảng, effect size, CI, p, q và robustness đã có trong PDF. [Bảng chuẩn khoa học — Manuscript Version 2](01_master_canonical_sheet_vi.md) ghi quy tắc nguồn, phương pháp và giới hạn claim để lập bản đồ này. Report sau Version 1 chỉ làm rõ phương pháp/diễn đạt/giới hạn, hoặc cung cấp phân tích mới không có trong PDF; không tự thay số đã chốt trong Version 1. Đây là argument map cho tạp chí dự kiến *Chaos, Solitons & Fractals*, không phải văn xuôi bản thảo. Việc sửa diễn đạt Simplex aggregation là sửa tài liệu, không phải sửa tính toán; các kết quả Simplex và robustness theo độ dài cửa sổ của Version 1 vẫn finalized.

## 1. Định danh bản thảo trong một đoạn

**Vấn đề và khoảng trống:** Declining vigilance là một quá trình chuyển tiếp mà PPG ngoại vi trong cửa sổ ngắn có thể thay đổi về động lực học, trong khi các nghiên cứu PPG về drowsiness thường nhấn mạnh đặc trưng truyền thống hoặc classification và sự tái tổ chức động lực học trực tiếp vẫn chưa được mô tả đầy đủ. **Đóng góp:** Trong protocol PPG 60 s đã kiểm tra, phép so sánh với một pseudoperiodic-surrogate cụ thể đánh giá liệu tín hiệu có tổ chức vượt quá null đó hay không (RQ1), còn các ước lượng Simplex, RQA và Rosenstein LLE ghép cặp ở cấp session mô tả các khác biệt trạng thái bổ sung cho nhau (RQ2). **Luận đề trung tâm:** Wakefulness-to-drowsiness transition liên quan đến sự tái tổ chức phối hợp của finite-horizon forecastability, diagonal recurrence organization và local trajectory divergence, không phải dịch chuyển trên một trục chaos/complexity duy nhất. Đối tượng khoa học của bài là quan hệ giữa các thuộc tính động lực học này, giới hạn do cửa sổ hữu hạn và reconstruction, cùng ranh giới suy luận do unknown repeated-session dependence. Đây không phải nghiên cứu về hiệu năng detector hoặc claim về cơ chế sinh lý nhân quả.

## 2. Logic khoa học cốt lõi

| Bước | Chức năng trong lập luận | Bằng chứng hoặc giới hạn khiến cần bước tiếp theo |
| --- | --- | --- |
| 1 | Định nghĩa Drowsy là declining vigilance trong bối cảnh sau bữa ăn, với nhãn dựa trên video/KSS. | Không có PSG; không gọi trạng thái là N1/NREM. |
| 2 | Xác lập vì sao cần nghiên cứu chính waveform PPG ngoài các đặc trưng truyền thống. | Introduction Version 1 cung cấp các vị trí cấu trúc cho literature; không thêm claim literature mới ở đây. |
| 3 | Định nghĩa khoảng trống là *thay đổi động lực học* ở cửa sổ ngắn giữa Awake và Drowsy, không phải thiếu classifier. | Một descriptor không thể đồng thời đại diện cho prediction, recurrence geometry và divergence. |
| 4 | Trình bày phase-space reconstruction chung và ba estimator bổ sung. | Đóng băng cấu hình phương pháp và dùng cùng embedding giữa các state trước khi so sánh. |
| 5 | Trả lời RQ1 bằng PPS trước khi so sánh hai state. | Departure chỉ áp dụng cho noisy pseudoperiodic null đã kiểm tra và không xác lập chaos. |
| 6 | Trả lời RQ2 bằng bảy metric paired nominal 60 s. | Bốn hướng headline tạo claim về tái tổ chức phối hợp; ba metric RQA còn lại là secondary. |
| 7 | Kiểm tra kết luận tồn tại đến mức nào qua cửa sổ hữu hạn, nhãn và tham số. | Robustness phụ thuộc metric; DET nhạy với embedding delay. Kết quả finalized theo độ dài cửa sổ giữ cả bốn hướng headline qua 30–180 s, với uncertainty lớn hơn ở 30 s. |
| 8 | Giới hạn suy luận khi thiếu liên kết giữa các session lặp lại. | Ghép cặp giả định giữ các hướng headline trong mẫu nhưng thay đổi độ lớn và q support; liên kết thật vẫn không có. |
| 9 | Thêm pattern symbolic làm bối cảnh và kết thúc bằng các giới hạn. | Kết quả symbolic là exploratory và không trực tiếp đo các nhánh autonomic. |

**Câu hỏi nghiên cứu.** RQ1: PPG trong cửa sổ ngắn ở cả Awake và Drowsy có tổ chức thời gian/động lực học vượt quá mức mà noisy pseudoperiodic null **đã kiểm tra** tái tạo hay không? Bằng chứng: phép so sánh rank PPS cấp cửa sổ và tóm tắt theo session. RQ2: Drowsy liên quan thế nào đến các thuộc tính PPG bổ sung cho nhau ở cửa sổ ngắn? Bằng chứng: Mean CC và Mean NRMSE theo Version 1 Table III, DET và LLE, với Lmean/LAM/TT là bối cảnh secondary. Đơn vị suy luận của RQ2 là session, không phải window hoặc participant.

**Thứ bậc bằng chứng được dùng xuyên suốt:** (1) primary/headline: Mean CC, Mean NRMSE, DET, LLE; (2) secondary: Lmean, LAM, TT; (3) supportive/exploratory: symbolic dynamics 0V/1V/2V. DET vẫn là headline **kèm giới hạn theo embedding delay**. PPS trả lời RQ1 và không được trộn với các tầng bằng chứng của RQ2.

## 3. Bản đồ Introduction

Bảy đoạn; mỗi hàng là chỉ dẫn lập luận, không phải bản thảo văn xuôi. Vai trò literature chỉ các chủ đề đã có trong Version 1 và cần kiểm tra nguồn khi viết sau này.

| Đoạn | Mục đích và nội dung thiết yếu | Vai trò bằng chứng/literature | Chuyển tiếp và claim cần tránh |
| --- | --- | --- | --- |
| 1 | Định nghĩa declining vigilance là bối cảnh sinh lý chuyển tiếp; nêu lý do đo sinh lý trong Awake-to-Drowsy transition. | Nền về drowsiness và sleep onset đã có; giới hạn nhãn theo video/KSS. | Từ trạng thái chuyển sang tín hiệu PPG có thể đo. Tránh đồng nhất Drowsy với giai đoạn ngủ PSG. |
| 2 | Cho thấy PPG trong ứng dụng này thường được quy về heart-rate/HRV, morphology hoặc đặc trưng cho classifier. | Literature về theo dõi PPG trong Version 1 là baseline để định khung, không phải bằng chứng về thực hành phổ quát. | Đặt câu hỏi về đóng góp của tổ chức thời gian trong chính waveform. Tránh nói chưa hề có nghiên cứu nonlinear trước đây. |
| 3 | Xác lập PPG là tín hiệu dao động/pseudoperiodic phù hợp với kiểm định động lực học theo một null cụ thể. | Các nghiên cứu PPG nonlinear/PPS đã dẫn trong Version 1 cung cấp bối cảnh. | Dẫn tới lý do cấu trúc quan sát cần surrogate null phù hợp. Tránh mặc định deterministic chaos. |
| 4 | Nêu chính xác khoảng trống: chưa mô tả đầy đủ tái tổ chức động lực học waveform trong Awake-to-Drowsy ở cửa sổ ngắn; độ nhạy với bản ghi hữu hạn và tham số là quan trọng. | Literature về window length và độ tin cậy NTSA đã có trong Version 1. | Biện minh cho nhiều descriptor thay vì một complexity score chung. Tránh nói mọi lựa chọn tham số đều robust. |
| 5 | Giải thích ba quan sát bổ sung: finite-horizon forecastability, recurrence organization và local trajectory divergence. | Literature phương pháp chỉ cung cấp định nghĩa. | Protocol chung cho phép đặt hai câu hỏi có thể kiểm tra. Tránh trình bày bài như ba thuật toán rời rạc. |
| 6 | Nêu RQ1 trước rồi RQ2, với PPS null đã kiểm tra và phép so sánh paired theo session. | Không đưa số kết quả; làm rõ surrogate comparison và state comparison trả lời hai câu hỏi khác nhau. | Chuyển sang thiết kế phân tích và thứ bậc bằng chứng. Tránh đồng nhất bác bỏ null với chứng minh chaos. |
| 7 | Nêu đóng góp có giới hạn: mô tả động lực học phối hợp kèm độ nhạy theo cửa sổ hữu hạn, nhãn, tham số và dependence. | Liên kết với vai trò bằng chứng canonical. | Dẫn sang lựa chọn thu nhận/phân tích chính xác ở Methods. Tránh hứa hẹn real-time detection hoặc giải thích autonomic nhân quả. |

## 4. Bản đồ Materials and Methods

Methods trả lời **đã làm chính xác điều gì**. Main text chỉ giữ định nghĩa cần thiết để tái lập; chuyển dẫn giải, hình minh họa, audit implementation và grid đầy đủ sang Supplementary. Mọi cấu hình bên dưới dẫn về canonical sheet, không phải cơ hội điều chỉnh hoặc tính lại.

| Tiểu mục | Phải giữ trong main Methods | Rút gọn hoặc chuyển Supplementary | Diễn đạt / giới hạn |
| --- | --- | --- | --- |
| 4.1 Dataset và experimental protocol | 20 sessions từ 10 người trưởng thành trẻ khỏe mạnh; PPG MAX30102/ESP32 sau bữa ăn; nhãn video/KSS; không PSG; không có participant–session linkage thực. Phân biệt thời lượng ghi với thời lượng cửa sổ được đưa vào. | Danh sách session đầy đủ và chi tiết thu nhận. | Dùng “recording sessions” và “session-level inference”, không gọi 20 participants độc lập. |
| 4.2 Tiền xử lý PPG | Butterworth band-pass bậc hai 0.5–8 Hz, áp dụng thuận/ngược zero-phase; PPG Processed làm input phân tích. | Minh họa bộ lọc và lý thuyết lọc chuẩn. | Không gợi ý có bước lọc mới trong label sensitivity. |
| 4.3 Phân đoạn và QC | Cửa sổ primary 60 s không chồng lấp; phân tích độ dài 30/120/180 s; SQI trên subwindow Processed 5 s, quy tắc artifact amplitude/roughness modified-z > 4.5, loại cửa sổ phân tích bị nhiễm; subwindow stationarity 10 s **chỉ theo phương sai**, S ≤ 0.5; cần đạt cả hai mask. | Dẫn giải phương trình SQI đầy đủ, audit interval/gap và số QC theo session. | Không thêm tiêu chí mean-stability chưa được ghi nhận. |
| 4.4 Phase-space reconstruction | Delay-coordinate embedding, cơ sở AMI/FNN, τ = 0.16 s và m = 8 chung giữa hai state; chuyển đổi round(τ × fs) và lý do dùng hệ tọa độ chung. | Đường AMI/FNN đầy đủ, audit ngưỡng và grid τ/m cục bộ. | Không chọn tham số bằng p value Awake–Drowsy. |
| 4.5.1 Simplex Projection | Leave-one-out; Euclidean k = m + 1 = 9; trọng số exponential; temporal exclusion 1.0 s; 18 horizons từ 0.04 đến 4.00 s. **Viết rõ aggregation: metric tại mỗi horizon trong mỗi valid window → mean các horizon trong window → median các window trong session × state.** | Đường theo horizon, grid Theiler và audit tái hiện chính xác. | Cách diễn đạt mean-of-horizon-medians trước đây là lỗi tài liệu; implementation và output finalized dùng window-first như đã nêu. |
| 4.5.2 RQA | Euclidean recurrence; ε riêng cửa sổ tại RR = 0.02; Theiler W = (m − 1)τ_samples; l_min = v_min = 2; DET/Lmean/LAM/TT; median cửa sổ hợp lệ. | Định nghĩa mọi loại đường, minh họa recurrence plot, audit tie/cache và các hàng RR/Theiler perturbation. | DET là diagonal recurrence organization, không phải physical determinism. |
| 4.5.3 Rosenstein LLE | Nearest admissible neighbor; Theiler spectral-period riêng từng cửa sổ; fit 0.80–1.30 s, follow 5 s, tối thiểu 50 initial/30 fit pairs và ba points; estimate hữu hạn và R² ≥ 0.90; s⁻¹; median cửa sổ hợp lệ. | Chi tiết pair-support, regression và audit fit-range/QC. | Descriptor divergence trên dữ liệu hữu hạn; không có claim deterministic chaos. |
| 4.6 Kiểm định pseudoperiodic surrogate | Noisy pseudoperiodic null; 39 PPS realizations mỗi cửa sổ hợp lệ; bảy metric được kiểm tra; phép kiểm rank hai phía trên 40 giá trị với p nhỏ nhất = 0.05. | Toán học tạo surrogate, calibration và waveform đại diện. | Null này là cụ thể; tỷ lệ bác bỏ cấp cửa sổ không phải p của paired-session RQ2. |
| 4.7 Phân tích thống kê | Window là đơn vị tính toán; session là đơn vị suy luận; Δ = Drowsy − Awake; median cửa sổ hợp lệ trong session-state; median paired Δ, Wilcoxon hai phía, matched-pairs r_rb, 20,000 bootstrap paired-session 95% CI; BH một lần trên đúng bảy metric nominal 60 s. | Chi tiết implementation về zero/tie và seed. | Version 1 Table III báo cáo CI, r_rb và q nhưng không báo raw p theo từng metric; không nhập raw p từ report sau. |
| 4.8 Độ nhạy và robustness | Độ dài cửa sổ, nhãn T30/T60/S3/S5, τ/m cục bộ và cấu hình estimator theo Version 1; hypothetical two-session clustering của 20 session deltas thành mười đơn vị với 100,000 matchings được lấy mẫu là phân tích sau Version 1; symbolic là phân tích exploratory riêng. | Ma trận độ nhạy đầy đủ, convergence, toàn bộ local-search records và chi tiết symbolic. | Kết quả 30/60/120/180 s trong Version 1 là finalized. Hypothetical clusters không phải những người đã xác định; baseline Simplex của phân tích mới này khác Table III. |

**Thứ tự Methods:** Giới thiệu cohort và đường dữ liệu chung một lần; mô tả ba estimator như các góc nhìn bổ sung; sau đó phân biệt đường PPS/RQ1 với đường thống kê paired-state/RQ2. Cách này tránh lặp setup phương pháp ở Results.

## 5. Bản đồ Results

**Thứ tự bắt buộc:** dataset/QC ngắn → **RQ1** PPS → **RQ2** hiệu ứng primary theo Version 1 → robustness theo độ dài → độ nhạy nhãn/tham số → độ nhạy repeated-session → hỗ trợ symbolic. Mỗi tiểu mục có một câu hỏi và một takeaway; dành diễn giải chi tiết cho Discussion.

| Tiểu mục | Câu hỏi khoa học và bằng chứng cần trình bày | Thống kê tối thiểu và hình/bảng dự kiến | Takeaway một câu; để dành cho Discussion |
| --- | --- | --- | --- |
| 5.1 Dataset và QC | Dữ liệu nào đi vào phân tích? 20 sessions; Version 1 Table I báo 623 cửa sổ ứng viên Awake và 328 Drowsy ở 60 s, với tỷ lệ đạt QC 95.67% và 92.99%. Số cửa sổ hợp lệ chi tiết, nếu cần, phải ghi rõ là tổng suy ra từ Table I hoặc provenance audit sau Version 1. | Bảng cohort/nhãn/QC nhỏ hoặc inset flow; phân biệt giờ ghi với cửa sổ sau QC. Không đưa retention LLE từ audit vào bảng Version 1 nếu PDF không báo. | “Đường QC đã đóng băng tạo dữ liệu Awake/Drowsy ghép cặp trong cả 20 sessions.” Để dành giới hạn khái quát hóa và gán nhãn. |
| 5.2 **RQ1: tổ chức vượt quá PPS** | Cửa sổ Awake và Drowsy gốc có khác ensemble PPS theo null đã kiểm tra không? Trình bày hướng original-minus-PPS của prediction, RQA và LLE trong cả hai state theo Version 1 Fig. 7. | Pattern và các tỷ lệ chỉ lấy như được hiển thị/báo cáo trong Version 1; không chép tỷ lệ chính xác từ audit sau nếu PDF không có. Nêu M = 39 và p nhỏ nhất = 0.05. Main Figure 3. | “Cả hai state có tổ chức mà noisy pseudoperiodic null này không tái tạo đầy đủ.” Để dành các null/cơ chế khác còn có thể; không gọi đây là chứng minh deterministic chaos. |
| 5.3 **RQ2: tái tổ chức trạng thái primary** | Các contrast paired theo session giữa ba thuộc tính động lực học là gì? Dẫn bằng [Version 1 Table III](../doc/manuscript_version1.pdf): Mean CC ↓ (Δ −0.0339), Mean NRMSE ↑ (+0.0294), DET ↓ (−0.0186), LLE ↓ (−0.0376 s⁻¹); sau đó Lmean/LAM/TT. | Một bảng bảy hàng gồm median Δ, 95% CI, r_rb và q_BH đúng như Table III; Figure 4 về paired/distribution. Bốn q headline tương ứng 0.0376, 0.0255, 0.0376 và 0.0050. Table III không báo raw p; CI của Mean CC [−0.0595, −0.0043] không chứa zero. | “Drowsy liên quan đến forecastability, diagonal recurrence organization và local divergence ước lượng thấp hơn.” Để dành giải thích forecastability–LLE và diễn giải sinh lý. Các dấu RQA secondary không được BH bảy metric hỗ trợ. |
| 5.4 Robustness theo độ dài cửa sổ | Hiệu ứng nào giữ hướng ở 30/60/120/180 s, và uncertainty cửa sổ hữu hạn rộng hơn ở đâu? | [Version 1 Fig. 9](../doc/manuscript_version1.pdf) là bằng chứng finalized: Mean CC ↓, Mean NRMSE ↑, DET ↓ và LLE ↓ ở bốn độ dài, với uncertainty lớn hơn ở 30 s; Figure 5 theo đúng asset/số của PDF. PDF không in bảng Δ chính xác cho từng duration nên không thêm số từ report sau như thể chúng thuộc Fig. 9. | “Cả bốn hướng headline được giữ qua các cửa sổ 30–180 s đã kiểm tra, với uncertainty lớn hơn ở 30 s.” 60 s là practical compromise trong dataset này, không phải optimum phổ quát. |
| 5.5 Độ nhạy nhãn và tham số NTSA | Các dấu headline có đứng vững trong các rule nhãn và lựa chọn estimator đã kiểm tra không? Metric nào nhạy? | T30/T60/S3/S5: 20/20/20/19 paired sessions, cả bốn hướng median headline giữ nguyên và 16/16 contrast được q trong từng rule hỗ trợ; hai CI chứa zero. Tóm tắt τ/m/RR/Theiler gọn phải cho thấy median DET ở τ = 0.12/0.20 s dương, gần zero so với nominal âm. Figure 6 hoặc bảng gọn nếu còn chỗ. | “Robustness phụ thuộc metric: dấu prediction và LLE giữ trong các grid đã kiểm tra, còn DET nhạy với embedding delay.” Để dành ý nghĩa diễn giải; không mang q family bốn metric vào family primary. |
| 5.6 Unknown repeated-session dependence | Kết luận thay đổi thế nào dưới mười hypothetical two-session units khi thiếu liên kết thật? Đây là phân tích sau Version 1, dựa trên baseline Simplex riêng của report dedicated. | Hướng median của cả bốn headline được giữ trong 100,000/100,000 matchings đã lấy mẫu; median Δ* và phân bố theo matching 2.5–97.5%; tỷ lệ q support 19.36% CC, 27.82% NRMSE, 22.59% DET, 79.69% LLE; bảng/panel main gọn, gắn nhãn nguồn dedicated. | “Hướng trong mẫu được giữ nhưng độ lớn và hỗ trợ suy luận thay đổi sau clustering giả định.” Phân tích này không kiểm định trực tiếp Δ, CI hoặc q Table III. Không gọi các matching là participants quan sát được, các phân vị là confidence interval, hoặc phép thử là chứng minh độc lập. |
| 5.7 Hỗ trợ symbolic | Có pattern sinh lý phụ trợ nào phù hợp với tái tổ chức động lực học không? | Main text chỉ nêu hướng theo Version 1 Table IV: 0V ↑, 2V ↓, 1V gần zero/không nhất quán; Version 1 không có hỗ trợ thống kê nhất quán qua cấu hình. Bảng đầy đủ theo độ dài ở Supplementary; không nhập q từ audit sau như thể là số của PDF. | “Thành phần symbolic chỉ cho bối cảnh exploratory.” Để dành diễn giải autonomic; không quy trực tiếp cho sympathetic/parasympathetic. |

**Cổng kiểm tra tài liệu Results:** Giữ [Version 1 Table III](../doc/manuscript_version1.pdf) cho kết quả primary, Tables IV–VI cho phân tích tương ứng và Fig. 9 cho duration finalized. Không thay số Version 1 bằng report sau hoặc tự tạo bảng Δ duration từ hình. Table III và Table VI có giá trị nominal Simplex khác nhau; ghi nhận bất đồng này theo vai trò hai bảng, không tự hòa giải. Sửa wording aggregation không hàm ý lỗi tính toán hoặc yêu cầu chạy lại.

## 6. Bản đồ Discussion

Xây Discussion quanh sáu lập luận thay vì kể lại Results. “Vai trò prior work” chỉ cách dùng các tài liệu tham khảo đã có trong Version 1 về sau; không cho phép thêm claim literature mới.

| Tiểu mục | Lập luận cốt lõi và bằng chứng | Vai trò prior work | Ranh giới claim chính xác và takeaway |
| --- | --- | --- | --- |
| 6.1 Tái tổ chức phối hợp | Kết hợp CC ↓/NRMSE ↑ theo Version 1 Table III, DET ↓ nominal và LLE ↓ như ba thuộc tính bổ sung; các xu hướng RQA secondary có thể bổ nghĩa geometry nhưng không gánh luận đề. | Liên hệ với bối cảnh PPG nonlinear và cardiovascular dynamics đã có. | Liên hệ giữa các descriptor đo được; không phải thang chaos/complexity có thứ tự. Takeaway: transition có dấu hiệu động lực học đa chiều. |
| 6.2 Vì sao forecastability ↓ và LLE ↓ cùng tồn tại | Simplex đo mức khớp/sai số dự báo finite-horizon từ các state gần nhau đã tái dựng; Rosenstein LLE ước lượng độ dốc tách xa của mean log-distance cục bộ trong fit interval cụ thể. Horizons, estimands và điểm yếu của chúng khác nhau, nên prediction skill giảm không đòi hỏi fitted local divergence tăng. | Chỉ dùng nguồn khái niệm prediction/LLE đã có để định nghĩa hai quan sát khác nhau. | Không đưa cơ chế ẩn mới, chứng minh chaos hoặc quan hệ phổ quát. Takeaway: hai hướng giảm là các quan sát bổ sung và tương thích. |
| 6.3 Giới hạn cửa sổ hữu hạn và robustness | Tích hợp bằng chứng duration finalized của Version 1, label rules, grid embedding cục bộ, RR/Theiler và fit/QC của LLE; trình bày hypothetical clustering sau Version 1 với baseline và nguồn riêng. Làm nổi bật độ nhạy DET với delay và bốn hướng được giữ qua 30–180 s, với uncertainty lớn hơn ở 30 s. | Nguồn NTSA về bản ghi ngắn đã có giải thích vì sao độ tin cậy phụ thuộc metric. | Chỉ dùng “robust trong setting đã kiểm tra” khi đúng; không claim bất biến tham số, tối ưu 60 s phổ quát hoặc chứng minh 20 sessions độc lập. Không lấy phân tích repeated-session có baseline Simplex khác để xác nhận trực tiếp CI/q Table III. Takeaway: hướng nói chung ổn định hơn độ lớn/hỗ trợ trong các thay đổi đã kiểm tra. |
| 6.4 Bối cảnh sinh lý | Đặt pattern PPG trong declining vigilance/điều hòa tim mạch sau bữa ăn; 0V ↑/2V ↓ có thể hỗ trợ tính tương thích với thay đổi cardiac autonomic modulation. | Các tài liệu sleep-onset và symbolic-autonomic đã có cung cấp bối cảnh, không xác minh cơ chế cho dataset này. | Drowsy được xác định bằng video/KSS, không phải giấc ngủ PSG; symbolic PPG không đo trực tiếp sympathetic/parasympathetic; không gán cơ chế nhân quả. Takeaway: sinh lý là bối cảnh hợp lý, không phải mediator đã đo. |
| 6.5 Hàm ý thực tiễn | Giải thích vì sao mô tả động lực học cửa sổ ngắn có thể giúp phát triển PPG descriptors trong tương lai. | Nghiên cứu wearable/monitoring đã có cung cấp bối cảnh ứng dụng. | Chưa chứng minh classifier, triển khai prospective, real-time detection hoặc hiệu năng bên ngoài. Takeaway: tính khả thi của descriptor thúc đẩy validation sau này. |
| 6.6 Giới hạn | Nêu cohort nhỏ gồm người trẻ khỏe mạnh; bối cảnh sau bữa ăn; không PSG; chỉ PPG ngoại vi; thiếu multimodal/external validation; thiếu participant–session linkage và không ước lượng được tương quan trong người thực; phụ thuộc dữ liệu hữu hạn, QC và tham số; PPS null cụ thể; LLE không chứng minh chaos. Ghi rõ Table III và Table VI của Version 1 có nominal Simplex khác nhau, không tự giải thích nguyên nhân. | Không cần literature để làm nhẹ các giới hạn này. | Phân tích độ nhạy giới hạn một số uncertainty nhưng không xóa chúng. Takeaway: suy luận ở cấp session và có điều kiện theo các setting đã kiểm tra. |

## 7. Bản đồ Conclusion

Dùng bốn vai trò câu ngắn trong Conclusion sau này, không thêm q chi tiết hoặc claim mới:

1. Trả lời RQ1: PPG Awake và Drowsy đều khác ensemble noisy pseudoperiodic surrogate đã kiểm tra.
2. Trả lời RQ2: Drowsy liên quan đến finite-horizon forecastability thấp hơn, diagonal recurrence organization nominal thấp hơn và fitted local trajectory divergence thấp hơn.
3. Tích hợp ba thuộc tính thành sự tái tổ chức phối hợp, bổ sung cho nhau; không đặt chúng trên trục more/less chaos.
4. Kết thúc bằng hướng nghiên cứu có giới hạn về multimodal, participant được định danh và external validation cho short-window descriptors, không claim hiệu năng classifier.

## 8. Bản đồ Abstract

Chỉ định các phần cấu trúc; nội dung văn xuôi sẽ viết sau. Abstract phải tự đủ hiểu khi không đọc Supplementary.

| Vị trí | Nội dung cần mang | Đưa vào / loại trừ |
| --- | --- | --- |
| 1. Background và gap | Theo dõi PPG thường nhấn mạnh derived features; động lực học waveform qua declining vigilance cần mô tả trực tiếp. | Không claim tính mới tuyệt đối. |
| 2. Objective | Tổ chức theo null cụ thể của RQ1, rồi khác biệt Awake–Drowsy bổ sung của RQ2. | Không đồng nhất RQ1 với kiểm định chaos nói chung. |
| 3. Data và method | 20 sessions từ 10 người trưởng thành; cửa sổ primary Processed 60 s không chồng lấp; PPS, Simplex, RQA, LLE; suy luận paired cấp session. | Nêu đơn vị là sessions, không phải những người độc lập. |
| 4. Kết quả RQ1 | Tổ chức vượt quá PPS null đã kiểm tra ở cả hai state. | Một phát biểu có giới hạn; không liệt kê dày đặc tỷ lệ bác bỏ. |
| 5. Kết quả RQ2 | Các mốc số nếu giới hạn độ dài cho phép: Version 1 Table III Mean CC −0.0339, Mean NRMSE +0.0294, DET −0.0186, LLE −0.0376 s⁻¹. | Nếu nêu q, dùng đúng q_BH tương ứng của Table III: 0.0376, 0.0255, 0.0376, 0.0050. CI của Mean CC [−0.0595, −0.0043] không chứa zero. Không thêm raw p mà Table III không báo cáo. |
| 6. Sắc thái robustness | Version 1 Fig. 9 giữ cả bốn hướng headline qua 30/60/120/180 s, với uncertainty lớn hơn ở 30 s; DET nhạy với delay. Phân tích ghép cặp giả định sau Version 1 giữ hướng trong mẫu nhưng q support biến đổi. | Ghi giới hạn hypothetical pairing và baseline Simplex riêng; không biến phân tích này thành bằng chứng trực tiếp cho CI/q Table III. |
| 7. Conclusion | Tái tổ chức phối hợp ở ba thuộc tính, với diễn giải có giới hạn. | Không claim deterministic chaos, đo autonomic trực tiếp hoặc nhân quả. |

## 9. Kế hoạch Figure

Đây là các vị trí biên tập, không phải yêu cầu tạo phân tích mới. Figure của Version 1 là nguồn có thẩm quyền cho các kết quả số/robustness đã có trong PDF; khi thiết kế lại phải giữ dữ liệu và caption tương ứng, không thay bằng output audit sau. Chỉ giữ những figure thực hiện vai trò lập luận khác nhau.

| Figure | Vai trò khoa học và panel dự kiến | Cấp bằng chứng / lý do ở main text | Quyết định với asset Version 1 |
| --- | --- | --- | --- |
| 1. Đường nghiên cứu và phân tích | Cohort/nhãn → filter/QC → cửa sổ 60 s → embedding chung → nhánh PPS/RQ1 và paired RQ2 → sensitivity. Sơ đồ gọn với n khi thiết yếu. | Main: làm rõ đơn vị suy luận và trình tự câu hỏi từ đầu. | Bố cục mới; V1 Fig. 1 là minh họa lọc và thuộc Supplementary nếu giữ. |
| 2. Lựa chọn reconstruction | Bằng chứng AMI/FNN gọn cho cấu hình cộng với τ/m chung; tránh panel attractor chỉ mang tính trang trí. | Main chỉ khi giúp hiểu định nghĩa state-space chung; nếu không thì Supplementary. | Làm lại V1 Fig. 2; kiểm tra trục và cấu hình theo canonical sheet. |
| 3. Bằng chứng PPS | Original-minus-PPS hoặc pattern bác bỏ phân theo state trên prediction, RQA và LLE; nêu rõ null đã kiểm tra và mẫu số LLE. | Main: trả lời trực tiếp RQ1. | Dùng V1 Fig. 7 làm nguồn kết quả; có thể thiết kế lại cách trình bày mà không thay số. Waveform surrogate ở V1 Fig. 6 có thể chuyển Supplementary. |
| 4. Hiệu ứng Awake–Drowsy primary | Phân bố/interval paired Δ của bốn headline làm trọng tâm visual; RQA secondary trình bày tiết chế hoặc chỉ ở Table 3. | Main: trả lời trực tiếp RQ2. | Dùng V1 Fig. 8 và Table III làm nguồn số; nếu thiết kế lại, các nhãn/giá trị phải khớp Version 1. |
| 5. Robustness theo độ dài cửa sổ | Hướng và uncertainty của Mean CC, Mean NRMSE, DET và LLE trong phân tích finalized 30/60/120/180 s; thể hiện uncertainty lớn hơn ở 30 s. | Main: xác lập phát hiện hướng theo cửa sổ hữu hạn đã kiểm tra. | V1 Fig. 9 là nguồn kết quả có thẩm quyền. Có thể dùng nguyên hình hoặc thiết kế lại trung thành với hình gốc; không tự tạo bảng Δ duration từ report sau hoặc thay số trong hình. |
| 6. Ranh giới sensitivity/inference (tùy chọn) | Một panel gọn cho DET theo embedding delay và/hoặc hướng headline so với tần suất q support dưới các ghép cặp giả định. | Main chỉ nếu bổ sung điều mà đoạn Results ngắn không thể thể hiện; chi tiết ở Supplementary. | Thiết kế mới từ các sensitivity report đã đóng băng. Tránh hình tổng hợp quá nhiều tham số của mọi phương pháp. |

V1 Figs. 3–5 là minh họa estimator; chuyển sang Supplementary nếu cần để người đọc hiểu. Tên/caption figure phải nêu câu hỏi khoa học và đơn vị, không chỉ tên phương pháp.

## 10. Kế hoạch Table

| Table | Nội dung và mục đích | Vị trí | Quy tắc tránh trùng lặp / tái lập |
| --- | --- | --- | --- |
| 1. Cohort và QC | Recording sessions/người, thời lượng ghi, cửa sổ ứng viên/được đưa vào của primary theo state và tính hợp lệ LLE khi liên quan. | Main, gọn. | Không lặp số của Figure 1 ngoài các mẫu số cần để diễn giải. |
| 2. Protocol nominal đã đóng băng | Tín hiệu Processed, windowing, SQI/stationarity, τ/m, estimator Theiler/fit/RR/PPS và đơn vị aggregation/inference trong ma trận setting gọn. | Main hoặc main ngắn cộng bảng đầy đủ ở Supplementary. | Lấy Version 1 Table II làm nguồn cho thông tin đã công bố; chi tiết audit sau này chỉ làm rõ phương pháp/diễn đạt. |
| 3. Hiệu ứng paired primary bảy metric | Median Δ, percentile CI, r_rb và q_BH của bảy metric đúng như Version 1 Table III, với vai trò headline/secondary. | Main, thiết yếu. | Figure 4 trực quan hóa pattern; Table III là nguồn số có thẩm quyền. PDF không báo raw p theo từng metric trong Table III; không lấy raw p hoặc giá trị primary thay thế từ report sau. |
| 4. Ranh giới sensitivity gọn | Nhãn và tham số theo Version 1 Tables V–VI; hướng duration theo Fig. 9; repeated-session sau Version 1 theo report dedicated với baseline riêng. | Main chỉ nếu không dùng Figure 6; nếu không thì chi tiết ở Supplementary. | Không lặp toàn bộ grid hoặc nhầm q family bốn metric với q primary family bảy metric; nêu rõ DET nhạy với embedding delay. |

## 11. Kiến trúc Supplementary

| Phần | Nội dung và chức năng trước reviewer |
| --- | --- |
| S1. Data, segmentation và QC | Coverage theo session, retained intervals, implementation SQI 5 s và stationarity chỉ theo phương sai 10 s, chuyển đổi sampling rate và visual tiền xử lý bổ sung. |
| S2. Chọn và kiểm tra độ nhạy phase-space | Các đường AMI/FNN, grid τ/m, lý do dùng embedding chung và giới hạn DET theo delay đầy đủ. |
| S3. Verification Simplex | Danh sách horizon, lựa chọn k/weights/Theiler, prediction support và window-first aggregation thực tế. Ghi lỗi diễn đạt trước đây tách khỏi kết quả tính toán; giữ tài liệu multi-duration finalized. |
| S4. Verification RQA | RR/ε/Theiler, line settings, provenance tie-safe so với legacy cache, ma trận độ nhạy đầy đủ và recurrence plots đại diện. |
| S5. Verification LLE | Theiler spectral-period, fit/QC/pair-support, perturbation tham số và minh họa estimator. |
| S6. Chi tiết PPS | Cấu hình tạo surrogate, tính rank trên mẫu hữu hạn, bằng chứng đầy đủ theo state × metric và waveform ví dụ. |
| S7. Độ nhạy duration và label | Giữ Fig. 9 và Table V của Version 1 cho các kết quả finalized theo duration/label; chỉ chép số mà PDF thực sự báo cáo. PDF không in bảng Δ đầy đủ 30/60/120/180 s. Ghi riêng bất đồng nominal Simplex Table III–VI mà không tự hòa giải. |
| S8. Unknown repeated-session dependence | Theo report dedicated sau Version 1: provenance input 20 session, baseline Simplex riêng khác Table III, 100,000 matchings đã lấy mẫu, cả bảy metric, tỷ số độ lớn, phân vị phân bố matching, quy tắc zero/tie và q support. Không dùng phân tích này thay hoặc xác nhận trực tiếp số primary PDF. |
| S9. Monte Carlo và conservative search | Prefix convergence và bốn objective local-search riêng cho mỗi headline metric, diagnostics tìm kiếm và các matching giả định tốt nhất tìm được; không nói đã tìm global optimum. |
| S10. Phân tích symbolic | Giữ Version 1 Table IV cho kết quả 0V/1V/2V ở 60/120/180 s; các kiểm tra sau Version 1 chỉ được trình bày riêng và có nguồn, không âm thầm bổ sung q vào Table IV. Giới hạn diễn giải sinh lý. |

Supplementary phải giữ khả năng audit, còn bài chính cần làm rõ lập luận RQ1→RQ2.

## 12. Bảng quyết định Main text và Supplementary

| Phân tích / bằng chứng | Main text | Supplementary | Lý do |
| --- | --- | --- | --- |
| Cohort, nhãn và QC primary | Các mẫu số gọn | Audit đầy đủ theo session/đường xử lý | Xác lập dữ liệu nào hỗ trợ cả hai RQ. |
| Cấu hình nominal của reconstruction/estimator | Quy tắc đã đóng băng thiết yếu | Phương trình, đường cong và kiểm tra implementation | Main text tái lập được mà không trở thành bài giảng phương pháp. |
| PPS RQ1 | Bằng chứng hướng xuyên phương pháp | Rank đầy đủ theo metric/state và ví dụ | PPS là tiền đề cho RQ2, giới hạn trong một null. |
| Bảy hiệu ứng primary 60 s theo Version 1 | Visual bốn headline cộng table bảy hàng đúng Table III | Vector paired và diagnostic plots, nếu có, phải ghi rõ nguồn | Đây là kết quả trung tâm; không thay số PDF bằng audit. |
| Robustness ở bốn độ dài cửa sổ | Tóm tắt hướng finalized của bốn headline theo V1 Fig. 9 | Hình và uncertainty đúng Fig. 9; không tự thêm bảng Δ chính xác chưa in trong PDF | Hỗ trợ lập luận cửa sổ hữu hạn. |
| Label rules T30/T60/S3/S5 | Một câu hoặc một hàng gọn theo V1 Table V | Các ước lượng Table V và CI/q nếu Version 1 thực sự báo cáo | Hỗ trợ robustness mà không lấn át RQ2. |
| Độ nhạy τ/m, Simplex, RQA và LLE | Cảnh báo DET theo delay cộng tóm tắt headline chọn lọc | Grid đầy đủ, audit Theiler/fit/RR/QC | Cần nêu giới hạn theo metric; các hàng đầy đủ không cần ở main. |
| Phân tích hypothetical repeated-session | Giữ hướng và biến thiên q support kèm giới hạn định danh; gắn nhãn sau Version 1 | Phân bố matching, cả bảy metric, convergence, local search từ report dedicated; nêu baseline Simplex riêng | Trực tiếp giới hạn suy luận cấp session, không xác nhận CI/q Table III. |
| Symbolic 0V/1V/2V | Một câu hỗ trợ ngắn nếu còn chỗ | Phân tích đầy đủ ở ba độ dài | Version 1 không khẳng định hỗ trợ thống kê nhất quán qua các cấu hình; symbolic không đo autonomic trực tiếp. |
| Minh họa estimator dạng textbook | Không | Ví dụ chọn lọc kiểu V1 | Figure main phải trả lời câu hỏi nghiên cứu. |

## 13. Bản đồ giới hạn claim

| Chủ đề bản thảo | Claim chính được phép | Giới hạn bắt buộc | Overclaim bị cấm |
| --- | --- | --- | --- |
| PPS/RQ1 | Có tổ chức vượt quá noisy pseudoperiodic null đã kiểm tra ở cả hai state. | 39 surrogates; p nhỏ nhất trên mẫu hữu hạn = 0.05; chỉ một null. | Chứng minh deterministic chaos hoặc loại trừ mọi khả năng ngẫu nhiên. |
| Simplex/RQ2 | Finite-horizon forecastability thấp hơn: Mean CC ↓ và Mean NRMSE ↑ theo Version 1 Table III. | Window-first aggregation; CI của Mean CC [−0.0595, −0.0043] không chứa zero; q_BH = 0.0376. Table VI có nominal Simplex khác Table III, giữ nguyên theo vai trò sensitivity. | Âm thầm thay số PDF bằng audit/duration hoặc claim unpredictability phổ quát. |
| DET | Diagonal recurrence organization thấp hơn tại embedding nominal. | Nhạy với embedding delay: median ở τ không nominal tiến gần/cắt zero; độ ổn định theo RR/Theiler có phạm vi hẹp hơn. | Physical determinism thấp hơn hoặc bất biến tham số. |
| LLE | Local trajectory divergence ước lượng thấp hơn trong fit interval đã đóng băng. | Phụ thuộc dữ liệu hữu hạn, fit/QC/embedding. | “Less chaos,” exponent thực của hệ hoặc chứng minh chaos. |
| Diễn giải autonomic | Tương thích với thay đổi cardiac autonomic modulation. | Dữ liệu symbolic là supportive/exploratory; Version 1 không khẳng định hỗ trợ thống kê nhất quán qua các cấu hình. | Hoạt động/cơ chế sympathetic hoặc parasympathetic trực tiếp. |
| Cửa sổ 60 s | “60 s là sự cân bằng thực tế giữa định vị thời gian và độ ổn định estimator trong dataset này.” | Version 1 Fig. 9 giữ các hướng headline ở 30–180 s với uncertainty lớn hơn ở 30 s; không tự bổ sung Δ chính xác của duration từ report sau. | Độ dài tối ưu phổ quát hoặc độ chính xác giống nhau ở mọi độ dài đã kiểm tra. |
| Robustness tham số | Hướng robust trong các phạm vi cụ thể đã kiểm tra với các metric cụ thể. | DET đổi dấu gần zero theo embedding delay ở Version 1 Table VI; CI và hỗ trợ có thể thay đổi. | Mọi phương pháp/metric đều không phụ thuộc tham số. |
| Label sensitivity | Các rule loại vùng transition/giới hạn độ dài episode đã kiểm tra giữ dấu median headline. | T30/T60/S3 có n = 20, S5 có n = 19; hai CI theo rule chứa zero; uncertainty của nhãn còn. | Nhãn hoàn toàn đúng hoặc kết quả miễn nhiễm với mọi định nghĩa. |
| Repeated-session dependence | Hướng median headline tồn tại qua các hypothetical two-session matchings đã lấy mẫu trong phân tích dedicated sau Version 1. | Effect size và q support thay đổi; liên kết/tương quan thật chưa biết; baseline Simplex riêng không kiểm định trực tiếp số Table III. | Đã chứng minh statistical independence hoặc có suy luận cấp participant. |
| Nhân quả và giai đoạn ngủ | Drowsy liên quan đến các PPG descriptors đã đo. | Protocol quan sát sau bữa ăn; không PSG. | Drowsiness gây thay đổi hoặc Drowsy bằng N1/NREM. |
| Ứng dụng thực tế | Descriptors có thể hỗ trợ nghiên cứu monitoring trong tương lai. | Không có classifier hoặc external/real-time validation. | Đã chứng minh hiệu năng detection. |

## 14. Bản đồ chuyển tiếp giữa các phần

| Chuyển tiếp | Cầu nối logic một câu |
| --- | --- |
| Introduction → Methods | Hai câu hỏi cần một đường signal/QC đã đóng băng và reconstruction chung để phép so sánh surrogate và state có thể diễn giải. |
| Methods → Results | Sau khi xác định cửa sổ, estimator và đơn vị suy luận, báo cáo dữ liệu hợp lệ rồi trả lời RQ1 trước RQ2. |
| RQ1 → RQ2 | Khi đã ghi nhận tổ chức vượt quá PPS null đã kiểm tra trong từng state, hỏi các thuộc tính đo được khác nhau thế nào giữa Awake và Drowsy. |
| Hiệu ứng primary → robustness | Pattern paired nominal thúc đẩy kiểm tra hướng và uncertainty có phụ thuộc độ dài cửa sổ, nhãn hoặc setting phân tích hay không. |
| Robustness → repeated-session sensitivity | Kiểm tra phương pháp và nhãn vẫn để lại một vấn đề suy luận riêng vì thiếu ánh xạ participant–session thật. |
| Repeated-session sensitivity → hỗ trợ symbolic | Khi phạm vi thống kê đã được giới hạn, pattern symbolic phụ trợ có thể cho bối cảnh sinh lý mà không gánh suy luận chính. |
| Results → Discussion | Chuỗi kết quả thực nghiệm cần diễn giải chung các descriptor bổ sung và giới hạn của chúng, không cần một danh mục metric khác. |
| Diễn giải động lực học → sinh lý | Pattern PPG đa chiều cho phép bối cảnh tim mạch thận trọng, trong khi cơ chế và giai đoạn ngủ vẫn chưa xác định. |
| Sinh lý → giới hạn | Bối cảnh được đề xuất phải được cân với nhãn video/KSS, đo ngoại vi, thiếu linkage và phụ thuộc dữ liệu hữu hạn. |
| Discussion → Conclusion | Kết thúc bằng câu trả lời RQ1 theo null cụ thể và tổng hợp RQ2 có giới hạn, rồi chỉ tới validation multimodal và participant được định danh. |

## 15. Bản đồ đóng góp và điểm yếu trước reviewer

| Khía cạnh | Đóng góp có thể bảo vệ | Thách thức có thể gặp và nơi bản thảo trả lời |
| --- | --- | --- |
| Khái niệm | Một mô tả phối hợp của forecastability, recurrence geometry và local divergence khi declining vigilance. | Căng thẳng bề ngoài CC/NRMSE–LLE: Discussion 6.2 phân biệt estimands và thang fit/horizon. |
| Nonlinear dynamics | PPS đi trước phép so sánh trạng thái; reconstruction chung và các quan sát bổ sung tránh câu chuyện chaos dựa trên một metric. | PPS chỉ kiểm tra một null và LLE phụ thuộc dữ liệu hữu hạn: Methods 4.6, Results 5.2 và Discussion 6.6 giữ claim có giới hạn. |
| Tính chặt chẽ phương pháp | QC/embedding/estimator đã đóng băng, Simplex window-first được mô tả đúng, BH trên bảy metric paired và verification audit. | Khả năng tái lập và bất đồng nội bộ PDF: Table 2, Table 3 và Supplementary S2–S6 phải giữ Table III primary, Table VI sensitivity, nêu khác biệt nominal Simplex mà không tự hòa giải. |
| Đóng góp cửa sổ ngắn | Phân tích primary 60 s, với bằng chứng finalized theo Version 1 Fig. 9 về hướng của bốn headline và uncertainty nêu rõ. | Results 5.4 và Figure 5 giữ hướng finalized 30–180 s, cho thấy uncertainty lớn hơn ở 30 s; không thay Fig. 9 bằng bảng audit sau. |
| Robustness/suy luận | Phân tích nhãn/tham số Version 1 và repeated-session giả định sau Version 1 nêu rõ hướng nào giữ và hỗ trợ nào yếu đi. | DET nhạy với delay; cohort nhỏ; thiếu linkage; baseline Simplex của repeated-session khác Table III nên không kiểm định trực tiếp CI/q primary: Results 5.5–5.6 và Discussion 6.3/6.6. |
| Phạm vi sinh lý | Pattern symbolic cho bối cảnh phụ trợ của một vigilance transition sau bữa ăn. | Không PSG, đo autonomic trực tiếp, dữ liệu multimodal hoặc cohort bên ngoài: Discussion 6.4–6.6 tránh overclaim về giai đoạn ngủ, nhân quả và population. |

Các điểm này là checklist biên tập để trình bày công bằng, không phải văn bản trả lời reviewer hoặc bảng xếp hạng đóng góp.

## 16. Kiểm tra định danh bản thảo cuối

Reviewer chỉ đọc title, abstract, figure chính và Conclusion cần hiểu đây là **nghiên cứu về sự tái tổ chức đa chiều phối hợp của động lực học PPG cửa sổ ngắn qua wakefulness-to-drowsiness transition**, với tổ chức vượt quá một PPS null cụ thể, các contrast paired theo Version 1 Table III, robustness finalized theo Fig. 9 và giới hạn suy luận được nêu rõ. Thứ bậc hiển thị phải là: tiền đề RQ1 → bốn hiệu ứng headline RQ2 → độ nhạy theo metric và unknown repeated-session dependence sau Version 1 → bối cảnh symbolic hỗ trợ. Bài phải đọc như một lập luận nonlinear-dynamics về các thuộc tính bổ sung của cùng một tín hiệu, không phải danh mục ba estimator hay một detector drowsiness đã validation.

## Trạng thái đóng băng

> Manuscript map này xác định kiến trúc lập luận, thứ bậc bằng chứng, vai trò các phần và giới hạn claim cho Manuscript Version 2. Mọi thay đổi số đã có trong Version 1 chỉ được thực hiện khi người dùng chỉ rõ kết quả mới nào supersede PDF; các bước viết tiếp theo phải tuân theo quy tắc này.
