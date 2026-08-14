# Paper Metadata
* **Title**: Ordinal analysis of time series
* **Authors**: K. Keller, M. Sinn
* **Year**: 2005
* **Keywords**: Time series; Complexity; Ordinal patterns; Permutation entropy

# 1. Why

## Research Question

Làm thế nào để biểu diễn và khai thác **toàn bộ thông tin ordinal** của một chuỗi thời gian, thay vì nén cấu trúc ordinal xuống một giá trị entropy duy nhất?

## Motivation

Bandt–Pompe cho thấy có thể phân tích time series một cách robust bằng cách sử dụng **quan hệ thứ tự tương đối** thay cho giá trị biên độ tuyệt đối:

$$
x_t
\rightarrow
\text{ordinal patterns}
$$

Tuy nhiên, cấu trúc ordinal chứa nhiều thông tin hơn một scalar complexity measure.

Keller & Sinn hướng tới một representation có thể:

- giữ lại ordinal state tại mỗi thời điểm;
- được tính toán hiệu quả;
- hỗ trợ các phân tích sâu hơn ngoài entropy.

Ý tưởng cốt lõi:

$$
\boxed{
\text{Giữ lại ordinal structure trước}
\rightarrow
\text{quantify sau}
}
$$

## Previous Methods

### Bandt–Pompe Permutation Entropy

Pipeline:

$$
x_t
\rightarrow
\pi_t
\rightarrow
p(\pi)
\rightarrow
H
$$

Permutation Entropy tóm tắt distribution của ordinal patterns bằng:

$$
H
=
-\sum_{\pi}p(\pi)\log p(\pi)
$$

Đây là một complexity measure hữu ích, nhưng chỉ cung cấp **một chi tiết của ordinal structure**.

Bước nén:

$$
p(\pi)
\rightarrow
H
$$

làm mất nhiều thông tin về cấu trúc cụ thể của các ordinal patterns.

Vì vậy Keller & Sinn chuyển từ:

$$
\boxed{
\text{ordinal structure}
\rightarrow
\text{scalar complexity}
}
$$

sang:

$$
\boxed{
\text{ordinal structure}
\rightarrow
\text{richer ordinal representation}
}
$$