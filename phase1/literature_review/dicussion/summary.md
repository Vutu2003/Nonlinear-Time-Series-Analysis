# Paper 6 — Martín-González et al. (2018)
## RQA for sleep-apnea characterization

## Method

- Phân tích **RR intervals / HRV từ single-lead ECG** trên 2 databases.
- Dùng **RQA** để phân biệt apnea vs non-apnea.
- Sweep đồng thời các RQA parameters:
  - embedding dimension
  - delay
  - recurrence threshold
- So sánh:
  - Fixed Distance
  - FAN (Fixed Amount of Nearest Neighbours)
- Các RQA metrics gồm:
  - DET, L, Lmax, ENTR
  - LAM, TT, Vmax
  - recurrence-time features
  - network-based features

### Parameter finding

Kết quả tốt nhất chủ yếu quanh:

```text
m ≈ 7–8
delay ≈ 4–5
FAN ≈ 5%
````

→ nhấn mạnh rằng **RQA results phụ thuộc mạnh vào parameter selection**.

---

## Main findings

Trong apnea:

```text
LAM ↑
Vmax ↑
DET ↑
Lmax ↑
```

→ recurrence structure trở nên:

```text
more regular
more predictable
more laminar
less complex
```

Vertical và diagonal structures đều chứa information quan trọng.

---

## Physiological interpretation

* Cardiovascular dynamics chịu ảnh hưởng của nhiều interacting mechanisms:

  * ANS
  * respiration
  * baroreflex
  * cardiorespiratory coupling
* Trong apnea, control system được diễn giải là **simplified / more regular**, với nhiều recurrence và laminar states hơn.
* Authors liên hệ điều này với altered autonomic regulation và impaired baroreflex.

Quan trọng:

> RQA metrics không nên được xem như direct measurement của sympathetic / parasympathetic activity.

---

## Relevance to current study

Rất quan trọng cho việc diễn giải:

```text
DET ↓
LAM ↑ tendency
TT ↑ tendency
```

### RQA geometry

```text
DET ↓
→ reduced diagonal recurrence organization

LAM / TT ↑
→ greater local persistence / laminar behavior
```

Hai nhóm metrics phản ánh **different dynamical properties**, nên không cần thay đổi cùng chiều.

Current pattern:

```text
less diagonal organization
+
greater laminar persistence
```

→ phù hợp hơn với **redistribution / reorganization of recurrence structure**
hơn là một simple increase/decrease of "complexity".

---

## Important contrast

Sleep apnea trong paper:

```text
DET ↑ + LAM ↑
→ global regularization / simplification
```

Current Drowsiness:

```text
DET ↓ + LAM/TT ↑ tendency
```

→ Drowsiness không giống simple pathological loss of complexity.

Nó có thể phản ánh một **mixed transitional dynamical regime**.

---

## Methodological relevance

Paper support mạnh rằng:

> RQA conclusions phụ thuộc vào embedding, delay và threshold.

Do đó rất relevant cho:

* frozen RQA parameters
* parameter-dependence verification
* robustness analysis

Ngoài ra, paper dùng **median + quartiles trong boxplots**, là supporting precedent cho việc mô tả heterogeneous RQA distributions, nhưng không phải direct justification cho session-level median aggregation.

---

## Discussion role

### RQ2 — RQA

* Cung cấp interpretation rõ cho diagonal vs vertical structures.
* Hỗ trợ cách diễn giải `DET↓` và `LAM/TT↑` như **different aspects of recurrence organization**.

### Verification / Method

* Strong citation cho việc RQA parameterization cần được kiểm tra cẩn thận.

### Claim boundary

Không nên suy ra:

```text
DET ↓ = less physical determinism
LAM ↑ = specific ANS shift
RQA change = chaos transition
```

---

## Main takeaway

> **Martín-González et al. cho thấy diagonal và vertical recurrence structures phản ánh các khía cạnh khác nhau của cardiovascular dynamics và phụ thuộc mạnh vào RQA parameterization. Điều này hỗ trợ trực tiếp cách diễn giải pattern `DET↓` cùng `LAM/TT↑` của nghiên cứu hiện tại như một reorganization của recurrence geometry, thay vì một thay đổi đơn chiều của complexity.**

```
# Paper 5 — Rolink et al. (2015)
## Recurrence Quantification Analysis Across Sleep Stages

## Method

- Dataset lớn: **313 healthy subjects**, >2300 h PSG.
- So sánh **Wake, NREM, REM**.
- Áp dụng RQA trên:
  - ECG
  - respiratory effort
  - heart rate
  - cross-RQA giữa các signals
- Các metrics chính gồm:
  - REC
  - DET
  - L / Lmax
  - ENTR
  - LAM
  - TT
  - recurrence-time metrics

RQA parameters:
- `m = 4`
- delay theo mutual information
- threshold `ε` subject-specific để `REC ≈ 10%`

---

## Main findings

- RQA features có thể phân biệt **Wake vs Sleep**, đặc biệt tốt với cardiac và respiratory signals.
- Trong **NREM**, cardiac và respiratory dynamics nhìn chung **regular hơn**.
- Các differences được phản ánh bởi các metrics như:
  - DET
  - LAM
  - ENTR
  - recurrence times
- REM thường gần Wake hoặc NREM tùy feature, nên discrimination kém hơn.

---

## Physiological interpretation

Paper support rằng:

> Sleep-state changes đi kèm **reorganization of cardio-respiratory dynamics**.

Đặc biệt:

```text
NREM
→ more regular cardiac / respiratory activity
→ altered recurrence structure
````

Tuy nhiên paper không map trực tiếp:

```text
DET / LAM / TT
→ sympathetic / parasympathetic activity
```

---

## Relevance to current study

Rất gần với phần RQA của nghiên cứu hiện tại:

```text
Rolink:
cardiac waveform / HR
→ RQA
→ recurrence differences across Wake / Sleep

Current study:
PPG waveform
→ RQA
→ recurrence differences across Awake / Drowsy
```

Điểm quan trọng:

* Rolink support mạnh rằng **recurrence organization is state-dependent**.
* Nhưng họ gộp `N1 + N2 + N3 = NREM`.

Do đó:

```text
Rolink NREM
≠ current Drowsiness
```

Current dataset gần với:

```text
Awake ↔ Drowsiness
```

hơn là:

```text
Wake → stable NREM
```

---

## Relation to current RQA findings

Current study:

```text
DET ↓
LAM ↑ tendency
TT ↑ tendency
```

Có thể diễn giải như:

```text
less diagonal recurrence organization
+
greater local / laminar persistence
```

Rolink giúp support ý nghĩa của các recurrence structures này, nhưng **không trực tiếp giải thích direction** của drowsiness.

---

## Discussion role

### RQ2 — RQA

Đây là một reference quan trọng để support:

> Sleep-related physiological states are associated with measurable changes in cardiovascular recurrence organization.

### Claim boundary

Không nên dùng paper này để claim:

```text
Drowsiness = NREM
DET ↓ = less physiological determinism
LAM / TT ↑ = specific ANS shift
```

---

## Main takeaway

> **Rolink et al. cung cấp direct evidence rằng recurrence structure của cardio-respiratory dynamics thay đổi theo sleep/wake state. Paper rất quan trọng cho physiological relevance của RQA, nhưng không giải thích trực tiếp direction của DET/LAM/TT trong unstable Awake–Drowsy transition.**

```
# Paper 7 — Calderón-Juárez et al. (2023)
## Revisiting nonlinearity of heart rate variability in healthy aging

## Method

- Dataset lớn: **1026 healthy subjects**, 18–92 tuổi.
- Phân tích **5-min HRV từ ECG**.
- Dùng RQA:
  - `DET`
  - `LAM`
- Kết hợp **surrogate data testing** bằng wavelet-based surrogates để kiểm tra nonlinear information.
- RQA dùng:
  - FAN với recurrence density cố định 7%
  - delay từ mutual information
  - embedding dimension từ FNN

### Statistics

- mean ± SD
- ANOVA + Bonferroni
- logistic regression
- OR + **95% CI**

→ philosophy thống kê khá gần nghiên cứu hiện tại ở điểm:
`effect/direction + uncertainty + multiple-comparison control`

---

## Main findings

- Tỷ lệ HRV series được xác định là nonlinear giảm theo tuổi.
- BMI và HR cao hơn liên quan đến khả năng xuất hiện nonlinear information thấp hơn.
- Female sex liên quan đến tỷ lệ nonlinear HRV cao hơn.
- DET và LAM thay đổi theo age/sex, nhưng metric value không được xem là proof trực tiếp của complexity loss.

---

## Physiological interpretation

Nonlinear HRV được xem là kết quả của tương tác liên tục giữa:

```text
sympathetic
parasympathetic
neuroendocrine system
intrinsic cardiac nervous system
central control pathways
````

→ nonlinear organization có thể phản ánh **multisystem cardiovascular regulation**.

Authors cũng nhấn mạnh rằng cơ chế sinh học cụ thể phía sau các nonlinear changes vẫn chưa thể xác định trực tiếp.

---

## Relevance to current study

Paper rất quan trọng để tách:

```text
RQA metric value
≠
proof of nonlinearity
```

và:

```text
surrogate testing
→ evidence for nonlinear information

DET / LAM comparison
→ description of recurrence organization
```

Điều này phù hợp trực tiếp với:

```text
RQ1:
PPS surrogate rejection

RQ2:
DET / LAM changes
```

---

## Relation to current findings

Current study:

```text
DET ↓
LAM ↑ tendency
```

Paper này giúp giữ claim boundary:

```text
DET ↓
≠ less complexity
≠ less determinism
≠ less chaos

LAM ↑
≠ more/less nonlinear
```

RQA metrics nên được diễn giải như **changes in recurrence geometry**, không phải scalar measure của toàn bộ system complexity.

---

## Discussion role

### RQ1

Strong support cho việc dùng **surrogate testing** để kiểm tra nonlinear organization.

### RQ2

Support việc xem `DET` và `LAM` như các descriptive dynamical properties khác nhau.

### Physiological foundation

Support rằng nonlinear cardiovascular dynamics có thể sinh ra từ **interacting regulatory systems**.

### Statistical reporting

Supporting precedent cho:

* confidence intervals
* effect-oriented reporting
* multiple-comparison correction

Nhưng không phải direct justification cho bootstrap median CI của nghiên cứu hiện tại.

---

## Main takeaway

> **Calderón-Juárez et al. củng cố distinction giữa nonlinearity testing và RQA metric interpretation: surrogate testing dùng để xác nhận nonlinear information, còn DET/LAM chỉ mô tả các khía cạnh khác nhau của recurrence organization. Đây là reference rất mạnh cho claim boundaries của nghiên cứu hiện tại.**

```
# Paper 3 — Porta et al. (2007)

## Method

- Phân tích **short-term RR interval dynamics** (~240–350 beats).
- Dùng **local nonlinear prediction** trên reconstructed phase space.
- Đánh giá:
  - **predictability / complexity**
  - **nonlinearity** bằng surrogate testing.
- Surrogates: FT, AAFT, IAAFT-1, IAAFT-2.

Nguyên lý:

```text
similar past states
→ similar future evolution
→ prediction quality reflects dynamical predictability
````

---

## Main findings

* Different prediction methods cho absolute values khác nhau nhưng **physiological changes được detect khá nhất quán**.
* Sympathetic activation và complete vagal blockade:

```text
predictability ↑
regularity ↑
complexity ↓
```

* Short-term RR dynamics lúc nghỉ chủ yếu **linear**.
* Autonomic imbalance không tự động làm nonlinear components tăng.
* **Complexity / predictability ≠ nonlinearity**.

---

## Physiological interpretation

Cardiovascular dynamics sinh ra từ nhiều interacting mechanisms:

```text
sympathetic / parasympathetic regulation
baroreflex
respiration
vasomotor oscillations
feedback loops
```

Thay đổi autonomic regulation có thể làm thay đổi **predictability / complexity**, nhưng không thể suy trực tiếp:

```text
predictability change
→ more/less chaos
```

---

## Relevance to current study

Rất gần về methodological logic:

```text
Porta:
RR → local nonlinear prediction → predictability

Current study:
PPG → Simplex Projection → CC / NRMSE
```

Do đó:

```text
CC ↓ / NRMSE ↑
→ reduced finite-horizon forecastability
```

không nên diễn giải là:

```text
more chaos
```

Ngoài ra, pattern của Porta:

```text
sympathetic activation → predictability ↑
```

khác với:

```text
Drowsy → predictability ↓
```

→ Awake–Drowsy change khó giải thích bằng một simple sympathetic shift.

---

## Discussion role

### RQ1

* Hỗ trợ tách rõ:

  * nonlinearity
  * complexity
  * predictability
* Surrogate rejection phải được diễn giải theo **specific null hypothesis**.

### RQ2

* Là reference quan trọng để diễn giải `CC↓ / NRMSE↑` như **reduced forecastability**.
* Cung cấp bridge:

```text
physiological/autonomic perturbation
→ altered cardiovascular dynamics
→ altered short-term predictability
```

---

## Main takeaway

> **Porta et al. cung cấp methodological foundation mạnh cho việc dùng local prediction để đặc trưng short-term cardiovascular dynamics, đồng thời cho thấy predictability/complexity và nonlinearity là các properties khác nhau.**

# Paper 9 — Porta et al. (2007)
## Symbolic analysis of HRV during graded head-up tilt

## Method

- 17 healthy subjects.
- Phân tích **short-term RR series từ ECG** (~220–260 beats).
- Dùng symbolic analysis với 4 pattern families:
  - `0V`: no variation
  - `1V`: one variation
  - `2LV`: two like variations
  - `2UV`: two unlike variations
- Graded head-up tilt: `0° → 90°`.
- So sánh symbolic indexes với spectral HRV.
- Kết quả được báo bằng **median (Q1–Q3)** và nonparametric statistics.

---

## Main findings

Khi tilt angle tăng:

```text
0V ↑
2UV ↓
2LV ↓
1V thay đổi ít
````

`0V` và `2UV` theo dõi graded autonomic shift tốt hơn nhiều spectral indexes ở individual level.

Nếu gộp:

```text
2V = 2LV + 2UV
```

thì interpretation vẫn phù hợp với framework của Guzzetti.

---

## Physiological interpretation

Head-up tilt gây:

```text
sympathetic modulation ↑
parasympathetic modulation ↓
```

và symbolic response tương ứng:

```text
0V ↑
→ compatible with increased sympathetic modulation

2UV / 2V ↓
→ compatible with reduced vagal modulation
```

Quan trọng:

> sympathetic và parasympathetic changes không nhất thiết reciprocal hoàn toàn về magnitude.

`0V` và `2UV` có thể phản ánh **different and partially independent aspects of autonomic regulation**.

---

## Relevance to current study

Current study:

```text
PPG-derived RR
→ 0V ↑
→ 2V ↓
→ 1V ≈ unchanged
```

Pattern này qualitatively rất gần với response trong graded tilt.

Do đó symbolic result hiện tại có thể được diễn giải là:

> **consistent with altered cardiac autonomic modulation, potentially involving relatively greater sympathetic and/or reduced vagal modulation.**

Tuy nhiên:

```text
Drowsiness ≠ head-up tilt
PPG-derived RR ≠ ECG RR
```

nên không nên xem đây là direct proof của sympathetic activation.

---

## Role in Discussion

### Physiological anchor

Đây là một trong những reference mạnh nhất cho symbolic findings:

```text
0V ↑
2V ↓
→ autonomic cardiac reorganization
```

### Support cho ANS interpretation

Cung cấp experimental validation rằng symbolic patterns có thể track gradual sympathetic/vagal changes.

### Integration với NTSA findings

Symbolic analysis cung cấp physiological support ở beat-to-beat level:

```text
RR symbolic dynamics
→ altered autonomic cardiac modulation

PPG waveform NTSA
→ altered forecastability / recurrence / divergence
```

### Claim boundary

Không nên viết:

```text
0V ↑ = sympathetic activation proven
2V ↓ = parasympathetic withdrawal proven
```

Nên viết:

```text
consistent with / compatible with
```

---

## Main takeaway

> **Porta et al. cung cấp strong physiological support cho việc diễn giải pattern `0V↑ / 2V↓` như một dấu hiệu của altered cardiac autonomic modulation, nhưng không đủ để suy ra trực tiếp sympathetic/vagal activity trong drowsiness.**

```


# Paper 4 — Porta et al. (2015)

## Main idea

Short-term heart period variability có thể chứa **nhiều loại nonlinear dynamics khác nhau**, hoạt động ở các temporal scales khác nhau.

Do đó:

> Một metric không nhất thiết capture toàn bộ nonlinear organization của cardiovascular dynamics.

---

## Method

Hai nonlinear approaches được áp dụng trên cùng data:

### 1. Time irreversibility — NV%
- embedding dimension cố định `L = 2`
- nhạy với **very short time scales**
- departure khỏi reversibility → evidence of nonlinearity

### 2. Local prediction — UPI
- reconstructed phase space với optimized embedding dimension
- `k = 30`, Euclidean distance
- UPI thấp → predictability cao
- capture **longer temporal scales**

Cả hai được kết hợp với **IAAFT surrogate testing**.

---

## Main findings

Hai methods cho kết quả khác nhau trên cùng dữ liệu:

```text
Time irreversibility
→ detect one nonlinear component

Local prediction
→ detect another nonlinear component
````

Sự khác biệt không nhất thiết là contradiction.

Nguyên nhân chính:

> chúng khảo sát các **temporal scales khác nhau**.

---

## Physiological interpretation

Cardiovascular regulation gồm nhiều interacting mechanisms hoạt động ở nhiều time scales.

Do đó nonlinear dynamics quan sát được có thể là kết quả của:

```text
multiple regulatory mechanisms
+ sympatho-vagal interactions
+ respiration
+ other cardiovascular control processes
```

Paper đặc biệt thận trọng:

> Không thể gán một nonlinear component cụ thể trực tiếp cho sympathetic hoặc parasympathetic activity.

---

## Relevance to current study

Rất quan trọng cho nghiên cứu hiện tại vì bạn cũng sử dụng nhiều NTSA metrics:

```text
Simplex
→ forecastability

RQA
→ recurrence organization

LLE
→ local divergence
```

Các metric này không nhất thiết phải thay đổi cùng chiều vì chúng đang probe **different dynamical properties / temporal organizations**.

Điều này giúp giải thích vì sao:

```text
CC ↓ / NRMSE ↑
nhưng
LLE ↓
```

không nhất thiết là contradiction.

---

## Discussion role

### RQ1

* Hỗ trợ mạnh claim rằng nonlinear dynamics là **multiscale and method-dependent**.
* Surrogate rejection chỉ cho biết observed dynamics vượt quá specific null ở property được kiểm tra.

### RQ2

* Cung cấp framework để giải thích các NTSA metrics như **complementary views**, không phải các phép đo thay thế cho cùng một quantity.
* Rất hữu ích để bảo vệ việc Simplex, RQA và LLE có thể cho các direction khác nhau.

---

## Main takeaway

> **Porta et al. (2015) mở rộng Porta 2007 bằng cách cho thấy nonlinear cardiovascular dynamics có thể gồm nhiều components ở các temporal scales khác nhau; vì vậy các nonlinear metrics khác nhau có thể đưa ra những kết quả khác nhau nhưng vẫn đồng thời đúng.**

```

Điểm này thực sự rất gần với vấn đề trung tâm của Discussion của bạn: **`forecastability ↓` nhưng `LLE ↓` không cần phải “giải hòa” thành một scalar complexity duy nhất; chúng có thể phản ánh các dynamical properties khác nhau của cùng một physiological transition.**
# Paper 10 — Sviridova et al. (2022)
## Photoplethysmogram Recording Length: Defining Minimal Length Requirement from Dynamical Characteristics

## Method

- Phân tích trực tiếp **NIR PPG waveform** ở healthy subjects.
- 30 recordings, mỗi recording 5 phút, sampling rate `409.6 Hz`.
- Dùng **time-delay reconstruction + RQA**.
- Parameters:
  - `m = 4`
  - `τ`: khi autocorrelation giảm dưới `1/e`
  - `ε = 10%` kích thước reconstructed attractor
- RQA metrics:
  - `DET`
  - `Lmax`
  - `L`
  - `ENTR`
- Đánh giá estimation error khi giảm recording length.
- Kiểm tra thêm trên noisy Rössler system và PPG đã subsample.

---

## Main findings

Khả năng estimate RQA phụ thuộc mạnh vào từng metric.

Với PPG, để error < 1%:

```text
DET   ≈ 2.4 s
ENTR  ≈ 17 s
L     ≈ 105 s
Lmax  ≈ 120 s
````

→ `DET` rất robust với short recordings.

→ các diagonal-length metrics như `L` và đặc biệt `Lmax` cần data dài hơn nhiều.

Sampling-rate reduction từ `409.6 → 204.8 → 102.4 Hz` chỉ làm thay đổi nhỏ minimum-length estimates trong dataset này.

---

## Relevance to current study

Đây là một trong những paper gần nhất về:

```text
PPG waveform
+
phase-space reconstruction
+
RQA
+
short recording length
```

Current study sử dụng:

```text
30 / 60 / 120 / 180 s windows
```

Do đó paper support mạnh rằng **short-window PPG RQA là khả thi**, nhưng độ ổn định phụ thuộc metric.

Đặc biệt:

```text
DET
→ expected to be relatively robust even for short windows

L / diagonal-length measures
→ more sensitive to window length
```

Điều này phù hợp với current findings:

```text
DET ↓
→ stable across window durations

Lmean ↓
→ weaker / less statistically stable
```

---

## Methodological relevance

Paper nhấn mạnh:

> recording length là một parameter quan trọng của nonlinear time-series analysis.

Do đó hỗ trợ trực tiếp việc current study:

* kiểm tra `30 / 60 / 120 / 180 s`
* chọn `60 s` như practical compromise
* không giả định tất cả NTSA metrics có cùng minimum data requirement

Paper cũng cảnh báo rằng **filtering có thể thay đổi nonlinear dynamical characteristics của PPG**, nên preprocessing cần được kiểm soát và giữ nhất quán.

---

## Physiological / dynamical interpretation

Paper chủ yếu là methodological, không nghiên cứu Awake–Drowsy physiology.

Nó support rằng PPG waveform chứa measurable dynamical structure có thể được đặc trưng bằng phase-space / recurrence analysis.

Tuy nhiên authors dùng các claim khá mạnh như:

```text
PPG dynamics → deterministic chaos
DET > 0.9 → sign of determinism
1/Lmax → trajectory divergence
```

Các claim này không nên transfer trực tiếp vào current manuscript.

Current study nên giữ interpretation thận trọng hơn:

```text
DET
→ diagonal recurrence organization

L
→ average diagonal persistence

LLE
→ local trajectory divergence

surrogate testing
→ evidence relative to a specified null
```

---

## Role in Discussion

### Short-window justification

Strong reference cho việc **ultra-short PPG dynamics có thể được estimated bằng RQA**, đặc biệt với `DET`.

### Window-length robustness

Rất relevant để giải thích vì sao:

```text
DET
→ stable across short windows

Lmean
→ potentially more duration-sensitive
```

### Methodological precedent

Một trong các nghiên cứu gần nhất sử dụng:

```text
raw PPG waveform → reconstructed dynamics → RQA
```

### Claim boundary

Không dùng paper để claim:

```text
PPG is definitively chaotic
DET > 0.9 proves physical determinism
60 s is universally sufficient for every NTSA metric
```

Kết quả của họ áp dụng cho specific NIR PPG, acquisition setting và RQA parameterization.

---

## Main takeaway

> **Sviridova et al. cung cấp strong methodological support cho việc phân tích nonlinear dynamics trên short PPG waveform. Quan trọng nhất, paper cho thấy minimum recording length phụ thuộc mạnh vào từng dynamical metric: DET ổn định rất sớm, trong khi diagonal-length measures cần recordings dài hơn đáng kể.**

```

# Paper 2 — Tobaldini et al. (2013)

## Physiological Foundation

- Wake → sleep là một **complex physiological transition** có sự tham gia của nhiều cơ chế điều hòa:
  - sympathetic / parasympathetic modulation
  - baroreflex / chemoreflex
  - respiration
  - central oscillators
  - hormonal regulation

- Trong **drowsiness / sleep onset**:
  - alpha rhythm giảm
  - theta rhythm bắt đầu xuất hiện
  - autonomic cardiovascular regulation bắt đầu thay đổi

- Cardiovascular dynamics vì vậy được tạo bởi nhiều interacting control mechanisms ở nhiều time scales.

> Điều này cung cấp physiological foundation rằng PPG dynamics có thể chứa cấu trúc phức tạp hơn một simple periodic / pseudoperiodic process.

---

## Relevance to current study

Dataset hiện tại phù hợp hơn với:

```text
Awake ↔ Drowsiness ↔ Awake ↔ Drowsiness
````

hơn là:

```text
Awake → N1 → N2 → N3
```

Do đó drowsiness nên được xem như một **unstable transitional regime near sleep onset**, không phải established NREM sleep.

Các findings của NREM như:

```text
HR ↓
BP ↓
MSNA ↓
parasympathetic modulation ↑
```

chỉ nên dùng như **broader physiological context**, không phải direct evidence cho drowsiness trong dataset.

---

## Role in Discussion

### RQ1 — Null test

Paper này hỗ trợ khá tốt:

> Cardiovascular dynamics được hình thành bởi nhiều interacting regulatory mechanisms, nên việc observed PPG dynamics vượt quá một noisy pseudoperiodic null có physiological plausibility.

### RQ2 — Awake vs Drowsy

Paper chỉ hỗ trợ ở mức high-level:

> Awake → Drowsy có thể liên quan đến reorganization của autonomic cardiovascular control trong wake-to-sleep transition.

Nhưng chưa giải thích trực tiếp direction của:

```text
CC ↓
NRMSE ↑
DET ↓
LLE ↓
LAM / TT ↑ tendency
```

→ cần metric-specific literature.

---

## Claim boundary

Không nên suy ra trực tiếp:

```text
Drowsiness = NREM
Drowsiness = N1
PPG metric change = sympathetic/vagal change
```

Cách diễn giải phù hợp hơn:

> Drowsiness represents a transitional physiological regime near sleep onset, in which cardiovascular autonomic regulation is being reorganized.




# Paper 11 — Vaussenat et al. (2026)
## Early Drowsiness Detection via HRV Derivative Analysis

## Method

- 25 participants, 49 driving-simulator sessions.
- Non-contact capacitive ECG từ seat backrest.
- RR intervals được dùng để tính:
  - conventional HRV metrics
  - first derivative `dRRI/dt`
  - second derivative `d²RRI/dt²`
- Features được tính trên **30 s windows, 50% overlap**.
- Ground truth classification dựa trên **crash proximity**, độc lập với HRV features.
- Drowsiness labels mô tả dựa trên behavioral indicators:
  - PERCLOS
  - yawning
  - blink
  - posture

---

## Main idea

Paper xem early drowsiness như một **dynamic transition**, không phải static physiological state.

```text
conventional HRV
→ autonomic state

HRV derivatives
→ transition dynamics
````

Trong đó:

```text
1st derivative
→ velocity / direction of cardiac change

2nd derivative
→ acceleration / transition onset
```

---

## Main findings

* HRV derivatives alone có discriminative power thấp:

  * 1st derivative AUC ≈ 0.549
  * 2nd derivative AUC ≈ 0.568
  * derivatives combined AUC ≈ 0.573
* Khi kết hợp với conventional HRV:

```text
AUC ≈ 0.863
```

→ derivatives chủ yếu cung cấp **complementary transition information**.

HRV-based detection xuất hiện:

```text
~5.8 min trước PERCLOS
~6.8 min trước crash
```

→ cardiac physiological changes có thể xuất hiện trước overt behavioral manifestations.

---

## Physiological interpretation

Authors diễn giải drowsiness onset như một gradual autonomic shift:

```text
sympathetic dominance
→ parasympathetic dominance
```

với:

```text
RRI ↑
HR ↓
RMSSD ↑
HF ↑
```

First derivative phản ánh hướng thay đổi của cardiac rhythm, còn second derivative được xem như marker của transition onset.

Tuy nhiên đây vẫn là **HRV-based physiological interpretation**, không phải direct measurement của sympathetic/vagal neural activity.

---

## Relevance to current study

Paper rất gần với current phenomenon:

```text
Alert / Awake
→ early Drowsiness transition
```

và support mạnh rằng:

> Drowsiness nên được xem như một **time-varying physiological transition**, không chỉ hai static classes.

Điều này phù hợp với current dataset:

```text
Awake ↔ Drowsy ↔ Awake ↔ Drowsy
```

và với việc dùng short windows để capture transition dynamics.

---

## Important contrast with current symbolic result

Vaussenat:

```text
Drowsiness
→ parasympathetic dominance ↑
→ sympathetic dominance ↓
```

Current symbolic analysis:

```text
0V ↑
2V ↓
```

theo Guzzetti / Porta framework:

```text
→ compatible with sympathetic modulation ↑
and/or vagal modulation ↓
```

Hai interpretations không hoàn toàn cùng chiều.

Điều này gợi ý rằng current Awake–Drowsy regime có thể không phải một simple monotonic sympathovagal shift, mà là một **unstable autonomic reorganization**.

---

## Short-window relevance

Paper dùng:

```text
30 s windows
50% overlap
```

để giữ temporal resolution của transition.

Authors cũng thừa nhận 30 s không đủ chuẩn cho reliable LF-HRV estimation.

→ support quan trọng rằng:

> short windows có thể cần thiết để capture transition dynamics, dù estimator reliability phải được cân bằng với temporal resolution.

---

## Discussion role

### Physiological foundation

Strong direct reference cho idea:

```text
early drowsiness
→ dynamic cardiovascular/autonomic transition
```

### Transition-based interpretation

Support việc current study tập trung vào **dynamical changes**, thay vì static feature differences.

### Short-window justification

Cung cấp precedent rằng short windows có thể phù hợp khi mục tiêu là capture onset / transition.

### Complementary-metrics principle

Derivatives alone không đủ mạnh nhưng bổ sung thông tin khi kết hợp với HRV.

Điều này phù hợp với current framework:

```text
Simplex
RQA
LLE
Symbolic RR
```

→ complementary views of the same transition.

### Claim boundary

Không nên dùng paper để claim:

```text
Drowsiness = parasympathetic dominance
Light drowsiness = N1
HRV derivative = direct ANS measurement
current study detects drowsiness earlier than behavior
```

---

## Main takeaway

> **Vaussenat et al. cung cấp direct support rằng early drowsiness là một dynamic autonomic/cardiovascular transition và rằng short-term cardiac changes có thể xuất hiện trước behavioral manifestations. Paper đặc biệt quan trọng để support transition-based physiological interpretation của current study, nhưng sympathovagal direction vẫn nên được xem là literature-based interpretation chứ không phải direct neural evidence.**

```

# Paper 8 — Yeragani et al. (2004)
## LLE of heart-rate dynamics across frequency bands

## Method

- Phân tích **HR / RR dynamics từ ECG**.
- So sánh:
  - Awake vs Sleep
  - Supine vs Standing
  - Healthy controls vs Panic disorder
- Tính:
  - Minimum Embedding Dimension (MED)
  - Largest Lyapunov Exponent (LLE)
- Dùng **Rosenstein algorithm** để ước lượng LLE.
- Tách HR time series thành:
  - VLF: < 0.04 Hz
  - LF: 0.04–0.15 Hz
  - HF: 0.15–0.5 Hz
- Sau đó tính LLE riêng cho từng band.

---

## Main findings

Ở healthy controls:

```text
Sleep:
UF-LLE ↑
HF-LLE ↑

Standing:
LF-LLE ↑
HF-LLE ↓
````

→ LLE thay đổi theo physiological state và frequency content.

Paper cũng cho thấy:

* LLE phụ thuộc vào **sampling rate**
* data length ảnh hưởng estimation
* preprocessing/filtering có thể ảnh hưởng nonlinear measures

---

## Physiological interpretation

Authors đề xuất:

```text
HF-LLE
→ có thể liên quan vagal modulation

LF-LLE / HF-LLE
→ có thể phản ánh relative sympathovagal interaction
```

Tuy nhiên chính authors nhấn mạnh rằng các mapping này vẫn cần **physiological/pharmacological validation**.

Do đó không nên hiểu:

```text
LLE ↑/↓
→ direct sympathetic/vagal ↑/↓
```

---

## Relevance to current study

Current study:

```text
PPG waveform
→ bandpass 0.5–8 Hz
→ Rosenstein LLE
```

Yeragani:

```text
HR/HRV
→ VLF/LF/HF decomposition
→ band-specific LLE
```

Hai loại frequency band **không tương đương**.

Vì vậy LLE hiện tại nên được diễn giải là:

> **local divergence of PPG waveform dynamics**

không phải direct autonomic-band LLE.

---

## Relation to current finding

Current study:

```text
Drowsy → LLE ↓
```

Yeragani:

```text
Sleep → LLE ↑
```

→ cho thấy LLE direction phụ thuộc physiological context.

Điều này support rằng:

> Drowsiness không nên được đồng nhất với established sleep.

---

## Role in Discussion

### LLE interpretation

Strong reference để support:

```text
LLE
→ local trajectory divergence / sensitivity to nearby states
```

### Physiological sensitivity

Cho thấy LLE thay đổi theo sleep/posture/autonomic perturbation.

### Claim boundary

Không nên suy:

```text
LLE ↓ = less chaos
LLE ↓ = parasympathetic ↑
LLE ↓ = sympathetic ↓
```

### Robustness

Hữu ích để support việc:

* giữ sampling rate nhất quán
* kiểm tra data-length dependence
* thận trọng với preprocessing/filtering

---

## Main takeaway

> **Yeragani et al. cho thấy LLE của cardiovascular dynamics nhạy với physiological state, nhưng direction và physiological meaning phụ thuộc mạnh vào signal representation, frequency content và autonomic context. Vì vậy LLE trong nghiên cứu hiện tại nên được diễn giải như local trajectory divergence, không phải direct marker của sympathetic/vagal activity hay chaos.**

```
# Paper 1 — de Zambotti et al. (2018)

## Liên quan đến nghiên cứu hiện tại

- **Drowsiness không đồng nghĩa với PSG-defined sleep onset hoặc N1**, nhưng là trạng thái sinh lý rất gần với **wake-to-sleep transition**.
- Sleep onset là một **transitional physiological regime**, đi kèm thay đổi đồng thời ở:
  - CNS regulation
  - ANS regulation
  - respiration
  - baroreflex
  - cardiovascular control

Vì vậy, Awake → Drowsy nên được nhìn như một **quá trình tái tổ chức sinh lý đa chiều**, không chỉ là một simple sympathetic/vagal shift.

## Liên hệ với findings

```text
CC ↓ / NRMSE ↑
→ có thể phù hợp với transitional-state instability
→ regulatory configuration thay đổi theo thời gian
→ finite-horizon predictability giảm
````

```text
DET ↓ / LLE ↓ / LAM-TT ↑
→ paper này chưa giải thích trực tiếp
→ nhưng phù hợp với ý tưởng multidimensional dynamical reorganization
```

## Claim boundaries quan trọng

```text
PPG ≠ direct ANS measurement
PPG ≠ direct sympathetic/vagal measurement
Drowsy ≠ N1
Drowsiness ≠ more/less chaos
```

Cách diễn giải phù hợp:

> Các thay đổi PPG dynamics có thể phản ánh sự thay đổi của cardiovascular/autonomic regulation trong quá trình wake-to-sleep transition.

## Takeaway chính

> **Drowsiness có thể được xem là một transitional state gần với sleep onset, trong đó cardiovascular regulation đang được tái tổ chức; điều này cung cấp physiological context hợp lý cho các thay đổi đa chiều của PPG dynamics trong nghiên cứu hiện tại.**



## Physiological foundation

- Drowsiness có thể được xem là một **complex transitional regime** gần với **sleep onset**.
- Wake-to-sleep transition liên quan đến sự tái tổ chức đồng thời của nhiều hệ:
  - CNS
  - ANS
  - respiration
  - baroreflex
  - cardiovascular regulation
- **N1** là sleep stage được chuẩn hóa bằng PSG và đại diện gần nhất cho giai đoạn chuyển tiếp này.

### Main implication

> Awake → Drowsy nên được diễn giải như một **multisystem physiological reorganization**, không phải một simple sympathetic/vagal shift.

## Role in Discussion

### RQ1 — Null test
Cung cấp physiological foundation cho việc PPG có thể chứa dynamical organization phức tạp hơn một noisy pseudoperiodic process, do cardiovascular dynamics chịu ảnh hưởng của nhiều interacting regulatory systems trong wake-to-sleep transition.

### RQ2 — Awake vs Drowsy
Chỉ cung cấp high-level physiological context rằng drowsiness/sleep onset liên quan đến multisystem reorganization.

Paper này chưa giải thích trực tiếp direction của:
- CC / NRMSE
- DET / LAM / TT
- LLE

→ cần metric-specific literature để giải thích các finding này.

