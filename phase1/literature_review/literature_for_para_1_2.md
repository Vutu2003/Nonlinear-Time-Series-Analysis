
### 1.Amidei et al. (2021)
- **Tên tác giả**: Alberto Amidei, Pier Giorgio Fallica, Sabrina Conoci, Paolo Pavan
- **Tên bài báo**: *Validating photoplethysmography (PPG) data for driver drowsiness detection*
- **Hội thảo**: *2021 IEEE International Workshop on Metrology for Automotive (MetroAutomotive)*, trang 147–151 (2021)
- **DOI / Link**: [10.1109/MetroAutomotive50197.2021.9545855](https://doi.org/10.1109/MetroAutomotive50197.2021.9545855)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Đo tín hiệu quang thể tích đồ (PPG) qua cảm biến tiếp xúc da.
  - *Xử lý & Mô hình*: Phân tích hình thái sóng xung mạch (Pulse Wave Analysis) và sự biến thiên thể tích máu; đánh giá và kiểm chứng định lượng độ tin cậy của PPG so với các chỉ số sinh lý chuẩn trong bài toán phát hiện buồn ngủ.


### 2.Cao et al. (2023)
- **Tên tác giả**: Yimeng Cao, Fan Li, Xuxin Liu, Song Yang, Yu Wang
- **Tên bài báo**: *Towards reliable driver drowsiness detection leveraging wearables*
- **Tạp chí**: *ACM Transactions on Sensor Networks*, Tập 19, Số 2, trang 1–23 (2023)
- **DOI / Link**: [10.1145/3546067](https://doi.org/10.1145/3546067)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Vòng đeo tay FDWatch tích hợp PPG hai bước sóng, cảm biến gia tốc (đo cử động xoay vô-lăng) và theo dõi nhịp sinh học trên 10 tài xế thực địa.
  - *Xử lý & Mô hình*: Trích xuất nhịp ngáp từ phép biến đổi bình phương PPG hai bước sóng và tính HRV; dùng mạng BPNN tính xác suất tin cậy và Lý thuyết bằng chứng Dempster-Shafer (DST) để dung hợp quyết định.


### 3.Lu et al. (2024)
- **Tên tác giả**: Yu Lu, Xiang Yang, Hong Wei, Jun Liu, Bo Li
- **Tên bài báo**: *Driver fatigue detection using PPG signal, facial features, head postures with an LSTM model*
- **Tạp chí**: *Heliyon*, Tập 10, Số 21, Mã bài e39479 (2024)
- **DOI / Link**: [10.1016/j.heliyon.2024.e39479](https://doi.org/10.1016/j.heliyon.2024.e39479)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Thực nghiệm trên 30 tài xế lái xe thực tế trên cao tốc Dalian–Shenyang thu tín hiệu PPG, khuôn mặt và tư thế đầu.
  - *Xử lý & Mô hình*: Trích xuất véc-tơ dung hợp 10 chiều gồm đặc trưng HRV từ PPG (SDNN, RMSSD, LF/HF) kết hợp đặc trưng mắt/miệng (EAR, MAR) và góc xoay đầu (pitch, roll, yaw); phân loại bằng mạng LSTM 2 lớp tối ưu hóa bằng Adam.

### 4.Siyang et al. (2024)
- **Tên tác giả**: Siyang Hu, Qian Gao, Kai Xie, Cong Wen, Wei Zhang, Jing He
- **Tên bài báo**: *Efficient detection of driver fatigue state based on all-weather illumination scenarios*
- **Tạp chí**: *Scientific Reports*, Tập 14, Số 1, Bài số 17075 (2024)
- **DOI / Link**: [10.1038/s41598-024-67891-9](https://doi.org/10.1038/s41598-024-67891-9)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Video hồng ngoại và ánh sáng thường của khuôn mặt tài xế trong điều kiện chiếu sáng biến đổi (ngày, đêm, ngược sáng).
  - *Xử lý & Mô hình*: Trích xuất rPPG từ video hồng ngoại tính HRV kết hợp đặc trưng khuôn mặt cắt bằng MTCNN; ứng dụng mạng Tái cấu trúc Đa hàm mất mát (MLR) để giảm dư thừa dữ liệu và Bi-LSTM để bắt động lực học thời gian.

### 5.Tsai et al. (2024)
- **Tên tác giả**: Cheng-Yi Tsai, Hsiang Cheong, Robert Houghton, Wei-Hsuan Hsu, Kuo-Yi Lee, Jenn-Haung Kang, Yi-Chun Kuan, Hsin-Ching Lee, Wan-Chun Cheng-Jung, Li-Ying J. Li, et al.
- **Tên bài báo**: *Predicting fatigue-associated aberrant driving behaviors using a dynamic weighted moving average model with a long short-term memory network based on heart rate variability*
- **Tạp chí**: *Human Factors*, Tập 66, Số 6, trang 1681–1702 (2024)
- **DOI / Link**: [10.1177/00187208221142828](https://doi.org/10.1177/00187208221142828)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Thu chuỗi HRV (SDNN, RMSSD, nHF) qua đồng hồ thông minh từ 20 tài xế xe buýt đô thị/đường dài trong 4 ngày thực tế, ghi nhận hành vi bất thường (ADB) qua ứng dụng GPS.
  - *Xử lý & Mô hình*: Dùng mô hình Trung bình động có trọng số động (DWMA) xử lý các cửa sổ HRV 5 phút trước sự kiện và huấn luyện mạng LSTM để dự báo hành vi lái xe bất thường do mệt mỏi.


### 6.Fujiwara et al. (2019)
- **Tên tác giả**: Koichi Fujiwara, Emi Abe, Kenta Kamata, Chika Nakayama, Yoko Suzuki, Toshitaka Yamakawa, Takashi Hiraoka, Michihiro Kano, Yoko Sumi, Futoshi Masuda, Masahiro Matsuo, Hiroshi Kadotani
- **Tên bài báo**: *Heart rate variability-based driver drowsiness detection and its validation with EEG*
- **Tạp chí**: *IEEE Transactions on Biomedical Engineering*, Tập 66, Số 6, trang 1769–1778 (2019)
- **DOI / Link**: [10.1109/TBME.2018.2879346](https://doi.org/10.1109/TBME.2018.2879346)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Thu chuỗi R-R interval (RRI) từ cảm biến ECG dạng đeo kết hợp ghi EEG đối chứng trên 34 người tham gia lái xe mô phỏng.
  - *Xử lý & Mô hình*: Chia epoch 30 giây; trích xuất 8 chỉ số HRV (MeanNN, SDNN, RMSSD, Total Power, NN50, LF, HF, LF/HF). Áp dụng thuật toán Kiểm soát quá trình thống kê đa biến dựa trên PCA (MSPC-PCA) để phát hiện sớm đợt buồn ngủ pre-N1 với độ nhạy 92% và tỷ lệ báo động giả thấp (1.7/giờ).

### 7.AlArnaout et al. (2025)
- **Tên tác giả**: Zakwan AlArnaout, Chamseddine Zaki, Yehia Kotb, Mouhammad AlAkkoumi, Nour Mostafa
- **Tên bài báo**: *Exploiting heart rate variability for driver drowsiness detection using wearable sensors and machine learning*
- **Tạp chí**: *Scientific Reports*, Tập 15, Bài số 24898 (2025)
- **DOI / Link**: [10.1038/s41598-025-08582-2](https://doi.org/10.1038/s41598-025-08582-2)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Tín hiệu PPG (5Hz) thu từ vòng đeo Fitbit Charge 5, truyền qua Bluetooth 5.0 tới smartphone và máy chủ AWS EC2 [1]; bao gồm 6.300 đoạn PPG 30 giây từ 10 tài xế mô phỏng và 900 đoạn đối chứng từ 3 tài xế taxi [2, 3].
  - *Xử lý & Mô hình*: Phân đoạn và gán nhãn bằng ngưỡng nhịp tim lâm sàng (72.3–90.7 bpm) [4]; trích xuất 7 đặc trưng HRV qua ANOVA và RFE [5, 6]. Mô hình **Random Forest (RF)** đạt độ chính xác 86.05% (89.38% trên tập chung), F1-score 89.02%–91.91% với thời gian suy luận 12.3 ms/mẫu [1, 7, 8].


### 8.Hyeonjeong Lee et al. (2019)
- **Tên tác giả**: Hyeonjeong Lee, Joonsoo Lee, Minsik Shin
- **Tên bài báo**: *Using Wearable ECG-PPG Sensors for Driver Drowsiness Detection Based on Distinguishable Pattern of Recurrence Plots*
- **Tạp chí**: *Electronics*, Tập 8, Số 2, Bài số 192 (2019)
- **DOI / Link**: [10.3390/electronics8020192](https://doi.org/10.3390/electronics8020192)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Thu nhận chuỗi R-R interval (RRI) cửa sổ 2 phút từ 6 tài xế mô phỏng (22 bản ghi) bằng cảm biến đai ngực Polar H7 (ECG) và vòng đeo tay Microsoft Band 2 (PPG); gán nhãn Awake/Drowsy dựa trên video khuôn mặt và hành vi lái xe.
  - *Xử lý & Mô hình*: Chuẩn hóa RRI và biểu diễn thành 3 dạng ma trận lặp lại (Bin-RP, Cont-RP, ReLU-RP); huấn luyện mạng **CNN (tinh chỉnh từ VGG16)** để phân loại. Mô hình **ReLU-RP-CNN** đạt độ chính xác 70% (ECG) và 64% (PPG), vượt trội từ 4–17% so với các thuật toán ML truyền thống sử dụng đặc trưng RQA.

### 9. Charlton et al. (2023): little research on NTSA regarding PPG =--> gap
- **Tên tác giả**: Peter H. Charlton, John Allen, Raquel Bailón, Stephanie Baker, Joachim A. Behar, Fei Chen, Gari D. Clifford, Harry J. Davies, Cheng Ding, Xiaorong Ding, et al.
- **Tên bài báo**: *The 2023 wearable photoplethysmography roadmap*
- **Tạp chí**: *Physiological Measurement*, Tập 44, Số 11, Bài số 111001 (2023)
- **DOI / Link**: [10.1088/1361-6579/acead0](https://doi.org/10.1088/1361-6579/acead0)

### 10. Jiao et al. (2023)
- **Tên tác giả**: Yubo Jiao, Ce Zhang, Xiaoyu Chen, Liping Fu, Chaozhe Jiang, Chao Wen
- **Tên bài báo**: *Driver Fatigue Detection Using Measures of Heart Rate Variability and Electrodermal Activity*
- **Tạp chí**: *IEEE Transactions on Intelligent Transportation Systems*, Tập 25, Số 5, trang 3888–3898 (2024 / Online 2023)
- **DOI / Link**: [10.1109/TITS.2023.3333252](https://doi.org/10.1109/TITS.2023.3333252)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Thu tín hiệu PPG (64 Hz) và EDA (4 Hz) đồng thời qua vòng đeo tay Empatica E4 kết hợp tự đánh giá thang đo KSS trên tài xế mô phỏng đường sắt đô thị [1, 2].
  - *Xử lý & Mô hình*: Chia cửa sổ 5 phút (độ phủ 50%) [3]; trích xuất đặc trưng HRV (miền thời gian, tần số, phi tuyến) và 49 đặc trưng EDA [4-6]; áp dụng thuật toán SFS chọn đặc trưng [7]. Mô hình **LightGBM** đạt độ chính xác **88.7%** (nhị phân) và **Random Forest** đạt **85.6%** (phân loại 3 mức) [1].


### 11. Shoeibi et al. (2023)
- **Tên tác giả**: Fatemeh Shoeibi, Esmaeil Najafiaghdam, Afshin Ebrahimi
- **Tên bài báo**: *Nonlinear features of photoplethysmography signals for Non-invasive blood pressure estimation*
- **Tạp chí**: *Biomedical Signal Processing and Control*, Tập 85, Bài số 105067 (2023)
- **DOI / Link**: [10.1016/j.bspc.2023.105067](https://doi.org/10.1016/j.bspc.2023.105067)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Sử dụng tập dữ liệu con từ cơ sở dữ liệu MIMIC-II bao gồm 500 bản ghi tín hiệu PPG (125 Hz) và huyết áp động mạch xâm nhập (ABP) làm chuẩn đối chiếu, phân thành các đoạn 10 giây (hơn 28.000 đoạn PPG sạch sau tiền xử lý).
  - *Xử lý & Mô hình*: Khôi phục không gian pha 2D (Poincaré map) từ PPG với độ trễ (lag) 15 mẫu; trích xuất 101 đặc trưng phi tuyến từ 3 chuỗi thời gian giao điểm đường cắt Poincaré; dùng F-test chọn 73 đặc trưng tối ưu; phân loại/hồi quy huyết áp bằng **Gaussian Process Regression (GPR)** đạt MAE $0.79 \pm 3.08$ mmHg (SBP) và $1.38 \pm 4.53$ mmHg (DBP), đạt chuẩn Grade A (BHS) và đáp ứng tiêu chuẩn AAMI.

### 12. de Pedro-Carracedo et al. (2020)
- **Tên tác giả**: Javier de Pedro-Carracedo, David Fuentes-Jimenez, Ana P. Gonzalez-Marcos
- **Tên bài báo**: *Is the PPG Signal Chaotic?*
- **Tạp chí**: *IEEE Access*, Tập 8, trang 198038–198056 (2020)
- **DOI / Link**: [10.1109/ACCESS.2020.3034873](https://doi.org/10.1109/ACCESS.2020.3034873)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Tín hiệu PPG đo ở ngón tay trỏ tay trái (250 Hz) từ 40 sinh viên trẻ khỏe mạnh (dữ liệu thực tế lên tới 600.000 điểm / 40 phút) cùng các tín hiệu tham chiếu tổng hợp đại diện cho 5 loại động lực học (định kỳ, bán định kỳ, phi định kỳ, hỗn loạn Hénon map, ngẫu nhiên).
  - *Xử lý & Mô hình*: Xây dựng 2 kiến trúc Deep Neural Network (1D-ResNet CNN phân loại dạng động lực học ở thang thời gian nhỏ 5.000 điểm và lớn 60.000 điểm; RNN-LSTM dự báo chuỗi thời gian). Kết quả khẳng định ở thang thời gian nhỏ PPG chủ yếu có tính bán định kỳ (quasi-periodic), ở thang thời gian lớn xuất hiện động lực phi định kỳ (aperiodic) kết hợp thành phần ngẫu nhiên, và không phát hiện hành vi hỗn loạn (chaotic) đơn thuần.

### 13. Goshvarpour & Goshvarpour (2018)
- **Tên tác giả**: Atefeh Goshvarpour, Atefeh Goshvarpour
- **Tên bài báo**: *Poincaré’s section analysis for PPG-based automatic emotion recognition*
- **Tạp chí**: *Chaos, Solitons & Fractals*, Tập 114, trang 400–407 (2018)
- **DOI / Link**: [10.1016/j.chaos.2018.07.032](https://doi.org/10.1016/j.chaos.2018.07.032)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Tín hiệu PPG (512 Hz, lấy mẫu lại) từ 30 người tham gia trong cơ sở dữ liệu DEAP khi xem các đoạn video nhạc kích thích 3 trạng thái cảm xúc (Love, Hate, Fun).
  - *Xử lý & Mô hình*: Lọc Butterworth (0.6–30 Hz), chuẩn hóa và phân đoạn theo chu kỳ xung; tái thiết không gian pha 2D ($x_t$ vs $x_{t+4}$) và tạo các mặt cắt Poincaré theo các góc từ $0^\circ$ đến $360^\circ$ (bước $30^\circ$); trích xuất 10 chỉ số hình học (diện tích quỹ đạo, moment, độ lệch chuẩn, số điểm cắt); phân loại bằng **Support Vector Machine (SVM)** với hàm nhân Polynomial đạt độ chính xác tối đa **96.67%** (nhị phân: Love vs Hate) và **91.11%** (đa lớp).

### 14. Szczęsna et al. (2023)
- **Tên tác giả**: Agnieszka Szczęsna, Dariusz Rafał Augustyn, Henryk Josiński, Katarzyna Harężlak, Adam Świtoński, Paweł Kasprowski
- **Tên bài báo**: *Chaotic biomedical time signal analysis via wavelet scattering transform*
- **Tạp chí**: *Journal of Computational Science*, Tập 72, Bài số 102080 (2023)
- **DOI / Link**: [10.1016/j.jocs.2023.102080](https://doi.org/10.1016/j.jocs.2023.102080)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Bộ dữ liệu tín hiệu PPG (32 Hz, các đoạn 1000 mẫu / 31.2s) trong các hoạt động hàng ngày (đi bộ, đạp xe, đá bóng, v.v.), kết hợp dữ liệu cử động mắt (1000 Hz) và động học dáng đi (Vicon capture) cùng 13 hệ thống động lực học tổng hợp (5 hệ hỗn loạn như Rössler/Lorenz và 8 hệ phi hỗn loạn).
  - *Xử lý & Mô hình*: Áp dụng Biến đổi Wavelet Scattering (WST 2 tầng với sóng Gabor) để trích xuất đặc trưng bất biến dịch chuyển/co giãn từ các cửa sổ 125 mẫu; định nghĩa chỉ số đo độ hỗn loạn (chaos measure); huấn luyện mô hình **SVM (RBF kernel)** phân loại 2 lớp (chaotic / non-chaotic). Kết quả cho thấy WST-SVM phân loại hiệu quả tính hỗn loạn và chịu nhiễu tốt (đạt 99.88% trên tập tổng hợp), đồng thời chỉ số chaos measure ở PPG biến thiên rõ rệt theo từng loại hoạt động thể chất.

### 15. Hernández-Obín et al. (2026)
- **Tên tác giả**: David Hernández-Obín, Gertrudis Hortensia González-Gómez, Adriana Torres-Machorro, Claudia Lerma
- **Tên bài báo**: *Recurrence quantification analysis of photoplethysmography time series for assessing patients with peripheral artery disease*
- **Tạp chí**: *The European Physical Journal Special Topics*, trang 1–15 (2026 / Online May 2026)
- **DOI / Link**: [10.1140/epjs/s11734-026-02373-0](https://doi.org/10.1140/epjs/s11734-026-02373-0)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Chuỗi thời gian các thông số hình thái PPG (PTTp, MSS, Pulse Amplitude) và khoảng inter-beat (RR, pp) ghi nhận từ 40 chân của 25 bệnh nhân mắc bệnh động mạch ngoại biên (PAD), phân nhóm theo chỉ số Ankle-Brachial Index (Normal ABI $\ge 0.9$ vs Altered ABI $< 0.9$).
  - *Xử lý & Mô hình*: Tái thiết không gian pha ($m=3$, $\tau$ tối ưu) và phân tích định lượng ma trận lặp lại (**Recurrence Quantification Analysis - RQA**) tính toán Determinism, Mean/Max Diagonal Length, Entropy, Laminarity, Vertical Length; kiểm định Wilcoxon, Mann-Whitney U, Spearman và phân tích đường cong ROC. Kết quả chỉ ra động lực học RQA của PPG khác biệt đáng kể so với RR interval, trong đó các chỉ số RQA của $pp$ interval (như Max Diagonal Length, Laminarity, Max Vertical Length) có sự khác biệt có ý nghĩa thống kê giữa nhóm chân bình thường và tổn thương PAD, thể hiện giá trị chẩn đoán tiềm năng.



### 16. Liu et al. (2023)
- **Tên tác giả**: Kaipeng Liu, Yubo Jiao, Chen Du, Xiaoyu Zhang, Xiaoyu Chen, Fei Xu, Chaozhe Jiang
- **Tên bài báo**: *Driver Stress Detection Using Ultra-Short-Term HRV Analysis under Real World Driving Conditions*
- **Tạp chí**: *Entropy*, Tập 25, Số 2, Bài số 194 (2023)
- **DOI / Link**: [10.3390/e25020194](https://doi.org/10.3390/e25020194)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Tín hiệu ECG từ cơ sở dữ liệu PhysioNet của 17 tài xế lái xe thực tế tại Boston qua 3 kịch bản gây căng thẳng (nghỉ ngơi/thấp, cao tốc/trung bình, thành phố/cao) [1-3].
  - *Xử lý & Mô hình*: Chia các khung thời gian siêu ngắn (30-s, 1-min, 2-min, 3-min) đối chứng với khung chuẩn 5-min [3, 4]; trích xuất 22 đặc trưng HRV và chọn 4 đặc trưng đại diện tối ưu (MeanNN, SDNN, NN20, MeanHR) bằng kiểm định t-test, tương quan Spearman và phân tích Bland–Altman [4-6]. Phân loại mức độ căng thẳng bằng mô hình **SVM** đạt độ chính xác 85.3% (với cửa sổ 3 phút) và 85.0% (với cửa sổ 30 giây) [4, 7].


### 17. Awais et al. (2017)
- **Tên tác giả**: Muhammad Awais, Nasreen Badruddin, Micheal Drieberg [1]
- **Tên bài báo**: *A Hybrid Approach to Detect Driver Drowsiness Utilizing Physiological Signals to Improve System Performance and Wearability* [1]
- **Tạp chí**: *Sensors*, Tập 17, Số 9, Bài số 1991 (2017) [2]
- **DOI / Link**: [10.3390/s17091991](https://doi.org/10.3390/s17091991)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Tín hiệu 19 kênh EEG (Enobio-20) và 1 kênh ECG đeo ở cổ thu từ 22 sinh viên tham gia lái xe mô phỏng 80 phút trong kịch bản đường trường đơn điệu [3-5]; gán nhãn trạng thái Alert/Drowsy dựa trên quan sát video độc lập và đánh giá tự báo cáo theo thang đo KSS [6-8].
  - *Xử lý & Mô hình*: Cửa sổ phân tích 5 phút; trích xuất đặc trưng thời gian (mean, variance, sample entropy) và tần số (công suất tuyệt đối/tương đối các dải sóng) từ EEG [9-11], cùng các chỉ số HRV (LF, HF, LF/HF) từ ECG [12, 13]; dùng paired t-test chọn đặc trưng có ý nghĩa ($p < 0.05$) [14]; phân loại bằng **Support Vector Machine (SVM)** đạt độ chính xác 70.00% (chỉ ECG), 76.36% (chỉ EEG) và **80.90%** khi dung hợp EEG + ECG [15]; rút gọn cấu hình xuống 2 kênh (1 EEG + 1 ECG) vẫn duy trì độ chính xác 80.90% [16].

### 18. Peng et al. (2024)
- **Tên tác giả**: Yong Peng, Hong Deng, Guoliang Xiang, Xianhui Wu, Xizhuo Yu, Yingli Li, Tianjian Yu [17-19]
- **Tên bài báo**: *A Multi-Source Fusion Approach for Driver Fatigue Detection Using Physiological Signals and Facial Image*
- **Tạp chí**: *IEEE Transactions on Intelligent Transportation Systems*, Tập 25, Số 11, trang 16614–16624 (2024) [20]
- **DOI / Link**: [10.1109/TITS.2024.3420409](https://doi.org/10.1109/TITS.2024.3420409) [20]
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Camera Logitech C920 (30Hz) thu video toàn bộ khuôn mặt và đai đeo Empatica E4 thu tín hiệu BVP (32Hz), HR (1Hz), EDA (4Hz) từ 21 tài xế lái xe mô phỏng (tổng cộng 45.480 đoạn dữ liệu 3 giây) [21-24].
  - *Xử lý & Mô hình*: Khử nhiễu tín hiệu sinh lý bằng lọc Kalman [25]; theo dõi và phân đoạn khuôn mặt tự động bằng MTCNN và Linknet [26]; trích xuất đặc trưng sâu tự động bằng mạng dung hợp đa nguồn **1D CNN + 3D CNN** (không phụ thuộc đặc trưng thủ công) [27, 28]; mô hình đạt độ chính xác **93.15%** (Specificity: 94.04%, Sensitivity: 91.71%) trong cửa sổ tính toán ngắn 3 giây [29, 30].

### 19. Schwarz et al. (2023)
- **Tên tác giả**: Chris Schwarz, John Gaspar, Reza Yousefian [31, 32]
- **Tên bài báo**: *Multi-sensor driver monitoring for drowsiness prediction* [31, 32]
- **Tạp chí**: *Traffic Injury Prevention*, Tập 24, Số sup1, trang S100–S104 (2023) [31]
- **DOI / Link**: [10.1080/15389588.2023.2164839](https://doi.org/10.1080/15389588.2023.2164839) [31]
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Dữ liệu hành vi từ hệ thống DMS cột lái (Aisin), dữ liệu vận hành xe từ mô phỏng NADS-1, và tín hiệu BVP/HRV từ vòng đeo Empatica E4 thu từ 40 tài xế lái xe 3 giờ sau ít nhất 16 giờ thức liên tục [32-34]; gán nhãn định kỳ mỗi 10 phút qua KSS và quan sát ORD [32].
  - *Xử lý & Mô hình*: Ước tính khoảng IBI và tính chỉ số HRV qua Lomb-Scargle periodogram (cửa sổ 5 phút cho HRV, 3 phút cho các chỉ số khác) [35, 36]; xây dựng 9 mô hình phân loại bằng **Random Forest (RF)** [32, 37]; mô hình kết hợp đa nguồn (RCH) đạt độ chính xác **92%** ($0.88 - 0.95$) với PERCLOS và SDNN đóng vai trò quan trọng nhất [38, 39], đồng thời dự báo trạng thái buồn ngủ sớm **6.7 phút** trước khi xảy ra sự kiện chệch làn do buồn ngủ [32, 40].

### 20. Arefnezhad et al. (2019)
- **Tên tác giả**: Saeed Arefnezhad, S. Samiee, Arno Eichberger, Ali Nahvi
- **Tên bài báo**: *Driver drowsiness detection based on steering wheel data applying adaptive neuro-fuzzy feature selection*
- **Tạp chí**: *Sensors*, Tập 19, Số 4, Bài số 943 (2019)
- **DOI / Link**: [10.3390/s19040943](https://doi.org/10.3390/s19040943)
- **Tóm tắt phương pháp**:
  - *Cảm biến & Dữ liệu*: Tín hiệu góc xoay và vận tốc vô-lăng (tần số lấy mẫu 60 Hz) thu từ 39 tài xế xe buýt trên trình mô phỏng lái xe (BI301Semi, thu thập 20 giờ 36 phút dữ liệu); gán nhãn trạng thái Alert (KSS 1–6) và Drowsy (KSS 8–9) dựa trên thang đo KSS nhị phân [1, 2].
  - *Xử lý & Mô hình*: Khử hiệu ứng độ cong đoạn đường bằng cửa sổ trượt 3 giây (chồng lấp 1.5 giây); trích xuất 36 đặc trưng miền thời gian và tần số; dung hợp 4 chỉ số lọc (Fisher, Correlation, T-test, Mutual Information) qua hệ mờ thích ứng ANFIS tối ưu hóa bằng thuật toán PSO để chọn đặc trưng; phân loại bằng **Support Vector Machine (SVM)** đạt độ chính xác **98.12%** (AUC = 0.97) chỉ với 5 đặc trưng tối ưu [3-6].



Đoạn 1: Nói về Drowsiness là một quá trình chuyển pha sinh lý phức tạp và diễn ra từ từ, nhắc đến muốn liên quan giữa Drowsiness với ANS (Peker, 2026), Sau đó nêu ra ưu điểm của việc dùng tín hiệu sinh lý thay vì các phương pháp khác (vì nó mang thông tin bản chất sinh lý, ....) --> EEG, ECG, EMG, ... tuy nhiên PPG là một lựa chọn nổi bật vì tính noninsave, ... --> Đã có rất nhiều nghiên cứu sử dụng PPG cho bài toán drowsiness detection --> tuy nhiên các phương pháp phổ biến lại là time, frequency domain (sẽ nêu cụ thể một số đặc trưng hay sử dụng)  --> nhưng PPG là được coi là một chaotic dataa nên việc dùng các phương pháp trên chưa khai thác hết được bản chất động lực học của PPG trong bài toán trên.



Đoạn 2: Đang có rất ít nghiên cứu NTSA trên PPG (Charlton, 2023) --> một số nhgien cứu NTSA đã được áp dụng trên PPG -->  tuy nhiên với drowsiness thì còn khá hạn chế --> một số nghiên cứu chỉ dùng nó như một feature extraction sơ sài rồi cho vào một mô hình black box để thu được các con số --->Và chưa có nhiều nghiên cứu chỉ ra mối quan hệ giữa drowsiness với ANS hay PPG với ANS (Peker, 2026) -->  Cần một đánh giá chi tiết hơn về transition  state awake to drowsiness và chỉ ra mối quan hệ giữa PPG, Drowsiness và ANS.



Đoạn 3: Trong thực tế việc triển khai DDS (Drowsiness Detection System) sẽ phụ thuộc khá lớn vào windowing ---> 2 nghiên cứu của Shaffer  (2017, 2020) đã chỉ ra các khái niệm về UST, .... trong HRV --> Đông thời cũng chỉ ra tính bền vững, ổn định của các miền đặc trưng trên từng kích thước cửa sổ --> Một số nghiên cứu DDS có sử dụng nhiều kích thước khác nhau: từ UST --> kích thước lớn --> Việc chọn cửa sổ ảnh hưởng đến độ trễ của hệ thống và tính real time cũng như sự biểu diễn sinh lý của đặc trưng --> tuy nhiên còn rất hạn chế trong việc phân tích NTSA trên các kích thước cửa sổ --> đặc biệt NTSA là các phương pháp dễ bị tác động bởi tính dừng. 



Đoạn 4: Trong nỗ lực phân tích NTSA trên PPG, Sviridova 2015 đã áp dụng kết hợp các NTSA như để chứng minh PPG có đặc tính của một hệ chaos --> Đặt tiềm năng NTSA trên PPG trong các bài toán detect mental và physiological conditions. Sau đó, là Sviridova 2018 với sự kiểm định PPG vượt qua được PPS --> Sviridova 2022 đã nêu ra tiềm năng NTSA trên các kích thước cửa sổ ngắn của PPG signal  --> nhưng các nghiên cứu đều được thực hiện với PPG một trạng thái mà chưa hề phân tích NTSA để đánh giá sự thay đổi động lực học qua việc transition state awake to drowsiness và đánh giá chi tiết sự bền vững của NTSA với các kích thước cửa sổ khác nhau.



Đoạn 5:  Với các nghiên cứu trên, nghiên cứu này đề xuất một framework NTSA trên tín hiệu PPG --> Đề xuất gap + RQs