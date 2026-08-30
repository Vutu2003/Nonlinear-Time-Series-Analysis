# RQ2 — Final conclusion: Drowsiness-induced reorganization of PPG dynamics

Sau khi áp dụng BH-FDR trên 7 primary metrics của 60-s Processed PPG, bốn findings vẫn được hỗ trợ:

- **Mean_CC ↓**
- **Mean_NRMSE ↑**
- **DET ↓**
- **LLE ↓**

Các finding này trải trên ba domain độc lập:

```text
Prediction
→ forecastability ↓

RQA
→ diagonal recurrence organization ↓

Rosenstein LLE
→ local trajectory divergence ↓
````

Do đó, RQ2 có thể được chốt:

> **Drowsiness is associated with a reproducible reorganization of short-window PPG dynamics, characterized primarily by reduced forecastability, reduced diagonal recurrence organization, and lower local trajectory divergence.**

### Vai trò của các RQA metrics còn lại

* `Lmean ↓` cho bằng chứng cùng hướng với `DET` nhưng không vượt BH-FDR.
* `LAM ↑` và `TT ↑` chỉ cho xu hướng yếu hơn và heterogeneous hơn giữa các session.

Điều này gợi ý rằng trong dataset hiện tại, các metric liên quan đến **trajectory organization / determinism-related structure / local divergence** bộc lộ state modulation rõ hơn các metric liên quan đến **laminar trapping hoặc state-transition persistence**.

Tuy nhiên, không nên diễn giải điều này thành việc các khía cạnh “chaos” thay đổi rõ hơn theo nghĩa tuyệt đối. An toàn hơn là nói rằng các đặc trưng **chaos-related và trajectory-based** cho sensitivity mạnh hơn với drowsiness trong thiết kế hiện tại.

### Một khả năng giải thích

Sự khác biệt về strength giữa hai nhóm metric có thể đến từ cả yếu tố sinh lý và giới hạn đo lường:

* Prediction, DET và LLE phản ánh các đặc trưng trajectory-based có thể nhạy với thay đổi ngắn hạn của dynamical organization.
* LAM và TT liên quan nhiều hơn đến vertical recurrence, local trapping và persistence của các trạng thái tương đối chậm; các pattern này có thể cần tín hiệu ổn định hơn hoặc observation window dài hơn để được ước lượng rõ.
* Dataset được thu bằng hệ thống PPG đơn giản dựa trên ESP32 + MAX32xxx, nên tín hiệu thực nghiệm chịu ảnh hưởng của noise, motion artifact, sensor limitations và nonstationarity.
* Các yếu tố này có thể làm suy giảm khả năng nhận diện các laminar/transition structures tinh tế hơn, đặc biệt trong cửa sổ ngắn 60 s.

### Claim boundary

Không kết luận rằng:

* drowsiness làm PPG trở nên “ít chaotic hơn” theo nghĩa tuyệt đối;
* positive/negative change của LLE chứng minh một chaos transition;
* laminar dynamics không thay đổi.

Kết luận phù hợp hơn là:

> **Các bằng chứng mạnh nhất hiện tại cho thấy drowsiness làm thay đổi organization của reconstructed PPG dynamics, với ảnh hưởng rõ nhất trên forecastability, diagonal recurrence structure và local trajectory divergence; laminar changes hiện chỉ được xem là xu hướng hỗ trợ yếu hơn.**

```

