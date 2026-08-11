# Paper Metadata
* **Title**: What symbolic dynamics do we get with a misplaced partition? On the validity of threshold crossings analysis of chaotic time-series
* **Authors**: Erik M. Bollt, Theodore Stanford, Ying-Cheng Lai, Karol Życzkowski
* **Year**: 2001
* **Keywords**: Symbol dynamics; Topological entropy; Kneading theory; Devil's staircase

# 1. Why

## Research Question
Một **phân vùng tùy ý (non-generating partition)** có phản ánh đúng động lực học của hệ thống?
$$
\boxed{
\text{Arbitrary non-generating partition}
\stackrel{?}{\longrightarrow}
\text{faithful symbolic dynamics}
}
$$

## Motivation
Generating partition là lý tưởng nhưng **khó xác định** trong thực tế. Do đó, các nghiên cứu thực nghiệm thường lạm dụng phương pháp **threshold-crossing tùy ý** để mã hóa chuỗi dữ liệu.

## Problem
Kỹ thuật threshold-crossing ngầm định chuỗi ký hiệu đại diện đúng hệ động lực gốc. Tuy nhiên, một ngưỡng tùy ý gây ra:
- Mất khả năng phân biệt các trạng thái (states).
- Thay đổi sai lệch allowed/forbidden words.
- Suy giảm topological entropy.
- Tạo ra cấu trúc ký hiệu mang tính "nhiễu" do phụ thuộc vào vách ngăn hơn là hệ gốc.

## Research Gap
Chưa làm rõ **mức độ và cơ chế bóp méo** biểu diễn ký hiệu khi đặt sai phân vùng (misplaced partition). Nghiên cứu giải quyết bằng cách cố tình dịch chuyển vách ngăn trên một hệ chuẩn (đã biết rõ generating partition) để đối chiếu và đo lường sai lệch.

# 2. What
## Nguyên nhân của kết quả ở Section 2–3

### Hiện tượng

Khi partition bị đặt lệch, symbolic representation thay đổi mạnh:

- topological entropy giảm;
- entropy thay đổi **không đơn điệu** theo mức lệch;
- nhiều trạng thái khác nhau có thể nhận cùng symbolic itinerary.

$$
\downarrow
$$

### Lý do

Dịch partition làm **đổi cách gán nhãn cho các trajectory**.

Vì vậy một số symbolic words có thể:

$$
\text{allowed}
\rightarrow
\text{forbidden}
\rightarrow
\text{allowed again}
$$

và nhiều trajectory khác nhau có thể bị gộp vào cùng một symbolic description.

$$
\downarrow
$$

### Bản chất

$$
\boxed{
\text{Partition không chỉ mã hóa dữ liệu;}
\text{ nó quyết định grammar mà ta quan sát được.}
}
$$

Do đó, nếu partition không phù hợp:

$$
\boxed{
\text{symbolic dynamics quan sát được}
\neq
\text{dynamics thật của hệ}
}
$$

Kết quả entropy và symbolic patterns có thể phản ánh **cách partition được chọn** nhiều hơn là cấu trúc thật của hệ.

## Generalization

Kết quả của tent map được mở rộng bằng hai mức evidence:

$$
\boxed{\text{Tent map}}
\rightarrow
\boxed{\text{Hénon map}}
\rightarrow
\boxed{\text{Experimental BZ data}}
$$

- Hénon cho thấy entropy vẫn phụ thuộc mạnh và phức tạp vào arbitrary threshold trong hệ 2D.
- BZ data cho thấy một threshold nhìn “tự nhiên” vẫn có thể gây under-representation mạnh.
- Simple threshold thường không phản ánh geometry phức tạp của generating partition trong state space.
- Chọn threshold có entropy lớn nhất cũng không đảm bảo đúng, vì representation/alphabet itself có thể quá hạn chế.

$$
\boxed{
\text{Lesson: threshold validity cannot be inferred from convenience, visual plausibility, or entropy maximization alone.}
}
$$

# 3. How

## 3.1 System / Model

Sử dụng tent map:

$$
x_{n+1}=1-2\left|x_n-\frac12\right|
$$

với generating partition đã biết:

$$
x_c=\frac12
$$

và topological entropy:

$$
h_T=\ln2.
$$

## 3.2 Symbolic Encoding / Partition

Dịch partition một lượng:

$$
p=x_c+d
$$

và encode:

$$
\phi_i=
\begin{cases}
a,&f^i(x)<p\\
b,&f^i(x)\ge p.
\end{cases}
$$

## 3.3 Numerical Estimation

Với mỗi $d$:

1. Generate một long orbit.
2. Encode thành symbolic sequence.
3. Đếm số unique words $w_n$ ở mỗi word length $n$.
4. Estimate:

$$
h_T(d)
\approx
\text{slope of }\log w_n\text{ vs }n.
$$

## 3.4 Core Observation

$$
h_T(0)\approx\ln2,
\qquad
h_T(\pm1/2)=0.
$$

Misplaced partitions làm giảm representation và tạo non-uniqueness, nhưng:

$$
\boxed{
h_T(d)\text{ is surprisingly non-monotonic}
}
$$

# 5. Conclusion

## Main Takeaways

- **Arbitrary threshold crossing không đảm bảo tạo ra faithful symbolic dynamics.**
- Misplaced partition có thể:
  - làm thay đổi symbolic grammar;
  - tạo / loại bỏ forbidden words;
  - làm giảm topological entropy;
  - khiến nhiều trạng thái khác nhau trở nên symbolically indistinguishable.
- Mức sai lệch không thay đổi đơn giản theo vị trí partition; entropy có thể **non-monotone** và có dạng **devil's staircase-like**.

$$
\boxed{
\text{Observed symbolic dynamics}
=
\text{Underlying dynamics}
+
\text{Effect of partition}
}
$$

## Assumptions

- Phân tích rigor chủ yếu dựa trên **deterministic, noise-free dynamics**.
- Tent map được dùng làm benchmark vì generating partition và true symbolic dynamics đã biết.
- Phân tích tập trung vào **partition misplacement**, không đồng thời xét ảnh hưởng của measurement/dynamical noise.

## Limitations

- Kết quả toán học chặt chẽ chủ yếu được chứng minh cho **tent map**.
- Không có phương pháp tổng quát để tìm generating partition cho experimental/high-dimensional systems.
- Hénon map và BZ data chủ yếu cung cấp **numerical/experimental evidence**, không phải proof tổng quát.
- Paper không giải quyết đầy đủ interaction giữa **partition error và noise**.

## Generalizability

Authors cho rằng cơ chế misrepresentation do non-generating partition có khả năng xuất hiện rộng hơn tent map.

Evidence được mở rộng theo:

$$
\boxed{
\text{Tent map}
\rightarrow
\text{Hénon map}
\rightarrow
\text{Experimental BZ data}
}
$$

Tuy nhiên, mức generalization nên được hiểu là **strong methodological warning**, không phải một theorem áp dụng cho mọi dynamical system.

$$
\boxed{
\text{Threshold-based symbolic results must be interpreted with caution}
}
$$

# 6. My Research

## Research Ideas

Với PPG trong drowsiness detection, không xem **symbolization là một preprocessing trung tính**.

Mỗi phương pháp symbolic encoding cần được đặt câu hỏi:

$$
\boxed{
\text{Representation này giữ lại dynamics nào và làm mất dynamics nào?}
}
$$

Đặc biệt cần đánh giá ảnh hưởng của:

- loại tín hiệu được symbol hóa: raw PPG, PPI, $\Delta PPI$, morphology,...
- vị trí và hình dạng partition;
- alphabet size;
- độ nhạy của kết quả khi partition thay đổi.

## Knowledge Contribution

Paper này cung cấp một nguyên tắc phương pháp luận quan trọng:

$$
\boxed{
\text{Symbolic result}
=
\text{Underlying dynamics}
+
\text{Effect of representation}
}
$$

Vì vậy, khi đánh giá một phương pháp Symbolic Time-Series Analysis, không chỉ hỏi:

> Feature có phân biệt được drowsiness hay không?

mà còn phải hỏi:

> Symbolic representation có cơ sở sinh lý / động lực học hợp lý hay chỉ là một arbitrary partition?

Một phương pháp mạnh hơn cần chứng minh rằng kết quả không chỉ là **encoding artifact**.

## Practical Implications

Khi thiết kế hoặc nhận xét một symbolic method cho PPG:

1. **Không mặc định threshold đơn giản là hợp lý** chỉ vì dễ triển khai.
2. **Không đánh giá partition chỉ bằng entropy hoặc classification accuracy cao.**
3. Thực hiện **sensitivity analysis**:

$$
\text{partition}
\rightarrow
\text{small perturbation}
\rightarrow
\text{symbolic patterns / statistics}
$$

để kiểm tra độ ổn định của kết quả.
4. Ưu tiên encoding có **physiological hoặc dynamical justification**.
5. Phân biệt rõ:

$$
\boxed{
\text{predictive usefulness}
\neq
\text{faithful dynamical representation}
}
$$

Một representation có thể dự đoán tốt nhưng chưa chắc phản ánh đúng underlying cardiovascular dynamics.


## Bảo vệ phương pháp luận khi dùng Symbolic Encoding

Sau Bollt et al. (2001), không nên giả định partition là faithful representation khi true dynamics không biết.

Thay vào đó, biện luận bằng nhiều lớp evidence:

1. **Theoretical / physiological justification**  
   Giải thích tại sao cách symbolization phù hợp với dynamics hoặc ý nghĩa sinh lý cần nghiên cứu.

2. **Partition sensitivity / robustness**  
   Perturb threshold, alphabet hoặc partition và kiểm tra kết luận có ổn định không.

3. **Surrogate testing**  
   Kiểm tra symbolic structure có vượt quá một null model phù hợp hay không.

4. **External validation**  
   Kiểm tra symbolic measures có liên hệ nhất quán với trạng thái / marker độc lập hay không.

5. **Alternative encodings**  
   So sánh nhiều representation hợp lý để tránh kết luận phụ thuộc vào một encoding duy nhất.

$$
\boxed{
\text{Justification}
+
\text{Robustness}
+
\text{Surrogates}
+
\text{External validity}
}
$$

Mục tiêu không phải chứng minh:

$$
\text{partition = true generating partition}
$$

mà là chứng minh:

$$
\boxed{
\text{representation is reasonable, robust, non-trivial, and interpretable}
}
$$