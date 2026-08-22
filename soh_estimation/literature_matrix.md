#Khoảng trống nghiên cứu nổi lên cho GSI

1. **Khái quát cấp đặc trưng / ổn định ánh xạ**  
   Hạn chế trước → dùng nhiều bộ dữ liệu không đồng nghĩa chuyển giao; Wen cho thấy đặc trưng hữu ích nhưng ánh xạ thay đổi.  
   → Giả thuyết GSI → ΔGSI giảm độ lệch riêng theo cell và ổn định hệ số góc/hệ số chặn/tính tuyến tính hơn GSI thô.  
   → Thí nghiệm → LOCO lồng nhau; đóng băng vùng/mô hình; dữ liệu ngoài không dùng nhãn để tinh chỉnh; báo cáo riêng độ phân tán FL và sai số ML.

2. **Hiệu quả tính toán được định lượng**  
   Hạn chế trước → các tuyên bố đều định tính; thiếu thời gian chạy, tham số, FLOPs/MACs, bộ nhớ và phần cứng.  
   → Giả thuyết GSI → một vô hướng + tuyến tính có đánh đổi độ chính xác–chi phí tốt hơn ANN nhiều ΔV, HPO-OS-ELM và TFMN.  
   → Thí nghiệm → định chuẩn tiền xử lý, trích đặc trưng, huấn luyện và suy luận trên phần cứng cố định; báo cáo độ trễ, lưu trữ, phép toán, bộ nhớ cực đại và độ chính xác.

3. **Độ bền không đạo hàm / ít tiền xử lý**  
   Hạn chế trước → ICA và `dV/dt` cần đạo hàm/lọc, nhưng IV và ΔSoC chứng minh “không đạo hàm” không còn mới.  
   → Giả thuyết GSI → trung bình vùng + ΔV giữ ổn định đặc trưng/dự đoán với ít tiền xử lý hơn.  
   → Thí nghiệm → nhiều mức nhiễu, giảm tần số lấy mẫu, thiếu mẫu, thí nghiệm loại bỏ lọc; báo cáo nhiễu đặc trưng và sai số SOH so với ICA/`dV/dt`, IV và ΔSoC.

4. **Diễn giải vật lý**  
   Hạn chế trước → Naha chỉ hiện tượng học; Wen/Jenu chỉ nhất quán ICA; chưa xác nhận cơ chế cụ thể.  
   → Giả thuyết GSI → GSI theo dõi hình học vùng nhạy lão hóa, nhất quán với ICA/DVA cục bộ.  
   → Thí nghiệm → chồng Head/Tail lên ICA/DVA; so sánh vị trí/biên độ/diện tích đỉnh và độ dốc; dùng nhiều C-rate để tách dòng/phân cực. Không tuyên bố đo LLI/LAM/SEI nếu thiếu chẩn đoán mạnh hơn.

5. **Độ bền vùng/cửa sổ**  
   Hạn chế trước → IV phụ thuộc khoảng điện áp; Naha dùng điểm đầu phụ thuộc ứng dụng; Wen chọn bằng tương quan; chưa có miền ổn định rộng theo quy trình không rò rỉ.  
   → Giả thuyết GSI → hiệu năng ổn định trên lân cận rộng thay vì cực trị nhọn phụ thuộc bộ dữ liệu.  
   → Thí nghiệm → bản đồ nhiễu hai chiều vùng và Head–Tail trong từng vòng LOCO ngoài; đóng băng vùng; báo cáo phân bố hiệu năng và độ rộng miền tối ưu.

6. **Chuẩn hóa tham chiếu BOL**  
   Hạn chế trước → không xác định được phương pháp `HI_t - HI_0` trong năm ghi chú; ánh xạ thô có độ lệch, còn tham chiếu đầu nhiễu có thể làm nhiễu mọi ΔGSI.  
   → Giả thuyết GSI → BOL giảm dịch chuyển hệ số chặn giữa cell và biến thiên ánh xạ giữa bộ dữ liệu.  
   → Thí nghiệm → so sánh GSI thô, ΔGSI tham chiếu chu kỳ đầu và trung bình K chu kỳ; đo phân tán hệ số, co cụm quỹ đạo, truyền nhiễu, sai số LOCO và sai số ngoài.

## D. Tóm tắt một slide cho giáo sư

| Câu hỏi | Kết luận ngắn theo góc nhìn phản biện |
|---|---|
| **Điều đã biết** | Quỹ đạo điện áp sạc/xả một phần chứa thông tin SOH. Đã có ΔV theo dung lượng, ΔSoC theo vùng, `dV/dt` theo vùng, ICA và IV. Vị trí vùng quan trọng; đặc trưng hữu ích không đồng nghĩa ánh xạ bất biến giữa bộ dữ liệu. |
| **Điều không còn mới** | Khi xét riêng: ΔV hữu hạn; trích theo vùng/đường đặc tính một phần; đặc trưng không đạo hàm hoặc “nhẹ”; chọn cửa sổ bằng tương quan; một vô hướng + SOH tuyến tính; kiểm định giữa cell; tuyên bố định tính “trực tuyến/hiệu quả”. |
| **Điều có thể vẫn mới** | **Chỉ trong năm ghi chú:** tổ hợp một ΔV theo dung lượng, trung bình vùng + BOL + chọn vùng không rò rỉ + kiểm định CC/CD nghiêm ngặt + đánh đổi độ chính xác–chi phí định lượng. Đây **không phải** bằng chứng mới trong toàn tài liệu khoa học. |
| **Điều phải chứng minh** | Một vô hướng so với nhiều đặc trưng; LOCO lồng nhau và chuyển giao ngoài; ổn định GSI thô/ΔGSI; nhiễu/giảm tần số/thiếu mẫu ở cấp đặc trưng và dự đoán; vùng ổn định rộng; độ trễ/tham số/phép toán/bộ nhớ; nhất quán ICA/DVA và độ nhạy C-rate/phân cực. |
| **Rủi ro chính** | Naha trùng mạnh với ΔV theo dung lượng; Wen đã có hình học vùng một vô hướng, chọn tương quan và tuyến tính; BOL có thể truyền nhiễu; chọn cửa sổ có thể rò rỉ nhãn; điện áp thô có thể phản ánh vận hành/điện trở; ICA/DVA vẫn không chứng minh cơ chế. |

## Kết luận tổng quát

Năm ghi chú **không** hỗ trợ tuyên bố rằng từng thành phần phổ quát của GSI là mới. Chúng chỉ hỗ trợ giả thuyết đóng góp hẹp hơn: GSI/ΔGSI có thể tạo đóng góp nhờ **nén tối giản theo tọa độ dung lượng, khả năng chuyển giao được chứng minh, độ bền theo vùng và chi phí thấp được định lượng**. Trạng thái hiện tại là **có khác biệt tiềm năng, chưa xác lập tính mới**.
