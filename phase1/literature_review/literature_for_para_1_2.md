
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
