# Tổng hợp tham số đã freeze cho các phương pháp NTSA

**Phạm vi của bản freeze:** primary **processed PPG, cửa sổ 60 s**, 20 sessions, dùng đúng các window có `analysis_included=True` cùng SQI và processed-stationarity mask hiện tại. Tổng cohort đầu vào là **901 windows**. Các cấu hình raw PPG và cửa sổ 120/180 s trong notebook cũ không thuộc bản freeze primary được tổng hợp ở đây.

**Thứ tự ưu tiên khi đối chiếu:** notebook verification cuối cùng → notebook production → estimator core trong `src`. Các giá trị sensitivity chỉ là perturbation để kiểm tra robustness, không thay thế nominal setting.

## 1. Cấu hình chung

| Thành phần | Giá trị đã freeze |
|---|---|
| Signal representation | Processed PPG |
| Window | 60 s |
| Cohort | 901 primary windows, 20 sessions |
| Eligibility | `analysis_included=True`; giữ nguyên SQI và processed-stationarity mask |
| State labels | Awake = 0; Drowsy = 1 |
| Embedding dimension | `m = 8` |
| Embedding delay | `τ = 0.16 s` |
| Chuyển `τ` sang samples | `round(τ × fs)`: 4 samples tại 25 Hz, 8 samples tại 50 Hz |
| Distance trong reconstructed space | Euclidean |
| Nguyên tắc lựa chọn | Không tối ưu hoặc chọn lại tham số theo p-value/effect Awake–Drowsy |

## 2. Nonlinear prediction — Simplex Projection

### Tham số estimator đã freeze

| Tham số | Giá trị / quy tắc freeze |
|---|---|
| Input scaling | Z-score riêng trong từng window: `(x − mean(x)) / std(x)`, dùng `numpy.std` (`ddof=0`) |
| Embedding | `m=8`, `τ=0.16 s` |
| Số nearest neighbours | `k = m + 1 = 9` |
| Distance | Euclidean |
| Prediction mode | Leave-one-out state-space prediction |
| Temporal exclusion | Chỉ nhận neighbour khi `|t_neighbor − t_query| > W` |
| Theiler window | `W = 1.0 s` |
| Theiler theo sampling rate | 25 samples tại 25 Hz; 50 samples tại 50 Hz |
| Weighting | Normalized exponential weighting: `w_i ∝ exp(−d_i/d_1)`; nếu có exact-distance ties tại 0 thì chia đều trọng số cho các exact matches |
| Prediction horizons | 18 horizons: `0.04, 0.08, 0.12, 0.16, 0.20, 0.28, 0.40, 0.60, 0.80, 1.00, 1.20, 1.60, 2.00, 2.40, 2.80, 3.20, 3.60, 4.00 s` |
| Horizon conversion | `round(h × fs)` bằng `numpy.rint`; tại 25 Hz: `1,2,3,4,5,7,10,15,20,25,30,40,50,60,70,80,90,100` samples; tại 50 Hz các giá trị này nhân đôi |
| Maximum prediction horizon | `Hmax = 4.0 s` |
| Window-level metrics | Pearson `CC`, `RMSE`, `NRMSE`; do signal đã z-score nên `NRMSE = RMSE / 1.0` |
| Canonical aggregation | Mean qua 18 horizons trong mỗi window → median các valid windows trong `session × state` → paired `Δ = Drowsy − Awake` |

### Bằng chứng dùng để freeze

- Theiler sensitivity đã kiểm tra `W = {0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0} s`.
- Transition chính nằm quanh `0.6–0.8 s`; `W=1.0 s` nằm trong vùng ổn định sau transition và giữ prediction support đầy đủ.
- Nominal audit dùng 901 windows × 18 horizons = **16,218 window–horizon outputs**. CC/NRMSE tái lập chính xác, max absolute difference bằng 0 khi dùng cùng dữ liệu, cấu hình và aggregation.
- Sai khác Simplex trước đây được xác định do thứ tự aggregation, không phải estimator.

**Trạng thái:** `Simplex Projection verification status: COMPLETE`.

## 3. Recurrence Quantification Analysis — RQA

### Tham số estimator đã freeze

| Tham số | Giá trị / quy tắc freeze |
|---|---|
| Embedding | `m=8`, `τ=0.16 s` |
| Distance matrix | Pairwise Euclidean distance |
| Threshold strategy | Fixed recurrence rate; chọn `epsilon` riêng cho từng window bằng tie-safe thresholding |
| Target recurrence rate | `RR = 0.02` |
| RR tolerance | `5 × 10⁻⁵` |
| Nominal Theiler corridor | `W = (m − 1) × tau_samples` |
| Theiler theo sampling rate | 28 samples tại 25 Hz và 56 samples tại 50 Hz, tương đương khoảng 1.12 s |
| Exclusion rule | Loại line of identity và mọi pair có `|i−j| ≤ W` trước khi tính metric |
| Minimum diagonal line | `l_min = 2` |
| Minimum vertical line | `v_min = 2` |
| Diagonal metrics | `DET`, `Lmean`, `ENTR`, `Lmax` |
| Vertical metrics | `LAM`, `TT`, `Vmax` |
| Verification headline | `DET`; secondary: `LAM`, `TT` |
| Canonical aggregation | Metric của từng window → median các valid windows trong `session × state` → paired `Δ = Drowsy − Awake` |

`epsilon` không phải một hằng số freeze: nó được recompute trong từng window để đạt target RR trên admissible region sau Theiler exclusion. Current tie-safe implementation trong `src/rqa/rqa.py` là reference chính thức.

### Bằng chứng dùng để freeze

- RR sensitivity: `RR = 0.01, 0.02, 0.03`; nominal vẫn là `0.02`.
- Theiler sensitivity: `0.75×, 1.00×, 1.25×` nominal corridor; nominal vẫn là `1.00×`.
- Cả sáu setting giữ đủ 901 valid windows và 20 paired sessions.
- `DET` robust với cả RR và Theiler; `LAM` robust; `TT` robust với Theiler và moderately sensitive về magnitude theo RR nhưng không đổi direction.
- Hai nhánh nominal RR và Theiler khớp tuyệt đối trên 901 windows cho `epsilon`, achieved RR, DET, LAM và TT: max absolute difference = 0, mismatch = 0.
- Cache nominal cũ có 55 mismatch chỉ ở `sample_12`, đã truy về linear-quantile tie handling cũ. Cache cũ được giữ cho provenance; không dùng để thay đổi current tie-safe freeze.

**Trạng thái:** `RQA verification status: COMPLETE`.

## 4. Largest Lyapunov Exponent — Rosenstein LLE

### Tham số estimator và QC đã freeze

| Tham số | Giá trị / quy tắc freeze |
|---|---|
| Estimator | Rosenstein largest Lyapunov exponent |
| Embedding | `m=8`, `τ=0.16 s` |
| Neighbour | Một nearest admissible neighbour trong Euclidean space |
| Nominal Theiler rule | Spectral mean period riêng cho từng window |
| Spectral-period definition | Nghịch đảo spectral centroid của one-sided power spectrum sau khi bỏ DC |
| Theiler conversion | `W_samples = max(round(W_seconds × fs), 1)`; neighbour hợp lệ khi `|j−i| > W_samples` |
| Divergence curve | Mean log Euclidean distance của các neighbour pairs khi cùng tiến theo lag |
| Nominal fit interval | `0.80–1.30 s`, hai đầu được đưa vào fit nếu thỏa support/QC |
| Maximum follow time | `5.0 s` |
| Regression | Linear regression của mean log-distance theo thời gian; LLE là slope, đơn vị `s⁻¹` |
| Minimum initial pairs | `50` |
| Minimum pairs tại mỗi fit lag | `30` |
| Minimum usable fit points | `3` |
| Nominal QC threshold | `R² ≥ 0.90` |
| Valid result | Đủ pair support, đủ fit points, LLE hữu hạn và đạt ngưỡng `R²` |
| Canonical aggregation | LLE của valid window → median trong `session × state` → paired `Δ = Drowsy − Awake` |

Theiler duration và số samples của LLE thay đổi theo phổ của từng window; phần được freeze là **quy tắc spectral-mean-period**, không phải một số giây cố định.

### Bằng chứng dùng để freeze

- Fit-range sensitivity: `0.60–1.10 s`, `0.80–1.30 s` nominal, `1.00–1.50 s`.
- QC sensitivity: `R² ≥ 0.90` nominal và `R² ≥ 0.95`.
- Theiler sensitivity: `0.75×, 1.00×, 1.25×` spectral mean period.
- Direction `ΔLLE < 0` được giữ ở mọi setting và đủ 20 paired sessions. Fit-range và Theiler được đánh giá robust; QC moderately sensitive về retention nhưng không đổi kết luận.
- Nominal QC giữ 872/901 valid windows (96.8%). Pair support quan sát được cao hơn nhiều ngưỡng freeze: minimum initial support 1,471 và minimum fitted-region support 1,366.
- Audit đại diện cho cả nhóm 25 và 50 Hz tái lập chính xác tau samples, Theiler samples, neighbours, divergence curves, fit indices, LLE và R²; max absolute difference = 0, mismatch = 0.

**Trạng thái:** `LLE verification status: COMPLETE`.

## 5. Bảng freeze cô đọng

| Phương pháp | Nominal configuration | Sensitivity đã kiểm tra | Trạng thái |
|---|---|---|---|
| Simplex Projection | `m=8`, `τ=0.16 s`, `k=9`, Euclidean, exponential weighting, leave-one-out, `W=1 s`, 18 horizons `0.04–4.0 s` | Theiler `0–2 s`; downstream embedding sensitivity quanh nominal đã được kiểm tra trong phase-space verification | **COMPLETE** |
| RQA | `m=8`, `τ=0.16 s`, fixed `RR=0.02`, tie-safe per-window epsilon, `W=(m−1)tau_samples`, `l_min=v_min=2` | RR `0.01/0.02/0.03`; Theiler `0.75/1.00/1.25×` | **COMPLETE** |
| Rosenstein LLE | `m=8`, `τ=0.16 s`, spectral-period Theiler, fit `0.80–1.30 s`, follow `5 s`, pairs `50/30`, `R²≥0.90` | Fit interval; `R²≥0.90/0.95`; Theiler `0.75/1.00/1.25×` | **COMPLETE** |

## 6. Nguồn đối chiếu

- [`verification_ntsa_parameter/verification_prediction.ipynb`](verification_ntsa_parameter/verification_prediction.ipynb)
- [`verification_ntsa_parameter/verification_rqa.ipynb`](verification_ntsa_parameter/verification_rqa.ipynb)
- [`verification_ntsa_parameter/verification_lle.ipynb`](verification_ntsa_parameter/verification_lle.ipynb)
- [`verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb`](verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb)
- [`../notebook/simplex_projection.ipynb`](../notebook/simplex_projection.ipynb)
- [`../notebook/rqa.ipynb`](../notebook/rqa.ipynb)
- [`../notebook/lyapunov.ipynb`](../notebook/lyapunov.ipynb)
- [`../src/prediction/simplex_projection.py`](../src/prediction/simplex_projection.py)
- [`../src/rqa/rqa.py`](../src/rqa/rqa.py)
- [`../src/chaos/lyapunov.py`](../src/chaos/lyapunov.py)
