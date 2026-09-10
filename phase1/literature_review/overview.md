# Literature Review Plan — PPG Drowsiness Nonlinear Dynamics

## Mục tiêu chung

Literature review trong giai đoạn tiếp theo không nhằm mở rộng thêm nhiều phương pháp phân tích mới, mà tập trung vào ba mục tiêu:

1. **Xác định research gap** của nghiên cứu hiện tại trong literature về PPG và drowsiness.
2. **Giải thích các empirical findings** đã quan sát được bằng nền tảng sinh lý và nonlinear dynamics.
3. **Củng cố methodological justification** cho surrogate testing, short-window analysis và physiological interpretation.

Empirical pattern cần được literature giải thích:

```text
Drowsiness
→ forecastability ↓
→ diagonal recurrence organization ↓
→ local trajectory divergence ↓
→ laminarity ↑ tendency
````

---

# 1. Drowsiness physiology và cardiovascular/autonomic regulation

## Mục tiêu

Xây dựng nền tảng sinh lý cho sự chuyển đổi từ trạng thái Awake sang Drowsy.

## Literature cần khảo sát

Tập trung vào những thay đổi của:

* Heart rate
* Heart-rate variability
* Sympathetic modulation
* Parasympathetic / vagal modulation
* Sympathovagal balance
* Peripheral vascular tone
* Vasoconstriction / vasodilation
* Respiration
* Baroreflex regulation
* Cardiovascular coupling

## Câu hỏi cần trả lời

* Drowsiness làm autonomic regulation thay đổi theo hướng nào?
* Sympathetic và parasympathetic activity thay đổi ra sao khi tiến gần sleep onset?
* Peripheral circulation thay đổi như thế nào?
* Respiration và cardiovascular control có trở nên chậm hơn, ổn định hơn hay biến thiên hơn?
* Những thay đổi này có thể giải thích pattern nonlinear dynamics quan sát được hay không?

## Vai trò trong manuscript

Đây là literature nền tảng để giải thích:

```text
CC ↓
NRMSE ↑
DET ↓
LLE ↓
LAM/TT ↑ tendency
```

Đặc biệt quan trọng cho **Discussion và mechanistic interpretation**.

---

# 2. PPG / pulse-wave changes during drowsiness, sleepiness and sleep onset

## Mục tiêu

Xác định những gì đã được biết trực tiếp về PPG khi con người trở nên buồn ngủ.

## Literature cần khảo sát

Ưu tiên các nghiên cứu sử dụng:

* Raw / processed PPG waveform
* Pulse amplitude
* Pulse morphology
* Pulse interval / pulse-to-pulse interval
* Pulse-wave variability
* Peripheral vascular features
* PPG-derived HR / HRV
* PPG during sleep onset
* PPG during driver drowsiness / fatigue / sleepiness

## Câu hỏi cần trả lời

* PPG waveform thay đổi như thế nào khi drowsiness tăng?
* Những thay đổi nào đã được báo cáo ở amplitude, morphology hoặc timing?
* Existing studies chủ yếu dùng PPG để **detect/classify drowsiness**, hay để nghiên cứu dynamics?
* Có nghiên cứu nào đã trực tiếp phân tích nonlinear dynamics của continuous PPG waveform giữa Awake và Drowsy hay chưa?

## Vai trò trong manuscript

Cụm này quan trọng nhất để xác định **direct research gap**.

Working question:

> Existing studies đã biết rằng PPG thay đổi khi drowsy, nhưng liệu họ đã khảo sát **state-dependent nonlinear dynamical reorganization** hay chưa?

---

# 3. Nonlinear cardiovascular dynamics under autonomic/state changes

## Mục tiêu

Hiểu cách cardiovascular dynamics thay đổi khi physiological/autonomic state thay đổi.

## Signal có thể mở rộng

Không giới hạn ở PPG:

* PPG
* HRV
* ECG
* Blood pressure
* Respiration
* Pulse interval series

## Physiological states cần khảo sát

* Drowsiness
* Sleep
* Sleep onset
* Fatigue
* Mental stress
* Autonomic blockade
* Anesthesia
* Exercise / recovery
* Cardiovascular disease
* Altered vigilance

## Nonlinear quantities cần chú ý

* Predictability
* Recurrence measures
* Entropy
* Lyapunov exponent
* Determinism
* Fractal / scaling characteristics
* Complexity measures

## Câu hỏi cần trả lời

* Khi autonomic regulation thay đổi, nonlinear cardiovascular dynamics thường thay đổi theo hướng nào?
* Reduced physiological complexity có luôn đồng nghĩa với reduced predictability hoặc reduced divergence không?
* Một physiological state có thể đồng thời làm một số aspects của dynamics tăng và các aspects khác giảm hay không?
* Có precedent cho một **coordinated dynamical reorganization** thay vì một thay đổi đơn metric hay không?

## Vai trò trong manuscript

Cụm này tạo cầu nối giữa:

```text
physiology
→ dynamical mechanisms
→ observed nonlinear metrics
```

---

# 4. Mechanistic interpretation of Prediction + RQA + LLE

## Mục tiêu

Giải thích từng thành phần của dynamical pattern và đặc biệt là mối quan hệ giữa chúng.

---

## 4.1 Nonlinear prediction / forecastability

### Literature cần tìm

* Nonlinear prediction in physiological signals
* Local/simplex prediction
* Short-term forecastability
* Predictability of cardiovascular dynamics
* Prediction decay in nonlinear biological systems

### Câu hỏi chính

* Forecastability phản ánh aspect nào của dynamics?
* Reduced CC / increased NRMSE nên được diễn giải như thế nào về temporal organization?
* Predictability giảm có nhất thiết đồng nghĩa với chaos mạnh hơn không?

---

## 4.2 RQA — diagonal organization

### Metrics

* DET
* Lmean
* Diagonal-line structures

### Literature cần tìm

* RQA interpretation in cardiovascular signals
* Determinism in physiological recurrence plots
* Diagonal line length and trajectory similarity
* RQA under state changes

### Câu hỏi chính

* DET giảm phản ánh điều gì về recurrence organization?
* Lmean giảm có thể được hiểu như giảm persistence của similar trajectory evolution hay không?
* Diagonal recurrence structure có liên hệ thế nào với predictability?

---

## 4.3 RQA — laminar dynamics

### Metrics

* LAM
* TT

### Literature cần tìm

* Laminarity in physiological systems
* Trapping time
* Intermittency
* Laminar states
* Recurrence-based state transitions

### Câu hỏi chính

* LAM/TT tăng phản ánh dạng dynamical behavior nào?
* Laminarity tăng có thể đồng thời xuất hiện với DET giảm hay không?
* Physiologically, increased trapping có thể liên hệ với slower regulatory modes hoặc more persistent local states hay không?

---

## 4.4 Largest Lyapunov exponent

### Literature cần tìm

* LLE in cardiovascular dynamics
* Local trajectory divergence
* Lyapunov exponent during sleep / stress / disease / autonomic changes
* Interpretation of reduced LLE in noisy physiological signals

### Câu hỏi chính

* LLE giảm phản ánh điều gì ngoài cách diễn giải đơn giản “less chaos”?
* Local divergence giảm có thể xuất hiện đồng thời với reduced global predictability hay không?
* LLE và nonlinear prediction phản ánh những temporal/dynamical scales khác nhau như thế nào?

---

## 4.5 Integrated mechanistic problem

Đây là câu hỏi quan trọng nhất cho Discussion:

> **Tại sao forecastability giảm nhưng local trajectory divergence cũng giảm?**

và:

> **Tại sao diagonal recurrence organization giảm trong khi laminarity có xu hướng tăng?**

Không nên cố ép tất cả metrics vào một trục:

```text
more chaos ↔ less chaos
```

Thay vào đó cần xem chúng như các aspects khác nhau của một **dynamical reorganization**.

---

# 5. Surrogate testing in physiological nonlinear dynamics

## Mục tiêu

Củng cố RQ1 và claim boundary của nghiên cứu.

## Literature cần khảo sát

Các surrogate approaches:

* Phase-randomized surrogates
* AAFT
* IAAFT
* Pseudoperiodic surrogates
* Cycle-shuffled surrogates
* Other nonlinear null models

## Signal domains

* PPG
* HRV
* ECG
* Respiration
* Blood pressure
* Other physiological oscillatory signals

## Câu hỏi cần trả lời

* Các null hypothesis khác nhau kiểm tra điều gì?
* Tại sao phase-randomized surrogate có thể chưa đủ khó cho pseudoperiodic signals?
* Khi nào PPS phù hợp hơn AAFT/IAAFT?
* Surrogate rejection cho phép claim đến mức nào?
* Những lỗi phổ biến nào dẫn đến overclaim “deterministic chaos”?

## Vai trò trong manuscript

Hỗ trợ RQ1:

> **Observed PPG contains dynamical organization beyond the tested noisy pseudoperiodic null.**

Không dùng để claim:

> deterministic chaos has been proven.

Ba paper Sviridova 2015/2018/2022 hiện là literature core ban đầu của cụm này.

---

# 6. Short-window / ultra-short physiological nonlinear analysis

## Mục tiêu

Củng cố việc sử dụng:

```text
60 s primary
30 / 120 / 180 s robustness
```

## Literature cần khảo sát

* Short-window PPG analysis
* Ultra-short HRV
* Short-time RQA
* Short-time LLE estimation
* Prediction from limited physiological recordings
* Effect of data length on nonlinear metrics
* Wearable / real-time physiological analysis

## Câu hỏi cần trả lời

* Mỗi nonlinear metric cần bao nhiêu dữ liệu để estimate ổn định?
* Data-length dependence khác nhau như thế nào giữa DET, Lmean, LLE, entropy, prediction?
* 60 s có precedent nào trong physiological literature?
* Window ngắn hơn mang lại temporal resolution nhưng phải trả giá bằng variance như thế nào?
* Robustness across 60/120/180 s có thể được diễn giải ra sao?

## Vai trò trong manuscript

Dùng để biện luận rằng:

> short-window nonlinear analysis là khả thi, nhưng reliability phải được đánh giá theo metric và window length.

Sviridova et al. 2022 là core methodological reference, nhưng cần mở rộng sang HRV/ECG/wearable literature.

---

# 7. Symbolic dynamics and ANS interpretation

## Mục tiêu

Xây dựng một **supportive physiological interpretation layer** cho findings chính.

## Core literature

Ưu tiên lineage:

* Porta et al.
* Guzzetti et al.
* Later symbolic HRV studies

## Metrics cần tập trung

```text
0V
1V
2V
2LV
2UV
```

## Physiological mapping cần xác minh

Đặc biệt quan tâm:

```text
0V ↑
→ sympathetic modulation / reduced variability tendency

2V ↓
→ reduced vagal / parasympathetic modulation tendency
```

Cần kiểm tra kỹ context trong từng experimental protocol.

## Câu hỏi cần trả lời

* 0V và 2V phản ánh autonomic modulation như thế nào?
* Mapping này ổn định tới mức nào giữa các studies?
* Các studies dùng bao nhiêu beats?
* Short-window symbolic analysis có limitation gì?
* Có evidence trong drowsiness/sleep cho pattern tương tự hay không?

## Vai trò trong manuscript

Symbolic dynamics không phải primary evidence.

Nó chỉ hỗ trợ hypothesis rằng:

> observed nonlinear dynamical reorganization may be compatible with altered autonomic regulation.

Không claim direct sympathetic/vagal measurement.

---

# Thứ tự ưu tiên literature review

## Phase 1 — Xác định gap trực tiếp

```text
1. Drowsiness physiology / ANS
2. PPG changes during drowsiness
```

Mục tiêu:

* hiểu physiology;
* xác định literature đã làm gì với PPG;
* kiểm tra novelty của state-dependent nonlinear analysis.

---

## Phase 2 — Giải thích empirical findings

```text
3. Nonlinear cardiovascular dynamics
4. Prediction + RQA + LLE interpretation
```

Mục tiêu:

* xây mechanistic story;
* giải thích các seemingly contradictory findings;
* kết nối các metric thành một dynamical pattern thống nhất.

---

## Phase 3 — Củng cố methodology

```text
5. Surrogate testing
6. Short-window nonlinear analysis
```

Mục tiêu:

* bảo vệ RQ1;
* bảo vệ PPS choice;
* bảo vệ 60-s primary window;
* xác định claim boundaries.

---

## Phase 4 — Physiological support

```text
7. Symbolic dynamics / ANS
```

Mục tiêu:

* cung cấp secondary physiological interpretation;
* không biến symbolic findings thành confirmatory evidence.

---

# Literature extraction template

Với mỗi paper nên ghi lại ít nhất:

| Field                            | Nội dung cần extract                                 |
| -------------------------------- | ---------------------------------------------------- |
| **Scientific question**          | Paper thực sự muốn trả lời gì?                       |
| **Signal**                       | PPG / HRV / ECG / BP / respiration                   |
| **Population / state**           | Awake / drowsy / sleep / stress / disease...         |
| **Data length**                  | Window / recording duration                          |
| **Method**                       | Prediction / RQA / LLE / entropy / surrogate...      |
| **Main finding**                 | Metric thay đổi theo hướng nào?                      |
| **Physiological interpretation** | Authors giải thích mechanism ra sao?                 |
| **Claim strength**               | Association / mechanism / causality                  |
| **Relevance to current study**   | Support / precedent / direct competitor / limitation |
| **What remains unanswered**      | Gap paper đó để lại                                  |

---

# Mục tiêu cuối cùng của literature review

Literature review cần giúp xây được chuỗi lập luận:

```text
Drowsiness
        ↓
altered autonomic / cardiovascular regulation
        ↓
reorganization of peripheral pulse dynamics
        ↓
changes across complementary dynamical dimensions

forecastability ↓
recurrence organization ↓
local divergence ↓
laminarity ↑ tendency
```

Từ đó manuscript không chỉ nói:

> “Several nonlinear metrics were significantly different.”

mà có thể xây một argument mạnh hơn:

> **Drowsiness is associated with a coordinated reorganization of short-window PPG dynamics across temporal predictability, recurrence geometry, and local trajectory divergence.**

---

# Research principle

Literature review ở giai đoạn này không nhằm tìm thêm thật nhiều nonlinear methods để đưa vào experiment.

Mục tiêu là:

```text
find the gap
→ explain the findings
→ construct the mechanism
→ defend the methodology
→ define the claim boundary
```

Không phải:

```text
find another metric
→ run another experiment
→ expand the feature battery
```

```

