# Paper Metadata
* **Title**: Permutation Entropy: A Natural Complexity Measure for Time Series
* **Authors**: Christoph Bandt and Bernd Pompe
* **Year**: 2002
* **Keywords**: Permutation entropy, Complexity measure, Time series, Chaotic dynamical systems, Noise

# 1. Why

## Research Question

Làm thế nào để xây dựng một **thước đo độ phức tạp đơn giản, bền vững và có thể tính trực tiếp** cho các chuỗi thời gian thực tế?

## Motivation

Các thước đo độ phức tạp cổ điển như entropy, fractal dimension và Lyapunov exponent có nền tảng lý thuyết mạnh, nhưng khi áp dụng lên dữ liệu thực thường cần:

- giả định về hệ động lực bên dưới;
- tiền xử lý và tinh chỉnh tham số;
- xử lý nhiễu;
- các thủ tục ước lượng không đơn giản.

Authors muốn một phương pháp:

- áp dụng trực tiếp lên chuỗi thời gian quan sát được;
- tính nhanh và đơn giản;
- dùng được cho tín hiệu regular, chaotic, noisy và real-world;
- không cần biết mô hình động lực hay generating partition.

## Previous Methods

### Classical dynamical complexity measures

- Shannon / Kolmogorov-Sinai entropy
- Fractal dimensions
- Lyapunov exponents

Các đại lượng này phù hợp với hệ động lực lý tưởng nhưng có thể khó ước lượng đáng tin cậy từ dữ liệu hữu hạn và có nhiễu.

### Symbolic partition methods

Chuỗi liên tục được chuyển thành symbols bằng một partition:

$$
x_t \rightarrow s_t
$$

sau đó entropy được tính trên symbolic sequence.

Hạn chế chính:

$$
\text{Symbolic representation tốt}
\Rightarrow
\text{cần partition phù hợp / generating partition}
$$

nhưng generating partition thường khó xác định, và partition đặt sai có thể làm giảm complexity quan sát được.

### Authors' Motivation

Thay vì dùng các ngưỡng biên độ bên ngoài, authors đề xuất xây representation trực tiếp từ:

$$
\boxed{\text{thứ tự tương đối giữa các giá trị lân cận}}
$$

để symbolic structure phát sinh tự nhiên từ chính chuỗi thời gian.