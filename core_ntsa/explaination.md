# 🛠️ TÀI LIỆU CỐT LÕI: HỆ SINH DỮ LIỆU VÀ CÔNG CỤ NHIỄU

Thư mục `core_ntsa` chứa các "động cơ" toán học nền tảng phục vụ cho việc kiểm thử các thuật toán Động lực học phi tuyến (NTSA).

---

## 1. Hệ Sinh Dữ Liệu (`generators.py`)

Module này tạo ra các dữ liệu chuẩn (Ground Truth) từ các hệ hỗn mang kinh điển. Mọi hàm đều có tham số `transient_drop` để loại bỏ trạng thái chuyển tiếp ban đầu, đảm bảo quỹ đạo đã hội tụ vào bộ hấp dẫn (Attractor).

### A. Hệ Lorenz (Liên tục)
Mô tả sự đối lưu của chất lưu. Là hệ phương trình vi phân thường (ODEs) 3 chiều:
$$\frac{dx}{dt} = \sigma(y - x)$$
$$\frac{dy}{dt} = x(\rho - z) - y$$
$$\frac{dz}{dt} = xy - \beta z$$
*Thuật toán giải:* Runge-Kutta bậc 4-5 (`RK45` từ `scipy.integrate.solve_ivp`).

### B. Hệ Rössler (Liên tục)
Được thiết kế để có cấu trúc hỗn mang đơn giản hơn Lorenz (chỉ gập 1 lần):
$$\frac{dx}{dt} = -y - z$$
$$\frac{dy}{dt} = x + a y$$
$$\frac{dz}{dt} = b + z(x - c)$$

### C. Ánh xạ Hénon (Rời rạc)
Khác với ODEs, đây là hệ sai phân sinh ra dữ liệu rời rạc 2D, mô phỏng cơ chế giãn-gập (stretching and folding):
$$x_{n+1} = 1 - a x_n^2 + y_n$$
$$y_{n+1} = b x_n$$

---

## 2. Công Cụ Nhiễu (`noise_tools.py`)

Thuật toán NTSA rất nhạy cảm với nhiễu. Module này cung cấp 4 kịch bản nhiễu để "stress-test" thuật toán, phản ánh các điều kiện thực tế của tín hiệu sinh lý (như PPG/ECG).

### A. Nhiễu Trắng (White Noise) & Tỷ số SNR
Thêm nhiễu phân phối chuẩn (Gaussian). Năng lượng nhiễu được tính ngược từ tỷ số Tín hiệu/Nhiễu (SNR) mục tiêu:
$$SNR_{dB} = 10 \log_{10} \left( \frac{P_{signal}}{P_{noise}} \right) \implies P_{noise} = \frac{P_{signal}}{10^{SNR_{dB}/10}}$$

### B. Nhiễu Có Màu (Colored Noise)
Sử dụng biến đổi Fourier ($FFT$) để lọc phổ tần số của nhiễu trắng:
* **Nhiễu Hồng (Pink Noise - $1/f$):** Mô phỏng nhiễu nền sinh lý học. Biên độ tỷ lệ với $1/\sqrt{f}$.
* **Nhiễu Nâu (Brown Noise - $1/f^2$):** Bước đi ngẫu nhiên (Random walk). Biên độ tỷ lệ với $1/f$.

### C. Nhiễu Chuyển Động (Motion Artifacts)
Mô phỏng sự xô lệch cảm biến. Tạo ra các xung động (bursts) biên độ lớn, cục bộ. Sử dụng **Cửa sổ Hanning** để vuốt mịn hai đầu xung nhiễu, tránh đứt gãy tần số cao:
$$Artifact(t) = Noise(t) \times \sin^2\left(\frac{\pi t}{N-1}\right)$$

### D. Trôi Đường Nền (Baseline Wander)
Cộng thêm một sóng sin tần số cực thấp (ví dụ: $0.2 Hz$) để mô phỏng sự trôi dạt do nhịp thở hoặc thay đổi trở kháng da, tạo ra tính phi dừng (non-stationarity).