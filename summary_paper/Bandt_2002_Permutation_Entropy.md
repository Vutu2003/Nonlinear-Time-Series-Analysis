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

# 2. What

## Core Insight

Bandt & Pompe đề xuất đo complexity của time series bằng **thứ tự tương đối của các giá trị lân cận**, thay vì amplitude tuyệt đối.

Một local vector:

$$
(x_t,x_{t+1},\ldots,x_{t+n-1})
$$

được chuyển thành một **ordinal pattern / permutation**:

$$
\boxed{
\text{Local temporal values}
\rightarrow
\text{relative ordering}
\rightarrow
\text{permutation symbol}
}
$$

Sau đó complexity được đo từ phân bố xác suất của các permutation này.

Ý tưởng cốt lõi:

$$
\boxed{
\text{Permutation Entropy}
=
\text{Shannon entropy của ordinal-pattern distribution}
}
$$

Method cố ý:

- bỏ thông tin amplitude tuyệt đối;
- giữ thông tin về temporal ordering;
- không cần amplitude threshold hay generating partition được biết trước.

---

## Mathematical Foundation

Với time series:

$$
x_1,x_2,\ldots,x_T
$$

chọn embedding dimension / order $n$ và tạo các local vectors:

$$
W_t=(x_t,x_{t+1},\ldots,x_{t+n-1})
$$

Mỗi $W_t$ được ánh xạ thành một permutation $\pi_t$ dựa trên rank ordering của các phần tử.

Số possible ordinal patterns là:

$$
|\mathcal{A}|=n!
$$

Xác suất của permutation $\pi$ được estimate bằng relative frequency:

$$
p(\pi)
=
\frac{
\#\{t:W_t\text{ có ordinal type }\pi\}
}{
T-n+1
}
$$

Permutation entropy order $n$:

$$
H(n)
=
-\sum_{\pi}p(\pi)\log p(\pi)
$$

với:

$$
0\le H(n)\le \log(n!)
$$

- $H(n)=0$: chỉ một ordinal pattern chiếm ưu thế → dynamics rất regular.
- $H(n)=\log(n!)$: các patterns xuất hiện đồng đều → maximum ordinal uncertainty.

Authors còn định nghĩa permutation entropy per symbol:

$$
h_n=\frac{H(n)}{n-1}
$$

Parameter $n$ quyết định đồng thời:

$$
\boxed{
\text{temporal pattern length}
+
\text{alphabet size }n!
+
\text{data requirement}
}
$$

Vì vậy:

$$
n\uparrow
\Rightarrow
\text{richer temporal structure}
\quad\text{but}\quad
n!\uparrow
\Rightarrow
\text{more samples required}
$$

# 3. How

## 3.1 Algorithm

Input:

$$
x_1,x_2,\ldots,x_T
$$

Chọn embedding dimension / order $n$.

Với mỗi vị trí $t$, tạo local vector:

$$
W_t=(x_t,x_{t+1},\ldots,x_{t+n-1})
$$

Sau đó:

1. Xếp hạng các giá trị trong $W_t$.
2. Chuyển thứ tự tương đối thành một permutation $\pi_t$.
3. Lặp trên toàn bộ signal để tạo ordinal-pattern sequence.
4. Đếm số lần xuất hiện của từng permutation.
5. Estimate $p(\pi)$ bằng relative frequency.
6. Tính permutation entropy từ distribution $p(\pi)$.

Authors khuyến nghị trong practical applications:

$$
n=3,\ldots,7
$$

---

## 3.2 Mathematical Formulation

### Ordinal encoding

Mỗi vector:

$$
W_t=(x_t,\ldots,x_{t+n-1})
$$

được ánh xạ thành một permutation:

$$
W_t\rightarrow\pi_t
$$

biểu diễn rank ordering của $n$ giá trị.

Số possible patterns:

$$
n!
$$

### Pattern probability

$$
p(\pi)
=
\frac{
\#\{t:W_t\text{ có type }\pi\}
}{
T-n+1
}
$$

### Permutation Entropy

$$
H(n)
=
-\sum_{\pi}p(\pi)\log p(\pi)
$$

với:

$$
0\le H(n)\le\log(n!)
$$

### Permutation entropy per symbol

$$
h_n
=
\frac{H(n)}{n-1}
$$

Authors còn định nghĩa sorting entropy:

$$
d_n
=
H(n)-H(n-1)
$$

nhưng đây không phải quantity chính trong implementation PE cơ bản.

---

## 3.3 End-to-End Pipeline

$$
\boxed{
\text{Raw time series}
\rightarrow
\text{Local windows of length }n
\rightarrow
\text{Ordinal ranking}
}
$$

$$
\boxed{
\rightarrow
\text{Permutation symbols}
\rightarrow
\text{Pattern frequencies}
\rightarrow
p(\pi)
\rightarrow
H(n)
}
$$

Theo symbolic-encoding view:

$$
\boxed{
x_t
\rightarrow
W_t
\rightarrow
\pi_t
\rightarrow
p(\pi)
\rightarrow
\text{Permutation Entropy}
}
$$

---

## 3.4 Computational Complexity

Paper không đưa một Big-O analysis đầy đủ.

Authors nhấn mạnh:

- calculation rất nhanh;
- mỗi pair of values chỉ cần được so sánh một lần trong optimized implementation;
- computational time không phải bottleneck chính.

Bottleneck quan trọng hơn là số possible patterns:

$$
n!
$$

Khi $n$ tăng:

$$
n!\uparrow
\Rightarrow
\text{memory requirement và data requirement tăng rất nhanh}
$$

Để estimate $H(n)$ đáng tin cậy:

$$
\boxed{
T \gg n!
}
$$

Trong chaotic-map experiments, authors dùng:

$$
T=10^6
$$

để estimate các orders lớn.

---

## 3.5 Implementation Notes

- Paper gốc dùng consecutive samples:

$$
(x_t,x_{t+1},\ldots,x_{t+n-1})
$$

tức delay mặc định là $1$.

- Authors khuyến nghị:

$$
n=3,\ldots,7
$$

cho practical applications.

- Các giá trị bằng nhau (ties) gây ambiguity trong ranking.

Paper giả định ties hiếm khi distribution liên tục; nếu có, authors đề xuất thêm perturbation ngẫu nhiên rất nhỏ để phá ties.

- $n$ càng lớn:
  - capture temporal structure dài hơn;
  - nhưng alphabet tăng thành $n!$;
  - cần nhiều data hơn để estimate probabilities.

- Không cần amplitude threshold hay generating partition được biết trước.

- PE invariant dưới strictly monotonic transformations:

$$
y_t=f(x_t)
$$

nếu $f$ strictly increasing/decreasing thì ordinal structure và PE không đổi.

- Finite-sample bias xuất hiện khi:

$$
T
$$

quá nhỏ so với:

$$
n!
$$

nên việc chọn $n$ phải phù hợp với độ dài dữ liệu.

# 4. Experiments

## Setups

### Speech Signal

- Dữ liệu: câu nói dài khoảng 4 s, sampling frequency 11 kHz.
- Sliding window:

$$
T_{\text{win}}=512
$$

samples, tương đương khoảng 46 ms.

- Window shift: 1 sample.
- Permutation entropy được tính với các order thấp:

$$
n=3,4,5
$$

- So sánh với Zero-Crossing Rate (ZCR).

### Chaotic Time Series

- Hệ chính: logistic map

$$
x_{t+1}=r x_t(1-x_t)
$$

với:

$$
3.5\le r\le4
$$

- Quét 5001 giá trị của $r$.
- So sánh permutation entropy:

$$
h_6,\;h_{12}
$$

với Lyapunov exponent.
- Với nghiên cứu finite-sample tại $r=4$, authors dùng nhiều độ dài:

$$
T=10^2,\ldots,10^6
$$

và lặp 1000 time series cho mỗi $T$.

---

## Results

### Speech Signal

- Noise và unvoiced sounds có normalized PE gần:

$$
1
$$

- Voiced sounds làm PE giảm rõ rệt:

$$
\text{more regular temporal structure}
\Rightarrow
\text{lower PE}
$$

- PE nhận diện một số transitions tốt hơn ZCR.
- Kết quả tương đối ổn khi thay đổi:
  - window length;
  - sampling frequency;
  - observational noise;
  - permutation order $n=3,\ldots,7$.
- Phương pháp có computational cost thấp và phù hợp cho real-time analysis.

### Chaotic Time Series

Permutation entropy có cấu trúc rất giống Lyapunov exponent:

$$
\boxed{
\text{PE} \approx \text{dynamical complexity}
}
$$

trên phần lớn chaotic regime của logistic map.

- Periodic windows:

$$
\text{restricted ordinal patterns}
\Rightarrow
\text{low PE}
$$

- Chaotic regions:

$$
\text{greater ordinal-pattern diversity}
\Rightarrow
\text{higher PE}
$$

- $h_6$ và $h_{12}$ cho overall behavior khá giống nhau, cho thấy low-order PE có thể đủ trong applications.
- $h_6$ có thể được estimate khá tin cậy với khoảng:

$$
T\approx1000
$$

samples.

Finite-sample bias xuất hiện khi:

$$
T
$$

quá nhỏ so với:

$$
n!
$$

---

## Discussion

Hai experiments kiểm chứng PE ở hai góc độ bổ sung:

$$
\boxed{
\text{Real-world applicability}
+
\text{Dynamical validity}
}
$$

Speech experiment cho thấy PE:

- đơn giản;
- nhanh;
- robust;
- usable trực tiếp trên noisy real-world signals.

Chaotic-system experiment cho thấy ordinal-pattern complexity có thể phản ánh cấu trúc động lực học tương tự Lyapunov exponent.

Trade-off thực tế quan trọng:

$$
n\uparrow
\Rightarrow
\text{capture richer temporal patterns}
$$

nhưng:

$$
n!\uparrow
\Rightarrow
\text{need much more data}
$$

Do đó:

$$
\boxed{
\text{low-order PE can provide a practical balance between temporal detail and statistical reliability}
}
$$

Kết quả tổng quát:

$$
\boxed{
\text{Ordinal representation is simple enough for real data}
\\
\text{but rich enough to reflect nonlinear dynamical complexity}
}
$$

# 5. Conclusion

## Assumptions

- Time series cần cho phép xác định **relative ordering** giữa các giá trị trong local window.
- Authors giả định ties hiếm; nếu có thể thêm perturbation rất nhỏ để phá ties.
- Probability của ordinal patterns được ước lượng từ finite observations, nên cần đủ dữ liệu so với số possible patterns:

$$
n!
$$

- Với interpretation xác suất dài hạn, authors giả định một weak stationarity condition cho các ordinal relations.

## Limitations

- Số possible ordinal patterns tăng factorial:

$$
n!
$$

nên order $n$ lớn đòi hỏi sequence dài hơn nhiều.

- Finite-sample bias xuất hiện khi:

$$
T \text{ không đủ lớn so với } n!
$$

- PE không giữ:
  - absolute amplitude;
  - amplitude differences;

mà chỉ giữ relative ordering.

- Ties gây ambiguity trong ordinal ranking.

- PE không hoàn toàn immune với noise:

$$
\text{noise changes ordering}
\Rightarrow
\text{PE changes}
$$

Đặc biệt với near-constant hoặc low-period signals, một lượng noise nhỏ có thể tạo nhiều ordinal patterns mới và làm PE tăng mạnh.

- Quan hệ giữa PE và dynamical complexity được paper kiểm chứng mạnh trên chaotic systems, nhưng không có nghĩa PE luôn bằng Lyapunov exponent hoặc KS entropy trong mọi hệ.

## Main Takeaways

Permutation Entropy cung cấp một complexity measure:

$$
\boxed{
\text{simple}
+
\text{fast}
+
\text{robust}
+
\text{directly applicable to real-world time series}
}
$$

Cốt lõi của phương pháp là:

$$
\boxed{
\text{discard amplitude}
+
\text{preserve temporal ordering}
}
$$

Kết quả thực nghiệm cho thấy PE:

- phân biệt được regular / periodic và chaotic behavior;
- có cấu trúc tương tự Lyapunov exponent trên logistic map;
- hoạt động tốt trên real-world speech signal;
- tương đối robust trước observational và dynamical noise;
- phù hợp với large datasets và applications cần ít preprocessing / fine-tuning.

# 6. My Research

## Research Ideas

Bandt–Pompe gợi ý một hướng rất phù hợp cho symbolic analysis trên PPG/PPI:

$$
\text{Physiological time series}
\rightarrow
\text{Ordinal patterns}
\rightarrow
\text{Pattern distribution}
\rightarrow
\text{Permutation Entropy}
$$

Các hướng có thể triển khai:

- Đánh giá thay đổi của ordinal-pattern distribution giữa alert và drowsy.
- So sánh PE giữa các trạng thái thay vì chỉ dùng raw amplitude features.
- Kiểm tra sensitivity theo pattern order $n$ và window length.
- Khảo sát xem drowsiness có làm temporal organization trở nên:
  - regular hơn;
  - random hơn;
  - hay chỉ thay đổi distribution của một số ordinal motifs cụ thể.
- Không chỉ dùng PE như một scalar feature, mà phân tích trực tiếp các ordinal patterns để tăng interpretability.

Một câu hỏi nghiên cứu tiềm năng:

$$
\boxed{
\text{Does drowsiness alter the ordinal organization of beat-to-beat cardiovascular dynamics?}
}
$$

## Knowledge Contribution

Bandt–Pompe bổ sung một hướng symbolic encoding khác với amplitude partition:

$$
\boxed{
\text{Amplitude-based encoding}
\rightarrow
\text{Ordinal-based encoding}
}
$$

Điểm quan trọng nhất cho nghiên cứu của tôi:

$$
\boxed{
\text{Representation can preserve temporal order while discarding absolute amplitude}
}
$$

Điều này mở ra một symbolic representation:

- ít phụ thuộc vào amplitude scale;
- invariant với monotonic transformations;
- đơn giản và computationally efficient;
- phù hợp với noisy physiological time series.

Về phương pháp luận, paper cho thấy:

$$
\boxed{
\text{Symbolic encoding không nhất thiết phải bắt đầu bằng amplitude thresholds}
}
$$

mà có thể được xây trực tiếp từ **temporal relations giữa các samples**.

Do đó, khi thiết kế symbolic pipeline cho PPG/PPI, cần xem ordinal encoding như một candidate representation và đánh giá:

$$
\boxed{
\text{What physiological information is preserved?}
\quad
\text{vs.}
\quad
\text{What amplitude information is discarded?}
}
$$