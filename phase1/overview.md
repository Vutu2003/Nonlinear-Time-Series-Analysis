# PPG-Based Drowsiness Detection — Research Questions

## Paper 1 — Core Research Direction

### Overall Aim

Kiểm tra liệu PPG ở trạng thái **tỉnh (awake)** và **buồn ngủ (drowsy)** có biểu hiện **động lực phi tuyến xác định (deterministic nonlinear dynamics)** khác nhau hay không; đồng thời xác định khác biệt nằm ở **dạng sóng PPG thô**, **khoảng giữa các nhịp mạch (PPI)** hay cả hai.

---

## RQ1 — Existence

**Do PPG signals acquired during awake and drowsy states exhibit statistically significant deterministic nonlinear dynamics beyond noisy pseudoperiodicity?**

Phân tích riêng $\text{PPG}_{awake}$ và $\text{PPG}_{drowsy}$ theo chuỗi bằng chứng:

$$
\text{Phase-space reconstruction}
\rightarrow \text{MI/FNN}
\rightarrow \text{Nonlinear prediction}
\rightarrow \lambda_{\max}
\rightarrow \text{PPS surrogate test}
$$

Không kết luận chaos chỉ từ $\lambda_{\max}>0$, mà dựa trên **nhiều bằng chứng hội tụ (converging evidence)**.

---

## RQ2 — State-Dependent Nonlinear Dynamics

**Does the nonlinear dynamical organization of PPG change significantly between awake and drowsy states?**

So sánh giữa hai trạng thái:

$$
\lambda_{\max}^{awake} \text{ vs } \lambda_{\max}^{drowsy},\qquad
E_{\text{pred}}^{awake} \text{ vs } E_{\text{pred}}^{drowsy},\qquad
m^{awake} \text{ vs } m^{drowsy}
$$

và khoảng cách original–surrogate:

$$
\Delta E=E_{\text{surrogate}}-E_{\text{original}}.
$$

Trọng tâm không chỉ là *chaos có tồn tại hay không*, mà là **cấu trúc động lực phi tuyến có phụ thuộc trạng thái tỉnh táo hay không** ($D_{awake}\neq D_{drowsy}$).

---

## RQ3 — Raw PPG vs PPI

**Are state-dependent nonlinear changes primarily expressed in the raw PPG waveform, in pulse-to-pulse interval dynamics, or in both?**

Từ cùng một bản ghi, phân tích hai biểu diễn:

$$
\text{PPG}\rightarrow
\begin{cases}
\text{Filtered raw PPG}\\
\text{PPI}
\end{cases}
$$

| Representation | Awake | Drowsy |
|---|---|---|
| Raw PPG | $D_{PA}$ | $D_{PD}$ |
| PPI | $D_{IA}$ | $D_{ID}$ |

So sánh $D_{PA}-D_{PD}$ với $D_{IA}-D_{ID}$ để xác định nguồn gốc khác biệt:

- Raw PPG thay đổi mạnh nhưng PPI không rõ: khác biệt có thể đến từ **hình thái xung/động lực mạch máu**.
- PPI cũng thay đổi rõ: khác biệt có thể liên quan đến **điều hòa tim theo từng nhịp**.

Qua đó hình thành cầu nối:

$$
\text{ANS modulation}
\rightarrow \text{cardiovascular regulation}
\rightarrow \text{PPG/PPI dynamics}.
$$

---

## Physiological Hypothesis

ANS không phải RQ độc lập trong Paper 1 mà là **lớp diễn giải sinh lý**:

$$
\text{Awake}
\rightarrow \text{Drowsy}
\rightarrow \text{ANS modulation changes}
\rightarrow \text{cardiovascular dynamics changes}
\rightarrow \text{PPG/PPI dynamical signatures}.
$$

Các chỉ số hỗ trợ gồm $HR$, $PPI$, $HRV/PRV$ và những chỉ số liên quan đến điều hòa giao cảm, phó giao cảm/dây thần kinh phế vị. Câu hỏi bổ sung là liệu **các thước đo động lực phi tuyến có cung cấp thông tin vượt ngoài HR/PRV truyền thống hay không**.

---

## Overall Logic

$$
\boxed{
\text{RQ1: Existence}
\rightarrow \text{RQ2: State Dependence}
\rightarrow \text{RQ3: Physiological Localization}
}
$$

---

## Long-Term Research Direction

Paper 1 tạo nền tảng cho:

$$
\text{Dynamical evidence}
\rightarrow \text{Dynamical biomarkers}
\rightarrow \text{Machine learning}
\rightarrow \text{Wearable drowsiness detection}.
$$

Các hướng mở rộng gồm **transition dynamics**, **synchronization/coupling**, **stress recognition** và những trạng thái sinh lý khác liên quan đến ANS.
