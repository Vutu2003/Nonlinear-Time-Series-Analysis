# Observation: Raw PPG vs First-Differenced PPG in EDM Analysis

## Initial Motivation

Mục tiêu là kiểm tra liệu PPG có chứa cấu trúc động lực học tất định (deterministic nonlinear dynamics) hay không bằng phương pháp Simplex Projection theo tinh thần Sugihara & May (1990).

Hai biểu diễn tín hiệu được khảo sát:

1. Raw PPG
2. First-differenced PPG

---

# Case 1: First-Differenced PPG

## Embedding Diagnostics

### p(E)

Kết quả cho thấy tồn tại cực đại rõ ràng:

- Optimal embedding dimension: E ≈ 4
- Kết quả phù hợp với FNN

Đồ thị p(E) có hình dạng phù hợp với kỳ vọng của Takens reconstruction:

- E thấp → under-embedding
- E tối ưu → forecast skill cao nhất
- E quá lớn → giảm nhẹ do curse of dimensionality

=> Geometry của phase space tương đối hợp lý.

---

## p(T)

Forecast skill giảm theo prediction horizon nhưng không hoàn toàn đơn điệu.

Xuất hiện các vùng hồi phục cục bộ của p(T).

Điều này có thể phản ánh:

- nhiều thang thời gian sinh lý cùng tồn tại
- cardiac rhythm
- respiratory modulation
- autonomic regulation

Thay vì một attractor chaos lý tưởng kiểu Lorenz.

---

## Linear vs Nonlinear Forecast

AR benchmark > Simplex

Kết luận:

- Differencing làm phase-space reconstruction trở nên "đẹp" hơn.
- Tuy nhiên nonlinear forecast không còn vượt linear predictor.

---

# Case 2: Raw PPG

## Embedding Diagnostics

### p(E)

Không xuất hiện optimum rõ ràng.

Forecast skill giảm gần như đơn điệu khi E tăng.

Không giống hành vi textbook của Lorenz hoặc các attractor low-dimensional lý tưởng.

Điều này gợi ý:

- redundancy mạnh
- multiscale oscillations
- trend/modulation sinh lý
- measurement noise

đang làm méo phase-space geometry.

---

## Linear vs Nonlinear Forecast

Simplex > AR

Đây là kết quả ngược với trường hợp differencing.

Theo tiêu chuẩn Sugihara (1990), đây là dấu hiệu thuận lợi hơn cho giả thuyết tồn tại cấu trúc phi tuyến.

---

# Key Contradiction

Hai biểu diễn tín hiệu cho hai kết luận khác nhau:

| Representation | p(E) | Simplex vs AR |
|---------------|------|---------------|
| Raw PPG | Kém rõ ràng | Simplex > AR |
| Differenced PPG | Rõ ràng (E≈4) | AR > Simplex |

---

# Possible Interpretation

Differencing không đơn thuần loại bỏ trend.

Nó còn thay đổi hình học của attractor.

Có thể:

- làm giảm redundancy
- mở rộng phase-space geometry
- cải thiện embedding diagnostics

Nhưng đồng thời:

- loại bỏ một phần thông tin động lực học hữu ích cho dự báo phi tuyến.

Do đó:

"Phase-space reconstruction đẹp hơn"
không đồng nghĩa với
"Forecast skill phi tuyến mạnh hơn".

---

# Important Lesson

Takens reconstruction quality và nonlinear forecast superiority là hai câu hỏi khác nhau:

1. Attractor có được reconstruct tốt hay không?
2. Nonlinear predictor có vượt linear predictor hay không?

Một representation có thể tốt cho (1) nhưng không tốt cho (2).

---

# Current Working Hypothesis

PPG không giống Lorenz.

PPG có thể được mô tả gần đúng bởi:

Deterministic Dynamics
+ Multiscale Physiological Oscillations
+ Measurement Noise
+ Autonomic Modulation

Do đó không nên kỳ vọng:

- p(E) hình chuông hoàn hảo
- p(T) decay hoàn hảo

như trong các hệ chaos lý tưởng.

---

# Next Experiments

Các kiểm định có giá trị hơn việc tiếp tục tranh luận về p(E):

1. Surrogate Data Test
   - Raw PPG
   - Differenced PPG

2. S-map
   - Kiểm tra optimum θ > 0 hay không

3. PRV Analysis
   - So sánh với waveform PPG

Nếu Raw PPG đánh bại surrogate và/hoặc S-map tối ưu tại θ > 0, đây sẽ là bằng chứng mạnh hơn nhiều cho tính phi tuyến/tất định của hệ.


# PPG = Deterministic dynamics+multiscale oscillations+measurement noise+physiological modulation