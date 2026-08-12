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
