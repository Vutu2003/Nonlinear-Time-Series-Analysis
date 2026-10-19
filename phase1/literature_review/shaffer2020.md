# Evidence Audit: Shaffer, Meehan & Zerr (2020)

> Báo cáo phục vụ literature review cho manuscript *Ultra-Short PPG Dynamics Across the Wakefulness-to-Drowsiness Transition: A Nonlinear Time-Series Analysis*, theo cấu trúc và cách truy vết của `summary.md`. Phân tích dựa trực tiếp trên [PDF được cung cấp](paper/fnins-14-594880.pdf). Đây là bản tóm tắt một **critical review về HRV**, không phải một nghiên cứu thực nghiệm mới về dynamics của waveform PPG. Những nghiên cứu được review trích dẫn chỉ được thuật lại theo PDF này, chưa được audit từ bài gốc. Không viết đoạn Introduction hoàn chỉnh.

**Quy ước truy vết.** Mọi số trang là **trang PDF, đếm từ 1**, trùng với trang bài in trong PDF này. Mã **[S2020-E01]** trỏ tới bảng `Source evidence` tại §2. Confidence đánh giá độ chắc chắn khi trích xuất hoặc nhận diện phát biểu trong nguồn, không chứng nhận tính đúng đắn tuyệt đối của kết luận. Các đoạn **Nhận xét phân tích** là đánh giá của báo cáo này; relevance và research gap dựa trên bối cảnh manuscript trong `summary.md`.

- **High:** văn bản, công thức, bảng hoặc caption nêu rõ.
- **Medium:** cần tổng hợp nhiều vị trí, nguồn có bất nhất, hoặc kết luận về thông tin thiếu.
- **Not established from the provided source:** không xác lập được trong PDF; không bổ sung bằng suy đoán.
- **Direct support** trong bảng evidence nghĩa là PDF trực tiếp hỗ trợ phát biểu đó. Với các nghiên cứu 2014/2015/2019, đây vẫn là **secondary reporting**, không thay thế việc đọc primary source.

| Paper ID | PDF gốc | Số trang | Loại bài |
|---|---|---:|---|
| S2020 | [fnins-14-594880.pdf](paper/fnins-14-594880.pdf) | 11 | Critical review; không có cohort thực nghiệm mới |

## 1. Executive Scientific Summary

Shaffer et al. (2020) xem xét cách xác lập **criterion validity** của ultra-short-term HRV (**UST, <5 min**) so với short-term HRV (**ST, khoảng 5 min**). Đóng góp chính là phê bình tiêu chí kiểm chứng và chỉ ra nhu cầu đánh giá agreement, measurement bias, artifacts và predictive validity. Bài không đề xuất một thuật toán NTSA mới và không chứng minh tính chaotic của PPG. [S2020-E01–E05, E15–E16]

1. **Phạm vi review:** tác giả báo cáo đánh giá **28 nghiên cứu**, mỗi nghiên cứu có tối thiểu **20 người tham gia**. Theo phân loại trong Abstract và nội dung chính: **17** không khảo sát criterion validity, **8** chủ yếu dùng correlation/group differences, **3** dùng LOA làm tiêu chí. Có **4** nghiên cứu trình bày LOA plots, nhưng việc có biểu đồ LOA không đồng nghĩa dùng LOA để ra quyết định. Table 2 có các mục chồng lấn giữa nhóm; không dùng số dòng trong bảng để tạo một phân loại độc lập khác với số tác giả báo cáo. [S2020-E01, E05, E09, E16]
2. **Association khác agreement:** Pearson r, r² hoặc một group difference không có ý nghĩa thống kê không tự xác lập phép đo ngắn và dài có thể thay thế nhau. Ví dụ giả định của bài cho thấy hai phép đo nhịp tim có **r = 1** vẫn lệch nhau **10 bpm**. Đây là minh họa thống kê, không phải kết quả thực nghiệm về sai số HRV. [S2020-E06–E07]
3. **LOA cần ngưỡng chấp nhận đặt trước:** Bland–Altman mô tả bias và phân bố chênh lệch, nhưng bản thân biểu đồ không quyết định agreement có đủ tốt hay không. Tác giả yêu cầu đặt trước sai khác lớn nhất chấp nhận được, báo cáo confidence intervals và cân nhắc phân bố của paired differences. [S2020-E08]
4. **Thời lượng phụ thuộc feature và tiêu chí:** Table 4, chuyển từ **Shaffer et al. (2019)**, báo cáo RMSSD/SDNN **60 s**, DFA α1 **120 s**, DFA α2/DET/SampEn **180 s**, Shannon entropy **240 s**. Các mốc này thuộc HRV dựa trên interbeat intervals trong điều kiện nghiên cứu được mô tả; không phải ngưỡng phổ quát cho mọi người, mọi trạng thái hoặc waveform PPG. [S2020-E12–E13]
5. **Agreement với 5 phút không đồng nghĩa dự báo sức khỏe:** tác giả gọi UST là “proxies of proxies” vì UST tìm cách ước lượng ST, trong khi ST được dùng như proxy cho các metrics dài hạn. Bài kêu gọi kiểm chứng UST có dự báo được health/performance outcomes hay không và kiểm soát artifacts; một heartbeat giả có thể làm biến đổi mạnh HRV. [S2020-E01–E03, E15]

**Hàm ý cho manuscript hiện tại — nhận xét phân tích:** đây là nguồn trực tiếp cho rationale rằng lựa chọn cửa sổ ngắn cần bằng chứng theo từng feature và mục tiêu sử dụng. Bài không trực tiếp validate Simplex, PPS, Rosenstein LLE hoặc DET/Lmean/LAM/TT trên waveform PPG 60 s, và không nghiên cứu so sánh Awake–Drowsy. Cần phân biệt việc mô tả dynamics trong cửa sổ 60 s với claim rằng các estimates đó thay thế estimates của bản ghi dài hơn. [S2020-E03–E04, E13, E16]

## 2. Shaffer, Meehan & Zerr (2020)

**Thông tin thư mục.** Fred Shaffer, Zachary M. Meehan và Christopher L. Zerr. *A Critical Review of Ultra-Short-Term Heart Rate Variability Norms Research*. **Frontiers in Neuroscience**, 14:594880, xuất bản **19 November 2020**. DOI: [10.3389/fnins.2020.594880](https://doi.org/10.3389/fnins.2020.594880). Bài thuộc chuyên mục Autonomic Neuroscience và được đánh dấu **REVIEW**. [S2020-E01]

### Research question and motivation

Câu hỏi trung tâm là: **những tiêu chí đang được dùng có đủ để xác lập rằng UST HRV ước lượng được ST HRV với sai số chấp nhận được không?** Tác giả đồng thời xem xét concurrent validity, predictive validity, measurement bias và artifacts. Động cơ ứng dụng gồm giảm thời gian đo, các experimental tasks ngắn và khả năng tích hợp vào thiết bị theo dõi cá nhân. [S2020-E01–E03, E05]

Phần sinh lý trình bày HRV là sự biến thiên của thời gian giữa các heartbeat, liên hệ với regulatory capacity, health và performance; neurovisceral integration và vagal tank theory là **background được tổng hợp từ literature**, không phải cơ chế được kiểm định mới trong review này. [S2020-E02]

Bài phân biệt ba độ dài recording: long-term **≥24 h**, ST **~5 min**, UST **<5 min**. Tác giả nhấn mạnh cùng một công thức metric không làm ba chế độ đo trở nên interchangeable: chúng phản ánh các quá trình theo thang thời gian khác nhau và có predictive power khác nhau. Các claim dự báo morbidity/mortality được phần background gắn với literature về HRV, đặc biệt long-term recordings; không chuyển thành bằng chứng UST PPG đã có predictive validity. [S2020-E02–E03]

### Experimental data / reviewed evidence base

| Hạng mục | Thông tin xác lập từ PDF | Truy vết |
|---|---|---|
| Thiết kế | Critical review về UST HRV và method agreement; không báo cáo cohort thực nghiệm mới của bài 2020 | [S2020-E01, E05, E16] |
| Corpus | Tác giả báo cáo 28 nghiên cứu UST HRV, minimum 20 participants/study | [S2020-E01, E05] |
| Tuyển chọn/search protocol | Database tìm kiếm, search strings, khoảng ngày tìm kiếm, screening flow và protocol đăng ký trước: **Not established from the provided source** | [S2020-E16] |
| Meta-analysis | Không báo cáo pooled effect sizes, pooled LOA hoặc phân tích heterogeneity định lượng | [S2020-E16] |
| Biến quan sát | Chủ yếu HRV metrics tính từ interbeat/NN/RR intervals; cần phân biệt với waveform PPG lấy mẫu liên tục | [S2020-E02–E04] |
| Reference trong các so sánh UST–ST | Thường là 300-s HRV cùng feature; không phải outcome sức khỏe dài hạn | [S2020-E09–E14] |
| Modality trong bốn nghiên cứu LOA được mô tả | PPG, ECG và finger beat-to-beat pressure; không phải bốn dataset cùng sensor/protocol | [S2020-E09–E12] |
| Trạng thái | Baseline/resting; riêng Esco & Flatt có pre/post-exercise. Không có một thí nghiệm Awake–Drowsy của review | [S2020-E09–E12, E16] |
| Sampling rate/acquisition settings | Không có một sampling rate chung cho review; thông số chi tiết để tái lập các study không được xác lập đầy đủ | [S2020-E09–E12, E16] |
| Artifact control | Shaffer et al. (2019) được mô tả loại artifacts thủ công; Abstract/Conclusion yêu cầu automatic artifact correction cho ứng dụng rộng | [S2020-E01, E12, E15] |
| Cỡ mẫu tổng hợp | Không báo cáo một pooled N có thể dùng như cohort độc lập; không cộng N của studies để diễn giải như một thí nghiệm mới | [S2020-E16]; nhận xét phân tích |

### Methods and technical configuration

Các hàng dưới đây phân biệt **phương pháp review phê bình/khuyến nghị** với những thuật toán nằm trong studies được review thuật lại. Bài 2020 không tự chạy các phương pháp này trên một dataset mới. [S2020-E05–E14, E16]

| Phương pháp/khái niệm | Vai trò trong bài | Cấu hình hoặc lập luận báo cáo | Ranh giới sử dụng |
|---|---|---|---|
| **Concurrent criterion validity** | So sánh UST với validated ST measure được thu đồng thời | Criterion phải relevant, reliable và valid | Agreement với ST không tự xác lập predictive validity cho outcome. [S2020-E04] |
| **Predictive validity** | Kiểm tra khả năng dự báo outcomes/performance tương lai | Được nêu là nhu cầu nghiên cứu; review không có validation cohort mới | Không gọi UST đã clinically validated chỉ vì liên hệ với ST. [S2020-E03–E04, E15] |
| **Pearson r** | Phê bình việc dùng association như agreement; có thể sàng lọc potential surrogates | Ví dụ r = 1 nhưng bias +10 bpm; Shaffer 2019 dùng r ≥ 0.90 để sàng lọc | r cao không bảo đảm absolute agreement. [S2020-E06, E12] |
| **r² / ordinary simple regression** | Phê bình việc dùng shared variance/model fit để kết luận equivalence | Hai phép đo đều có measurement error; bài bàn về hạn chế của ordinary regression trong so sánh phương pháp | Không phải một benchmark regression mới. [S2020-E07] |
| **Deming / Passing–Bablok regression** | Các lựa chọn được trình bày khi cần regression với error ở cả hai biến | Deming: independent, normally distributed errors, nhạy outliers; Passing–Bablok: rank-based, ít nhạy outliers, cần quan hệ tuyến tính | Chỉ là methodological discussion; không có kết quả áp dụng mới trong review. [S2020-E07] |
| **Group mean/median comparison** | Phê bình inference từ non-significant difference | Group average có thể che individual errors; p-value phụ thuộc power và N | Không bác bỏ H0 không tự chứng minh equivalence. [S2020-E07] |
| **Bland–Altman / LOA** | Công cụ agreement tác giả khuyến nghị làm cơ sở quyết định | Paired difference theo paired mean; bias d̄; LOA d̄ ± 1.96 × s nếu differences normal; CI cho bias và hai LOA | Cần acceptable difference đặt trước; LOA không tự tạo ngưỡng chấp nhận. [S2020-E08] |
| **Log transformation / ratios / percentages** | Xử lý non-normality hoặc differences tăng theo magnitude | Bàn về log raw data hoặc ratio/percentage representations trước khi dựng plot | Kiểm tra phân bố **differences** là điều kiện của LOA dạng normal; không chỉ kiểm tra raw values. [S2020-E08, E14] |
| **Equality test sau LOA** | Khuyến nghị của tác giả | H0: mean difference = 0; ví dụ Student’s t-test; thử lần lượt các duration | Đây là lời khuyên của nguồn; không đồng nhất non-significant equality test với proof of equivalence. [S2020-E08, E14]; nhận xét phân tích |
| **DFA, recurrence và entropy metrics** | Table 1 định nghĩa các HRV metrics; Table 4 thuật lại minimum periods từ study 2019 | DFA α1/α2, DET, REC, ApEn, SampEn, D2, SD1/SD2 và ShanEn xuất hiện trong danh mục Table 1 | Không có code, DFA fitting scales, embedding, ε, Theiler window hoặc entropy parameters đủ để tái lập từng metric. [S2020-E04, E13, E16] |

**Công thức LOA và cách diễn giải:** với một paired observation, bài đặt `dᵢ = Aᵢ − Bᵢ`, `mᵢ = (Aᵢ + Bᵢ)/2`; `d̄` là bias và `s` là SD của paired differences. Khi assumptions phù hợp, `LOA_lower = d̄ − 1.96 × s`, `LOA_upper = d̄ + 1.96 × s`. Đây là khoảng mô tả xấp xỉ 95% differences, **khác** với 95% confidence intervals quanh các estimates. Ngưỡng acceptable difference do mục tiêu ứng dụng quyết định trước, không lấy chính empirical LOA làm chứng cứ rằng sai số đã chấp nhận được. [S2020-E08; câu cuối là diễn giải phân tích]

**Phân biệt thuật ngữ:** “surrogate” trong bài này nghĩa là **phép đo thay thế** cho một reference measure. Không phải surrogate time series dùng để kiểm định null model như phase randomization hoặc **PPS**. Review không thực hiện PPS, Simplex forecasting hay Rosenstein LLE. [S2020-E06, E09–E16]

### Principal empirical findings / review findings

| Kết quả review thuật lại | Điều kiện, số liệu/hướng kết quả | Vị trí | Ranh giới bằng chứng |
|---|---|---|---|
| Nhiều UST studies chưa kiểm chứng criterion validity | Tác giả báo cáo 17/28 không khảo sát; 8 chủ yếu correlation/group differences; 3 dùng LOA criterion | Abstract p. 1; UST HRV Research/Table 2 p. 5 | Là phân loại của authors; Table 2 có overlapping entries, không coi là mutually exclusive list đã được tái kiểm chứng. [S2020-E01, E05, E16] |
| Bốn study có LOA plots | Baek 2015, Esco & Flatt 2014, Munoz 2015, Shaffer 2019 | Table 3 p. 7; phần LOA studies p. 8 | Chỉ ba được review phân loại là dùng LOA criterion; Baek dùng correlation/group comparison để ra quyết định. [S2020-E09] |
| Baek 2015 | 467 người khỏe mạnh, 8–69 tuổi; resting PPG, sitting; significant Pearson r và non-significant Kruskal–Wallis là tiêu chí | pp. 7–8, Table 3 | LOA plots được trình bày nhưng review nói không dùng để rút conclusions; không coi là validation bằng LOA. [S2020-E09] |
| Esco & Flatt 2014 | 23 nam collegiate athletes, 19–21 tuổi; supine pre/post-exercise; review báo **60 s** để ước lượng 300-s RMSSD | pp. 7–8, Table 3 | So sánh log-transformed 10/30/60 s, ICC và LOA; chỉ RMSSD trong protocol này. [S2020-E10] |
| Munoz 2015 | 3,387 người, 44–63 tuổi; Portapres finger pressure, supine baseline; review báo **10 s RMSSD**, **30 s SDNN** | pp. 7–8, Table 3 | Dữ liệu cuối 4–5 min có stationarity pattern; không suy ra tương đương cho mọi modality/state. Sex counts trong Table 3 và prose bất nhất. [S2020-E11] |
| Shaffer 2019 | 38 healthy undergraduates, 18–23 tuổi, 20 nam/18 nữ; sitting, resting, eyes open; manual artifact removal | pp. 7–8, Tables 3–4 | Table 3 ghi ECG; prose p. 8 ghi EEG. Báo cáo giữ bất nhất thay vì tự sửa âm thầm. [S2020-E12, E16] |
| Shaffer 2019 chọn proxy theo nhiều tiêu chí | r ≥ 0.90, LOA với allowable difference **±5% của range của 5-min value**, và Student’s t-test theo mô tả review | pp. 7–8 | Không phải ±5% của từng observation; không phải ngưỡng HRV phổ quát. Cách tính “range” chi tiết chưa được xác lập. [S2020-E12, E16] |
| Minimum periods không thống nhất giữa studies | Shaffer 2019/Esco 2014: RMSSD 60 s; Munoz 2015: RMSSD 10 s và SDNN 30 s | p. 8 | Review đề xuất khác biệt có thể do LOA requirement nghiêm hơn và sample nhỏ hơn; không có causal decomposition. [S2020-E10–E13] |

**Table 4: minimum UST periods được review chuyển từ Shaffer et al. (2019).** Reference là 5-min HRV, điều kiện resting của study được mô tả ở trên; đây không phải pooled norms của 28 studies. [S2020-E12–E13]

| Minimum UST period | HRV metrics trong Table 4 | Truy vết |
|---:|---|---|
| **10 s** | HR | [S2020-E13], p. 7 |
| **60 s** | pNN50, NN50, RMSSD, SDNN | [S2020-E13], p. 7 |
| **90 s** | TINN, LF absolute power, SD1, SD2 | [S2020-E13], p. 7 |
| **120 s** | HRV triangular index, **DFA α1** | [S2020-E13], p. 7 |
| **180 s** | LFnu, HF absolute power, HFnu, LF/HF power, **DFA α2, DET, SampEn** | [S2020-E13], p. 7 |
| **240 s** | **ShanEn** | [S2020-E13], p. 7 |

**Đọc đúng bảng:** Table 4 không cung cấp threshold cho mọi metric trong Table 1; ví dụ **REC, D2 và ApEn** không có một minimum period được liệt kê tại Table 4. Bài cũng không báo cáo ở đây threshold cho **Lmean, LAM, TT, Simplex hoặc LLE**. DET trong Table 4 là **recurrence determinism trên HRV interbeat-interval series**, không phải validation trực tiếp cho DET tính trên waveform PPG. [S2020-E04, E13, E16]

### Interpretation and claims

**Tác giả thực sự kết luận gì?** Review cho rằng các prescriptions về minimum duration chỉ dựa trên correlation/group differences cần được dùng thận trọng và xác nhận bằng LOA criterion cùng equality tests theo đề xuất của tác giả. Bài kêu gọi evidence về accuracy và predictive validity trước khi áp dụng UST rộng rãi trong medicine, performance và personal wellness. [S2020-E14–E15]

**Điều nguồn trực tiếp hỗ trợ mạnh:** sự khác biệt giữa association và agreement; nhu cầu đặt trước acceptable difference; yêu cầu báo uncertainty của bias/LOA; duration khác theo feature và nghiên cứu; artifacts có thể làm hỏng HRV measurements. Những điểm này có thể dẫn mà không cần khẳng định một duration áp dụng chung. [S2020-E01, E06–E08, E10–E15]

**Nhận xét phân tích về equality tests:** bài phản đối việc coi non-significant mean/median difference là evidence of comparability, nhưng sau đó lại đề xuất Student’s t-test để xác nhận equality. H0: mean difference = 0 kiểm tra average bias; không bác bỏ H0 không chứng minh hai methods tương đương trong một sai số đặt trước, và mean bias nhỏ vẫn có thể đi cùng individual differences lớn. Vì vậy nên giữ phần khuyến nghị LOA/a priori tolerance và thuật rõ equality-test advice là lời khuyên của nguồn, không viết “t-test không significant chứng minh validity”. Đây là đánh giá logic thống kê của báo cáo, không phải lời tự phê bình của authors. [S2020-E07–E08, E14]

**Nhận xét phân tích về transfer sang PPG:** thời lượng của HRV intervals và waveform PPG không chỉ khác số sample; chúng là hai representations khác nhau. Một cửa sổ PPG sampling cao không tự chứa lượng thông tin về beat-to-beat variability tương đương một bản ghi dài. Bài tạo rationale cho việc kiểm tra độ phụ thuộc duration nhưng không cung cấp validation trực tiếp cho cấu hình NTSA hiện tại. [S2020-E02–E04, E13, E16]

### Limitations

| Loại | Giới hạn | Nguồn / hệ quả |
|---|---|---|
| Tác giả nêu | Không có accuracy standards tương đương heart rate/blood pressure cho các ST HRV features như SDNN | p. 6; ngưỡng phải phù hợp câu hỏi, không mặc định lấy ±5% làm chuẩn chung. [S2020-E08] |
| Tác giả nêu | UST predictive validity cần được xác lập; UST là proxies of proxies | pp. 1, 3, 9; agreement với 5 min không thay thế outcome validation. [S2020-E01, E03, E15] |
| Tác giả nêu | Artifactual heartbeat có thể làm thay đổi mạnh HRV; cần automatic artifact correction để mở rộng ứng dụng | pp. 1, 9; không có artifact-tolerance benchmark mới trong review. [S2020-E01, E15] |
| Tác giả nêu | Minimum periods khác nhau giữa các studies; stricter LOA và sample size được nêu như lời giải thích có thể | p. 8; không có ngưỡng phổ quát cho RMSSD/SDNN. [S2020-E10–E13] |
| Tác giả nêu | Cần accuracy ở stationary/non-stationary conditions, age/sex norms và health/performance outcomes | pp. 3–4, 9; mục tiêu phát triển, không phải kết quả đã hoàn thành. [S2020-E03, E15] |
| Nhận xét phân tích | Search/screening protocol không đủ để đánh giá coverage hoặc selection bias như một systematic review | Toàn PDF; không gọi đây là comprehensive systematic review/meta-analysis. [S2020-E16] |
| Nhận xét phân tích | Bằng chứng cho các studies được thuật lại là secondary; không có raw data, code hoặc detailed estimator settings | pp. 7–8; không tuyên bố tái lập DFA/RQA/entropy từ review. [S2020-E09–E13, E16] |
| Nhận xét phân tích | “Equality test” không tự chứng minh equivalence | pp. 6–8; giữ sự khác nhau giữa mean bias và individual agreement. [S2020-E07–E08, E14] |
| Nhận xét phân tích | Phạm vi là HRV intervals và method validity; không trực tiếp khảo sát raw PPG dynamics across states | Toàn PDF; giới hạn khả năng hỗ trợ claims về manuscript. [S2020-E02–E04, E16] |

**Bất nhất trong nguồn cần ghi nhận:** [S2020-E16]

- **Sensor của Shaffer 2019:** Table 3 p. 7 ghi **ECG**, prose p. 8 ghi **EEG**. Có thể là lỗi biên tập, nhưng PDF này không cho phép xác nhận nguyên nhân. Khi mô tả, dùng “ECG theo Table 3; prose ghi EEG”, hoặc tránh chi tiết modality cho tới khi kiểm tra primary source.
- **Sex counts của Munoz 2015:** Table 3 ghi **1,658 nam / 1,729 nữ**; prose p. 8 ghi **1,660 nam / 1,727 nữ**. Tổng N = **3,387** nhất quán; không chọn một sex breakdown như đã xác thực.
- **Nhóm trong Table 2:** phần correlation/group differences có **10 entries**, gồm Esco & Flatt và Munoz cũng xuất hiện trong nhóm LOA; Li et al. (2009) còn xuất hiện ở nhóm không khảo sát validity. Abstract/prose báo **17/8/3**. Không xem Table 2 là một partition không chồng lấn.
- **Mô tả r²:** p. 6 ghi range −1 đến +1, trong khi định nghĩa ngay tại đó là bình phương Pearson r. Với định nghĩa `r² = r × r`, range là **0 đến 1**. Đây là hiệu chỉnh đại số của báo cáo, không chép lỗi nguồn như một tính chất thống kê.
- **LF lower bound:** p. 3 và footnote Table 1 p. 4 có **0.004 Hz**, trong khi p. 3 đoạn trước và dòng LF của Table 1 ghi **0.04 Hz**. Không lấy số bất nhất làm thông số triển khai từ review này.

### Relevance to current manuscript

Phân loại dưới đây là **nhận xét phân tích**, không phải endorsement cho kết quả của manuscript.

| Thành phần | Phân loại | Lý do và giới hạn | Nguồn |
|---|---|---|---|
| Ultra-short windows | **Direct methodological relevance** | Cung cấp rationale đánh giá duration theo feature, reference và acceptable error | [S2020-E03, E08, E13–E15] |
| Chọn cửa sổ PPG 60 s | **Indirect conceptual relevance** | 60 s đủ cho một số HRV features trong Shaffer 2019; không validate mọi NTSA feature trên waveform PPG | [S2020-E12–E13, E16] |
| DFA trong dự án | **Indirect conceptual relevance** | Table 4 có α1 120 s, α2 180 s trên HRV; không xác lập scales, detrending order hay settings cho `core_ntsa/dfa.py` | [S2020-E04, E13, E16] |
| RQA recurrence organization | **Indirect conceptual relevance** | DET có minimum 180 s trong study HRV được thuật lại; không có minimum cho Lmean/LAM/TT | [S2020-E13, E16] |
| Simplex forecastability | **No direct algorithmic relevance** | Không thực hiện Simplex hoặc đánh giá forecast error theo horizon | [S2020-E16] |
| Rosenstein divergence/LLE | **No direct algorithmic relevance** | Không có LLE estimation hoặc fit-window validation | [S2020-E16] |
| RQ1: PPS/noisy pseudoperiodic null | **No direct relevance** | “Surrogate” nghĩa là proxy measure; không có PPS null test | [S2020-E06, E16] |
| RQ2: Awake–Drowsy | **Background relevance** | Nêu nhu cầu validity trong các điều kiện; không so sánh hai trạng thái này | [S2020-E03, E09–E12, E16] |
| Bias/agreement khi so cửa sổ ngắn–dài | **Direct methodological relevance** | LOA, a priori tolerance và confidence intervals là đóng góp trực tiếp | [S2020-E06–E08, E14] |
| Signal/beat quality | **Direct relevance cho HRV; indirect cho waveform NTSA** | Artifact warning tập trung vào interbeat intervals; chưa lượng hóa effects trên waveform metrics | [S2020-E01, E12, E15–E16] |
| Health/performance inference | **Direct conceptual relevance** | Phân biệt estimation agreement với predictive validity; không xác lập drowsiness classification performance | [S2020-E03–E04, E15–E16] |

### Source evidence

| Mã / Paper ID | Trang PDF, section, figure/table | Bằng chứng diễn giải trung thành | Confidence |
|---|---|---|---|
| **S2020-E01 / S2020** | p. 1, metadata/Abstract | Tên bài, authors, review, ngày xuất bản, DOI; UST <5 min/ST ~5 min; 28 studies ≥20 participants; phân loại 17/8/3; artifacts và proxies of proxies | High |
| **S2020-E02 / S2020** | pp. 2–3, Heart Rate Variability; Length of the HRV Recording Period | HRV từ interbeat intervals; neurovisceral integration/vagal tank là background; LT ≥24 h, ST ~5 min, UST <5 min; khác physiological processes/predictive powers | High |
| **S2020-E03 / S2020** | pp. 3–4, Length of the HRV Recording Period; Why Is There Interest in UST HRV Measurements? | LT/ST norms không interchangeable; UST predictive validity cần nghiên cứu; motivation tasks/wearables; ECG/PPG xác định beats; cần validation stationary/non-stationary conditions và norms | High |
| **S2020-E04 / S2020** | p. 4, Table 1; Criterion Validity Ensures Measurement Integrity | Danh mục time/frequency/nonlinear HRV metrics; DFA α1/α2, DET, REC, entropy/Poincaré/CD; concurrent/predictive approaches; relevant/reliable/valid criterion | High |
| **S2020-E05 / S2020** | p. 5, UST HRV Research; Table 2 | Prose báo 28 studies ≥20 participants, 17 không validity, 8 chủ yếu association/group comparison; phê bình không kiểm soát measurement bias; Table 2 liệt kê các nhóm | High cho báo cáo authors; Medium cho nhất quán phân nhóm |
| **S2020-E06 / S2020** | pp. 5–6, Correlation Coefficients; Figures 1–2 | Correlation không xác lập agreement; hypothetical r = 1 và +10 bpm bias; minh họa scatterplot/Bland–Altman | High |
| **S2020-E07 / S2020** | pp. 5–6, Coefficient of Determination or Regression; Group Mean or Median Comparisons | r²/regression không tự chứng minh agreement; bàn Deming/Passing–Bablok; non-significant group difference có thể do power/N và không kiểm chứng individual agreement | High |
| **S2020-E08 / S2020** | pp. 6–8, Limits of Agreement (LOA) Solutions | A priori acceptable differences; paired difference-vs-mean plot; d̄ ±1.96 × s với normal differences; CI cho bias/LOA; transformations; equality-test advice; HRV accuracy standards chưa có theo bài | High |
| **S2020-E09 / S2020** | pp. 7–8, Table 3; UST HRV Studies That Report Limits of Agreement Solutions, opening/Baek paragraph | Bốn studies có LOA plots; Baek n = 467, PPG sitting baseline, 8–69 tuổi; r và Kruskal–Wallis dùng chọn duration, LOA không dùng ra conclusions | High |
| **S2020-E10 / S2020** | pp. 7–8, Table 3; Esco & Flatt paragraph | n = 23 nam athletes 19–21 tuổi, supine, trước/sau treadmill; ECG, last 5 min; log 10/30/60 s vs 300 s RMSSD, ICC/LOA; review kết luận 60 s | High cho secondary reporting |
| **S2020-E11 / S2020** | pp. 7–8, Table 3; Munoz paragraph | N = 3,387, 44–63 tuổi, supine, Portapres finger pressure, 15-min acquisition/last stationary 4–5 min; RMSSD 10 s/SDNN 30 s; sex breakdown bất nhất | High cho protocol/tổng N; Medium cho sex counts |
| **S2020-E12 / S2020** | pp. 7–8, Table 3; Shaffer et al. (2019) paragraph | n = 38, 20 nam/18 nữ, 18–23 tuổi, resting/sitting/eyes open, 5 min; epochs 10–240 s; manual artifact removal, r ≥ 0.90, LOA ±5% range và t-test; ECG/EEG bất nhất | High cho settings được nêu; Medium cho modality |
| **S2020-E13 / S2020** | p. 7, Table 4; p. 8, comparison paragraph | Minimum periods từ Shaffer 2019: HR 10; time-domain features 60; TINN/LF/SD1/SD2 90; HTI/DFA α1 120; frequency features/DFA α2/DET/SampEn 180; ShanEn 240; khác Munoz, authors nêu possible stricter LOA/smaller sample | High cho bảng/wording; Medium cho giải thích nguyên nhân |
| **S2020-E14 / S2020** | p. 8, Practical Recommendations | Bốn bước: distribution/transformation, a priori tolerance, LOA+CI/equality test, tăng duration nếu không đạt; không có code hoặc validation mới | High |
| **S2020-E15 / S2020** | pp. 8–9, Conclusion | 8/11 validity studies dùng criteria không kiểm soát bias; sáu hướng phát triển gồm artifact correction, chọn ST outcome-related metrics, UST duration, predictive validity, age/sex norms, education | High |
| **S2020-E16 / S2020** | Toàn PDF pp. 1–11; đối chiếu Tables 1–4/prose pp. 3, 6–8 | Không báo cáo cohort mới, meta-analysis/search protocol chi tiết, PPS/Simplex/LLE, Awake–Drowsy comparison hoặc full estimator settings; Tables/prose có các bất nhất được nêu trong Limitations | High cho nội dung đối chiếu trực tiếp; Medium cho audit thông tin thiếu |

## 3. Comparison of the UST Studies Discussed in the Review

Phần này thay cho các mục audit từng bài gốc trong mẫu ba nghiên cứu. **Chỉ so sánh cách Shaffer 2020 thuật lại bốn study có LOA**, không giả định đã đọc bốn primary sources. [S2020-E09–E13]

| Study được review | Sample / acquisition | Duration so với reference | Metric / decision criterion | Điều có thể rút ra |
|---|---|---|---|---|
| Baek 2015 | 467 healthy; PPG; sitting baseline | Prose liệt kê 10, 20, 30, 60, 90, 180, 210, 240, 270 s vs 300 s | Nhiều HRV metrics; r và non-significant Kruskal–Wallis; LOA chỉ minh họa | Có LOA plot không đủ để gọi là LOA-based validation. [S2020-E09] |
| Esco & Flatt 2014 | 23 nam athletes; ECG; supine pre/post-exercise | 10/30/60 s vs 300 s | RMSSD log-transformed; ICC và LOA | Review báo 60 s; scope là metric/protocol này. [S2020-E10] |
| Munoz 2015 | 3,387; Portapres finger pressure; supine baseline | 10/30/120 s so với reference 5 min trong mô tả review | RMSSD/SDNN log-transformed; ICC, r, LOA | Review báo 10 s RMSSD, 30 s SDNN; khác Shaffer 2019. [S2020-E11] |
| Shaffer 2019 | 38 healthy undergraduates; sitting baseline; ECG theo Table 3, prose ghi EEG | 10/20/30/60/90/120/180/240 s vs 300 s | Table 1 metrics; r ≥ 0.90, LOA ±5% range, t-test | Minimum periods theo feature ở Table 4, không dùng như universal norms. [S2020-E12–E13] |

## 4. Duration Requirements and Representation Boundaries

**Một mốc 60 s không có cùng ý nghĩa cho mọi feature.** Trong Table 4, RMSSD và SDNN có mốc 60 s, trong khi DFA α1 là 120 s và DET là 180 s. Mặt khác, Munoz được review báo RMSSD 10 s. Khác biệt này cho thấy một con số cần đi kèm metric, reference, protocol và acceptance criterion; review không chứng minh một cutoff duy nhất. [S2020-E10–E13]

**Nhận xét phân tích:** khi dùng nguồn cho manuscript cần phân biệt ba câu hỏi:

1. Có thể tính được metric trên một cửa sổ ngắn hay không?
2. Estimate từ cửa sổ ngắn có agreement đủ tốt với estimate dài hơn trong cùng setting hay không?
3. Estimate đó có giúp dự báo outcome hoặc phân biệt trạng thái theo thiết kế nghiên cứu hay không?

Review tập trung vào câu hỏi 2 cho UST HRV và kêu gọi bằng chứng cho predictive validity thuộc câu hỏi 3. Việc thuật toán trả về một giá trị ở câu hỏi 1 không giải quyết hai câu hỏi còn lại. Tương tự, finding Awake–Drowsy khác nhau không tự chứng minh interchangeability với bản ghi 5 min. [S2020-E04, E06–E08, E15–E16]

## 5. Relationship to the Existing PPG Evidence Audit

Mục này nối vai trò của nguồn mới với **phạm vi manuscript và các nhóm evidence trong `summary.md`**, không tái audit các PDF Sviridova ở đây.

| Vai trò trong literature review | Đóng góp của Shaffer 2020 | Cách kết nối với manuscript |
|---|---|---|
| Background về recording length | Phân biệt UST/ST/LT và predictive powers | Motivate cửa sổ ngắn, đồng thời xác định câu hỏi cửa sổ đang trả lời. [S2020-E02–E03] |
| Phương pháp validity | Association/group comparison không đủ agreement; LOA cần tolerance | Bổ sung một góc nhìn về validation, bên cạnh prediction, divergence và recurrence trong mẫu review. [S2020-E06–E08] |
| Feature-specific duration | Table 4 có DFA/DET/entropy thresholds trên HRV | Cung cấp tiền lệ cần duration sensitivity; không nhập thresholds của HRV như đã validate waveform PPG. [S2020-E13, E16] |
| Quality và applicability | Artifact control và predictive validity là thách thức | Motivate reporting chất lượng và giới hạn outcome inference. [S2020-E01, E15] |
| State comparison | Không có Awake–Drowsy experiment | Hỗ trợ rationale phương pháp, không cung cấp expected direction của state differences. [S2020-E16] |

## 6. Critical Scientific Synthesis

### A. Bài đã xác lập điều gì trong phạm vi review?

Bài trình bày rõ vì sao correlation, explained variance và non-significant group averages có thể gây ngộ nhận về khả năng thay thế phép đo. Nó cũng tập hợp các kết quả duration không thống nhất và làm rõ distinction giữa LOA plots và LOA decision criteria. Đây là đóng góp phương pháp cho thiết kế validation, không phải empirical proof về dynamics hoặc physiological states của waveform PPG. [S2020-E05–E13]

### B. Những claims nào còn conditional?

| Claim | Điều nguồn thực sự cho | Điều chưa được xác lập |
|---|---|---|
| “UST thay thế được ST” | Một số feature/durations trong studies cụ thể đạt tiêu chí được review mô tả | Agreement mọi population/state/sensor và criteria. [S2020-E09–E13] |
| “60 s đủ cho HRV” | Một số time-domain features ở Table 4; RMSSD 60 s trong Esco/Shaffer | Mọi HRV metric, nhất là DFA/DET/entropy. [S2020-E10, E13] |
| “LOA chứng minh validity” | LOA là công cụ agreement được khuyến nghị | Validity nếu chưa có tolerance hợp lý, uncertainty/assumption checks và relevant criterion. [S2020-E04, E08] |
| “UST có giá trị dự báo sức khỏe” | Đây là nhu cầu cần được chứng minh | Outcome validation mới của review. [S2020-E03, E15] |
| “DET 180 s áp dụng cho PPG” | Table 4 thuật HRV DET 180 s ở Shaffer 2019 | Validation DET trên raw waveform PPG và chosen RQA settings. [S2020-E13, E16] |

### C. Bài học phương pháp manuscript có thể kế thừa

**Nhận xét phân tích:** trước hết xác định mục tiêu của short-window analysis: mô tả state-specific dynamics hay thay thế một longer-reference estimate. Nếu claim interchangeability, cần reference phù hợp, tolerance đặt trước và agreement/uncertainty theo từng feature. Nếu chỉ mô tả hoặc so sánh states, vẫn cần quality và duration sensitivity, nhưng không phải mọi phân tích đều là method-comparison study mà bài này thảo luận. Không áp máy móc quy trình LOA vào mọi RQ. [S2020-E04, E08, E14–E16]

Các kết quả DFA/DET trong review nhắc rằng duration có thể ảnh hưởng khác nhau tới features. Tuy nhiên, bài không xác lập settings của DFA/RQA cho dữ liệu hiện tại; cần reporting và kiểm chứng từ implementation/dataset của manuscript. [S2020-E04, E13, E16]

### D. Những comparisons chưa trực tiếp được khảo sát

Trong phạm vi PDF này không có waveform PPG Simplex forecastability, PPS null rejection, Rosenstein divergence hoặc joint comparison DET/Lmean/LAM/TT giữa Awake và Drowsy. Review cũng không cung cấp direction hoặc effect size cho trạng thái buồn ngủ. Đây là absence trong **nguồn được audit**, không phải universal absence trong literature. [S2020-E16]

## 7. Defensible Research Gap

**Gap được hỗ trợ bởi nguồn này:** Shaffer 2020 chỉ ra nhu cầu xác lập accuracy/agreement và ý nghĩa của UST HRV theo feature và conditions. Review không trực tiếp trả lời liệu complementary dynamics của waveform PPG trong cửa sổ ngắn thay đổi giữa Awake và Drowsy như thế nào. Nguồn này có thể hỗ trợ một **methodological motivation** cho đánh giá duration và quality; nó không tự tạo empirical evidence cho state dynamics. [S2020-E03, E13–E16]

**Nhận xét phân tích — gap cho manuscript:** có thể đặt câu hỏi về empirical characterization của forecastability, recurrence organization và local divergence trên short state-labeled PPG, kèm kiểm tra độ phụ thuộc duration/quality thích hợp. Claim của manuscript cần giới hạn ở properties được đo và design thực tế, không dựa vào review HRV để khẳng định PPG 60 s đã được validate. [S2020-E08, E13, E16; manuscript context]

**Gap cần broader verification:** “đầu tiên trên thế giới”, “chưa ai khảo sát nonlinear PPG trong drowsiness”, hoặc “không có validation nào sau 2020”. Một review xuất bản 2020 không xác lập tình trạng toàn literature hiện nay; báo cáo này không thực hiện systematic search ngoài PDF được cung cấp. [S2020-E01, E16]

## 8. Introduction-Ready Evidence Table

| Vai trò | Statement được evidence hỗ trợ | Vị trí | Điều kiện / classification |
|---|---|---|---|
| UST motivation | Thời gian đo 5 min thúc đẩy nghiên cứu UST HRV dưới 5 min | pp. 1,3 | **Direct support** cho HRV rationale; không có validated PPG 60 s claim. [S2020-E01, E03] |
| Recording-length distinction | UST, ST, LT không tự interchangeable dù cùng metric formulas | p. 3 | **Direct support** cho review statement; không dùng LT norms cho UST. [S2020-E02–E03] |
| Validity caution | Correlation cao không tự xác lập absolute agreement giữa short và reference measures | pp. 5–6; Figures 1–2 | **Direct support**; hypothetical example, không empirical bias estimate. [S2020-E06] |
| Agreement framework | Accuracy assessment cần tolerance đặt trước và LOA/uncertainty | pp. 6–8 | **Direct support** cho methodological recommendation. [S2020-E08, E14] |
| Feature-specific duration | Minimum periods của các HRV features khác nhau trong study được review tổng hợp | Table 4 p. 7; p. 8 | **Direct support qua secondary reporting**; không pooled universal thresholds. [S2020-E12–E13] |
| DFA/DET examples | Table 4 báo DFA α1 120 s; DFA α2/DET 180 s | p. 7 | **Direct support qua secondary reporting** cho HRV; **Unsupported** nếu viết như PPG waveform validation. [S2020-E13, E16] |
| Data quality | Artifactual beats có thể ảnh hưởng mạnh tới HRV; review yêu cầu artifact correction | pp. 1,9 | **Direct support** cho HRV; **Partial support** cho general quality motivation của waveform NTSA. [S2020-E01, E15] |
| Predictive validity | Agreement với ST không thay thế evidence dự báo real-world outcomes của UST | pp. 3,9 | **Direct support** cho rationale trong review. [S2020-E03, E15] |
| State-specific gap | Nguồn này không directly compare complementary waveform dynamics giữa Awake/Drowsy | Toàn PDF | **Direct support** cho limited-source absence; không universal novelty. [S2020-E16] |
| RQ1/RQ2 motivation | Short-window state analysis cần assumptions và reliability được đánh giá riêng | pp. 3–4, 8–9 | **Partial support**: synthesis cho manuscript, không source outcome. [S2020-E03–E04, E08, E15–E16] |

**Chi tiết phù hợp Methods/Discussion hơn Introduction — nhận xét phân tích:** LOA formulas/CI, exact tolerance, lựa chọn raw-vs-log differences, beat correction, sample dependence, DFA fitting scales và recurrence parameters. Introduction có thể nêu principle về feature-specific duration và inferential limits mà không liệt kê mọi cutoff. [S2020-E08, E13–E16]

## 9. Statements to Avoid or Qualify

| Tránh hoặc qualify | Vì sao | Hướng diễn đạt |
|---|---|---|
| “Shaffer 2020 proved 60-s PPG is reliable” | Bài là review HRV; không validation waveform PPG 60 s. [S2020-E01, E13, E16] | Review motivates feature-specific validation of short measurements |
| “UST means <1 min” | Bài định nghĩa UST <5 min. [S2020-E01–E03] | Ghi rõ definition của nguồn và duration thực tế |
| “All HRV features need only 60 s” | Table 4 có 120/180/240 s cho nhiều features. [S2020-E13] | Nêu metric/protocol/criterion cụ thể |
| “DFA α1/α2 were validated on 60-s waveform PPG” | Bảng là HRV:120/180 s; không DFA waveform implementation. [S2020-E13, E16] | Tách representation và validation của dataset hiện tại |
| “DET 180 s is a universal cutoff” | Secondary report cho một HRV study, không universal threshold. [S2020-E12–E13] | Reported minimum under the reviewed study’s conditions |
| “r ≥ 0.90 proves agreement” | r sàng lọc potential proxy; không kiểm soát bias. [S2020-E06, E12] | Correlation indicates association; agreement assessed separately |
| “p>0.05 proves equivalence” | Group difference/equality test không tự kiểm chứng acceptable individual errors. [S2020-E07–E08, E14] | Nêu bias/LOA/tolerance và uncertainty theo mục tiêu |
| “95% of points inside empirical LOA means valid” | LOA mô tả differences; vẫn cần ngưỡng ngoài đặt trước. [S2020-E08] | So agreement với acceptable error đã xác định |
| “±5% is the accepted HRV standard” | ±5% range là tiêu chí study 2019; review nói chưa có comparable HRV accuracy standards. [S2020-E08, E12] | Study-specific acceptable difference |
| “Four studies validated UST using LOA” | Bốn có plots, Baek không dùng LOA ra conclusion. [S2020-E09] | Four reported plots; three classified as LOA-criterion studies |
| “Shaffer 2020 ran PPS surrogate tests” | Surrogate là proxy measure, không surrogate-data null test. [S2020-E06, E16] | Dẫn PPS từ một primary algorithm/application source khác |
| “HRV outcome associations validate drowsiness detection” | Không có Awake–Drowsy experiment hoặc classifier outcome validation. [S2020-E02–E03, E16] | Background rationale; state inference cần evidence riêng |
| “28 independent experiments were pooled” | Không meta-analysis/cohort mới; Table 2 còn overlap entries. [S2020-E05, E16] | Authors critically reviewed 28 studies |
| “This review establishes current universal norms” | Review 2020, không systematic current-literature verification. [S2020-E01, E16] | Giới hạn vào studies và definitions được review |

## 10. Outstanding Questions and Verification Needs

### Những chi tiết chưa được xác lập từ PDF

| Câu hỏi | Source/status | Ý nghĩa khi sử dụng |
|---|---|---|
| Search databases, dates, strings và screening rules là gì? | **Not established** ngoài tiêu chí minimum 20 participants và corpus được nêu. [S2020-E05, E16] | Không gọi review comprehensive/systematic nếu chưa xác minh |
| Shaffer 2019 thực tế dùng ECG hay EEG? | **Unresolved:** Table 3 vs prose. [S2020-E12, E16] | Kiểm tra primary source trước khi khẳng định modality |
| Sex breakdown chính xác của Munoz 2015? | **Unresolved:** bảng và prose khác, tổng 3,387 nhất quán. [S2020-E11, E16] | Dùng tổng N, không chọn breakdown tùy ý |
| ±5% range được tính cụ thể thế nào, ở scale nào? | **Not established đầy đủ.** [S2020-E12, E16] | Không tự chuyển thành ±5% từng giá trị hoặc một margin dùng chung |
| Exact LOA acceptance margins của Esco/Munoz? | **Not established đầy đủ** trong phần thuật lại. [S2020-E10–E11, E16] | Cần primary sources nếu so sánh mức nghiêm ngặt/tái lập |
| LOA estimates, confidence intervals và sample-specific distributions? | Review không trình bày đầy đủ numerical agreement results của từng feature/study. [S2020-E09–E13, E16] | Không chế ra effect sizes, bias hoặc uncertainty từ minimum-duration table |
| DFA scales/order/fit và RQA embedding/ε/Theiler/lmin? | **Not established.** [S2020-E04, E13, E16] | Không dùng review làm specification cho `dfa.py` hoặc RQA |
| Vì sao một số Table 1 metrics thiếu threshold ở Table 4? | **Not established.** [S2020-E04, E13, E16] | Không suy ra missing metric failed hoặc cùng cutoff với metric khác |
| Dependence/epoch selection/repeated-window treatment? | **Not established đầy đủ.** [S2020-E09–E12, E16] | Cần primary study methods nếu muốn đánh giá agreement design |
| Thresholds có chuyển được sang PPG Awake/Drowsy 60 s không? | **Không được thiết lập trong nguồn.** [S2020-E16] | Cần evidence trên representation, protocol và features của manuscript |

### Verification cần cho claims vượt phạm vi nguồn

1. **Primary-source verification** nếu đưa exact minimum periods, acquisition details hoặc LOA margins vào Methods/Discussion; nhất là Shaffer 2019 và các bất nhất về modality/sex counts.
2. **Dataset-specific duration/quality assessment** cho waveform PPG và các chosen metrics. Review cung cấp motivation, không cung cấp kết quả của phép kiểm chứng này.
3. **Claim-specific validation:** phân biệt stability, agreement với reference, association với state và prediction of outcomes; chọn evidence phù hợp với claim thực sự của manuscript.
4. **Broader literature verification** trước universal novelty hoặc phát biểu về tình trạng nghiên cứu hiện nay.

Đây là recommendations từ critical synthesis, không phải những analyses đã được thực hiện trong PDF hoặc bằng chứng rằng manuscript chắc chắn phải đạt một cutoff HRV cụ thể.

## 11. Recommended Introduction Narrative Structure

Đây là **logical sequence**, không phải polished English prose hoặc đoạn Introduction hoàn chỉnh.

1. **Motivate short measurements:** nhu cầu giảm thời gian đo và khảo sát physiological tasks ngắn khiến UST được quan tâm; chỉ rõ Shaffer 2020 bàn về HRV. [S2020-E01, E03]
2. **Nêu methodological caution:** shorter estimates không tự interchangeable với ST/LT, dù dùng cùng metric formulas. [S2020-E02–E03]
3. **Nêu contribution chính:** review chỉ ra correlation/group averages chưa đủ agreement; cần acceptable error đặt trước và đánh giá bias/LOA phù hợp. [S2020-E06–E08]
4. **Chuyển sang feature dependence:** duration requirements khác giữa HRV features và studies; có thể dẫn Table 4 như một ví dụ được review thuật lại, tránh biến thành cutoff cho waveform PPG. [S2020-E10–E13]
5. **Nối với manuscript:** các bài học này motivate khảo sát complementary short-window PPG dynamics với duration/quality checks riêng; không claim nguồn đã validate Simplex/RQA/Rosenstein trên 60 s. [S2020-E13, E16; manuscript context]
6. **Giới hạn state/outcome inference:** review chưa trực tiếp trả lời Awake–Drowsy và agreement không đồng nghĩa predictive validity. Nêu RQ của manuscript theo empirical state association/dynamical characterization và giới hạn design thực tế. [S2020-E03–E04, E15–E16]

