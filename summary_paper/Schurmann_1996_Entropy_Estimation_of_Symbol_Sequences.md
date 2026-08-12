# Paper Metadata
* **Title**: Entropy estimation of symbol sequences
* **Authors**: Thomas Schürmann and Peter Grassberger
* **Year**: 1996
* **Keywords**: Shannon entropy, symbol sequences, data compression, chaotic dynamical systems, natural languages

# 1. Why

## Research Question

Làm sao estimate **Shannon entropy rate** $h$ một cách đáng tin cậy từ một **finite symbolic sequence**, đặc biệt khi sequence có long-range correlations?

$$
\boxed{
s_1,\ldots,s_N
\rightarrow
\hat h
\approx
h
}
$$

## Motivation

Entropy phản ánh lượng **new information per symbol** sau khi đã tính đến correlations.

Tuy nhiên, với finite data:

- long-range correlations cần context dài để được capture;
- số possible words tăng exponential theo block length;
- entropy estimates có thể hội tụ rất chậm và bị finite-sample bias.

$$
\boxed{
\text{Need long context}
\;\leftrightarrow\;
\text{Insufficient finite data}
}
$$

## Previous Methods

Các hướng chính trước đó gồm:

1. **Block counting**  
   Estimate word probabilities trực tiếp, nhưng nhanh chóng breakdown khi số possible words $d^n$ trở nên comparable với $N$.

2. **Lempel–Ziv / compression-based methods**  
   Khai thác repeated structures để estimate entropy qua code length, nhưng finite-$N$ convergence chưa được hiểu rõ.

3. **Context / prediction-based methods**  
   Estimate next-symbol probability từ past contexts, nhưng phải cân bằng giữa:
   - short context: reliable nhưng bỏ sót long correlations;
   - long context: informative nhưng poorly sampled.

$$
\boxed{
\text{Gap: reliable entropy estimation under finite data + long-range dependence}
}
$$

# Section II — Block Entropy: Core Idea

Block entropy:

$$
H_n=-\sum p(s_1,\ldots,s_n)\log p(s_1,\ldots,s_n)
$$

Conditional entropy:

$$
h_n=H_n-H_{n-1}
$$

Entropy rate:

$$
h=\lim_{n\to\infty}h_n
$$

Ý nghĩa:

$$
\boxed{
n\uparrow
\Rightarrow
\text{capture longer correlations}
\Rightarrow
h_n\rightarrow h
}
$$

Tuy nhiên, với alphabet size $d$:

$$
\#\text{possible words}=d^n
$$

nên khi $n$ tăng trong khi sequence length $N$ hữu hạn:

$$
\boxed{
d^n\uparrow
\Rightarrow
\text{undersampling}
\Rightarrow
\hat H_n\text{ bị bias}
}
$$

Hai failure modes:

$$
\boxed{
n\text{ quá nhỏ}
\Rightarrow
\text{miss long-range correlations}
\Rightarrow
\hat h\text{ quá cao}
}
$$

$$
\boxed{
n\text{ quá lớn so với }N
\Rightarrow
\text{poor word statistics}
\Rightarrow
\hat H_n\text{ bị underestimate}
}
$$

Các bias-correction methods chỉ giảm vấn đề khi sampling vẫn đủ; chúng không giải quyết severe undersampling.

$$
\boxed{
\text{Need long context}
\;\leftrightarrow\;
\text{Need exponentially more data}
}
$$

Section II vì vậy **formalize giới hạn của block-counting methods** đã được nêu trong Introduction và tạo động lực cho các compression/context-based estimators ở các phần sau.

# Section III — Ziv–Lempel: Core Idea

Thay vì estimate probability của toàn bộ possible words, Ziv–Lempel khai thác **những repeated patterns thực sự xuất hiện trong sequence**.

$$
\boxed{
\text{more repetition}
\Rightarrow
\text{better compression}
\Rightarrow
\text{lower entropy}
}
$$

Average match / word length liên hệ với entropy:

$$
\langle L(w)\rangle
\approx
\frac{\log N}{h}
$$

nên:

$$
\boxed{
\text{long repeated matches}
\Rightarrow
h\text{ nhỏ}
}
$$

So với block counting:

$$
\boxed{
\text{Block counting}
=
\text{enumerate }d^n\text{ possible words}
}
$$

$$
\boxed{
\text{LZ}
=
\text{selectively exploit observed repetitions}
}
$$

Một estimator dựa trên novelty length $L_i$:

$$
\hat h_N
=
\frac{N\log N}
{\sum_{i=1}^{N}L_i}
$$

trong đó $L_i$ là độ dài tối thiểu cần đọc từ vị trí $i$ để gặp một substring chưa từng xuất hiện trước đó.

Ý nghĩa:

$$
\boxed{
L_i\uparrow
\Rightarrow
\text{past predicts current sequence better}
\Rightarrow
\hat h\downarrow
}
$$

### Limitation

- Finite-$N$ convergence vẫn có thể chậm.
- Một số estimator repetition-based chỉ được đảm bảo convergence cho các source như finite-order Markov chains.
- Với complex / long-memory sources, performance không guaranteed.

$$
\boxed{
\text{Section III: replace exhaustive word counting with repetition-based compression}
}
$$

Nhưng vấn đề **finite-data convergence và long-range dependence** vẫn chưa được giải quyết hoàn toàn.

# Section IV — Gambling & Suffix Trees: Core Idea

Entropy estimation được chuyển thành bài toán **predict next symbol from past context**.

$$
\hat p(s_t \mid s_{t-1},s_{t-2},\ldots)
$$

Nếu past giúp prediction tốt:

$$
\boxed{
\text{better prediction}
\Rightarrow
\text{lower uncertainty}
\Rightarrow
\text{lower entropy}
}
$$

Với strategy tối ưu:

$$
\left\langle
\log \frac{K_n}{K_{n-1}}
\right\rangle
=
\log d-h_n
$$

nên entropy có thể được suy ra từ khả năng prediction.

### Variable-length context

Fixed context length gặp lại vấn đề:

$$
d^r\uparrow
\Rightarrow
\text{undersampling}
$$

Do đó, context nên **adaptive**:

$$
\boxed{
\text{different patterns}
\Rightarrow
\text{different relevant context lengths}
}
$$

### Suffix Tree

Suffix tree lưu:

- các past contexts đã xuất hiện;
- số lần mỗi symbol xuất hiện sau từng context.

Từ đó estimate:

$$
\hat p(s_t \mid \text{context})
$$

một cách hiệu quả.

$$
\boxed{
\text{Past sequence}
\rightarrow
\text{Suffix tree}
\rightarrow
\text{Conditional probabilities}
\rightarrow
\text{Entropy estimate}
}
$$

Full suffix tree có thể tăng rất nhanh, nên Rissanen's tree chỉ mở rộng ở những contexts có đủ repeated evidence.

$$
\boxed{
\text{Section IV: entropy estimation}
\rightarrow
\text{adaptive context prediction}
}
$$

1. **Block / frequency-based** — “Đếm mẫu”

   * Cắt chuỗi thành các đoạn ngắn như `AB`, `BA`, `AA`.
   * Đếm xem mỗi đoạn xuất hiện bao nhiêu lần.
   * Nếu chỉ có vài mẫu lặp đi lặp lại → entropy thấp.
   * Nếu rất nhiều mẫu xuất hiện tương đối đều → entropy cao.

   $$
   \text{Count patterns} \rightarrow \text{Entropy}
   $$

2. **Compression-based** — “Xem nén được bao nhiêu”

   * Tìm các đoạn lặp lại.
   * Nếu có thể mô tả chuỗi bằng một câu ngắn kiểu “lặp `AB` 100 lần” → entropy thấp.
   * Nếu gần như phải lưu từng ký hiệu một → entropy cao.

   $$
   \text{More compressible} \rightarrow \text{Lower entropy}
   $$

3. **Context / prediction-based** — “Đoán ký hiệu tiếp theo”

   * Nhìn các ký hiệu trước đó.
   * Hỏi: “Sau `ABA` thì thường là gì?”
   * Nếu đoán rất chắc → ít thông tin mới → entropy thấp.
   * Nếu luôn kiểu 50/50, khó đoán → entropy cao.

   $$
   \text{Better prediction} \rightarrow \text{Lower entropy}
   $$

4. **Bayesian / bias-corrected** — “Sửa lại việc đếm khi dữ liệu ít”

   * Giả sử chỉ thấy `A` 9 lần và `B` 1 lần.
   * Không nên quá tự tin rằng xác suất thật chính xác là 90% và 10%, nhất là khi mẫu còn ít.
   * Bayesian/bias correction điều chỉnh các probability estimates để chúng bớt bị lệch vì finite data.

   $$
   \text{Raw counts} \rightarrow \text{corrected probabilities} \rightarrow \text{better entropy estimate}
   $$

Nếu nén cả bốn thành một câu:

$$
\boxed{
\text{Đếm} \mid \text{Nén} \mid \text{Dự đoán} \mid \text{Sửa sai do dữ liệu ít}
}
$$

# 2. What

## Core Insight

Entropy rate của một finite symbolic sequence có thể được estimate hiệu quả bằng cách xem bài toán entropy như **sequential prediction**:

$$
\boxed{
\text{Past context}
\rightarrow
\hat p(s_t\mid \text{context})
\rightarrow
\text{information}
\rightarrow
\hat h
}
$$

Thay vì dùng fixed block length, authors ưu tiên **adaptive context length**:

* context ngắn: nhiều samples nhưng bỏ sót long-range correlations;
* context dài: nhiều information hơn nhưng dễ undersampling.

Do đó, context dài chỉ nên được dùng khi nó thực sự cải thiện prediction / compression.

Final strategy của paper:

$$
\boxed{
\text{Bayesian smoothing}
+
\text{Rissanen adaptive context selection}
+
\text{suffix tree}
}
$$

## Mathematical Foundation

Conditional probability được estimate từ context counts với smoothing:

$$
\hat p(s_t=a\mid s_j)
=====================

\frac{n_j^{(a)}+\beta}
{n_j+\beta d}
$$

để tránh zero-frequency problem.

Context length được chọn bằng cách so sánh code length giữa context hiện tại và context ngắn hơn:

$$
D_j
===

## l(z_j\mid s_j)

l(z_j\mid s_{j-1})
$$

Trong đó:

$$
D_j<0
\Rightarrow
\text{longer context improves prediction}
$$

Probability của observed symbol được chuyển thành information:

$$
I_t=-\log \hat p(s_t\mid \text{context})
$$

và entropy rate được hiểu như average information per symbol:

$$
\boxed{
\hat h_N
\approx
\frac{1}{N}
\sum_t
-\log \hat p(s_t\mid \text{past})
}
$$

Suffix tree được dùng để lưu hiệu quả variable-length contexts và các conditional counts cần cho probability estimation.

# 3. How

## 3.1 Algorithm

Với symbolic sequence:

$$
s_1,s_2,\ldots,s_N
$$

authors sử dụng **context-based sequential prediction**:

1. Xây dựng suffix tree từ past symbols.
2. Với mỗi context, lưu số lần mỗi symbol xuất hiện sau context đó.
3. Estimate conditional probability bằng Bayesian smoothing.
4. Dùng Rissanen's criterion để chọn context length phù hợp.
5. Tính code length / information của observed symbol.
6. Average trên toàn sequence để thu được $\hat h_N$.
7. Lặp với nhiều $N$ và extrapolate về $N\rightarrow\infty$.

---

## 3.2 Mathematical Formulation

### Probability estimation

$$
\hat p(s_t=a\mid s_j)
=====================

\frac{n_j^{(a)}+\beta}
{n_j+\beta d}
$$

* $n_j$: số lần context $s_j$ đã xuất hiện.
* $n_j^{(a)}$: số lần context đó followed by symbol $a$.
* $d$: alphabet size.
* $\beta$: smoothing parameter.

### Context selection

So sánh code length của context dài và parent context:

$$
D_j
===

## l(z_j\mid s_j)

l(z_j\mid s_{j-1})
$$

Context dài được ưu tiên khi nó cải thiện compression đủ rõ:

$$
D_j<-\delta
$$

### Entropy estimate

Information của observed symbol:

$$
I_t=-\log \hat p(s_t\mid\text{context})
$$

Entropy estimate:

$$
\hat h_N
\approx
\frac{1}{N}
\sum_{t=1}^{N} I_t
$$

Do $\hat h_N$ hội tụ chậm, authors đề xuất:

$$
\boxed{
\hat h_N
\approx
h+c\frac{\log N}{N^\gamma}
}
$$

để extrapolate $h$ khi $N\rightarrow\infty$.

---

## 3.3 End-to-End Pipeline

$$
\boxed{
\text{Symbol sequence}
\rightarrow
\text{Suffix tree}
\rightarrow
\text{Context counts}
\rightarrow
\hat p(s_t\mid context)
}
$$

$$
\boxed{
\rightarrow
\text{Adaptive context selection}
\rightarrow
-\log \hat p
\rightarrow
\hat h_N
\rightarrow
\text{Extrapolated }h
}
$$

---

## 3.4 Computational Complexity

Paper không đưa một complexity analysis đầy đủ theo Big-O cho toàn algorithm.

Tuy nhiên:

* full suffix tree có thể grow nhanh;
* memory requirement tăng approximately **linearly với sequence length $N$** khi $h>0$;
* workspace trở thành practical limitation với long sequences.

Rissanen's tree giảm growth bằng cách chỉ mở rộng những contexts có repeated evidence.

---

## 3.5 Implementation Notes

* Tránh raw frequency vì có thể tạo $\hat p=0$ → infinite code length.
* Context quá dài dễ bị undersampling; không nên mặc định “longer is better”.
* Authors sử dụng:

  * Bayesian-smoothed probability estimator;
  * Rissanen adaptive context selection;
  * full suffix tree khi computationally feasible;
  * threshold $\delta$ để hạn chế overuse of long contexts.
* $\beta$ và $\delta$ là model parameters và được chọn khác nhau giữa các applications.
* Finite-$N$ convergence rất chậm, nên extrapolation theo $N$ là một phần quan trọng của phương pháp.

$$
\boxed{
\text{Core implementation principle:}
\quad
\text{use the longest context only when data justify it}
}
$$

# 4. Experiments

## Setups

Authors evaluate entropy estimator trên nhiều loại symbolic sources:

1. **Logistic map**

   * Chaotic regime: $a=1.8$
   * Strong intermittency: $a=1.7499$
   * Feigenbaum point: $h=0$

2. **Ikeda map**

   * Binary generating partition.
   * True entropy được benchmark bằng positive Lyapunov exponent.

3. **1-D Cellular Automaton — Rule 150**

   * Input entropy đã biết: $h=0.286$ bits.
   * Tăng số iterations để tạo correlations ngày càng dài.

4. **Written English**

   * Shakespeare, LOB corpus, Bible.
   * Alphabet gồm 27 symbols.
   * Dùng Rissanen/context-tree estimator.

Các finite-$N$ estimates được extrapolate bằng:

$$
\hat h_N
\approx
h+c\frac{\log N}{N^\gamma}
$$

---

## Results

### Chaotic systems

Estimated entropy sau extrapolation gần với ground truth:

$$
\hat h \approx \text{Lyapunov exponent}
$$

Ví dụ:

* Logistic $a=1.8$: $\hat h\approx0.404$, reference $\approx0.405$.
* Logistic $a=1.7499$: $\hat h\approx0.186$, reference $\approx0.184$.
* Ikeda map: $\hat h\approx0.506$, reference $\approx0.508$.

### Cellular Automaton

True entropy được giữ nguyên nhưng correlations dài hơn khi iterations tăng.

Estimator vẫn recover gần đúng $h$, nhưng:

$$
\boxed{
\text{longer correlations}
\Rightarrow
\text{slower convergence}
}
$$

### Written English

Entropy convergence rất chậm do long-range linguistic correlations.

Extrapolated estimates:

* Shakespeare: $\sim1.7$ bits/letter.
* LOB corpus: $\sim1.25$ bits/letter.
* Bible: khó extrapolate ổn định do statistical inhomogeneity.

---

## Discussion

Experiments cho thấy:

$$
\boxed{
\text{Context-based estimator can capture complex correlations}
}
$$

nhưng finite-$N$ convergence có thể **rất chậm**, đặc biệt khi long-range dependencies mạnh.

Scaling law hoạt động tốt trên nhiều source rất khác nhau:

$$
\boxed{
\text{chaotic dynamics}
\rightarrow
\text{cellular automata}
\rightarrow
\text{natural language}
}
$$

Kết quả chính:

$$
\boxed{
\text{More complex / longer-range structure}
\Rightarrow
\text{more data needed for reliable entropy estimation}
}
$$

Do đó, **finite-sample extrapolation là một phần thiết yếu của entropy estimation**, không chỉ là bước phụ.

# 5. Conclusion

## Assumptions

* Symbol sequence được xem như realization của một **stochastic process**, thường giả định **stationary**; nhiều convergence results còn cần **ergodicity**.
* Alphabet là finite.
* Với chaotic systems, cần một symbolic representation đủ phù hợp; trong các benchmark, authors dùng generating partition khi biết.
* Scaling law

$$
\hat h_N
\approx
h+c\frac{\log N}{N^\gamma}
$$

là **empirical ansatz**, không phải theorem tổng quát.

## Limitations

* Entropy estimates có thể hội tụ **rất chậm** khi có strong long-range correlations.
* Reliable estimation cần sequence dài và computational resources lớn.
* Suffix trees có memory cost tăng theo sequence length và có thể trở thành bottleneck.
* Không có một probability/context strategy **globally optimal** cho mọi source.
* Một estimator asymptotically universal chưa chắc hoạt động tốt với finite $N$.
* Với non-stationary hoặc statistically heterogeneous sequences, entropy estimation và extrapolation có thể kém ổn định.
* Kết quả phụ thuộc vào chất lượng symbolic representation; paper không giải quyết bài toán tìm generating partition tổng quát.

# 6. My Research

## Research Ideas

Với symbolic PPG/PPI trong drowsiness detection, entropy không nên được xem là một feature “tính trực tiếp” từ sequence mà cần kiểm tra **estimation reliability**.

Các hướng có thể áp dụng:

* So sánh nhiều entropy estimators trên cùng symbolic sequence.
* Kiểm tra sensitivity theo:

  * sequence/window length $N$;
  * alphabet size $d$;
  * word/context length.
* Đánh giá finite-sample convergence của entropy trong các trạng thái alert/drowsy.
* Kiểm tra xem short physiological windows có đủ dài để entropy estimate ổn định hay không.
* So sánh block-based với context/compression-based estimators khi PPG/PPI có long-range temporal structure.

$$
\boxed{
\text{Entropy difference between states}
\neq
\text{reliable difference}
}
$$

nếu estimator chưa được kiểm chứng về finite-sample behavior.

## Knowledge Contribution

Paper này bổ sung một lớp bảo vệ phương pháp luận sau bước Symbolic Encoding:

$$
\boxed{
\text{Representation validity}
+
\text{Estimation validity}
}
$$

Bollt nhắc rằng symbolic representation có thể sai do partition.

Schürmann--Grassberger cho thấy ngay cả khi symbolic sequence hợp lý, entropy estimate vẫn có thể sai do:

$$
\boxed{
\text{finite data}
+
\text{long-range correlations}
+
\text{estimator choice}
}
$$

Do đó, khi dùng entropy cho physiological STSA, cần biện luận không chỉ:

> Entropy có thay đổi giữa alert và drowsy không?

mà còn:

> Entropy estimate có ổn định và đáng tin với độ dài dữ liệu hiện có không?

$$
\boxed{
\text{Observed entropy}
=======================

\text{Underlying temporal structure}
+
\text{Finite-sample / estimator effects}
}
$$
