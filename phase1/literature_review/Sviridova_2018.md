## Sviridova et al. (2018) — Core contribution

### Câu hỏi nghiên cứu

Liệu green-light PPG (gPPG) có chứa động lực học hỗn độn tương tự red/NIR PPG hay không, và liệu các đặc trưng đó có thể được giải thích chỉ bằng một quá trình tuần hoàn bị nhiễu?

### Đóng góp chính

Nghiên cứu mở rộng framework nonlinear của Sviridova (2015) bằng cách kết hợp:

- phase-space reconstruction;
- Wayland test;
- deterministic nonlinear prediction;
- Fourier phase-randomized surrogates;
- pseudoperiodic surrogates;
- LLE;
- 0–1 test for chaos.

Điểm methodological quan trọng nhất là việc sử dụng **PPS** để kiểm tra null:

> observed PPG có thể chỉ là một **noise-driven periodic orbit**.

Original gPPG cho prediction behavior khác rõ với PPS, cho phép bác bỏ noisy pseudoperiodic explanation trong statistic được kiểm tra.

### Kết quả chính

- gPPG cho bằng chứng phù hợp với determinism;
- có short-term predictability nhưng prediction decay nhanh hơn rPPG;
- LLE dương và trung bình cao hơn rPPG;
- 0–1 test cho giá trị gần 1;
- original gPPG khác cả phase-randomized và pseudoperiodic surrogates.

### Kết luận

gPPG biểu hiện nhiều đặc trưng phù hợp với chaotic dynamics và có dynamical organization không dễ được giải thích chỉ bằng linear stochasticity hoặc noisy periodicity.

### Vai trò đối với nghiên cứu hiện tại

Paper 2018 cung cấp precedent trực tiếp cho việc dùng **PPS như một difficult null model đối với PPG gần chu kỳ**.

Nó chuyển câu hỏi từ:

`PPG có nonlinear organization hay không?`

sang:

`Organization đó có vượt noisy pseudoperiodic explanation hay không?`


## Khoảng trống nghiên cứu từ Sviridova et al. (2018)

Sviridova et al. (2018) cho thấy động lực học PPG có thể vượt qua cách giải thích đơn giản bằng **quá trình chu kỳ bị nhiễu**, thông qua kiểm định pseudoperiodic surrogate (PPS). :contentReference[oaicite:0]{index=0}

Tuy nhiên, nghiên cứu này chủ yếu trả lời câu hỏi:

> **PPG có chứa tổ chức động lực học vượt noisy pseudoperiodicity hay không?**

Nó chưa trả lời:

> **Tổ chức động lực học đó thay đổi như thế nào giữa các trạng thái sinh lý khác nhau?**

### Khoảng trống nghiên cứu

> **Sự biến đổi theo trạng thái của PPG dynamics sau khi đã vượt qua noisy pseudoperiodic null vẫn chưa được đặc trưng đầy đủ.**

Đặc biệt, vẫn chưa rõ từ **Awake sang Drowsy**, các khía cạnh sau thay đổi ra sao:

- khả năng dự báo;
- tổ chức recurrence;
- mức độ phân kỳ cục bộ của quỹ đạo.

### Liên hệ với nghiên cứu hiện tại

Nghiên cứu hiện tại mở rộng logic của Sviridova et al. (2018) từ:

```text
PPG vượt noisy pseudoperiodic null
→
PPG dynamics thay đổi thế nào theo trạng thái sinh lý?