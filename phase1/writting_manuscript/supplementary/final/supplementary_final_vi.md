# Tài liệu bổ sung

## S1. Dữ liệu, gán nhãn và tính toàn vẹn dữ liệu

Phân tích gồm 20 session ghi nhận từ 10 người tham gia, theo báo cáo trong bản thảo chính. Tổng thời lượng ghi nhận là 17.40 h: 11.33 h Awake và 6.07 h Drowsy. Nhãn được gán bằng Karolinska Sleepiness Scale (KSS), kết hợp quan sát video để đối chiếu. Không có thông tin liên kết người tham gia–session. Vì vậy, suy luận chính sử dụng các session ghi nhận và không xác lập hiệu ứng ở cấp người tham gia.

Dữ liệu gồm 1,620,038 mẫu. Session ghi nhận 01 có tần số lấy mẫu 50 Hz, các session còn lại khoảng 25 Hz. Tần số lấy mẫu được ước tính bằng nghịch đảo của trung vị khoảng thời gian dương giữa các dấu thời gian liên tiếp. Kiểm tra tính toàn vẹn cho thấy dấu thời gian tăng nghiêm ngặt, không có mẫu trùng hoặc nhãn không hợp lệ, và không có giá trị tín hiệu/thời gian bị thiếu, không phải số hoặc vô hạn. PPG thô, PPG đã xử lý và nhãn được căn chỉnh trên cùng trục hàng. Tất cả session đều đạt kiểm tra tính toàn vẹn và điều kiện tham gia phân tích (Bảng S1).

Có 69 khoảng gián đoạn thời gian vượt quá 1.5 lần khoảng lấy mẫu trung vị; 62 khoảng vượt quá hai lần khoảng này và không có khoảng nào vượt quá năm lần. Các khoảng gián đoạn được giữ nguyên, không nội suy. Nhãn có 86 lần chuyển trạng thái, không có lần nào đi qua khoảng gián đoạn. Tách dữ liệu tại các lần chuyển trạng thái và khoảng gián đoạn tạo ra 175 đoạn trạng thái liên tục (93 Awake, 82 Drowsy), với thời lượng trung vị 260.04 s; 60 đoạn ngắn hơn 60 s, 78 đoạn ngắn hơn 180 s và 94 đoạn ngắn hơn 300 s.

**Bảng S1. Tóm tắt dữ liệu và tính toàn vẹn.**

| Session | Số mẫu | fs ước tính (Hz) | Số mẫu Awake / Drowsy | Gián đoạn | Toàn vẹn | Đủ điều kiện phân tích |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 117,828 | 50.000 | 77,805 / 40,023 | 0 | Đạt | Có |
| 04 | 75,416 | 24.992 | 46,897 / 28,519 | 3 | Đạt | Có |
| 05 | 91,211 | 25.003 | 59,235 / 31,976 | 4 | Đạt | Có |
| 06 | 79,179 | 24.993 | 51,240 / 27,939 | 5 | Đạt | Có |
| 07 | 79,768 | 24.994 | 59,225 / 20,543 | 3 | Đạt | Có |
| 08 | 77,595 | 24.994 | 61,405 / 16,190 | 4 | Đạt | Có |
| 09 | 119,272 | 25.001 | 83,631 / 35,641 | 8 | Đạt | Có |
| 10 | 60,386 | 24.998 | 45,365 / 15,021 | 3 | Đạt | Có |
| 11 | 61,582 | 24.994 | 33,062 / 28,520 | 2 | Đạt | Có |
| 12 | 89,853 | 24.989 | 34,376 / 55,477 | 2 | Đạt | Có |
| 13 | 76,473 | 25.000 | 40,272 / 36,201 | 2 | Đạt | Có |
| 14 | 85,948 | 24.994 | 54,871 / 31,077 | 5 | Đạt | Có |
| 15 | 69,362 | 24.996 | 54,511 / 14,851 | 6 | Đạt | Có |
| 17 | 68,752 | 24.993 | 45,601 / 23,151 | 2 | Đạt | Có |
| 18 | 69,937 | 24.997 | 30,634 / 39,303 | 3 | Đạt | Có |
| 19 | 73,041 | 24.996 | 54,123 / 18,918 | 4 | Đạt | Có |
| 21 | 69,660 | 25.000 | 41,549 / 28,111 | 2 | Đạt | Có |
| 22 | 74,710 | 25.001 | 50,359 / 24,351 | 3 | Đạt | Có |
| 23 | 109,452 | 24.997 | 87,703 / 21,749 | 3 | Đạt | Có |
| 25 | 70,613 | 24.996 | 46,905 / 23,708 | 5 | Đạt | Có |
| Tổng | 1,620,038 | Hỗn hợp | 1,058,769 / 561,269 | 69 | 20/20 | 20/20 |

Thành phần trạng thái là số mẫu, không phải ước tính thời lượng. Khoảng gián đoạn dùng ngưỡng 1.5 lần khoảng dấu thời gian trung vị. Đủ điều kiện phân tích không hàm ý mọi mẫu đều vào window được giữ lại.

Thời lượng theo trạng thái trong tóm tắt tính toàn vẹn sử dụng khoảng thời gian gắn với mẫu, chặn khoảng gián đoạn ở khoảng lấy mẫu trung vị và gán một khoảng trung vị cho mẫu cuối. Tổng thời lượng ghi nhận trong văn bản theo bản thảo chính.

## S2. Tiền xử lý, kiểm soát chất lượng và số window được giữ lại

PPG thô được nhân với $-1$ rồi xử lý bằng bộ lọc thông dải Butterworth bậc hai (0.5–8 Hz), áp dụng xuôi và ngược để đạt pha bằng không. Tất cả bước QC và phân tích phi tuyến sau đó đều sử dụng PPG đã xử lý.

Sàng lọc nhiễu sử dụng các khối 5-s hoàn chỉnh, không chồng lấp, gồm $\mathrm{round}(5f_s)$ mẫu trong từng session ghi nhận. Biên độ và độ gồ ghề được định nghĩa là

\[
A=Q_{0.95}(x)-Q_{0.05}(x),\qquad R=\sqrt{\mathrm{mean}((\Delta x)^2)}.
\]

Trong đó, $Q_p$ là phân vị thứ $p$ và $\Delta x$ là sai phân bậc nhất. Mỗi đặc trưng $F\in\{A,R\}$ được chuẩn hóa trên các khối hoàn chỉnh của cùng session:

\[
z_F=0.6745\,\frac{F-\mathrm{median}(F)}{\max(\mathrm{MAD}(F),\epsilon)}.
\]

Với $\mathrm{MAD}(F)=\mathrm{median}(|F-\mathrm{median}(F)|)$ và epsilon máy $\epsilon$, khối được đánh dấu khi $z_A>4.5$ hoặc $z_R>4.5$. Toàn bộ mẫu của khối được đánh dấu; bất kỳ window phân tích nào chứa mẫu đã đánh dấu đều bị loại. Khối không hoàn chỉnh ở cuối không được sàng lọc.

Trong mỗi chuỗi cùng trạng thái, các window 60-s hoàn chỉnh, không chồng lấp sử dụng $\mathrm{round}(60f_s)$ mẫu. Phần dư không hoàn chỉnh bị bỏ và không tạo window vượt qua ranh giới trạng thái. Window ứng viên chứa khoảng thời gian giữa dấu thời gian lớn hơn $1.5/f_s$ bị loại, còn vị trí các window sau đó vẫn neo theo chuỗi trạng thái ban đầu. Quy trình tương tự được áp dụng ở 120 và 180 s.

Window đạt sàng lọc nhiễu và gián đoạn được đánh giá độ ổn định phương sai bằng các subwindow 10-s hoàn chỉnh, không chồng lấp, gồm $\mathrm{round}(10f_s)$ mẫu; cần ít nhất hai subwindow. Với $v_k=\mathrm{Var}(x_k)$ được tính bằng $\mathrm{ddof}=0$, chỉ số là

\[
S=\frac{\mathrm{IQR}(v)}{\max(\mathrm{median}(v),\epsilon)},\qquad \mathrm{IQR}(v)=Q_{0.75}(v)-Q_{0.25}(v).
\]

Điều kiện chấp nhận là $S\leq0.5$. Sàng lọc này hỗ trợ tính gần dừng cục bộ thông qua độ ổn định phương sai, thay vì xác lập tính dừng đầy đủ. Ở 60 s, sàng lọc phương sai giữ lại 596 window Awake và 305 window Drowsy từ 623 và 328 window đạt sàng lọc nhiễu/gián đoạn. Tổng dữ liệu cuối cùng gồm 901, 405 và 238 window tại 60, 120 và 180 s (Bảng S2).

Dữ liệu 30-s gồm hai nửa liên tiếp của mỗi window cha 60-s đã được chấp nhận. Các nửa này kế thừa QC của window cha và không được sàng lọc phương sai độc lập, tạo ra 1,192 window Awake và 610 window Drowsy (tổng 1,802). Điều kiện chấp nhận phép khớp LLE được áp dụng riêng (Mục S7); mức giữ lại danh định là 872/901 (96.78%). Toàn bộ số lượng theo từng thước đo nằm trong Bảng S2, còn minh họa tiền xử lý/giữ lại dữ liệu nằm trong Hình S1.

**Bảng S2. Các bước QC và số window được giữ lại theo từng thước đo.**

| Thời lượng (s) | Trạng thái | Sau SQI/gián đoạn | Đạt phương sai / non-LLE cuối | LLE hợp lệ | Tỷ lệ đạt phương sai | Tỷ lệ đạt LLE |
| --- | --- | --- | --- | --- | --- | --- |
| 30 | Awake | Không áp dụng | 1,192 | 1,089 | Không áp dụng | 1089/1192 (91.36%) |
| 30 | Drowsy | Không áp dụng | 610 | 549 | Không áp dụng | 549/610 (90.00%) |
| 60 | Awake | 623 | 596 | 579 | 596/623 (95.67%) | 579/596 (97.15%) |
| 60 | Drowsy | 328 | 305 | 293 | 305/328 (92.99%) | 293/305 (96.07%) |
| 120 | Awake | 284 | 269 | 264 | 269/284 (94.72%) | 264/269 (98.14%) |
| 120 | Drowsy | 148 | 136 | 135 | 136/148 (91.89%) | 135/136 (99.26%) |
| 180 | Awake | 168 | 161 | 160 | 161/168 (95.83%) | 160/161 (99.38%) |
| 180 | Drowsy | 86 | 77 | 77 | 77/86 (89.53%) | 77/77 (100.00%) |

Tỷ lệ đạt sàng lọc phương sai chia số non-LLE cuối cho số sau SQI/gián đoạn. Tỷ lệ đạt LLE chia số phép khớp được chấp nhận cho số non-LLE cuối. SQI là sàng lọc chất lượng tín hiệu theo biên độ/độ gồ ghề.

Ở 30 s, các bước sau SQI/gián đoạn và đạt phương sai độc lập không áp dụng vì QC được kế thừa từ window cha. Dữ liệu ở các thời lượng dùng chung bản ghi nguồn.

![Figure S1](figures/figure_S01.pdf)

**Hình S1.** Tiền xử lý và số window được giữ lại. (A) PPG thô sau đảo dấu và (B) PPG đã xử lý bằng bộ lọc Butterworth pha bằng không 0.5–8 Hz. (C) Số window đạt QC chung và có LLE hợp lệ theo trạng thái và thời lượng, như trong Bảng S2. Window 30-s là hai nửa liên tiếp của window cha 60-s đã được chấp nhận và kế thừa QC của window cha.

## S3. Cấu hình phân tích danh định đã cố định

Cấu hình tái dựng danh định chung và thiết lập riêng của từng thước đo được tóm tắt trong Bảng S3A. Hai trạng thái sử dụng cùng cấu hình nhúng. Window là đơn vị tính toán, còn session ghi nhận là đơn vị suy luận chính. Các họ hiệu chỉnh được liệt kê trong Bảng S3B và được giữ riêng giữa các phân tích và cấu hình.

**Bảng S3. Cấu hình danh định và các họ hiệu chỉnh đa kiểm định.**

**Panel A. Cấu hình bộ ước lượng danh định**

| Thành phần | Cấu hình |
| --- | --- |
| Đầu vào và tạo window | PPG đã xử lý; window 60-s không chồng lấp; 596 Awake + 305 Drowsy = 901. |
| Nhúng | $\tau=0.16$ s; $m=8$; $\tau_{\mathrm{samples}}=\mathrm{round}(\tau f_s)$ (4/8 mẫu ở 25/50 Hz). |
| Simplex Projection | $k=m+1=9$; khoảng cách Euclidean; trọng số mũ chuẩn hóa; dự báo leave-one-out; loại trừ theo thời gian $W=1.0$ s; 18 chân trời thời gian thực từ 0.04 đến 4.00 s, chuyển đổi bằng $\mathrm{round}(T_p f_s)$. Mean CC và Mean NRMSE là trung bình qua chân trời trong mỗi window. |
| RQA | Khoảng cách Euclidean; ngưỡng riêng theo window hướng đến $\mathrm{RR}=0.02$; loại trừ $W=(m-1)\tau_{\mathrm{samples}}$; $l_{\min}=v_{\min}=2$. Đầu ra: DET, $L_{\mathrm{mean}}$, LAM, TT. DET mô tả tổ chức đường chéo tái diễn. |
| Rosenstein LLE | Láng giềng Euclidean gần nhất hợp lệ; loại trừ theo chu kỳ trung bình phổ; theo dõi tối đa 5 s; khoảng khớp 0.80–1.30 s; ≥50 cặp ban đầu; ≥30 cặp mỗi điểm khớp; ≥3 điểm khớp; phép khớp hữu hạn; $R^2\geq0.90$. Đơn vị: s$^{-1}$. |
| PPS | $M=39$ surrogate mỗi window được kiểm định; giả thuyết không giả tuần hoàn có nhiễu đã kiểm định; kiểm định thứ hạng hai phía hữu hạn mẫu. |
| Tổng hợp và hiệu ứng | Trung vị session-trạng thái của thước đo window hợp lệ; ghép cặp $\Delta_i=\mathrm{Drowsy}_i-\mathrm{Awake}_i$; báo cáo trung vị sai khác ghép cặp. Tổng hợp Simplex theo trung bình chân trời trong window ở trên. |
| Thống kê chính | Kiểm định Wilcoxon signed-rank hai phía; rank-biserial correlation cho cặp ghép; 20,000 lần bootstrap session ghép cặp; CI phân vị 95% của trung vị sai khác ghép cặp; BH-FDR một lần trên bảy thước đo danh định 60-s. |

**Panel B. Các họ thống kê**

| Họ phân tích | Báo cáo hiệu chỉnh đa kiểm định |
| --- | --- |
| RQ2 chính | BH một lần trên 7 thước đo danh định 60-s |
| Độ nhạy nhãn | BH trên 4 thước đo trọng tâm trong mỗi quy tắc thay thế |
| Độ nhạy độ trễ/số chiều | BH trên 4 thước đo trọng tâm trong mỗi thiết lập |
| Độ nhạy RR/Theiler của RQA | Chỉ p thô |
| Độ nhạy LLE | Chỉ p thô |
| Độ ổn định theo độ dài window | Chỉ p thô |
| Độ nhạy session lặp lại | BH trên 7 thước đo mỗi ghép cặp giả định |
| Động lực học ký hiệu | BH trên 3 thước đo mỗi thời lượng |
| Kiểm định thứ hạng PPS cấp window | Không hiệu chỉnh |
| Họ sai lệch PPS cấp session | BH trên 12 kiểm định: 6 thước đo × 2 trạng thái |

Bảy thước đo chính là Mean CC, Mean NRMSE, DET, $L_{\mathrm{mean}}$, LAM, TT và LLE. Bốn thước đo trọng tâm là Mean CC, Mean NRMSE, DET và LLE. Hiệu chỉnh Benjamini–Hochberg kiểm soát tỷ lệ phát hiện sai trong từng họ xác định; không gộp họ qua các thiết lập.

Họ sai lệch PPS theo session gồm sáu thước đo không phải LLE trong mỗi trạng thái. Hàng tham chiếu danh định trong bảng độ nhạy giữ họ chính gồm bảy thước đo.

## S4. Tái dựng không gian pha: AMI và FNN

Average Mutual Information (AMI) được tính riêng cho từng window PPG đã xử lý dài 60-s bằng bộ ước lượng KSG 1 với $k=3$, khoảng cách Chebyshev trong không gian kết hợp và đơn vị log tự nhiên (nats). Độ trễ ứng viên trải từ một mẫu đến $\mathrm{round}(f_s\times1.0~\mathrm{s})$ mẫu. Quy tắc chọn dùng cực tiểu cục bộ nghiêm ngặt đầu tiên ở bên trong miền, không dùng điểm biên làm phương án thay thế; cả 901 window đều chọn được độ trễ (Bảng S4A).

Độ trễ được chọn có trung vị 0.160 s ở Awake (Q25–Q75: 0.120–0.260 s) và 0.120 s ở Drowsy (0.120–0.160 s). Trung vị của 20 trung vị theo session hỗ trợ độ trễ vận hành chung $\tau=0.16$ s; 14/20 trung vị theo session nằm trong $0.16\pm0.04$ s. Độ trễ này được dùng chung giữa hai trạng thái và không được tối ưu hóa để tạo khác biệt trạng thái.

False Nearest Neighbors (FNN) được đánh giá trên số chiều 1–10 bằng láng giềng gần nhất theo khoảng cách Euclidean và tiêu chí kiểu Kennel. Láng giềng được xem là giả nếu độ tách ở tọa độ bổ sung chia cho khoảng cách $m$ chiều $R_m$ vượt quá 15, hoặc khoảng cách đầy đủ $(m+1)$ chiều chia cho độ lệch chuẩn tín hiệu vượt quá 2. Loại các tự ghép và khoảng cách bằng hoặc gần bằng không; chẩn đoán này không áp dụng loại trừ theo thời gian.

Ở độ trễ danh định, trung vị FNN trên 20 đường cong theo session là 0.900%, 0.886% và 1.008% tại $m=7,8,9$ (Bảng S4B). Số chiều chung $m=8$ được chọn trong vùng FNN thấp này. Ở $m=8$, độ trễ 0.12, 0.16 và 0.20 s cho trung vị FNN 0.593%, 0.886% và 1.284%, với 19/20, 11/20 và 7/20 đường cong theo session dưới 1% (Bảng S4C). Không tham số nào được xem là tối ưu duy nhất; cấu hình danh định không đòi hỏi mọi session có FNN dưới 1%. Các chẩn đoán này mô tả hành vi tái dựng phục vụ phân tích (Hình S2); độ nhạy suy luận được trình bày tại Mục S12.1.

**Bảng S4. Bằng chứng AMI và FNN cho cấu hình tái dựng chung.**

**Panel A. Độ trễ được chọn bằng AMI**

| Trạng thái | Window | Trung vị τ (s) | Q25 (s) | Q75 (s) | Số chọn thành công |
| --- | --- | --- | --- | --- | --- |
| Awake | 596 | 0.160 | 0.120 | 0.260 | 596/596 |
| Drowsy | 305 | 0.120 | 0.120 | 0.160 | 305/305 |

**Panel B. FNN theo số chiều tại τ = 0.16 s**

| Số chiều | Trung vị FNN (%) | Q25 (%) | Q75 (%) |
| --- | --- | --- | --- |
| 7 | 0.900 | 0.679 | 1.155 |
| 8 | 0.886 | 0.613 | 1.132 |
| 9 | 1.008 | 0.666 | 1.298 |

**Panel C. Độ nhạy độ trễ tại m = 8**

| τ (s) | Trung vị FNN (%) | Đường cong session <1% |
| --- | --- | --- |
| 0.12 | 0.593 | 19/20 |
| 0.16 | 0.886 | 11/20 |
| 0.20 | 1.284 | 7/20 |

Panel A tóm tắt độ trễ được chọn trên các window trong mỗi trạng thái; số chọn thành công dùng mẫu số window hợp lệ. Panel B/C tóm tắt đường cong theo session được tạo từ trung vị FNN qua window ở mỗi số chiều. Trung vị/phân vị và số lượng dưới ngưỡng được tính trên 20 session ghi nhận. FNN được báo cáo dưới dạng phần trăm.

![Figure S2](figures/figure_S02.pdf)

**Hình S2.** Bằng chứng tái dựng từ PPG đã xử lý dài 60-s. (A) Độ trễ được chọn bằng AMI, với $\tau=0.16$ s dùng chung. (B) Đường cong FNN ở Awake và (C) ở Drowsy, với $m=8$ trong vùng FNN thấp. Hai trạng thái sử dụng cùng cấu hình tái dựng. Những chẩn đoán này hỗ trợ lựa chọn vận hành, thay vì một giá trị tối ưu phổ quát.

## S5. Simplex Projection

Khả năng dự báo trên chân trời hữu hạn được đánh giá trên 901 window được giữ lại. Mỗi dạng sóng được chuẩn hóa thành $u=(x-\bar{x})/\sigma_x$, dùng độ lệch chuẩn tổng thể của toàn window ($\mathrm{ddof}=0$). Tái dựng chung sử dụng $m=8$, $\tau=0.16$ s và $d=\mathrm{round}(\tau f_s)$ mẫu.

Vector tọa độ trễ tiến là $\mathbf{z}_i=[u_i,u_{i+d},\ldots,u_{i+(m-1)d}]$, với chỉ số tọa độ cuối $t_i=i+(m-1)d$. Tại chân trời $T_p$, độ dịch $h=\mathrm{round}(T_pf_s)$ xác định đích $u_{t_i+h}$. Điểm cuối của truy vấn và láng giềng được giới hạn riêng tại từng chân trời để vector và đích đều nằm trong cùng window. Không dùng thư viện dự báo xuyên window.

Dự báo leave-one-out sử dụng $k=m+1=9$ láng giềng Euclidean gần nhất hợp lệ. Tự ghép bị loại và yêu cầu $|t_j-t_i|>\mathrm{round}(f_sW)$ với $W=1.0$ s. Với khoảng cách láng giềng $D_j$ và khoảng cách nhỏ nhất $D_1$, trọng số và dự báo là

\[
w_j=\frac{\exp(-D_j/D_1)}{\sum_{r=1}^{9}\exp(-D_r/D_1)},\qquad \widehat{u}_{t_i+h}=\sum_{j=1}^{9}w_j u_{t_j+h}.
\]

Nếu khoảng cách đã chọn không lớn hơn epsilon máy, các láng giềng đó chia đều toàn bộ trọng số, còn các láng giềng được chọn khác có trọng số bằng không. Dự báo cần đủ cả chín láng giềng hợp lệ. Với các cặp đích quan sát/dự báo hợp lệ, CC và NRMSE là

\[
\mathrm{CC}=\frac{\sum_i(y_i-\bar{y})(\widehat{y}_i-\bar{\widehat{y}})}{\sqrt{\sum_i(y_i-\bar{y})^2\sum_i(\widehat{y}_i-\bar{\widehat{y}})^2}},\qquad \mathrm{NRMSE}=\frac{\sqrt{n^{-1}\sum_i(y_i-\widehat{y}_i)^2}}{\sigma_u}.
\]

Trong đó, $n$ là số cặp dự báo hợp lệ và $\sigma_u$ là độ lệch chuẩn tổng thể của toàn window đã chuẩn hóa, bằng một trong giới hạn độ chính xác số. Đại lượng này không được tính lại trên tập đích riêng của từng chân trời. CC cao hơn và NRMSE thấp hơn biểu thị khả năng dự báo cao hơn. Mean CC và Mean NRMSE được lấy trung bình trên 18 chân trời trong mỗi window, sau đó tổng hợp bằng trung vị các window hợp lệ trong từng session và trạng thái, theo bản thảo. 901 window tạo ra 16,218 kết quả ở cấp chân trời.

Bảng S5A liệt kê chân trời theo thời gian thực và độ dịch nguyên ở tần số lấy mẫu danh định. Hiệu chuẩn loại trừ theo thời gian thử $W\in\{0,0.2,0.4,0.6,0.8,1.0,1.5,2.0\}$ s. Tóm tắt giữa các thiết lập liền kề gộp 120 tổ hợp session–trạng thái–thời lượng (20 session, hai trạng thái, 60/120/180 s) và mô tả thay đổi hiệu chuẩn tuyệt đối, không phải hiệu ứng trạng thái. Thay đổi lớn nhất xuất hiện từ 0.6 đến 0.8 s; 1.0 s là thiết lập ổn định duy trì đầu tiên sau thay đổi này (Bảng S5B). Hành vi theo chân trời được minh họa trong Hình S3.

**Bảng S5. Các chân trời dự báo Simplex và hiệu chuẩn loại trừ theo thời gian.**

**Panel A. Chân trời thời gian thực và độ dịch mẫu**

| Chân trời (s) | Độ dịch 25-Hz (mẫu) | Độ dịch 50-Hz (mẫu) |
| --- | --- | --- |
| 0.04 | 1 | 2 |
| 0.08 | 2 | 4 |
| 0.12 | 3 | 6 |
| 0.16 | 4 | 8 |
| 0.20 | 5 | 10 |
| 0.28 | 7 | 14 |
| 0.40 | 10 | 20 |
| 0.60 | 15 | 30 |
| 0.80 | 20 | 40 |
| 1.00 | 25 | 50 |
| 1.20 | 30 | 60 |
| 1.60 | 40 | 80 |
| 2.00 | 50 | 100 |
| 2.40 | 60 | 120 |
| 2.80 | 70 | 140 |
| 3.20 | 80 | 160 |
| 3.60 | 90 | 180 |
| 4.00 | 100 | 200 |

**Panel B. Hiệu chuẩn thiết lập liền kề**

| W liền kề (s) | Trung vị tuyệt đối ΔCC | Trung vị tuyệt đối ΔNRMSE | Hỗ trợ tối thiểu | Ổn định / lựa chọn |
| --- | --- | --- | --- | --- |
| 0.0 → 0.2 | 0.003550 | 0.003370 | 1.00 | Ổn định; trước chuyển đổi |
| 0.2 → 0.4 | 2.204e-06 | 2.213e-06 | 1.00 | Ổn định; trước chuyển đổi |
| 0.4 → 0.6 | 0.002137 | 0.002059 | 1.00 | Ổn định; trước chuyển đổi |
| 0.6 → 0.8 | 0.020254 | 0.015614 | 1.00 | Chuyển đổi lớn nhất; chưa ổn định |
| 0.8 → 1.0 | 0.003605 | 0.003260 | 1.00 | Đã chọn: W=1.0 s; duy trì |
| 1.0 → 1.5 | 0.008894 | 0.007937 | 1.00 | Ổn định; duy trì |
| 1.5 → 2.0 | 0.007034 | 0.006442 | 1.00 | Ổn định; duy trì |

Độ dịch ở Panel A minh họa cho 25/50 Hz; độ dịch thực dùng $f_s$ ước tính theo session. Panel B cho trung vị thay đổi tuyệt đối giữa thiết lập liền kề trên 120 tổ hợp, với mức hỗ trợ là tỷ lệ dự báo hợp lệ nhỏ nhất.

Ổn định đòi hỏi cả hai tốc độ thay đổi, chuẩn hóa theo tốc độ lớn nhất tương ứng, đều $\leq0.25$ và mức hỗ trợ tối thiểu $\geq0.95$. Tốc độ thay đổi bằng thay đổi tuyệt đối chia cho khoảng cách theo $W$. Ổn định duy trì đòi hỏi mọi cặp tiếp theo đều đạt; thiết lập trên được chọn là 1.0 s. Các đại lượng hiệu chuẩn này không phải kiểm định hiệu ứng trạng thái.

![Figure S3](figures/figure_S03.pdf)

**Hình S3.** Hành vi theo chân trời của Simplex trên PPG đã xử lý dài 60-s. (A) CC và (B) NRMSE trên 18 chân trời theo thời gian thực từ 0.04 đến 4.00 s, dùng tái dựng chung và loại trừ theo thời gian 1.0-s. Các đường theo session và trung vị theo trạng thái thể hiện khả năng dự báo trên chân trời hữu hạn; hiệu ứng trạng thái ghép cặp nằm trong Bảng S7.

## S6. Recurrence Quantification Analysis

RQA sử dụng khoảng cách Euclidean trong không gian trạng thái tái dựng chung. Ngưỡng riêng theo window $\varepsilon$ hướng đến $\mathrm{RR}=0.02$, với tái diễn được xác định bởi khoảng cách $\leq\varepsilon$. Loại đường đồng nhất và các cặp có $|i-j|\leq W$, trong đó $W=(m-1)d$: 28 mẫu ở khoảng 25 Hz và 56 mẫu ở 50 Hz (khoảng 1.12 s). Hiệu chuẩn mật độ đếm mỗi khoảng cách hợp lệ trong tam giác trên một lần. Khi có đồng hạng tại biên, so sánh số lượng khả đạt dưới/tại biên với mục tiêu; chọn RR gần mục tiêu hơn, hoặc RR thấp hơn khi sai số bằng nhau. Các khoảng cách bằng nhau được cùng đưa vào hoặc cùng loại ra.

Gọi $C_{\mathrm{upper}}$ là số điểm tái diễn hợp lệ trong tam giác trên và $P_d(l)$ là số chuỗi chéo cực đại dài $l$. Với $l_{\min}=2$, tổ chức đường chéo tái diễn và độ dài chéo trung bình đủ điều kiện là

\[
\mathrm{DET}=\frac{\sum_{l\geq2}lP_d(l)}{C_{\mathrm{upper}}},\qquad L_{\mathrm{mean}}=\frac{\sum_{l\geq2}lP_d(l)}{\sum_{l\geq2}P_d(l)}.
\]

Các chuỗi thẳng đứng được đếm theo cột trong ma trận tái diễn đối xứng đầy đủ sau cùng mặt nạ loại trừ. Với số điểm tái diễn $C_{\mathrm{full}}$ và số chuỗi thẳng đứng cực đại $P_v(v)$, khi $v_{\min}=2$, laminarity và trapping time là

\[
\mathrm{LAM}=\frac{\sum_{v\geq2}vP_v(v)}{C_{\mathrm{full}}},\qquad \mathrm{TT}=\frac{\sum_{v\geq2}vP_v(v)}{\sum_{v\geq2}P_v(v)}.
\]

Mẫu số DET/LAM gồm mọi điểm tái diễn trong miền đếm tương ứng, kể cả chuỗi ngắn hơn hai. $L_{\mathrm{mean}}$ và TT lấy trung bình các chuỗi đủ điều kiện theo độ dài chỉ số mẫu, không phải giây. Triển khai trả về không nếu không có chuỗi đủ điều kiện, và tỷ lệ bằng không nếu số điểm tái diễn bằng không. DET mô tả tổ chức đường chéo tái diễn; LAM/TT mô tả tổ chức thẳng đứng, không được diễn giải trực tiếp thành tính tất định vật lý hoặc hoạt động thần kinh tự chủ. Hình S4 minh họa hình học tái diễn; hiệu ứng danh định nằm trong Bảng S7, còn độ nhạy bộ ước lượng nằm tại Mục S12.2.

![Figure S4](figures/figure_S04.pdf)

**Hình S4.** Ví dụ biểu đồ tái diễn Awake và Drowsy từ session ghi nhận 01, dùng window đã xử lý dài 60-s, cấu hình nhúng chung, $\mathrm{RR}=0.02$ và loại trừ $W=(m-1)d$. Chuỗi chéo đóng góp cho DET và $L_{\mathrm{mean}}$; chuỗi thẳng đứng đóng góp cho LAM và TT. Biểu đồ minh họa hình học tái diễn, không phải hiệu ứng trạng thái suy luận.

## S7. Rosenstein Largest Lyapunov Exponent

Bộ ước lượng Rosenstein đánh giá sự phân kỳ quỹ đạo cục bộ trong window hữu hạn bằng cấu hình nhúng chung. Loại trừ theo thời gian dựa trên chu kỳ trung bình phổ của dạng sóng đã xử lý sau khi trừ trung bình. Công suất là bình phương biên độ Fourier trong phổ một phía, loại DC và giữ các tần số dương đến Nyquist mà không áp dụng thêm mặt nạ tần số. Với công suất $P_k$ tại $f_k$,

\[
\bar{f}=\frac{\sum_{k:f_k>0}f_kP_k}{\sum_{k:f_k>0}P_k},\qquad T=\bar{f}^{-1},\qquad W=\max\{1,\mathrm{round}(f_sT)\}.
\]

Chọn láng giềng Euclidean gần nhất đầu tiên thỏa mãn $|j-i|>W$. Sau đó loại khoảng cách $\leq\delta=10\epsilon_{\mathrm{machine}}\max\{\mathrm{std}(\mathbf{Z}),1\}\sqrt{m}$ mà không thay láng giềng; $\mathrm{std}(\mathbf{Z})$ là độ lệch chuẩn tổng thể trên ma trận trạng thái. Các cặp hợp lệ được theo dõi tối đa 5 s. Cặp có điểm cuối sau tiến hóa vẫn nằm trong window và khoảng cách hữu hạn lớn hơn $\delta$ đóng góp cho đường log-khoảng cách trung bình,

\[
D(t)=\frac{1}{n_t}\sum_{j\in\mathcal{P}_t}\ln\|\mathbf{z}_{j+\ell}-\mathbf{z}_{\nu(j)+\ell}\|,\qquad t=\ell/f_s.
\]

Trong đó, $\nu(j)$ xác định láng giềng đã chọn, $\mathcal{P}_t$ là tập cặp hợp lệ ở độ trễ $\ell$ và $n_t$ là kích thước tập. Hồi quy tuyến tính theo thời gian tính bằng giây trên khoảng đóng 0.80–1.30 s cho hệ số dốc đơn vị s$^{-1}$ (Hình S5). Chấp nhận cần ít nhất 50 cặp ban đầu, 30 cặp mỗi điểm khớp, ba điểm khớp hữu hạn, hệ số dốc hữu hạn và $R^2\geq0.90$.

Điều kiện chấp nhận giữ lại 872/901 window đầu vào (96.78%): 579 Awake và 293 Drowsy. Trên toàn bộ window đầu vào, số cặp ban đầu nhỏ nhất là 1,471, số cặp nhỏ nhất tại một điểm khớp là 1,366 và trung vị $R^2$ của phép khớp là 0.973. Vì vậy, mức hỗ trợ cặp luôn vượt các ngưỡng vận hành tối thiểu. 29 window bị loại (17 Awake, 12 Drowsy) không đạt $R^2$, thay vì tiêu chí hỗ trợ cặp. Các chẩn đoán này gồm cả phép khớp bị loại; so sánh trạng thái chỉ dùng phép khớp được chấp nhận. LLE là ước lượng phân kỳ từ dữ liệu hữu hạn, không phải bằng chứng xác lập hỗn loạn tất định. Hiệu ứng danh định nằm trong Bảng S7; các thay đổi thiết lập nằm tại Mục S12.3.

![Figure S5](figures/figure_S05.pdf)

**Hình S5.** Ví dụ đường log-khoảng cách trung bình Rosenstein $D(t)$ và phép khớp tuyến tính từ window Awake đã xử lý dài 60-s trong session ghi nhận 01. Khoảng khớp là 0.80–1.30 s. Tiêu chí chấp nhận được định nghĩa tại Mục S7. Hệ số dốc là ước lượng LLE trên window hữu hạn, đơn vị s$^{-1}$.

## S8. Kiểm định Pseudoperiodic Surrogate

Pseudoperiodic surrogates (PPS) kiểm định giả thuyết không giả tuần hoàn có nhiễu. Dạng sóng đã xử lý được nhúng tiến bằng tái dựng chung; chỉ số ban đầu được lấy đều từ các trạng thái nhúng. Với trạng thái hiện tại $\mathbf{s}$, chỉ số ứng viên gồm mọi trạng thái có trạng thái kế tiếp quan sát được, với xác suất

\[
\Pr(j\mid\mathbf{s})=\frac{\exp[-(\|\mathbf{z}_j-\mathbf{s}\|-D_{\min})/\rho]}{\sum_{r=0}^{N_e-2}\exp[-(\|\mathbf{z}_r-\mathbf{s}\|-D_{\min})/\rho]},
\]

Trong đó, $N_e$ là số trạng thái nhúng và $D_{\min}$ là khoảng cách ứng viên nhỏ nhất; phép trừ này ổn định hàm mũ mà không thay xác suất chuẩn hóa. Sau khi chọn $j$, surrogate tiếp tục ở trạng thái kế tiếp quan sát được $j+1$. Cho phép ứng viên tự ghép và liền kề theo thời gian; trạng thái nhúng cuối bị loại vì không có trạng thái kế tiếp. Tọa độ đầu tiên của từng trạng thái được xuất đến khi đạt độ dài window gốc, không quay vòng qua biên.

Bán kính riêng theo window $\rho$ tối đa hóa số chuỗi chỉ số nguồn liên tiếp cực đại có độ dài ít nhất hai, lấy trung bình qua ba lần thử tại mỗi trong 21 bán kính ứng viên; khi đồng hạng dùng cực đại đầu tiên. Mỗi window được so với $M=39$ surrogate. Sáu thước đo không phải LLE dùng chung một tập; LLE dùng tập riêng, giữ loại trừ của window gốc nhưng không áp ngưỡng $R^2\geq0.90$ gốc lên phép khớp surrogate. So sánh LLE dùng 579 phép khớp gốc Awake và 293 Drowsy đã được chấp nhận.

Với giá trị gốc $a$ và giá trị surrogate $s_1,\ldots,s_M$, kiểm định hai phía hữu hạn mẫu tính cả đồng hạng trong hai đuôi:

\[
p=\min\left\{1,\frac{2\min\left(1+\#\{s_b\leq a\},\;1+\#\{s_b\geq a\}\right)}{M+1}\right\}.
\]

$p$ nhỏ nhất có thể đạt là $2/40=0.05$, với bác bỏ tại $p\leq0.05$ và không hiệu chỉnh ở cấp window. Có 24 đồng hạng chính xác giữa gốc và surrogate trong so sánh sáu thước đo, không trường hợp nào đổi kết quả bác bỏ tại ngưỡng này; các so sánh LLE được đưa vào không có đồng hạng.

Bảng S6A phân biệt phần trăm bác bỏ gộp với trung vị/IQR của 20 tỷ lệ riêng theo session. CC bác bỏ trong 374/596 window Awake (62.75% gộp; trung vị session 60.66%) và 229/305 window Drowsy (75.08%; 71.01%). Hướng kỳ vọng của gốc trừ PPS là dương với CC, DET, $L_{\mathrm{mean}}$ và LLE, âm với NRMSE, LAM và TT. Một lần bác bỏ LAM ở Drowsy có hướng ngược lại; tất cả trường hợp khác theo hướng kỳ vọng.

Đối với suy luận sai lệch theo session (Bảng S6B), mỗi window đóng góp giá trị gốc trừ trung vị của 39 surrogate. Trung vị sai lệch theo session-trạng thái được tổng hợp và kiểm định trên 20 session, với BH trên 12 kiểm định thước đo–trạng thái. Tỷ lệ bác bỏ là mô tả; họ này không chứa CI, p hoặc q cho sai lệch LLE.

Bác bỏ PPS cho thấy sự khác biệt với giả thuyết không giả tuần hoàn có nhiễu đã được kiểm định. Kết quả không xác lập hỗn loạn tất định và không loại trừ mọi mô hình ngẫu nhiên hoặc giả tuần hoàn có cấu trúc. Tỷ lệ bác bỏ trong từng trạng thái không phải kiểm định Awake–Drowsy ghép cặp. Dạng sóng minh họa và heatmap bác bỏ nằm trong Hình S6.

**Bảng S6. Bằng chứng bác bỏ PPS ở cấp window và sai lệch ở cấp session.**

**Panel A. Tóm tắt bác bỏ cấp window**

| Thước đo | Trạng thái | Window hợp lệ | n bác bỏ | Gộp (%) | Trung vị session (%) | IQR (pp) | n theo hướng kỳ vọng | n ngược hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mean CC | Awake | 596 | 374 | 62.75 | 60.66 | 16.98 | 374 | 0 |
| Mean CC | Drowsy | 305 | 229 | 75.08 | 71.01 | 23.31 | 229 | 0 |
| Mean NRMSE | Awake | 596 | 542 | 90.94 | 91.59 | 12.57 | 542 | 0 |
| Mean NRMSE | Drowsy | 305 | 291 | 95.41 | 100.00 | 7.27 | 291 | 0 |
| DET | Awake | 596 | 595 | 99.83 | 100.00 | 0.00 | 595 | 0 |
| DET | Drowsy | 305 | 305 | 100.00 | 100.00 | 0.00 | 305 | 0 |
| $L_{\mathrm{mean}}$ | Awake | 596 | 594 | 99.66 | 100.00 | 0.00 | 594 | 0 |
| $L_{\mathrm{mean}}$ | Drowsy | 305 | 305 | 100.00 | 100.00 | 0.00 | 305 | 0 |
| LAM | Awake | 596 | 537 | 90.10 | 95.50 | 16.36 | 537 | 0 |
| LAM | Drowsy | 305 | 273 | 89.51 | 92.38 | 18.59 | 272 | 1 |
| TT | Awake | 596 | 580 | 97.32 | 100.00 | 4.31 | 580 | 0 |
| TT | Drowsy | 305 | 295 | 96.72 | 100.00 | 7.28 | 295 | 0 |
| LLE | Awake | 579 | 545 | 94.13 | 96.30 | 7.28 | 545 | 0 |
| LLE | Drowsy | 293 | 287 | 97.95 | 100.00 | 0.76 | 287 | 0 |

**Panel B. Sai lệch gốc trừ PPS cấp session**

| Thước đo | Trạng thái | Session | Sai lệch trung vị | CI 95% | $p$ thô | $q_{\mathrm{BH}}$ | $r_{\mathrm{rb}}$ | Trung vị bác bỏ theo session (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mean CC | Awake | 20 | +0.1192 | [0.1034, 0.1278] | 1.90735e-6 | 1.90735e-6 | +1.000 | 60.66 |
| Mean CC | Drowsy | 20 | +0.1441 | [0.1245, 0.1906] | 1.90735e-6 | 1.90735e-6 | +1.000 | 71.01 |
| Mean NRMSE | Awake | 20 | -0.1321 | [-0.1658, -0.1273] | 1.90735e-6 | 1.90735e-6 | -1.000 | 91.59 |
| Mean NRMSE | Drowsy | 20 | -0.1557 | [-0.1901, -0.1370] | 1.90735e-6 | 1.90735e-6 | -1.000 | 100.00 |
| DET | Awake | 20 | +0.1833 | [0.1727, 0.1939] | 1.90735e-6 | 1.90735e-6 | +1.000 | 100.00 |
| DET | Drowsy | 20 | +0.1885 | [0.1713, 0.1971] | 1.90735e-6 | 1.90735e-6 | +1.000 | 100.00 |
| $L_{\mathrm{mean}}$ | Awake | 20 | +1.1528 | [1.0947, 1.1891] | 1.90735e-6 | 1.90735e-6 | +1.000 | 100.00 |
| $L_{\mathrm{mean}}$ | Drowsy | 20 | +1.1508 | [1.1023, 1.1815] | 1.90735e-6 | 1.90735e-6 | +1.000 | 100.00 |
| LAM | Awake | 20 | -0.1244 | [-0.1411, -0.1130] | 1.90735e-6 | 1.90735e-6 | -1.000 | 95.50 |
| LAM | Drowsy | 20 | -0.1266 | [-0.1282, -0.1091] | 1.90735e-6 | 1.90735e-6 | -1.000 | 92.38 |
| TT | Awake | 20 | -0.1139 | [-0.1367, -0.0855] | 1.90735e-6 | 1.90735e-6 | -1.000 | 100.00 |
| TT | Drowsy | 20 | -0.1188 | [-0.1283, -0.1077] | 1.90735e-6 | 1.90735e-6 | -1.000 | 100.00 |

Panel A: CC/NRMSE là trung bình chân trời theo window. Bác bỏ gộp bằng window bác bỏ/hợp lệ $\times100$; trung vị session và IQR tóm tắt 20 tỷ lệ theo session nhân với 100. Hướng kỳ vọng là gốc trừ PPS: dương với CC, DET, $L_{\mathrm{mean}}$, LLE và âm với NRMSE, LAM, TT. LLE dùng 579/293 window gốc được chấp nhận, các thước đo khác dùng 596/305.

Panel B: CI, p Wilcoxon signed-rank, $r_{\mathrm{rb}}$ và q hiệu chỉnh BH mô tả trung vị sai lệch gốc trừ PPS theo session-trạng thái trên 20 session. BH áp dụng một lần trên 12 kiểm định sáu thước đo–trạng thái. Tỷ lệ bác bỏ là mô tả; họ này không có suy luận sai lệch LLE. Đơn vị sai lệch/CI là mẫu với $L_{\mathrm{mean}}$/TT và không thứ nguyên với các thước đo khác.

![Figure S6](figures/figure_S06.pdf)

**Hình S6.** Minh họa PPS và mẫu hình bác bỏ. (A) Đoạn 15-s của PPG gốc đã xử lý và một surrogate minh họa từ session ghi nhận 01. (B) Tỷ lệ riêng theo session ở Awake và (C) ở Drowsy bác bỏ giả thuyết không giả tuần hoàn có nhiễu đã kiểm định. Kiểm định dùng 39 surrogate, thứ hạng hai phía có tính đồng hạng và $p\leq0.05$ không hiệu chỉnh. Tỷ lệ LLE dùng phép khớp gốc được chấp nhận. Dạng sóng chỉ minh họa; heatmap mô tả bác bỏ trong từng trạng thái, không phải hiệu ứng trạng thái ghép cặp.

## S9. Khung thống kê và hiệu chỉnh đa kiểm định

Mỗi thước đo được tổng hợp bằng trung vị các window hợp lệ trong từng session ghi nhận và trạng thái. Với Simplex, thước đo theo window được lấy trung bình trên các chân trời trước (Mục S5). Mỗi trong 20 session đóng góp một sai khác ghép cặp,

\[
\Delta_i=\mathrm{Drowsy}_i-\mathrm{Awake}_i,\qquad \Delta=\mathrm{median}_i(\Delta_i).
\]

Kiểm định Wilcoxon signed-rank hai phía loại sai khác bằng không trước khi xếp hạng và gán hạng trung bình cho giá trị tuyệt đối bằng nhau. Simplex xem sai khác tuyệt đối $\leq10^{-12}$ là không và dùng phân bố có điều kiện chính xác; RQA/LLE loại sai khác bằng không chính xác và dùng phương pháp tự động, không hiệu chỉnh liên tục. Không so sánh danh định nào trong bảy so sánh có sai khác bằng không.

Rank-biserial correlation cho cặp ghép là $r_{\mathrm{rb}}=(W_+-W_-)/(W_++W_-)$, với tổng hạng dương/âm sau khi loại sai khác bằng không. CI bootstrap phân vị 95% của hiệu ứng ghép cặp trung vị dùng 20,000 lần lấy mẫu lại có hoàn lại từ vector sai khác theo session và phân vị 2.5/97.5 của các trung vị lấy mẫu lại. Đơn vị suy luận và bootstrap vẫn là session ghi nhận (Mục S1). CI mô tả độ bất định của hiệu ứng trung vị; kiểm định signed-rank phụ thuộc phân bố hạng có dấu, nên kết luận của hai cách không nhất thiết trùng khớp.

BH-FDR chính được áp dụng một lần trên bảy thước đo danh định 60-s, với hỗ trợ thống kê tại $q_{\mathrm{BH}}<0.05$. Các họ khác được giữ riêng (Bảng S3B). Trong Bảng S7, Mean CC giảm và Mean NRMSE tăng, biểu thị khả năng dự báo trên chân trời hữu hạn thấp hơn ở Drowsy. DET giảm dưới tái dựng danh định và LLE giảm, mô tả tổ chức đường chéo tái diễn và sự phân kỳ quỹ đạo cục bộ ước lượng thấp hơn. Bốn thước đo này đạt tiêu chí BH7. $L_{\mathrm{mean}}$ âm với CI không chứa không nhưng không có hỗ trợ BH; LAM/TT cũng không có hỗ trợ. Đây là các thuộc tính bổ sung trên window hữu hạn, không phải một thang đo hỗn loạn chung. Tất cả phân tích độ nhạy tiếp theo dùng lại cùng bản ghi và mang tính hỗ trợ, không phải lặp lại độc lập.

**Bảng S7. Toàn bộ thống kê chính với window 60-s.**

| Thước đo | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $q_{\mathrm{BH}}$ | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mean CC | 20 | -0.0339 | [-0.0595, -0.0043] | 0.02148438 | 0.0376 | -0.581 | 15/20 thấp hơn |
| Mean NRMSE | 20 | +0.0294 | [0.0047, 0.0530] | 0.00729561 | 0.0255 | +0.667 | 15/20 cao hơn |
| DET | 20 | -0.0186 | [-0.0364, -0.0069] | 0.02148438 | 0.0376 | -0.581 | 15/20 thấp hơn |
| $L_{\mathrm{mean}}$ | 20 | -0.0630 | [-0.1247, -0.0139] | 0.05825806 | 0.0816 | -0.486 | 16/20 thấp hơn |
| LAM | 20 | +0.0165 | [-0.0044, 0.0635] | 0.14290619 | 0.1667 | +0.381 | 13/20 cao hơn |
| TT | 20 | +0.0095 | [-0.0034, 0.0160] | 0.20244980 | 0.2024 | +0.333 | 14/20 cao hơn |
| LLE | 20 | -0.0376 | [-0.0537, -0.0230] | 0.00070763 | 0.0050 | -0.810 | 16/20 thấp hơn |

Mọi so sánh dùng 20 session ghi nhận ghép cặp. QC chung giữ 596 window Awake và 305 Drowsy (tổng 901); LLE dùng 579 và 293 phép khớp được chấp nhận (tổng 872). Số đếm theo hướng tuân theo dấu trung vị báo cáo; không sai khác danh định nào bằng không.

$\Delta$ là trung vị sai khác ghép cặp, không phải sai khác giữa các trung vị trạng thái biên. Đơn vị hiệu ứng/CI là mẫu với $L_{\mathrm{mean}}$/TT, s$^{-1}$ với LLE và không thứ nguyên với thước đo khác. p thô có tám chữ số thập phân; giữ độ chính xác hiệu ứng, CI, $r_{\mathrm{rb}}$ và q của bản thảo. q thuộc họ BH7 chính.

## S10. Độ ổn định theo độ dài window

Độ nhạy theo độ dài window so sánh bốn thước đo trọng tâm tại 30, 60, 120 và 180 s (Bảng S8; Hình S7). Mỗi thời lượng có 20 session ghép cặp, với số window hợp lệ riêng theo thước đo. Số lượng theo hướng đếm giảm đối với Mean CC/DET/LLE và tăng đối với Mean NRMSE. Quy ước hiệu ứng ghép cặp và CI theo Mục S9; phân tích này chỉ báo cáo p thô.

Hướng của cả bốn hiệu ứng trung vị được giữ qua các thời lượng, nhưng độ lớn và độ bất định khác nhau. Ước lượng 30-s nhìn chung có độ bất định cao hơn; window dài hơn thường giảm độ bất định nhưng cũng giảm số window hợp lệ. Khoảng DET ở 180-s vẫn tương đối rộng. CI DET chứa không tại 30 và 180 s; p thô tại 180-s là 0.053169. Vì vậy, giữ hướng không đồng nghĩa với hỗ trợ thống kê đồng đều. Trong bộ dữ liệu này, 60 s cân bằng thực tế giữa thời gian quan sát và độ bất định, thay vì là tối ưu phổ quát.

**Bảng S8. Độ nhạy theo độ dài window của bốn thước đo trọng tâm.**

| Thước đo | Thời lượng (s) | Window Awake | Window Drowsy | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mean CC | 30 | 1192 | 610 | 20 | -0.0147 | [-0.0712, -0.0039] | 0.03276825 | -0.543 | 15/20 |
| Mean CC | 60 | 596 | 305 | 20 | -0.0339 | [-0.0595, -0.0043] | 0.02148438 | -0.581 | 15/20 |
| Mean CC | 120 | 269 | 136 | 20 | -0.0271 | [-0.0490, -0.0156] | 0.01361656 | -0.619 | 16/20 |
| Mean CC | 180 | 161 | 77 | 20 | -0.0428 | [-0.0516, -0.0133] | 0.00943565 | -0.648 | 15/20 |
| Mean NRMSE | 30 | 1192 | 610 | 20 | +0.0203 | [+0.0009, +0.0554] | 0.00943565 | +0.648 | 14/20 |
| Mean NRMSE | 60 | 596 | 305 | 20 | +0.0294 | [0.0047, 0.0530] | 0.00729561 | +0.667 | 15/20 |
| Mean NRMSE | 120 | 269 | 136 | 20 | +0.0321 | [+0.0196, +0.0495] | 0.00830841 | +0.657 | 15/20 |
| Mean NRMSE | 180 | 161 | 77 | 20 | +0.0321 | [+0.0186, +0.0465] | 0.00729561 | +0.667 | 15/20 |
| DET | 30 | 1192 | 610 | 20 | -0.0169 | [-0.0318, +0.0002] | 0.01531219 | -0.610 | 14/20 |
| DET | 60 | 596 | 305 | 20 | -0.0186 | [-0.0364, -0.0069] | 0.02148438 | -0.581 | 15/20 |
| DET | 120 | 269 | 136 | 20 | -0.0201 | [-0.0399, -0.0134] | 0.00638962 | -0.676 | 15/20 |
| DET | 180 | 161 | 77 | 20 | -0.0248 | [-0.0416, +0.0008] | 0.05316925 | -0.495 | 14/20 |
| LLE | 30 | 1089 | 549 | 20 | -0.0325 | [-0.0549, -0.0066] | 0.00315285 | -0.724 | 17/20 |
| LLE | 60 | 579 | 293 | 20 | -0.0376 | [-0.0537, -0.0230] | 0.00070763 | -0.810 | 16/20 |
| LLE | 120 | 264 | 135 | 20 | -0.0442 | [-0.0591, -0.0216] | 0.00232506 | -0.743 | 18/20 |
| LLE | 180 | 160 | 77 | 20 | -0.0498 | [-0.0584, -0.0213] | 0.00058556 | -0.819 | 16/20 |

Số lượng là window hợp lệ riêng theo thước đo; LLE gồm sàng lọc phép khớp (Mục S7). Hiệu ứng/CI dùng s$^{-1}$ với LLE và không thứ nguyên với thước đo khác. Số đếm theo hướng tuân theo dấu kỳ vọng danh định. Giá trị hiệu ứng/CI/$r_{\mathrm{rb}}$ danh định 60-s khớp Bảng S7; mọi p theo thời lượng đều không hiệu chỉnh.

![Figure S7](figures/figure_S07.pdf)

**Hình S7.** Độ nhạy theo độ dài window. Hiệu ứng ghép cặp trung vị và CI bootstrap phân vị 95% của Mean CC, Mean NRMSE, DET và LLE tại 30, 60, 120 và 180 s. Hướng trung vị được giữ, còn độ lớn và độ bất định thay đổi; khoảng DET chứa không tại 30 và 180 s. Mỗi thời lượng có 20 session ghép cặp, với ít window hợp lệ hơn khi thời lượng dài hơn và sàng lọc phép khớp bổ sung cho LLE (Bảng S8).

## S11. Độ nhạy đối với quy tắc gán nhãn

P0 dùng nhãn ghi nhận chính. T30/T60 loại các mẫu trong ±30/±60 s quanh chuyển trạng thái; S3/S5 giữ chuỗi cùng trạng thái dài ít nhất 180/300 s. Window được tạo và sàng lọc theo từng quy tắc; dữ liệu giữ lại không nhất thiết là các tập con lồng nhau của P0. Số lượng sau QC chung nằm trong Bảng S9A. P0/T30/T60/S3 giữ 20 session ghép cặp, S5 giữ 19; LLE áp dụng thêm điều kiện chấp nhận phép khớp.

Cả 16 hiệu ứng trung vị theo quy tắc thay thế giữ hướng của bốn thước đo trọng tâm và có $q_{\mathrm{BH}}<0.05$ trong họ BH4 của từng quy tắc (Bảng S9B; Hình S8). Độ lớn khác nhau. CI Mean CC theo T60 $[-0.0561,+0.0059]$ và CI LLE theo T30 $[-0.0535,+0.0020]$ chứa không, phù hợp với phân biệt CI/kiểm định tại Mục S9. P0 vẫn là tham chiếu chính cố định, với hiệu chỉnh BH7 thay vì BH4 của quy tắc thay thế.

**Bảng S9. Định nghĩa nhãn, dữ liệu được giữ lại và hiệu ứng của bốn thước đo.**

**Panel A. Quy tắc và số lượng sau QC chung**

| Quy tắc | Định nghĩa | Window Awake | Window Drowsy | Tổng window | n ghép cặp |
| --- | --- | --- | --- | --- | --- |
| P0 | Nhãn ghi nhận chính | 596 | 305 | 901 | 20 |
| T30 | Loại mẫu trong ±30 s quanh chuyển trạng thái | 586 | 274 | 860 | 20 |
| T60 | Loại mẫu trong ±60 s quanh chuyển trạng thái | 551 | 236 | 787 | 20 |
| S3 | Giữ chuỗi cùng trạng thái ≥180 s | 609 | 291 | 900 | 20 |
| S5 | Giữ chuỗi cùng trạng thái ≥300 s | 581 | 265 | 846 | 19 |

**Panel B. Suy luận bốn thước đo**

| Quy tắc | Họ | Thước đo | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $q_{\mathrm{BH}}$ | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | Chính BH7 | Mean CC | 20 | -0.0339 | [-0.0595, -0.0043] | 0.02148438 | 0.0376 | -0.581 | 15/20 |
| P0 | Chính BH7 | Mean NRMSE | 20 | +0.0294 | [0.0047, 0.0530] | 0.00729561 | 0.0255 | +0.667 | 15/20 |
| P0 | Chính BH7 | DET | 20 | -0.0186 | [-0.0364, -0.0069] | 0.02148438 | 0.0376 | -0.581 | 15/20 |
| P0 | Chính BH7 | LLE | 20 | -0.0376 | [-0.0537, -0.0230] | 0.00070763 | 0.0050 | -0.810 | 16/20 |
| T30 | Độ nhạy BH4 | Mean CC | 20 | -0.0482 | [-0.0689, -0.0152] | 0.0048599 | 0.0097 | -0.695 | 17/20 |
| T30 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0406 | [+0.0190, +0.0570] | 0.0031528 | 0.0097 | +0.724 | 16/20 |
| T30 | Độ nhạy BH4 | DET | 20 | -0.0183 | [-0.0332, -0.0011] | 0.0083084 | 0.0111 | -0.657 | 14/20 |
| T30 | Độ nhạy BH4 | LLE | 20 | -0.0322 | [-0.0535, +0.0020] | 0.021484 | 0.0215 | -0.581 | 14/20 |
| T60 | Độ nhạy BH4 | Mean CC | 20 | -0.0251 | [-0.0561, +0.0059] | 0.039989 | 0.0400 | -0.524 | 13/20 |
| T60 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0278 | [+0.0027, +0.0479] | 0.013617 | 0.0256 | +0.619 | 14/20 |
| T60 | Độ nhạy BH4 | DET | 20 | -0.0167 | [-0.0294, -0.0066] | 0.019234 | 0.0256 | -0.590 | 15/20 |
| T60 | Độ nhạy BH4 | LLE | 20 | -0.0393 | [-0.0636, -0.0075] | 0.0023251 | 0.0093 | -0.743 | 15/20 |
| S3 | Độ nhạy BH4 | Mean CC | 20 | -0.0361 | [-0.0548, -0.0033] | 0.010689 | 0.0136 | -0.638 | 14/20 |
| S3 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0357 | [+0.0032, +0.0457] | 0.0063896 | 0.0128 | +0.676 | 15/20 |
| S3 | Độ nhạy BH4 | DET | 20 | -0.0189 | [-0.0326, -0.0069] | 0.013617 | 0.0136 | -0.619 | 15/20 |
| S3 | Độ nhạy BH4 | LLE | 20 | -0.0344 | [-0.0495, -0.0104] | 0.0010166 | 0.0041 | -0.790 | 15/20 |
| S5 | Độ nhạy BH4 | Mean CC | 19 | -0.0337 | [-0.0495, -0.0077] | 0.01236 | 0.0141 | -0.642 | 14/19 |
| S5 | Độ nhạy BH4 | Mean NRMSE | 19 | +0.0367 | [+0.0056, +0.0504] | 0.0045776 | 0.0092 | +0.716 | 16/19 |
| S5 | Độ nhạy BH4 | DET | 19 | -0.0213 | [-0.0305, -0.0049] | 0.014069 | 0.0141 | -0.632 | 15/19 |
| S5 | Độ nhạy BH4 | LLE | 19 | -0.0321 | [-0.0499, -0.0147] | 0.0014114 | 0.0056 | -0.789 | 14/19 |

Số lượng ở Panel A là trước sàng lọc phép khớp LLE. Trong Panel B, cột Họ phân biệt hàng tham chiếu BH7 chính với hàng độ nhạy BH4; không gộp hiệu chỉnh qua quy tắc.

Số đếm theo hướng là giảm với Mean CC/DET/LLE và tăng với Mean NRMSE. Đơn vị hiệu ứng/CI là s$^{-1}$ với LLE và không thứ nguyên với thước đo khác. p thô giữ độ chính xác nguồn; q quy tắc thay thế có bốn chữ số thập phân.

![Figure S8](figures/figure_S08.pdf)

**Hình S8.** Độ nhạy đối với nhãn. (A) Số window Awake/Drowsy sau QC chung theo P0/T30/T60/S3/S5. (B–E) Hiệu ứng ghép cặp trung vị và CI phân vị 95% của bốn thước đo, dùng Bảng S7 cho P0 và tóm tắt quy tắc thay thế cho độ nhạy. n ghép cặp là 20, ngoại trừ S5 (19). Hướng trung vị được giữ; CI Mean CC theo T60 và LLE theo T30 chứa không. Hỗ trợ theo quy tắc thay thế dùng BH4 trong quy tắc; P0 giữ BH7 chính.

## S12. Độ nhạy của tái dựng và bộ ước lượng

Mỗi lần chỉ thay đổi một thiết lập tái dựng hoặc bộ ước lượng, giữ các lựa chọn khác ở danh định. Các phân tích này mô tả sự phụ thuộc trong phạm vi cấu hình đã thử.

### S12.1 Độ trễ nhúng và số chiều

Độ nhạy độ trễ sử dụng $\tau=0.12,0.16,0.20$ s tại $m=8$; độ nhạy số chiều dùng $m=7,8,9$ tại $\tau=0.16$ s (Bảng S10). Mean CC, Mean NRMSE và LLE giữ hiệu ứng trung vị âm, dương và âm qua các độ trễ. DET nhạy với độ trễ: giá trị danh định $-0.0186$ trở thành gần không và dương tại 0.12 s ($+0.0025$) và 0.20 s ($+0.0015$). Cả hai CI ngoài danh định đều chứa không và không có hỗ trợ BH.

Hướng trung vị của cả bốn thước đo được giữ trên $m=7$–9, nhưng độ lớn thay đổi, kể cả LLE. DET không có hỗ trợ BH4 tại $m=7$ ($q=0.053169$) và $m=9$ ($q=0.058258$), dù hiệu ứng âm và CI không chứa không. Một số CI Mean CC/NRMSE cũng chứa không. Bảng S10 phân biệt hàng danh định BH7 chính với hàng thiết lập thay thế BH4; không gộp hiệu chỉnh qua các thiết lập. Vì vậy, DET không ổn định đồng đều theo độ trễ nhúng.

**Bảng S10. Độ nhạy của tái dựng với các họ hiệu chỉnh được phân biệt rõ.**

**Panel A. Độ nhạy độ trễ tại m=8**

| Thiết lập | Họ | Thước đo | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $q_{\mathrm{BH}}$ | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.12 | Độ nhạy BH4 | Mean CC | 20 | -0.0317 | [-0.0522, +0.0094] | 0.036234 | 0.048312 | -0.533 | 13/20 |
| 0.12 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0321 | [-0.0042, +0.0492] | 0.029575 | 0.048312 | +0.552 | 13/20 |
| 0.12 | Độ nhạy BH4 | DET | 20 | +0.0025 | [-0.0078, +0.0076] | 0.784126 | 0.784126 | +0.076 | 7/20 |
| 0.12 | Độ nhạy BH4 | LLE | 20 | -0.0361 | [-0.0567, +0.0042] | 0.017181 | 0.048312 | -0.600 | 14/20 |
| 0.16 | Chính BH7 | Mean CC | 20 | -0.0339 | [-0.0595, -0.0043] | 0.02148438 | 0.0376 | -0.581 | 15/20 |
| 0.16 | Chính BH7 | Mean NRMSE | 20 | +0.0294 | [0.0047, 0.0530] | 0.00729561 | 0.0255 | +0.667 | 15/20 |
| 0.16 | Chính BH7 | DET | 20 | -0.0186 | [-0.0364, -0.0069] | 0.02148438 | 0.0376 | -0.581 | 15/20 |
| 0.16 | Chính BH7 | LLE | 20 | -0.0376 | [-0.0537, -0.0230] | 0.00070763 | 0.0050 | -0.810 | 16/20 |
| 0.20 | Độ nhạy BH4 | Mean CC | 20 | -0.0316 | [-0.0529, -0.0008] | 0.015312 | 0.020416 | -0.610 | 14/20 |
| 0.20 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0296 | [+0.0056, +0.0476] | 0.005581 | 0.011162 | +0.686 | 16/20 |
| 0.20 | Độ nhạy BH4 | DET | 20 | +0.0015 | [-0.0099, +0.0148] | 0.985435 | 0.985435 | +0.010 | 10/20 |
| 0.20 | Độ nhạy BH4 | LLE | 20 | -0.0464 | [-0.0572, -0.0240] | 0.000036 | 0.000145 | -0.933 | 17/20 |

**Panel B. Độ nhạy số chiều tại độ trễ 0.16 s**

| Thiết lập | Họ | Thước đo | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $q_{\mathrm{BH}}$ | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | Độ nhạy BH4 | Mean CC | 20 | -0.0307 | [-0.0565, +0.0045] | 0.026642 | 0.035522 | -0.562 | 13/20 |
| 7 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0377 | [-0.0023, +0.0561] | 0.023951 | 0.035522 | +0.571 | 13/20 |
| 7 | Độ nhạy BH4 | DET | 20 | -0.0145 | [-0.0303, -0.0047] | 0.053169 | 0.053169 | -0.495 | 15/20 |
| 7 | Độ nhạy BH4 | LLE | 20 | -0.0285 | [-0.0549, -0.0076] | 0.004860 | 0.019440 | -0.695 | 16/20 |
| 8 | Chính BH7 | Mean CC | 20 | -0.0339 | [-0.0595, -0.0043] | 0.02148438 | 0.0376 | -0.581 | 15/20 |
| 8 | Chính BH7 | Mean NRMSE | 20 | +0.0294 | [0.0047, 0.0530] | 0.00729561 | 0.0255 | +0.667 | 15/20 |
| 8 | Chính BH7 | DET | 20 | -0.0186 | [-0.0364, -0.0069] | 0.02148438 | 0.0376 | -0.581 | 15/20 |
| 8 | Chính BH7 | LLE | 20 | -0.0376 | [-0.0537, -0.0230] | 0.00070763 | 0.0050 | -0.810 | 16/20 |
| 9 | Độ nhạy BH4 | Mean CC | 20 | -0.0251 | [-0.0492, +0.0055] | 0.029575 | 0.039434 | -0.552 | 13/20 |
| 9 | Độ nhạy BH4 | Mean NRMSE | 20 | +0.0315 | [+0.0043, +0.0483] | 0.008308 | 0.016617 | +0.657 | 15/20 |
| 9 | Độ nhạy BH4 | DET | 20 | -0.0200 | [-0.0321, -0.0052] | 0.058258 | 0.058258 | -0.486 | 15/20 |
| 9 | Độ nhạy BH4 | LLE | 20 | -0.0247 | [-0.0534, -0.0102] | 0.000586 | 0.002342 | -0.819 | 16/20 |

Thiết lập Panel A là độ trễ tính bằng giây; Panel B là số chiều. Hàng BH7 chính tái hiện Bảng S7, còn hàng BH4 độ nhạy dùng họ bốn thước đo trong từng thiết lập thay thế.

Số đếm theo hướng dùng dấu kỳ vọng danh định (Mean CC/DET/LLE giảm; Mean NRMSE tăng), kể cả khi DET tổng thể đảo dấu. Hiệu ứng/CI giữ độ chính xác và đơn vị của bản thảo; p/q thay thế giữ sáu chữ số thập phân của nguồn. Đây là phân tích từng yếu tố, không phải lưới tổ hợp đầy đủ.

### S12.2 Thiết lập bộ ước lượng RQA

Độ nhạy RQA thử $\mathrm{RR}=0.01,0.02,0.03$ và hệ số Theiler 0.75, 1.00, 1.25 so với $W=(m-1)d$ danh định. Mọi thiết lập giữ 901 window và 20 session ghép cặp. Bảng S11A báo cáo suy luận DET/LAM/TT hiện có, chỉ với p thô. DET vẫn âm qua các thiết lập này, nhưng tại RR=0.01, CI chứa không và p là 0.082550. Việc giữ hướng dưới những lựa chọn RQA này khác với đảo dấu phụ thuộc độ trễ tại Mục S12.1.

LAM/TT vẫn là kết quả thứ cấp: mọi hiệu ứng trung vị đều dương, mọi CI chứa không và mọi p thô vượt 0.05. Không có kết quả độ nhạy bộ ước lượng cho $L_{\mathrm{mean}}$. Diễn giải thước đo theo Mục S6.

### S12.3 Thiết lập bộ ước lượng LLE

Độ nhạy LLE thử khoảng khớp 0.60–1.10, 0.80–1.30 (danh định) và 1.00–1.50 s; ngưỡng $R^2$ 0.90/0.95; hệ số Theiler 0.75/1.00/1.25 so với loại trừ dựa trên chu kỳ trung bình phổ (Mục S7). Mọi thiết lập giữ 20 session ghép cặp. Mỗi hiệu ứng trung vị đều âm, mọi CI không chứa không và p thô dưới 0.05 (Bảng S11B). Không áp dụng BH qua các thiết lập bộ ước lượng.

Các khoảng khớp giữ 802/872/889 trong 901 window đầu vào. Nâng ngưỡng $R^2$ từ 0.90 lên 0.95 giữ 734 thay vì 872 window và giảm mức giảm trung vị. Hệ số Theiler 0.75/1.00 cho cùng hiệu ứng và mức giữ lại; 1.25 giữ 874 window và đổi độ lớn. Vì vậy, việc giữ hướng đồng thời đi kèm thay đổi độ lớn và tập window; bộ ước lượng không độc lập với tham số.

**Bảng S11. Độ nhạy của bộ ước lượng RQA và LLE.**

**Panel A. Thiết lập RR và Theiler của RQA**

| Yếu tố | Thiết lập | Thước đo | Window hợp lệ | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RR | 0.01 | DET | 901 | 20 | -0.015214 | [-0.033764, +0.002064] | 0.082550 | -0.447619 | 14/20 |
| RR | 0.01 | LAM | 901 | 20 | 0.014242 | [-0.005819, +0.057725] | 0.132727 | 0.390476 | 13/20 |
| RR | 0.01 | TT | 901 | 20 | 0.000343 | [-0.000043, +0.004808] | 0.214602 | 0.352941 | 10/20; 4 bằng không |
| RR | 0.02 | DET | 901 | 20 | -0.0186 | [-0.0364, -0.0069] | 0.021484 | -0.581 | 15/20 |
| RR | 0.02 | LAM | 901 | 20 | +0.0165 | [-0.0044, 0.0635] | 0.142906 | +0.381 | 13/20 |
| RR | 0.02 | TT | 901 | 20 | +0.0095 | [-0.0034, 0.0160] | 0.202450 | +0.333 | 14/20 |
| RR | 0.03 | DET | 901 | 20 | -0.017813 | [-0.033859, -0.007863] | 0.021484 | -0.580952 | 15/20 |
| RR | 0.03 | LAM | 901 | 20 | 0.020281 | [-0.005463, +0.051395] | 0.082550 | 0.447619 | 13/20 |
| RR | 0.03 | TT | 901 | 20 | 0.022063 | [-0.007639, +0.033264] | 0.294252 | 0.276190 | 14/20 |
| Hệ số Theiler | 0.75 | DET | 901 | 20 | -0.019191 | [-0.036836, -0.006809] | 0.021484 | -0.580952 | 15/20 |
| Hệ số Theiler | 0.75 | LAM | 901 | 20 | 0.019785 | [-0.003072, +0.062855] | 0.123093 | 0.400000 | 13/20 |
| Hệ số Theiler | 0.75 | TT | 901 | 20 | 0.009809 | [-0.003114, +0.015962] | 0.189348 | 0.342857 | 14/20 |
| Hệ số Theiler | 1.00 | DET | 901 | 20 | -0.0186 | [-0.0364, -0.0069] | 0.021484 | -0.581 | 15/20 |
| Hệ số Theiler | 1.00 | LAM | 901 | 20 | +0.0165 | [-0.0044, 0.0635] | 0.142906 | +0.381 | 13/20 |
| Hệ số Theiler | 1.00 | TT | 901 | 20 | +0.0095 | [-0.0034, 0.0160] | 0.202450 | +0.333 | 14/20 |
| Hệ số Theiler | 1.25 | DET | 901 | 20 | -0.019033 | [-0.037873, -0.007730] | 0.017181 | -0.600000 | 15/20 |
| Hệ số Theiler | 1.25 | LAM | 901 | 20 | 0.019372 | [-0.005161, +0.062616] | 0.132727 | 0.390476 | 12/20 |
| Hệ số Theiler | 1.25 | TT | 901 | 20 | 0.009844 | [-0.002347, +0.017601] | 0.176853 | 0.352381 | 14/20 |

**Panel B. Thiết lập khớp, chất lượng và Theiler của LLE**

| Yếu tố | Thiết lập | Đạt / đầu vào | Window Awake | Window Drowsy | n ghép cặp | Trung vị $\Delta$ | CI 95% | $p$ thô | $r_{\mathrm{rb}}$ | Số giảm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Khoảng khớp (s) | 0.60–1.10 | 802/901 | 542 | 260 | 20 | -0.034980 | [-0.064607, -0.019121] | 0.000261 | -0.857143 | 18/20 |
| Khoảng khớp (s) | 0.80–1.30 | 872/901 | 579 | 293 | 20 | -0.0376 | [-0.0537, -0.0230] | 0.000708 | -0.810 | 16/20 |
| Khoảng khớp (s) | 1.00–1.50 | 889/901 | 588 | 301 | 20 | -0.030357 | [-0.045778, -0.003941] | 0.008308 | -0.657143 | 15/20 |
| Ngưỡng $R^2$ | 0.90 | 872/901 | 579 | 293 | 20 | -0.0376 | [-0.0537, -0.0230] | 0.000708 | -0.810 | 16/20 |
| Ngưỡng $R^2$ | 0.95 | 734/901 | 500 | 234 | 20 | -0.030618 | [-0.041701, -0.013987] | 0.002325 | -0.742857 | 16/20 |
| Hệ số Theiler | 0.75 | 872/901 | 579 | 293 | 20 | -0.037570 | [-0.053698, -0.022976] | 0.000708 | -0.809524 | 16/20 |
| Hệ số Theiler | 1.00 | 872/901 | 579 | 293 | 20 | -0.0376 | [-0.0537, -0.0230] | 0.000708 | -0.810 | 16/20 |
| Hệ số Theiler | 1.25 | 874/901 | 580 | 294 | 20 | -0.029763 | [-0.056095, -0.016331] | 0.002325 | -0.742857 | 16/20 |

Cả hai panel chỉ báo cáo p thô, không hiệu chỉnh BH qua thiết lập. n ghép cặp luôn là 20. Panel A đếm giảm với DET và tăng với LAM/TT; TT tại RR=0.01 có bốn sai khác bằng không bị loại trước tính hạng. DET/LAM không thứ nguyên, TT dùng độ dài chỉ số mẫu.

Số đạt ở Panel B dùng mẫu số 901 window đầu vào; hiệu ứng/CI có đơn vị s$^{-1}$. Hệ số Theiler dùng loại trừ danh định riêng của từng bộ ước lượng. Hiệu ứng/CI/$r_{\mathrm{rb}}$ danh định tái hiện Bảng S7 theo độ chính xác bản thảo; giá trị khi thay đổi thiết lập giữ sáu chữ số thập phân.

## S13. Sự phụ thuộc giữa các session lặp lại khi chưa biết liên kết

Để đánh giá hạn chế về liên kết trong Mục S1, phân tích sự phụ thuộc giả định nhóm 20 session thành 10 cụm gồm hai session bằng ghép cặp hoàn hảo ngẫu nhiên. Lấy mẫu có hoàn lại ghép các phần tử liền kề trong hoán vị ngẫu nhiên, tạo ra 100,000 ghép cặp được lấy mẫu và 99,990 ghép cặp duy nhất trong 654,729,075 ghép cặp có thể có về lý thuyết. Các cụm này không khôi phục danh tính người tham gia hoặc xác lập tính độc lập thực tế giữa session.

Với mỗi ghép cặp, sai khác cụm là trung bình số học của hai sai khác theo session; hiệu ứng là trung vị của 10 sai khác cụm. Kiểm định signed-rank hai phía có điều kiện loại sai khác trong $10^{-12}$ quanh không và lấy hạng trung bình khi giá trị tuyệt đối đồng hạng. BH bao phủ bảy thước đo trong mỗi ghép cặp, không có bootstrap lồng bên trong. Bảng S12A đưa ra phân vị của phân bố ghép cặp, không phải CI bootstrap.

Hướng trung vị của cả bốn thước đo trọng tâm được giữ trong mọi ghép cặp đã lấy mẫu. Tỷ lệ có $q_{\mathrm{BH}}<0.05$ là 19.36% (Mean CC), 27.82% (Mean NRMSE), 22.59% (DET) và 79.69% (LLE). Hướng ổn định hơn hỗ trợ thống kê sau khi giảm đơn vị hiệu dụng xuống 10 cụm giả định; LLE giữ hỗ trợ cao nhất trong phân tích này. Tần suất mô tả thiết kế ghép cặp giả định đã xác định, không phải xác suất kết quả thực có ý nghĩa thống kê. Chúng không cung cấp suy luận ở cấp người tham gia. Tóm tắt tích lũy 50,000/100,000 lượt tương tự nhau (Bảng S12B; Hình S9), hỗ trợ sự ổn định Monte Carlo nhưng không giải quyết liên kết.

**Bảng S12. Phân bố ghép cặp giả định và sự hội tụ.**

**Panel A. Phân bố ghép cặp giả định, 100,000 lượt**

| Thước đo | Hướng danh định | Giữ dấu (%) | $q_{\mathrm{BH}}<0.05$ (%) | $\Delta$ ghép cặp trung vị | Khoảng phân vị 2.5th–97.5th |
| --- | --- | --- | --- | --- | --- |
| Mean CC | Giảm | 100.00 | 19.36 | -0.0242 | [-0.0359, -0.0147] |
| Mean NRMSE | Tăng | 100.00 | 27.82 | +0.0263 | [+0.0185, +0.0343] |
| DET | Giảm | 100.00 | 22.59 | -0.0181 | [-0.0255, -0.0100] |
| $L_{\mathrm{mean}}$ | Giảm | 100.00 | 2.41 | -0.0657 | [-0.1000, -0.0333] |
| LAM | Tăng | 99.63 | 2.94 | +0.0227 | [+0.0063, +0.0402] |
| TT | Tăng | 99.25 | 0.04 | +0.0076 | [+0.0012, +0.0137] |
| LLE | Giảm | 100.00 | 79.69 | -0.0356 | [-0.0446, -0.0266] |

**Panel B. Tóm tắt Monte Carlo tích lũy**

| Số lượt | Thước đo | Giữ dấu (%) | $q_{\mathrm{BH}}<0.05$ (%) | $\Delta$ ghép cặp trung vị | Khoảng phân vị 2.5th–97.5th |
| --- | --- | --- | --- | --- | --- |
| 50000 | Mean CC | 100.00 | 19.44 | -0.0242 | [-0.0360, -0.0147] |
| 50000 | Mean NRMSE | 100.00 | 27.94 | +0.0263 | [+0.0185, +0.0342] |
| 50000 | DET | 100.00 | 22.69 | -0.0181 | [-0.0256, -0.0100] |
| 50000 | LLE | 100.00 | 79.69 | -0.0356 | [-0.0446, -0.0266] |
| 100000 | Mean CC | 100.00 | 19.36 | -0.0242 | [-0.0359, -0.0147] |
| 100000 | Mean NRMSE | 100.00 | 27.82 | +0.0263 | [+0.0185, +0.0343] |
| 100000 | DET | 100.00 | 22.59 | -0.0181 | [-0.0255, -0.0100] |
| 100000 | LLE | 100.00 | 79.69 | -0.0356 | [-0.0446, -0.0266] |

Giữ dấu so sánh hiệu ứng cụm trung vị của mỗi ghép cặp với hướng danh định. Hỗ trợ q dùng BH7 trong ghép cặp. Khoảng là phân vị 2.5th–97.5th của phân bố ghép cặp giả định, không phải CI bootstrap hoặc khoảng hiệu ứng người tham gia. Đơn vị theo Bảng S7.

Hàng 50k/100k là các tiền tố tích lũy của cùng chuỗi, không phải lượt chạy độc lập. Không suy ra liên kết người tham gia.

![Figure S9](figures/figure_S09.pdf)

**Hình S9.** Sự phụ thuộc giả định giữa các session lặp lại. (A) Tỷ lệ trong 100,000 ghép cặp có $q_{\mathrm{BH}}<0.05$ cho bốn thước đo trọng tâm, áp dụng BH7 trong mỗi ghép cặp. Hướng trung vị của cả bốn thước đo được giữ trong mọi ghép cặp lấy mẫu. (B) Tần suất hỗ trợ tích lũy tại 1k/10k/50k/100k lượt. Đây là tóm tắt của phân bố ghép cặp giả định, không phải xác suất ý nghĩa thống kê thực hoặc khôi phục người tham gia.

## S14. Động lực học ký hiệu

Phân tích ký hiệu thăm dò mã hóa khoảng giữa hai đỉnh PPG liên tiếp (PPI) tại 60/120/180 s. Đỉnh được phát hiện không làm trơn bổ sung, với khoảng cách tối thiểu $\lceil0.30f_s\rceil$ mẫu và prominence bằng 0.20 lần chênh lệch phân vị biên độ 95th–5th. PPI bằng sai khác chỉ số đỉnh liên tiếp chia cho $f_s$. Chấp nhận cần PPI hữu hạn, không có khoảng ngoài 0.30–2.00 s, độ bao phủ từ đỉnh đầu đến đỉnh cuối $\geq90\%$ và ít nhất $\max\{3,\lceil T/2\rceil-2\}$ khoảng cho thời lượng $T$ giây. Thay đổi tương đối trên 0.20 chỉ là chẩn đoán, không phải tiêu chí loại.

Trong mỗi window được chấp nhận, PPI được lượng tử hóa thành sáu mức có độ rộng bằng nhau giữa giá trị nhỏ nhất và lớn nhất. Giá trị tại biên trong thuộc bin phía trên; chuỗi hằng dùng mức không. Các từ chồng lấp gồm ba ký hiệu được gán 0V khi cả hai sai khác liền kề bằng không, 1V khi đúng một sai khác bằng không và 2V khi cả hai khác không. 2V gộp thay đổi cùng dấu 2LV và khác dấu 2UV. Phần trăm xuất hiện cộng thành 100% trong window, dù các trung vị session-trạng thái tổng hợp riêng không nhất thiết như vậy. So sánh ghép cặp sử dụng trung vị session-trạng thái của các window được chấp nhận.

Bảng S13 giữ cả chín kết quả phân loại–thời lượng, với BH3 trong từng thời lượng. Hiệu ứng trung vị 0V dương và 2V âm ở mọi thời lượng; 1V gần không và đổi dấu tổng thể ở 180 s. Không kết quả nào đạt họ BH tương ứng. CI tại 60-s của 0V và tại 180-s của 2V không chứa không; p thô của kết quả sau là 0.048441 nhưng q là 0.145323. Những đặc điểm CI/kiểm định thô này không thay thế kết quả hiệu chỉnh đa kiểm định mang tính thăm dò.

Hiệu ứng ghép cặp giữ cùng dấu qua cả ba thời lượng ở 17/20 session với 0V, 11/20 với 1V và 14/20 với 2V. Các số đếm gồm session luôn dương hoặc luôn âm, không phụ thuộc hướng tổng thể, và không hàm ý độ lớn bằng nhau. Tỷ lệ ký hiệu cung cấp bối cảnh theo hướng (Hình S10) ngoài khẳng định chính của bốn thước đo; không phải thước đo giao cảm/phế vị trực tiếp hoặc thước đo thần kinh tự chủ từ ECG đã được xác nhận.

**Bảng S13. Kết quả ký hiệu hỗ trợ mang tính thăm dò.**

| Phân loại | Thời lượng (s) | n ghép cặp | $\Delta$ (pp) | CI 95% (pp) | $p$ thô | $q_{\mathrm{BH}}$ | $r_{\mathrm{rb}}$ | Số theo hướng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0V | 60 | 20 | +4.04 | [+0.35, +7.18] | 0.053169 | 0.113777 | +0.495 | 14/20 |
| 1V | 60 | 20 | +0.41 | [-1.47, +2.23] | 0.498009 | 0.498009 | +0.181 | 10/20 |
| 2V | 60 | 20 | -0.91 | [-6.40, +0.37] | 0.075851 | 0.113777 | -0.457 | 13/20 |
| 0V | 120 | 20 | +2.32 | [-2.64, +5.63] | 0.474905 | 0.712358 | +0.190 | 13/20 |
| 1V | 120 | 20 | +0.03 | [-1.67, +2.13] | 0.927279 | 0.927279 | +0.029 | 10/20 |
| 2V | 120 | 20 | -2.30 | [-4.68, +1.78] | 0.329983 | 0.712358 | -0.257 | 12/20 |
| 0V | 180 | 20 | +4.58 | [-1.12, +13.94] | 0.164957 | 0.247436 | +0.362 | 13/20 |
| 1V | 180 | 20 | -0.06 | [-4.31, +1.95] | 0.956329 | 0.956329 | -0.019 | 10/20 |
| 2V | 180 | 20 | -2.67 | [-5.37, -0.44] | 0.048441 | 0.145323 | -0.505 | 15/20 |

Cả chín kiểm định đều thăm dò, với BH3 riêng trong thời lượng. pp là điểm phần trăm. Số đếm theo hướng là dương với 0V/1V và âm với 2V; 1V dùng quy ước báo cáo dương ngay cả khi trung vị 180-s hơi âm.

Số cùng dấu qua thời lượng là 17/20 (0V), 11/20 (1V), 14/20 (2V), gồm session luôn ngược hướng. Hiệu ứng/CI dùng hai chữ số thập phân, p/q thô sáu và hiệu ứng rank-biserial ba.

![Figure S10](figures/figure_S10.pdf)

**Hình S10.** Bằng chứng PPI ký hiệu thăm dò tại (A) 60, (B) 120 và (C) 180 s. Tỷ lệ xuất hiện 0V/2V theo session-trạng thái ghép cặp sử dụng lượng tử hóa PPI sáu mức và từ chồng lấp ba ký hiệu. Thay đổi trung vị 0V dương và 2V âm, nhưng không kiểm định nào trong chín kiểm định phân loại–thời lượng, kể cả 1V trong Bảng S13, đạt BH3 trong thời lượng. Các tỷ lệ cung cấp bối cảnh hỗ trợ, không phải hoạt động giao cảm/phế vị trực tiếp.

## S15. Tổng hợp độ ổn định của các kết quả

Bảng S14 phân biệt hiệu ứng danh định, việc giữ hướng, độ bất định và hỗ trợ thống kê. Mean CC giảm và Mean NRMSE tăng qua các thiết lập window, nhãn, độ trễ và số chiều đã thử, với độ lớn/CI thay đổi và hỗ trợ suy giảm dưới nhóm giả định.

DET giữ hướng giảm danh định qua window, nhãn, số chiều và thiết lập RR/Theiler của RQA đã thử, nhưng trở thành gần không và dương ở độ trễ ngoài danh định. Sự phụ thuộc độ trễ nhúng vì vậy là một điều kiện diễn giải rõ ràng. LLE giữ hướng giảm qua mọi nhánh đã thử và hỗ trợ cao nhất dưới nhóm giả định, còn lựa chọn khớp/QC làm thay đổi độ lớn và số window được chấp nhận.

Bằng chứng ký hiệu vẫn mang tính thăm dò. Các phân tích độ nhạy hỗ trợ trên cùng bản ghi, không phải lặp lại độc lập. Liên kết người tham gia–session chưa biết vẫn không được giải quyết bằng nhóm giả định. Ma trận không gán ý nghĩa thống kê gộp, điểm độ ổn định hoặc thứ hạng thước đo.

**Bảng S14. Ma trận bằng chứng về độ ổn định tổng thể.**

| Thước đo | Danh định 60-s | Độ dài window | Quy tắc nhãn | $\tau/m$ | Thiết lập bộ ước lượng riêng | Nhóm giả định | Giới hạn diễn giải |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mean CC | Giảm; có hỗ trợ BH | Giữ hướng; độ bất định thay đổi | Giữ hướng; CI T60 chứa không | Giữ hướng; một số CI chứa không | Không thử riêng tại đây | Giữ hướng; hỗ trợ suy giảm | Độ lớn/hỗ trợ phụ thuộc thiết lập; khả năng dự báo cấp session |
| Mean NRMSE | Tăng; có hỗ trợ BH | Giữ hướng; độ lớn thay đổi | Giữ hướng; độ lớn khác nhau | Giữ hướng; một số CI chứa không | Không thử riêng tại đây | Giữ hướng; hỗ trợ suy giảm | Độ lớn/hỗ trợ phụ thuộc thiết lập; khả năng dự báo cấp session |
| DET | Giảm; có hỗ trợ BH | Giữ hướng; CI 30/180-s chứa không | Giữ hướng; độ lớn khác nhau | Nhạy độ trễ; giữ hướng theo số chiều | Giữ hướng RR/Theiler; hỗ trợ yếu hơn tại RR=0.01 | Giữ hướng; hỗ trợ suy giảm | Tổ chức đường tái diễn phụ thuộc độ trễ; không phải tất định vật lý |
| LLE | Giảm; có hỗ trợ BH | Giữ hướng; độ bất định thay đổi | Giữ hướng; CI T30 chứa không | Giữ hướng; độ lớn thay đổi | Giữ hướng; số lượng đạt khớp/QC và độ lớn thay đổi | Giữ hướng; hỗ trợ cao nhất trong phân tích này | Phân kỳ quỹ đạo trong window hữu hạn; QC đổi tập dữ liệu; không suy luận người tham gia |
| Động lực học ký hiệu | Thăm dò; không có hỗ trợ BH | Bối cảnh hướng 0V/2V tại 60/120/180 s | Chưa thử | Chưa thử | Chưa thử | Chưa thử | Ngoài khẳng định chính; không diễn giải thần kinh tự chủ trực tiếp |

Các mô tả phân biệt hướng trung vị, độ bất định CI và hỗ trợ theo họ hiệu chỉnh trong phạm vi cấu hình đã thử. Ô chưa thử không hàm ý ổn định. Kết quả ký hiệu nằm ngoài khẳng định chính của bốn thước đo; liên kết người tham gia chưa biết vẫn là hạn chế.

