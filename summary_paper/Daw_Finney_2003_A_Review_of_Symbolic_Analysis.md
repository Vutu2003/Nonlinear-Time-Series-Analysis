# Introduction — Reasoning Chain

$$
\boxed{\text{Dữ liệu thực nghiệm phức tạp khó phân tích}}
$$

Các công cụ truyền thống như Fourier có thể không đủ với dynamics phi tuyến, hỗn loạn và nhiễu.

$$
\downarrow
$$

$$
\boxed{\text{Coarse-graining có thể hữu ích}}
$$

Ta chủ động bỏ bớt độ phân giải để giữ lại cấu trúc thời gian quan trọng.

$$
\downarrow
$$

$$
\boxed{x_t \longrightarrow s_t}
$$

Tín hiệu liên tục được ánh xạ thành chuỗi ký hiệu thuộc một bảng chữ cái hữu hạn.

$$
\downarrow
$$

$$
\boxed{\text{Chuỗi ký hiệu là một representation mới của dynamics}}
$$

Mục tiêu không phải giữ toàn bộ dữ liệu, mà giữ phần thông tin hữu ích về temporal structure.

$$
\downarrow
$$

$$
\boxed{\text{Tại sao discretization mạnh như vậy vẫn có ích?}}
$$

Ý tưởng này có nền tảng từ information theory, Markov chains và các hệ vốn có trạng thái rời rạc.

$$
\downarrow
$$

$$
\boxed{\text{Symbolization có nguồn gốc từ symbolic dynamics}}
$$

Từ Hadamard và Morse, dynamics có thể được mô tả qua các chuỗi ký hiệu và các quy tắc allowed/forbidden.

$$
\downarrow
$$

$$
\boxed{\text{Continuous flow} \longrightarrow \text{Poincaré map}}
$$

Poincaré section biến một trajectory liên tục thành chuỗi các lần quay trở lại rời rạc.

$$
\downarrow
$$

$$
\boxed{\text{Partition phase space} \longrightarrow \text{Symbols}}
$$

Mỗi vùng của phase space được gán một ký hiệu, biến trajectory thành một symbolic itinerary.

$$
\downarrow
$$

$$
\boxed{\text{Geometry} \longrightarrow \text{Symbolic sequence}}
$$

Ta thay tọa độ chính xác bằng thứ tự các vùng mà trajectory đi qua.

$$
\downarrow
$$

$$
\boxed{\text{Symbolic dynamics có thể được mô tả thống kê}}
$$

Tần suất symbol và transition cho biết cách hệ di chuyển giữa các trạng thái coarse-grained.

$$
\downarrow
$$

$$
\boxed{\text{Ergodic theory nối time statistics với ensemble statistics}}
$$

Điều này quan trọng vì thực nghiệm thường chỉ quan sát được một hoặc vài trajectory.

$$
\downarrow
$$

$$
\boxed{\text{Coarse-graining} \longrightarrow \text{finite-state dynamics}}
$$

Dynamics liên tục có thể được xấp xỉ bằng chuyển trạng thái giữa một số hữu hạn các vùng.

$$
\downarrow
$$

$$
\boxed{\text{Lý tưởng: generating partition}}
$$

Một generating partition cho phép các trajectory khác nhau tương ứng với các symbolic sequence khác nhau.

$$
\downarrow
$$

$$
\boxed{\text{Nhưng dữ liệu thực nghiệm hiếm khi cho phép điều đó}}
$$

Với hệ chưa biết và có nhiễu, generating partition thường không thể xác định hoặc không tồn tại theo nghĩa lý tưởng.

$$
\downarrow
$$

$$
\boxed{\text{Symbolic Dynamics} \neq \text{Symbolic Time-Series Analysis}}
$$

Phân tích thực nghiệm thường phải dùng các partition heuristic hoặc empirical thay vì partition tối ưu về mặt toán học.

$$
\downarrow
$$

$$
\boxed{\text{Partition hữu ích không nhất thiết phải là generating partition}}
$$

Điều quan trọng là encoding giữ được thông tin liên quan đến câu hỏi khoa học.

$$
\downarrow
$$

$$
\boxed{\text{Symbols} \longrightarrow \text{Words} \longrightarrow \text{Statistics}}
$$

Các symbol liên tiếp được ghép thành words và nghiên cứu thông qua phân phối tần suất của chúng.

$$
\downarrow
$$

$$
\boxed{\text{Statistics} \longrightarrow \text{Temporal structure / Information}}
$$

Entropy, correlation và các thống kê khác được dùng để đặc trưng organization của symbolic sequence.

$$
\downarrow
$$

$$
\boxed{\text{Symbolic analysis}=\text{giữ thông tin có chọn lọc}}
$$

Câu hỏi cốt lõi không phải là **mất bao nhiêu thông tin**, mà là **mất thông tin nào và thông tin đó có quan trọng hay không**.


# Practical Measurements Issues
$$
\boxed{\text{Sampling}}
$$

Dữ liệu được lấy theo fixed-rate hay event-triggered? Có aliasing không?

$$
\downarrow
$$

$$
\boxed{\text{Noise}}
$$

Noise đến từ measurement hay chính dynamics? Coarse-graining sẽ lọc hay làm méo nó?

$$
\downarrow
$$

$$
\boxed{\text{Observability}}
$$

Ta có full state hay chỉ một observable? Có cần reconstructed phase space không?

$$
\downarrow
$$

$$
\boxed{\text{Stationarity}}
$$

Statistics có ổn định trong khoảng phân tích không, hay đang trộn nhiều regimes?

$$
\downarrow
$$

$$
\boxed{\text{Sau đó mới symbolization}}
$$

# III. Defining Symbols

$$
\boxed{\text{Digitization} \neq \text{Symbolization}}
$$

Dữ liệu số đã rời rạc, nhưng symbolic analysis thường coarse-grain mạnh hơn nhiều.

$$
\downarrow
$$

$$
\boxed{\text{Partition dữ liệu thành alphabet hữu hạn}}
$$

$$
x_t \in A_i \Rightarrow s_t=i
$$

Alphabet size quyết định trade-off giữa **giữ chi tiết** và **giữ cả noise**.

$$
\downarrow
$$

$$
\boxed{\text{Ideal: Generating Partition}}
$$

Với hệ deterministic, noise-free, đây là encoding lý tưởng; nhưng thường không khả thi với dữ liệu thực nghiệm.

$$
\downarrow
$$

$$
\boxed{\text{Practical / Heuristic Partition}}
$$

Có thể dùng mean, median, equal-width bins, equiprobable bins,...

$$
\downarrow
$$

$$
\boxed{\text{Ưu tiên partition có ý nghĩa vật lý}}
$$

Nếu hệ có natural threshold hoặc discrete states, nên tận dụng chúng.

$$
\downarrow
$$

$$
\boxed{\text{Luôn kiểm tra sensitivity}}
$$

Partition xấu có thể làm mất meaningful dynamics; “optimal” luôn phụ thuộc objective.

$$
\downarrow
$$

$$
\boxed{\text{Không chỉ encode amplitude}}
$$

Có thể encode:

$$
x_t,\qquad \Delta x_t,\qquad \mathbf{x}_t \text{ trong phase space}
$$

tương ứng với static, dynamic hoặc phase-space symbolization.

$$
\downarrow
$$

$$
\boxed{\text{Continuous data} \rightarrow \text{Symbol sequence}}
$$

Cốt lõi của Section III:

$$
\boxed{\text{Encoding = quyết định giữ thông tin gì và bỏ thông tin gì}}
$$