# Tổng hợp ghi chú thảo luận

Tài liệu này tập hợp nguyên văn nội dung của toàn bộ 17 file ghi chú trong thư mục dicussion (không tính summary.md).

## Danh mục nguồn

- [# Paper 1 — de Zambotti et al. (2018)](Zambotti_2018.md)
- [# Paper 2 — Tobaldini et al. (2013)](Tobaldini_2013.md)
- [# Paper 3 — Porta et al. (2007)](Porta_2007.md)
- [# Paper 4 — Porta et al. (2015)](Porta_2015.md)
- [# Paper 5 — Rolink et al. (2015)](Jorome_2015.md)
- [# Paper 6 — Martín-González et al. (2018)](Gonzales_2018.md)
- [# Paper 7 — Calderón-Juárez et al. (2023)](Juarez_2023.md)
- [# Paper 8 — Yeragani et al. (2004)](Yeragani_2004.md)
- [# Paper 9 — Porta et al. (2007)](Porta_2007_p2.md)
- [# Paper 10 — Sviridova et al. (2022)](Sviridova_2018.md)
- [# Paper 11 — Vaussenat et al. (2026)](Vaussenat_2026.md)
- [# Paper 12 — Shinar et al. (2006)](Shinar_2005.md)
- [# Paper 13 — Carrington et al. (2005)](Carrington_2005.md)
- [# Paper 14 — Tsai et al. (2019)](Tsai_2016.md)
- [# Paper 15 — Faes et al. (2016)](Paes_2016.md)
- [# Paper 16 — Hu, Gao & Tung (2009)](Hu_2009.md)
- [# Paper 17 — Carrington et al. (2003)](Carrington_2003.md)

## Nội dung nguyên văn

---

**Nguồn: [Zambotti_2018.md](Zambotti_2018.md)**

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


---

**Nguồn: [Tobaldini_2013.md](Tobaldini_2013.md)**

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





---

**Nguồn: [Porta_2007.md](Porta_2007.md)**

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


---

**Nguồn: [Porta_2015.md](Porta_2015.md)**


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

---

**Nguồn: [Jorome_2015.md](Jorome_2015.md)**

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

---

**Nguồn: [Gonzales_2018.md](Gonzales_2018.md)**

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

---

**Nguồn: [Juarez_2023.md](Juarez_2023.md)**

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

---

**Nguồn: [Yeragani_2004.md](Yeragani_2004.md)**

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

---

**Nguồn: [Porta_2007_p2.md](Porta_2007_p2.md)**

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


---

**Nguồn: [Sviridova_2018.md](Sviridova_2018.md)**

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


---

**Nguồn: [Vaussenat_2026.md](Vaussenat_2026.md)**

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


---

**Nguồn: [Shinar_2005.md](Shinar_2005.md)**

# Paper 12 — Shinar et al. (2006)
## Thay đổi thần kinh tự chủ trong quá trình chuyển từ thức sang ngủ

## Phương pháp

- 34 đối tượng được đo bằng **polysomnography toàn đêm**:
  - 12 người bình thường
  - 11 bệnh nhân OSAS
  - 11 người có các rối loạn giấc ngủ khác
- Các tín hiệu gồm:
  - EEG / EOG
  - EMG
  - ECG-derived RR intervals
  - hô hấp
  - pulse wave
- Phân tích giai đoạn quanh **sleep onset (SO)** trong cửa sổ 19 phút.
- HRV được phân tích theo time-frequency bằng wavelet:
  - VLF: `0.005–0.04 Hz`
  - LF: `0.04–0.15 Hz`
  - HF: `0.15–0.5 Hz`
  - LF/HF
- Multiple comparisons được hiệu chỉnh bằng **BH-FDR**.

---

## Ý tưởng chính

Sleep onset không phải một sự kiện xảy ra tại một thời điểm duy nhất.

```text
Wake
↔ dao động mức tỉnh táo
↔ giai đoạn ngủ sớm
→ giấc ngủ ổn định
```

Tác giả cho thấy một số đối tượng có thể **dao động qua lại giữa wakefulness và sleep** trước khi đạt được stable sleep.

> Quá trình đi vào giấc ngủ nên được xem là một **transitional process**, không phải một discrete event.

---

## Kết quả chính

Trong quá trình sleep onset:

```text
RRI ↑
→ HR ↓

RRI variability ↓

respiratory rate ≈ không đổi
respiratory variability ↓

EMG amplitude ↓
EMG variability ↓
```

HRV frequency dynamics:

```text
VLF ↓ mạnh
→ bắt đầu khoảng 2 phút trước SO

LF ↓

HF ≈ không thay đổi đáng kể

LF/HF ↓
```

Nhiều chỉ số variability đạt mức thấp nhất khoảng `1–2 phút` sau SO.

---

## Diễn giải sinh lý

Tác giả diễn giải wake–sleep transition như một quá trình **tái tổ chức / resetting của autonomic regulation**.

```text
wake-like autonomic regulation
→ progressive transition
→ lower sympathovagal balance
→ stable sleep physiology
```

`LF/HF ↓` được diễn giải là xu hướng dịch chuyển về phía **parasympathetic predominance**.

Tuy nhiên:
- VLF và LF chịu ảnh hưởng của nhiều cơ chế sinh lý.
- HF không tăng đáng kể.
- Vì vậy đây vẫn là **HRV-based interpretation**, không phải đo trực tiếp sympathetic/vagal neural activity.

Điểm đặc biệt quan trọng:

> **Autonomic changes có thể bắt đầu trước EEG-defined sleep onset.**

Cụ thể:

```text
VLF ↓
→ xuất hiện trước các thay đổi EEG rõ rệt
```

---

## Liên quan đến nghiên cứu hiện tại

Paper này rất gần với hiện tượng trong dataset hiện tại:

```text
Awake ↔ Drowsy ↔ Awake ↔ Drowsy
```

Shinar cho thấy trước khi stable sleep hình thành có thể tồn tại:

```text
wake–sleep fluctuations
+
physiological fluctuations
```

Điều này support trực tiếp cách xem Drowsiness là:

> **một unstable transitional regime gần sleep onset**

chứ không phải:

```text
Drowsiness = N1
hoặc
Drowsiness = stable NREM
```

---

## Điểm quan trọng về định nghĩa Sleep Onset

Tác giả nhận thấy standard sleep-onset criteria có thể gây nhầm khi đối tượng liên tục oscillate giữa wake và sleep.

Do đó họ yêu cầu:

```text
EEG alpha giảm bền vững
trong ít nhất 5 phút
```

để đánh dấu **steady, unequivocal sleep**.

Ý nghĩa đối với nghiên cứu hiện tại:

> Xuất hiện early sleep / Stage-1-like activity chưa có nghĩa toàn bộ physiological system đã ổn định sang sleep.

---

## Liên hệ với findings hiện tại

Paper không trực tiếp giải thích direction của:

```text
CC ↓ / NRMSE ↑
DET ↓
LLE ↓
LAM / TT ↑ tendency
```

nhưng support mạnh cho overarching interpretation:

```text
Wake → Drowsiness
→ regulatory configuration thay đổi
→ multidimensional dynamical reorganization
```

Các vigilance fluctuations cũng tạo physiological context hợp lý cho việc **finite-horizon predictability giảm**.

---

## Điểm đối lập với Symbolic Analysis

Shinar diễn giải:

```text
sleep onset
→ sympathovagal balance ↓
→ parasympathetic predominance ↑
```

Trong khi current symbolic result:

```text
0V ↑
2V ↓
```

theo Porta/Guzzetti lại tương thích với:

```text
sympathetic modulation tương đối ↑
và/hoặc
vagal modulation ↓
```

Hai directions này không hoàn toàn一致.

Điều này gợi ý rằng current Drowsiness có thể phản ánh một:

> **unstable, repeatedly switching autonomic regime**

thay vì một monotonic transition liên tục về phía stable sleep.

Không nên ép hai kết quả này thành một sympathovagal narrative duy nhất.

---

## Ý nghĩa phương pháp

Paper nhấn mạnh rằng sleep onset là một quá trình **non-stationary**, nên các phương pháp steady-state truyền thống có thể bỏ lỡ transition dynamics.

```text
transient physiology
→ cần time-resolved analysis
```

Điều này support về mặt khái niệm cho việc sử dụng:

```text
short-window NTSA
```

trong nghiên cứu hiện tại.

---

## Vai trò trong Discussion

### Physiological backbone

Đây là một trong những reference mạnh nhất để support:

> **Sleep onset là một quá trình động, không phải một thời điểm rời rạc.**

### Direct support cho unstable transition

Cung cấp bằng chứng trực tiếp rằng:

```text
Wake ↔ Sleep fluctuations
```

có thể xảy ra trước khi stable sleep được thiết lập.

### ANS interpretation

Cho thấy cardiovascular/autonomic regulation đã bắt đầu thay đổi trong quá trình transition, thậm chí trước khi stable sleep xuất hiện.

### RQ1

Cung cấp physiological plausibility cho việc PPG dynamics phức tạp hơn một simple stationary pseudoperiodic process.

### RQ2

Support cách diễn giải Awake → Drowsy như:

> **một transition giữa các regulatory regimes**

thay vì chỉ là khác biệt giữa hai static states.

### Claim boundary

Không nên suy ra:

```text
Drowsiness = N1
Drowsiness = stable NREM
LF/HF là direct measure hoàn hảo của sympathovagal balance
NTSA metrics hiện tại trực tiếp đo ANS activity
```

---

## Main takeaway

> **Shinar et al. cung cấp bằng chứng trực tiếp rằng wake–sleep transition là một quá trình sinh lý không ổn định và biến thiên theo thời gian, trong đó các thay đổi của autonomic, cardiac, respiratory, muscular và EEG xuất hiện ở những thời điểm khác nhau trước khi stable sleep được thiết lập. Paper này support rất mạnh việc diễn giải Awake–Drowsy trong nghiên cứu hiện tại như một transitional regulatory regime thay vì một static sleep state.**

---

**Nguồn: [Carrington_2005.md](Carrington_2005.md)**

# Paper 13 — Carrington et al. (2005)
## Thay đổi chức năng tim mạch trong giai đoạn sleep onset ở người trẻ

## Phương pháp

- 21 healthy young adults.
- Theo dõi từ **1 giờ trước lights out** đến hết first NREM period.
- Đo liên tục:
  - ECG / HR
  - systolic BP / diastolic BP
  - baroreflex activity
  - EEG / EOG / EMG để xác định sleep-wake state
- Sleep onset được chia thành 5 phase:

```text
Phase 1
→ relaxed presleep wakefulness

Phase 2
→ lights out → trước Stage 1

Phase 3
→ Stage 1 + repeated arousals

Phase 4
→ Stage 1/2 + repeated arousals

Phase 5
→ stable NREM after last arousal
```

Phases 3–4 được xem là giai đoạn **sleep–wake state instability**.

---

## Kết quả chính

Từ wakefulness đến stable sleep:

```text
SBP ↓ ~12 mmHg
DBP ↓ ~7 mmHg
HR ↓ ~6.6 bpm
```

Nhưng quá trình giảm **không monotonic**.

Đặc biệt:

```text
after lights out
→ BP / HR bắt đầu giảm

during unstable Stage 1–2 with arousals
→ decline bị chậm / gián đoạn

stable sleep
→ BP / HR tiếp tục giảm và ổn định
```

---

## Vai trò của arousal

Có 435 spontaneous arousals trong phases 3–4.

Mỗi arousal gây:

```text
BP ↑ transiently
HR ↑ transiently
```

và peak response có thể quay gần về mức wakefulness.

Quan trọng hơn:

> repeated arousals không chỉ tạo transient spikes mà còn **retard underlying cardiovascular decline** trong quá trình sleep onset.

Số arousals nhiều hơn liên quan đến:
- sleep onset latency dài hơn
- BP / HR giảm ít hơn
- tốc độ giảm BP / HR chậm hơn

---

## Physiological interpretation

Paper cho thấy sleep onset là một **multi-phase cardiovascular transition**, không phải sự chuyển trạng thái tức thời.

Pattern tổng thể:

```text
wake-like cardiovascular regulation
↓
initial decline after lights out
↓
unstable sleep-onset period with repeated arousals
↕
temporary cardiovascular reactivation
↓
stable sleep
→ lower BP / HR
```

Tác giả cũng thấy baroreflex activity nhìn chung không giảm trong khi BP và HR giảm.

Do đó họ hypothesize rằng quá trình sleep onset có thể liên quan đến:

> **downward resetting of cardiovascular/baroreflex regulation**

hơn là đơn giản loss of regulatory sensitivity.

Cơ chế cụ thể của baroreflex resetting vẫn chưa được chứng minh trực tiếp.

---

## Điểm đặc biệt quan trọng

Cardiovascular changes bắt đầu:

```text
sau lights out
nhưng
trước EEG-defined Stage 1 sleep
```

Do đó:

> physiological transition có thể bắt đầu trước formal electrophysiological sleep onset.

Điều này củng cố việc không nên đồng nhất:

```text
physiological drowsiness transition
=
PSG-defined N1
```

---

## Liên quan đến nghiên cứu hiện tại

Current dataset:

```text
Awake ↔ Drowsy ↔ Awake ↔ Drowsy
```

Carrington cho thấy sleep-onset period cũng có:

```text
sleep-driving processes
↔ repeated arousals
↔ wake-like cardiovascular reactivation
```

Do đó rất phù hợp với cách xem Drowsiness như một:

> **unstable regulatory regime**

thay vì một static sleep state.

---

## Liên hệ với current NTSA findings

Paper không trực tiếp đo:

```text
CC / NRMSE
DET / LAM / TT
LLE
```

nhưng cung cấp physiological mechanism hợp lý cho:

```text
unstable cardiovascular regulation
+
repeated arousal-driven perturbations
→ less stable short-term trajectory evolution
```

Điều này có thể tạo physiological context cho:

```text
CC ↓
NRMSE ↑
```

tức **reduced finite-horizon forecastability**.

Đây vẫn là inference của current study, không phải direct finding của Carrington.

---

## Liên hệ với Symbolic Analysis

Overall sleep-onset trajectory trong paper hướng tới:

```text
HR ↓
BP ↓
stable sleep physiology
```

nhưng repeated arousals tạo:

```text
HR ↑ transiently
BP ↑ transiently
```

Do đó early sleep onset có thể chứa **mixed autonomic influences**, thay vì một simple monotonic sympathovagal shift.

Điều này giúp contextualize current pattern:

```text
0V ↑
2V ↓
```

mà không cần ép nó phải giống hoàn toàn established stable-sleep physiology.

---

## Liên hệ với Shinar et al. (2006)

```text
Shinar
→ wake–sleep transition có vigilance fluctuations

Carrington
→ arousals trong transition làm thay đổi cardiovascular trajectory
```

Hai paper bổ sung nhau rất tốt:

> **State instability không chỉ tồn tại về EEG/vigilance mà còn có measurable cardiovascular consequences.**

---

## Role in Discussion

### Physiological backbone

Strong reference cho việc:

> **sleep onset là một multi-phase physiological transition.**

### Unstable transition

Support trực tiếp rằng:

```text
Stage 1 / early Stage 2
+ repeated arousals
→ unstable cardiovascular regulation
```

### Prediction interpretation

Cung cấp physiological rationale cho hypothesis rằng unstable transition có thể làm **finite-horizon predictability giảm**.

### ANS / cardiovascular interpretation

Support cách diễn giải drowsiness như:

> **reorganization of cardiovascular control**

thay vì chỉ:

```text
sympathetic ↓
parasympathetic ↑
```

### Claim boundary

Không nên suy ra:

```text
Drowsiness = Stage 1 / Stage 2
arousal directly explains CC↓ / NRMSE↑
baroreflex resetting đã được chứng minh hoàn toàn
current PPG metrics trực tiếp đo autonomic activity
```

---

## Main takeaway

> **Carrington et al. cho thấy sleep onset là một quá trình tim mạch đa phase, trong đó BP và HR không giảm một cách monotonic mà bị gián đoạn bởi repeated arousals. Những arousals này tạo transient wake-like cardiovascular reactivation và làm chậm quá trình settling vào stable sleep. Paper cung cấp strong physiological support cho việc xem Awake–Drowsy trong nghiên cứu hiện tại như một unstable regulatory transition và tạo mechanistic context hợp lý cho reduced short-term forecastability.**

---

**Nguồn: [Tsai_2016.md](Tsai_2016.md)**

# Paper 14 — Tsai et al. (2019)
## Failure to de-arouse during sleep-onset transitions in sleep-onset insomnia

## Phương pháp

- 17 good sleepers và 17 người có **sleep-onset insomnia**.
- Đo bằng miniature polysomnography tại nhà:
  - EEG
  - EOG
  - EMG
  - ECG
- Phân tích ba mốc transition:
  - N1 onset
  - N2 onset
  - subjective sleep onset
- Với mỗi mốc:
  - phân tích cửa sổ `8 phút`
  - `4 phút trước + 4 phút sau transition`
  - HR được theo dõi với temporal resolution `20 s`
- HRV được tính trên các đoạn ECG 4 phút:
  - LF
  - HF
  - LF/HF
  - LF%

---

## Ý tưởng chính

Cardiovascular de-arousal không nhất thiết xảy ra đồng thời với cortical sleep onset.

```text
cardiac transition
≠
EEG-defined sleep onset
≠
subjective sleep onset
```

Do đó sleep onset là một quá trình **asynchronous giữa nhiều physiological systems**.

---

## Kết quả chính

### Good sleepers

Trước N1:

```text
HR bắt đầu giảm ~160 s trước N1
→ sau đó duy trì mức thấp và khá ổn định
```

Trước N2:

```text
HR đã giảm ~220 s trước N2
→ ổn định xuyên qua transition
```

→ cardiovascular de-arousal xuất hiện **trước cortical sleep onset**.

### Sleep-onset insomnia

Trước N1:

```text
HR vẫn duy trì cao
→ chỉ giảm sau khi N1 đã bắt đầu
```

Trước N2:

```text
HR bắt đầu giảm ~80 s trước N2
```

→ quá trình de-arousal bị trì hoãn.

---

## Physiological interpretation

Authors diễn giải good sleepers như sau:

```text
wake-like arousal
→ cardiac de-arousal
→ N1 transition
→ more stable N2 sleep
```

Trong khi sleep-onset insomnia thể hiện:

> **failure to de-arouse from the high-arousal wake state before N1 onset.**

Điều này cho thấy transition không chỉ phụ thuộc vào sleep stage, mà còn phụ thuộc vào:

> **khả năng hệ sinh lý chuyển từ một regulatory regime sang regime khác.**

---

## ANS findings

Ở good sleepers:

```text
HF ↑ sau N1 / N2
```

→ compatible với increased parasympathetic modulation.

Ở insomnia:

```text
LF% cao hơn trước N1
```

→ authors diễn giải là relative sympathetic predominance / incomplete de-arousal.

Quan trọng:

> autonomic direction quanh sleep onset có thể phụ thuộc vào mức độ ổn định của transition.

Do đó không nên xem sleep onset như một monotonic sympathovagal shift giống nhau ở mọi thời điểm và mọi đối tượng.

---

## N1 và N2

Paper nhấn mạnh:

```text
N1
→ light / unstable sleep stage

N2
→ more stable sleep
→ sensory disconnection rõ hơn nhờ sleep spindles / K-complexes
```

Điều này rất quan trọng với current study:

> Drowsiness có thể nằm ở vùng trước hoặc quanh unstable N1 boundary, chứ không cần phải tương đương với established N1/N2.

---

## Objective vs Subjective Sleep Onset

Thời điểm subjects cảm nhận mình "falling asleep" rất không đồng bộ với PSG.

Subjective sleep onset có thể xảy ra khi EEG vẫn đang ở:

```text
Awake
N1
N2
N3
thậm chí REM
```

HR quanh subjective sleep onset cũng không cho transition pattern rõ như N1/N2.

Điều này cho thấy:

> **subjective/behavioral sleepiness, cardiovascular transition và cortical sleep staging không nhất thiết đồng bộ theo thời gian.**

---

## Liên quan đến nghiên cứu hiện tại

Current dataset:

```text
Awake ↔ Drowsy ↔ Awake ↔ Drowsy
```

Tsai support mạnh rằng:

```text
physiological transition
→ có thể bắt đầu trước N1

N1
→ vẫn là unstable state

transition timing
→ phụ thuộc regulatory state
```

Do đó Drowsiness nên được xem như:

> **một transitional physiological regime quanh sleep onset**

chứ không phải một PSG-defined sleep stage.

---

## Liên hệ với current symbolic findings

Current symbolic result:

```text
0V ↑
2V ↓
```

theo Porta/Guzzetti:

```text
compatible with relatively greater sympathetic modulation
and/or reduced vagal modulation
```

Tsai cho thấy một wake-like / sympathetic-dominant autonomic pattern vẫn có thể tồn tại quanh N1 khi de-arousal chưa hoàn tất.

Do đó symbolic result hiện tại không nhất thiết contradict general sleep literature.

Interpretation phù hợp hơn:

> current Drowsiness có thể phản ánh **incomplete / unstable autonomic de-arousal**, thay vì một simple parasympathetic-dominant state.

Không được suy rằng current subjects có insomnia.

---

## Liên hệ với Simplex / Prediction

Paper không trực tiếp đo predictability.

Tuy nhiên nó cung cấp physiological context:

```text
different systems transition at different times
+
N1 instability
+
possible incomplete de-arousal
→ regulatory configuration thay đổi theo thời gian
```

Điều này tạo mechanistic plausibility cho:

```text
CC ↓
NRMSE ↑
```

tức reduced finite-horizon forecastability.

Đây là inference của current study, không phải direct finding của Tsai.

---

## Methodological relevance

Paper sử dụng short transition windows để giữ temporal resolution:

```text
HR: 20 s resolution
HRV: 4-min windows
```

Authors cũng thừa nhận 4-min HRV ngắn hơn standard 5-min recommendation.

→ tiếp tục support trade-off:

```text
temporal resolution
vs
estimator reliability
```

trong nghiên cứu transient physiology.

---

## Liên hệ với Shinar và Carrington

```text
Shinar 2006
→ sleep onset là process với vigilance fluctuations

Carrington 2005
→ arousals làm gián đoạn cardiovascular settling

Tsai 2019
→ cardiac de-arousal có thể precede cortical sleep onset
   và timing của transition phụ thuộc physiological state
```

Ba paper cùng support rằng:

> **Wake-to-sleep transition là một quá trình asynchronous, multidimensional và dynamically unstable.**

---

## Role in Discussion

### Physiological backbone

Strong reference cho claim:

> cardiovascular regulation có thể bắt đầu thay đổi trước PSG-defined sleep onset.

### Drowsiness interpretation

Support việc xem Drowsiness là:

> **pre-/peri-sleep-onset transitional regime**

chứ không phải N1.

### Transition instability

Giúp phân biệt:

```text
unstable N1 boundary
vs
more stable N2
```

### Symbolic ANS interpretation

Cung cấp context rằng wake-like autonomic characteristics có thể còn tồn tại quanh N1 nếu de-arousal chưa hoàn tất.

### Label / timing uncertainty

Support rằng:

```text
behavioral/subjective drowsiness
≠ exact cardiac transition
≠ exact cortical transition
```

### Claim boundary

Không nên suy:

```text
current Drowsiness = insomnia
current Drowsiness = N1
LF% = direct sympathetic measurement
symbolic pattern chứng minh incomplete de-arousal
```

---

## Main takeaway

> **Tsai et al. cho thấy cardiovascular de-arousal ở healthy sleepers có thể bắt đầu vài phút trước EEG-defined N1, trong khi N1 vẫn là một unstable transition state và sự ổn định hơn chỉ xuất hiện gần N2. Paper này support rất mạnh việc xem Awake–Drowsy như một asynchronous physiological transition, đồng thời giúp giải thích vì sao autonomic patterns quanh drowsiness không nhất thiết tuân theo một simple monotonic sympathovagal shift.**

---

**Nguồn: [Paes_2016.md](Paes_2016.md)**

# Paper 15 — Faes et al. (2016)
## Predictability decomposition of brain–heart dynamical networks during sleep

## Phương pháp

- So sánh:
  - 14 healthy controls
  - 8 bệnh nhân severe sleep apnea–hypopnea syndrome (SAHS)
  - cùng 8 bệnh nhân sau long-term CPAP treatment
- Sử dụng:
  - ECG-derived HRV
  - EEG band-power dynamics
- Tạo 6 synchronous time series:
  - cardiac parasympathetic component `η`
  - EEG: `δ, θ, α, σ, β`
- Dùng **multivariate linear autoregressive models** để phân rã predictability thành:

```text
full predictability
self-predictability
causal predictability
interaction predictability
```

Ý nghĩa:

```text
self-predictability
→ information retained in the signal's own past

causal predictability
→ additional information from other physiological processes

interaction predictability
→ redundancy / synergy among source processes
```

---

## Main findings

Trong healthy sleep:

```text
~50% cardiac dynamics
→ predictable from past cardiac + brain dynamics
```

Ở SAHS:

```text
full cardiac predictability ↓
self-predictability ↓
brain → heart causal predictability ↓
```

Healthy controls:

```text
cardiac + brain dynamics
→ structured and mutually informative
```

SAHS:

```text
temporal structure ↓
brain–heart network organization impaired
```

Một số brain-wave predictability và network interactions được phục hồi sau CPAP.

---

## Physiological interpretation

Paper xem cơ thể như một **physiological network**:

```text
brain
↔ autonomic regulation
↔ heart
```

Mỗi hệ có:

```text
internal dynamics
+
information received from other systems
```

Do đó predictability của một physiological signal không chỉ phản ánh regularity nội tại, mà còn phụ thuộc vào:

```text
self-dynamics
+
cross-system interactions
```

Authors diễn giải reduced predictability trong SAHS như:

```text
weaker temporal organization
+
altered neuroautonomic regulation
```

Trong framework này:

```text
predictability ↓
→ unpredictability / "complexity" ↑
```

Nhưng đây là **definition riêng của model-based framework**, không nên transfer trực tiếp thành general complexity claim.

---

## Relevance to current study

Current study:

```text
PPG waveform
→ Simplex Projection
→ CC / NRMSE
→ finite-horizon forecastability
```

Faes:

```text
brain–heart multivariate time series
→ linear prediction
→ self / causal / interaction predictability
```

Hai methods khác nhau, nhưng cùng một principle:

> **Prediction quality phản ánh mức độ temporal organization có thể được khai thác từ past dynamics.**

Do đó current finding:

```text
CC ↓
NRMSE ↑
```

nên được diễn giải an toàn là:

> **reduced finite-horizon forecastability**

chứ không tự động là:

```text
more chaos
hoặc
more complexity
```

---

## Important conceptual insight

Reduced predictability có thể xuất hiện do:

```text
weaker self-dynamics
+
changing external inputs
+
changing interactions among physiological systems
```

Do đó:

```text
forecastability ↓
```

không nhất thiết yêu cầu:

```text
local trajectory divergence ↑
```

Điều này giúp giải thích current pattern:

```text
CC ↓ / NRMSE ↑
nhưng
LLE ↓
```

Hai findings có thể đồng thời đúng vì chúng probe **different dynamical properties**.

---

## Sleep-state transition relevance

Authors nhấn mạnh rằng brain–heart interactions trong sleep được sustain mạnh bởi:

```text
transitions across sleep states
```

và network connectivity yếu hơn khi xét từng stable sleep stage riêng biệt.

Điều này support concept:

> **state transitions có thể chứa richer dynamical reorganization hơn stable states.**

Rất phù hợp với current focus:

```text
Awake → Drowsiness
```

thay vì stable sleep staging.

---

## Temporal-scale limitation

Faes phân tích dynamics ở very slow scale:

```text
EEG power: 60 s windows
HRV: 120 s windows
sampling of derived series ≈ 1 min
dominant dynamics >15 min
```

Current study:

```text
PPG waveform
→ forecast horizons 0.04–4 s
```

Vì vậy paper này chỉ nên dùng ở **conceptual / physiological level**, không phải direct quantitative comparison.

---

## Methodological relevance

Authors thừa nhận limitation của linear prediction và đề xuất future work với:

```text
model-free nonlinear prediction methods
```

Điều này tạo bridge tốt với current use of:

```text
Simplex Projection
```

nhưng không phải direct validation cho Simplex.

---

## Role in Discussion

### Prediction interpretation

Strong reference cho idea:

> predictability phản ánh exploitable temporal structure của physiological dynamics.

### Physiological relevance

Support rằng cardiovascular predictability có thể thay đổi khi:

```text
autonomic regulation
+
brain–heart interactions
```

bị reorganization.

### Integrated mechanistic story

Kết hợp với sleep-onset literature:

```text
wake–sleep transition
→ regulatory configuration changes
→ cross-system interactions change
→ temporal organization / predictability may change
```

### CC↓ + LLE↓ tension

Giúp support rằng:

```text
forecastability
≠
local divergence
```

nên hai metrics không cần thay đổi cùng chiều.

### Claim boundary

Không nên suy:

```text
CC ↓ = complexity ↑
CC ↓ = pathological dysregulation
Drowsiness behaves like sleep apnea
Faes directly validates Simplex Projection
```

---

## Main takeaway

> **Faes et al. cho thấy predictability của cardiovascular dynamics phản ánh cả temporal structure nội tại lẫn interactions với các physiological systems khác. Reduced predictability vì vậy nên được hiểu là altered dynamical organization under a prediction framework, không phải trực tiếp là greater chaos. Paper đặc biệt hữu ích để contextualize `CC↓ / NRMSE↑` và để giải thích vì sao reduced forecastability vẫn có thể đồng thời tồn tại với `LLE↓`.**

---

**Nguồn: [Hu_2009.md](Hu_2009.md)**

# Paper 16 — Hu, Gao & Tung (2009)
## Characterizing heart rate variability by scale-dependent Lyapunov exponent

## Phương pháp

- Phân tích HRV của 3 nhóm:
  - Healthy
  - Congestive Heart Failure (CHF)
  - Atrial Fibrillation (AF)
- Sử dụng **Scale-Dependent Lyapunov Exponent (SDLE)** thay vì một single global LLE.
- SDLE đánh giá divergence của nearby trajectories theo từng **scale** trong reconstructed phase space.
- Mục tiêu:
  - phân biệt deterministic chaos
  - noisy chaos
  - stochastic dynamics
  - `1/f`-type processes

---

## Ý tưởng chính

Lyapunov behavior của physiological signals có thể phụ thuộc mạnh vào scale.

Do đó:

```text
single LLE
≠
full description of cardiovascular dynamics
```

và:

```text
positive / larger Lyapunov behavior
≠
proof of deterministic chaos
```

---

## Main findings

Authors không quan sát được clear chaotic scaling trên một significant scale range ở các HRV datasets.

Kết luận:

```text
HRV dynamics
→ mostly stochastic
```

nhưng dạng stochasticity khác nhau giữa các nhóm.

Broad pattern:

```text
Healthy
→ structured multiscale dynamics

CHF
→ more 1/f-like behavior

AF
→ more white-noise-like behavior
```

---

## Physiological interpretation

Authors đề xuất rằng healthy cardiovascular system có thể là một:

> **tightly coupled and coherently functioning system**

trong khi CHF / AF có thể thể hiện:

```text
looser coupling
+
higher effective dimensionality
+
less coherent organization
```

Tuy nhiên đây là high-level interpretation.

Không nên suy trực tiếp:

```text
current LLE ↓
→ tighter physiological coupling
```

---

## Relevance to current study

Current study:

```text
Drowsy → LLE ↓
```

Interpretation an toàn nhất:

> **reduced local trajectory divergence**

không phải:

```text
less chaos
lower complexity
more stable system in every sense
```

Paper này support rất mạnh cho claim boundary này vì Lyapunov behavior có thể phụ thuộc vào:

- scale
- noise
- embedding
- data length
- nonstationarity

---

## Scale dependence

SDLE cho thấy trajectory divergence không nhất thiết có cùng behavior ở mọi scale.

Do đó:

> một scalar LLE chỉ mô tả một phần của dynamical behavior.

Điều này đặc biệt quan trọng khi diễn giải physiological signals vốn chứa:

```text
multiple time scales
+
stochastic components
+
nonlinear structure
```

---

## Noise và nonstationarity

Paper nhấn mạnh HRV thường chứa:

```text
measurement / dynamical noise
sudden jumps / outliers
oscillatory components
nonstationarity
```

Noise có thể làm thay đổi hoặc thu hẹp vùng scale mà Lyapunov-type behavior được quan sát.

→ LLE estimation cần được diễn giải trong context của preprocessing và signal quality.

---

## Data length và embedding

Authors chỉ ra:

```text
data length ↓
→ scaling estimation kém ổn định hơn

embedding dimension ↑ với finite data
→ reliable scale range ↓
```

Điều này rất relevant với current ultra-short analysis.

Nó support tầm quan trọng của:

```text
30 / 60 / 120 / 180 s robustness
fixed embedding parameters
fit-quality control
parameter verification
```

---

## Relation to RQ1

Paper cho thấy HRV có thể đồng thời chứa:

```text
stochastic
fractal
nonlinear
scale-dependent dynamics
```

Do đó không nên dùng một metric duy nhất để kết luận chaos.

Điều này support mạnh current framework:

```text
PPS surrogate testing
→ test against a specific pseudoperiodic null
```

thay vì:

```text
positive LLE
→ chaos
```

---

## Relation to current multidimensional findings

Current study:

```text
CC ↓
DET ↓
LLE ↓
LAM / TT ↑ tendency
```

Hu et al. support rằng các dynamical metrics không nên bị ép lên một single axis:

```text
more complexity
vs
less complexity
```

Mỗi metric phản ánh một khía cạnh khác nhau của system dynamics.

---

## Relation to Yeragani

```text
Yeragani 2004
→ LLE nhạy với physiological state
→ sleep / posture / autonomic context

Hu 2009
→ Lyapunov interpretation is scale-dependent
→ HRV may be predominantly stochastic
→ strong caution against chaos claims
```

Hai paper bổ sung nhau rất tốt:

- Yeragani → physiological sensitivity
- Hu → theoretical / methodological boundary

---

## Role in Discussion

### LLE interpretation

Strong reference cho:

> **LLE nên được hiểu là trajectory-divergence measure, không phải direct chaos index.**

### Chaos claim boundary

Support rất mạnh:

```text
LLE ↓
≠ less chaos

LLE ↑
≠ more chaos
```

### RQ1

Củng cố việc dùng **surrogate testing với explicit null hypothesis** thay vì kết luận chaos từ một nonlinear metric.

### Methodological robustness

Support cho việc cần kiểm tra:

- data length
- embedding dependence
- noise sensitivity
- nonstationarity

### Complexity interpretation

Strong support cho việc không diễn giải toàn bộ current findings bằng một single “complexity ↑ / ↓” narrative.

---

## Claim boundary

Không nên dùng paper này để claim:

```text
HRV luôn stochastic
PPG dynamics = HRV dynamics
current LLE ↓ proves stochasticity
current LLE ↓ means tighter cardiovascular coupling
```

Paper chỉ phân tích HRV trong specific datasets và bằng SDLE.

---

## Main takeaway

> **Hu et al. cho thấy Lyapunov behavior trong cardiovascular time series có thể phụ thuộc mạnh vào scale, noise, embedding và data length, đồng thời HRV không nên mặc định được xem là low-dimensional chaotic. Vì vậy current `LLE↓` nên được diễn giải như reduced local trajectory divergence, không phải bằng chứng trực tiếp của less chaos hay lower complexity.**

---

**Nguồn: [Carrington_2003.md](Carrington_2003.md)**

# Paper 17 — Carrington et al. (2003)
## Ảnh hưởng của sleep onset lên biến thiên ngày–đêm của hoạt động tim mạch và autonomic control

## Phương pháp

- Healthy young adults.
- So sánh 2 điều kiện:
  - **NSO**: ngủ vào thời điểm bình thường.
  - **DSO**: trì hoãn sleep onset thêm 3 giờ.
- Mục tiêu: tách ảnh hưởng của:
  - **sleep onset**
  - khỏi **circadian timing**
- Các chỉ số:
  - HR
  - systolic / diastolic BP
  - HF-HRV
  - LF/HF
  - PEP (pre-ejection period)
- Phân tích theo các đoạn **2 phút**, sau đó tổng hợp theo 30-min bins.

---

## Ý tưởng chính

Thiết kế nghiên cứu dựa trên logic:

```text
thay đổi đi cùng sleep onset
dù ngủ đúng giờ hay trễ 3 h
→ sleep-related effect

thay đổi xảy ra ở cùng circadian time
dù subject còn thức hay đã ngủ
→ circadian-related effect
```

→ cho phép phân biệt sleep effect khỏi time-of-day effect.

---

## Main findings

### Heart rate

```text
HR ↓ dần theo thời gian
```

→ chịu ảnh hưởng của cả:
- circadian system
- sleep onset

Trong đó circadian influence có vẻ mạnh hơn.

### Blood pressure

```text
BP ↓ khá abrupt tại sleep onset
```

→ chủ yếu là **sleep-onset-related effect**, ít phụ thuộc circadian timing.

### HF-HRV và LF/HF

```text
HF ↑
LF/HF ↓
```

quanh sleep onset.

Authors diễn giải là:

```text
greater vagal contribution
 / shift toward vagal dominance
```

### PEP

```text
PEP thay đổi chủ yếu theo time/circadian influence
```

→ không cho clear sleep-onset effect.

---

## Physiological interpretation

Sleep onset không tạo một **single autonomic switch** giống nhau cho mọi cardiovascular variable.

Thay vào đó:

```text
HR
BP
vagal-related HRV
sympathetic-related cardiac control
```

có thể chịu các mức ảnh hưởng khác nhau từ:

```text
sleep mechanisms
+
circadian mechanisms
```

Điều này support cách nhìn:

> **Sleep onset là một multidimensional cardiovascular/autonomic reorganization.**

Không nên đơn giản hóa thành:

```text
sympathetic ↓
+
parasympathetic ↑
```

cho toàn bộ hệ thống.

---

## Điểm quan trọng về circadian confound

Paper cho thấy một phần đáng kể của cardiovascular transition quanh sleep onset:

```text
không thể giải thích chỉ bằng time-of-day / circadian phase
```

Đặc biệt:
- BP fall có strong sleep-onset component.
- HF/LF-HF changes cũng có strong sleep-related contribution.
- HR lại chịu cả sleep và circadian influences.

→ rất hữu ích để support rằng:

> physiological changes quanh sleep onset có **sleep-specific contribution**, không chỉ là diurnal drift.

---

## Caveat về lights off

Authors thừa nhận chưa thể loại bỏ hoàn toàn ảnh hưởng của:

```text
lights off / reduced illumination
```

đối với một số cardiovascular changes.

Do đó không nên claim:

```text
sleep itself alone
→ causes all observed changes
```

---

## Relevance to current study

Current study quan sát:

```text
Awake → Drowsy
```

với nhiều NTSA findings thay đổi theo các hướng khác nhau.

Carrington support mạnh rằng physiological transition quanh sleep onset vốn đã là:

```text
multicomponent
+
multi-mechanism
+
non-uniform
```

Do đó current pattern:

```text
CC ↓
NRMSE ↑
DET ↓
LLE ↓
LAM / TT ↑ tendency
0V ↑
2V ↓
```

không cần phải collapse thành một single:

```text
complexity ↑ / ↓
hoặc
sympathetic ↑ / ↓
```

narrative.

---

## Liên hệ với Symbolic Analysis

Carrington quan sát:

```text
HF ↑
LF/HF ↓
```

→ compatible với greater vagal contribution quanh sleep onset.

Trong khi current symbolic findings:

```text
0V ↑
2V ↓
```

theo Porta/Guzzetti có thể tương thích với relatively greater sympathetic modulation và/hoặc reduced vagal modulation.

Hai pattern không nhất thiết mâu thuẫn trực tiếp vì paper này cho thấy:

```text
different autonomic/cardiovascular components
→ có different timing và different regulatory drivers
```

Do đó symbolic result có thể phản ánh một aspect/timescale khác của transitional regime.

---

## Liên hệ với sleep-onset corpus

```text
Carrington 2003
→ tách sleep-onset effects khỏi circadian effects

Carrington 2005
→ repeated arousals làm gián đoạn cardiovascular settling

Shinar 2006
→ wake–sleep transition là unstable process

Tsai 2019
→ cardiac de-arousal có thể precede cortical N1
```

Bốn paper cùng support:

> **Wake-to-sleep transition là một asynchronous, multi-phase và dynamically unstable physiological reorganization, không được giải thích hoàn toàn bởi circadian timing.**

---

## Methodological relevance

Paper chỉ lấy các đoạn tương đối **stable** để tính HRV:

```text
2-min epochs
không movement
không arousal
không stage transition
```

và loại:

```text
wake-after-lights-out
stage 1
```

khỏi HRV analysis vì các đoạn này transitory / dễ nhiễu.

Điều này tạo contrast quan trọng với current study:

```text
Carrington
→ tránh unstable transition để estimate conventional HRV

Current study
→ unstable transition chính là scientific target
```

→ nhấn mạnh giá trị của short-window NTSA trong việc phân tích transitional physiology.

---

## Role in Discussion

### Physiological foundation

Strong support cho:

> **sleep onset gây ra cardiovascular/autonomic changes vượt ra ngoài circadian timing.**

### Multidimensional interpretation

Support việc không diễn giải toàn bộ findings bằng một single sympathovagal hoặc complexity axis.

### Circadian confound

Rất hữu ích để phản biện claim:

```text
Awake–Drowsy differences
= chỉ do time-of-day drift
```

### Symbolic interpretation

Giúp contextualize sự khác biệt giữa symbolic RR results và conventional HRV literature.

### Methodological rationale

Cho thấy conventional HRV thường tránh transitional epochs, trong khi current study cố tình nghiên cứu chính transitional regime đó.

### Claim boundary

Không nên suy:

```text
sleep onset effects hoàn toàn độc lập với light exposure
HF = direct vagal neural measurement
LF/HF = precise sympathovagal balance
current Drowsiness = established sleep onset
```

---

## Main takeaway

> **Carrington et al. cho thấy các cardiovascular changes quanh sleep onset không chỉ phản ánh circadian timing mà còn có sleep-related effects riêng, đồng thời các biến HR, BP, HF-HRV, LF/HF và PEP chịu những regulatory influences khác nhau. Paper này củng cố mạnh cách diễn giải Awake–Drowsy như một multidimensional physiological reorganization, thay vì một simple monotonic autonomic shift.**
