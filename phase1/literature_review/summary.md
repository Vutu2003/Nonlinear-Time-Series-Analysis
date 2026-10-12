# Evidence Audit: Three Sviridova PPG Studies

> Báo cáo phục vụ literature review cho manuscript *Ultra-Short PPG Dynamics Across the Wakefulness-to-Drowsiness Transition: A Nonlinear Time-Series Analysis*. Phân tích dựa trực tiếp trên ba PDF được cung cấp; không dùng các bản tóm tắt có sẵn để thay thế bài gốc. Tên tệp `summary.md` theo yêu cầu trực tiếp của người dùng, thay cho tên trong mẫu nhiệm vụ. Không viết đoạn Introduction hoàn chỉnh.

**Quy ước truy vết.** Mọi số trang dưới đây là **trang PDF, đếm từ 1**, không phải số trang in của tạp chí. Với bài 2015, trang in = trang PDF + 52; với bài 2018, trang in = trang PDF + 156; bài 2022 đánh số trang bài từ 1 đến 14. Mã như **[2015-E03]** trỏ tới bảng `Source evidence` của chính bài đó, nơi ghi Paper ID, trang, section, figure/table, diễn giải bằng chứng và confidence. Một mã có thể hỗ trợ nhiều diễn giải cùng nguồn. Confidence đánh giá độ chắc chắn của việc trích xuất hoặc nhận diện phát biểu trong PDF, **không** chứng nhận tính đúng đắn tuyệt đối của kết luận sinh lý/chaos của tác giả.

- **High:** văn bản, công thức, bảng hoặc caption nêu rõ.
- **Medium:** cần đọc kết hợp hình và Discussion, hoặc phạm vi kết quả không được báo cáo đầy đủ.
- **Low:** chứng cứ thiếu hoặc bất nhất; không dùng làm khẳng định chắc chắn.
- **Not established from the provided source:** chi tiết không được xác lập trong PDF; không điền bằng suy đoán hoặc kiến thức từ nguồn khác.
- Các đoạn ghi **Nhận xét phân tích** là đánh giá của báo cáo này, không phải hạn chế do tác giả tự tuyên bố. Đánh giá relevance/gap cũng thuộc loại này và chỉ dùng bối cảnh manuscript do người dùng cung cấp.

| Paper ID | PDF gốc | Số trang |
|---|---|---:|
| 2015 | [1-s2.0-S0960077915001344-main.pdf](paper/1-s2.0-S0960077915001344-main.pdf) | 11 |
| 2018 | [1-s2.0-S0960077918309810-main.pdf](paper/1-s2.0-S0960077918309810-main.pdf) | 9 |
| 2022 | [sensors-22-05154-v2.pdf](paper/sensors-22-05154-v2.pdf) | 14 |

## 1. Executive Scientific Summary

Ba nghiên cứu cung cấp ba loại đóng góp bổ sung nhau: kiểm tra nhiều đặc tính động lực của PPG lúc nghỉ; so sánh PPG theo điều kiện đo quang học và xem xét nguồn hình thành độ phức tạp; đánh giá độ phụ thuộc chiều dài bản ghi của các chỉ số RQA. Không nên mô tả chúng là ba lần áp dụng cùng một bộ thuật toán. [2015-E01, E03–E11; 2018-E01, E03–E10; 2022-E01, E03–E09]

1. **2015:** ở chín người trẻ khỏe mạnh, PPG có cấu trúc quỹ đạo tái dựng, LLE theo **Wolf** dương, short-term predictability, Wayland translation error nhỏ và kết quả prediction phân biệt với Fourier-phase-randomized surrogates. Tác giả kết luận dynamics phù hợp định nghĩa chaotic motion họ sử dụng, đồng thời so sánh định tính với noisy Rössler single-band chaos. Bài không thực hiện PPS, Rosenstein LLE hoặc RQA. [2015-E02–E11]
2. **2018:** nghiên cứu green PPG (**gPPG**, 530 nm) và NIR PPG (**rPPG**, 900 nm; ký hiệu rPPG trong bài không có nghĩa dữ liệu thực nghiệm red 660 nm). Bài dùng FNN, Wayland test, DNP, hai surrogate nulls gồm **PPS**, LLE theo **Rosenstein**, và 0–1 test. Prediction của gPPG phân biệt với cả hai loại surrogate; tác giả kết luận cả gPPG và rPPG chaotic và đề xuất đóng góp từ lớp da nông. Nguồn cơ chế sâu hơn vẫn chưa được phân giải trực tiếp. [2018-E02–E11]
3. **2022:** bài đánh giá **DET, Lmax, L và ENTR**, không thực hiện Simplex hay LLE estimation. Sai số được tính so với chỉ số của chuỗi dài tham chiếu. DET và ENTR ổn định trên chuỗi ngắn hơn nhiều so với L và Lmax trong dữ liệu NIR tham chiếu. Table 3 cho ngưỡng trung bình để sai số dưới 1% ở 409.6 Hz: DET 3.05 cycles, ENTR 21.34 cycles, L 131.10 cycles, Lmax 149.39 cycles. Theo quy ước 0.8 s/cycle của bài, tương ứng khoảng 2.44, 17.07, 104.88 và 119.51 s; đây là **quy đổi của báo cáo**, không phải tất cả các số giây nguyên văn trong Discussion. [2022-E02, E06–E10]

**Hàm ý cho manuscript hiện tại — nhận xét phân tích:** bài 2018 là tiền lệ trực tiếp cho prediction kết hợp PPS và Rosenstein trajectory divergence; bài 2022 là tiền lệ trực tiếp cho kiểm tra recording-length sensitivity của RQA. Ba bài không trực tiếp so sánh Awake–Drowsy, cũng không đồng thời khảo sát Simplex forecastability, DET/Lmean/LAM/TT và Rosenstein divergence giữa hai trạng thái này. Khoảng trống có thể nêu là khoảng trống **trong ba nghiên cứu này**, còn tuyên bố đầu tiên trên toàn literature cần kiểm chứng rộng hơn. [2015-E02, E12; 2018-E02, E12; 2022-E02, E11]

**Ranh giới suy luận:** các bài 2015/2018 thực sự dùng ngôn ngữ kết luận chaos; báo cáo không được làm nhẹ hoặc che giấu điều đó. Tuy nhiên, khi xây Introduction của manuscript hiện tại, nên dẫn các đặc tính được quan sát và việc tác giả đã diễn giải chúng là compatible with chaos, thay vì chuyển chúng thành một tiền đề rằng mọi PPG đều là deterministic chaos. PPS rejection bác bỏ null được kiểm tra; positive estimated LLE và RQA DET không tự mình chứng minh deterministic chaos. Đây là đánh giá phương pháp của báo cáo, dựa trên phạm vi kiểm định và các cảnh báo về noise của chính nguồn. [2015-E04, E09–E11; 2018-E06–E10; 2022-E05, E10–E11]

## 2. Sviridova & Sakai (2015)

**Thông tin thư mục.** Nina Sviridova và Kenshi Sakai. *Human photoplethysmogram: new insight into chaotic characteristics*. **Chaos, Solitons & Fractals**, 77 (2015), 53–63. DOI: [10.1016/j.chaos.2015.05.005](https://doi.org/10.1016/j.chaos.2015.05.005). Mục tiêu: kiểm tra dynamics của finger PPG ở người trẻ khỏe mạnh có phù hợp định nghĩa chaotic motion được chọn hay không và mô tả các đặc tính đó bằng nhiều công cụ NTSA. [2015-E01, E11]

### Research question and motivation

Các tác giả đặt vấn đề rằng kết luận PPG chaotic trong nghiên cứu trước chủ yếu dựa vào reconstructed trajectory, correlation dimension và Lyapunov exponent, trong khi các công cụ này có thể nhạy với noise và tạo dấu hiệu giống chaos ở hệ không chaotic. Vì vậy họ muốn phối hợp các phép phân tích kiểm tra nhiều khía cạnh của dynamics, thay vì dựa vào một chỉ số. [2015-E01, E04, E11]

PPG được xem như một tín hiệu quan sát của hệ tim mạch và vi tuần hoàn da có nhiều quá trình tương tác. Introduction phân biệt thành phần pulsatile gắn với nhịp tim và baseline biến đổi chậm liên quan đến respiration, sympathetic activity và thermoregulation. Những mô tả sinh lý này là background được bài trích từ literature, **không phải các quá trình được đo độc lập trong thí nghiệm của bài**. [2015-E01]

Mục tiêu không chỉ là phát hiện nonlinearity: bài chủ động kiểm tra các đặc tính phục vụ diễn giải chaotic motion gồm orbital instability, determinism/predictability và recurrence of motion theo time-delay geometry/Poincaré section. Bài còn so sánh PPG với Rössler single-band chaos. Định nghĩa broad/“positive” của Thompson được dùng làm khung kết luận; vì vậy cần nêu rõ phạm vi định nghĩa khi thuật lại claim chaos. [2015-E03–E11]

### Experimental data

| Hạng mục | Thông tin xác lập từ PDF | Truy vết |
|---|---|---|
| Người tham gia | 9 volunteers, tuổi 19–27, sinh viên TUAT; khỏe mạnh, không hút thuốc, hoạt động thể lực mức tương tự, không dùng thuốc, không khai tiền sử bệnh tim | [2015-E02] |
| Số lần ghi | 5 measurement repeats/người; suy ra 45 bản ghi theo protocol, không phải 45 người độc lập | [2015-E02]; phép nhân của báo cáo |
| Thời lượng | 5 min/bản ghi | [2015-E02] |
| Sampling | Bước lấy mẫu 5 ms, tương đương **200 Hz**; WTE sử dụng chuỗi 60,000 điểm | [2015-E02, E08]; 200 Hz là quy đổi |
| Vị trí | Ngón trỏ phải | [2015-E02] |
| Thiết bị/quang học | BACS (Computer convenience, Inc.) transmission-mode PPG sensor; nguồn NIR | [2015-E02] |
| Bước sóng chính xác | **Not established from the provided source.** Khoảng NIR nêu ở §2.1 là mô tả công nghệ, không xác lập LED thực nghiệm có một wavelength cụ thể | [2015-E01–E02] |
| Điều kiện | Ngồi thư giãn; phòng có kiểm soát temperature, noise, vibration; nghỉ 5 min trước đo; vị trí đo để hở; kiểm tra huyết áp trước mỗi lần ghi | [2015-E02] |
| Trạng thái sinh lý | Healthy resting condition; không có nhãn Awake–Drowsy hoặc sleep-stage comparison | [2015-E02, E12] |
| Preprocessing/filter | Tần số cắt, filter order, normalization, detrending và quy tắc loại artifact: **Not established from the provided source** | [2015-E12] |
| Điều kiện chất lượng | Thiết kế môi trường nhằm hạn chế tác động bên ngoài; tác giả vẫn thừa nhận physiological data có environmental noise/movement artifacts | [2015-E02, E11] |

**Lưu ý dữ liệu:** §2.2 ban đầu mô tả ánh sáng phản xạ nhưng cùng section xác định sensor transmission-mode. Ghi nhận cả hai chi tiết; không tự sửa nguồn thành thiết bị reflectance. Điều xác lập rõ nhất về thiết bị là tên BACS và mô tả transmission-mode. [2015-E02; confidence Medium cho tính nhất quán của mô tả quang học]

### Methods and technical configuration

| Phương pháp thực sự áp dụng | Thuộc tính/vai trò và lý do chọn | Cấu hình báo cáo | Quan hệ với các phương pháp khác; giới hạn |
|---|---|---|---|
| **Fourier spectral analysis** | Nhận diện predominant frequency (PF) và low-frequency components; đặt nền cho delay selection | PF theo từng subject/repeat, Table 1; delay sau đó bằng quarter-period của PF | Cấu trúc phổ không chứng minh chaos; diễn giải các thành phần LF về sinh lý không được kiểm chứng bằng đo respiration riêng. [2015-E03] |
| **Time-delay embedding** | Khảo sát geometry của possible dynamics và cấu trúc quỹ đạo | **m = 4**, chọn theo nghiên cứu trước; **τ = 1/(4 PF)** về thời gian; hình 4 dùng màu thể hiện tọa độ thứ tư | Không có FNN/AMI sweep mới được báo cáo trong bài này. Delay cần cân bằng dependence và independence. Dùng cho geometry và các NTSA phía sau. [2015-E04] |
| **Largest Lyapunov exponent — Wolf’s method** | Ước lượng divergence giữa nearby trajectories; kiểm tra orbital instability | Table 2 cho toàn bộ subject × repeats | Không phải Rosenstein. PDF cảnh báo LLE có thể dương ở hệ không chaotic và có thể bị overestimate; neighbor replacement/fit settings không được báo cáo đủ để tái lập. [2015-E04] |
| **Deterministic nonlinear prediction (DNP)** | Kiểm tra short-term predictability và biến đổi chất lượng theo forecast horizon | Dùng **CC** và **RRMSE**; Figure 6: forecast 160 steps = 0.8 s; Figure 5 có đường theo prediction steps | PDF không xác lập thuật toán này là **Simplex Projection**, không cho đủ library/test split, số neighbors, weights, Theiler exclusion, hoặc công thức chuẩn hóa RRMSE. Không đồng nhất RRMSE với Mean NRMSE của manuscript. [2015-E05–E06, E12] |
| **Numerical Rössler/Lorenz comparison** | Đặt các prediction curves của PPG trong tương quan với hai hệ chaotic có biểu hiện dự báo khác nhau | Rössler **a = 0.398, b = 2, c = 4**; Lorenz **σ = 10, ρ = 28, β = 8/3**; RK4, step **0.01**; Rössler với **7%** additive noise trong Figures 5/10 | Đây là benchmarks mô phỏng, không phải fitted physiological model. Bài dùng cả additive và dynamical terminology; cách tạo noise cụ thể và chuẩn hóa phần trăm chưa được xác lập đầy đủ. Không suy ra PPG có 7% noise. [2015-E05, E10] |
| **Poincaré section** | Khảo sát qualitative geometry của vòng quỹ đạo, stretching/bending/folding | Cắt **3D** time-delay reconstructed attractor bằng mặt phẳng **2D** quay clockwise; Figures 7–8 có các góc α | Khác với Figure 4 hiển thị reconstruction 4D. Không phải RP/RQA; “recurrence of motion” ở đây không có nghĩa họ tính DET/LAM/TT. [2015-E07] |
| **Wayland test / Wayland translation error (WTE)** | Đánh giá local flow continuity/smoothness; tác giả dùng như chỉ báo determinism với noise tolerance | PPG chuỗi **60,000 points**; Table 3 cho 45 giá trị; benchmarks Rössler, Rössler +10% noise và white noise | Số nearest neighbors, image time step và cách tổng hợp local errors không nêu đủ. WTE nhỏ là kết quả của phép đánh giá này, không tự loại trừ tất cả stochastic processes. [2015-E08] |
| **Fourier-phase-randomized surrogate data + DNP** | Kiểm tra null: dữ liệu là realization của **linear Gaussian stochastic process**; preserve power spectrum | **30** surrogate datasets; phase randomization Fourier transform rồi inverse transform; CC curves, Figure 9 | Discriminating quantity là DNP CC. Không có PPS trong phần thí nghiệm, dù tài liệu PPS được trích trong references. Không báo cáo formal p-value/rank rule/α hoặc điều chỉnh nhiều horizons. [2015-E09, E12] |
| **Direct trajectory tracing** | Minh họa divergence rồi bounded return/continuous bending | Chọn arbitrary point và nearest neighbor; minh họa 140- và 300-step segments; Figure 10 đối chiếu PPG với Rössler +7% noise | Qualitative visualization hỗ trợ interpretation topology; không phải kiểm định statistical equivalence với Rössler. [2015-E10] |

**Phân biệt background với application:** correlation dimension (CD) được nhắc để giải thích những nghiên cứu trước và giới hạn chaos detection; bài không báo cáo một phân tích CD mới cho dataset này. Kaplan–Glass được nhắc như họ phương pháp liên quan đến Wayland; không có kết quả Kaplan–Glass riêng. PPS xuất hiện trong reference list, nhưng §3.7 chỉ thực hiện Fourier phase randomization. Không có RQA, LAM, TT, AMI hoặc kiểm định state differences trong kết quả. [2015-E01, E08–E09, E12]

### Principal empirical findings

| Kết quả trực tiếp | Điều kiện, số liệu/hướng biến đổi | Figure/table và statistical support | Ranh giới bằng chứng |
|---|---|---|---|
| Predominant frequency | PF **1.02–1.52 Hz** trên các bản ghi | PDF p.4, §3.1, Figure 3/Table 1; descriptive | Phù hợp nhịp tim bình thường theo tác giả; không phải dấu hiệu riêng của chaos. [2015-E03] |
| Reconstructed geometry | Quỹ đạo có cấu trúc “screwing”, tác giả ví với Möbius band | PDF p.5, §3.2, Figure 4, ví dụ subject 1/repeat 1 | Nhận diện qualitative geometry, không tính invariant topological equivalence. [2015-E04] |
| Positive LLE | Toàn bộ Table 2 dương; **0.731–1.692** là min–max đọc từ 45 entries | PDF p.5, §3.3, Table 2; không có CI/p-value | Khoảng là tổng hợp của báo cáo; đơn vị trong table không được xác lập rõ, không tự gắn s⁻¹. [2015-E04] |
| Finite-horizon prediction | CC nói chung giảm, RRMSE tăng theo horizon; Figure 6 cho 0.8 s forecast vẫn tái hiện waveform và dicrotic notch | PDF pp.6–7, §3.4, Figures 5–6; typical examples | Không có population mean CC/NRMSE hay statistics giữa trạng thái. Không đọc số CC cụ thể từ đồ thị rồi coi là số bảng. [2015-E05–E06] |
| Prediction benchmark pattern | PPG có xu hướng prediction giống noisy Rössler hơn kiểu decay nhanh của Lorenz; noiseless Rössler có **CC > 0.96**, **RRMSE < 0.28** trên khoảng dài trong ví dụ | PDF pp.6–7, §3.4, Figure 5 | Các ngưỡng >0.96/<0.28 là của **Rössler**, không phải giá trị PPG. Similar trends là qualitative comparison. [2015-E05–E06] |
| Poincaré geometry | Các lát cắt thể hiện expansion, bending, stretching, fold-back tại các α khác nhau | PDF pp.7–9, §3.5, Figures 7–8 | “Stretch-and-fold generates sensitivity” là interpretation; không phải sensitivity test độc lập trong hình. [2015-E07] |
| WTE nhỏ | Table 3: **0.005–0.092**, min–max tổng hợp của báo cáo; benchmarks: Rössler **0.0002**, Rössler +10% noise **0.0045**, white noise **1.08** | PDF p.9, §3.6, Table 3; descriptive | Các benchmark dùng 60,000 points. WTE không trực tiếp đo noise fraction. [2015-E08] |
| Original khác phase surrogates | Original CC curve được tác giả mô tả tách khỏi các curves của 30 surrogate datasets | PDF pp.9–10, §3.7, Figure 9 | Tác giả bác bỏ linear Gaussian null; không báo cáo exact p-value hoặc tỷ lệ reject trên toàn 45 recordings. [2015-E09] |
| Bounded trajectory behavior | Nearby trajectories ban đầu tách xa, sau đó gần lại trong vùng bounded; bending liên tục | PDF p.10, §4, Figure 10 | Minh họa selected segments, không phải full attractor proof. [2015-E10] |

### Interpretation and claims

**Tác giả thực sự kết luận gì?** Discussion và Conclusion khẳng định dữ liệu phù hợp chaotic motion theo định nghĩa đã chọn, nêu determinism, short-term predictability, sensitivity và topology/prediction similarity với noise-induced Rössler single-band chaos. Vì vậy không được viết rằng bài này chỉ mô tả nonlinearity và không đưa ra chaos claim. [2015-E11]

**Điều nguồn trực tiếp hỗ trợ mạnh:** các bản ghi thực nghiệm có short-term forecasting, positive Wolf estimates, WTE nhỏ và prediction khác với surrogate ensemble dưới linear Gaussian null. Đây là những kết quả có thể trích độc lập với sự đồng thuận về claim chaos. [2015-E04–E09]

**Nhận xét phân tích:** bằng chứng hội tụ từ nhiều công cụ giúp khảo sát nhiều mặt của dynamics, nhưng không biến null rejection thành bằng chứng loại trừ mọi stochastic explanation. Đặc biệt, phase randomization bảo toàn power spectrum dưới null đã chọn; nó không kiểm tra riêng noisy periodic orbit như PPS. Positive LLE cũng được chính §3.3 cảnh báo là có thể xuất hiện ngoài chaos. [2015-E04, E09]

**Hai cách diễn giải cần thận trọng:**

- Tác giả cho rằng sự phân biệt prediction với surrogates gợi ý Gaussian noise không có ảnh hưởng đáng kể lên DNP. **Nhận xét phân tích:** surrogate discrimination không định lượng riêng tác động noise contamination lên estimator; câu này nên được ghi là diễn giải của tác giả, không chuyển thành “DNP đã được chứng minh noise-proof”. [2015-E09, E11]
- Tác giả suy luận không có long-term prediction bằng so sánh với Rössler và lý giải high CC ở Rössler không bảo đảm long-term prediction. **Nhận xét phân tích:** bằng chứng hữu hạn ở horizons đã khảo sát không xác lập một mathematical forecast horizon phổ quát cho PPG. [2015-E06, E11]

### Limitations

**Hạn chế/cảnh báo tác giả nêu rõ:**

1. Các classical chaos tests, nhất là CD/LLE, noise-sensitive và có thể cho kết luận sai; LLE có thể bị overestimate hoặc dương ở non-chaotic systems. [2015-E01, E04, E11]
2. Physiological signals khó tránh environmental noise và movement artifacts. [2015-E11]
3. Kết luận về long-term forecastability không luôn rõ, đôi khi phụ thuộc empirical comparison/researcher interpretation. [2015-E06]
4. Kết luận thực nghiệm áp dụng cho người **healthy, young, resting** trong controlled environment; Conclusion không cung cấp xác nhận cho drowsiness. [2015-E02, E11]

**Nhận xét phân tích — không phải tự nhận của tác giả:**

1. Chín người và repeated measurements hạn chế generalizability; số bản ghi không tăng sample size độc lập lên 45. [2015-E02]
2. Không có physiological-state contrast chủ động; liên hệ với mental/physical monitoring trong Conclusion là tiềm năng ứng dụng, không phải kết quả Awake–Drowsy. [2015-E02, E11–E12]
3. Embedding m = 4 dựa nghiên cứu trước; không báo cáo dataset-specific FNN và parameter sensitivity có hệ thống. [2015-E04, E12]
4. DNP, WTE và Wolf settings thiếu chi tiết quan trọng để tái lập; không chứng minh DNP chính là Simplex. [2015-E04–E09, E12]
5. Surrogate null hẹp; không có PPS test, comprehensive stochastic alternative tests, hay exact rejection rates/formal rank statistics trong PDF. [2015-E09, E12]
6. Similarity với noisy Rössler không xác định governing equations hoặc một physiological mechanism tạo chaos. [2015-E05–E11]
7. Không kiểm tra recording-length sweep trên 30/60/120/180 s; Figure 2 dài 30 s là ví dụ waveform, không phải study of 30 s estimator reliability. [2015-E02, E12]
8. Prediction curves dùng trục steps; sampling step của PPG là 0.005 s còn numerical integration step của các benchmark là 0.01 trong thời gian mô hình. Không tự coi cùng số steps là cùng physical prediction duration hoặc calibrated physiological time giữa PPG và các models. [2015-E02, E05–E06]

### Relevance to current manuscript

Các phân loại dưới đây là **nhận xét phân tích** về mối liên hệ, không phải endorsement cho kết quả của manuscript.

| Thành phần | Phân loại | Lý do và giới hạn | Nguồn |
|---|---|---|---|
| RQ1: PPS/noisy pseudoperiodic null | **Indirect conceptual relevance** | Tiền lệ cho surrogate-based hypothesis testing, nhưng null ở đây là linear Gaussian; không trực tiếp hỗ trợ một PPS rejection | [2015-E09] |
| RQ2: Awake–Drowsy | **Background relevance** | Hỗ trợ tính hợp lý của khảo sát PPG dynamics; không đo hai trạng thái này | [2015-E02, E11–E12] |
| Simplex forecastability | **Indirect conceptual relevance** | DNP có CC/RRMSE theo horizon; không xác lập Simplex hoặc cấu hình giống manuscript | [2015-E05–E06, E12] |
| RQA recurrence organization | **Indirect conceptual relevance** | Tìm hiểu recurrent geometry bằng reconstruction/Poincaré; không áp dụng RP/RQA | [2015-E04, E07, E12] |
| Rosenstein LLE | **Indirect conceptual relevance** | Cùng khảo sát trajectory divergence và finite-data pitfalls, nhưng dùng **Wolf** | [2015-E04] |
| Ultra-short windows | **No direct relevance** | Dữ liệu 5 min, không đánh giá systematic length sensitivity | [2015-E02, E12] |
| Reconstruction/estimator sensitivity | **Direct methodological relevance** | Quarter-period delay rule và cảnh báo LLE/noise là bài học trực tiếp; không bảo đảm lựa chọn m/τ phù hợp dataset hiện tại | [2015-E04, E06] |

### Source evidence

| Mã / Paper ID | Trang PDF, section, figure/table | Bằng chứng diễn giải trung thành | Confidence |
|---|---|---|---|
| **2015-E01 / 2015** | pp.1–2, Abstract; §1 Introduction; §2.1 | Nêu mục tiêu nghiên cứu dynamics healthy young subjects; giải thích các claim trước dựa CD/LE và tính noise-sensitive/inconclusive; mô tả background AC/DC và sinh lý PPG | High |
| **2015-E02 / 2015** | pp.3–4, §2.2; Figures 1–2 | 9 volunteers 19–27 tuổi, 5 repeats, 5 min, sampling steps 5 ms, right forefinger, BACS transmission-mode, resting/control protocol; wording reflected light và transmission-mode cùng tồn tại | High cho protocol; Medium cho nhất quán quang học |
| **2015-E03 / 2015** | p.4, §3 opening/§3.1; Figure 3, Table 1 | Nêu phân công các NTSA tests; phổ Fourier và PF 1.02–1.52 Hz; các LF được tác giả diễn giải về respiration/slow effects | High |
| **2015-E04 / 2015** | p.5, §§3.2–3.3; Figure 4, Table 2 | m = 4 dựa các nghiên cứu trước, delay quarter-period PF; Wolf LLE, bảng 45 estimates dương; cảnh báo positive LLE ngoài chaos/overestimation | High |
| **2015-E05 / 2015** | p.6, §3.4; Figure 5 | DNP CC/RRMSE theo prediction steps; equations/parameters Rössler và Lorenz, RK4 step 0.01; benchmark +7% noise; Figure 5 có cả Lorenz trong legend | High |
| **2015-E06 / 2015** | p.7, §3.4; Figure 6 và diễn giải Figure 5 | 160 steps = 0.8 s forecast, dicrotic notch còn tái hiện; high CC >0.96 và RRMSE <0.28 mô tả noiseless Rössler; khó diễn giải long-term prediction | High cho số liệu; Medium cho long-term interpretation |
| **2015-E07 / 2015** | pp.7–9, §3.5; Figures 7–8 | Poincaré sections từ 3D reconstruction bằng 2D clockwise rotating plane; expand/bend/stretch/fold theo α | High cho method; Medium cho topology interpretation |
| **2015-E08 / 2015** | p.9, §3.6; Table 3 | WTE PPG 60,000 points; entries 0.005–0.092; benchmark Rössler 0.0002, +10% noise 0.0045, white noise 1.08; tác giả diễn giải WTE nhỏ là determinism | High |
| **2015-E09 / 2015** | pp.9–10, §3.7; Figure 9 | Null linear Gaussian stochastic process, Fourier phase randomization bảo toàn power spectrum, 30 surrogates, DNP CC tách ensemble; tác giả reject null và suy luận về Gaussian noise | High cho thiết kế/claim; Medium cho phạm vi dataset được minh họa |
| **2015-E10 / 2015** | p.10, §4; Figure 10 | Arbitrary point/nearest neighbor, 140/300-step tracing; PPG và Rössler +7% noise; divergence rồi bounded behavior và continuous bending | High cho mô tả; Medium cho equivalence interpretation |
| **2015-E11 / 2015** | pp.10–11, §§4–5 | Discussion/Conclusion khẳng định consistency with chaotic motion và similarity với noisy Rössler; cảnh báo noise/previous tests, đề xuất future health monitoring applications | High cho phát biểu của tác giả |
| **2015-E12 / 2015** | Toàn PDF pp.1–11; đối chiếu §2.2/§§3.1–3.7/§5 | Không thấy application của PPS/RQA/Simplex, CD mới, FNN mới, length sweep hay Awake–Drowsy comparison; các cấu hình preprocessing/DNP/WTE chi tiết và formal p-values không được xác lập | High cho phạm vi phương pháp; Medium cho thông tin thiếu |

## 3. Sviridova et al. (2018)

**Thông tin thư mục.** Nina Sviridova, Tiejun Zhao, Kazuyuki Aihara, Kazuyuki Nakamura và Akimasa Nakano. *Photoplethysmogram at green light: Where does chaos arise from?* **Chaos, Solitons & Fractals**, 116 (2018), 157–165. DOI: [10.1016/j.chaos.2018.09.016](https://doi.org/10.1016/j.chaos.2018.09.016). Mục tiêu: kiểm tra gPPG có chaotic dynamics không, so sánh với NIR rPPG và xem các quá trình ở lớp da nông có thể đóng góp thế nào vào PPG complexity. [2018-E01, E10–E11]

### Research question and motivation

Introduction nêu rằng green PPG phổ biến trong wearables nhưng chưa được nghiên cứu dynamics đầy đủ như NIR PPG. Do green light có độ xuyên mô thấp hơn, gPPG có thể chịu ảnh hưởng của một tập quá trình khác hoặc ít yếu tố hơn rPPG. Tác giả đặt câu hỏi gPPG có complexity/chaotic properties tương tự rPPG không và liệu NTSA có hữu ích cho các ứng dụng gPPG. [2018-E01]

Bài cũng xem xét một model hình thành PPG từ literature: arterial transmural pressure làm thay đổi khoảng cách/mật độ mao mạch và tissue optical properties ở lớp nông, khác với giải thích chỉ dựa blood-volume variation. So sánh gPPG–rPPG được dùng để tìm dấu hiệu hỗ trợ vai trò của upper layers. **Model này được viện dẫn làm cơ sở giả thuyết, không được xây dựng hoặc trực tiếp đo/kiểm chứng cơ học trong thí nghiệm 2018.** [2018-E01, E10–E11]

Do đó mục tiêu của bài bao gồm cả **chaos identification**, **comparison of dynamical characteristics**, và **possible physical origin**; không phải một nghiên cứu wakefulness hoặc estimator-length reliability. [2018-E01, E12]

### Experimental data

| Hạng mục | Thông tin xác lập | Truy vết |
|---|---|---|
| Người tham gia | 18 người, tuổi 21–49, workers tại NIVFS/NARO; khỏe mạnh, không hút thuốc, không dùng thuốc, hoạt động thể lực mức tương tự, không tiền sử bệnh tim theo questionnaire | [2018-E02] |
| Thiết kế hai phần | 8 người được đo gPPG và rPPG **simultaneously**; 10 người khác chỉ ghi thêm gPPG | [2018-E02] |
| Repeats/thời lượng | Hai lần ghi/người, mỗi lần 5 min; từ protocol suy ra 36 gPPG và 16 rPPG records, không phải 52 người độc lập | [2018-E02]; số records là phép tính của báo cáo |
| gPPG | Green **530 nm**, reflectance-type recorder dựa Arduino UNO và PPG sensor for Arduino; **500 Hz**; ngón trỏ phải ở phần simultaneous experiment | [2018-E02] |
| rPPG | NIR **900 nm**, transmission-type finger recorder I.W. Technology Firm/Tokyo Devices; **400 Hz**; đặt ở bàn tay trái trong phần simultaneous experiment | [2018-E02] |
| Vị trí rPPG chi tiết | Văn bản xác lập left hand nhưng không nêu rõ ngón trong câu về simultaneous recording; **không tự bổ sung “left forefinger”** | [2018-E02] |
| Môi trường/trạng thái | Ngồi thư giãn, phòng yên tĩnh có air conditioning khoảng 24–25 °C, moderate ambient light; yêu cầu hạn chế chuyển động cánh tay; summer collection | [2018-E02] |
| Comfort/thermal perception | Comfortable 78%, slightly uncomfortable 22%; neutral 44%, slightly cool 39%, cool 17% | [2018-E02] |
| Kiểm soát physiological states | Không có Awake–Drowsy labels, sleep staging hoặc state intervention; comfort survey mô tả điều kiện đo, không trở thành một contrast outcome trong kết quả NTSA | [2018-E02, E12] |
| Preprocessing | Author Contributions ghi có data preprocessing; nhưng filter type/cutoff/order, normalization, artifact rejection: **Not established from the provided source** | [2018-E11–E12] |
| Resampling cho 0–1 test | Chuỗi được thinned tới **40 Hz** để xử lý oversampling; đây là thao tác riêng được báo cáo cho 0–1 test | [2018-E09] |

**Ý nghĩa của rPPG:** Introduction dùng rPPG cho red/NIR nói chung; dữ liệu comparison trong thí nghiệm này dùng **900 nm NIR**, không phải red 660 nm. Không viết đây là thí nghiệm three-wavelength comparison. [2018-E01–E02]

### Methods and technical configuration

| Phương pháp thực sự áp dụng | Thuộc tính/vai trò và lý do chọn | Cấu hình báo cáo | Quan hệ và giới hạn |
|---|---|---|---|
| **Time-delay reconstruction + false nearest neighbors (FNN)** | Tái dựng possible dynamics từ scalar series; FNN hướng dẫn embedding dimension | FNN cho gPPG, Figure 2; **m = 4 hoặc 5** được nhận định phù hợp, các kết quả sau ít khác; chọn **m = 4**; **τ = 40 samples**, Figure 3 caption cho gPPG/rPPG | Bài không giải thích đầy đủ cách chọn τ = 40; FNN thresholds và temporal exclusion chưa xác lập. Không đồng nhất với quarter-period rule của 2015 hoặc ACF 1/e của 2022. [2018-E03] |
| **Wayland test / local translation error (LTE) / WTE** | Kiểm tra continuity của local flow; xem noise-related heterogeneity dọc quỹ đạo | Từ arbitrary X0 và k neighbors Xi, translation vectors vi = yi − Xi; local error là average squared deviation khỏi mean vector, chuẩn hóa squared norm của mean vector; Figure 4 trên đoạn **10 s** | Giá trị k, mapping horizon và aggregation details chưa nêu đủ. Tác giả cảnh báo Wayland có thể sai với significant noise; dùng DNP/surrogates bổ sung. [2018-E04–E05] |
| **Deterministic nonlinear prediction (DNP)** | Ước lượng short-term predictability và decay của chất lượng dự báo | Discriminating statistic **CC**; curves tới **200 prediction steps**; histogram ở **1 và 20 steps**, Figures 5–6 | Không xác lập thuật toán chính xác là Simplex; không có RRMSE result mới tương ứng bài 2015 hoặc Mean NRMSE. Split, weights, neighbors và temporal exclusion chưa được xác lập. [2018-E06, E12] |
| **Fourier-transform phase-randomized surrogates (FTPRS)** | Test null **linear Gaussian stochastic process**, giữ power spectrum vốn chứa heart-rate information | **50** surrogate datasets theo loại được thể hiện trong Figures 5–6; phase randomization Fourier transform | DNP CC gốc được so với ensemble. Không kiểm tra mọi stochastic model; số 50 không tự xác lập p-value. [2018-E06–E07] |
| **Pseudoperiodic surrogates (PPS)** | Test null **uncorrelated noise-driven periodic orbit**; giải quyết khả năng DNP của noisy periodic và chaotic series giống nhau | Ensemble **50 PPS** trong Figures 5–6; viện dẫn Small, Yu & Harrison, reference [45]; cấu trúc large scale được giữ theo mô tả bài | Không nêu đủ neighborhood/noise radius, initialization và surrogate generation diagnostics. PPS ở đây là kiểm định cụ thể, không synonym của phase randomization. [2018-E06–E07] |
| **Largest Lyapunov exponent — Rosenstein et al. method** | Ước lượng average nearby-trajectory divergence; khảo sát khác biệt gPPG/rPPG | §3.4 trích reference **[47] = Rosenstein, Collins & De Luca (1993)**; dùng slope least-squares trên mean log-distance curve; Figure 7 khảo sát **m = 3,…,10**, panel b slope cho **m = 4** | Không phải Wolf. Fit interval, Theiler separation, neighbor rules và sensitivity của τ chưa được nêu đủ. Bài cảnh báo noise khiến LLE khó so sánh unambiguously. [2018-E08] |
| **0–1 test for chaos** | Thêm công cụ chaos classification không cần phase-space reconstruction | Translation variables pc/qc từ weighted cosine/sine sums; mean-square displacement Mc; growth rate Kc; **K = median(Kc)**, **c ∈ (0,2π)**; displacement lags tới **N/10**; input thinned **40 Hz** | Tác giả nói chỉ áp dụng cho deterministic time series và sensitivity to oversampling. Số c values, thinning/anti-aliasing algorithm và finite-sample implementation details chưa được xác lập. [2018-E09] |

**Các chi tiết thời gian — quy đổi, không phải cấu hình mới do tác giả báo cáo:** 40 samples ở 500 Hz tương đương 80 ms, ở 400 Hz tương đương 100 ms. Nếu prediction steps trên gPPG giữ sampling 500 Hz được nêu, 200 steps tương đương 0.4 s và 20 steps tương đương 40 ms. PDF báo cáo prediction chủ yếu bằng **steps**; không nên viết 200 steps = 1 s hoặc coi Figure 5 bao phủ recording duration 60 s. Không áp dụng mức 40 Hz của 0–1 test cho DNP hoặc mọi phép phân tích. [2018-E02–E03, E06, E09]

**Methods được nhắc nhưng không áp dụng như analysis riêng ở đây:** physiological waveform formation models là background; spectral predominant frequency được nêu trong động cơ surrogate selection/Discussion, nhưng không có một spectral-analysis result section tương đương §3.1 của 2015. Không có Poincaré section, correlation-dimension calculation, RP/RQA, LAM/TT hay recording-length sweep trong bài 2018. Các nghiên cứu về noise induction và prediction của rPPG được trích là nguồn trước, không được nhập thành thí nghiệm mới của bài này. [2018-E01, E05–E07, E10–E12]

### Principal empirical findings

| Kết quả trực tiếp | Pattern/số liệu và điều kiện | Evidence/statistical support | Caveat |
|---|---|---|---|
| Embedding dimension | FNN cho thấy m = 4–5 là lựa chọn phù hợp; chọn 4 do quantitative results ít khác | PDF pp.3–4, §3.1, Figures 2–3 | Threshold cụ thể của FNN và bằng chứng across subjects không nêu đủ. [2018-E03] |
| Quỹ đạo khác về hình dạng | gPPG/rPPG reconstructed trajectories khác đáng kể trong typical example | PDF pp.3–4, §3.1, Figure 3 | Geometry khác không tự đồng nghĩa complexity khác hoặc mechanism khác. [2018-E03] |
| WTE nhỏ | §3.2 báo **mean gPPG 0.069; mean rPPG 0.073**. Table 1 chỉ cho first simultaneous measurement của 8 người | PDF pp.3–4, §3.2, Table 1 | Không trộn means ở text với mean tự tính của Table 1; phạm vi tổng hợp của reported means chưa nêu đủ. Không có state test. [2018-E04] |
| LTE không đồng đều | Một số vùng có LTE cao; nhiều phần khác gần zero trên 10 s representative trajectory | PDF pp.4–5, §3.2, Figure 4 | Tác giả diễn giải local noise sensitivity; đây không phải quantitative measurement của noise fraction. [2018-E05] |
| Finite-horizon forecastability + surrogate discrimination | gPPG có short-term predictability; original CC curve/histogram marker phân biệt với phase-randomized và PPS ensembles | PDF pp.4–6, §3.3, Figures 5–6 | Typical examples; tác giả reject hai nulls, nhưng PDF không báo cáo formal rank p-values, rejection fraction hoặc multiplicity correction. [2018-E06–E07] |
| LLE dương | Table 1: gPPG **0.285–1.679**, rPPG **0.446–1.132**; Discussion reported means **0.938** và **0.797** | PDF pp.3,5–7, §3.4/§4, Table 1/Figure 7 | Ranges là min–max do báo cáo tổng hợp từ first measurements của 8 paired subjects; table không nêu rõ đơn vị. [2018-E08, E10] |
| Không có subject-independent difference rõ ở LLE | Tác giả nhận định không có clear observable difference consistent across subjects, dù mean gPPG lớn hơn | PDF pp.6–7, §3.4/§4, Table 1 | Wording “significant observable” không kèm formal test/p-value; không gọi đây là statistically significant group effect hoặc demonstrated equivalence. [2018-E08, E10] |
| 0–1 outputs gần 1 | Reported means: gPPG **0.996**, rPPG **0.993**; Table 1 ranges gPPG **0.990–0.997**, rPPG **0.979–0.996** | PDF pp.3,6–7, §3.5, Table 1/Figure 8 | Ranges là đọc bảng; near-1 classification được tác giả diễn giải trong giả định determinism đã chấp nhận. [2018-E09] |
| gPPG prediction decay nhanh hơn | Discussion mô tả gPPG CC giảm nhanh hơn previously reported rPPG results | PDF p.7, §4, Figure 5 và references [19,42] | Không phải một formal paired prediction-effect estimate được báo cáo đầy đủ trong cùng figure; cần giữ từ “reported comparison”. [2018-E10] |

### Interpretation and claims

**Authors’ claims:** bài kết luận gPPG và rPPG chaotic, coi Wayland/DNP/surrogates là bằng chứng determinism rồi áp dụng 0–1 test để hỗ trợ chaos classification. Tác giả cho rằng gPPG có chaotic characteristics biểu hiện mạnh hơn và các quá trình ở upper skin layers tạo gPPG complexity, có khả năng góp phần vào rPPG. [2018-E09–E11]

**Những nulls được reject:** linear Gaussian stochastic process và uncorrelated noise-driven periodic orbit. Original CC khác các surrogate ensembles là bằng chứng được bài dùng để reject; không có test của mọi stochastic dynamics hoặc mọi noisy pseudoperiodic model. [2018-E06–E07]

**Điểm giới hạn cơ chế được tác giả thừa nhận:** vẫn khó xác định rPPG complexity hoàn toàn do các quá trình tạo gPPG, còn blood-volume variation chỉ thêm amplitude, hay rPPG là interaction của nhiều complex processes. Vì vậy không thuật lại bài như đã chứng minh cơ chế vật lý duy nhất của chaos. [2018-E10–E11]

**Nhận xét phân tích về chaos:** kết luận của tác giả mạnh hơn mô tả đơn thuần nonlinear organization. Tuy nhiên, với manuscript hiện tại có thể trích cách họ kết hợp forecastability, divergence và surrogate tests mà không tiếp nhận claim mọi measured PPG là deterministic chaos. Đặc biệt, điều kiện áp dụng 0–1 test ở §3.5 dựa trên việc họ đã diễn giải các tests trước là determinism; gần 1 không trở thành một chứng minh độc lập loại trừ mọi stochastic alternatives. [2018-E04–E09]

**Nhận xét phân tích về physiological origin:** wavelength thay đổi đồng thời với recorder geometry, sampling rate và measurement side. Do đó cross-modality differences không tách riêng effect của depth hoặc chứng minh upper-layer process tự tạo chaos bằng một cơ chế độc lập. Đặc tính của observed signal không xác định duy nhất dynamics của từng physiological component tạo nó. Đây là hạn chế suy luận thiết kế, không phải một kết quả phủ định mô hình tác giả. [2018-E01–E02, E10–E11]

### Limitations

**Tác giả nêu rõ:**

1. Wayland test có thể có flaws với noise-contaminated data, nhất là noise đáng kể; cần thêm DNP/surrogates. [2018-E05–E06, E10]
2. Noise có thể làm sai hoặc overestimate LLE; gPPG/rPPG estimates không thể trực tiếp so sánh unambiguously. Tác giả cho rằng WTE nhỏ gợi ý noise thấp, nhưng đây là một assumption/inference. [2018-E08, E10]
3. 0–1 test cần deterministic-series interpretation và nhạy oversampling; phải thin input. [2018-E09]
4. Left/right hand có thể khác measurement-site effects; tác giả dựa literature để cho rằng khác biệt nhỏ ở healthy subjects. [2018-E02]
5. Blood-volume contribution và việc rPPG complexity có chỉ từ upper-layer processes hay không vẫn chưa rõ. [2018-E10–E11]

**Nhận xét phân tích — không phải tự nhận của tác giả:**

1. Chỉ 8 người có simultaneous cross-modality recordings; 10 người bổ sung chỉ có gPPG. Không trình bày mọi group summaries như fully paired data trên 18 người. [2018-E02]
2. Không có physiological-state change/control; comfort distributions không phải Awake–Drowsy outcomes. [2018-E02, E12]
3. Khác biệt modality bị gộp với wavelength, sensor/device, optical geometry, side và sampling frequency. [2018-E02]
4. Surrogate-generation và DNP details chưa đủ tái lập đầy đủ; không có exact p-values, population rejection rates hoặc kiểm tra độ ổn định mọi PPS parameters. [2018-E06–E07, E12]
5. Các 5-min recordings không kiểm chứng estimator performance riêng trên ultra-short windows. Prediction horizon ngắn là một khái niệm khác với input recording ngắn. [2018-E02, E06, E12]
6. LLE mean lớn hơn nhưng direction không nhất quán across subjects; không suy ra gPPG luôn “more chaotic” hoặc chaos intensity là một scalar physiological truth. [2018-E08, E10]
7. Figure 7 kiểm tra dimension của divergence curves nhưng không thay thế một comprehensive parameter/noise robustness study trong dataset khác. [2018-E08]
8. Motion-artifact robustness của green PPG được nêu như background và proposed insight; protocol hạn chế movement, không chủ động thử standardized motion challenges. [2018-E01–E02, E11–E12]

### Relevance to current manuscript

| Thành phần | Phân loại | Lý do và giới hạn | Nguồn |
|---|---|---|---|
| RQ1: PPS/noisy pseudoperiodic null | **Direct methodological relevance** | DNP dùng PPS để test uncorrelated noise-driven periodic orbit; tiền lệ gần nhất trong ba bài. Vẫn phải xác lập null/configuration của manuscript riêng | [2018-E06–E07] |
| RQ2: Awake–Drowsy | **Background relevance** | Có cross-measurement-condition comparison, không có so sánh hai physiological states này | [2018-E02, E10, E12] |
| Simplex forecastability | **Indirect conceptual relevance** | Prediction CC có vai trò trực tiếp trong surrogate discrimination; không xác lập DNP = Simplex | [2018-E06–E07, E12] |
| RQA recurrence organization | **No direct relevance** | Không sử dụng RP/RQA; trajectory geometry chỉ cho conceptual background gián tiếp | [2018-E03, E12] |
| Rosenstein LLE | **Direct methodological relevance** | Cùng họ estimator và mean log-distance slope; cảnh báo noise/embedding có giá trị trực tiếp | [2018-E08] |
| Ultra-short windows | **No direct relevance** | Không có length-reliability sweep; 5 min input khác short forecast horizon | [2018-E02, E06, E12] |
| Reconstruction/estimator sensitivity | **Direct methodological relevance** | FNN, m = 4 vs 5, dimension sweep m = 3–10 cho divergence, xử lý oversampling trong 0–1 test; không chứng nhận parameters của manuscript | [2018-E03, E08–E09] |

### Source evidence

| Mã / Paper ID | Trang PDF, section, figure/table | Bằng chứng diễn giải trung thành | Confidence |
|---|---|---|---|
| **2018-E01 / 2018** | pp.1–2, Abstract/§1 | Bibliography/DOI; gap về gPPG; khác biệt optical depth; mô hình tissue/capillary-density được trích từ literature; objective chaos và origin comparison | High |
| **2018-E02 / 2018** | pp.2–3, §2.1; Figure 1 | 18 subjects 21–49; 8 simultaneous g/r và 10 additional g; 2 × 5 min; 530 nm/500 Hz reflectance g, 900 nm/400 Hz transmission r; right forefinger/left hand; resting protocol và percentages comfort/thermal survey | High |
| **2018-E03 / 2018** | pp.3–4, §3.1; Figures 2–3 | FNN gPPG; m = 4/5 appropriate, minor differences rồi chọn 4; lag 40; typical geometry differs | High |
| **2018-E04 / 2018** | pp.3–4, §3.2; Table 1 | LTE definition với neighbor translation vectors; WTE means 0.069/0.073; Table 1 first simultaneous measurements | High cho số liệu; Medium cho phạm vi reported means |
| **2018-E05 / 2018** | pp.4–5, §3.2/§3.3; Figure 4 | LTE distribution trên đoạn 10 s không đều; cảnh báo Wayland với noise; rationale thêm predictability/surrogates | High |
| **2018-E06 / 2018** | pp.4–5, §3.3; Figure 5 | DNP CC đến 200 steps; FT phase-randomized và PPS, 50 datasets thể hiện cho mỗi loại; linear Gaussian và noisy-periodic nulls; giải thích lựa chọn theo PPG spectrum/cyclic behavior | High |
| **2018-E07 / 2018** | pp.5–6, §3.3; Figure 6 | Histograms ở 1/20 steps; tác giả nói original prediction distinguishable và reject hai nulls | High cho claim; Medium cho generality trên toàn dataset |
| **2018-E08 / 2018** | pp.3,5–6, §3.4; Table 1/Figure 7; p.9 ref. [47] | LLE theo Rosenstein; mean log-distance linear slope, m = 3–10 và m = 4 slope; estimates dương, noise caveats, no clear subject-independent difference | High |
| **2018-E09 / 2018** | pp.3,6–7, §3.5; Table 1/Figure 8 | 0–1 formulas và deterministic prerequisite, c range, N/10, median; thin tới 40 Hz; reported means 0.996/0.993 | High |
| **2018-E10 / 2018** | p.7, §4 | Means LLE 0.938/0.797; interpretation gPPG prediction decay nhanh hơn prior rPPG; no significant observable subject-independent LLE difference; origin ambiguity | High cho văn bản; Medium cho strength của cross-signal comparison |
| **2018-E11 / 2018** | p.8, §§4–5/Author Contributions | Tác giả kết luận chaos/gPPG complexity, upper-layer contribution, ambiguity về rPPG mechanism, potential applications; ghi có preprocessing nhưng không cho cấu hình | High |
| **2018-E12 / 2018** | Toàn PDF pp.1–9; đặc biệt §§2.1,3.1–3.5,4–5 | Không có Awake–Drowsy, RQA/Poincaré/CD mới, length sweep, standardized motion intervention hoặc thuật toán tên Simplex; formal p-values và nhiều technical settings không được xác lập | High cho phạm vi; Medium cho chi tiết thiếu |

## 4. Sviridova et al. (2022)

**Thông tin thư mục.** Nina Sviridova, Tiejun Zhao, Akimasa Nakano và Tohru Ikeguchi. *Photoplethysmogram Recording Length: Defining Minimal Length Requirement from Dynamical Characteristics*. **Sensors**, 22(14) (2022), article **5154**. DOI: [10.3390/s22145154](https://doi.org/10.3390/s22145154). Mục tiêu: đánh giá sai số của các RQA features theo chiều dài PPG và đề xuất minimum recording lengths để giữ relative error trong giới hạn được chọn. [2022-E01]

### Research question and motivation

Introduction nêu hai khó khăn đối với nonlinear PPG analysis: noise/artifacts có thể ảnh hưởng dynamics, còn filtering có thể thay đổi nonlinear features dù hữu ích cho conventional physiological measurements. Một lựa chọn khác là chỉ sử dụng các đoạn ngắn chất lượng tốt; cách này giảm computational cost và có tiềm năng cho real-time/wearable use, nhưng cần biết short-recording estimates đáng tin đến mức nào. [2022-E01]

Bài nhận xét literature sử dụng recording lengths rất khác nhau và chưa xác định có hệ thống minimum length/sai số cho short PPG RQA trong phạm vi hiểu biết tác giả lúc đó. Tác giả muốn tính error curves và recommended limits cho NIR PPG trong reference environment. Đây là **estimator/recording-design study**, không phải một chaos-identification experiment mới và không phải physiological-state discrimination study. Các assertions về deterministic chaos trong Introduction dựa trên literature, gồm bài 2015/2018. [2022-E01, E11]

**Nhận xét phân tích:** không dùng câu “no study so far” của bài 2022 như một kết luận hiện hành rằng toàn bộ lĩnh vực chưa có nghiên cứu short PPG. Nó là phát biểu phạm vi literature của tác giả tại thời điểm xuất bản và không trực tiếp bao gồm Awake–Drowsy. [2022-E01]

### Experimental data

| Hạng mục | Thông tin xác lập | Truy vết |
|---|---|---|
| Dữ liệu thực | **30 datasets**, từ participants tuổi **21–49** | [2022-E02] |
| Số người độc lập | **Not established from the provided source.** Có hai measurement repeats nhưng không đủ căn cứ để tự ghi 15 participants | [2022-E02, E11] |
| Địa điểm/thời gian | NIVFS/NARO, **2017–2018** | [2022-E02] |
| Điều kiện chọn | Nonsmoking, không history of CVD, good health, reported comfortable environment theo questionnaire; thu thập thêm thông tin gender, age, sickness và lifestyle | [2022-E02] |
| Thiết bị | **IWS920**, I.W. Technology Firm/Tokyo Devices; transmission-type **NIR PPG** | [2022-E02, E10] |
| Bước sóng chính xác/vị trí giải phẫu | **Not established from the provided source.** Figure 1 là schematic conventional finger setup, không thay thế một acquisition-site statement cụ thể | [2022-E02, E11] |
| Sampling rate | **409.6 Hz**; subsampling factor **2** và **4**, tạo **204.8** và **102.4 Hz** | [2022-E02] |
| Recording duration | Mỗi measurement **5 min**, lặp hai lần | [2022-E02] |
| Môi trường/trạng thái | Relaxed sitting position, air-conditioned room **25 °C**; healthy/comfortable reference recordings; không Wake–Drowsy labels | [2022-E02, E10–E11] |
| Preprocessing/filter | Specific filter type/cutoff/order, artifact handling và anti-aliasing trước subsampling: **Not established from the provided source**. Không nhập filtering từ các papers được cite thành thao tác họ đã làm | [2022-E01–E02, E11] |
| Phạm vi length analysis | PPG segments **3–152 average cycles**, mô tả khoảng **2.4–122 s**; cycle được đặt **0.8 s** | [2022-E08] |
| Dữ liệu mô phỏng | Original và noisy **Rössler model**, dùng làm preliminary benchmark length/noise sensitivity | [2022-E03, E07] |

**Quan hệ dataset giữa các bài:** tuổi/địa điểm và thời gian thu thập có nét gần bài 2018, nhưng PDF 2022 không xác lập đầy đủ mapping participants/records với bài 2018. Không coi ba bài là ba cohorts hoàn toàn độc lập hoặc tự khẳng định 2022 tái dùng toàn bộ dữ liệu 2018. Sampling NIR được báo cáo **400 Hz** ở 2018 và **409.6 Hz** ở 2022; giữ nguyên thông tin của mỗi bài. [2018-E02; 2022-E02, E11; nhận xét phân tích]

### Methods and technical configuration

| Phương pháp thực sự áp dụng | Thuộc tính/vai trò và lý do chọn | Cấu hình báo cáo | Quan hệ, assumptions và limits |
|---|---|---|---|
| **Rössler numerical simulation + dynamical noise** | Benchmark để kiểm tra RQA error theo noise/length trước PPG; dựa sự tương đồng được đề xuất ở study 2015 | **a = 0.2, b = 0.2, c = 5.7**; RK4 **1000 Hz**; mỗi iteration dùng x̃ᵢ = xᵢ + θγᵢ làm input iteration tiếp theo; γᵢ là fixed uniform random-noise vector; θ mô tả từ **0 đến 0.5**, increments **0.05**; subsample factor **5** | Noise đi vào evolution, không chỉ cộng lên output cuối cùng. θ là scale coefficient, không phải phần trăm noise PPG. Tables 1–2 ghi **0.245**, khác grid 0.05 mô tả trong §2.3; cần giữ discrepancy. [2022-E03, E07] |
| **Time-delay embedding** | Cung cấp trajectory distances cho recurrence analysis | Xⱼ = (xⱼ,xⱼ₊τ,…,xⱼ₊₍ₘ₋₁₎τ), N = n − (m−1)τ; với NIR PPG **m = 4**, **τ = thời điểm ACF giảm dưới 1/e** | Numeric τ values không được liệt kê; bài nói loại PPG khác có thể cần delay khác. Không báo cáo FNN sweep mới ở 2022. [2022-E04] |
| **Recurrence plot (RP)** | Binary representation của returns/near-neighbor relations trong reconstructed state space | Rᵢⱼ = 1 khi distance < ε; **ε = 10% maximal distance** giữa attractor points | Threshold rule dựa attractor size, **không phải fixed recurrence rate**. Distance norm name, line-of-identity exclusion, Theiler window và việc giữ/recompute ε qua lengths chưa được xác lập đủ. [2022-E04, E11] |
| **RQA — DET** | Fraction recurrence points nằm trên diagonal lines có length ≥ lmin; tác giả gọi determinism | Công thức weighted diagonal-line count; text nói DET > **0.9** có thể coi là sign of determinism | Giá trị **lmin** thực tế không nêu; DET là statistic của RP, không chứng minh physical determinism. [2022-E05] |
| **RQA — Lmax** | Longest diagonal line; tác giả liên hệ **1/Lmax** với trajectory divergence | Lmax từ longest diagonal; Tables 1–3 và error curves đánh giá chính **Lmax** | Không phải Rosenstein/Wolf LLE; bài không ước lượng LLE mới từ data. Inverse-longest-diagonal interpretation không chứng minh bằng với dynamical invariant LLE. [2022-E05, E07–E09] |
| **RQA — L** | Average diagonal line length; tác giả diễn giải là mean prediction time | L = Σ(lP(l))/ΣP(l) trên l ≥ lmin | Trực tiếp gần **Lmean** của manuscript về họ statistic; không đồng nhất với measured Simplex CC/NRMSE hoặc direct forecast horizon. [2022-E05] |
| **RQA — ENTR** | Entropy của distribution diagonal-line lengths; mô tả complexity của RP theo statistic này | ENTR = −Σp(l)ln p(l), p(l) = P(l)/Nl | Không phải Sample Entropy, Permutation Entropy, Kolmogorov–Sinai entropy hay blanket physiological complexity measure. [2022-E05] |
| **Recording-length / relative-error analysis** | Tìm minimum length theo từng feature, sử dụng long-series estimate làm reference | **Eₗ = abs(Sₗ − S_T)/S_T × 100%**; lower initial range 3–5 cycles; reference length giả định đủ chính xác khi **>100 average cycles**; examine **5% và 1%** limits | “Error” là discrepancy với reference estimate, không error so với known true physiological invariant. **1% là criterion được chọn**, không một chuẩn validity chung. [2022-E06] |
| **Rössler segment repetition** | Tổng hợp variability của error theo segment | **1500–50,000 points**, tương ứng mô tả **5–168 average cycles**; **100 different segments cho mỗi length** | 100-segment statement xác lập rõ cho simulated system; số segments/start-selection cho mỗi PPG length không được mô tả rõ tương đương. [2022-E07–E08] |
| **Sampling-rate sensitivity by subsampling** | Xem length recommendations có ổn định khi giảm sampling rate | 409.6/204.8/102.4 Hz; Table 3 reporting length bằng average cycles | Chỉ ba rates có liên hệ từ cùng bản ghi; không xác nhận mọi sensor/sampling regime. [2022-E02, E09–E10] |

**Lưu ý reference của embedding dimension:** §3.1 ghi chọn m = 4 theo reference **[25]**, đồng thời mô tả minimum dimension từng được xác định bằng FNN. Reference [25] ở p.13 chính là bài **2015**. Tuy nhiên §3.2 của PDF 2015 chọn m = 4 từ prior studies, không báo cáo FNN mới; FNN được thể hiện trực tiếp ở bài 2018. Đây là **điểm truy dẫn chưa khớp**, không phải căn cứ để bổ sung FNN vào methods thực nghiệm 2015 hoặc 2022. [2022-E04, E12; 2015-E04, E12; 2018-E03]

**Chỉ thảo luận/cite, không thực hiện mới:** chaos trong cardiac/respiratory dynamics; effect of filtering từ papers trước; short hypertension PPG/RQA trước đây; state-space filtering cho HRV như future direction. Không có PPS/phase surrogates, DNP/Simplex, Wolf/Rosenstein LLE, 0–1 test, Poincaré sections hoặc correlation-dimension calculation mới trong bài 2022. **LAM và TT không nằm trong bộ RQA họ đánh giá.** [2022-E01, E05, E10–E11]

### Principal empirical findings

**1. Benchmark Rössler: noise có tác động feature-specific.** Table 1 báo các reference values sau; đây là noisy simulated system, không phải PPG hoặc physiological-state effects. [2022-E07]

| θ đúng như Table 1 | DET | Lmax | L | ENTR |
|---:|---:|---:|---:|---:|
| 0 | 0.9992 | 3763.9 | 60.4329 | 4.6079 |
| 0.245 | 0.4138 | 7.52 | 2.3379 | 0.7544 |
| 0.5 | 0.0910 | 3.24 | 2.0455 | 0.1765 |

Thêm noise làm ngắn diagonal lines và thay đổi DET/ENTR mạnh trong các ví dụ bảng. Discussion cho rằng high noise phá determinism khi DET thấp hơn 0.9; báo cáo ghi nhận đây là **cách tác giả diễn giải DET**, không là phép chứng minh bản chất hệ từ một ngưỡng. [2022-E05, E07, E10]

Table 2 cho lengths, đơn vị **points**, tại criterion **1%** của Rössler: [2022-E07]

| θ đúng như Table 2 | DET | Lmax | L | ENTR |
|---:|---:|---:|---:|---:|
| 0 | 1500 | 48,500 | 16,000 | 26,000 |
| 0.245 | 17,000 | 46,000 | 3500 | 30,000 |
| 0.5 | 7000 | 47,000 | 13,500 | 43,500 |

**Pattern:** Lmax yêu cầu lengths gần reference 50,000; DET có thể ổn định trên đoạn ngắn, còn required length của L/ENTR thay đổi theo noise, không nhất thiết monotonic. Với θ = 0, **ENTR cần 26,000 points**, nên không viết noiseless-system entropy luôn ổn định trên vài chu kỳ. Các bảng không cung cấp CI hay formal hypothesis tests. [2022-E07, E10]

**2. PPG: reference values và minimum lengths khác nhau theo feature.** Table 3 tại 409.6 Hz báo reference DET **0.998**, Lmax **49,859**, L **144.38**, ENTR **5.73**. Không nhầm **L = 144.38 points** với **minimum input length L = 131.10 cycles** để đạt criterion 1%. [2022-E09]

| Feature | Criterion | 409.6 Hz: cycles | 204.8 Hz: cycles | 102.4 Hz: cycles | Giây ở 409.6 Hz, quy đổi ×0.8 |
|---|---:|---:|---:|---:|---:|
| DET | 5% | 3.05 | 3.05 | 3.05 | 2.440 |
| DET | 1% | 3.05 | 3.05 | 3.05 | 2.440 |
| Lmax | 5% | 144.82 | 143.38 | 143.39 | 115.856 |
| Lmax | 1% | 149.39 | 150.28 | 150.25 | 119.512 |
| L | 5% | 65.55 | 64.19 | 64.02 | 52.440 |
| L | 1% | 131.10 | 132.79 | 133.02 | 104.880 |
| ENTR | 5% | 7.62 | 9.65 | 10.67 | 6.096 |
| ENTR | 1% | 21.34 | 22.05 | 24.39 | 17.072 |

Nguồn trực tiếp: **2022, PDF p.10, §4.2, Figure 8/Table 3**; confidence **High** cho table entries. Cột giây là tính toán của báo cáo theo average cycle 0.8 s ở p.9; không phải reproduction của mọi giá trị giây trong Discussion. Caption Table 3 nói **average lengths**; không diễn giải như guarantees cho mọi individual recording/window. [2022-E08–E09]

**3. Lmax gần giới hạn bản ghi.** Figure 8 cho Lmax relative error giảm mạnh khi length tiến gần maximal analysed length; Discussion cho rằng Lmax không phù hợp short recordings loại PPG này vì required length và chính Lmax đều gần maximal length. Đây là giới hạn của **Lmax-based analysis**, không phải một kết quả trực tiếp về validity của Rosenstein LLE trên cửa sổ ngắn. [2022-E09–E10]

**Nhận xét phân tích bổ sung:** L error curve trong Figure 8 không hoàn toàn monotonic; có vùng ngắn đạt error thấp rồi tăng trước khi giảm ở lengths lớn. Vì vậy một local crossing dưới criterion không đủ để khẳng định mọi length dài hơn đều đạt cùng reliability. Table 3 và shape của error curve cần được đọc cùng nhau. [2022-E09; confidence Medium cho qualitative curve reading]

**4. Sampling-rate comparisons.** Required lengths bằng cycles thay đổi ít với subsampling trong Table 3; thay đổi rõ hơn đối với ENTR ở 5% criterion. Kết quả hỗ trợ độ ổn định tương đối trong rates thử nghiệm, không một invariance theo arbitrary sampling. [2022-E09–E10]

**5. Hai vị trí số liệu chưa khớp cần bảo toàn.**

| Điểm | Table/methods | Discussion | Cách xử lý trong audit |
|---|---|---|---|
| Ngưỡng 1% của ENTR/L/Lmax | Table 3 tại 409.6 Hz: **21.34 / 131.10 / 149.39 cycles** | p.11 ghi **21.35 / 131.15 / 149.75 cycles**, tương ứng **17.08 / 104.92 / 119.8 s** | Khác nhỏ nhưng không hoàn toàn bằng; dùng Table 3 khi trích bảng, Discussion khi thuật wording, không ghép thành bộ số “chính xác” duy nhất. [2022-E09–E10] |
| ENTR dưới 5% | Table 3: **7.62 cycles ≈ 6.096 s** ở 409.6 Hz | p.12 nêu **3.8 s** có average error thấp hơn 5% | Chưa có giải thích thống nhất trong PDF; không dùng 3.8 s như recommended universal threshold. [2022-E09–E10] |
| Noise grid mô phỏng | §2.3: increments **0.05** từ 0 đến 0.5 | Tables 1–2 chọn **θ = 0.245** | Không tự đổi 0.245 thành 0.25 hoặc đoán grid thực tế; cần author/code clarification nếu replicate. [2022-E03, E07] |

**Statistical support:** error curves và average limits là descriptive/relative-reference analyses. Không thấy tests của physiological group differences, p-values hoặc confidence intervals cho recommended cutoffs; không gọi chúng là validated clinical thresholds. [2022-E06–E11]

### Interpretation and claims

**Tác giả kết luận:** RQA có thể cung cấp sufficiently accurate estimates của một số dynamical features từ short NIR PPG, với requirements riêng cho từng feature. DET/ENTR có thể đạt sai số nhỏ trên đoạn ngắn, L cần dài hơn, Lmax problematic cho short recordings. Bài gọi các features theo determinism, divergence, average prediction time và complexity. [2022-E05, E09–E10]

**Điều bài không thực hiện:** không đưa một new surrogate rejection/chaos-detection test; không trực tiếp forecast future samples bằng Simplex/DNP; không ước lượng largest Lyapunov exponent; không xác nhận Awake–Drowsy differences. Introduction nhận deterministic chaos như một literature premise, khác với empirical objective của study. [2022-E01, E11]

**Nhận xét phân tích về “accuracy”:** S_T cũng là một finite-data estimate, được giả định đủ chính xác từ >100 cycles. Eₗ nhỏ cho thấy agreement với reference của cùng analysis, chưa chứng minh agreement với một known ground-truth physiological invariant. Đặc biệt, DET gần 0.998 có thể ít thay đổi theo length; estimator stability của một statistic gần saturation không tự xác nhận physiological discrimination hoặc physical determinism. [2022-E05–E06, E09]

**Nhận xét phân tích về “prediction time” và “divergence”:** L là mean recurrence diagonal length, Lmax là maximum recurrence diagonal length. Chúng không thay thế out-of-sample CC/NRMSE hoặc slope của Rosenstein mean-log-distance curves. Có conceptual overlap giữa recurrence organization, forecastability và divergence, nhưng mỗi phép đo có construction/assumptions riêng. [2022-E05; 2018-E06, E08]

### Limitations

**Tác giả nêu rõ:**

1. Study là preliminary, dùng PPG của healthy people ngồi thoải mái trong reference environment. [2022-E10]
2. Kết quả áp dụng cho **transmission-type NIR PPG**; cần kiểm tra các loại PPG và experimental settings khác. [2022-E10]
3. Sampling rate khác đáng kể có thể thay đổi kết quả; cần systematic sampling investigation với high-rate/long reference recordings. [2022-E10]
4. Lmax không phù hợp cho short recordings của loại PPG được khảo sát. [2022-E10]
5. Filtering có thể ảnh hưởng nonlinear features; state-space noise reduction là future direction được đề nghị, không một preprocessing pipeline đã validated ở đây. [2022-E01, E10]

**Nhận xét phân tích — không phải tự nhận của tác giả:**

1. **30 datasets không xác lập số participants** hoặc structure of repeated-measure dependence; không suy ra independent n = 30. [2022-E02, E11]
2. Không có bệnh lý/state-dependent validation hoặc Awake–Drowsy comparison; comfort/healthy selection không đại diện đầy đủ real wearable settings. [2022-E02, E10–E11]
3. Cycle 0.8 s là quy ước physiology-average, không measured cardiac-cycle length riêng của mỗi người; khi chuyển recommended cycles thành giây cần giữ assumption này. [2022-E08]
4. Reference accuracy dựa finite length và cùng estimator; không phải unbiased-error analysis against ground truth. [2022-E06, E09]
5. Chưa xác lập lmin, Theiler window, identity-line handling, norm implementation và việc ε được giữ hay tính lại qua lengths. Các lựa chọn này quan trọng khi so sánh với RQA của manuscript. [2022-E04–E06, E11]
6. **Không được kết luận họ đã giữ hoặc đã loại line of identity.** Lmax gần maximal length làm vấn đề này cần kiểm chứng; PDF không đủ để quy kết một implementation error cụ thể. [2022-E04, E09–E11]
7. Một ngưỡng dài trung bình không bảo đảm low error cho mọi session, state hay recording; chưa có reported CI/distribution đủ để diễn giải individual reliability. [2022-E09, E11]
8. **LAM/TT chưa được nghiên cứu**, nên không mở rộng short-recording results của DET/ENTR/L sang vertical-line metrics. [2022-E05, E11]
9. **Lmean trong 60 s:** nếu lấy Table 3 làm bối cảnh ở 409.6 Hz, 60 s vượt mean 5% cutoff (~52.44 s), nhưng thấp hơn mean 1% cutoff (~104.88 s) của L. Điều này không chứng minh Lmean hiện tại “invalid”, cũng không cho phép quảng cáo 60 s đạt <1% error; cấu hình/điều kiện khác cần sensitivity analysis riêng. [2022-E08–E10]
10. Mức noise trong simulated Rössler không đo mức noise PPG; không áp các θ thresholds thành cutoffs cho physiological data. [2022-E03, E07–E08]
11. Các discrepancies trong Table/Discussion và embedding reference phải được ghi nhận thay vì sửa im lặng. [2022-E04, E09–E12]

### Relevance to current manuscript

| Thành phần | Phân loại | Lý do và giới hạn | Nguồn |
|---|---|---|---|
| RQ1: PPS/noisy pseudoperiodic null | **No direct relevance** | Không chạy surrogate tests; RQA error stability không cho bằng chứng reject PPS | [2022-E05–E11] |
| RQ2: Awake–Drowsy | **Background relevance** | Cho biết cần xét reliability trước state comparison; không cung cấp state outcome | [2022-E02, E10–E11] |
| Simplex forecastability | **Indirect conceptual relevance** | L được gọi mean prediction time nhưng không phải direct forecasting hoặc Simplex CC/NRMSE | [2022-E05] |
| RQA recurrence organization | **Direct methodological relevance** | DET và L cùng họ metrics với DET/Lmean; ε/delay/length considerations có giá trị trực tiếp. Không trực tiếp validate LAM/TT | [2022-E04–E09] |
| Rosenstein LLE | **Indirect conceptual relevance** | Recording-length caution và Lmax/divergence interpretation; không khảo sát Rosenstein estimator | [2022-E05–E10] |
| Ultra-short windows | **Direct methodological relevance** | Systematic length sensitivity trên 2.4–122 s; nhấn mạnh feature-specific requirements | [2022-E06, E08–E10] |
| Reconstruction/estimator sensitivity | **Direct methodological relevance** | m = 4, ACF 1/e delay, relative-distance threshold, length/noise/subsampling analyses; parameters không tự transfer | [2022-E03–E10] |

### Source evidence

| Mã / Paper ID | Trang PDF, section, figure/table | Bằng chứng diễn giải trung thành | Confidence |
|---|---|---|---|
| **2022-E01 / 2022** | pp.1–3, Abstract/§1 | Bibliography/DOI, objective error/minimum length; noise/filtering motivation, short quality segments, recording-length diversity; chaos premise được viện dẫn từ literature | High |
| **2022-E02 / 2022** | pp.3–4, §§2.1–2.2; Figures 1–2 | NIR recordings NIVFS 2017–2018; 21–49 tuổi, healthy/nonsmoking/comfortable selection, 30 datasets; IWS920, 409.6 Hz, 5 min ×2, 25 °C; subsample factors 2/4 | High |
| **2022-E03 / 2022** | pp.4–5, §2.3; Figure 3 | Rössler a/b/c = 0.2/0.2/5.7; RK4 1000 Hz, state noise x̃ᵢ input next iteration, θ 0–0.5 grid 0.05; subsample factor 5 | High |
| **2022-E04 / 2022** | p.5, §§3.1–3.2 | Embedding equation, NIR m = 4 theo [25], ACF dưới 1/e delay, ε = 10% max attractor-point distance; cautions adjustment for other PPG types | High |
| **2022-E05 / 2022** | p.6, §3.3 | Công thức/diễn giải DET, Lmax, L, ENTR; DET >0.9 theo literature; chỉ four diagonal-line features; lmin có định nghĩa nhưng không numeric setting | High |
| **2022-E06 / 2022** | pp.6–7, §3.4 | Lower range 3–5 cycles, reference assumed accurate >100 cycles, relative error abs(Sₗ−S_T)/S_T ×100% | High |
| **2022-E07 / 2022** | pp.7–9, §4.1; Figures 4–6/Tables 1–2 | Simulated length 1500–50,000 points, 100 segments/length; noise-dependent errors and thresholds; tables ghi θ = 0,0.245,0.5 | High |
| **2022-E08 / 2022** | p.9, §4.2; Figure 7 ở p.10 | PPG range 3–152 cycles ≈2.4–122 s, fixed average cycle 0.8 s; RP illustration từ segment 24.4 s | High |
| **2022-E09 / 2022** | p.10, §4.2; Figure 8/Table 3 | Average lower limits tại 5%/1% cho 409.6/204.8/102.4 Hz; reference DET/Lmax/L/ENTR = 0.998/49,859/144.38/5.73; exact table entries như trích ở trên | High |
| **2022-E10 / 2022** | pp.11–12, §§5–6 | Preliminary/reference-setting limitation; DET/ENTR short vs L/Lmax dài; số giây trong Discussion, 3.8 s ENTR example; other-type/sampling/filtering caveats | High cho wording; Medium cho các ngưỡng bất nhất |
| **2022-E11 / 2022** | Toàn PDF pp.1–14; đặc biệt §§2.2,3.1–3.4,4.2,5–6 | Không xác lập participant count/site/wavelength exact hay nhiều implementation settings; không có new surrogate/DNP/LLE/state contrasts, LAM/TT; không thấy formal group p-values/threshold CIs | High cho method scope; Medium cho chi tiết thiếu |
| **2022-E12 / 2022** | p.5 §3.1; p.13 reference [25]; đối chiếu 2015 p.5 §3.2 và 2018 pp.3–4 §3.1/Figure 2 | FNN attribution trong 2022 trỏ về 2015, nhưng 2015 chọn dimension theo prior studies; empirical FNN rõ trong 2018 | High cho discrepancy; nguyên nhân chưa xác lập |

## 5. Cross-Paper Comparison

| Tiêu chí | 2015 | 2018 | 2022 |
|---|---|---|---|
| Research objective | Kiểm tra consistency với chaotic motion, characterize nhiều mặt PPG dynamics. [2015-E01, E11] | Kiểm tra gPPG chaos, so sánh với rPPG, xem xét possible origin trong tissue layers. [2018-E01, E10–E11] | Đánh giá RQA error theo length và recommended minima. [2022-E01, E06] |
| PPG/setting | 9 healthy young people, 5 × 5 min, NIR finger PPG, 200 Hz quy đổi; controlled resting environment. [2015-E02] | 18 healthy people; 8 paired simultaneous g/r +10 g-only, 2 × 5 min; 530 nm reflectance 500 Hz và 900 nm transmission 400 Hz. [2018-E02] | 30 datasets, participant count chưa xác lập; 5-min NIR transmission recordings ở 409.6 Hz, subsampling; healthy/comfortable reference environment. [2022-E02, E10–E11] |
| Reconstruction | m = 4 từ prior studies; τ quarter-period PF. [2015-E04] | FNN m = 4–5, chọn 4; τ = 40 samples. [2018-E03] | NIR m = 4 theo cited study; τ khi ACF <1/e; không new FNN experiment. [2022-E04, E12] |
| Nonlinear techniques | Wolf LLE, DNP CC/RRMSE, Poincaré, Wayland, Fourier phase surrogates, trajectory tracing; spectral/modeled-system comparison bổ sung. [2015-E03–E10] | Wayland/LTE, DNP CC, FTPRS + PPS, Rosenstein LLE, 0–1 test. [2018-E03–E09] | RP/RQA DET, Lmax, L, ENTR; relative-reference error, noisy-Rössler and subsampling sensitivity. [2022-E03–E09] |
| Properties investigated | Geometry, local flow continuity, finite-horizon predictability, divergence và linear-null discrimination. [2015-E04–E10] | Geometry/flow, predictability, divergence, two-null discrimination, 0–1 chaos classification và cross-modality characteristics. [2018-E03–E10] | Diagonal recurrence statistics, estimator stability theo length/noise/sampling; không direct forecasting. [2022-E05–E10] |
| Main findings | Positive Wolf LLE, WTE nhỏ, short prediction, phase-surrogate distinction, noisy-Rössler-like patterns. [2015-E04–E11] | g/r positive Rosenstein estimates, near-1 0–1 outputs; gPPG prediction khác hai surrogate types; mean/qualitative differences không có demonstrated state effect. [2018-E06–E10] | DET/ENTR cần length ngắn hơn L/Lmax; Lmax gần maximal reference length; sampling reductions ít đổi average-cycle limits. [2022-E09–E10] |
| Chaos/nonlinearity interpretation | Authors conclude consistency with chaotic motion under chosen definition. [2015-E11] | Authors conclude both g/r chaotic, g characteristics more emphasized; proposed upper-layer origin contribution. [2018-E10–E11] | Literature premise về chaos; empirical outcome là RQA relative-error/length, không new chaos proof. [2022-E01, E10–E11] |
| Surrogate/null model | 30 Fourier-phase surrogates; linear Gaussian stochastic null. **Không PPS**. [2015-E09, E12] | 50 surrogates mỗi loại được thể hiện; linear Gaussian và uncorrelated noise-driven periodic orbit. **Có PPS**. [2018-E06–E07] | **Không surrogate analysis mới**. Noisy Rössler simulations không phải PPS ensembles. [2022-E03, E11] |
| Length/noise | Fixed 5-min acquisition; noise-sensitive LLE cảnh báo; noisy Rössler comparison/WTE benchmarks; không length sweep. [2015-E02, E04–E08, E12] | Fixed 5-min acquisition; noise caveats, dimension curves, thinning 40 Hz cho 0–1; không systematic length sweep. [2018-E02, E08–E09, E12] | Trọng tâm length/noise; mô phỏng và PPG length sweep, criterion 1%/5%, rate sensitivity. [2022-E03, E06–E10] |
| Physiological-state comparison | Resting healthy PPG; không Awake–Drowsy. [2015-E02, E12] | Comparison **measurement modalities**, không Awake–Drowsy; comfort survey không được dùng làm state-effect test. [2018-E02, E12] | Healthy reference data; không Awake–Drowsy hay clinical-state comparison mới. [2022-E02, E11] |
| Limits trọng yếu | Small cohort, settings chưa đủ replicate, limited null, no ultra-short validation. [2015-E02, E04, E09, E12; analytical observations] | Small paired cohort; modality confounds; finite-noise inference; surrogate settings/statistics chưa đủ; origin không phân giải. [2018-E02, E08–E12; phần confounds là analytical] | Relative reference không ground truth; unknown n participants/settings; feature-specific cutoffs, applicability limits, internal numeric differences. [2022-E02, E04–E12; phần reference/n là analytical] |
| Relevance manuscript | Forecastability/divergence background và rationale nhiều tests; không direct PPS/RQA/short-state study. [2015-E04–E12] | Direct tiền lệ **PPS + prediction** và **Rosenstein**; không Simplex/state/RQA/short-length validation. [2018-E06–E12] | Direct **RQA/length sensitivity**; không validate PPS, Simplex, Rosenstein hoặc LAM/TT cho states. [2022-E04–E11] |

**Ma trận chống gán nhầm methods.** “Có” nghĩa được áp dụng trong study, “Không” nghĩa không thấy application mới trong provided PDF; không có nghĩa phương pháp chưa từng tồn tại trong literature.

| Method | 2015 | 2018 | 2022 |
|---|---|---|---|
| Time-delay embedding | Có | Có | Có |
| Dataset-specific FNN được thể hiện | Không | Có, gPPG | Không; chỉ cited rationale |
| LLE — Wolf | Có | Không | Không |
| LLE — Rosenstein | Không | Có | Không |
| DNP + prediction CC | Có | Có | Không |
| DNP RRMSE | Có | Không thấy result mới | Không |
| Explicit Simplex Projection algorithm | Không được xác lập | Không được xác lập | Không |
| Fourier-phase-randomized surrogates | Có | Có | Không |
| PPS | Không | Có | Không |
| Poincaré sections | Có | Không | Không |
| Wayland/LTE | Có WTE | Có WTE/LTE | Không |
| 0–1 test | Không | Có | Không |
| RP/RQA DET, Lmax, L, ENTR | Không | Không | Có |
| RQA LAM, TT | Không | Không | Không |
| New correlation-dimension analysis | Không | Không | Không |
| Recording-length sweep | Không | Không | Có |

Nguồn cho ma trận: [2015-E03–E12; 2018-E03–E12; 2022-E03–E12]. Confidence High cho method scope; “Simplex không được xác lập” có nghĩa không có mô tả đủ để đồng nhất tên/cấu hình, không khẳng định DNP hoàn toàn không có liên hệ thuật toán với local-neighbor prediction.

**Sự thay đổi trọng tâm khoa học.** Có một liên hệ thực tế: 2018 viện dẫn kết quả NIR của 2015 và mở câu hỏi sang green PPG/formation mechanism; 2022 viện dẫn cả hai và tập trung reliability khi bản ghi ngắn. Tuy vậy, đây không phải một chuỗi chứng minh hoàn chỉnh mà bài sau “xác nhận” mọi inference của bài trước. 2015 bổ sung nhiều diagnostic perspectives; 2018 làm rõ việc cần phân biệt noisy periodic structure qua PPS và đặt measurement-origin question; 2022 cho thấy độ ổn định theo length phụ thuộc **statistic**, với một bộ methods khác. [2018-E01, E06, E10; 2022-E01, E03–E06, E12]

Điểm chung là dùng reconstructed dynamics và ý thức noise/real-data limitations. Điểm khác có ý nghĩa cho CSF là phân biệt **evidence about properties**, **evidence against a null**, **interpretation of chaos**, **interpretation of physiological origin**, và **relative accuracy of an estimator**. Không có loại bằng chứng nào trong số đó tự động thay thế các loại khác. [2015-E04–E11; 2018-E06–E11; 2022-E05–E10; nhận xét phân tích]

## 6. Critical Scientific Synthesis

### A. Ba bài đã xác lập thuyết phục điều gì trong phạm vi dữ liệu của chúng?

1. **Nonlinear time-series tools có thể khai thác nhiều thuộc tính khác nhau của measured PPG**, gồm finite-horizon prediction, nearby-trajectory divergence, local-flow continuity và recurrence-line organization. Các bài có kết quả tương ứng để kiểm tra, không chỉ đề xuất phương pháp trên lý thuyết. Điều này hỗ trợ một framework đa góc nhìn; không khẳng định các descriptors hoàn toàn độc lập hoặc đều đo một latent quantity tên “chaos”. [2015-E04–E09; 2018-E04–E09; 2022-E05, E09]
2. **Prediction-based surrogate comparisons có tiền lệ trực tiếp trên PPG.** 2015 kiểm tra một spectral-preserving linear Gaussian null; 2018 thêm noisy-periodic/PPS null. Các comparisons cho thấy original prediction phân biệt với surrogate ensembles được sử dụng. Đây là evidence against specified nulls trong study, không universal evidence against stochasticity. [2015-E09; 2018-E06–E07]
3. **Acquisition context cần được mô tả:** NIR và green PPG có reconstructed/prediction/divergence characteristics được so sánh ở 2018. Các kết quả cho thấy measurement modality là một consideration thực tế khi diễn giải PPG dynamics, dù design chưa tách riêng nguyên nhân wavelength/geometry/site. [2018-E02–E03, E08, E10–E11; analytical qualification]
4. **Recording length ảnh hưởng khác nhau lên RQA statistics.** Không thể lấy sự ổn định của DET hoặc ENTR để kết luận L hoặc Lmax ổn định cùng length. 2022 đưa error curves và feature-specific numerical limits cho NIR reference data. [2022-E06–E10]

### B. Những claim nào vẫn conditional hoặc method-dependent?

| Claim | Điều nguồn thực sự cho | Điều chưa được thiết lập | Hệ quả khi viết Introduction |
|---|---|---|---|
| “PPG là deterministic chaos” | Authors 2015/2018 kết luận chaos bằng combined evidence. [2015-E11; 2018-E09–E11] | Universal determinism across subjects/sensors/states; loại trừ mọi stochastic explanation | Dẫn bằng “reported evidence interpreted as compatible with chaotic dynamics”, hoặc thuật authors’ claim có phạm vi |
| “Positive LLE chứng minh chaos” | Positive estimates, kèm warnings noise/false positives. [2015-E04; 2018-E08] | Proof of deterministic invariant/exponential regime under all estimator choices | Trong manuscript giữ finite-data local-divergence descriptor |
| “Surrogate rejection chứng minh determinism” | Discrimination với defined linear/PPS ensembles. [2015-E09; 2018-E06–E07] | Rejection của tất cả stochastic/colored/nonstationary alternatives | Gắn mọi câu rejection với tên null và statistic |
| “RQA DET đo physical determinism” | Diagonal-line fraction; tác giả liên hệ determinism. [2022-E05] | Mapping duy nhất từ DET tới governing deterministic equations | Viết recurrence organization/diagonal structure, giải thích tên DET khi cần |
| “Upper-layer physiology là origin duy nhất của chaos” | Authors 2018 đề xuất upper-layer contribution và tự nêu ambiguity rPPG. [2018-E10–E11] | Causal isolation, independently measured capillary/pressure/volume dynamics | Chỉ dùng “suggested/considered a contribution”, hoặc bỏ khỏi Paragraph 2 nếu không cần |
| “Short PPG luôn sufficient cho NTSA” | 2022 có thresholds riêng cho four RQA features. [2022-E09–E10] | Simplex/Rosenstein/LAM/TT reliability ở mọi states/parameters | Nêu feature-specific reliability và lý do sensitivity checks |
| “L của RQA = direct forecast skill” | L liên quan persistence của nearby recurrence diagonals. [2022-E05] | Quantitative equivalence với out-of-sample CC/NRMSE | Dùng hai perspectives bổ sung; không gọi chúng là cùng outcome |

Tất cả qualifications trên là **nhận xét phân tích**. Chúng không cáo buộc các tác giả sai hay phủ nhận usefulness của study; chúng giới hạn điều có thể chuyển hợp lệ sang một manuscript với mục tiêu khác.

### C. Những bài học phương pháp manuscript nên kế thừa

1. **Chọn và công bố null rõ.** RQ1 nên hỏi organization beyond the **tested noisy pseudoperiodic null**, với PPS construction/configuration và statistics được định nghĩa; không dùng “chaos detected” như synonym cho reject. Tiền lệ 2018 hỗ trợ test rationale, không cấp sẵn calibration cho window/state của dataset hiện tại. [2018-E06–E07]
2. **Tách property descriptors.** Simplex Mean CC/Mean NRMSE, DET/Lmean/LAM/TT và Rosenstein estimate phản ánh ba constructions khác nhau. Nghiên cứu trước cho lý do cần nhiều perspectives nhưng không chứng minh chúng sẽ cùng direction giữa Awake và Drowsy. [2015-E03–E11; 2018-E06–E10; 2022-E05]
3. **Reconstruction cần phù hợp dữ liệu.** Ba papers dùng delay rules khác nhau; m = 4 trong literature không phải lý do đủ để cố định m cho mọi input. Report delay/dimension selection và kiểm tra sensitivity có ích vì algorithms dựa reconstructed distances. [2015-E04; 2018-E03, E08; 2022-E04]
4. **Phân biệt recording duration và forecast horizon.** 5-min input trong 2015/2018 vẫn có short-horizon prediction; điều đó không validate 60 s input. 2022 cho thấy input length reliability cần kiểm tra riêng theo feature. [2015-E02, E06; 2018-E02, E06; 2022-E06–E10]
5. **Sensitivity theo length phải feature-specific.** 30/60/120/180 s analyses trong manuscript có scientific motivation từ 2022; vẫn cần dữ liệu/analysis của manuscript để xác lập stability cho từng descriptor, nhất là Lmean, LAM/TT và Rosenstein. Bài 2022 chưa chứng nhận cutoffs cho các metrics không được họ đánh giá. [2022-E05, E09–E11]
6. **Report preprocessing và quality assumptions.** Noise/filtering có thể làm thay đổi estimates; chỉ dẫn tên NTSA không đủ để replicate. Một mô tả đầy đủ về input representation và estimator settings giúp tránh transferring results giữa raw/filtered series thiếu căn cứ. [2015-E04, E11–E12; 2018-E08, E12; 2022-E01, E10–E11]
7. **Giới hạn inferential unit.** Repeats/windows không tự trở thành independent participants. Cross-state conclusions cần phù hợp repeated-session/subject structure của manuscript; ba papers không cung cấp statistical design sẵn cho contrast đó. [2015-E02; 2018-E02; 2022-E02; analytical lesson]
8. **Giữ inference theo physiological-state comparison.** Nếu analysis so sánh labeled Awake và Drowsy windows, kết quả là association/difference giữa states. Không chuyển thành một continuous transition mechanism hoặc causal pathway chỉ vì title dùng “transition”. Ba sources không cung cấp cơ chế chuyển trạng thái này. [2015-E12; 2018-E12; 2022-E11; analytical lesson theo manuscript context]

### D. Những thuộc tính/comparisons chưa trực tiếp được ba bài khảo sát

Trong ba PDF không thấy **Awake–Drowsy contrasts**, đồng thời phân tích **explicit Simplex forecastability + DET/Lmean/LAM/TT + Rosenstein divergence** giữa physiological states, hoặc PPS testing của tất cả nhóm descriptors trong non-overlapping 60 s windows với sensitivity 30/120/180 s. Không thấy **LAM/TT** được đánh giá, hay validation của Rosenstein/explicit Simplex theo input length ở 2022. [2015-E12; 2018-E12; 2022-E05, E11]

Đây là statement về **scope của ba nguồn**, không một systematic-literature absence claim. Noise-sensitive estimates, local predictability hoặc direct Rosenstein application **không** phải những thứ hoàn toàn chưa từng nghiên cứu: chúng đã có trong 2015/2018 như mô tả ở trên. [2015-E04–E06; 2018-E06–E08]

### E. Các bài có điều tra thay đổi complementary dynamics giữa Awake và Drowsy không?

**Không trong ba nguồn được cung cấp.** Các acquisition protocols là healthy resting/reference settings. Bài 2018 có green–NIR measurement comparison, không phải Awake–Drowsy contrast; việc các Introduction/Conclusion đề cập mental-health hoặc sleep-related applications không biến chúng thành state experiments trong study. [2015-E02, E11–E12; 2018-E01–E02, E11–E12; 2022-E01–E02, E11]

### F. Các bài có trực tiếp so sánh forecastability, recurrence organization và local divergence across physiological states không?

**Không.** 2015/2018 có prediction và LLE; 2022 có RQA diagonal features. Không bài nào có combined three-perspective **state comparison** như design của manuscript. L trong 2022 có predictability interpretation nhưng không direct forecastability measurement; Poincaré trong 2015 không phải RQA. [2015-E05–E07, E12; 2018-E06–E08, E12; 2022-E05, E11]

### G. Khoảng trống hợp lệ có thể được motivate?

Ba studies motivate việc **empirically characterize** complementary descriptors trong short state-labeled PPG và kiểm tra organization against an explicit noisy pseudoperiodic null, đồng thời kiểm tra dependence theo window duration/estimator choices. Chúng cung cấp methodological rationale, nhưng chưa trả lời RQ1/RQ2 của manuscript. Gap này được hỗ trợ **specifically by these three papers**. [2018-E06–E08; 2022-E06–E11; đối chiếu 2015-E12, 2018-E12]

### H. Những gap statements nào misleading?

- “Chưa nghiên cứu nonlinear predictability/LLE của PPG”: trái với 2015/2018. [2015-E04–E06; 2018-E06–E08]
- “PPG chưa từng được PPS tested”: trái với 2018. [2018-E06–E07]
- “Recording length chưa từng được khảo sát”: trái với 2022. [2022-E06–E10]
- “Các bài trước chỉ dùng positive LLE để chứng minh chaos”: bỏ qua DNP, Wayland, surrogates, Poincaré và 0–1 tests. [2015-E03–E11; 2018-E03–E09]
- “NTSA chưa từng liên quan physiological/mental conditions”: không thể kết luận từ ba bài; chính sources cite prior health/state applications. Việc ba studies không làm Awake–Drowsy không phủ nhận toàn literature. [2015-E01, E11; 2018-E01; 2022-E01]
- “Manuscript sẽ chứng minh cơ chế chaos khi chuyển sang drowsiness”: vượt RQs, dữ liệu state comparison và limitations do người dùng cung cấp; ba sources không hỗ trợ inference đó. [2015-E12; 2018-E12; 2022-E11; manuscript context]

## 7. Defensible Research Gap

### Gap được hỗ trợ specifically by these three papers

**G1 — empirical physiological-state characterization.** Ba papers characterise healthy/reference PPG, measurement-modality differences và length-dependent RQA reliability, nhưng không trực tiếp xác lập how complementary PPG descriptors differ between Awake and Drowsy. Vì vậy chúng tạo rationale cho một nghiên cứu trạng thái có thiết kế rõ. **Không được đổi thành** “no previous study anywhere has compared PPG dynamics across wakefulness and drowsiness”. [2015-E02, E12; 2018-E02, E12; 2022-E02, E11]

**G2 — complementary descriptors trong cùng empirical question.** 2015/2018 cung cấp prediction/divergence evidence, 2022 recurrence/length evidence; không có combined comparison của explicit Simplex CC/NRMSE, DET/Lmean/LAM/TT và Rosenstein estimates across Awake/Drowsy trong ba nguồn. Novelty dự kiến là characterization/evidence dưới một framework, không invention của Simplex, RQA hoặc Rosenstein. [2015-E04–E07; 2018-E06–E08; 2022-E05, E11; analytical formulation]

**G3 — null-specific evaluation trên short state windows.** 2018 đã có PPS prediction test trên gPPG. Câu hỏi còn mở trong ba studies là kết quả organization relative to a specified noisy pseudoperiodic null trong short Awake/Drowsy windows và theo các descriptors của manuscript. Không dự đoán trước reject ở cả hai states và không gọi đây là lần đầu tiên PPS được dùng cho PPG. [2018-E02, E06–E07, E12; 2022-E11]

**G4 — robustness của state-level characterization khi thay đổi duration.** 2022 cho thấy different RQA features cần different lengths và giới hạn modality/setting. Điều này motivate window-duration sensitivity của manuscript, nhưng không trực tiếp validate 30/60/120/180 s choices cho mọi metric và không bảo đảm RQ2 effect ổn định. [2022-E05, E09–E11]

### Gap cần broader literature verification

| Proposed claim | Trạng thái | Evidence cần bổ sung trước khi dùng |
|---|---|---|
| “First Awake–Drowsy PPG nonlinear study” | **Requires broader literature verification** | Nghiên cứu drowsiness/sleepiness/fatigue/sleep-transition trên PPG; không chỉ ba papers của cùng author group |
| “First combined Simplex–RQA–LLE study of PPG” | **Requires broader literature verification** | Cross-method PPG papers và equivalent method/statistic names |
| “First PPS test in ultra-short state-labeled PPG” | **Requires broader literature verification** | Pseudoperiodic/noisy-periodic surrogate studies với short segments và state labels |
| “60 s is sufficient/optimal for all chosen estimators” | **Not established from these sources; cần validation riêng** | Dataset-specific duration/reconstruction/noise sensitivity, không chỉ literature novelty search |
| “PPG dynamics during drowsiness have never been characterized” | **Requires broader literature verification** | Broad physiological/signal-processing literature, kể cả studies không dùng từ chaos hoặc NTSA |
| “These methods discover the mechanism of wakefulness-to-drowsiness transition” | **Unsupported by these sources and stated manuscript design** | Cần evidence/mechanistic design khác; không giải quyết bằng việc cite thêm ba sources |

**Formulation nên dùng ở mức ý tưởng:** previous PPG studies motivate nonlinear prediction/divergence analysis, explicit surrogate testing và feature-dependent recording-length checks; những contributions đó chưa trực tiếp trả lời empirical question về complementary short-window PPG descriptors trong Awake/Drowsy. Cần giữ scope “the studies reviewed here” nếu chưa có broader verification. Đây là outline nội dung, không phải final Introduction paragraph. [2015-E04–E12; 2018-E06–E12; 2022-E05–E11]

## 8. Introduction-Ready Evidence Table

Các defensible statements bên dưới là các đơn vị bằng chứng để xây Paragraph 2. Không nối chúng thành polished English prose. Confidence kế thừa evidence registry; “Citation suitability” đánh giá **mức hỗ trợ cho đúng statement trong hàng**, không mức uy tín chung của paper.

| Intended narrative role | Scientifically defensible statement | Supporting paper(s) | Exact page/section/figure evidence | Caveat/qualification | Citation suitability |
|---|---|---|---|---|---|
| Transition from Paragraph 1 | PPG có thể được khảo sát bằng nonlinear descriptors của prediction, trajectory divergence và recurrence organization | 2015/2018/2022 | 2015 PDF p.5 §3.3, pp.6–7 §3.4 Figures 5–6; 2018 pp.5–6 §3.4 Figure 7; 2022 p.6 §3.3, p.10 Figure 8/Table 3 | Chỉ nêu availability/usefulness của perspectives; không coi nonlinearity/chaos là đã universal established | **Direct support** [2015-E04–E06; 2018-E08; 2022-E05, E09] |
| Sviridova 2015 contribution | Healthy resting finger PPG được kiểm tra bằng multiple NTSA tools; có short-term predictability, positive Wolf estimates và prediction khác Fourier-phase surrogates | 2015 | PDF pp.3–4 §2.2; p.5 Table 2/§3.3; pp.6–7 Figures 5–6/§3.4; pp.9–10 Figure 9/§3.7 | Healthy young sample; không dùng PPS/Rosenstein; original authors diễn giải combined results compatible with chaotic motion | **Direct support** [2015-E02, E04–E06, E09–E11] |
| 2015 chaos interpretation | Authors interpreted combined findings as consistent with chaotic motion and compared them qualitatively with noisy Rössler single-band dynamics | 2015 | PDF pp.10–11 §§4–5; Figures 5/10 ở pp.6/10 | Đây là authors’ interpretation; không proof cho mọi PPG và không physiological equation identification | **Direct support** cho việc thuật interpretation [2015-E05, E10–E11] |
| Sviridova 2018 contribution | gPPG prediction được so với Fourier-phase và PPS ensembles để kiểm tra linear-Gaussian và uncorrelated-noise-driven-periodic nulls | 2018 | PDF pp.4–6 §3.3, Figures 5–6; ref. [45] p.9 | DNP CC/statistics trên data của study; không direct validation cho 60 s Awake/Drowsy | **Direct support** [2018-E06–E07] |
| 2018 divergence contribution | Study cũng sử dụng Rosenstein-type LLE trong so sánh green/NIR PPG, kèm cảnh báo noise-sensitive inference | 2018 | PDF pp.5–6 §3.4 Figure 7; Table 1 p.3; ref. [47] p.9 | Không viết mean difference có formal statistical significance; modality khác physiological state | **Direct support** [2018-E02, E08, E10] |
| 2018 physiological-origin contribution, nếu cần | Comparison g/r khiến tác giả đề xuất vai trò upper skin processes, nhưng nguồn complexity của rPPG chưa được phân giải duy nhất | 2018 | PDF pp.7–8 §§4–5 | Không direct causal experiment; wavelength/geometry/site/rate khác cùng lúc. Có thể bỏ khỏi Paragraph 2 nếu làm loãng trọng tâm dynamics/state | **Partial support** cho physiological-mechanism statement; **Direct support** cho authors’ proposal/uncertainty [2018-E02, E10–E11] |
| Sviridova 2022 contribution | Required recording length để tái hiện long-reference RQA estimates phụ thuộc feature; DET/ENTR ổn định trên length ngắn hơn L/Lmax trong studied NIR setting | 2022 | PDF pp.6–7 §3.4; p.10 §4.2 Figure 8/Table 3; pp.11–12 §5 | Relative-reference error, averages, modality/setting specific; không generic NTSA validity statement | **Direct support** [2022-E06, E09–E10] |
| Methodological synthesis | Forecastability/divergence và recurrence-based estimates cần được diễn giải với reconstruction, noise, null model và recording-length assumptions riêng | 2015/2018/2022 | 2015 p.5 §§3.2–3.3/p.9 §3.7; 2018 pp.4–7 §§3.3–3.5; 2022 p.5 §§3.1–3.2/pp.11–12 §5 | Là synthesis của các sources, không verbatim conclusion của một bài; không nói previous work ignored robustness | **Direct support** cho methodological rationale [2015-E04, E09; 2018-E06–E09; 2022-E04, E10] |
| Research gap | Ba studies không trực tiếp so sánh complementary short-window PPG descriptors giữa Awake/Drowsy | Cả ba, scope audit | 2015 pp.3–4 §2.2/pp.10–11 §§4–5; 2018 pp.2–3 §2.1/pp.7–8 §§4–5; 2022 pp.3–4 §2.2/pp.9–12 §§4.2–6 | Absence claim chỉ về three reviewed studies; universal novelty cần broader literature | **Direct support** cho limited-scope gap [2015-E12; 2018-E12; 2022-E11] |
| Link to RQ1 | Tiền lệ PPS motivates hỏi short state-labeled PPG có organization beyond the **specified noisy pseudoperiodic null** hay không | 2018, manuscript context | PDF pp.4–6 §3.3 Figures 5–6 | RQ của manuscript là extension; source không xác lập outcome của dataset hiện tại | **Partial support** cho research motivation, không kết quả [2018-E06–E07] |
| Link to RQ2 | Prediction/divergence và RQA length evidence motivates khảo sát association của complementary descriptors với Awake/Drowsy | 2015/2018/2022, manuscript context | 2015 pp.5–7 §§3.3–3.4; 2018 pp.5–6 §3.4; 2022 p.6 §3.3/p.10 Table 3 | Không previous-state-result support; không direction prediction, diagnosis hoặc continuous-transition mechanism | **Partial support** cho motivation; **Context only** cho specific state relation [2015-E04–E06; 2018-E08; 2022-E05, E09] |
| Universal novelty claim | “This is the first study worldwide…” | Không có supporting source trong corpus này | Không có evidence location hợp lệ | Không suy ra universal absence từ ba studies | **Unsupported** |

**Statements có thể dùng an toàn, dưới dạng ý tưởng và với citations:**

- Nonlinear PPG studies trước đã xem xét forecastability và nearby-trajectory divergence. [2015-E04–E06; 2018-E06, E08]
- 2018 dùng cả phase-randomized và pseudoperiodic surrogates để đánh giá prediction dưới hai nulls cụ thể. [2018-E06–E07]
- 2022 cho thấy recording-length requirements khác giữa RQA features trong controlled NIR data. [2022-E09–E10]
- Ba studies được audit không trực tiếp trả lời complementary-dynamics comparison giữa Awake và Drowsy. [2015-E12; 2018-E12; 2022-E11]

**Statements cần wording có điều kiện:** reported evidence compatible with chaotic dynamics; proposed upper-layer contribution; average recording-length requirements relative to reference; potential usefulness cho health monitoring; rationale for short-window/state analyses. Không coi chúng là unconditional physiological truths hoặc validated clinical outcomes. [2015-E11; 2018-E10–E11; 2022-E09–E10]

**Chi tiết phù hợp Methods/Discussion hơn Introduction:** specific PF/delay rule, FNN settings, m-sweeps, Wolf/Rosenstein fit choices, PPS generator parameters, library/test separation, Theiler window, ε definition, lmin/identity-line handling, exact cutoff tables, θ grid discrepancy và Table/Discussion numeric mismatches. Paragraph 2 chỉ cần enough detail để hiểu contributions và inferential limits. Những missing settings phải được report trong manuscript's Methods, không chép từ literature như đã established. [2015-E04–E12; 2018-E03–E12; 2022-E03–E12; editorial analytical recommendation]

## 9. Statements to Avoid or Qualify

| Tránh hoặc qualify | Vì sao | Hướng sửa ở mức nội dung |
|---|---|---|
| “All three papers prove PPG is chaotic” | 2022 nghiên cứu RQA relative-error, không new chaos identification; 2015/2018 authors’ claims không universal proof. [2015-E11; 2018-E11; 2022-E01, E11] | Phân biệt observations, authors’ interpretation và estimator study |
| “2015 and 2018 used the same LLE algorithm” | **Wolf 2015, Rosenstein 2018**. [2015-E04; 2018-E08] | Ghi đúng estimator nếu chi tiết cần cho narrative |
| “2015 performed PPS testing” | Chỉ phase-randomization application; cited PPS paper không nghĩa applied PPS. [2015-E09, E12] | PPS contribution cite **2018** |
| “Sviridova validated Simplex Projection/Mean NRMSE for PPG” | Không xác lập explicit Simplex; 2015 dùng CC/RRMSE, 2018 CC; 2022 L không direct forecast statistic. [2015-E05–E06, E12; 2018-E06, E12; 2022-E05] | Dẫn nonlinear prediction ở mức method family, cite algorithm origin riêng nếu cần |
| “Poincaré recurrence in 2015 was RQA” | Methods khác nhau; no RP/RQA estimates. [2015-E07, E12] | Dùng “qualitative reconstructed trajectory/Poincaré structure” |
| “RQA DET above 0.9 establishes determinism” | Ngưỡng diễn giải theo literature trong bài; statistic không một physical proof. [2022-E05] | Nêu diagonal recurrence organization, tách interpretation |
| “2022 established reliable LLE on 2.44/60 s PPG” | 2.44 s cutoff là **DET**; bài không tính Rosenstein LLE. [2022-E05, E09–E11] | Length result gắn đúng feature |
| “All NTSA features are accurate to <1% on 60 s” | L của 2022 cần khoảng 105 s cho mean 1% cutoff; chưa đánh giá chosen Simplex/LLE/LAM/TT. [2022-E09–E11] | Feature-specific sensitivity; không generic error guarantee |
| “The 2022 study used 30 participants/15 participants” | Text ghi 30 datasets; không xác lập independent participant count. [2022-E02, E11] | Giữ **30 datasets** |
| “2018 compares physiological states” | Comparison chủ yếu green/NIR measurement modalities trên resting recordings. [2018-E02, E10, E12] | Ghi measurement condition đúng |
| “gPPG is significantly more chaotic than rPPG” | Descriptive means/interpretations; no formal significance test, no consistent subject-independent LLE direction. [2018-E08, E10] | Report qualitative/prediction comparison và uncertainty |
| “2018 proves the upper dermis is the sole chaos generator” | Authors giữ ambiguity về rPPG; thiết kế không causal isolation. [2018-E02, E10–E11] | Proposed contribution, không exclusive mechanism |
| “Gaussian noise does not affect DNP” | Authors suggest từ surrogate results; không controlled estimator-noise calibration trên PPG. [2015-E09, E11] | Report null discrimination, qualify noise interpretation |
| “Filtering necessarily destroys all nonlinear information” | 2022 discusses potential alteration và future alternatives, không chứng minh mọi filter/mọi dataset đều unusable. [2022-E01, E10] | Filtering **may alter** nonlinear features; cần validation representation riêng |
| “PPS rejection rules out stochastic PPG” | Null là uncorrelated noise-driven periodic orbit trong 2018, không mọi stochastic model. [2018-E06–E07] | Reject the specified tested null |
| “State differences demonstrate a continuous transition mechanism” | Không nằm trong source evidence; state comparisons trong manuscript không tự nhận diện mechanism | Mô tả association/difference giữa labeled states, theo manuscript limitations |
| “We introduce new Simplex/RQA/Rosenstein algorithms” | Sources đã dùng NTSA families; manuscript context xác định empirical characterization là novelty chính | Tập trung empirical characterization/framework, không algorithm invention |
| “Nobody has studied nonlinear PPG in drowsiness” | Three-source scope không đủ universal literature claim | Giới hạn three reviewed studies hoặc verify broader literature |

**Không dùng các số của mô phỏng như số của PPG.** CC >0.96/RRMSE <0.28 trong 2015 mô tả noiseless Rössler, WTE 1.08 là white-noise benchmark, và θ = 0.245/0.5 trong 2022 là simulated noise coefficients. Không dùng những số đó để mô tả awake/drowsy physiology hoặc estimator accuracy của manuscript. [2015-E06, E08; 2022-E03, E07]

## 10. Outstanding Questions and Verification Needs

### Những chi tiết chưa được xác lập từ các PDF

| Câu hỏi | Source/status | Ý nghĩa và cách dùng trong manuscript |
|---|---|---|
| DNP 2015/2018 có đúng là Simplex? | **Not established from the provided source**; [2015-E12; 2018-E12] | Chỉ cite prediction-family contribution; cần separate primary algorithm citation và manuscript implementation details |
| Công thức RRMSE 2015 có cùng denominator với manuscript NRMSE? | **Not established**; [2015-E05–E06, E12] | Không equate numerical values hoặc names |
| PPS 2018 dùng radius/neighborhood/initialization và diagnostics nào? | **Not established đầy đủ**; [2018-E06–E07, E12] | Cần original PPS algorithm paper/code hoặc author clarification nếu replicate; manuscript công bố cấu hình riêng |
| Formal rank p-values, α và multiplicity của surrogate decisions? | **Not established đầy đủ** ở 2015/2018; [2015-E09, E12; 2018-E06–E07, E12] | Không chế ra p-value từ N surrogates; report current inference procedure riêng |
| Wolf/Rosenstein Theiler separation và fit-selection details? | **Not established đầy đủ**; [2015-E04, E12; 2018-E08, E12] | Không gọi direct numerical replication/equivalence khi chưa có settings |
| Preprocessing/filtering thực tế của ba datasets? | **Not established đầy đủ**; [2015-E12; 2018-E11–E12; 2022-E11] | Không diễn giải “không được mô tả” thành “không filtering”; giữ uncertainty |
| Participant count/unique records và repetition structure của 2022? | **Not established**; [2022-E02, E11] | Không viết n = 30 people hoặc n = 15 people |
| LED wavelength và exact acquisition site của 2022? | **Not established**; [2022-E02, E11] | Không nhập wavelength/site từ 2018 hoặc schematic Figure 1 |
| 2022 lmin/Theiler window/identity-line treatment/ε theo length? | **Not established đầy đủ**; [2022-E04–E06, E11] | Quan trọng nếu transfer reliability cutoffs; không quy kết method error khi chưa rõ |
| 2022 PPG có dùng đúng 100 segments/length như Rössler? | **Not established rõ** cho PPG; [2022-E07–E08, E11] | Chỉ gắn 100 với simulated-system protocol khi trích |
| T của PPG reference có phải toàn bộ 5 min không? | §3.4 cho reference assumption >100 cycles; §4.2 phân tích tới ~122 s. **Không đủ để gọi toàn bộ 5 min là reference cho Table 3**. [2022-E06, E08–E09] | Phân biệt acquisition length và analysed reference range |
| Vì sao 3.8 s ENTR example không khớp Table 3 7.62 cycles cho 5%? | **Unresolved in PDF**; [2022-E09–E10] | Không dùng làm key Introduction threshold; cần code/author clarification nếu replicate |
| Vì sao θ grid/0.245 và FNN reference chưa khớp? | **Unresolved in PDF**; [2022-E03, E07, E12] | Giữ nguyên evidence; không silently correct |
| Three datasets có overlap participants/records? | **Not established đầy đủ**; [2015-E02; 2018-E02; 2022-E02, E11] | Không gọi contributions là independent replications nếu chưa verify |

### Những verification cần cho claims vượt phạm vi ba nguồn

1. **Broader novelty verification** trước bất kỳ “first”, “never”, “no previous studies” statement về short PPG, drowsiness, combined NTSA hoặc PPS. Audit này không thực hiện systematic literature search, nên không cung cấp universal novelty verdict.
2. **Dataset-specific robustness** cho manuscript: input duration, reconstruction, nearest-neighbor exclusions, forecast evaluation và divergence fit regime; reliability của recurrence vertical features LAM/TT cần evidence riêng vì 2022 không đánh giá chúng.
3. **Null-model validity/quality**: mức preserving pseudoperiodicity và statistic distributions của PPS trên từng representation/window; reject/non-reject cần gắn với generator và actual hypothesis.
4. **State-inference design**: quality/labeling và dependence của recordings; comparison Awake–Drowsy là empirical association, không diagnosis hoặc mechanistic progression nếu design không hỗ trợ.

Các mục 2–4 là recommendations từ critical synthesis và manuscript context, không các kết quả mới hoặc yêu cầu tác giả nguồn đã đặt ra. Các công trình được các PDF cite nhưng không được cung cấp không được audit sâu ở đây; bài này không thay thế việc đọc primary sources của Simplex, PPS, Rosenstein hoặc broader state literature.

## 11. Recommended Paragraph 2 Narrative Structure

Đây là **logical sequence**, không polished English prose và không final Introduction paragraph.

1. **Nối từ Paragraph 1:** sau khi xác lập PPG là observed physiological waveform, chuyển sang câu hỏi temporal/dynamical organization; giới thiệu nonlinear perspectives bằng từ dễ hiểu cho nonlinear-dynamics researchers không chuyên PPG. Tránh dùng “PPG is proven chaotic” như tiền đề. Evidence: 2015 pp.5–7 §§3.3–3.4; 2022 p.6 §3.3. [2015-E04–E06; 2022-E05]
2. **Đóng góp 2015:** nêu multi-method assessment của healthy resting PPG; chọn finite-horizon prediction và trajectory divergence làm chi tiết chính; nếu nhắc chaos, đánh dấu authors’ interpretation và noise caveat. Không liệt kê mọi technical parameter. [2015-E02, E04–E06, E09–E11]
3. **Đóng góp 2018:** nêu prediction với explicit surrogate nulls, đặc biệt PPS; có thể thêm Rosenstein divergence và green/NIR comparison nếu cần. Không biến modality comparison thành state comparison. [2018-E02, E06–E08]
4. **Đóng góp 2022:** chuyển sang giới hạn practical recording length; nêu RQA reliability phụ thuộc feature, short length không có cùng implication cho DET/ENTR và L/Lmax. Dùng qualitative distinction thay exact seconds trong đoạn Introduction nếu không cần. [2022-E05–E10]
5. **Methodological synthesis:** từ ba contributions rút ra cần kết hợp complementary descriptors, explicit null interpretation và feature-specific length/reconstruction checks. Nêu ngắn gọn đây là khảo sát properties của observed data, không automatic chaos proof. [2015-E04, E09; 2018-E06–E08; 2022-E06, E09–E10]
6. **Khoảng trống có scope:** the studies reviewed here chưa trực tiếp characterise complementary short-window descriptors giữa Awake và Drowsy. Không khẳng định toàn literature chưa có nghiên cứu đó; nếu muốn universal novelty, bổ sung broader verification trước. [2015-E12; 2018-E12; 2022-E11]
7. **Nối RQ1/RQ2:** motivate hai câu hỏi: organization beyond tested noisy pseudoperiodic null; association của forecastability, recurrence organization và local divergence với physiological states. Giới thiệu 60 s với duration sensitivity ở đoạn design phù hợp; không tuyên bố nguồn 2022 đã validate toàn bộ chosen metrics ở 60 s. [2018-E06–E08; 2022-E09–E11; manuscript context]

**Trọng tâm CSF nên giữ:** empirical dynamical characterization, assumptions của reconstructed-data analysis và null-specific inference. Physiological-state context tạo câu hỏi ứng dụng, còn contribution chính là evidence về complementary dynamics và robustness trong dữ liệu đó; không cần khẳng định deterministic chaos hoặc đề xuất algorithm mới để có một rationale khoa học rõ.

