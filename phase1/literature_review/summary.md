# Evidence Audit: Munoz (2015) and Hypertension PPG RQA (2020)

> Báo cáo phục vụ literature review cho manuscript *Ultra-Short PPG Dynamics Across the Wakefulness-to-Drowsiness Transition: A Nonlinear Time-Series Analysis*. Phân tích dựa trực tiếp trên hai PDF được cung cấp, theo cấu trúc của `summary.md` trước đó. Nội dung này thay thế bản tổng hợp ba bài Sviridova theo yêu cầu của người dùng. Không dùng review Shaffer 2020 để thay thế việc đọc bài gốc Munoz. Không viết đoạn Introduction hoàn chỉnh.

**Quy ước truy vết.** Mọi số trang là **trang PDF, đếm từ 1**. Munoz có trang bài 1–15, trùng trang PDF. Bài NOLTA có trang in 56–58, tức **trang in = trang PDF + 55**. Mã **[M2015-E01]** hoặc **[H2020-E01]** trỏ tới bảng `Source evidence` của từng bài. Confidence đánh giá độ chắc chắn khi trích xuất nguồn, không chứng nhận tính đúng đắn tuyệt đối của kết luận khoa học.

- **High:** văn bản, công thức, bảng hoặc caption nêu rõ.
- **Medium:** cần tổng hợp nhiều vị trí, có bất nhất hoặc cấu hình/phạm vi chưa đầy đủ.
- **Not established from the provided source:** PDF không xác lập thông tin; không điền bằng suy đoán hoặc thông tin từ tài liệu được trích nhưng chưa đọc.
- Các đoạn **Nhận xét phân tích**, relevance và research gap là đánh giá của báo cáo này, không phải kết luận/hạn chế tác giả tự nêu.

| Paper ID | PDF gốc | Số trang |
|---|---|---:|
| M2015 | [Munoz.pdf](paper/Munoz.pdf) | 15 |
| H2020 | [Application of Recurrence Quantification Analysis to Hypertension Photoplethysmograms](<paper/Application of Recurrence Quantification Analysis to Hypertension Photoplethysmograms.pdf>) | 3 |

## 1. Executive Scientific Summary

Hai bài cung cấp hai loại bằng chứng khác nhau: **Munoz et al. (2015)** đánh giá agreement của SDNN/RMSSD từ khoảng nhịp tim ngắn với reference dài hơn; **Sviridova & Ikeguchi (2020)** so sánh RQA features của waveform PPG rất ngắn giữa các nhóm huyết áp. Không coi chúng là hai lần validation cùng một representation hoặc cùng một bộ NTSA features. [M2015-E01–E04; H2020-E01–E04]

1. **Munoz 2015:** 3,387 người từ PREVEND; NN intervals suy ra từ **finger beat-to-beat pressure qua Portapres**, không phải ECG trực tiếp dù mục tiêu ứng dụng hướng tới routine ECG. Ba đoạn 10 s, average của ba estimates này (**Avg10s**), đoạn 30 s và 120 s được so với reference danh định **240–300 s** cùng recording. Bài chỉ trực tiếp đánh giá **SDNN và RMSSD**. [M2015-E01–E04]
2. **Munoz findings:** agreement nhìn chung tăng theo duration và RMSSD tốt hơn SDNN. Table 4 ở 120 s: SDNN **r = 0.956, bias = 0.064, d = 0.137**; RMSSD **r = 0.986, bias = 0.014, d = 0.027**. Bias/LOA thuộc **natural-log scale**, không phải ms của raw HRV. Authors khuyến nghị single 10 s cho RMSSD, ưu tiên averaging; SDNN ≥30 s, hoặc multiple 10 s nếu không có 30 s. [M2015-E05–E07, E10–E12]
3. **Hypertension RQA 2020:** PPG-BD, **2.1 s/dataset tại 1 kHz**, **m = 4**. Table 1: **49 normal, 73 preH, 31 S1H, 20 S2H datasets**, tổng **173** do báo cáo cộng. Không tự đổi thành 173 người độc lập hoặc final retained records. Series có **DET < 0.9** bị bỏ; số bị bỏ không được báo cáo. [H2020-E02–E04, E09]
4. **Hypertension findings:** RR/DET không có significant omnibus group difference theo ANOVA; **L, Lmax, TT** được báo khác biệt ở năm cặp nhóm tại level **0.05**. **Không index nào phân biệt S1H với S2H** theo authors. Không có classifier, AUC, sensitivity/specificity, BP prediction error hoặc external validation. [H2020-E05–E09]

**Hàm ý cho manuscript — nhận xét phân tích:** Munoz hỗ trợ rationale về feature-specific duration và phân biệt correlation, bias, agreement, reliability. H2020 là tiền lệ trực tiếp dùng diagonal/vertical RQA trên short waveform PPG và so clinical groups. Hai bài không trực tiếp so **Awake–Drowsy**, không dùng **PPS, Simplex, Rosenstein LLE hoặc DFA**, và không validate bộ complementary metrics hiện tại trên waveform PPG **60 s**. [M2015-E12; H2020-E04–E09]

**Ranh giới suy luận:** group differences không đồng nghĩa reliable estimation theo độ dài hoặc diagnostic performance; high DET không tự chứng minh deterministic chaos. Bootstrap null của Munoz về part–whole agreement khác null noisy pseudoperiodic orbit của PPS. [M2015-E08–E09; H2020-E04–E09; nhận xét phân tích]

## 2. Munoz et al. (2015)

**Thông tin thư mục.** M. Loretto Munoz, Arie van Roon, Harriëtte Riese, Chris Thio, Emma Oostenbroek, Iris Westrik, Eco J. C. de Geus, Ron Gansevoort, Joop Lefrandt, Ilja M. Nolte và Harold Snieder. *Validity of (Ultra-)Short Recordings for Heart Rate Variability Measurements*. **PLOS ONE**, 10(9):e0138921, **28 September 2015**. DOI: [10.1371/journal.pone.0138921](https://doi.org/10.1371/journal.pone.0138921). [M2015-E01]

### Research question and motivation

Bài hỏi SDNN/RMSSD từ recordings rất ngắn phản ánh được “actual HRV” lúc nghỉ đến mức nào, với reference là khoảng 4–5 min của cùng recording. Motivation là lượng routine ECG 10–20 s có sẵn và nhu cầu phenotyping trong large-scale epidemiology. “Actual HRV” được vận hành bằng reference đã chọn, không một ground truth độc lập hoặc 24-h HRV. [M2015-E01–E03]

Authors nhận thấy nghiên cứu trước có sample nhỏ và thường dùng correlation/ICC, chưa mô tả đầy đủ bias/disagreement. Bài kết hợp Pearson r, Bland–Altman LOA, Cohen’s d, ICC giữa ba đoạn 10 s và bootstrap kiểm tra inflation do short segment thuộc full reference. Các liên hệ HRV–mortality là background, không outcome-prediction experiment mới. [M2015-E01, E04, E08–E12]

### Experimental data

| Hạng mục | Thông tin xác lập từ PDF | Truy vết |
|---|---|---|
| Cohort / sample | PREVEND, Groningen, Netherlands; **3,387 người** có usable HRV | [M2015-E02–E03] |
| Sex | Table 1: **1,658 nam, 1,729 nữ** | [M2015-E02] |
| Age | Results gọi mean age 53; Table 1 ghi **53 [44.8–63.2]**, footnote dùng brackets cho IQR. Methods cũng ghi aged 44.8–63.2; **không xác lập đây là observed min–max** | [M2015-E02, E13] |
| Health | General-population cohort, không chỉ healthy volunteers; tác giả báo khoảng 39% hypertension, có diabetes/CKD và comorbidities | [M2015-E02] |
| Modality | Continuous middle-finger pressure qua **Portapres/Beatscope**; cuff ở middle finger của dominant arm | [M2015-E03] |
| Conditions | Supine; quiet room **22°C**; spontaneous breathing; cuff ngang tim; không nói/chuyển động | [M2015-E03] |
| Acquisition / reference | Ghi **15 min**; chọn last stationary **4–5 min**, nominal **240–300 s**; Results: mean **294 s**, observed **239–302 s** | [M2015-E03, E05] |
| Short segments | Ba **non-overlapping 10-s** segments chọn ngẫu nhiên; **30/120 s** lấy từ đầu reference | [M2015-E03], Figure 1 p. 4 |
| Avg10s | Average của ba **estimates**; không nối intervals thành một continuous 30-s series | [M2015-E03] |
| Detection / artifacts | NN detection accuracy **±5 ms**; visual exclusion non-sinus/ectopic/artifactual beats; gaps interpolated; bỏ recording nếu **>5% interpolated NN intervals** | [M2015-E03] |
| Software | CARSPAN 2.0 tính HRV; Stata v11.2 thống kê | [M2015-E03–E04] |
| Selection | Table 2: included **3,387/6,894**, excluded **3,507** | [M2015-E02] |
| Sampling/filter settings | **Not established** đầy đủ; detection accuracy không phải sampling frequency | [M2015-E03, E12] |
| State labels | Resting; không Awake–Drowsy comparison | [M2015-E03, E12] |

### Methods and technical configuration

| Phương pháp thực sự áp dụng | Vai trò / cấu hình | Quan hệ và giới hạn |
|---|---|---|
| **SDNN / RMSSD** | Overall NN variability / successive NN-difference variability, tính ở mọi recording periods | Chỉ time-domain interval HRV, không nonlinear waveform metrics. [M2015-E01, E03] |
| **Natural-log transformation** | lnSDNN/lnRMSSD để distributions xấp xỉ normal; Table 3 báo raw/log | Table 4 agreement numbers thuộc log scale. [M2015-E04–E07] |
| **Pearson r** | Linear association short–reference, có CI | Authors nói r không nhận diện bias; overlap được kiểm tra bằng simulation. [M2015-E04, E06, E08] |
| **Bland–Altman LOA** | Bias = reference log HRV − short log HRV; x-axis dùng **gold-standard value**, khác traditional paired mean | Không nhầm bias CI với LOA. Không xác lập một application-specific tolerance đặt trước. [M2015-E04, E07, E13] |
| **Cohen’s d theo bài** | Bias chia **SD của total-reference values**; generic small/moderate/large thresholds 0.20/0.50/0.80 | Không mặc định denominator là paired-difference SD hoặc pooled SD. [M2015-E04] |
| **ICC giữa ba 10-s estimates** | Absolute agreement, **two-way ANOVA**; Table 5 có ba cặp | Within-record reliability, không separate-session test–retest hay short–reference ICC. [M2015-E04, E10] |
| **Bootstrap simulation** | Approximate remainder HRV bằng variance decomposition; resample short/remainder độc lập với replacement; recombine; **1,000 repetitions**, 95% reference ranges | Null: agreement chỉ do short segment thuộc full recording. Không PPS/phase surrogate hoặc chaos test. [M2015-E08] |
| **Significance** | p<0.05; observed ngoài simulation 95% reference range được gọi significant | Vượt null không tự xác lập clinical interchangeability. [M2015-E04, E08–E09]; nhận xét phân tích |

**Background vs application:** frequency-domain HRV xuất hiện để giải thích scope; authors nói conclusions không áp dụng cho frequency domain. Không có DFA, RQA, entropy, Simplex, LLE hoặc PPS analysis. [M2015-E11–E12]

### Principal empirical findings

**Table 4, p. 9: agreement statistics.** Bias/LOA là chênh lệch trên **natural-log scale**, không ms. Số dẫn từ bảng vì prose p. 9 có LOA bất nhất. r và d không có đơn vị. [M2015-E06–E07, E13]

| Feature | Period | Pearson r | Bias | 95% LOA | Cohen’s d |
|---|---|---:|---:|---|---:|
| SDNN | 10 s, recording 1 | 0.758 | 0.416 | −0.362 đến 1.193 | 0.894 |
| SDNN | 10 s, recording 2 | 0.764 | 0.398 | −0.386 đến 1.181 | 0.855 |
| SDNN | 10 s, recording 3 | 0.760 | 0.406 | −0.386 đến 1.198 | 0.873 |
| SDNN | Avg10s | 0.863 | 0.406 | −0.131 đến 0.944 | 0.874 |
| SDNN | 30 s | 0.859 | 0.240 | −0.300 đến 0.780 | 0.516 |
| SDNN | 120 s | 0.956 | 0.064 | −0.222 đến 0.349 | 0.137 |
| RMSSD | 10 s, recording 1 | 0.853 | 0.096 | −0.525 đến 0.716 | 0.161 |
| RMSSD | 10 s, recording 2 | 0.862 | 0.079 | −0.533 đến 0.691 | 0.150 |
| RMSSD | 10 s, recording 3 | 0.858 | 0.090 | −0.528 đến 0.709 | 0.171 |
| RMSSD | Avg10s | 0.941 | 0.088 | −0.282 đến 0.459 | 0.167 |
| RMSSD | 30 s | 0.932 | 0.055 | −0.343 đến 0.453 | 0.104 |
| RMSSD | 120 s | 0.986 | 0.014 | −0.166 đến 0.194 | 0.027 |

**120-s uncertainty:** SDNN r CI **0.953–0.959**, bias CI **0.059–0.069**, d CI **0.122–0.153**; RMSSD r CI **0.985–0.987**, bias CI **0.011–0.017**, d CI **0.009–0.044**. Bias nhỏ nhưng CI vẫn dương; không viết bias = 0 hoặc perfect agreement. [M2015-E07]

| Finding | Evidence / support | Ranh giới |
|---|---|---|
| Duration dependence | Table 3 raw SDNN mean **25.87 ms Avg10s →35.81 ms reference**; RMSSD **28.17→29.48 ms** | Descriptive; RMSSD ít thay đổi hơn. Prose Avg10s RMSSD ghi 28.16, khác bảng. [M2015-E05, E13] |
| Averaging cải thiện spread | Avg10s r **0.863/0.941** và LOA hẹp hơn single 10 s; bias/d không giảm tương ứng | Không nói averaging loại SDNN bias. [M2015-E06–E07] |
| Correlation có thể che bias | SDNN Avg10s vs 30 s: r **0.863 vs 0.859**, bias **0.406→0.240**, d **0.874→0.516** | Discussion p. 13 dùng ví dụ này phê bình r-only inference. [M2015-E06–E07, E11] |
| Short-epoch reliability | Table 5: SDNN ICC **0.657/0.668/0.670**; RMSSD **0.740/0.751/0.746** | Ba cặp within-record 10-s segments, có CI. [M2015-E10] |
| Beyond trivial overlap | Observed r cao hơn/LOA hẹp hơn simulated null ở mọi duration; bias/d **không khác** expectation | Không viết mọi agreement measure đều vượt null. [M2015-E08–E09] |
| Authors’ recommendations | RMSSD single 10 s, ưu tiên averaging; SDNN ≥30 s hoặc multiple 10 s nếu không có; 120 s đủ theo authors | Không universal NTSA threshold. [M2015-E11–E12] |

### Interpretation and claims

**Authors’ conclusion:** single 10-s RMSSD là valid và averaging được ưu tiên; SDNN nên ≥30 s hoặc multiple 10 s khi không có recording dài hơn; 120 s được xem đủ cho hai metrics. Không mô tả bài như chỉ dùng correlation, vì authors có LOA, d và simulation. [M2015-E01, E07–E12]

**Nhận xét phân tích:** reference chứa short segments, nên agreement không độc lập. Authors nhận diện và kiểm tra bằng bootstrap; đây là điểm mạnh, nhưng không thay thế independent acquisition hoặc cross-sensor validation. “Gold standard” chỉ reference 240–300 s của study. Generic d thresholds/observed LOA không tự tạo một tolerance phù hợp mọi use case. [M2015-E03–E04, E08–E13]

### Limitations

| Loại | Giới hạn | Nguồn / hệ quả |
|---|---|---|
| Tác giả nêu | Non-independence short–full recording; simulation kiểm tra inflation | pp. 4–5,13. [M2015-E08, E11] |
| Tác giả nêu | Single 10-s SDNN là bad proxy; 30-s agreement còn moderate | p. 11. [M2015-E11] |
| Tác giả nêu | Arrhythmia/artifact nguy hiểm với ít beats | p. 13: bỏ edge artifact rồi dùng phần liên tục; interior artifact hoặc >1 artifact thì bỏ segment. Đây là recommendation, khác acquisition interpolation. [M2015-E03, E11] |
| Tác giả nêu | Conclusions không áp dụng cho frequency domain | pp. 13–14. [M2015-E12] |
| Nhận xét phân tích | Motivation ECG nhưng measurement là pressure-derived intervals; stationary/quality-selected sample | Không direct ECG/waveform PPG/transition validation. [M2015-E02–E03, E12] |
| Nhận xét phân tích | Khoảng nửa screening cohort được dùng; chưa xác lập application-specific acceptance margin | Included/excluded comparison không loại trừ mọi selection effect. [M2015-E02, E13] |

**Bất nhất nguồn:** [M2015-E13]

- Prose p. 9 gọi 120-s LOA **−0.059–0.069** cho SDNN và **−0.011–0.017** cho RMSSD; Table 4 LOA là **−0.222–0.349** và **−0.166–0.194**. Bảng có bias CI **+0.059–0.069**, **+0.011–0.017**; prose có dấu hiệu lẫn bounds, nhưng nguyên nhân chưa xác minh. Báo cáo dùng cột LOA của bảng.
- Avg10s raw RMSSD prose p. 6 **28.16 ms**, Table 3 **28.17 ms**. Recording3 RMSSD d **0.171**, CI **0.130–0.170** không bao phủ point estimate; không dùng CI này cho precision claim.
- Age wording và IQR không nhất quán như bảng dữ liệu ở trên. Recent CV event Results p. 5 **6.7%**, Table 1 **106 (3.1%)**; không chọn prose như số chắc chắn.
- Figure 2 caption có “milliseconds” dù kết quả là log-transformed metrics. Không gắn ms cho Table 4 bias/LOA.

### Relevance to current manuscript

| Thành phần | Phân loại | Lý do / giới hạn | Nguồn |
|---|---|---|---|
| Duration sensitivity / agreement | **Direct methodological relevance** | Feature-specific checks; r không đủ bias/agreement | [M2015-E03–E11] |
| Waveform PPG 60 s | **Indirect conceptual relevance** | Không có 60-s arm hoặc waveform NTSA | [M2015-E03, E12] |
| Beat quality | **Direct cho HRV; indirect cho waveform** | Artifact effects chưa benchmark cho waveform estimators | [M2015-E03, E11] |
| RQA/DFA/Simplex/Rosenstein | **No direct algorithmic relevance** | Không thực hiện | [M2015-E12] |
| RQ1: PPS | **No direct relevance** | Bootstrap overlap-null khác dynamics-null | [M2015-E08] |
| RQ2: Awake–Drowsy / outcomes | **Background relevance** | Resting, không state comparison hoặc outcome validation mới | [M2015-E03, E12] |

### Source evidence

| Mã / Paper ID | Trang PDF / vị trí | Evidence | Confidence |
|---|---|---|---|
| **M2015-E01 / M2015** | pp. 1–2 metadata/Abstract/Introduction | Bibliography, routine ECG motivation, n = 3,387, periods/features, recommendations và health background | High |
| **M2015-E02 / M2015** | pp. 2–3 population; p. 5 Results; Tables 1–2 pp. 7–8 | PREVEND, sample/sex/age, comorbidities và included/excluded counts | High cho bảng; Medium cho age/CV discrepancy |
| **M2015-E03 / M2015** | p. 3 procedure/processing; Figure 1 p. 4 | Portapres pressure, conditions, acquisition/reference, NN accuracy/artifacts, segment selection/averaging và CARSPAN | High |
| **M2015-E04 / M2015** | pp. 3–4 statistical analyses | Log metrics, r, BA reference x-axis/bias, d denominator, ICC type, Stata/p threshold | High |
| **M2015-E05 / M2015** | pp. 5–6 Results; Table 3 p. 9 | Reference mean/range; raw/log means theo duration, Avg10s discrepancy | High |
| **M2015-E06 / M2015** | p. 6 correlations; Table 4 p. 9; Figure 3 p. 10 | r/CI theo periods; RMSSD association mạnh hơn, Avg10s–30-s comparison | High |
| **M2015-E07 / M2015** | pp. 6,9–10 LOA/d; Table 4; Figures 4–5 pp. 11–12 | Bias/LOA/d và CI; log scale; prose/table disagreement | High cho bảng; Medium cho consistency |
| **M2015-E08 / M2015** | pp. 4–5 simulation, equations1–2 | Overlap-null, variance approximation, independent resampling, 1,000 repetitions/95% ranges | High |
| **M2015-E09 / M2015** | Figure 2 p. 6; Figure 3 p. 10; Discussion p. 13 | Observed r/LOA vượt null; bias/d không khác expectation | High |
| **M2015-E10 / M2015** | ICC p. 11; Table 5 p. 12 | Ba cặp ICC 10-s SDNN/RMSSD và CI | High |
| **M2015-E11 / M2015** | Discussion pp. 11–13 | Metric comparison, SDNN qualifications, design/reliability, artifact advice và r-only warning | High |
| **M2015-E12 / M2015** | pp. 13–14 conclusion; scope pp. 1–15 | Time-domain scope, ECG/GWAS proposal, duration conclusions; không nonlinear waveform/state/outcome analysis | High cho scope |
| **M2015-E13 / M2015** | Methods pp. 3–4; Results/Figures/Tables pp. 5–10 | No prespecified use-case tolerance established; age/CV/raw mean/LOA/log-unit/d CI inconsistencies | High cho đối chiếu; Medium cho thông tin thiếu |

## 3. Sviridova & Ikeguchi (2020)

**Thông tin thư mục.** Nina Sviridova và Tohru Ikeguchi. *Application of Recurrence Quantification Analysis to Hypertension Photoplethysmograms*. **2020 International Symposium on Nonlinear Theory and Its Applications (NOLTA2020)**, Virtual, **16–19 November 2020**, trang in **56–58**. DOI riêng của conference paper: **Not established from the provided source**. DOI dataset/descriptor trong references không phải DOI bài này. [H2020-E01, E09]

### Research question and motivation

Bài hỏi RQA indices có phát hiện differences trong dynamics của short-recorded PPG giữa **normal, prehypertension, stage 1 và stage 2 hypertension** hay không. Motivation là wearable/cuffless BP monitoring, khác biệt thiết bị/protocol và nhu cầu xử lý các đoạn ngắn khi recordings trong sinh hoạt có thể nhiễu hoặc bị motion artifacts. [H2020-E01]

Introduction gọi PPG chaotic theo các studies trước, và đề xuất NTSA/RQA để khảo sát dynamics. Đây là background/interpretation của authors, không chaos-identification experiment mới. Thí nghiệm thực tế dùng database; không có thử nghiệm smartwatch hoạt động liên tục hoặc predicted BP. [H2020-E01–E02, E08–E09]

### Experimental data

| Hạng mục | Thông tin xác lập từ PDF | Truy vết |
|---|---|---|
| Database | **PPG-BD**, short-recorded PPG for BP monitoring; ref[10] dataset, ref[11] descriptor | [H2020-E02, E09] |
| Source pool | **219 subjects**, age range **21–86** theo §2 | [H2020-E02] |
| Selected subset | BP groups; không có records diabetes, cerebral infarction, cerebrovascular disease; prose chọn subjects “over 45” | [H2020-E02] |
| Duration / sampling | **2.1 s/dataset, 1 kHz**; nominal **2,100 samples** là phép nhân của báo cáo, không sample count riêng được tác giả nêu | [H2020-E02] |
| Table 1 N | **49/73/31/20 datasets**, tổng **173** do báo cáo cộng | [H2020-E03] |
| Independent subjects / final N | Không xác lập record-per-person mapping, repeated-record dependence hoặc counts sau DET exclusion | [H2020-E02–E04, E09] |
| Quality screen | Bỏ series **DET < 0.9** do possible noise contamination; không báo số loại | [H2020-E04] |
| Sensor/site/wavelength | **Not established**; acquisition details được dẫn sang descriptor chưa audit ở đây | [H2020-E02, E09] |
| BP classification cutoffs | Không báo SBP/DBP thresholds hoặc adjudication details; giữ labels nguồn, không điền theo guidelines khác | [H2020-E02–E03, E09] |
| Preprocessing | Figure 1 là typical **unprocessed** signals; không xác lập toàn RQA pipeline dùng filters/detrending/normalization nào | [H2020-E03–E04, E09] |
| Age consistency / states | Prose “over 45”, bảng có minimum 45; không có Awake–Drowsy labels | [H2020-E02–E03, E09] |

**Table 1, p. 2 (trang in57).** N được gọi là datasets; average BP không phải classification threshold hoặc predicted BP. [H2020-E03]

| Nhóm | N datasets | Age range theo bảng | Average BP (mmHg) |
|---|---:|---|---|
| Normal | 49 | 45–75 | 110/64 |
| Prehypertension (preH) | 73 | 45–84 | 130/72 |
| Stage 1 hypertension (S1H) | 31 | 46–77 | 148/82 |
| Stage 2 hypertension (S2H) | 20 | 45–80 | 168/89 |

**Nhận xét phân tích:** không đổi 173 datasets thành 173 independent people. Table 1 không nói rõ N trước hay sau DET screen; khi dẫn sample size cần giữ uncertainty này. Age restriction giảm phạm vi tuổi, không chứng minh đã loại toàn bộ age confounding giữa nhóm. [H2020-E02–E04, E09]

### Methods and technical configuration

| Phương pháp áp dụng | Vai trò / cấu hình báo cáo | Giới hạn |
|---|---|---|
| **RP / reconstruction** | RP cho mỗi dataset, **m = 4**, dựa refs[4,5]; Figure 2 minh họa bốn nhóm | Không τ, norm, ε/rule, normalization, Theiler/identity-line settings hoặc FNN/AMI optimization mới. [H2020-E04, E09] |
| **MATLAB CRP toolbox / RQA** | Methods liệt kê RR, DET, L, Lmax, LAM, TT, Vmax; Table 2/results còn có **ENTR** | Không version/commands/lmin/vmin/line-length units; ENTR omitted trong method list nhưng có empirical results. [H2020-E04–E07] |
| **DET screening** | Loại series DET < 0.9 | Không independent quality ground truth/excluded counts; selected DET distribution không độc lập với screen. [H2020-E04, E09]; nhận xét phân tích |
| **One-factor ANOVA** | Test equal means của bốn nhóm; RR/DET non-significant, “other indexes” reject H0 theo authors | Không F,df,exact p hoặc assumption diagnostics; non-rejection không proof of equality. [H2020-E05, E09] |
| **Pairwise t-tests** | Các indices còn lại, level **0.05**; danh sách significant indices theo cặp | Không exact p,CI,effect sizes, Student/Welch details hay multiplicity correction được xác lập. [H2020-E07, E09] |
| **Qualitative inspection** | Figure 1/2 typical waveforms/RPs; authors không thấy obvious qualitative difference | Không blinded classification hoặc formal equivalence test. [H2020-E03–E04, E08] |

**Phân biệt thuật ngữ:** **RR là recurrence rate**, khác RR intervals trong HRV. L/Lmax là diagonal-line lengths, không Lyapunov exponent. LAM/TT/Vmax là vertical-line measures. Không quy đổi line lengths sang seconds khi source không đủ convention/implementation details. [H2020-E04–E06, E09]

### Principal empirical findings

**Table 2, p. 3 (trang in58): group means.** Không có SD,SE,CI hoặc distribution plots; rounded means không đủ để đánh giá uncertainty hoặc magnitude của group effect. [H2020-E06]

| Index | Normal | preH | S1H | S2H |
|---|---:|---:|---:|---:|
| RR | 0.15 | 0.15 | 0.15 | 0.16 |
| DET | 0.98 | 0.98 | 0.98 | 0.99 |
| L | 27.44 | 25.67 | 25.09 | 28.46 |
| Lmax | 1600.78 | 1684.16 | 1742.39 | 1799.00 |
| ENTR | 2.98 | 2.94 | 2.93 | 3.03 |
| LAM | 0.99 | 0.99 | 0.99 | 1.00 |
| TT | 32.28 | 31.19 | 30.72 | 34.05 |
| Vmax | 32.28 | 31.19 | 30.72 | 34.05 |

**TT/Vmax:** cả bốn means giống nhau trong bảng. Chưa xác lập đó là observed equality hay table error; không sửa Vmax bằng suy đoán và không coi hai indices cùng definition. [H2020-E06, E09]

**Pairwise results, p. 3:** source liệt kê các significant comparisons ở level 0.05 như sau. “Không được liệt kê” không tự xác lập exact p hoặc equivalence. RR/DET không có significant omnibus result nên không nằm trong danh sách pairwise. [H2020-E05, E07]

| Cặp nhóm | Indices được báo significant | Giới hạn |
|---|---|---|
| Normal vs preH | **L, Lmax, ENTR, LAM, TT, Vmax** | Không exact p/effect size |
| Normal vs S1H | **L, Lmax, TT** | ENTR/LAM/Vmax không được liệt kê |
| Normal vs S2H | **L, Lmax, ENTR, LAM, TT** | Vmax không được liệt kê |
| preH vs S1H | **L, Lmax, ENTR, LAM, TT** | Vmax không được liệt kê |
| preH vs S2H | **L, Lmax, ENTR, LAM, TT** | Vmax không được liệt kê |
| S1H vs S2H | **Không index nào** theo authors | Không evidence of significant differentiation |

| Finding | Evidence / support | Ranh giới |
|---|---|---|
| RR/DET non-significant | ANOVA p. 2, Discussion p. 3 | Không chứng minh equal dynamics; DET đã được screening. [H2020-E04–E05, E08] |
| L/Lmax/TT nổi bật | Có trong năm significant pairs; Conclusion chọn ba indices này | Group means, không subject-level classification accuracy. [H2020-E07–E08] |
| Trends không đồng nhất | L/TT giảm normal→preH→S1H rồi tăng S2H; Lmax means tăng qua bốn nhóm | Không mọi metric tăng monotonic theo severity. [H2020-E06] |
| ENTR/LAM tùy cặp | Có ở bốn trong năm significant pairs, không normal–S1H | Không phân biệt tất cả bốn classes. [H2020-E07] |
| Qualitative vs quantitative | Authors thấy typical waveforms/RPs không obvious difference, RQA có group differences | Typical examples, không formal visual test. [H2020-E03–E04, E08] |

### Interpretation and claims

**Authors’ conclusion:** RQA có potential cho hypertension-related PPG; Discussion nhấn mạnh L/Lmax/ENTR/LAM/TT, Conclusion chọn **L/Lmax/TT**. Bài nêu rõ RR/DET non-significant và **không phân biệt S1H/S2H**. [H2020-E01, E05–E08]

**Authors’ determinism claim:** Discussion nói đa số datasets deterministic dựa vào DET; Introduction gọi PPG chaotic theo references trước. Giữ đúng việc authors có claim đó, đồng thời tách khỏi kết quả trực tiếp. [H2020-E01, E04, E08]

**Nhận xét phân tích:** high DET sau khi loại DET < 0.9 không độc lập với selection. Diagonal recurrence organization không tự chứng minh deterministic generator hoặc chaos; bài không có surrogate null/LLE test mới. T-tests hỗ trợ group differences trong selected database, không diagnosis accuracy hoặc cuffless BP performance. [H2020-E04–E09]

### Limitations

| Loại | Giới hạn | Nguồn / hệ quả |
|---|---|---|
| Tác giả nêu | RR/DET non-significant; S1H/S2H không separated | pp. 2–3. [H2020-E05, E07–E08] |
| Tác giả nêu | Restrict age và loại một số comorbidities | §2 p. 1; không adjusted/matched confounding analysis. [H2020-E02] |
| Nhận xét phân tích | Thiếu RQA parameters, preprocessing và final N/dependence | Không direct numeric replication từ m = 4 alone. [H2020-E04, E09] |
| Nhận xét phân tích | Single duration, không longer reference/error/length sweep | Application 2.1 s không validate reliable estimation ở 2.1/60 s. [H2020-E02, E09] |
| Nhận xét phân tích | Screen bằng một RQA outcome statistic, chưa independent quality validation | High-DET distribution cần qualifier. [H2020-E04] |
| Nhận xét phân tích | Nhiều features/pairs; thiếu multiplicity, p-values, CI/effect sizes/diagnostics | Không claim adjusted statistical robustness. [H2020-E05, E07, E09] |
| Nhận xét phân tích | Không classifier, independent validation hoặc continuous BP prediction | Clinical monitoring là motivation/potential. [H2020-E01, E08–E09] |

**Bất nhất cần ghi nhận:** Methods liệt kê bảy indices nhưng ENTR có trong Table 2/results; TT/Vmax identical rows; prose “over 45” nhưng table có45; Figure 2 caption lặp panel(b) cho stage 2. Không suy ra fixed-RR target từ rounded RR≈0.15 hoặc cáo buộc Lmax inflated by identity line khi source thiếu ε/LOI settings. [H2020-E03–E04, E06–E09]

### Relevance to current manuscript

| Thành phần | Phân loại | Lý do / giới hạn | Nguồn |
|---|---|---|---|
| Waveform PPG RQA / DET,Lmean,LAM,TT | **Direct methodological relevance** | Thực sự dùng diagonal/vertical features; outcomes tùy feature/pair | [H2020-E02–E08] |
| Short-window application | **Direct precedent** | RQA trên 2.1 s; không universal accuracy cutoff | [H2020-E02–E04] |
| Duration reliability | **No direct validation** | Không length sweep/long reference | [H2020-E09] |
| RQ2: Awake–Drowsy | **Indirect conceptual relevance** | Group-associated recurrence là tiền lệ; BP categories khác sleepiness labels | [H2020-E02, E07–E09] |
| RQ1: PPS | **No direct relevance** | Không surrogate-data null; DET screen không PPS | [H2020-E04, E09] |
| Simplex/Rosenstein/DFA | **No direct algorithmic relevance** | Không thực hiện | [H2020-E09] |
| Diagnosis/BP estimation | **Motivation only** | Không performance evaluation | [H2020-E01, E08–E09] |

### Source evidence

| Mã / Paper ID | Trang PDF / vị trí | Evidence | Confidence |
|---|---|---|---|
| **H2020-E01 / H2020** | p. 1 metadata/Abstract/§1; p. 3§5 | Authors/title/event/date; monitoring/short-PPG motivation; background chaos; potential L/Lmax/TT | High |
| **H2020-E02 / H2020** | p. 1§2; p. 3 refs[10–12] | PPG-BD source 219 subjects 21–86;2.1 s/1 kHz; BP subset/comorbidity/age rules; details deferred to descriptor | High |
| **H2020-E03 / H2020** | p. 2 Table 1/Figure 1 | Group N/age/BP; typical unprocessed normal/S2H signals | High |
| **H2020-E04 / H2020** | p. 2§§3.1–3.2/Figure 2 | RP, m = 4, CRP toolbox/indices; DET < 0.9 exclusion; caption inconsistency | High |
| **H2020-E05 / H2020** | p. 2§3.2 closing; p. 3§4 | One-factor ANOVA; RR/DET non-significant, other indices reject H0 theo authors | High cho báo cáo |
| **H2020-E06 / H2020** | p. 3 Table 2 | Eight indices/group means, ENTR có trong bảng, identical TT/Vmax, thiếu dispersion | High |
| **H2020-E07 / H2020** | p. 3 Results/bullet list | Pairwise tests level 0.05; five significant-pair lists; none S1H/S2H | High |
| **H2020-E08 / H2020** | p. 3§§4–5 | Qualitative comparison, interpretation/group findings, determinism claim và potential application | High cho claims; Medium cho mechanism interpretation |
| **H2020-E09 / H2020** | Toàn PDF pp. 1–3 | Không full settings/final counts/mapping/p-adjustment/classifier/length sweep/PPS/Simplex/LLE/DFA/state comparison; inconsistencies đã đối chiếu | High cho scope/bất nhất; Medium cho thông tin thiếu |

## 4. Cross-Paper Comparison

| Dimension | Munoz 2015 | Hypertension RQA 2020 | Hàm ý |
|---|---|---|---|
| Question | Agreement short–reference HRV | Differences between BP groups | Hai validation targets khác nhau. [M2015-E01; H2020-E01] |
| Representation | Pressure-derived NN intervals | Waveform PPG | Không transfer duration thresholds trực tiếp. [M2015-E03; H2020-E02] |
| Sample | 3,387 people | Table 1 sum 173 datasets; independence/final N chưa rõ | Không pooled cohort. [M2015-E02; H2020-E03–E04] |
| Duration design | 10 s×3/Avg10s/30/120 vs 240–300 s | Một duration 2.1 s/1 kHz | Length validation khác single-duration application. [M2015-E03; H2020-E02] |
| Quality | Visual processing/interpolation; >5% exclusion | DET < 0.9 exclusion | Không cùng artifact protocol. [M2015-E03; H2020-E04] |
| Methods | SDNN/RMSSD, r/LOA/d/ICC/bootstrap | RP/RQA, ANOVA/t-tests | Không cùng NTSA toolkit. [M2015-E04, E08; H2020-E04–E07] |
| Reconstruction | Không embedding | m = 4; τ/ε chưa rõ | Không cấu hình transferable chung. [M2015-E12; H2020-E04] |
| Diagonal/vertical recurrence | Không RQA | DET,L,Lmax,ENTR/LAM,TT,Vmax | H2020 là direct precedent cho vertical features. [H2020-E04–E07] |
| Nulls | Part–whole agreement bootstrap | Equal group means | Không PPS dynamics null. [M2015-E08; H2020-E05–E07] |
| State/outcome | Resting, không outcome experiment | BP groups, không classifier/BP prediction | Không Awake–Drowsy hoặc clinical performance validation. [M2015-E12; H2020-E09] |

## 5. Critical Scientific Synthesis

### A. Điều gì được xác lập trong phạm vi dữ liệu?

Munoz cho thấy recording length tác động khác nhau lên SDNN/RMSSD và r-only assessment có thể bỏ qua bias; authors kiểm tra overlap bằng simulation. H2020 cho empirical precedent rằng diagonal/vertical recurrence features trên 2.1-s PPG có thể khác giữa một số BP groups, dù typical waveform/RP inspection chưa cho obvious difference. [M2015-E05–E11; H2020-E03–E08]

**Nhận xét phân tích:** strength của Munoz là sample lớn và duration/agreement design; strength của H2020 là tính trực tiếp về waveform PPG và RQA group comparison. Evidence bổ sung nhau, không chứng minh một common reliability threshold.

### B. Conditional claims và inferential boundaries

| Claim | Evidence thực sự | Boundary |
|---|---|---|
| 10-s RMSSD valid | Authors’ inference trong processed resting intervals | Không mọi sensor/state/artifact/outcome. [M2015-E03, E07, E11–E12] |
| 30-s SDNN sufficient | Authors recommend; d = 0.516, moderate agreement | Không perfect/zero-bias guarantee. [M2015-E07, E11] |
| RQA discriminates hypertension | Significant group means cho một số pairs | Không four-class diagnostic accuracy. [H2020-E07–E09] |
| DET proves determinism | Authors’ interpretation sau DET screen | Không independent generator/chaos proof. [H2020-E04, E08] |
| 2.1 s validates reliable RQA | Thực sự có application trên độ dài đó | Không long-reference/length error test. [H2020-E02, E09] |
| These papers validate PPG 60 s | Không có design đó | Dataset-specific evidence cần riêng. [M2015-E12; H2020-E09] |

### C. Bài học manuscript có thể kế thừa

**Nhận xét phân tích:** phân biệt khả năng tính metric, agreement với reference, association với state và rejection của dynamics null. Chọn checks theo claim thực tế; LOA không tự trả lời state comparison và t-tests không tự trả lời interchangeability. Quality/duration cần theo feature/representation; không dùng interval thresholds cho waveform estimators. [M2015-E03–E11; H2020-E04–E09]

Subject/record dependence, selection, effect sizes/uncertainty, multiplicity và reconstruction/recurrence parameters cần report rõ. High DET sau screen không là quality/physical determinism evidence độc lập. [H2020-E02–E09; nhận xét phân tích]

### D. Phạm vi các comparisons và khoảng trống

H2020 **đã** so nhiều diagonal/vertical recurrence descriptors giữa clinical BP groups; không viết literature chưa có group-related PPG dynamics hoặc LAM/TT. Tuy nhiên, hai bài không so combined **forecastability, recurrence organization và local divergence giữa Awake/Drowsy**, không PPS test trên những windows đó và không DFA waveform analysis. Resting HRV/BP categories không phải sleepiness labels hoặc within-person temporal transition. [M2015-E12; H2020-E04–E09]

## 6. Defensible Research Gap

**Gap được hỗ trợ trong hai nguồn — nhận xét phân tích:** trước đó đã có duration-dependent validity của interval HRV và RQA group differences của very-short PPG, nhưng hai studies chưa trực tiếp characterise complementary waveform dynamics giữa Awake/Drowsy hoặc organization beyond một specified PPS noisy pseudoperiodic null. Nguồn này motivate empirical extension cùng duration/quality checks, không dự đoán findings hoặc prescribe 60 s cho mọi metric. [M2015-E03–E12; H2020-E02–E09]

**Gap cần broader verification:** “first”, “never studied” hoặc “no previous studies worldwide” về short nonlinear PPG, drowsiness, PPS hoặc combined descriptors. Hai articles 2015/2020 không cung cấp universal novelty verdict hoặc tình trạng literature hiện tại. Audit này chỉ đọc hai PDF được cung cấp.

## 7. Introduction-Ready Evidence Table

| Vai trò | Statement được hỗ trợ | Evidence location | Classification / qualification |
|---|---|---|---|
| Short-record motivation | Routine short recordings có cơ hội phenotyping nhưng cần validity | M2015 pp. 1–3 | **Direct support** cho interval HRV rationale. [M2015-E01–E03] |
| Duration dependence | SDNN/RMSSD agreement khác theo feature/length, RMSSD tốt hơn trong setting này | M2015 Tables 3–5/Discussion | **Direct support**, không all-NTSA guarantee. [M2015-E05–E11] |
| Agreement caution | r không tự nhận diện bias; authors có LOA/d/simulation | M2015 pp. 3–6,9,13 | **Direct support**; không nói họ bỏ qua agreement/dependence. [M2015-E04, E07–E11] |
| Short-PPG precedent | RQA áp dụng trên 2.1-s PPG với diagonal/vertical indices | H2020 §§2–3/Tables 1–2 | **Direct support**, không length-validation claim. [H2020-E02–E06] |
| Clinical-group RQA | L/Lmax/TT khác ở năm pairs; S1H/S2H không separated | H2020 p. 3 | **Direct support**, level 0.05/unknown multiplicity, không diagnosis. [H2020-E07–E09] |
| Method synthesis | Short-window claims cần checks theo feature, representation và inferential target | Methods/results cả hai | **Partial support**: analytical synthesis, không verbatim conclusion. [M2015-E04–E11; H2020-E04–E09] |
| Limited-source gap | Chưa direct combined descriptors across Awake/Drowsy | Scope cả hai | **Direct support** cho limited absence; không universal novelty. [M2015-E12; H2020-E09] |
| RQ1: PPS | Không PPS finding trong hai nguồn | M2015 simulation/H2020 scope | **Context only**; cần primary PPS source riêng. [M2015-E08, E12; H2020-E09] |
| RQ2 motivation | Clinical-group recurrence precedent motivate state-associated dynamics | H2020 p. 3 | **Partial support**, không expected direction/effect size cho drowsiness. [H2020-E07–E09] |
| Universal first claim | “This is the first study worldwide…” | Không supporting location | **Unsupported** từ corpus này |

**Editorial recommendation — nhận xét phân tích:** Introduction nên nêu contributions và giới hạn. Exact LOA/CI, segment selection, bootstrap overlap-null, DET screen, ε/τ/Theiler/lmin/vmin, dependence/multiplicity và table inconsistencies phù hợp Methods/Discussion hơn.

## 8. Statements to Avoid or Qualify

| Tránh hoặc qualify | Vì sao | Hướng sửa |
|---|---|---|
| “Munoz directly recorded ECG/PPG waveforms” | Portapres pressure-derived intervals. [M2015-E03] | Ghi modality và ECG motivation riêng |
| “Munoz validated60-s nonlinear PPG” | Không60-s arm/nonlinear metrics. [M2015-E03, E12] | Feature-specific interval HRV validity |
| “120-s SDNN bias 0.064 ms, LOA−0.059–0.069 ms” | Log scale; prose LOA inconsistent. [M2015-E07, E13] | Table 4 LOA−0.222–0.349, ghi scale |
| “Avg10s equals continuous30-s series” | Average estimates từ ba segments. [M2015-E03] | Không concatenate intervals |
| “Averaging removes SDNN bias” | Avg10s bias 0.406/d 0.874. [M2015-E07] | Spread/r cải thiện, bias còn |
| “All simulation measures exceed null” | Bias/d không khác expectation. [M2015-E09] | Chỉ r/LOA như authors báo |
| “Bootstrap gives PPS evidence” | Overlap-null khác dynamics-null. [M2015-E08] | Tách hai hypotheses |
| “2.1 s proves reliable RQA” | Single duration, không reference/error test. [H2020-E02, E09] | Application precedent |
| “173 independent participants” | Table N datasets; mapping/final N thiếu. [H2020-E03–E04, E09] | Report 49/73/31/20 datasets và sum 173 |
| “RQA distinguishes all four stages accurately” | S1H/S2H non-significant; không classifier. [H2020-E07–E09] | Specific group differences/potential utility |
| “DET≈0.98 proves chaos” | DET screen; không chaos null/LLE. [H2020-E04, E08–E09] | Recurrence statistic và authors’ interpretation |
| “RR≈0.15 proves fixed-RR threshold” | ε rule không reported. [H2020-E04, E09] | Không infer settings từ rounded means |
| “TT=Vmax by definition” | Identical table rows chưa giải thích. [H2020-E06, E09] | Giữ distinct definitions/flag inconsistency |
| “All metrics increase monotonically with BP” | L/TT non-monotonic. [H2020-E06] | Metric/group-dependent trends |
| “No previous PPG LAM/TT or short RQA” | H2020 có cả hai. [H2020-E02–E07] | Gap ở states/combined questions |
| “These papers validate every feature on 60 s” | Không supported design. [M2015-E12; H2020-E09] | Evidence của dataset/metrics hiện tại riêng |
| “This is universally first” | Two-source audit không systematic search | Limited-source absence hoặc broader verification |

## 9. Outstanding Questions and Verification Needs

| Câu hỏi | Source/status | Ý nghĩa |
|---|---|---|
| Exact Munoz min–max age/120-s prose LOA/d CI error? | Bất nhất chưa resolve. [M2015-E02, E07, E13] | Không silent correction hoặc precision claim |
| Munoz use-case acceptance margin/cross-sensor transfer? | **Not established** trực tiếp. [M2015-E03–E04, E13] | Không universal interchangeability |
| Sampling/filter/interpolation details đủ replication? | Không đầy đủ trong PDF; refs được dẫn. [M2015-E03, E12] | Cần primary methods/code nếu replicate |
| H2020 N trước/sau screen và record-person mapping? | **Not established.** [H2020-E02–E04, E09] | Independent-unit inference cần xác minh |
| H2020 BP cutoffs/sensor/site/wavelength/preprocessing? | **Not established** trong PDF này. [H2020-E02, E09] | Descriptor cited chưa audit, không điền bằng memory |
| RQA τ/ε/norm/Theiler/LOI/lmin/vmin/version? | **Not established.** [H2020-E04, E09] | Không direct numerical replication |
| ENTR omitted methods/identical TT,Vmax? | **Unresolved.** [H2020-E04, E06–E09] | Không invent corrected values/settings |
| Exact p/ANOVA diagnostics/t-test variant/multiplicity/effects? | **Not established.** [H2020-E05, E07, E09] | Không adjusted-robustness claim |
| Chosen waveform metrics reliable ở 60-s Awake/Drowsy? | Không established trong hai sources | Cần dataset-specific evidence |

**Verification ngoài phạm vi sources — nhận xét phân tích:**

1. Broader novelty search trước “first/no prior studies”.
2. Duration/reconstruction/quality checks cho từng chosen estimator trên representation của manuscript, không dùng SDNN/RMSSD cutoff cho cả toolkit.
3. PPS generator/null diagnostics riêng; part–whole bootstrap và DET screen không kiểm tra null đó.
4. State/group design: labels, independent unit/repeated windows, effect sizes/uncertainty và multiplicity; empirical association không tự diagnosis/mechanism.
5. Dataset descriptor/primary code nếu muốn replicate H2020 hoặc giải quyết missing settings/bất nhất. Những nguồn được hai PDF cite chưa được audit sâu ở đây.

Các mục này là recommendations, không analyses đã thực hiện hoặc bằng chứng manuscript đã đạt robustness đó.

## 10. Recommended Paragraph 2 Narrative Structure

Đây là **logical sequence**, không polished English prose hoặc final Introduction paragraph.

1. Nối physiological observation sang câu hỏi temporal/dynamical organization; tránh universal chaos premise. [H2020-E01–E04]
2. Dùng Munoz như tiền lệ **interval HRV** cho duration/bias/agreement khác theo feature; không direct waveform validation. [M2015-E03–E11]
3. Nêu **2.1-s PPG RQA** với diagonal/vertical features và BP-group findings; qualify S1H/S2H non-separation. [H2020-E02–E08]
4. Synthesis: tính được feature, agreement với reference, group/state association và null rejection là các claims khác nhau; cần assumptions/checks tương ứng. [M2015-E04–E11; H2020-E04–E09]
5. Nêu gap có scope: combined forecastability/recurrence/local divergence giữa Awake/Drowsy và PPS-tested organization chưa được hai studies trả lời; không phủ nhận previous short RQA/LAM/TT. [M2015-E12; H2020-E04–E09]
6. Nối RQ1/RQ2 theo manuscript context; cite primary algorithm/null sources riêng. Hai bài không dự đoán outcome của RQ hoặc validate toàn bộ metrics ở 60 s. [M2015-E08, E12; H2020-E09]

**Trọng tâm — nhận xét phân tích:** empirical characterization với assumptions và inferential boundaries rõ. Không cần claim invented algorithms, proven chaos hoặc validated diagnosis để có scientific rationale.
