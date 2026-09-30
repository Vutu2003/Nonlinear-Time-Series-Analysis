# Bảng chuẩn khoa học — Bản thảo Version 2

## 1. Định danh nghiên cứu và quy tắc nguồn

| Mục | Quy định đã đóng băng |
| --- | --- |
| Tên bài làm việc | Ultra-Short PPG Dynamics Across the Wakefulness-to-Drowsiness Transition: A Nonlinear Time-Series Analysis |
| Tạp chí dự kiến | Chaos, Solitons & Fractals |
| Câu hỏi | RQ1: PPG trong cửa sổ ngắn có tổ chức vượt quá noisy pseudoperiodic null đã kiểm tra hay không? RQ2: các thuộc tính động lực học bổ sung của PPG khác nhau thế nào giữa Awake và Drowsy? |
| Trạng thái | Đặc tả khoa học cho Manuscript Version 2. Phạm vi thực nghiệm đã đóng băng, trừ khi phát hiện lỗi upstream thật sự đã được xác minh. |
| **Nguồn số liệu bản thảo** | **[Manuscript Version 1](../doc/manuscript_version1.pdf) là nguồn có thẩm quyền** cho mọi kết quả, bảng, effect size, CI, p, q và robustness đã có trong PDF. Report mới hơn không thay thế các số này nếu người dùng chưa chỉ rõ kết quả nào supersede Version 1. |
| Vai trò report sau Version 1 | Làm rõ phương pháp/diễn đạt và claim boundaries; cung cấp phân tích độ nhạy mới không có trong PDF. Kết quả mới phải được gắn nhãn riêng, không nhập ngầm vào bảng primary Version 1. |

Simplex implementation và các output finalized đã dùng window-first aggregation từ đầu. Sai sót về thứ tự aggregation thuộc **mô tả tài liệu**, không phải lỗi tính toán, thống kê hay lý do chạy lại. Các report cũ có chẩn đoán khác chỉ được giữ để truy xuất provenance, không được dùng để đổi số Version 1. Nếu hai bảng ngay trong PDF khác nhau, giữ từng bảng theo đúng vai trò và ghi conflict; không tự hòa giải.

## 2. Dataset và protocol

| Mục | Thông tin đã đóng băng |
| --- | --- |
| Cohort | 20 recording sessions được giữ lại từ 10 người trưởng thành trẻ khỏe mạnh; thiết kế thu nhận ban đầu có hai session mỗi người. Sáu nam, bốn nữ; tuổi 21.8 ± 1.2 năm. Cohort nhỏ, khỏe mạnh và trẻ. |
| Thời lượng ghi | Tổng 17.40 h: Awake 11.33 h (65.35%); Drowsy 6.07 h (34.65%). Đây là thời lượng ghi được giữ lại, không phải tổng thời lượng cửa sổ sau QC. |
| Cảm biến và phần cứng | Cảm biến PPG MAX30102 với phần cứng thu nhận ESP32. PPG ngoại vi đã xử lý là tín hiệu phân tích chính. Các cửa sổ primary đến từ các bản ghi 25 và 50 Hz. |
| Bối cảnh và nhãn | Theo dõi giai đoạn giảm tỉnh táo xuất hiện tự nhiên sau bữa ăn. Nhãn Awake/Drowsy dựa trên video quan sát kết hợp Karolinska Sleepiness Scale (KSS), trong đó KSS là thước đo chủ quan chính về buồn ngủ. Không có polysomnography (PSG). Drowsy không phải giai đoạn ngủ N1/NREM đã xác nhận. |
| Liên kết định danh | Không có ánh xạ participant–session. Không thể xác định hai session thực tế của từng người; không được suy ra ánh xạ từ session ID. |

Nguồn: [Version 1, Methods và limitations](../doc/manuscript_version1.pdf); [phương pháp repeated-session](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_method.md). Version 1 Table I báo 20 paired sessions, 623 cửa sổ ứng viên Awake và 328 Drowsy ở 60 s, với tỷ lệ đạt QC 95.67% và 92.99%. Các số nguyên 596 Awake và 305 Drowsy (901/951 tổng) suy ra từ số lượng và tỷ lệ của Table I, đồng thời được [audit Simplex](../../sensitivy_data/reports/primary_simplex_windowfirst_resolution.md) xác nhận; đây là provenance của đường dữ liệu, không phải kết quả primary thay thế PDF.

## 3. Tiền xử lý và kiểm soát chất lượng tín hiệu

| Giai đoạn | Quy tắc đã đóng băng |
| --- | --- |
| Bộ lọc | Butterworth band-pass bậc hai, 0.5–8 Hz, áp dụng theo chiều thuận và ngược để lọc zero-phase. |
| Phân đoạn | Tách các khoảng Awake và Drowsy trong từng session, sau đó tạo cửa sổ không chồng lấp. Primary: 60 s; kiểm tra độ nhạy theo độ dài cửa sổ: 30, 120 và 180 s. |
| SQI | Trên tín hiệu session đã xử lý, dùng các cửa sổ cục bộ 5 s không chồng lấp. Biên độ robust A = Q0.95(x) − Q0.05(x); độ gồ ghề R = sqrt(mean(diff(x)^2)). Với từng đặc trưng, modified z trên toàn session = 0.6745(F − median(F))/max(MAD(F), machine epsilon). Đánh dấu cửa sổ cục bộ khi z_A > 4.5 hoặc z_R > 4.5. Loại mọi cửa sổ phân tích chứa sample đã đánh dấu artifact. Quy tắc chỉ xét đuôi dương là chủ ý. |
| Quasi-stationarity | **Chỉ kiểm tra độ ổn định phương sai**, trên các subwindow 10 s không chồng lấp của PPG đã xử lý: v_k = Var(x_k), ddof=0; S = [Q0.75(v) − Q0.25(v)]/max(median(v), machine epsilon). Chấp nhận khi S ≤ 0.5. Không có tiêu chí độ ổn định trung bình. |
| Điều kiện đưa vào cuối cùng | Cả SQI và stationarity của tín hiệu đã xử lý phải đạt; giữ nguyên ranh giới segment/gap và nhãn ban đầu. Primary P0: 901/951 được đưa vào; tỷ lệ đạt ở cửa sổ 60 s của Awake/Drowsy là 596/623 (95.67%) và 305/328 (92.99%). |

Nguồn: [implementation SQI](../../src/preprocessing/sqi.py), [tóm tắt verification](../../verification_result/summary.md), [Version 1](../doc/manuscript_version1.pdf).

## 4. Tái dựng không gian pha

- Delay-coordinate embedding: x_i = [x_i, x_{i−τ}, …, x_{i−(m−1)τ}]. Average Mutual Information (AMI) dùng để chọn delay; False Nearest Neighbors (FNN) hỗ trợ chọn dimension. Cấu hình chung đã đóng băng: τ = 0.16 s, m = 8. Chuyển sang số sample bằng round(τ × sampling frequency): 4 ở 25 Hz, 8 ở 50 Hz. Tái dựng chung giữ Awake và Drowsy trong cùng định nghĩa tọa độ; không chọn tham số theo p value của hiệu ứng trạng thái.
- Audit FNN sau Version 1 làm rõ grid m = 1–10, R_tol = 15, A_tol = 2, Theiler = 0 và tiêu chí 1%. Đây là chi tiết phương pháp, không thay kết quả primary trong PDF.
- [Version 1 Table VI](../doc/manuscript_version1.pdf) kiểm tra τ = 0.12/0.16/0.20 s tại m = 8 và m = 7/8/9 tại τ = 0.16 s. Theo bảng đó, Mean CC ↓, Mean NRMSE ↑ và LLE ↓ ở mọi mức; DET đổi từ +0.0025 tại τ = 0.12 s sang −0.0186 nominal và +0.0015 tại τ = 0.20 s. DET **nhạy với embedding delay**. Với m = 7/8/9, DET vẫn âm nhưng độ lớn thay đổi.
- Giá trị nominal Mean CC/Mean NRMSE trong Table VI (−0.0277/+0.0319) khác Table III primary (−0.0339/+0.0294) ngay trong Version 1. Table III chi phối kết quả primary; Table VI được trình bày đúng là bảng sensitivity. Không tự hòa giải hai bảng hoặc lấy Table VI thay Table III.

Nguồn số độ nhạy: [Version 1, Table VI](../doc/manuscript_version1.pdf). [Verification phase-space sau Version 1](../../verification_result/summary.md) chỉ bổ sung chi tiết phương pháp và bằng chứng độ nhạy, không đổi số PDF.

## 5. Simplex Projection

| Thành phần | Cấu hình đã đóng băng |
| --- | --- |
| Input | PPG Processed được chuẩn hóa trong từng cửa sổ (population SD, ddof=0); m = 8, τ = 0.16 s. |
| Dự báo | k = m + 1 = 9 láng giềng Euclidean gần nhất hợp lệ; leave-one-out state-space prediction; temporal exclusion chỉ nhận láng giềng khi khoảng cách chỉ số sample > W, với W = 1.0 s (25/50 samples ở 25/50 Hz). Trọng số exp(−d_i/d_1) được chuẩn hóa, chia đều trọng số cho các trường hợp khoảng cách chính xác bằng zero. |
| Horizons | 18 horizons tính bằng giây: 0.04, 0.08, 0.12, 0.16, 0.20, 0.28, 0.40, 0.60, 0.80, 1.00, 1.20, 1.60, 2.00, 2.40, 2.80, 3.20, 3.60, 4.00; chuyển bằng round(h × fs). |
| Metric cấp cửa sổ | Pearson CC và NRMSE; khi z-score trong từng cửa sổ, NRMSE dùng scale 1.0. Prediction support hợp lệ đầy đủ trên 901 × 18 = 16,218 bản ghi window–horizon. |
| **Thứ tự aggregation bắt buộc** | **1. Tính CC và NRMSE tại từng prediction horizon trong từng valid window. 2. Lấy mean qua 18 horizons để tạo window-level Mean CC và Mean NRMSE. 3. Lấy median qua các valid windows trong từng session × state.** Sau đó tính paired Δ theo session. |

Simplex implementation thực tế dùng đúng thứ tự window-first ở bảng trên. Một số mô tả trong report/manuscript trước đây đã viết sai thứ tự này; đó là **lỗi diễn đạt tài liệu, không phải lỗi implementation hay kết quả**. Các giá trị primary được lấy từ [Version 1, Table III](../doc/manuscript_version1.pdf): Mean CC Δ = −0.0339 và Mean NRMSE Δ = +0.0294. Các bảng audit sau này có số primary khác không có thẩm quyền thay thế Table III theo quy tắc nguồn hiện tại. Grid Theiler W = 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0 s và kiểm tra prediction support trong [verification summary](../../verification_result/summary.md) chỉ làm rõ cấu hình/phương pháp; W không được chọn theo p value tách trạng thái.

## 6. Recurrence Quantification Analysis

| Thành phần | Cấu hình đã đóng băng |
| --- | --- |
| Tái dựng/khoảng cách | Chung m = 8, τ = 0.16 s; khoảng cách Euclidean theo cặp. |
| Ngưỡng recurrence | Recurrence rate mục tiêu RR = 0.02; xác định ε tie-safe riêng cho từng cửa sổ trên các cặp hợp lệ, tolerance 5 × 10⁻⁵. Không có ε dùng chung. |
| Temporal exclusion | Theiler W = (m − 1) × τ_samples = 28/56 samples ở 25/50 Hz (khoảng 1.12 s); loại line of identity và cặp có khoảng cách ≤ W. |
| Đường và metric | Độ dài tối thiểu của đường chéo/đường thẳng đứng l_min = v_min = 2. Các metric RQA primary: DET, Lmean, LAM, TT. Aggregation session × state là median qua các cửa sổ hợp lệ. |

DET mô tả **diagonal recurrence organization**, không phải physical determinism. ΔDET nominal theo Version 1 Table III = −0.0186. Các RR = 0.01/0.02/0.03 và Theiler = 0.75/1.00/1.25 × nominal đã kiểm tra đều giữ hướng DET âm; CI tại RR = 0.01 chứa zero. LAM giữ hướng dương nhưng các CI đã kiểm tra chứa zero; TT giữ hướng dương và độ lớn nhạy với RR. Mọi claim robustness phải kèm độ nhạy DET mạnh hơn nhiều đối với embedding delay ở Mục 4. Implementation tie-safe hiện tại khác một chút so với legacy quantile cache tại 55 cửa sổ sample_12; giữ core hiện tại đã verification làm tham chiếu phương pháp, đồng thời giữ nguồn state contrast nominal đã công bố. [Tóm tắt verification](../../verification_result/summary.md), Mục 5.

## 7. Rosenstein Largest Lyapunov Exponent

| Thành phần | Cấu hình đã đóng băng |
| --- | --- |
| Estimator | Độ dốc của mean log-distance divergence theo follow time của Rosenstein; m = 8, τ = 0.16 s; một láng giềng Euclidean gần nhất hợp lệ. Đơn vị s⁻¹. |
| Temporal exclusion | Spectral mean period riêng mỗi cửa sổ (nghịch đảo spectral centroid của one-sided non-DC power spectrum); W_samples = max(round(W_seconds × fs), 1); khoảng cách giữa láng giềng > W_samples. |
| Fit và follow | Linear fit nominal 0.80–1.30 s; follow tối đa 5 s; tối thiểu 50 initial pairs, 30 pairs tại mỗi fit lag và ba fit points dùng được. Cần fit hữu hạn và R² ≥ 0.90. LLE tính được mang dấu âm không tự động bị loại. |
| Cửa sổ hợp lệ | Audit sau Version 1 ghi 872/901 (96.8%) cửa sổ LLE hợp lệ: 579 Awake và 293 Drowsy. Đây là provenance QC của estimator, không thay giá trị LLE primary trong PDF. Lấy median cửa sổ hợp lệ trong từng session × state, sau đó tính paired Δ. |

ΔLLE âm được giữ qua các khoảng fit 0.60–1.10, 0.80–1.30 và 1.00–1.50 s; Theiler 0.75/1.00/1.25 ×; ngưỡng R² 0.90 và 0.95; và grid embedding đã kiểm tra. Trong verification sau Version 1, siết R² lên 0.95 làm retention giảm còn 734/901 (81.5%) và cho median Δ = −0.030618; đây là kết quả độ nhạy riêng, không thay LLE primary của Version 1. Với m = 7/8/9, độ lớn thay đổi tối đa 34.24% so với nominal. Diễn giải LLE là **mô tả local trajectory divergence trên dữ liệu hữu hạn**, không bao giờ là bằng chứng deterministic chaos. [Tóm tắt verification](../../verification_result/summary.md), Mục 3 và 6.

## 8. Kiểm định PPS surrogate

- Pseudoperiodic surrogates (PPS) kiểm tra một **noisy pseudoperiodic null cụ thể**, giữ cấu trúc dao động tổng quát nhưng làm thay đổi tiến triển quỹ đạo cục bộ. Theo [Version 1, Methods và Fig. 7](../doc/manuscript_version1.pdf), mỗi cửa sổ PPG gốc hợp lệ được so với M = 39 PPS realizations trên CC, NRMSE, DET, Lmean, LAM, TT và LLE hợp lệ. Kiểm định rank hai phía xếp hạng 40 giá trị; p nhỏ nhất có thể đạt là 0.05. Tỷ lệ bác bỏ cấp cửa sổ có tính mô tả, không phải kiểm định paired Awake–Drowsy trên 20 sessions.
- Hướng observed-minus-PPS trong cả Awake và Drowsy theo Version 1: CC, DET, Lmean và LLE > PPS; NRMSE, LAM và TT < PPS. Fig. 7 là nguồn có thẩm quyền cho pattern kết quả và mức độ nhất quán được hiển thị; không lấy tỷ lệ số chính xác từ bảng audit sau này để thay figure/bảng trong PDF.
- Kết luận được phép: PPG quan sát có tổ chức thời gian/động lực học mà noisy pseudoperiodic null đã kiểm tra không tái tạo đầy đủ. **Bác bỏ PPS không chứng minh deterministic chaos** và không loại trừ mọi cơ chế ngẫu nhiên hoặc không dừng khác.

## 9. Khung thống kê

Các cửa sổ là đơn vị tính toán; **20 recording sessions** là các đơn vị suy luận ghép cặp primary. Với mỗi metric, trước tiên lấy median cửa sổ hợp lệ trong từng session × state (với Simplex, mean horizon được tính trước); sau đó tính Δ_i = Drowsy_i − Awake_i. Báo cáo median(Δ_i), p của Wilcoxon signed-rank hai phía, matched-pairs rank-biserial r_rb = (W⁺ − W⁻)/(W⁺ + W⁻), và percentile bootstrap 95% CI cho median với **20,000 lần resample paired-session**. CI của median và p của signed-rank nhắm đến hai tóm tắt thống kê khác nhau và không nhất thiết cho quyết định ngưỡng giống nhau. Áp dụng Benjamini–Hochberg FDR monotone một lần trên **đúng bảy metric P0 60 s nominal: Mean CC, Mean NRMSE, DET, Lmean, LAM, TT và LLE**. Các phân tích độ nhạy là kiểm tra robustness, không phải các phần tử bổ sung của family confirmatory này. n = 20 primary ở cấp session; sự phụ thuộc chưa biết giữa các session của cùng một người chỉ được xử lý bằng phân tích độ nhạy ở Mục 15. Nguồn số liệu primary và quy tắc thống kê: [Version 1, Methods và Table III](../doc/manuscript_version1.pdf). [Phương pháp repeated-session sau Version 1](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_method.md) chỉ áp dụng cho phân tích riêng ở Mục 15.

## 10. Kết quả primary 60-s P0 Processed theo Version 1

**[Version 1 Table III](../doc/manuscript_version1.pdf) là bảng primary có thẩm quyền.** Mọi Δ = Drowsy − Awake; ΔLLE có đơn vị s⁻¹. PDF báo cáo median Δ, bootstrap 95% CI, r_rb và q_BH ở độ chính xác hiển thị dưới đây; **không báo cáo raw p theo từng metric trong Table III**, nên không chèn p lấy từ report sau này. Vai trò headline/secondary không thay đổi.

| Metric | Median Δ | Bootstrap 95% CI | r_rb | p trong Table III | q_BH | Vai trò bằng chứng |
| --- | ---: | --- | ---: | --- | ---: | --- |
| Mean CC | −0.0339 | [−0.0595, −0.0043] | −0.581 | không báo | 0.0376 | headline |
| Mean NRMSE | +0.0294 | [+0.0047, +0.0530] | +0.667 | không báo | 0.0255 | headline |
| DET | −0.0186 | [−0.0364, −0.0069] | −0.581 | không báo | 0.0376 | headline |
| Lmean | −0.0630 | [−0.1247, −0.0139] | −0.486 | không báo | 0.0816 | secondary |
| LAM | +0.0165 | [−0.0044, +0.0635] | +0.381 | không báo | 0.1667 | secondary |
| TT | +0.0095 | [−0.0034, +0.0160] | +0.333 | không báo | 0.2024 | secondary |
| LLE | −0.0376 | [−0.0537, −0.0230] | −0.810 | không báo | 0.0050 | headline |

Theo Table III, CI của Mean CC **không chứa zero**; q_BH < 0.05 cho Mean CC, Mean NRMSE, DET và LLE. Bốn hướng headline là Mean CC ↓, Mean NRMSE ↑, DET ↓ và LLE ↓, tương ứng finite-horizon forecastability thấp hơn, diagonal recurrence organization giảm và local trajectory divergence thấp hơn. Forecastability và divergence là hai thuộc tính khác nhau; cùng giảm không tự thân mâu thuẫn. Không đặt chúng trên trục “more/less chaos” hoặc “greater/lower complexity”.

## 11. Các phát hiện headline

Bốn hiệu ứng headline nominal 60 s là **Mean CC ↓, Mean NRMSE ↑, DET ↓ và LLE ↓**. Các mô tả tương ứng là finite-horizon forecastability thấp hơn, diagonal recurrence organization thấp hơn và local trajectory divergence ước lượng thấp hơn ở Drowsy. Forecastability và local divergence mô tả các thuộc tính khác nhau nên cùng giảm không tự thân mâu thuẫn. Vai trò headline của DET không xóa đi độ nhạy của nó với embedding delay. Cả PPS lẫn LLE đều không cho phép kết luận deterministic chaos; không được tóm tắt các thay đổi này như một mức tăng/giảm đơn chiều của “complexity”.

## 12. Robustness theo độ dài cửa sổ

[Version 1, Fig. 9 và phần Results tương ứng](../doc/manuscript_version1.pdf) là nguồn có thẩm quyền cho robustness theo cửa sổ 30, 60, 120 và 180 s. Figure cho thấy cả bốn hướng headline được giữ qua các độ dài đã kiểm tra: Mean CC ↓, Mean NRMSE ↑, DET ↓ và LLE ↓. Cửa sổ 30 s có uncertainty lớn hơn. Fig. 9 **không in một bảng Δ chính xác cho từng độ dài**, nên tài liệu này không tự nhập các số Δ 30/120/180 s từ report mới hơn làm số manuscript của Version 1.

| Metric | 30 s | 60 s | 120 s | 180 s | Diễn giải từ Version 1 |
| --- | --- | --- | --- | --- | --- |
| Mean CC | ↓ | ↓ | ↓ | ↓ | Hướng âm giữ qua cả bốn độ dài; giá trị primary 60 s ở Table III là −0.0339. |
| Mean NRMSE | ↑ | ↑ | ↑ | ↑ | Hướng dương giữ qua cả bốn độ dài; giá trị primary 60 s ở Table III là +0.0294. |
| DET | ↓ | ↓ | ↓ | ↓ | Hướng âm giữ; uncertainty ở 30 s lớn hơn, và 180 s vẫn có bất định đáng chú ý. |
| LLE | ↓ | ↓ | ↓ | ↓ | Hướng âm giữ; mức giảm có xu hướng rõ hơn khi cửa sổ dài hơn. |

Kết quả window-length này **finalized**, không pending và không cần regenerate do lỗi mô tả aggregation. Cửa sổ 60 s là **sự cân bằng thực tế giữa định vị thời gian và độ ổn định estimator trong dataset này**, không phải optimum phổ quát.

## 13. Độ nhạy với định nghĩa nhãn

Theo [Version 1 Table V và phần Results](../doc/manuscript_version1.pdf), T30/T60 loại sample trong khoảng ±30/±60 s quanh state transition; S3/S5 giữ episode liên tục có thời lượng ít nhất 3/5 min. Không lọc hoặc gán nhãn lại tín hiệu. Table V dùng Δ = Drowsy − Awake; P0 là nhãn primary.

| Metric | P0 | T30 | T60 | S3 | S5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean CC | −0.0339 | −0.0482 | −0.0251 | −0.0361 | −0.0337 |
| Mean NRMSE | +0.0294 | +0.0406 | +0.0278 | +0.0357 | +0.0367 |
| DET | −0.0186 | −0.0183 | −0.0167 | −0.0189 | −0.0213 |
| LLE | −0.0376 | −0.0322 | −0.0393 | −0.0344 | −0.0321 |

Version 1 báo cáo T30/T60/S3 có 20 paired sessions, S5 có 19; 16/16 hiệu ứng theo hướng headline và q_BH < 0.05 trong các family rule tương ứng. 14/16 bootstrap CI không chứa zero; T60–Mean CC và T30–LLE chứa zero. Các q của rule không thay q primary Table III. Kết quả gợi ý vùng sát transition hoặc episode ngắn không phải yếu tố chi phối chính trong các định nghĩa đã kiểm tra; uncertainty của nhãn vẫn còn. Chi tiết audit sau Version 1 có thể làm rõ implementation nhưng không thay các số Table V.

## 14. Độ nhạy tham số NTSA

[Version 1 Table VI](../doc/manuscript_version1.pdf) là nguồn có thẩm quyền cho các median Δ của phân tích reconstruction sensitivity. Cột τ thay đổi delay ở m = 8; cột m thay đổi dimension ở τ = 0.16 s. Các số nominal ở bảng này giữ đúng vai trò sensitivity, không thay primary Table III.

| Metric | τ 0.12 s | τ 0.16 s | τ 0.20 s | m 7 | m 8 | m 9 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Mean CC | −0.0317 | −0.0277 | −0.0316 | −0.0307 | −0.0277 | −0.0251 |
| Mean NRMSE | +0.0321 | +0.0319 | +0.0296 | +0.0377 | +0.0319 | +0.0315 |
| DET | +0.0025 | −0.0186 | +0.0015 | −0.0145 | −0.0186 | −0.0200 |
| LLE | −0.0361 | −0.0376 | −0.0464 | −0.0285 | −0.0376 | −0.0247 |

Mean CC ↓, Mean NRMSE ↑ và LLE ↓ giữ hướng qua grid đã kiểm tra. **DET nhạy với embedding delay**: ở τ = 0.12/0.20 s median dương, gần zero; không gọi DET bất biến. Theo Version 1, DET giữ hướng dưới perturbation RR/RQA Theiler; LLE giữ hướng âm qua fit interval, ngưỡng chất lượng và local Theiler đã khảo sát; Simplex ổn định quanh Theiler nominal. Các verification report sau Version 1 có thể thêm chi tiết setting, QC và CI/q cho phân tích độ nhạy, nhưng không được dùng để thay các Δ Table III hoặc Table VI. Chỉ dùng “robust trong phạm vi đã kiểm tra” khi metric/range cụ thể hỗ trợ. Khác biệt giữa Table III và Table VI được ghi trong Mục 22.

## 15. Độ nhạy với sự phụ thuộc repeated-session chưa biết

Không có liên kết participant–session thực tế. Đây là **phân tích sau Version 1**, không có trong PDF, nên các số bên dưới lấy từ [report dedicated finalized](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_results.md). Input của report dùng một baseline Simplex khác Table III; vì vậy phân tích này không kiểm định trực tiếp độ lớn, CI hay q primary của Version 1 và không được dùng để thay chúng. Mô hình độ nhạy finalized phân hoạch 20 vector Δ cấp session từ 10 participants thành mười **hypothetical two-session clusters**, tính Δ* = (Δ_i + Δ_j)/2 cho từng cluster, rồi thực hiện Wilcoxon exact hai phía và BH bảy metric trên mười chênh lệch cluster. Trong 654,729,075 perfect matchings có thể có, 100,000 cách được lấy mẫu có hoàn lại với seed định trước; 99,990 cách là duy nhất. Các phân vị theo matching là phân bố trên các phép gán giả định, **không** phải bootstrap CI hay khoảng ở cấp participant. [Phương pháp đã đóng băng](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_method.md); [kết quả](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_results.md).

| Headline metric | Median Δ* qua mẫu | Δ* 2.5–97.5% qua mẫu | Median tỷ số độ lớn so với gốc | Tỷ lệ median giữ hướng kỳ vọng | q < 0.05 trong các matching |
| --- | ---: | --- | ---: | ---: | ---: |
| Mean CC | −0.024205 | [−0.035921, −0.014749] | 0.874 | 100.000% | 19.36% |
| Mean NRMSE | +0.026313 | [+0.018469, +0.034258] | 0.826 | 100.000% | 27.82% |
| DET | −0.018069 | [−0.025544, −0.010024] | 0.969 | 100.000% | 22.59% |
| LLE | −0.035608 s⁻¹ | [−0.044613, −0.026557] s⁻¹ | 0.948 | 100.000% | 79.69% |

Trong các prefix theo cùng chuỗi cố định 1,000/10,000/50,000/100,000, tỷ lệ giữ dấu của mọi headline đều là 100%; giữa 50,000 và 100,000, thay đổi mức hỗ trợ q của headline ≤0.116 điểm phần trăm. Local search với 100 điểm bắt đầu đã định trước tìm được median Δ* yếu hơn nhưng vẫn giữ dấu: CC −0.003904, NRMSE +0.012076, DET −0.004709, LLE −0.019763 s⁻¹. Các objective riêng biệt tìm được q ≥ 0.05 cho cả bốn metric, kể cả LLE; đây là kết quả local-search, **không phải cực trị toàn cục đã chứng minh**. Theo input riêng của report sau Version 1, hướng của các hiệu ứng chính được giữ trong cả 100,000 phép ghép cluster giả định đã lấy mẫu, còn độ lớn và hỗ trợ suy luận thay đổi sau khi gộp thành mười đơn vị giả định. Đây là bằng chứng độ nhạy bổ sung có giới hạn, không phải p/q cấp participant cho bảng primary Version 1. Điều này **không chứng minh statistical independence, không khôi phục danh tính participant, không xác lập suy luận cấp participant và không ước lượng tương quan thực tế giữa các session của cùng một người**.

## 16. Phân tích symbolic

[Version 1 Table IV và phần Results](../doc/manuscript_version1.pdf) là nguồn số liệu cho ba family pattern symbolic ở 60/120/180 s. Median paired Δ tính bằng điểm phần trăm; cột cuối là số session giữ cùng hướng qua cả ba độ dài.

| Pattern | 60 s Δ | 120 s Δ | 180 s Δ | Cùng hướng |
| --- | ---: | ---: | ---: | ---: |
| 0V | +4.04 | +2.32 | +4.58 | 17/20 |
| 1V | +0.41 | +0.03 | −0.06 | 11/20 |
| 2V | −0.91 | −2.30 | −2.67 | 14/20 |

0V tăng theo hướng, 2V giảm theo hướng, còn 1V gần zero/không nhất quán. Version 1 chỉ xem pattern này là **supportive/exploratory**, không báo cáo hỗ trợ thống kê nhất quán qua các cấu hình. Không nhập các q chi tiết từ bảng hậu kiểm vào Table IV nếu chưa được người dùng chỉ định supersede. Pattern 0V ↑ / 2V ↓ tương thích với thay đổi cardiac autonomic modulation; symbolic PPG ngoại vi **không đo trực tiếp hoạt động sympathetic hoặc parasympathetic** và không chứng minh cơ chế autonomic cụ thể.

## 17. Thứ bậc bằng chứng và diễn giải

1. **Primary/headline:** Mean CC, Mean NRMSE, DET, LLE. DET vẫn là headline, nhưng phải nêu cùng độ nhạy với embedding delay.
2. **Secondary:** Lmean, LAM, TT. Các dấu nominal chỉ có tính mô tả; không metric nào có q < 0.05 trong family bảy metric. Theo Table III, bootstrap CI của Lmean không chứa zero nhưng q_BH = 0.0816; báo cáo cả hai thay vì nâng nó thành bằng chứng headline.
3. **Supportive/exploratory:** symbolic dynamics 0V, 1V, 2V; Version 1 không khẳng định hỗ trợ thống kê nhất quán qua các cấu hình.

Kết quả trung tâm là sự liên hệ phối hợp giữa Drowsy với finite-horizon forecastability thấp hơn, diagonal recurrence organization thấp hơn và local trajectory divergence thấp hơn. Ba descriptor đo các thuộc tính bổ sung cho nhau; không được xếp chúng trên một trục chaos hoặc complexity đơn chiều.

## 18. Giới hạn

- Cohort nhỏ gồm người trưởng thành trẻ khỏe mạnh và protocol sau bữa ăn giới hạn khả năng khái quát hóa.
- Nhãn dựa trên video/KSS, không có PSG; Drowsy không thể đồng nhất với N1 hoặc NREM, và sự bất định của nhãn vẫn còn sau các rule độ nhạy đã kiểm tra.
- Chỉ có PPG ngoại vi, không đo đồng thời EEG, hô hấp, huyết áp liên tục hay xác minh multimodal khác, nên không thể định vị cơ chế sinh lý; không có cohort validation bên ngoài.
- Không có liên kết participant–session; không thể ước lượng tương quan repeated-session thực tế hoặc thực hiện suy luận cấp participant. Phân tích primary với n = 20 session có thể đánh giá quá lạc quan độ chính xác nếu các session của cùng người tương quan.
- Dữ liệu hữu hạn 30–180 s, tính hợp lệ của estimator và bộ lọc chất lượng ảnh hưởng đến suy luận. DET phụ thuộc reconstruction delay; retention/độ lớn LLE phụ thuộc các setting fit/QC/embedding đã chọn. Kết quả bị giới hạn bởi phạm vi tham số đã kiểm tra.
- PPS kiểm tra một noisy pseudoperiodic null cụ thể. Bác bỏ không chứng minh chaos. LLE là descriptor trên dữ liệu hữu hạn, không chứng minh Lyapunov exponent xác định hay chaos.
- Fig. 9 của Version 1 giữ bốn hướng headline qua 30/60/120/180 s, với uncertainty lớn hơn ở 30 s. Khác biệt nội bộ giữa Table III và Table VI về Simplex nominal được ghi tại Mục 22; không tự hòa giải hoặc suy ra lỗi tính toán từ việc sửa diễn đạt.

## 19. Giới hạn claim

| Chủ đề | Cách diễn đạt được phép | Cách diễn đạt không được phép |
| --- | --- | --- |
| PPS | “Tổ chức vượt quá noisy pseudoperiodic null đã kiểm tra.” | “Chứng minh deterministic chaos”; “loại trừ mọi giải thích ngẫu nhiên.” |
| LLE | “Local trajectory divergence ước lượng thấp hơn trong các cửa sổ hữu hạn.” | “Less chaos”; “Lyapunov exponent xác định đã được xác minh.” |
| DET | “Diagonal recurrence organization thấp hơn ở embedding nominal; nhạy với delay.” | “Physical determinism giảm”; “DET bất biến với tham số.” |
| Diễn giải autonomic | “Tương thích với thay đổi cardiac autonomic modulation.” | “Kích hoạt sympathetic trực tiếp” hoặc “giảm parasympathetic trực tiếp.” |
| Cửa sổ 60 s | “Sự cân bằng thực tế trong dataset này.” | “Độ dài cửa sổ tối ưu phổ quát.” |
| Tham số | “Robust trong phạm vi cụ thể đã kiểm tra” khi được tài liệu hỗ trợ. | “Không phụ thuộc tham số.” |
| Quan hệ nhân quả | “Liên quan đến Drowsy/declining vigilance.” | “Drowsiness gây ra thay đổi động lực học.” |
| Repeated sessions | “Độ nhạy đối với unknown repeated-session dependence dưới hypothetical two-session clustering.” | “Đã chứng minh statistical independence”; “đã xác lập hiệu ứng cấp participant”; “đã khôi phục participant ID.” |
| Giai đoạn ngủ | “Drowsy được xác định bằng video/KSS.” | “Giấc ngủ N1/NREM được PSG xác nhận.” |
| Window robustness | “Cả bốn hướng headline được giữ trong các cửa sổ 30–180 s đã kiểm tra.” | “60 s tối ưu phổ quát”; “uncertainty giống nhau tại mọi độ dài.” |

## 20. Thuật ngữ canonical

Dùng **Awake**, **Drowsy**, **wakefulness-to-drowsiness transition**, **declining vigilance**, **finite-horizon forecastability**, **recurrence organization**, **diagonal recurrence organization**, **local trajectory divergence**, **session-level inference**, **participant–session linkage**, **unknown repeated-session dependence**, **hypothetical two-session clustering** và **supportive symbolic analysis**. Tránh hoặc phải giới hạn chặt chẽ các thuật ngữ “chaos,” “complexity increase/decrease,” “determinism” như một claim vật lý, “subject-level,” “independent sessions,” “sleep stage,” “optimal window,” cùng các nhãn nhân quả/autonomic.

## 21. Ứng viên cho main text và Supplementary

| Phân tích | Vị trí dự kiến | Điều kiện |
| --- | --- | --- |
| Hiệu ứng primary 60 s, PPS, diễn giải headline | Có thể ở main text | Dùng số Version 1 Table III và claim PPS giới hạn theo null đã kiểm tra. |
| Robustness theo độ dài cửa sổ | Có thể ở main text | Dùng Fig. 9 của Version 1: bốn hướng headline giữ qua 30/60/120/180 s, uncertainty lớn hơn ở 30 s; không tự thêm bảng Δ chính xác chưa có trong PDF. |
| Label sensitivity, parameter sensitivity, repeated-session dependence | Kết quả ngắn trong main text; chi tiết có thể ở Supplementary | Giữ giới hạn DET theo delay và giới hạn suy luận của hypothetical clusters. |
| Symbolic analysis, verification estimator chi tiết, hồ sơ convergence/local search | Có thể ở Supplementary | Symbolic là exploratory; local search không chứng minh global optimum. |

Việc chọn vị trí này chỉ chuẩn bị cho Step 2, chưa phải layout cuối cùng.

## 22. Log xung đột, nguồn và diễn đạt bị thay thế

| Mục | Nguồn/diễn đạt khác | Quy tắc có thẩm quyền cho Version 2 | Giới hạn |
| --- | --- | --- | --- |
| Kết quả primary Simplex | Audit/report sau Version 1 ghi các số Mean CC/Mean NRMSE khác Table III. | **Version 1 Table III**: Mean CC Δ −0.0339, CI [−0.0595, −0.0043], r_rb −0.581, q_BH 0.0376; Mean NRMSE Δ +0.0294, CI [+0.0047, +0.0530], r_rb +0.667, q_BH 0.0255. | Không dùng số report sau để thay bảng primary nếu không có chỉ định supersede rõ ràng. Lỗi diễn đạt aggregation không phải bằng chứng sai implementation. |
| DET và các metric primary khác | Bảng BH hậu kiểm có thể ghi q hoặc precision khác. | Giữ toàn bộ bảy hàng đúng độ chính xác hiển thị của **Version 1 Table III**; raw p không được Table III báo cáo. | Không nhập p, q hoặc CI từ report sau vào Table III một cách âm thầm. |
| Bất đồng nội bộ Version 1 | Table VI ghi nominal Mean CC −0.0277 và Mean NRMSE +0.0319; Table III ghi −0.0339 và +0.0294. | Table III là kết quả primary; Table VI là bảng reconstruction sensitivity. | **Conflict chưa được hòa giải.** Cả hai ở trong PDF có thẩm quyền; giữ đúng vai trò nguồn và không tự suy ra nguyên nhân. |
| Diễn đạt Simplex aggregation | Một số report/manuscript mô tả mean_h(median_w(metric_w,h)). | Implementation thực tế dùng median_w(mean_h(metric_w,h)): mean horizons trong từng valid window rồi median windows trong session × state. | **Sửa documentation wording ≠ sửa kết quả tính toán.** Không vô hiệu hóa Table III, Fig. 9 hoặc yêu cầu rerun. |
| Window-length robustness | Bảng số chi tiết ngoài PDF có thể thêm Δ theo độ dài. | **Version 1 Fig. 9 và Results** chốt bốn hướng headline từ 30–180 s và uncertainty lớn hơn ở 30 s. | Fig. 9 không in bảng Δ đầy đủ; không thay số/bằng chứng PDF bằng output hậu kiểm. |
| Label và symbolic | Report sau cung cấp precision hoặc q chi tiết hơn. | **Version 1 Table V/IV** chốt các giá trị đã công bố; report mới chỉ làm rõ phương pháp hoặc phân tích mới. | Không thêm số hậu kiểm như thể chúng đã supersede PDF. |
| Unknown repeated-session dependence | Phân tích dedicated hoàn thành sau Version 1 dùng baseline Simplex riêng, khác Table III. | Dùng [report dedicated](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_results.md) **chỉ cho phân tích mới này**. | Không dùng các Δ*, CI phân bố matching hoặc q-support của nó để thay hoặc xác nhận p/q primary Version 1. Không chứng minh statistical independence hoặc suy luận cấp participant. |
| Claim chaos/autonomic/window | Cách diễn đạt quá mức có thể đồng nhất PPS/LLE với chaos, symbolic với autonomic activity trực tiếp hoặc 60 s với optimum. | PPS chỉ giới hạn một null; LLE là finite-data descriptor; symbolic supportive; 60 s là practical compromise. | Không có cơ chế sinh lý trực tiếp, chaos proof hoặc optimum phổ quát. |

## 23. Checklist validation cuối

- [x] Mọi số primary, effect size, CI và q lấy từ Version 1 Table III; raw p không được bịa hoặc nhập từ report sau.
- [x] Table IV/V/VI và Fig. 9 của Version 1 giữ vai trò nguồn riêng; bất đồng Table III–VI được ghi rõ mà không tự hòa giải.
- [x] Thứ tự aggregation Simplex canonical đúng; lỗi trước đây thuộc diễn đạt, không phải implementation hoặc kết quả.
- [x] Cả bốn hướng headline giữ qua 30–180 s theo Fig. 9; không gọi robustness pending hoặc yêu cầu rerun.
- [x] Kết quả repeated-session sau Version 1 được gắn nhãn riêng và không thay primary; thiếu participant–session linkage được nêu rõ.
- [x] Độ nhạy DET với embedding delay, giới hạn PPS/LLE/symbolic và phạm vi 60 s thực tế vẫn còn.
- [x] Không có claim statistical independence, deterministic chaos, autonomic trực tiếp, optimum phổ quát hoặc nhân quả.

## Trạng thái đóng băng

> File này là nguồn chuẩn khoa học cho Manuscript Version 2. Giữ các số đã có trong Version 1, trừ khi người dùng chỉ rõ kết quả mới nào supersede PDF. Mọi phân tích mới sau Version 1 phải có nguồn và nhãn riêng; không tự thay số primary hoặc robustness đã chốt.
