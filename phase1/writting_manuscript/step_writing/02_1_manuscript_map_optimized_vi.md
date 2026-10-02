# Step 2.1 — Bản đồ bản thảo tinh gọn cho Manuscript Version 2

**Quy tắc nguồn.** [Manuscript Version 1](../doc/manuscript_version1.pdf) quyết định mọi số liệu và kết quả robustness đã xuất hiện trong PDF; [Step 1 hiện có](1_master_canonical_sheet_vi.md) giữ đặc tả kỹ thuật, còn [Step 2 hiện có](2_manuscript_map_vi.md) giữ bản đồ chi tiết. Báo cáo sau Version 1 chỉ bổ sung phương pháp, giới hạn claim hoặc phân tích mới. Table III là nguồn kết quả primary; Table VI là nguồn độ nhạy reconstruction. Hai bảng có số nominal Simplex khác nhau: giữ đúng vai trò từng bảng, không tự hòa giải. Sửa mô tả thứ tự Simplex aggregation là sửa tài liệu; implementation và các kết quả finalized, gồm robustness theo độ dài cửa sổ, không bị thay đổi.

## 1. Định danh bản thảo

**Vấn đề → khoảng trống → đóng góp.** Declining vigilance sau bữa ăn có thể đi kèm thay đổi trong PPG, nhưng động lực học trực tiếp của waveform qua Awake → Drowsy ở cửa sổ ngắn còn chưa được mô tả đầy đủ. Bài này kiểm tra tổ chức của PPG so với một noisy pseudoperiodic null cụ thể, rồi mô tả sự **tái tổ chức phối hợp của finite-horizon forecastability, recurrence organization và local trajectory divergence** khi chuyển trạng thái. Đây là nghiên cứu về các thuộc tính động lực học bổ sung cho nhau, không phải một danh mục thuật toán Simplex/RQA/LLE, một drowsiness classifier hay một thang “more chaos/less chaos”.

**RQ1:** PPG cửa sổ ngắn ở Awake và Drowsy có tổ chức vượt quá noisy pseudoperiodic null đã kiểm tra không?  
**RQ2:** Drowsiness liên quan thế nào đến các thuộc tính động lực học bổ sung của PPG cửa sổ ngắn?

**Thứ bậc bằng chứng:** headline — Mean CC, Mean NRMSE, DET, LLE; secondary — Lmean, LAM, TT; supportive/exploratory — symbolic dynamics. DET giữ vai trò headline cùng caveat bắt buộc về embedding delay.

## 2. Introduction: bốn đoạn

| Đoạn | Mục đích và nội dung thiết yếu | Chuyển tiếp; claim cần tránh |
| --- | --- | --- |
| 1 | Declining vigilance, giá trị đo PPG và xu hướng dùng đặc trưng quy ước hoặc classifier. | Chuyển từ khả năng theo dõi sang câu hỏi waveform tổ chức ra sao; không đồng nhất Drowsy với PSG-confirmed sleep. |
| 2 | PPG là tín hiệu dao động phù hợp với kiểm tra động lực học; khoảng trống là tái tổ chức trực tiếp giữa Awake và Drowsy trong cửa sổ ngắn. | Chuyển sang yêu cầu nhiều góc nhìn; không tuyên bố chưa từng có nghiên cứu nonlinear PPG. |
| 3 | Giải thích ngắn vì sao forecastability, recurrence organization và local divergence đo các thuộc tính khác nhau; nêu giới hạn quan sát ngắn. | Chuyển từ ba thuộc tính sang hai câu hỏi kiểm tra; không gộp thành một complexity score. |
| 4 | Nêu RQ1, RQ2 và đóng góp là mô tả tái tổ chức phối hợp với phạm vi suy luận rõ. | Dẫn vào thiết kế chung ở Methods; không hứa hẹn chứng minh chaos, cơ chế autonomic hay hiệu năng detector. |

## 3. Methods: năm tiểu mục

| Tiểu mục | Giữ trong main text | Chuyển Supplementary | Ranh giới diễn đạt |
| --- | --- | --- | --- |
| 3.1 Dataset, protocol và preprocessing | 20 recording sessions từ 10 người; PPG sau bữa ăn; nhãn video/KSS; tín hiệu Processed và lọc thiết yếu. | Thu nhận, coverage và filter chi tiết. | Session là đơn vị suy luận; không gọi 20 session là 20 người độc lập. |
| 3.2 Segmentation, QC  | Cửa sổ primary 60 s không chồng lấp; hai mask QC;| Quy tắc QC.
| 3.3 Phân tích động lực học | AMI/FNN và grid reconstruction đầy đủ. | Không thêm tiêu chí QC chưa có hoặc chọn embedding theo hiệu ứng trạng thái. embedding chung cho hai state. |Simplex cho forecastability; RQA cho recurrence; Rosenstein LLE cho local divergence. Ghi đúng Simplex: metric theo horizon trong mỗi window → mean qua horizons trong window → median qua valid windows của session × state. | Tham số, phương trình và verification estimator. | Sai mô tả aggregation trước đây là lỗi wording, không phải lỗi tính toán; LLE/DET không mang nghĩa chaos/determinism vật lý. |
| 3.4 PPS surrogate testing | Null noisy pseudoperiodic cụ thể, 39 surrogates và so sánh original–PPS cho RQ1. | Cách sinh PPS, rank và hình ví dụ. | Bác bỏ null này không chứng minh deterministic chaos. |
| 3.5 Thống kê và sensitivity | Paired Δ = Drowsy − Awake ở cấp session; CI bootstrap và BH-FDR cho bảy metric nominal; một câu về duration, label, parameter và unknown repeated-session dependence. | Toàn bộ grid, diagnostics và [phân tích repeated-session sau Version 1](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_results.md). | Hypothetical pairing không khôi phục participant ID; baseline Simplex riêng của phân tích mới không thay hoặc xác nhận trực tiếp Table III. |

## 4. Results: ba tiểu mục

Mở Results bằng 1–2 câu về dữ liệu/QC; trình tự chính là **RQ1 → RQ2 → defense layer**. Symbolic là đoạn cuối ngắn của 4.3, không cần tiểu mục riêng.

### 4.1 RQ1 — Tổ chức vượt quá PPS

**Câu hỏi:** PPG gốc trong mỗi state khác noisy pseudoperiodic ensemble đã kiểm tra ra sao? **Bằng chứng:** Version 1 Fig. 7 cho các hướng original-minus-PPS trên prediction, RQA và LLE ở Awake và Drowsy. **Takeaway:** cả hai state có tổ chức mà null này không tái tạo đầy đủ. **Ranh giới:** tỷ lệ bác bỏ cấp window chỉ mô tả phép so với null; không phải bằng chứng chaos hoặc phép so sánh paired giữa hai state.

### 4.2 RQ2 — Tái tổ chức Awake–Drowsy

**Câu hỏi:** các thuộc tính bổ sung thay đổi cùng nhau thế nào? Đặt [Version 1 Table III](../doc/manuscript_version1.pdf) ở trung tâm; các số dưới đây là median paired Δ, bootstrap 95% CI và q_BH của family bảy metric:

| Headline | Δ (Drowsy − Awake) | 95% CI | q_BH | Vai trò trong lập luận |
| --- | ---: | --- | ---: | --- |
| Mean CC | −0.0339 | [−0.0595, −0.0043] | 0.0376 | Forecastability ↓ |
| Mean NRMSE | +0.0294 | [+0.0047, +0.0530] | 0.0255 | Forecastability ↓ |
| DET | −0.0186 | [−0.0364, −0.0069] | 0.0376 | Diagonal recurrence organization ↓ tại embedding nominal |
| LLE | −0.0376 s⁻¹ | [−0.0537, −0.0230] s⁻¹ | 0.0050 | Local trajectory divergence ước lượng ↓ |

**Takeaway:** Drowsy gắn với tái tổ chức phối hợp trên ba thuộc tính. Lmean/LAM/TT ở cùng bảng là bối cảnh secondary, không nâng thành headline; raw p theo metric không được Table III báo cáo. **Ranh giới:** không suy ra mức chaos, cơ chế sinh lý hay quan hệ nhân quả từ các dấu này.

### 4.3 Robustness và phạm vi suy luận

**Câu hỏi:** hướng primary giữ đến đâu khi đổi độ dài cửa sổ, nhãn, tham số và giả định dependence? **Bằng chứng cốt lõi:** Version 1 Fig. 9 giữ cả bốn hướng Mean CC ↓, Mean NRMSE ↑, DET ↓, LLE ↓ ở 30/60/120/180 s; uncertainty lớn hơn ở 30 s. Version 1 Table V hỗ trợ độ nhạy nhãn; Table VI cho thấy **DET nhạy với embedding delay**, dù các hướng prediction và LLE giữ trong grid đã kiểm tra. [Phân tích repeated-session sau Version 1](../../sensitivy_data/unknown_repeated_session_dependence_v1/unknown_repeated_session_dependence_results.md) giữ hướng dưới các ghép cặp giả định đã lấy mẫu nhưng độ lớn và q support thay đổi; nó dùng baseline Simplex riêng và chỉ đặt giới hạn suy luận. **Takeaway:** hướng trong các kiểm tra đã thực hiện thường bền hơn độ lớn và mức hỗ trợ thống kê. **Ranh giới:** 60 s là practical compromise trong dataset này, không phải universal optimum; hypothetical pairing không chứng minh statistical independence hoặc suy luận cấp participant.

**Đoạn hỗ trợ cuối:** Version 1 Table IV cho pattern 0V ↑, 2V ↓ và 1V gần zero/không nhất quán. Dùng như bối cảnh symbolic exploratory, không làm trục kết quả thứ tư và không diễn giải thành phép đo trực tiếp sympathetic/parasympathetic.

## 5. Discussion: bốn tiểu mục

| Tiểu mục | Lập luận và bằng chứng thiết yếu | Takeaway; ranh giới |
| --- | --- | --- |
| 5.1 Tái tổ chức phối hợp | Ghép CC ↓/NRMSE ↑, DET ↓ nominal và LLE ↓ từ Table III. Simplex đo prediction qua finite horizons; Rosenstein LLE ước lượng độ dốc mean log-distance cục bộ trong fit interval. Hai estimand và thang thời gian khác nhau, nên forecastability ↓ và LLE ↓ **không mâu thuẫn**. | Các descriptor bổ sung nhau; không dựng một trục more/less chaos hoặc cơ chế chưa đo. |
| 5.2 Robustness và cửa sổ hữu hạn | Fig. 9 giữ hướng 30–180 s nhưng 30 s bất định hơn; Tables V–VI giới hạn claim theo nhãn/tham số. DET đổi đáng kể khi đổi delay. Repeated-session sensitivity sau Version 1 phân biệt giữ hướng với thay đổi effect size/q support. | Bằng chứng defense layer củng cố phạm vi của primary finding; không nói estimator bất biến tham số, 60 s tối ưu phổ quát hay session độc lập. |
| 5.3 Bối cảnh sinh lý và hàm ý | Đặt pattern PPG trong declining vigilance sau bữa ăn; symbolic chỉ gợi ý tính tương thích với thay đổi cardiac autonomic modulation. Các descriptor có thể định hướng validation về sau. | Bối cảnh sinh lý là giả thuyết diễn giải; không có phép đo trực tiếp nhánh autonomic, classifier hay external/real-time validation. |
| 5.4 Giới hạn | Cohort nhỏ, trẻ khỏe mạnh; video/KSS thay PSG; PPG ngoại vi; dữ liệu hữu hạn và phụ thuộc QC/reconstruction/fit; một PPS null; thiếu participant–session linkage. | Suy luận ở cấp session và trong các setting đã kiểm tra; không gán sleep stage, chaos, nhân quả hoặc hiệu ứng cấp participant. |

## 6. Khung Abstract và Conclusion

**Abstract — tối đa sáu nhịp:** (1) khoảng trống về động lực học PPG khi declining vigilance; (2) RQ1 và RQ2; (3) 20 sessions, cửa sổ nominal 60 s, PPS và ba descriptor; (4) kết quả RQ1 theo null đã kiểm tra; (5) bốn hướng headline RQ2, chỉ dùng số Table III cần thiết; (6) robustness có điều kiện và kết luận tái tổ chức phối hợp. Không nhồi q-values hoặc đưa symbolic lên ngang primary.

**Conclusion — bốn chức năng câu:** trả lời RQ1 trong phạm vi PPS null; trả lời RQ2 bằng ba thuộc tính bổ sung; nêu sự tái tổ chức phối hợp cùng giới hạn của cửa sổ hữu hạn và dependence; kết bằng nhu cầu validation multimodal với participant được định danh.

## 7. Main text và Supplementary

| Vị trí | Ưu tiên |
| --- | --- |
| **Main paper** | PPS/RQ1; bốn hiệu ứng primary 60 s và bảng đủ bảy metric; robustness compact theo Fig. 9 với caveat DET/repeated-session; phương pháp nominal đủ để hiểu đơn vị phân tích. |
| **Supplementary** | Full label/parameter sensitivity; verification Simplex/RQA/LLE; chi tiết repeated-session, Monte Carlo/conservative search; symbolic đầy đủ; minh họa và audit phương pháp. |

## 8. Kế hoạch hình và bảng tối thiểu

| Asset main | Chức năng |
| --- | --- |
| Figure 1 — pipeline gọn | Dữ liệu/nhãn → QC/embedding → PPS/RQ1 và paired RQ2; cho thấy session là đơn vị suy luận. |
| Figure 2 — PPS | Dùng kết quả Version 1 Fig. 7 để trả lời RQ1. |
| Figure 3 — hiệu ứng primary | Trực quan hóa bốn headline theo Version 1 Fig. 8/Table III. |
| Figure 4 — robustness | Tóm tắt Version 1 Fig. 9; nếu có panel DET-delay, lấy từ Table VI và ghi nguồn riêng. Không biến repeated-session thành hình chính mặc định. |

**Tables:** một bảng protocol/QC gọn *nếu cần*; một bảng nominal configuration gọn hoặc gộp với protocol; **một bảng primary bảy metric từ Version 1 Table III là thiết yếu**. Figure/table thiết kế lại phải giữ đúng số PDF; Fig. 9 không in bảng Δ chính xác cho từng duration nên không tự bổ sung từ report sau.

## 9. Ranh giới claim thiết yếu

| Chủ đề | Ranh giới bắt buộc |
| --- | --- |
| PPS | Vượt quá noisy pseudoperiodic null đã kiểm tra ≠ proof of deterministic chaos. |
| LLE | Divergence ước lượng thấp hơn trên dữ liệu hữu hạn ≠ “less chaos” hoặc Lyapunov exponent thực đã chứng minh. |
| DET | Diagonal recurrence organization ở embedding nominal ≠ physical determinism; DET nhạy với embedding delay. |
| Symbolic | Supportive/exploratory ≠ phép đo trực tiếp sympathetic hoặc parasympathetic. |
| Cửa sổ 60 s | Practical compromise trong dataset này ≠ universal optimal window. |
| Repeated sessions | Hypothetical dependence sensitivity ≠ proof of statistical independence hoặc participant-level inference. |
| Nhãn Drowsy | Video/KSS ≠ PSG-confirmed N1/NREM. |
| Thiết kế quan sát | Association giữa state và PPG dynamics ≠ causation. |
