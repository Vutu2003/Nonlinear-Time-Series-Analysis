## Diễn giải hiện tại về GSI trước khi đọc sâu các prior art gần nhất

### 1. GSI là gì về mặt toán học?

GSI là một descriptor hình học có số chiều thấp được trích xuất từ
đường cong điện áp–dung lượng.

GSI đo độ chênh điện áp theo phương đứng giữa hai vùng dung lượng
được xác định trước:

$$
GSI = V_H - V_T
$$

Do đó, GSI có thể được hiểu là một chênh lệch điện áp hữu hạn trong
một vùng cục bộ của đường cong. Nếu khoảng cách dung lượng giữa hai
vùng được giữ cố định, GSI cũng mang thông tin gần tương đương với
độ dốc secant cục bộ của đường cong điện áp–dung lượng.

### 2. GSI được kỳ vọng phản ánh điều gì?

Giả thuyết làm việc hiện tại là quá trình lão hóa pin làm thay đổi hình
dạng và vị trí của đường cong điện áp–dung lượng.

Do đó:

$$
\text{lão hóa}
\rightarrow
\text{sự biến đổi của đường cong điện áp}
\rightarrow
\text{sự thay đổi của GSI}
$$

Ở thời điểm hiện tại, GSI nên được hiểu là một đại lượng hình học cô
đọng phản ánh sự biến đổi của voltage trajectory do lão hóa gây ra.

### 3. Điều gì vẫn chưa được giải thích rõ?

Cơ chế điện hóa nối giữa lão hóa pin và sự thay đổi quan sát được của
GSI hiện vẫn chưa được thiết lập rõ ràng.

Mắt xích còn thiếu là:

$$
\text{các cơ chế suy giảm}
\rightarrow
?
\rightarrow
\text{sự thay đổi của đường cong điện áp–dung lượng}
\rightarrow
\text{sự thay đổi của GSI}
$$

Ở giai đoạn này, chưa có đủ cơ sở để khẳng định rằng GSI trực tiếp đo
LLI, LAM, electrode slippage, SEI growth hoặc sự gia tăng điện trở.

### 4. Diễn giải hiện tại về Differential GSI

Differential GSI được định nghĩa là:

$$
\Delta GSI_t = GSI_t-GSI_0
$$

Hiện tại, $\Delta GSI$ nên được hiểu chủ yếu như một chiến lược chuẩn hóa
theo reference của chính cell, thay vì một cơ chế suy giảm vật lý riêng.

Giả thuyết là:

$$
GSI_t
=
\text{thành phần phụ thuộc lão hóa}
+
\text{baseline riêng của cell}
+
\epsilon
$$

vì vậy:

$$
\Delta GSI_t
=
GSI_t-GSI_0
$$

có thể loại bỏ một phần baseline riêng của từng cell và làm nổi bật hơn
sự thay đổi thực sự liên quan đến lão hóa.

Giả thuyết này vẫn cần được kiểm chứng bằng:
- ablation GSI so với $\Delta GSI$;
- phân tích mức độ giảm inter-cell offset;
- kiểm tra unseen-cell generalization.

### 5. Các câu hỏi cần trả lời khi đọc lại các prior art gần nhất

1. Vì sao đường cong điện áp thay đổi khi pin lão hóa?

2. Những degradation mechanisms nào có thể làm thay đổi:
   - khoảng cách điện áp cục bộ,
   - độ dốc,
   - hình dạng vùng plateau,
   - hoặc vị trí của voltage trajectory?

3. Các nghiên cứu trước diễn giải finite voltage difference theo cơ chế
   vật lý hay chỉ dừng ở empirical correlation?

4. Sự gia tăng impedance/polarization có đủ để giải thích thay đổi của
   GSI hay cần xét thêm LLI, LAM hoặc sự mất cân bằng giữa hai điện cực?

5. Có bằng chứng nào nối sự thay đổi của regional voltage feature với
   ICA/DVA evolution hay không?

6. Các diễn giải đó có áp dụng được cụ thể cho vùng early-discharge
   plateau của LFP hay không?

7. Phần nào của cơ chế có thể được claim an toàn cho GSI, và phần nào
   chỉ nên giữ ở mức hypothesis?

### 6. Cách hiểu ngắn gọn cần giữ trong đầu

GSI hiện tại trước hết là một **quan sát hình học** trên voltage curve,
chưa phải một **cơ chế vật lý đã được chứng minh**.

Có thể tóm tắt như sau:

$$
\text{GSI}
=
\text{descriptor hình học của voltage trajectory}
$$

và giả thuyết khoa học cần tiếp tục làm rõ là:

$$
\text{degradation mechanism}
\rightarrow
\text{trajectory evolution}
\rightarrow
\text{GSI evolution}
\rightarrow
\text{SOH}
$$