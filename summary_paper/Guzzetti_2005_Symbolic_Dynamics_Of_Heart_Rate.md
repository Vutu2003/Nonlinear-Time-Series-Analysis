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

# 3. How

## 3.1 Algorithm

Với mỗi chuỗi RR dài:

$$
N=300
$$

thực hiện:

1. Xác định:

$$
RR_{\min},\quad RR_{\max}
$$

2. Chia đều toàn bộ khoảng RR thành 6 mức:

$$
\mathcal{A}=\{0,1,2,3,4,5\}
$$

3. Ánh xạ mỗi RR interval thành một symbol:

$$
RR_t \rightarrow s_t
$$

4. Tạo các pattern dài 3 beats:

$$
w_t=(s_t,s_{t+1},s_{t+2})
$$

5. Phân loại mỗi pattern thành:

- 0V: không variation;
- 1V: một variation;
- 2V: hai variations.

6. Tính tỷ lệ xuất hiện:

$$
\%0V,\qquad \%1V,\qquad \%2V
$$

7. Tính thêm Shannon entropy của phân bố toàn bộ 216 patterns:

$$
H=-\sum_i p_i\log p_i
$$

8. So sánh symbolic features giữa các điều kiện sinh lý/dược lý hoặc giữa baseline và trước biến cố tim.

---

## 3.2 Mathematical Formulation

### Symbolization

Với:

$$
R=RR_{\max}-RR_{\min}
$$

chia range thành 6 khoảng có độ rộng:

$$
\Delta=\frac{R}{6}
$$

Mỗi:

$$
RR_t
$$

được ánh xạ thành:

$$
s_t\in\{0,1,2,3,4,5\}
$$

tùy theo khoảng mà nó thuộc vào.

### Pattern Construction

$$
w_t=(s_t,s_{t+1},s_{t+2})
$$

Số possible words:

$$
6^3=216
$$

### Pattern Families

$$
0V:\quad s_t=s_{t+1}=s_{t+2}
$$

$$
1V:\quad
\begin{cases}
s_t=s_{t+1}\neq s_{t+2}\\
\text{hoặc}\\
s_t\neq s_{t+1}=s_{t+2}
\end{cases}
$$

$$
2V:\quad
s_t\neq s_{t+1}
\quad\text{và}\quad
s_{t+1}\neq s_{t+2}
$$

Tỷ lệ một family $C$:

$$
\%C
=
\frac{N_C}{N_{\text{patterns}}}\times100
$$

với:

$$
N_{\text{patterns}}=N-2
$$

nếu dùng sliding window từng beat.

---

## 3.3 End-to-End Pipeline

$$
\text{RR intervals}
$$

$$
\downarrow
$$

$$
\text{6-level uniform quantization}
$$

$$
\downarrow
$$

$$
(s_1,s_2,\ldots,s_N)
$$

$$
\downarrow
$$

$$
(s_t,s_{t+1},s_{t+2})
$$

$$
\downarrow
$$

$$
\{0V,1V,2V\}
$$

$$
\downarrow
$$

$$
\boxed{
\%0V,\ \%1V,\ \%2V
}
$$

Song song:

$$
\text{216-pattern distribution}
\rightarrow
H_{\text{Shannon}}
$$

Và để kiểm tra cấu trúc thời gian:

$$
\text{original RR}
\rightarrow
\text{shuffle}
\rightarrow
\text{surrogate RR}
\rightarrow
\text{symbolic analysis}
$$

sau đó so sánh original với surrogate.

---

## 3.4 Computational Complexity

Với chuỗi dài $N$ và alphabet size cố định bằng 6:

- tìm min/max: $O(N)$;
- symbolization: $O(N)$;
- tạo và phân loại 3-beat patterns: $O(N)$;
- đếm pattern / family: $O(N)$.

Do đó tổng thể:

$$
\boxed{
O(N)
}
$$

Memory có thể giữ ở mức:

$$
O(N)
$$

hoặc gần:

$$
O(1)
$$

ngoài input nếu xử lý streaming.

---

## 3.5 Implementation Notes

- Mỗi subject và mỗi experimental condition có **RR range riêng**, nên các ngưỡng symbolization cũng khác nhau.
- Quantization là **uniform theo amplitude range**, không phải ordinal ranking.
- Word length được cố định:

$$
L=3
$$

- Alphabet size:

$$
\xi=6
$$

- Có:

$$
216
$$

possible symbolic words, nhưng kết quả sinh lý chính được tóm tắt bằng:

$$
\%0V,\quad \%2V
$$

- 1V được tính nhưng không cho thay đổi rõ trong các autonomic tests của paper.
- Với ectopic beats, paper nhấn mạnh cần correction; trong study họ dùng linear interpolation khi ectopic beats dưới ngưỡng cho phép.
- Surrogate data được tạo bằng cách shuffle temporal order, nhằm kiểm tra liệu các pattern quan sát được có phụ thuộc vào cấu trúc thời gian hay chỉ xuất hiện ngẫu nhiên.
- Không nên diễn giải:

$$
0V=\text{sympathetic}
$$

hay:

$$
2V=\text{parasympathetic}
$$

một cách tuyệt đối; chúng là các symbolic markers được validate dưới các điều kiện sinh lý và dược lý cụ thể.

# 4. Experiments

## Setups

Paper gồm 2 nhóm thực nghiệm chính.

### 1. Autonomic Tests — Healthy Subjects

Nghiên cứu trên:

$$
N=60
$$

người khỏe mạnh.

Mỗi chuỗi phân tích gồm:

$$
300\ \text{RR intervals}
$$

Các điều kiện được thiết kế để thay đổi điều biến thần kinh tự chủ:

- Rest: trạng thái nghỉ.
- Tilt test: tăng sympathetic modulation và vagal withdrawal.
- Handgrip: tăng sympathetic modulation.
- High-dose atropine: parasympathetic blockade.
- Low-dose atropine: tác động parasympathetic ở liều thấp.
- Phenylephrine: tăng reflex parasympathetic modulation.
- Nitroprusside: tăng reflex sympathetic modulation.

Trên mỗi chuỗi, authors tính:

$$
\%0V,\quad \%1V,\quad \%2V
$$

và Shannon entropy.

Ngoài ra, các chỉ số HRV tuyến tính trong miền thời gian và miền tần số cũng được tính để so sánh.

---

### 2. Patients Before Major Arrhythmias

Authors thu 28 chuỗi RR trước các biến cố:

$$
VT/VF
$$

ở bệnh nhân có implantable cardioverter-defibrillator (ICD).

Sau khi loại các recordings không phù hợp:

$$
21\ \text{patients}
$$

được đưa vào phân tích.

So sánh:

$$
\text{Baseline}
\quad \text{vs} \quad
\text{300 beats before VT/VF}
$$

Các feature chính:

$$
\%0V,\quad \%2V,\quad H_{\text{Shannon}}
$$

Ngoài ra, 15 surrogate series cho mỗi original series được tạo bằng cách shuffle temporal order để kiểm tra liệu symbolic structure có xuất hiện do chance hay không.

---

## Results

### Autonomic Tests

Trong các điều kiện tăng sympathetic modulation hoặc vagal withdrawal:

$$
\boxed{
0V\uparrow
}
$$

và:

$$
\boxed{
2V\downarrow
}
$$

Đặc biệt được quan sát trong:

- tilt;
- handgrip;
- high-dose atropine;
- nitroprusside.

Ngược lại, khi parasympathetic modulation tăng:

$$
\boxed{
2V\uparrow
}
$$

ví dụ trong phenylephrine infusion.

1V không cho thấy thay đổi có ý nghĩa thống kê rõ ràng.

Do đó:

$$
\boxed{
0V \sim \text{sympathetic prevalence}
}
$$

$$
\boxed{
2V \sim \text{parasympathetic/vagal prevalence}
}
$$

trong các điều kiện validation của nghiên cứu.

Shannon entropy cũng thay đổi trong một số autonomic tests, nhưng kém đặc hiệu hơn pattern classification trong việc phân biệt loại autonomic modulation.

---

### Before Major Arrhythmias

Trước VT/VF:

$$
0V:
24.4\pm2.9\%
\rightarrow
41.6\pm3.9\%
$$

với:

$$
P<0.01
$$

cho thấy sự gia tăng rõ của nonvariable patterns.

Trong khi đó:

$$
2V:
1.5\pm0.6\%
\rightarrow
3.2\pm1.0\%
$$

không thay đổi có ý nghĩa thống kê:

$$
P=0.14
$$

Shannon entropy giảm:

$$
3.59\pm0.07
\rightarrow
3.19\pm0.08
$$

với:

$$
P<0.05
$$

Các chỉ số HRV phổ truyền thống không cho thấy thay đổi đáng kể tương ứng.

---

## Discussion

Kết quả healthy-subject experiments hỗ trợ interpretation:

$$
\boxed{
\text{sympathetic dominance}
\rightarrow
0V\uparrow,\ 2V\downarrow
}
$$

và:

$$
\boxed{
\text{parasympathetic dominance}
\rightarrow
2V\uparrow,\ 0V\downarrow
}
$$

Điểm quan trọng là symbolic analysis không chỉ đo:

$$
\text{complexity}
$$

mà còn xác định:

$$
\boxed{
\text{loại local temporal pattern đang chiếm ưu thế}
}
$$

nên có khả năng diễn giải sinh lý tốt hơn một scalar entropy đơn lẻ.

Trước major arrhythmias, 0V tăng nhưng 2V không giảm tương ứng:

$$
\boxed{
0V\uparrow
\quad \text{nhưng} \quad
2V\not\downarrow
}
$$

Điều này gợi ý rằng trong trạng thái bệnh lý, sympathetic và parasympathetic modulation không nhất thiết hoạt động theo cơ chế reciprocal đơn giản.

Scientific insight chính:

$$
\boxed{
\text{Short symbolic patterns có thể phát hiện
những thay đổi autonomic ngắn hạn mà standard HRV analysis có thể bỏ sót.}
}
$$

Surrogate analysis bổ sung bằng chứng rằng các symbolic patterns quan sát được có liên quan đến temporal organization của RR series, thay vì chỉ do distribution của các RR values.

# 5. Conclusion

## Assumptions

Phương pháp dựa trên một số giả định chính:

- Chuỗi RR phản ánh một phần **điều hòa thần kinh tự chủ của tim (cardiac autonomic modulation)**.
- Các thay đổi ngắn hạn trong RR có thể được biểu diễn bằng các **mẫu ký hiệu dài 3 nhịp (3-beat symbolic patterns)**.
- Việc chia toàn bộ RR range thành 6 mức là đủ để giữ những thay đổi quan trọng liên quan đến autonomic modulation.
- Tỷ lệ các family:

$$
\%0V,\quad \%2V
$$

có thể được dùng như các symbolic markers của sympathetic và parasympathetic modulation sau khi đã được validate bằng các autonomic tests.
- Phương pháp giả định nút xoang (SA node) hoạt động bình thường để RR dynamics còn phản ánh cardiac autonomic control.

## Limitations

- 0V và 2V không phải phép đo trực tiếp sympathetic hoặc parasympathetic nerve activity.
- Mapping:

$$
0V \leftrightarrow \text{sympathetic}
$$

và:

$$
2V \leftrightarrow \text{parasympathetic}
$$

là association được validate trong các điều kiện cụ thể, không phải quan hệ tuyệt đối.
- Kết quả phụ thuộc vào lựa chọn:

$$
\text{6 levels} + \text{3-beat patterns}
$$

- Ectopic beats có thể làm giảm số pattern và làm sai lệch complexity, nên cần correction.
- Trong nhóm ICD, baseline không được ghi ngay trước cùng một loại hoạt động hằng ngày nên không thể kết luận sympathetic activation trước VT/VF là đặc hiệu cho arrhythmia.
- Phương pháp chỉ phản ánh RR dynamics và không đo trực tiếp các đặc tính tái cực cơ tim (myocardial repolarization) liên quan đến cơ chế gây arrhythmia.

Ý chính:

$$
\boxed{
\text{Symbolic pattern classification có thể cung cấp
thông tin sinh lý cụ thể hơn một global complexity measure.}
}
$$

# 6. My Research

## Research Ideas

Có thể chuyển framework từ RR sang **khoảng giữa các nhịp mạch (pulse-to-pulse interval, PPI)** được trích từ PPG:

$$
\text{PPG}
\rightarrow
\text{pulse detection}
\rightarrow
PPI_t
\rightarrow
\text{symbolization}
\rightarrow
\{0V,1V,2V\}
$$

Các hướng nghiên cứu tiềm năng:

- Kiểm tra liệu:

$$
\%0V,\quad \%2V
$$

trên PPI có thay đổi theo trạng thái alert/drowsy hay không.
- So sánh symbolic features với các chỉ số HRV/PRV truyền thống và entropy-based features.
- Kiểm tra robustness theo:
  - window length;
  - số mức quantization;
  - signal quality;
  - motion artifact;
  - inter-subject variability.
- Dùng surrogate data để kiểm tra liệu sự thay đổi feature đến từ temporal organization hay chỉ từ distribution của PPI.
- Mở rộng từ 0V/1V/2V sang các pattern families mới phù hợp hơn với physiological dynamics của PPG.

## Knowledge Contribution

Contribution tiềm năng không chỉ là áp dụng lại 0V/2V cho PPG, mà là kiểm tra:

$$
\boxed{
\text{Liệu symbolic organization của PPI có chứa
thông tin về autonomic changes liên quan đến drowsiness?}
}
$$

Có thể chuyển từ:

$$
\text{PPG}
\rightarrow
\text{global complexity feature}
$$

sang:

$$
\boxed{
\text{PPG/PPI}
\rightarrow
\text{physiologically interpretable local pattern features}
}
$$

Hướng đóng góp mạnh hơn:

$$
\boxed{
\text{Physiology-driven symbolic biomarker}
}
$$

thay vì chỉ:

$$
\boxed{
\text{generic nonlinear feature}
}
$$

Trong đó Guzzetti 2005 cung cấp template:

$$
\text{physiological hypothesis}
\rightarrow
\text{symbolic representation}
\rightarrow
\text{pattern family}
\rightarrow
\text{experimental validation}
$$