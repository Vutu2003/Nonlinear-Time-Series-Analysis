### TÓM TẮT: GIẢ THIẾT VÀ HẠN CHẾ CỦA THUẬT TOÁN PPS

**1. Hai giả thiết cốt lõi (Điều kiện cần)**
* **Tính giả tuần hoàn mạnh:** Dữ liệu bắt buộc phải có tính chu kỳ rõ rệt (như nhịp tim). PPS chỉ phục vụ một giả thuyết $H_0$ chuyên biệt: quỹ đạo chu kỳ bị chi phối bởi nhiễu không tương quan.
* **Không gian pha chuẩn xác:** Đa tạp động lực học phải được khôi phục trọn vẹn thông qua việc chọn đúng các tham số nhúng (số chiều $d_e$ và độ trễ $\tau$).

**2. Ba hạn chế và kịch bản thất bại (Điểm mù)**
* **Độ nhạy cực cao với bán kính $\rho$:** 
  * $\rho$ quá lớn $\rightarrow$ Sinh ra nhiễu trắng, phá hủy cấu trúc vĩ mô.
  * $\rho$ quá nhỏ $\rightarrow$ Sao chép y hệt bản gốc (đóng băng). 
  * *Khắc phục:* Bắt buộc phải quét tối ưu hóa $\rho$.
* **Khuếch đại sai số nhúng:** Nếu $d_e$ và $\tau$ cấu hình sai, hàm xác suất sẽ đo khoảng cách trên một không gian ảo, dẫn đến băm nát nhầm cả cấu trúc vĩ mô.
* **Bẫy diễn giải kết quả:** Bác bỏ được $H_0$ không đảm bảo 100% hệ thống có "hỗn loạn tất định" (nguyên nhân có thể do nhiễu màu/correlated noise). 
  * *Khắc phục:* Sử dụng kỹ thuật làm trắng (prewhitening) làm bộ lọc đối chứng.


### TÁC ĐỘNG CỦA NHIỄU LÊN THUẬT TOÁN PPS (Theo Michael Small)

Dựa trên các thử nghiệm của tác giả, thuật toán PPS phản ứng với nhiễu (Signal + Noise) qua 3 kịch bản cốt lõi:

* **Tín hiệu chu kỳ + Nhiễu trắng (White Noise):** Thuật toán **chấp nhận** giả thuyết $H_0$. Điều này minh chứng thuật toán hoạt động chuẩn xác theo thiết kế, vì dữ liệu đầu vào khớp hoàn toàn với định nghĩa của $H_0$ (hệ chu kỳ bị chi phối bởi nhiễu không tương quan).
* **Tín hiệu chu kỳ + Nhiễu màu (Colored Noise):** Thuật toán **bác bỏ** giả thuyết $H_0$. Nhiễu màu tạo ra các liên kết tương quan vắt ngang qua nhiều chu kỳ, và cơ chế xáo trộn láng giềng của PPS đã băm nát thành công các liên kết giả tạo này.
* **Hỗn loạn/Chu kỳ + Nhiễu đo lường (Measurement/Dynamic Noise):** Thuật toán **hoạt động hoàn hảo và bền bỉ**. Dù thử nghiệm trên dữ liệu mô phỏng bị bơm nhiễu (hệ Rössler) hay dữ liệu thực tế cực kỳ nhiễu (điện tim ECG), PPS vẫn phân định chính xác tính hỗn loạn (bác bỏ $H_0$) hoặc tính chu kỳ (chấp nhận $H_0$) mà vẫn giữ nguyên được hình dáng vĩ mô của quỹ đạo gốc.