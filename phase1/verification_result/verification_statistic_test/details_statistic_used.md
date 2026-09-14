
# Statistical Framework Used in This Study

## 1. Mục tiêu của khung thống kê

Nghiên cứu này không xem từng cửa sổ PPG như một quan sát thống kê độc lập.

Cấu trúc phân tích được xây dựng theo ba tầng:

```text
PPG window
→ tính metric phi tuyến trên từng window
→ tổng hợp trong từng session × state
→ so sánh Awake và Drowsy ở cấp session
````

Nguyên tắc chính:

* **Window** là đơn vị tính toán metric.
* **Session** là đơn vị suy luận thống kê chính.
* Awake và Drowsy được so sánh theo thiết kế **paired** trong cùng session.
* Các kiểm định không dựa vào giả định phân phối chuẩn của metric.
* Không chỉ báo cáo `p-value`, mà kết hợp:

  * paired effect,
  * bootstrap confidence interval,
  * Wilcoxon signed-rank,
  * rank-biserial effect size,
  * direction count,
  * BH-FDR correction.

Mục tiêu không phải chỉ trả lời:

> “Có khác biệt thống kê hay không?”

mà đồng thời trả lời:

1. khác biệt theo hướng nào?
2. độ lớn khoảng bao nhiêu?
3. mức độ nhất quán giữa các session như thế nào?
4. kết luận có phụ thuộc vào outlier hoặc giả định phân phối hay không?
5. kết luận có còn đứng vững sau multiple-comparison correction hay không?

---

# 2. Tại sao không dùng từng window làm sample độc lập?

Một session có thể chứa nhiều cửa sổ PPG 60 s.

Các window trong cùng session:

* đến từ cùng một người;
* cùng thời điểm đo;
* gần nhau theo thời gian;
* chịu chung physiological context;
* do đó không thể giả định độc lập hoàn toàn.

Nếu coi hàng trăm hoặc hàng nghìn window là các sample độc lập:

```text
n ≈ 900 windows
```

thay vì:

```text
n ≈ 20 paired sessions
```

thì sẽ tạo ra **pseudo-replication**.

Hậu quả có thể là:

* standard error bị đánh giá quá nhỏ;
* p-value quá nhỏ một cách giả tạo;
* confidence interval quá hẹp;
* mức độ chắc chắn của kết quả bị phóng đại.

Do đó nghiên cứu sử dụng:

$$
X_{i,s}
=
\operatorname{median}
\left(
x_{i,s,1},x_{i,s,2},...,x_{i,s,n}
\right)
$$

trong đó:

* \(i\): session;
* \(s\): trạng thái Awake hoặc Drowsy;
* \(x\): metric của từng window.

Sau đó mới xây dựng paired contrast:

$$
\Delta_i
=
X_{i,\mathrm{Drowsy}}
-
X_{i,\mathrm{Awake}}
$$

Mọi suy luận chính được thực hiện trên tập:

$$
\{\Delta_1,\Delta_2,\ldots,\Delta_N\}
$$

với \(N\approx20\) sessions.

---

# 3. Vì sao dùng median trong mỗi session thay vì mean?

Các metric phi tuyến như:

* prediction error,
* correlation skill,
* recurrence measures,
* Lyapunov exponent

thường không có phân phối đối xứng hoàn hảo ở cấp window.

Một vài window có thể có:

* nhiễu còn sót lại;
* dynamics bất thường;
* estimate không ổn định;
* giá trị cực đoan.

Mean:

$$
\bar{x}
=
\frac{1}{n}\sum_{j=1}^{n}x_j
$$

có thể bị ảnh hưởng mạnh bởi các giá trị cực đoan.

Median:

$$
\tilde{x}
=
\operatorname{median}(x_1,...,x_n)
$$

đại diện cho **window điển hình của session** và có robustness cao hơn đối với outlier.

Do câu hỏi khoa học là:

> trạng thái động lực học điển hình của PPG trong Awake và Drowsy khác nhau như thế nào?

median là lựa chọn phù hợp.

Điều này đặc biệt hữu ích khi số lượng window Awake và Drowsy trong một session không hoàn toàn bằng nhau.

---

# 4. Paired effect: \(\Delta = Drowsy - Awake\)

Đối với mỗi session:

$$
\Delta_i =
X_{i,D}-X_{i,A}
$$

Quy ước trong toàn bộ nghiên cứu:

$$
\boxed{\Delta = Drowsy-Awake}
$$

Do đó:

```text
Δ < 0
→ metric giảm khi chuyển Awake → Drowsy

Δ > 0
→ metric tăng khi chuyển Awake → Drowsy
```

Ví dụ:

```text
Mean_CC Δ < 0
→ forecast correlation thấp hơn trong Drowsy

Mean_NRMSE Δ > 0
→ prediction error cao hơn trong Drowsy

DET Δ < 0
→ diagonal recurrence organization giảm

LLE Δ < 0
→ local trajectory divergence giảm
```

Điểm quan trọng là statistical test được thực hiện trên **paired differences**, không phải hai nhóm Awake và Drowsy độc lập.

---

# 5. Median paired effect

Headline effect được mô tả bằng:

$$
\tilde{\Delta}
=
\operatorname{median}
(\Delta_1,\ldots,\Delta_N)
$$

Thay vì mean paired difference:

$$
\bar{\Delta}
=
\frac{1}{N}\sum_i\Delta_i
$$

median được dùng vì:

* \(N\) nhỏ;
* paired effects có thể không Gaussian;
* một hoặc hai session đảo chiều không nên chi phối toàn bộ effect estimate;
* phù hợp với cách tổng hợp robust ở cấp session.

Median paired effect trả lời:

> Một session điển hình thay đổi bao nhiêu từ Awake sang Drowsy?

---

# 6. Bootstrap 95% Confidence Interval

## 6.1. Mục đích

Bootstrap được dùng để đánh giá độ bất định của median paired effect mà không phải giả định:

$$
\Delta_i \sim N(\mu,\sigma^2)
$$

Đây là ưu điểm quan trọng vì:

* sample size khoảng 20 session;
* nonlinear metrics thường không Gaussian;
* median không có standard error đơn giản như mean.

---

## 6.2. Bootstrap procedure

Giả sử có:

$$
N=20
$$

paired-session effects:

$$
\Delta_1,...,\Delta_{20}
$$

Mỗi bootstrap iteration:

1. lấy mẫu lại **20 paired-session effects với replacement**;
2. tính median:

$$
\tilde{\Delta}^{*(b)}
$$

3. lặp lại:

$$
B=20,000
$$

lần.

Ta thu được bootstrap distribution:

$$
\tilde{\Delta}^{*(1)},
...,
\tilde{\Delta}^{*(20,000)}
$$

Percentile 95% CI:

$$
CI_{95\%}
=
[
Q_{0.025},
Q_{0.975}
]
$$

trong đó \(Q_p\) là percentile thứ \(p\) của bootstrap distribution.

---

## 6.3. Ý nghĩa

Ví dụ:

$$
\tilde{\Delta}_{LLE}=-0.0376
$$

và:

$$
95\%CI=[-0.0537,-0.0230]
$$

cho thấy:

* effect trung tâm là âm;
* bootstrap distribution nằm chủ yếu dưới 0;
* dấu của effect khá ổn định đối với sampling uncertainty ở cấp session.

---

# 7. Tại sao bootstrap phải resample session chứ không resample window?

Nếu resample từng window:

```text
window 1
window 2
...
window 901
```

ta lại giả định các window độc lập.

Điều đó không phù hợp với cấu trúc dữ liệu.

Bootstrap chính được thực hiện trên:

```text
paired-session Δ
```

do session là inference unit.

Tức là toàn bộ Awake–Drowsy relationship của một session được giữ nguyên trong mỗi bootstrap sample.

---

# 8. Two-sided Wilcoxon Signed-Rank Test

## 8.1. Giả thuyết

Với paired effects:

$$
\Delta_i
$$

kiểm định:

$$
H_0:
\text{phân phối paired differences đối xứng quanh }0
$$

so với:

$$
H_1:
\text{phân phối paired differences không centered quanh }0
$$

Nghiên cứu dùng **two-sided test**.

Điều này quan trọng vì statistical significance không được định nghĩa trước dựa trên hướng mong muốn.

Ví dụ, trước khi kiểm định:

```text
không giả định bắt buộc DET phải giảm
không giả định bắt buộc LLE phải giảm
```

Cả hai hướng đều được phép tạo bằng chứng chống lại \(H_0\).

---

# 9. Wilcoxon được tính như thế nào?

Với paired differences:

$$
\Delta_1,...,\Delta_N
$$

### Bước 1

Loại các zero differences theo quy tắc của implementation.

### Bước 2

Lấy absolute values:

$$
|\Delta_i|
$$

### Bước 3

Xếp hạng:

$$
R_i=\operatorname{rank}(|\Delta_i|)
$$

### Bước 4

Tính tổng rank của các effect dương:

$$
W_+
=
\sum_{\Delta_i>0}R_i
$$

và effect âm:

$$
W_-
=
\sum_{\Delta_i<0}R_i
$$

Nếu không có systematic effect:

$$
W_+
\approx
W_-
$$

Nếu effect chủ yếu âm:

$$
W_-
\gg W_+
$$

Nếu effect chủ yếu dương:

$$
W_+
\gg W_-
$$

Two-sided p-value đánh giá mức độ bất thường của sự mất cân bằng này dưới null hypothesis.

---

# 10. Vì sao Wilcoxon thay vì paired t-test?

Paired t-test kiểm định mean difference:

$$
H_0:E(\Delta)=0
$$

và dựa mạnh hơn vào tính phù hợp của mean và distribution của paired effects.

Với:

```text
N ≈ 20
```

và nonlinear metrics có thể:

* skewed;
* heavy-tailed;
* chứa outlier;
* không Gaussian;

Wilcoxon signed-rank là lựa chọn thận trọng hơn.

Wilcoxon cũng phù hợp với triết lý chung của nghiên cứu:

```text
median effect
+
rank-based inference
+
bootstrap uncertainty
```

thay vì phụ thuộc hoàn toàn vào moment-based parametric statistics.

---

# 11. Two-sided không có nghĩa là không được diễn giải direction

Two-sided Wilcoxon trả lời:

> Có bằng chứng về systematic paired difference hay không?

Sau khi kiểm định, direction được xác định từ:

$$
\tilde{\Delta}
$$

và paired effects.

Ví dụ:

$$
p<0.05
$$

và:

$$
\tilde{\Delta}<0
$$

cho phép diễn giải:

> có systematic Awake–Drowsy difference và direction quan sát được là giảm.

Việc dùng two-sided test tránh tình trạng giảm p-value bằng cách chọn one-sided hypothesis sau khi đã nhìn thấy dữ liệu.

---

# 12. Matched-pairs rank-biserial correlation

P-value chỉ cho biết mức độ không tương thích với null.

Nó không cho biết effect mạnh hay yếu.

Do đó nghiên cứu báo cáo:

$$
r_{rb}
$$

matched-pairs rank-biserial correlation.

Một định nghĩa tương đương thường dùng là:

$$
r_{rb}
=
\frac{W_+-W_-}{W_++W_-}
$$

với quy ước dấu phụ thuộc vào hướng định nghĩa paired difference.

Trong nghiên cứu này:

$$
\Delta=Drowsy-Awake
$$

nên:

```text
r_rb < 0
→ ranked differences nghiêng về giảm trong Drowsy

r_rb > 0
→ ranked differences nghiêng về tăng trong Drowsy
```

Range:

$$
-1\le r_{rb}\le1
$$

Interpretation định tính:

```text
|r_rb| gần 0
→ ít directional rank dominance

|r_rb| lớn
→ một direction chiếm ưu thế rõ hơn
```

Không nên áp dụng cứng các cut-off kiểu:

```text
0.1 = small
0.3 = medium
0.5 = large
```

như luật tuyệt đối.

Trong manuscript nên ưu tiên báo cáo giá trị thực tế.

---

# 13. Tại sao effect size rất quan trọng?

Ví dụ:

```text
p = 0.02
```

không nói cho reviewer biết:

* effect nhỏ hay lớn;
* có phải vài session cực đoan gây ra hay không;
* mức độ dominance của direction.

Ngược lại:

```text
median Δ
+
r_rb
+
direction count
```

cho phép đánh giá trực quan hơn.

Ví dụ:

```text
median Δ = -0.0376
r_rb = -0.81
16/20 negative
```

mạnh hơn nhiều về mặt diễn giải so với chỉ:

```text
p = 0.0007
```

---

# 14. Direction count

Nghiên cứu còn báo cáo:

```text
n_expected / N
n_reverse / N
n_zero / N
```

Ví dụ:

```text
16/20 negative
4/20 positive
0 zero
```

Direction count không phải là một inferential test chính.

Nó là một **descriptive robustness indicator**.

Nó trả lời:

> Effect có xuất hiện trên phần lớn session hay chỉ do vài session có effect rất lớn?

Ví dụ:

```text
median effect âm
15/20 session âm
```

cho thấy effect có tính distributed consistency.

Trong khi:

```text
median effect âm
10/20 âm
10/20 dương
```

sẽ cho thấy heterogeneity cao hơn.

---

# 15. Bootstrap CI và Wilcoxon p-value không kiểm tra cùng một thứ

Một điểm reviewer có thể hỏi:

> Tại sao đôi khi Wilcoxon significant nhưng bootstrap CI của median lại chứa 0?

Ví dụ có thể xảy ra:

```text
Wilcoxon p < 0.05
bootstrap median CI chứa 0
```

Điều này **không phải contradiction**.

Lý do:

## Wilcoxon

dùng:

```text
rank + sign + magnitude ordering
```

của toàn bộ paired-difference distribution.

## Bootstrap CI

ước lượng uncertainty của:

$$
\operatorname{median}(\Delta)
$$

Hai phương pháp không có cùng estimand.

Wilcoxon không đơn giản là:

> kiểm định median = 0.

Do đó:

```text
p-value
```

và:

```text
bootstrap CI of median
```

không bắt buộc đưa ra cùng một quyết định nhị phân.

Cách xử lý đúng là báo cáo cả hai, thay vì chọn kết quả thuận lợi hơn.

---

# 16. Benjamini–Hochberg False Discovery Rate

## 16.1. Tại sao cần correction?

Nếu kiểm định nhiều metric:

```text
Mean_CC
Mean_NRMSE
DET
LLE
```

và mỗi test dùng:

$$
\alpha=0.05
$$

thì xác suất xuất hiện ít nhất một false positive tăng khi số test tăng.

Do đó nghiên cứu sử dụng:

**Benjamini–Hochberg False Discovery Rate correction**

viết tắt:

```text
BH-FDR
```

---

# 17. BH-FDR hoạt động như thế nào?

Giả sử có:

$$
m
$$

p-values:

$$
p_1,...,p_m
$$

Sắp xếp:

$$
p_{(1)}
\le
p_{(2)}
\le
...
\le
p_{(m)}
$$

Tìm giá trị lớn nhất \(k\) sao cho:

$$
p_{(k)}
\le
\frac{k}{m}\alpha
$$

Các test từ:

$$
1,...,k
$$

được xem là vượt qua FDR threshold.

Adjusted p-values thường được báo cáo dưới dạng:

$$
q_{BH}
$$

và:

$$
q_{BH}<0.05
$$

được dùng làm criterion hỗ trợ sau correction.

---

# 18. FDR khác Bonferroni như thế nào?

Bonferroni kiểm soát:

$$
P(\text{ít nhất một false positive})
$$

rất nghiêm ngặt.

BH kiểm soát expected proportion của false discoveries trong tập discoveries:

$$
FDR
=
E
\left[
\frac{V}{R}
\right]
$$

trong đó:

* \(V\): số false discoveries;
* \(R\): tổng discoveries.

Với exploratory/physiological multi-metric analysis có các metric liên quan nhau, BH thường cân bằng tốt hơn giữa:

```text
Type-I error control
```

và:

```text
statistical power
```

so với Bonferroni.

---

# 19. Family của BH-FDR phải được xác định rõ

Không nên gom mọi p-value sinh ra trong toàn bộ project vào một BH correction duy nhất.

Correction được áp dụng trong các **predefined inferential families**.

Ví dụ primary RQ2:

```text
Mean_CC
Mean_NRMSE
DET
LLE
```

tạo một family gồm:

$$
m=4
$$

tests.

Trong label-sensitivity analysis:

```text
T30
T60
S3
S5
```

mỗi rule được xem như một sensitivity setting riêng và BH được áp dụng trên bốn headline metrics trong setting đó.

Tương tự đối với parameter sensitivity nếu bốn headline metrics được kiểm tra cùng nhau.

Điều này phải được mô tả rõ trong Methods để tránh impression rằng FDR family được chọn sau khi nhìn thấy kết quả.

---

# 20. Không dùng p < 0.05 như tiêu chí duy nhất

Trong nghiên cứu này, một finding không được đánh giá chỉ bằng:

$$
p<0.05
$$

Mức độ hỗ trợ được đánh giá từ sự kết hợp của:

```text
direction
+
median Δ
+
bootstrap CI
+
r_rb
+
direction count
+
Wilcoxon p
+
BH q
+
robustness across sensitivity settings
```

Ví dụ một sensitivity setting có thể có:

```text
q = 0.053
```

thay vì:

```text
q = 0.049
```

nhưng:

* effect cùng hướng;
* magnitude gần nominal;
* CI tương tự;
* 15/20 session cùng direction.

Không nên kết luận:

```text
0.049 = effect tồn tại
0.053 = effect biến mất
```

Đó là cách diễn giải threshold quá cứng.

Trong robustness analysis, consistency của effect quan trọng hơn việc mọi sensitivity setting đều vượt chính xác ngưỡng 0.05.

---

# 21. Statistical significance không phải scientific significance

Một effect có thể:

```text
p rất nhỏ
```

nhưng physiological magnitude rất nhỏ.

Ngược lại, một effect có:

```text
p ≈ 0.05
```

nhưng:

* magnitude ổn định;
* direction nhất quán;
* xuất hiện trên nhiều method;
* tái lập qua sensitivity analyses;

vẫn có thể có ý nghĩa khoa học.

Do đó nghiên cứu không dùng:

```text
significant / non-significant
```

như hai trạng thái tuyệt đối.

Ưu tiên cách diễn giải:

```text
supported
not clearly supported
directionally consistent
robust
moderately sensitive
parameter-sensitive
```

---

# 22. Statistical framework cho robustness analyses

Robustness analysis không phải một quá trình tối ưu p-value.

Nominal parameter được chọn trước dựa trên:

* methodological diagnostics;
* literature;
* algorithm definition;
* parsimony.

Sau đó parameter được perturb.

Mục tiêu:

$$
\text{Does the scientific conclusion persist?}
$$

Không phải:

$$
\text{Which parameter produces the smallest p-value?}
$$

Đánh giá robustness dựa trên:

1. sign của \(\Delta\);
2. magnitude;
3. bootstrap CI;
4. \(r_{rb}\);
5. direction count;
6. paired-session availability;
7. statistical support.

Do đó một parameter setting khác nominal có p-value nhỏ hơn không phải lý do để đổi nominal parameter.

---

# 23. Statistical framework cho label sensitivity

Label sensitivity cũng sử dụng cùng paired framework.

Các conservative rules:

```text
T30
T60
S3
S5
```

không nhằm tạo “ground truth mới”.

Mục tiêu là kiểm tra:

> Nếu loại bỏ những phần label có khả năng không chắc chắn nhất, finding còn tồn tại hay không?

Mỗi rule tạo lại session × state representation, sau đó:

$$
\Delta_i=D_i-A_i
$$

và áp dụng cùng inference.

Điều này cho phép kết luận:

> Findings robust to reasonable conservative label-selection rules.

Không nên kết luận:

> KSS labels đã được chứng minh là ground truth tuyệt đối.

---

# 24. Surrogate-data hypothesis testing trong RQ1

RQ1 sử dụng một loại hypothesis test khác.

Mục tiêu không phải:

```text
Awake vs Drowsy
```

mà là:

> Observed PPG dynamics có thể được giải thích bởi noisy pseudoperiodic process hay không?

Null hypothesis:

$$
H_0:
\text{observed dynamics compatible with the PPS null}
$$

Với mỗi observed window:

1. tạo \(M=39\) PPS surrogates;
2. tính cùng nonlinear statistic trên observed signal và surrogate signals;
3. so sánh vị trí của observed statistic trong surrogate distribution.

Đây là **rank-based surrogate test**.

---

# 25. Ý nghĩa của two-sided surrogate rank test

Observed statistic không được giả định phải:

```text
cao hơn surrogate
```

hoặc:

```text
thấp hơn surrogate
```

mới được xem là nonlinear evidence.

Two-sided test hỏi:

> observed value có nằm bất thường ở một trong hai tail của surrogate distribution hay không?

Với số surrogate hữu hạn, p-value có độ phân giải rời rạc.

Đặc biệt với 39 surrogates:

$$
M+1=40
$$

observed statistic được xếp hạng trong tổng cộng 40 values.

Nếu implementation dùng doubled-tail rank convention, smallest attainable two-sided level là khoảng:

$$
\frac{2}{40}=0.05
$$

Do đó việc dùng 39 surrogate là thiết kế phù hợp cho một two-sided rank test ở mức khoảng 5%, nhưng không tạo p-values cực nhỏ như parametric tests.

**Trong manuscript phải mô tả đúng công thức rank test thực tế được dùng trong code**, không nên thay bằng công thức surrogate-test khác chỉ vì chúng tương đương về ý tưởng.

---

# 26. Vì sao surrogate test và Awake–Drowsy test là hai tầng khác nhau?

RQ1:

```text
observed signal
vs
surrogate null
```

trả lời:

> dynamics có chứa organization vượt quá noisy pseudoperiodic null hay không?

RQ2:

```text
Awake
vs
Drowsy
```

trả lời:

> organization đó thay đổi như thế nào theo physiological state?

Hai câu hỏi này không nên trộn lẫn.

RQ1 cung cấp nền tảng rằng nonlinear analysis không chỉ đang mô tả một process trivial theo surrogate null.

RQ2 mới kiểm định state dependence.

---

# 27. Tại sao dùng nhiều lớp bằng chứng thay vì một test duy nhất?

Không có một statistic đơn lẻ nào có thể trả lời toàn bộ câu hỏi.

### Median Δ

trả lời:

> effect trung tâm là bao nhiêu?

### Bootstrap CI

trả lời:

> effect estimate bất định đến mức nào?

### Wilcoxon

trả lời:

> ranked paired differences có systematic shift khỏi zero hay không?

### \(r_{rb}\)

trả lời:

> directional rank dominance mạnh đến mức nào?

### Direction count

trả lời:

> bao nhiêu session thực sự đi theo direction đó?

### BH-FDR

trả lời:

> statistical evidence còn đứng vững khi xét multiple metrics hay không?

### Sensitivity analysis

trả lời:

> finding có phụ thuộc vào một lựa chọn parameter/data rule cụ thể hay không?

### Reproducibility audit

trả lời:

> cùng input và configuration có tái tạo đúng output hay không?

Các thành phần này bổ sung cho nhau.

---

# 28. Điểm mạnh của statistical design hiện tại

Khung thống kê hiện tại có một số điểm mạnh:

### 28.1. Tránh pseudo-replication

Inference ở cấp session thay vì window.

### 28.2. Paired design

Awake và Drowsy trong cùng session được so sánh trực tiếp.

Điều này giảm influence của between-session baseline variability.

### 28.3. Robust central tendency

Median giảm ảnh hưởng của outlier.

### 28.4. Distribution-light inference

Không phụ thuộc mạnh vào normality.

### 28.5. Effect size được báo cáo

Không chỉ dựa vào p-value.

### 28.6. Multiple-comparison control

BH-FDR giảm nguy cơ false discoveries.

### 28.7. Sensitivity analysis

Kiểm tra label và parameter dependence.

### 28.8. Deterministic reproducibility audit

Kiểm tra implementation-level reproducibility.

---

# 29. Những giới hạn thống kê vẫn phải thừa nhận

Verification không biến dataset thành một dataset lớn.

Primary inference vẫn chỉ dựa trên khoảng:

$$
N=20
$$

paired sessions.

Do đó:

* CI có thể rộng;
* power không lớn;
* một vài session đảo chiều vẫn có ảnh hưởng;
* không nên đưa ra claim quá mạnh về population generalization.

Một limitation khác là có nhiều session đến từ cùng subject.

Session-level inference giả định các session là đơn vị phân tích đủ độc lập về mặt nghiên cứu, nhưng repeated sessions từ cùng một subject có thể tạo residual within-subject dependence.

Do đó cần phân biệt:

> session-level pairing xử lý dependence giữa Awake và Drowsy trong cùng session,

nhưng không tự động chứng minh:

> hai session từ cùng subject hoàn toàn độc lập.

Nếu reviewer yêu cầu strict subject-level inference, có thể bổ sung:

* subject-level aggregation;
* cluster bootstrap theo subject;
* mixed-effects / hierarchical sensitivity analysis.

Đây là một robustness check bổ sung, không làm mất giá trị của primary session-level analysis.

---

# 30. Phản biện: “Dataset nhỏ nên p-value không đáng tin?”

Câu trả lời:

> Chính vì số session không lớn nên nghiên cứu không phụ thuộc vào một parametric test hoặc một p-value duy nhất. Inference sử dụng paired rank-based testing, bootstrap confidence intervals, effect sizes và direction counts. Ngoài ra findings còn được stress-test qua label và parameter sensitivity.

Điểm cần tránh:

> “Bootstrap giải quyết hoàn toàn vấn đề sample size nhỏ.”

Bootstrap không tạo thêm independent information.

Nó chỉ giúp đặc trưng hóa uncertainty mà không cần assumptions mạnh như normality.

---

# 31. Phản biện: “Có rất nhiều window, tại sao chỉ dùng n=20?”

Câu trả lời:

> Vì các window trong cùng session không độc lập. Sử dụng chúng trực tiếp làm inferential samples sẽ tạo pseudo-replication. Nhiều window được dùng để ước lượng ổn định state-level dynamics trong mỗi session, còn uncertainty được đánh giá ở cấp session.

Nói cách khác:

```text
many windows
→ tăng precision của within-session estimate

không phải

many windows
→ tăng independent statistical sample size
```

---

# 32. Phản biện: “Tại sao median chứ không mean?”

Câu trả lời:

> Các nonlinear metrics ở cấp window có thể skewed hoặc chứa extreme estimates. Median được chọn để đại diện cho trạng thái điển hình của mỗi session và giảm influence của một số window bất thường. Điều này phù hợp với nonparametric paired inference sau đó.

Điểm cần nhấn mạnh:

> median được chọn trước theo statistical rationale, không phải vì cho p-value đẹp hơn.

---

# 33. Phản biện: “Tại sao vừa bootstrap vừa Wilcoxon?”

Vì chúng trả lời hai câu hỏi khác nhau.

Bootstrap:

> uncertainty của median effect là bao nhiêu?

Wilcoxon:

> toàn bộ ranked paired-difference distribution có systematic displacement khỏi zero hay không?

Do đó chúng là complementary evidence.

Không phải redundant tests.

---

# 34. Phản biện: “CI chứa zero nhưng p < 0.05 có phải mâu thuẫn?”

Không.

Bootstrap CI ở đây là CI của:

$$
\operatorname{median}(\Delta)
$$

trong khi Wilcoxon signed-rank không phải test trực tiếp của bootstrap median estimand.

Hai phương pháp sử dụng thông tin khác nhau.

Cách xử lý minh bạch nhất là báo cáo cả hai.

Nếu CI chứa zero:

```text
uncertainty of median effect remains substantial
```

ngay cả khi rank-based test cho statistical support.

Không nên che giấu sự khác nhau này.

---

# 35. Phản biện: “Tại sao dùng BH-FDR mà không Bonferroni?”

Câu trả lời:

> Các nonlinear metrics cung cấp các góc nhìn bổ sung và có tương quan với nhau. Mục tiêu là kiểm soát expected false-discovery proportion trong một predefined family mà không hy sinh quá nhiều power. BH-FDR phù hợp hơn Bonferroni cho cấu trúc multi-metric này.

Nếu reviewer yêu cầu family-wise error rate cực nghiêm:

> Bonferroni có thể được trình bày như sensitivity supplementary correction, nhưng không nhất thiết là primary correction.

---

# 36. Phản biện: “Bạn có đang chọn parameter để đạt significance?”

Câu trả lời:

> Không. Parameter selection và parameter robustness được tách riêng.

```text
Parameter selection
→ literature / diagnostics / algorithm definition

Parameter sensitivity
→ perturb parameter sau khi nominal setting đã freeze
→ kiểm tra conclusion stability
```

Sensitivity analysis không được sử dụng để tìm parameter có p-value nhỏ nhất.

Nếu một sensitivity setting cho:

```text
p = 0.002
```

còn nominal cho:

```text
p = 0.02
```

nominal vẫn được giữ nếu không có methodological reason để thay đổi.

---

# 37. Phản biện: “Một vài sensitivity setting không đạt p<0.05, vậy robustness thất bại?”

Không nhất thiết.

Robustness không phải:

$$
\forall setting,\;p<0.05
$$

Robustness nên xem:

$$
\text{direction}
+
\text{effect magnitude}
+
\text{CI}
+
\text{effect size}
+
\text{session consistency}
$$

Nếu effect giữ cùng direction và magnitude gần tương đương nhưng p-value dịch từ:

```text
0.049 → 0.055
```

không có cơ sở khoa học để tuyên bố biological effect đột nhiên biến mất.

Ngược lại, nếu:

* effect đổi dấu;
* magnitude collapse về gần zero;
* direction count trở nên 50/50;

thì đó mới là bằng chứng parameter sensitivity thực sự.

---

# 38. Phản biện: “Robustness analysis có làm tăng Type-I error không?”

Nếu sensitivity outputs được xem như nhiều cơ hội để tìm significance thì có.

Nhưng framework của nghiên cứu không sử dụng sensitivity theo cách đó.

Nominal analysis là inferential analysis chính.

Sensitivity analysis trả lời:

> conclusion có ổn định khi perturb assumptions không?

Không dùng:

```text
“ít nhất một sensitivity setting significant”
```

làm evidence.

Do đó sensitivity analysis được diễn giải theo stability, không phải như một tập hypothesis tests để cherry-pick.

---

# 39. Phản biện: “Direction count có phải một statistical test khác không?”

Không.

Direction count chỉ là descriptive evidence.

Ví dụ:

```text
16/20 session có Δ < 0
```

giúp reviewer thấy heterogeneity giữa các session.

Primary inference vẫn đến từ:

* paired effect;
* bootstrap;
* Wilcoxon;
* effect size;
* multiple-comparison control.

---

# 40. Primary statistical hierarchy của nghiên cứu

Có thể tóm tắt framework như sau:

```text
Level 1 — Window
Compute nonlinear metric

        ↓

Level 2 — Session × state
Median across valid windows

        ↓

Level 3 — Paired effect
Δi = Drowsyi − Awakei

        ↓

Level 4 — Effect estimation
Median Δ

        ↓

Level 5 — Uncertainty
20,000 paired bootstrap resamples
95% percentile CI

        ↓

Level 6 — Hypothesis testing
Two-sided Wilcoxon signed-rank

        ↓

Level 7 — Effect size
Matched-pairs rank-biserial correlation

        ↓

Level 8 — Consistency
Direction count

        ↓

Level 9 — Multiplicity
BH-FDR within predefined test families

        ↓

Level 10 — Verification
Label sensitivity
Parameter sensitivity
Reproducibility audit
```

---

# 41. Nguyên tắc diễn giải cuối cùng

Một finding được xem là mạnh nhất khi đồng thời có:

```text
1. median Δ khác zero theo hướng rõ ràng
2. bootstrap CI hỗ trợ direction
3. Wilcoxon support
4. |r_rb| đáng kể
5. phần lớn session cùng direction
6. BH-FDR support
7. direction/effect ổn định qua sensitivity analyses
8. estimator tái lập chính xác
```

Không yêu cầu mọi sensitivity result phải đạt tất cả tám điều kiện.

Primary finding được đánh giá từ **convergence of evidence**.

---

# 42. Cách trình bày với reviewer

Câu ngắn gọn nhất:

> The statistical design deliberately separates metric estimation from inference. Nonlinear metrics were first estimated at the window level, summarized within each session and state, and then compared using paired session-level differences. Effect magnitude, bootstrap uncertainty, rank-based inference, effect size, direction consistency, and false-discovery control were reported jointly rather than relying on p-values alone.

Có thể bổ sung:

> Robustness analyses were used as stress tests of the conclusions rather than as parameter-optimization procedures.

---

# 43. Claim boundary

Statistical evidence của nghiên cứu hỗ trợ:

> Awake và Drowsy được liên hệ với systematic differences trong một số đặc trưng động lực học của processed PPG trong dataset này, và các differences chính vẫn ổn định qua nhiều kiểm tra robustness.

Statistical evidence **không tự động chứng minh**:

* causality;
* universal population effect;
* KSS là objective ground truth;
* mọi subject đều thay đổi giống nhau;
* mọi preprocessing pipeline đều tạo cùng result.

Do đó manuscript nên ưu tiên các từ:

```text
associated with
consistent with
supported
robust within the tested range
```

thay vì:

```text
proves
universally demonstrates
causes
```

---

# 44. Statistical philosophy của nghiên cứu

Khung thống kê có thể tóm tắt bằng một nguyên tắc:

> **Không tìm kiếm một p-value nhỏ nhất; tìm kiếm sự hội tụ của nhiều bằng chứng độc lập và bổ sung cho nhau.**

Trong nghiên cứu này, độ tin cậy không đến từ một test duy nhất mà từ sự kết hợp của:

```text
paired experimental structure
+
robust aggregation
+
nonparametric inference
+
bootstrap uncertainty
+
effect-size reporting
+
multiple-comparison control
+
label robustness
+
parameter robustness
+
deterministic reproducibility
```

Đây là cơ sở thống kê chính để bảo vệ độ tin cậy của các kết luận trước prof và reviewer.

```

