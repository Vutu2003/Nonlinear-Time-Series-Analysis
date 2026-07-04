# THUẬT TOÁN IAAFT (Iterative Amplitude Adjusted Fourier Transform)
*Dựa trên Schreiber & Schmitz (1996)*

## BƯỚC 0: Khởi tạo (Initialization)
Cho chuỗi thời gian gốc $s_n$ với $n = 0, 1, \dots, N-1$.

* **Lưu phân phối gốc:** Sắp xếp $s_n$ theo thứ tự tăng dần để tạo mảng mẫu phân phối $s_{sorted}$.
* **Lưu biên độ phổ gốc:** Thực hiện Biến đổi Fourier Rời rạc (DFT) chuỗi $s_n$ để trích xuất biên độ tuyệt đối lý tưởng $|S_k|$:
    $$|S_k| = \left| \sum_{n=0}^{N-1} s_n e^{i 2\pi k n / N} \right|$$
* **Khởi tạo chuỗi giả:** Khởi tạo $s_n^{(0)}$ bằng cách xáo trộn ngẫu nhiên (random shuffle) các giá trị của $s_n$.

---

## VÒNG LẶP ĐỆ QUY (Bước thứ $i$, với $i \ge 0$)

### BƯỚC 1: Khớp Phổ năng lượng (The Fourier Step)
* Thực hiện DFT trên chuỗi giả hiện tại $s_n^{(i)}$ để lấy biên độ và góc pha $\phi_k^{(i)}$:
    $$S_k^{(i)} = \sum_{n=0}^{N-1} s_n^{(i)} e^{i 2\pi k n / N} = |S_k^{(i)}| e^{i \phi_k^{(i)}}$$
* **Cưỡng ép phổ:** Bỏ biên độ hiện tại, thay thế bằng biên độ lý tưởng $|S_k|$, giữ nguyên góc pha:
    $$\tilde{S}_k^{(i)} = |S_k| e^{i \phi_k^{(i)}}$$
* Thực hiện biến đổi ngược (IFFT) để đưa về miền thời gian, tạo chuỗi trung gian $\tilde{s}_n^{(i)}$:
    $$\tilde{s}_n^{(i)} = \frac{1}{N} \sum_{k=0}^{N-1} \tilde{S}_k^{(i)} e^{-i 2\pi k n / N}$$
    *(Hệ quả: Phổ năng lượng chính xác hoàn toàn, nhưng các giá trị phân phối đã bị làm méo).*

### BƯỚC 2: Khớp Phân phối (The Rank-ordering Step)
* Tính thứ hạng (rank) của từng điểm dữ liệu trong chuỗi trung gian $\tilde{s}_n^{(i)}$ vừa tạo.
* **Cưỡng ép phân phối:** Tạo chuỗi mới $s_n^{(i+1)}$ bằng cách thay thế trực tiếp các giá trị của $\tilde{s}_n^{(i)}$ bằng các giá trị gốc trong mảng $s_{sorted}$ tương ứng với cùng một thứ hạng.
    *(Hệ quả: Các giá trị dữ liệu và phân phối chuẩn xác 100%, nhưng phổ năng lượng bị xô lệch nhẹ so với Bước 1).*

### BƯỚC 3: Kiểm tra Hội tụ (Convergence)
* So sánh chuỗi vừa tạo với chuỗi của vòng lặp trước. 
* **Điều kiện dừng:** Thuật toán kết thúc khi không còn bất kỳ sự hoán đổi thứ hạng nào xảy ra ở Bước 2, tức là:
    $$s_n^{(i+1)} = s_n^{(i)}$$
* Nếu điều kiện chưa thỏa mãn, gán $i = i + 1$ và quay lại **BƯỚC 1**. Chạy cho đến khi đạt điểm hội tụ hoặc chạm ngưỡng số vòng lặp tối đa.