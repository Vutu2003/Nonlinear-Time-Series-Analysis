**1. Đề xuất kỹ thuật Tái cấu trúc không gian pha (Phase-Space Reconstruction)**
Tác giả đề xuất một ý tưởng heuristic: Bạn không cần phải đo lường tất cả các biến số của hệ thống [1]. Bạn hoàn toàn có thể dùng một biến số duy nhất để tạo ra các "tọa độ độc lập" nhằm vẽ lại không gian pha nhiều chiều [1, 2]. 
Có 2 cách được tác giả đề xuất:
* **Dùng trễ thời gian (Time-delay):** Lấy chuỗi dữ liệu kết hợp với các mốc quá khứ của nó: $x(t), x(t-\tau), x(t-2\tau)$ [2].
* **Dùng đạo hàm:** Lấy chuỗi dữ liệu kết hợp với đạo hàm các bậc: $x(t), \dot{x}(t), \ddot{x}(t)$ [2].

**2. Đề xuất cách tính độ hỗn loạn (Số mũ Liapunov)**
Thay vì cần biết các phương trình vi phân gốc của hệ thống, tác giả đề xuất sử dụng chính không gian pha vừa được tái tạo (ở Đề xuất 1) để cắt ra một bản đồ hồi quy 1 chiều (1D return map) [3]. 
Từ bản đồ này, ta có thể tính được "số mũ Liapunov dương" - thước đo quan trọng nhất để xác định xem hệ thống có hỗn loạn (chaos) hay không [3-5].

**3. Đề xuất phương pháp tìm "Số chiều" (Dimension) của hệ thống**
Làm sao biết hệ thống cần bao nhiêu chiều để mô tả? Tác giả đề xuất dùng phân phối xác suất có điều kiện (conditional probability distributions) [6]. 
* **Cách thức:** Số chiều của hệ thống chính là số lượng các điều kiện (số điểm trễ thời gian) cần thiết để làm cho phân phối xác suất trở nên "cực kỳ sắc nét" (extremely sharp) [7]. Khi đó, trạng thái của hệ thống đã được xác định hoàn toàn bởi các điều kiện này [7].
Bạn có thể copy trực tiếp khối mã trên để đưa vào Obsidian, Notion, Jupyter Notebook, hoặc 