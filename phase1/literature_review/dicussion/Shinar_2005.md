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
