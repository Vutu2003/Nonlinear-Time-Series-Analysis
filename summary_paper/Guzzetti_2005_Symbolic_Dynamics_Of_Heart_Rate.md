# Paper Metadata
* **Title**: Symbolic Dynamics of Heart Rate Variability: A Probe to Investigate Cardiac Autonomic Modulation
* **Authors**: Stefano Guzzetti, Ester Borroni, Pietro E. Garbelli, Elisa Ceriani, Paolo Della Bella, Nicola Montano, Chiara Cogliati, Virend K. Somers, Alberto Malliani, Alberto Porta
* **Year**: 2005
* **Keywords**: arrhythmia, heart rate, nervous system, autonomic

# 1. Why

## Research Question

Liệu **phân tích ký hiệu (symbolic analysis)** trên các chuỗi RR ngắn dài 3 nhịp có thể phân biệt được:

- điều biến giao cảm (sympathetic modulation);
- điều biến đối giao cảm/phế vị (parasympathetic/vagal modulation);

và từ đó phát hiện những thay đổi thần kinh tự chủ ngắn hạn trước các biến cố tim cấp hay không?

## Motivation

Hệ giao cảm và đối giao cảm là hai hệ chính điều khiển nhịp tim, nhưng có **độ trễ và diễn tiến thời gian khác nhau**:

$$
\text{parasympathetic response}
\quad \text{nhanh hơn} \quad
\text{sympathetic response}
$$

Các thay đổi thần kinh tự chủ trước biến cố tim có thể:

- rất ngắn;
- không ổn định;
- không lặp lại theo chu kỳ rõ ràng.

Do đó cần một phương pháp có khả năng khai thác:

$$
\boxed{
\text{short-term beat-to-beat temporal patterns}
}
$$

thay vì chỉ mô tả biến thiên tổng thể của HRV.

## Previous Methods

Các phương pháp HRV tuyến tính, đặc biệt là **phân tích phổ (spectral analysis)**, có thể cung cấp các chỉ số điều biến thần kinh tự chủ khi tín hiệu có tính nhịp điệu và tương đối ổn định.

Tuy nhiên, chúng kém tin cậy hơn trong các giai đoạn:

$$
\text{rapid}
+
\text{transient}
+
\text{nonrepetitive changes}
$$

như trước các rối loạn nhịp tim cấp.

Vì vậy authors đề xuất:

$$
\boxed{
RR\ series
\rightarrow
\text{3-beat symbolic patterns}
\rightarrow
\text{pattern occurrence}
\rightarrow
\text{autonomic interpretation}
}
$$

nhằm bổ sung thông tin mà các chỉ số HRV tuyến tính truyền thống có thể bỏ sót.