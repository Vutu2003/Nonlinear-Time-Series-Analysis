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

# 2. What

## Core Insight

Authors không chỉ đo **mức độ phức tạp tổng thể (global complexity)** của HRV, mà thiết kế một **biểu diễn ký hiệu có thể diễn giải về sinh lý**.

Chuỗi RR được:

$$
\text{RR series}
\rightarrow
\text{6 symbolic levels}
\rightarrow
\text{3-beat patterns}
\rightarrow
\{0V,1V,2V\}
$$

Trong đó:

- **0V**: không có biến đổi giữa các ký hiệu liên tiếp;
- **1V**: có một biến đổi;
- **2V**: có hai biến đổi.

Ý tưởng cốt lõi:

$$
\boxed{
\text{Loại local pattern}
\rightarrow
\text{mức độ điều biến thần kinh tự chủ}
}
$$

Thay vì chỉ hỏi:

$$
\text{HRV phức tạp đến đâu?}
$$

paper hỏi:

$$
\boxed{
\text{Kiểu biến thiên ngắn hạn nào đang chiếm ưu thế?}
}
$$

---

## Mathematical Foundation

### 1. Symbolization

Với chuỗi RR dài:

$$
N=300
$$

toàn bộ khoảng giá trị RR của từng chuỗi được chia đều thành 6 mức:

$$
\mathcal{A}=\{0,1,2,3,4,5\}
$$

Mỗi RR interval được ánh xạ thành một symbol:

$$
RR_t \rightarrow s_t\in\mathcal{A}
$$

### 2. Pattern Construction

Tạo các pattern dài 3 beats:

$$
w_t=(s_t,s_{t+1},s_{t+2})
$$

Số pattern lý thuyết:

$$
6^3=216
$$

### 3. Pattern Classification

216 patterns được gom vào 3 families:

$$
0V:\quad (a,a,a)
$$

$$
1V:\quad (a,a,b)\ \text{hoặc}\ (a,b,b),\qquad a\neq b
$$

$$
2V:\quad (a,b,c),\qquad a\neq b,\ b\neq c
$$

Sau đó tính tỷ lệ xuất hiện:

$$
\%0V,\qquad \%1V,\qquad \%2V
$$

### 4. Complexity Measure

Authors đồng thời tính Shannon entropy của toàn bộ phân bố 216 patterns:

$$
H
=
-\sum_i p_i\log p_i
$$

nhưng entropy chỉ đo **độ phức tạp của phân bố**, trong khi các tỷ lệ:

$$
\boxed{
\%0V,\ \%2V
}
$$

cung cấp thông tin sinh lý cụ thể hơn về điều biến giao cảm và đối giao cảm.

Core representation:

$$
\boxed{
RR_t
\rightarrow
s_t
\rightarrow
w_t
\rightarrow
\{0V,1V,2V\}
\rightarrow
\text{pattern prevalence}
}
$$