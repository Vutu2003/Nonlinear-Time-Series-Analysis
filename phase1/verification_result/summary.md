# Tổng hợp kết quả verification dữ liệu và tham số NTSA

Bản tổng hợp bao quát **8 notebook** trong `verification_data` và `verification_ntsa_parameter`, dựa trên nội dung và output đã lưu. Các notebook, bảng kết quả và hình inline được giữ nguyên; không chạy lại notebook, estimator hoặc kiểm định khi lập tài liệu này. Số liệu trong bảng giữ độ chính xác hiển thị của nguồn; các tổng đếm bổ sung chỉ cộng các hàng output đã lưu.

**Kết quả chính:** dữ liệu đạt kiểm tra cấu trúc; bốn finding **Mean_CC ↓, Mean_NRMSE ↑, DET ↓, LLE ↓** giữ hướng dưới toàn bộ bốn label rules bảo thủ. CC/NRMSE/LLE giữ hướng khi thay đổi delay; **DET nhạy với delay**. Cả bốn metric giữ hướng ở `m=7/8/9`. Simplex, RQA và LLE có bằng chứng tái lập và robustness theo các tham số riêng đã khảo sát, với các giới hạn về CI, magnitude và retention được ghi bên dưới.

## 1. Phạm vi và quy ước đọc kết quả

- Audit dữ liệu: 20 processed-session CSV của `dhdata`, gồm **1.620.038 samples**; kiểm tra cả raw/processed/label/time trong cùng file.
- Cohort NTSA primary: **901 processed PPG windows dài 60 s**, gồm **596 Awake / 305 Drowsy**, thuộc 20 sessions. Chỉ dùng `analysis_included=True` theo SQI và processed-stationarity mask hiện tại.
- Các bộ label sensitivity có cửa sổ 60 s được dựng riêng bằng cùng segmentation/QC core; số lượng window được báo theo từng rule, không coi là phép trừ trực tiếp từ 901 window primary.
- Label mapping: Awake = 0, Drowsy = 1. Paired effect luôn là **Δ = Drowsy − Awake**; hướng kỳ vọng là CC âm, NRMSE dương, DET âm, LLE âm.
- Simplex: mean qua 18 horizons trong mỗi window → median các valid windows trong `session × state` → paired Δ. DET/LLE: median window metric trong `session × state` → paired Δ. LLE áp dụng QC riêng; không dùng QC của LLE để loại window của metric khác.
- Inference: median paired Δ, percentile bootstrap 95% CI với **20.000 paired-session resamples**, two-sided Wilcoxon, matched-pairs rank-biserial `r_rb`, và direction count. CI của median và p của signed-rank được đọc riêng.
- BH-FDR trong label sensitivity: **4 metrics/rule**. Trong embedding sensitivity: **4 metrics/setting**. P0 tham chiếu ở notebook label dùng BH đã lưu trên **7 metrics**; giữ nguyên, không hiệu chỉnh lại. Bảng RQA/LLE method-specific báo p như nguồn, không bổ sung q mới.
- Embedding nominal giữ nguyên **m=8, τ=0.16 s**, không lựa chọn lại theo p-value hoặc độ tách Awake–Drowsy.

**Hai mốc prediction đã lưu cần phân biệt:** notebook label validation tham chiếu P0 `Mean_CC=-0.033871`, `Mean_NRMSE=+0.029424`; notebook phase-space báo nominal `Mean_CC=-0.027705`, `Mean_NRMSE=+0.031855`. DET/LLE tại hai mốc đều là `-0.018645/-0.037570`. Tài liệu giữ các giá trị theo đúng nguồn, không thay thế mốc này bằng mốc kia hoặc tự tính lại để hòa giải chênh lệch.

## 2. Verification dữ liệu và label

### 2.1. Phase A — tính toàn vẹn dữ liệu và cấu trúc label

Nguồn: [verification_data.ipynb](verification_data/verification_data.ipynb).

**20/20 sessions** có `integrity_pass=True` và `analysis_eligible=True`. Không phát hiện cột thiếu/trùng, timestamp trùng, timestamp không hợp lệ, nhãn thiếu/sai mapping hoặc NaN/Inf/non-numeric trong raw và processed. Time tăng nghiêm ngặt; raw, processed, label cùng row axis; không có sample tín hiệu thiếu timestamp/label hay mất tương ứng raw–processed.

Tổng cộng **69 gap >1.5×median_dt**, trong đó **62 gap >2×median_dt**, **0 gap >5×median_dt**. `max_dt` lớn nhất là **0.198929 s**. Gap được tách continuity và giữ trong audit, không nội suy. Sampling rate quan sát nằm trong **24.989380–50.000000 Hz**. Subject identity chưa xác định được để trống trong audit; không suy ra subject từ số session.

Bảng dưới ghép các cột đã lưu của integrity và label summary; mọi session đều PASS.

| Session | Samples | fs (Hz) | Gap >1.5×dt | max_dt (s) | Segments | Transitions | Median segment (s) | Segments <60/<180/<300 s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | 117828 | 50.000000 | 0 | 0.020000 | 8 | 7 | 185.470000 | 0 / 4 / 6 |
| 04 | 75416 | 24.991878 | 3 | 0.144438 | 9 | 5 | 193.750753 | 3 / 4 / 6 |
| 05 | 91211 | 25.002500 | 4 | 0.150461 | 10 | 5 | 227.709890 | 3 / 5 / 5 |
| 06 | 79179 | 24.993127 | 5 | 0.198929 | 11 | 5 | 149.760030 | 5 / 6 / 6 |
| 07 | 79768 | 24.993752 | 3 | 0.147189 | 7 | 3 | 176.710309 | 3 / 4 / 4 |
| 08 | 77595 | 24.993752 | 4 | 0.129112 | 8 | 3 | 220.644494 | 3 / 4 / 5 |
| 09 | 119272 | 25.000625 | 8 | 0.189515 | 12 | 3 | 317.128968 | 5 / 5 / 6 |
| 10 | 60386 | 24.998236 | 3 | 0.153995 | 7 | 3 | 287.720119 | 2 / 3 / 4 |
| 11 | 61582 | 24.993767 | 2 | 0.127770 | 6 | 3 | 572.595002 | 2 / 2 / 2 |
| 12 | 89853 | 24.989380 | 2 | 0.146352 | 12 | 9 | 256.374558 | 5 / 5 / 6 |
| 13 | 76473 | 25.000378 | 2 | 0.155893 | 6 | 3 | 535.468362 | 2 / 2 / 2 |
| 14 | 85948 | 24.993627 | 5 | 0.144833 | 11 | 5 | 199.140020 | 4 / 5 / 6 |
| 15 | 69362 | 24.995626 | 6 | 0.155326 | 14 | 7 | 56.754119 | 7 / 10 / 12 |
| 17 | 68752 | 24.992877 | 2 | 0.158415 | 6 | 3 | 370.945815 | 1 / 1 / 2 |
| 18 | 69937 | 24.997500 | 3 | 0.148673 | 7 | 3 | 376.319836 | 2 / 2 / 2 |
| 19 | 73041 | 24.996219 | 4 | 0.173711 | 8 | 3 | 376.030609 | 3 / 3 / 3 |
| 21 | 69660 | 25.000000 | 2 | 0.138071 | 8 | 5 | 213.146094 | 2 / 4 / 5 |
| 22 | 74710 | 25.000625 | 3 | 0.143200 | 9 | 5 | 282.900491 | 3 / 4 / 5 |
| 23 | 109452 | 24.997500 | 3 | 0.141993 | 7 | 3 | 527.230864 | 2 / 2 / 2 |
| 25 | 70613 | 24.995938 | 5 | 0.191656 | 9 | 3 | 284.040073 | 3 / 3 / 5 |

**Label structure:** 175 contiguous segments gồm **93 Awake / 82 Drowsy**, với **86 transitions** và **0 transition across gap**. Median duration trên 175 segment là **260.039991 s** (khoảng 4.3 phút). Có **60 segment <60 s**, **78 segment <180 s**, **94 segment <300 s**; ba số đếm lồng nhau, không cộng thành tổng segment.

Oscillation audit ghi nhận **57 mẫu đảo trạng thái A→D→A hoặc D→A→D** trong quan sát liên tục; đoạn giữa <60/<180/<300 s tương ứng **7/17/27** mẫu. Đây là cờ mô tả, không phải căn cứ tự động sửa label hoặc loại session.

Đã lưu đầy đủ: integrity summary, processed lineage, label/session summary, 175 segment, 86 transition, oscillation audit, vùng loại ±30/60/90 s, **674 retained intervals** của Primary/T30/T60/S3/S5, và sample-exclusion audit. Các lý do invalid sample đều có số đếm 0. Vùng ±90 s chỉ được audit vị trí; không có bộ NTSA T90 trong phạm vi này.

### 2.2. Retention và feasibility trước SQI/stationarity

T30/T60 loại sample có khoảng cách tới transition **≤30/60 s**, hợp các vùng chồng lấp. S3/S5 giữ segment gốc có duration **≥180/300 s**. Duration tính theo observed sample support; gap không được cộng thành thời lượng quan sát.

Tỷ lệ retention dưới đây là **tỷ lệ samples**, lấy từ Phase A; không phải tỷ lệ window sau QC. `S0` trong bảng segment retention của notebook là mốc không áp ngưỡng segment, tương ứng Primary.

| Rule | Samples giữ lại | Tỷ lệ toàn bộ | Awake giữ lại | Drowsy giữ lại | Segments sau rule | Awake duration (s) | Drowsy duration (s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Primary | 1620038 | 1.000000 | 1.000000 | 1.000000 | 175 | 40902.152527 | 21721.929380 |
| T30 | 1488882 | 0.919041 | 0.939274 | 0.880875 | 164 | 38532.524606 | 19249.549016 |
| T60 | 1364164 | 0.842057 | 0.883860 | 0.763199 | 157 | 36338.759702 | 16809.587575 |
| S3 | 1537360 | 0.948965 | 0.968951 | 0.911265 | 97 | 39850.369620 | 20004.799781 |
| S5 | 1429409 | 0.882331 | 0.915083 | 0.820548 | 81 | 37830.183166 | 18168.720374 |

Khả năng tạo cửa sổ 60 s được **ước tính trước QC** như sau:

| Rule | Awake windows ước tính | Drowsy windows ước tính | Sessions Awake | Sessions Drowsy | Paired sessions |
| --- | --- | --- | --- | --- | --- |
| Primary | 649 | 333 | 20 | 20 | 20 |
| T30 | 615 | 291 | 20 | 20 | 20 |
| T60 | 577 | 254 | 20 | 20 | 20 |
| S3 | 639 | 313 | 20 | 20 | 20 |
| S5 | 609 | 286 | 20 | 19 | 19 |

Phase A đếm bằng `floor(duration_s/60)`; Phase B0 dùng segmentation core với `round(60×fs)` samples/window. Timestamp không đều có thể làm số candidate khác nhau; các số ước tính trên không thay thế candidate hoặc included count của B0.

### 2.3. Audit riêng sessions 09 và 13

Sessions 09/13 được so với phân bố 18 session còn lại trong cùng nguồn, không kiểm định và không loại hậu nghiệm.

| Metric | Session 09 | Session 13 | Median 18 session khác | Q25–Q75 khác |
| --- | --- | --- | --- | --- |
| n_transitions | 3.000000 | 3.000000 | 4.000000 | [3.000000, 5.000000] |
| median_segment_duration_s | 317.128968 | 535.468362 | 242.042224 | [195.098070, 350.139391] |
| min_segment_duration_s | 0.040584 | 0.040473 | 0.040358 | [0.040308, 0.040401] |
| n_segments_lt_180s | 5.000000 | 2.000000 | 4.000000 | [3.000000, 4.750000] |
| n_segments_lt_300s | 6.000000 | 2.000000 | 5.000000 | [3.250000, 6.000000] |
| fraction_samples_within_30s_transition | 0.037704 | 0.058622 | 0.075070 | [0.063615, 0.096669] |
| fraction_samples_within_60s_transition | 0.075416 | 0.117218 | 0.149903 | [0.127220, 0.193390] |

Không có bằng chứng rõ rằng hai session này có label bất thường hơn nhóm còn lại; cả hai vẫn đóng góp paired data trong các rules. Kết luận Phase A: dataset đạt kiểm tra kỹ thuật và có đủ dữ liệu cho sensitivity analysis; KSS chủ quan chưa được xác lập là ground truth khách quan.

### 2.4. Phase B0 — tạo bộ label-sensitive và cửa sổ 60 s

Nguồn: [create_data_label_sensitive.ipynb](verification_data/create_data_label_sensitive.ipynb).

Đã tạo **T30/T60/S3/S5**, mỗi rule có 20 filtered-session CSV, 20 candidate-window tables, retained intervals và summary; P0 không được tạo lại. Notebook ghi output tại `phase1/results/data_label_sensitive`.

SQI dùng processed session gốc, median/MAD theo session, grid **5 s**, calibration **4.5**; sau đó lấy mask theo original row index. Segmentation non-overlapping thực hiện riêng trên từng retained interval. Quasi-stationarity dùng core hiện có với **10 s / 0.5**; final inclusion là `sqi_pass AND processed_stationarity_pass`. Không refilter hoặc relabel.

Bảng stationarity-pass đếm trên **mọi candidate**; included là giao với SQI-pass, nên hai cột có thể khác nhau.

| Rule | Awake candidate | Awake SQI | Awake stationarity | Awake included | Drowsy candidate | Drowsy SQI | Drowsy stationarity | Drowsy included | Paired sessions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T30 | 610 | 609 | 586 | 586 | 290 | 289 | 275 | 274 | 20 |
| T60 | 574 | 573 | 551 | 551 | 254 | 253 | 236 | 236 | 20 |
| S3 | 636 | 635 | 609 | 609 | 313 | 312 | 292 | 291 | 20 |
| S5 | 606 | 605 | 581 | 581 | 286 | 285 | 266 | 265 | 19 |

Included/candidate theo Awake và Drowsy tương ứng: T30 **0.960656/0.944828**; T60 **0.959930/0.929134**; S3 **0.957547/0.929712**; S5 **0.958746/0.926573**.

Boundary checks đã PASS. **80/80 rule × session outputs** được đọc lại và xác nhận exact signal/label preservation, original row-index, interval/gap boundaries, windows không chồng/trùng, QC inclusion logic và input SHA-256 không đổi. Query mẫu `T30_01_00001` truy xuất đúng **3.000 processed samples**.

**Phase B0: COMPLETE.** S5 còn 19 paired sessions; session 15 không có Drowsy window hợp lệ. File của cả 20 sessions vẫn được giữ.

### 2.5. Phase B1 — chạy NTSA theo từng label rule

Nguồn: [ntsa_data_label_sensitive.ipynb](verification_data/ntsa_data_label_sensitive.ipynb).

Đã tính **3.393 sensitivity windows** với cấu hình nominal của Simplex/RQA/LLE, kết quả được notebook ghi tại `phase1/results/ntsa_label_sensitive/<rule>/`. `lle_success` chỉ xác nhận tính được LLE và R² hữu hạn; QC R² được báo riêng.

| Rule | Sessions | Input windows | Simplex success | RQA success | LLE success | LLE R²≥0.90 | LLE R²≥0.95 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T30 | 20 | 860 | 860 | 860 | 860 | 832 | 692 |
| T60 | 20 | 787 | 787 | 787 | 787 | 762 | 646 |
| S3 | 20 | 900 | 900 | 900 | 900 | 871 | 736 |
| S5 | 20 | 846 | 846 | 846 | 846 | 819 | 689 |

Tất cả rules: **0 lỗi Simplex/RQA/LLE**, **0 window thiếu metric**, `identical_signal_reused=0`. Tám kiểm tra/rule đều True: B0 count/identity, metadata, unique window ID, fs/tau conversion, fixed parameters, finite metrics, LLE QC flags và input hashes không đổi. Window đạt tính toán nhưng không qua R² vẫn được lưu với flag, không bị xóa khỏi output.

Các bộ đã hoàn thành là T30/T60/S3/S5. Source hỗ trợ tên thư mục S6 nhưng **không có kết quả S6** và không tự thay bằng S5.

### 2.6. Phase B2 — kết quả thống kê label sensitivity

Nguồn: [label_sensitive_validation.ipynb](verification_data/label_sensitive_validation.ipynb).

Simplex dùng exact two-sided signed-rank với average ranks/sign enumeration theo primary; DET/LLE dùng SciPy Wilcoxon (`zero_method='wilcox'`, không correction, two-sided, `auto`). Bootstrap resample paired-session Δ, không resample window hoặc gộp rules. LLE dùng nominal QC **R²≥0.90**.

**T30/T60/S3 có n=20; S5 có n=19** ở cả bốn metric. Session 15 của S5 không tạo cặp vì thiếu valid Drowsy; sessions 09/13 được giữ. Direction count là số session theo hướng kỳ vọng. LLE có đơn vị s⁻¹.

| Rule | Metric | n | Median Δ | Bootstrap 95% CI | r_rb | Direction count | p | q_BH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T30 | Mean_CC | 20 | -0.0482 | [-0.0689, -0.0152] | -0.695 | 17/20 | 0.0048599 | 0.0097198 |
| T30 | Mean_NRMSE | 20 | +0.0406 | [+0.0190, +0.0570] | +0.724 | 16/20 | 0.0031528 | 0.0097198 |
| T30 | DET | 20 | -0.0183 | [-0.0332, -0.0011] | -0.657 | 14/20 | 0.0083084 | 0.011078 |
| T30 | LLE | 20 | -0.0322 | [-0.0535, +0.0020] | -0.581 | 14/20 | 0.021484 | 0.021484 |
| T60 | Mean_CC | 20 | -0.0251 | [-0.0561, +0.0059] | -0.524 | 13/20 | 0.039989 | 0.039989 |
| T60 | Mean_NRMSE | 20 | +0.0278 | [+0.0027, +0.0479] | +0.619 | 14/20 | 0.013617 | 0.025645 |
| T60 | DET | 20 | -0.0167 | [-0.0294, -0.0066] | -0.590 | 15/20 | 0.019234 | 0.025645 |
| T60 | LLE | 20 | -0.0393 | [-0.0636, -0.0075] | -0.743 | 15/20 | 0.0023251 | 0.0093002 |
| S3 | Mean_CC | 20 | -0.0361 | [-0.0548, -0.0033] | -0.638 | 14/20 | 0.010689 | 0.013617 |
| S3 | Mean_NRMSE | 20 | +0.0357 | [+0.0032, +0.0457] | +0.676 | 15/20 | 0.0063896 | 0.012779 |
| S3 | DET | 20 | -0.0189 | [-0.0326, -0.0069] | -0.619 | 15/20 | 0.013617 | 0.013617 |
| S3 | LLE | 20 | -0.0344 | [-0.0495, -0.0104] | -0.790 | 15/20 | 0.0010166 | 0.0040665 |
| S5 | Mean_CC | 19 | -0.0337 | [-0.0495, -0.0077] | -0.642 | 14/19 | 0.01236 | 0.014069 |
| S5 | Mean_NRMSE | 19 | +0.0367 | [+0.0056, +0.0504] | +0.716 | 16/19 | 0.0045776 | 0.0091553 |
| S5 | DET | 19 | -0.0213 | [-0.0305, -0.0049] | -0.632 | 15/19 | 0.014069 | 0.014069 |
| S5 | LLE | 19 | -0.0321 | [-0.0499, -0.0147] | -0.789 | 14/19 | 0.0014114 | 0.0056458 |

Đối chiếu với P0 đã lưu trong notebook label:

| Metric | P0 Δ | T30 Δ | T60 Δ | S3 Δ | S5 Δ | Cùng hướng P0 |
| --- | --- | --- | --- | --- | --- | --- |
| Mean_CC | -0.0339 | -0.0482 | -0.0251 | -0.0361 | -0.0337 | 4/4 rules |
| Mean_NRMSE | +0.0294 | +0.0406 | +0.0278 | +0.0357 | +0.0367 | 4/4 rules |
| DET | -0.0186 | -0.0183 | -0.0167 | -0.0189 | -0.0213 | 4/4 rules |
| LLE | -0.0376 | -0.0322 | -0.0393 | -0.0344 | -0.0321 | 4/4 rules |

Tỷ lệ độ lớn `|Δ_rule|/|Δ_P0|` đã lưu, chỉ dùng mô tả:

| Metric | T30 | T60 | S3 | S5 |
| --- | --- | --- | --- | --- |
| Mean_CC | 1.424 | 0.741 | 1.066 | 0.996 |
| Mean_NRMSE | 1.380 | 0.946 | 1.212 | 1.246 |
| DET | 0.981 | 0.895 | 1.013 | 1.142 |
| LLE | 0.857 | 1.047 | 0.916 | 0.855 |

- **16/16 median effects** theo hướng kỳ vọng; mỗi metric giữ hướng trong **4/4 rules**.
- **16/16 q_BH<0.05**, BH riêng cho bốn metrics trong từng rule.
- **14/16 bootstrap CI không chứa 0**. Hai CI chứa 0 là T60–Mean_CC `[-0.0561,+0.0059]` và T30–LLE `[-0.0535,+0.0020]`; median direction và signed-rank/BH support vẫn giữ.
- LLE-valid Awake/Drowsy theo rule: T30 **573/259**, T60 **538/224**, S3 **594/277**, S5 **566/253**. Các counts tính trên toàn bộ windows; n paired được xác định riêng sau QC.

**Label Verification Status: COMPLETE. Frozen finding status: ROBUST TO LABEL-SELECTION SENSITIVITY.** Kết quả hỗ trợ việc các finding không bị chi phối chủ yếu bởi vùng gần transition hoặc episode ngắn trong các điều kiện đã thử. So sánh magnitude là mô tả, không phải equivalence test; label uncertainty chưa được loại bỏ hoàn toàn.

## 3. Verification phase-space reconstruction

Nguồn: [verification_phase_space_reconstruction.ipynb](verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb).

**Nominal: m=8, τ=0.16 s** trên 901 primary windows/20 sessions. Grid đã thực hiện là **one-factor-at-a-time**: `τ={0.12,0.16,0.20} s` tại m=8 và `m={7,8,9}` tại τ=0.16 s. Đây là hai grid ba mức có chung nominal, **không phải full Cartesian 3×3 grid m=6/8/10** nêu trong kế hoạch overview.

### 3.1. FNN evidence

FNN tính m=1–10, `R_tol=15`, `A_tol=2`, Theiler=0, threshold=1%; mỗi session đóng góp median FNN tại từng (τ,m). Median/IQR dưới đây tổng hợp giữa sessions. Core chọn dimension theo **≤1%**, nhưng cột session-below dùng **<1%**.

| τ (s) | m | Median FNN (%) | Q25 (%) | Q75 (%) | Sessions | Sessions <1% | Tỷ lệ <1% (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.12 | 1 | 95.991984 | 95.440882 | 96.258593 | 20 | 0 | 0.0 |
| 0.12 | 2 | 27.945114 | 26.497657 | 29.283802 | 20 | 0 | 0.0 |
| 0.12 | 3 | 7.075788 | 6.632479 | 7.251844 | 20 | 0 | 0.0 |
| 0.12 | 4 | 2.234543 | 1.814516 | 2.536962 | 20 | 0 | 0.0 |
| 0.12 | 5 | 1.043771 | 0.841751 | 1.212121 | 20 | 8 | 40.0 |
| 0.12 | 6 | 0.792848 | 0.598853 | 0.919366 | 20 | 18 | 90.0 |
| 0.12 | 7 | 0.659229 | 0.498648 | 0.819811 | 20 | 19 | 95.0 |
| 0.12 | 8 | 0.592818 | 0.499742 | 0.762195 | 20 | 19 | 95.0 |
| 0.12 | 9 | 0.577054 | 0.466735 | 0.797692 | 20 | 19 | 95.0 |
| 0.12 | 10 | 0.646259 | 0.493197 | 0.884354 | 20 | 18 | 90.0 |
| 0.16 | 1 | 96.006016 | 95.454545 | 96.231618 | 20 | 0 | 0.0 |
| 0.16 | 2 | 32.115279 | 30.956769 | 34.098525 | 20 | 0 | 0.0 |
| 0.16 | 3 | 6.502016 | 6.216398 | 6.938844 | 20 | 0 | 0.0 |
| 0.16 | 4 | 2.156334 | 1.869946 | 2.712264 | 20 | 0 | 0.0 |
| 0.16 | 5 | 1.351351 | 1.114865 | 1.486486 | 20 | 4 | 20.0 |
| 0.16 | 6 | 0.999322 | 0.863821 | 1.177168 | 20 | 10 | 50.0 |
| 0.16 | 7 | 0.900136 | 0.679348 | 1.154891 | 20 | 12 | 60.0 |
| 0.16 | 8 | 0.885559 | 0.613079 | 1.132493 | 20 | 11 | 55.0 |
| 0.16 | 9 | 1.007514 | 0.665984 | 1.297814 | 20 | 10 | 50.0 |
| 0.16 | 10 | 1.215753 | 0.659247 | 1.446918 | 20 | 9 | 45.0 |
| 0.20 | 1 | 95.567084 | 95.401338 | 95.953177 | 20 | 0 | 0.0 |
| 0.20 | 2 | 33.406040 | 32.869128 | 34.530201 | 20 | 0 | 0.0 |
| 0.20 | 3 | 7.188552 | 6.767677 | 7.474747 | 20 | 0 | 0.0 |
| 0.20 | 4 | 2.010135 | 1.816803 | 2.238176 | 20 | 0 | 0.0 |
| 0.20 | 5 | 1.186441 | 1.067797 | 1.398305 | 20 | 4 | 20.0 |
| 0.20 | 6 | 1.003401 | 0.884470 | 1.190476 | 20 | 10 | 50.0 |
| 0.20 | 7 | 1.092150 | 0.853371 | 1.313993 | 20 | 7 | 35.0 |
| 0.20 | 8 | 1.284247 | 0.881978 | 1.438356 | 20 | 7 | 35.0 |
| 0.20 | 9 | 1.443299 | 0.962199 | 1.597938 | 20 | 6 | 30.0 |
| 0.20 | 10 | 1.568966 | 1.155172 | 1.862069 | 20 | 3 | 15.0 |

Ở m=8, median FNN lần lượt **0.592818%, 0.885559%, 1.284247%** cho τ=0.12/0.16/0.20 s; số session <1% là **19/20, 11/20, 7/20**. FNN giảm mạnh từ m=1 đến vùng m≈8, nhưng m=9 không cải thiện nhất quán. Bằng chứng hỗ trợ vùng dimension quanh 8, không chứng minh mọi session/delay đều đạt <1%.

### 3.2. Delay sensitivity — m=8 cố định

Mỗi hàng dùng n=20 paired sessions. BH-FDR riêng cho bốn metrics tại từng τ.

| τ (s) | Metric | Median Δ | CI low | CI high | r_rb | Direction count | p | q_BH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.12 | Mean_CC | -0.031745 | -0.052156 | 0.009404 | -0.533333 | 13/20 expected; 7 reverse; 0 zero | 0.036234 | 0.048312 |
| 0.12 | Mean_NRMSE | 0.032103 | -0.004177 | 0.049237 | 0.552381 | 13/20 expected; 7 reverse; 0 zero | 0.029575 | 0.048312 |
| 0.12 | DET | 0.002471 | -0.007779 | 0.007603 | 0.076190 | 7/20 expected; 13 reverse; 0 zero | 0.784126 | 0.784126 |
| 0.12 | LLE | -0.036067 | -0.056745 | 0.004216 | -0.600000 | 14/20 expected; 6 reverse; 0 zero | 0.017181 | 0.048312 |
| 0.16 | Mean_CC | -0.027705 | -0.050898 | 0.006400 | -0.561905 | 13/20 expected; 7 reverse; 0 zero | 0.026642 | 0.026642 |
| 0.16 | Mean_NRMSE | 0.031855 | 0.000193 | 0.051871 | 0.609524 | 14/20 expected; 6 reverse; 0 zero | 0.015312 | 0.026642 |
| 0.16 | DET | -0.018645 | -0.036354 | -0.006899 | -0.580952 | 15/20 expected; 5 reverse; 0 zero | 0.021484 | 0.026642 |
| 0.16 | LLE | -0.037570 | -0.053698 | -0.022976 | -0.809524 | 16/20 expected; 4 reverse; 0 zero | 0.000708 | 0.002831 |
| 0.20 | Mean_CC | -0.031622 | -0.052868 | -0.000760 | -0.609524 | 14/20 expected; 6 reverse; 0 zero | 0.015312 | 0.020416 |
| 0.20 | Mean_NRMSE | 0.029578 | 0.005572 | 0.047555 | 0.685714 | 16/20 expected; 4 reverse; 0 zero | 0.005581 | 0.011162 |
| 0.20 | DET | 0.001493 | -0.009909 | 0.014791 | 0.009524 | 10/20 expected; 10 reverse; 0 zero | 0.985435 | 0.985435 |
| 0.20 | LLE | -0.046442 | -0.057164 | -0.024038 | -0.933333 | 17/20 expected; 3 reverse; 0 zero | 0.000036 | 0.000145 |

**Mean_CC ↓, Mean_NRMSE ↑ và LLE ↓ giữ hướng 3/3 delay. DET chỉ âm ở nominal**; tại τ=0.12/0.20 s, median DET lần lượt **+0.002471/+0.001493**, gần 0, CI chứa 0 và q=0.784126/0.985435. Vì vậy không kết luận DET robust đối với delay. LLE ở τ=0.12 s và CC ở τ=0.12/0.16 s có CI chứa 0 dù hướng median được giữ.

### 3.3. Dimension sensitivity — τ=0.16 s cố định

Simplex giữ rule k=m+1; RQA giữ Theiler=(m−1)×tau_samples. Mỗi hàng dùng n=20 paired sessions.

| m | Metric | Median Δ | CI low | CI high | r_rb | Direction count | p | q_BH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | Mean_CC | -0.030651 | -0.056483 | 0.004545 | -0.561905 | 13/20 expected; 7 reverse; 0 zero | 0.026642 | 0.035522 |
| 7 | Mean_NRMSE | 0.037698 | -0.002297 | 0.056124 | 0.571429 | 13/20 expected; 7 reverse; 0 zero | 0.023951 | 0.035522 |
| 7 | DET | -0.014453 | -0.030305 | -0.004746 | -0.495238 | 15/20 expected; 5 reverse; 0 zero | 0.053169 | 0.053169 |
| 7 | LLE | -0.028541 | -0.054931 | -0.007644 | -0.695238 | 16/20 expected; 4 reverse; 0 zero | 0.004860 | 0.019440 |
| 8 | Mean_CC | -0.027705 | -0.050898 | 0.006400 | -0.561905 | 13/20 expected; 7 reverse; 0 zero | 0.026642 | 0.026642 |
| 8 | Mean_NRMSE | 0.031855 | 0.000193 | 0.051871 | 0.609524 | 14/20 expected; 6 reverse; 0 zero | 0.015312 | 0.026642 |
| 8 | DET | -0.018645 | -0.036354 | -0.006899 | -0.580952 | 15/20 expected; 5 reverse; 0 zero | 0.021484 | 0.026642 |
| 8 | LLE | -0.037570 | -0.053698 | -0.022976 | -0.809524 | 16/20 expected; 4 reverse; 0 zero | 0.000708 | 0.002831 |
| 9 | Mean_CC | -0.025116 | -0.049245 | 0.005481 | -0.552381 | 13/20 expected; 7 reverse; 0 zero | 0.029575 | 0.039434 |
| 9 | Mean_NRMSE | 0.031458 | 0.004333 | 0.048332 | 0.657143 | 15/20 expected; 5 reverse; 0 zero | 0.008308 | 0.016617 |
| 9 | DET | -0.020042 | -0.032125 | -0.005192 | -0.485714 | 15/20 expected; 5 reverse; 0 zero | 0.058258 | 0.058258 |
| 9 | LLE | -0.024706 | -0.053414 | -0.010202 | -0.819048 | 16/20 expected; 4 reverse; 0 zero | 0.000586 | 0.002342 |

Bảng magnitude và hỗ trợ thống kê đã lưu:

| Metric | Effect span | Max relative change so nominal | CI loại 0 /3 | q<0.05 /3 |
| --- | --- | --- | --- | --- |
| Mean_CC | 0.005535 | 0.106325 | 0 | 3 |
| Mean_NRMSE | 0.006240 | 0.183410 | 2 | 3 |
| DET | 0.005589 | 0.224847 | 3 | 1 |
| LLE | 0.012864 | 0.342400 | 3 | 3 |

Cả bốn metrics giữ hướng **3/3 dimensions**. Mean_CC có CI chứa 0 ở cả ba m; DET q≈0.053169/0.026642/0.058258, nên mức hỗ trợ sau BH thay đổi dù median direction giữ. Magnitude LLE lệch tối đa **34.24%** so nominal; không mô tả kết quả là bất biến với dimension.

### 3.4. Nominal reproducibility và kết luận embedding

Audit khớp **901 valid windows trên 951 ứng viên**, cùng analysis mask và signal hashes; **16.218 horizon rows** và per-window Simplex outputs khớp chính xác. Max absolute difference của Mean_CC/Mean_NRMSE/DET/LLE đều **0**. Cùng 20 paired sessions; nominal paired results, CI và BH q tái lập khi dùng cùng aggregation.

Sai khác Simplex trước đây được xác định do thứ tự aggregation: median tại từng horizon rồi mean khác với mean horizons trong window rồi median windows. Aggregation chuẩn trong báo cáo là cách thứ hai.

**Final embedding status: robustness có điều kiện.** Giữ nominal đã chốt; báo rõ DET nhạy theo τ, statistical support của DET theo m và biến thiên magnitude LLE. Không dùng q<0.05 làm tiêu chí duy nhất.

## 4. Verification Simplex Projection

Nguồn: [verification_prediction.ipynb](verification_ntsa_parameter/verification_prediction.ipynb).

Notebook này gồm **hai markdown cells**, tổng hợp completed cached/results outputs; không có code/output cells riêng cho sensitivity. Các con số dưới đây là bằng chứng được notebook ghi nhận, không phải một lần chạy mới trong tài liệu này.

Cấu hình: m=8, τ=0.16 s, k=m+1=9, Euclidean, normalized exponential weighting, leave-one-out với temporal exclusion, nominal **W=1.0 s**, 18 prediction horizons **0.04–4.0 s**.

| Nội dung verification | Kết quả đã ghi nhận |
|---|---|
| Theiler grid | W={0,0.2,0.4,0.6,0.8,1.0,1.5,2.0} s |
| Dominant transition | Khoảng 0.6→0.8 s |
| Nominal W=1.0 s | Nằm trong vùng ổn định kéo dài sau transition |
| Median adjacent change 0.8→1.0 s | CC=0.003605; NRMSE=0.003260 |
| Prediction support | Complete; minimum valid prediction fraction=1.000 |
| Cohort audit | 901 windows ×18 horizons=16.218 outputs |
| Per-window CC/NRMSE reproduction | Exact; max absolute difference=0 |
| Sai khác trước đây | Aggregation order, không phải estimator |

W=1.0 s được chọn từ curve stability và prediction support; các tham số không được tối ưu theo Awake–Drowsy separation, p-value hoặc effect size. Các lựa chọn k=m+1, Euclidean, exponential weights và leave-one-out là cấu hình phương pháp giữ nguyên.

**Simplex Projection verification status: COMPLETE.** Bằng chứng embedding sensitivity liên quan được báo tại mục 3; notebook prediction không chứa bảng inference riêng cho từng horizon để tổng hợp thêm.

## 5. Verification RQA

Nguồn: [verification_rqa.ipynb](verification_ntsa_parameter/verification_rqa.ipynb).

Phạm vi: 901 processed windows 60 s, 20 paired sessions, giữ analysis mask. Cố định m=8, τ=0.16 s, Euclidean, `l_min=v_min=2`, tie-safe thresholding. Nominal **RR=0.02** và **W=(m−1)×tau_samples**: 28 samples ở nhóm 25 Hz, 56 ở 50 Hz (khoảng 1.12 s).

Hai thí nghiệm one-factor-at-a-time: **RR=0.01/0.02/0.03** và **W=0.75/1.00/1.25× nominal**. Mỗi thí nghiệm lưu 2.703 rows; cả sáu batches giữ 901 valid windows và 20 paired sessions.

### 5.1. Paired inference đầy đủ

DET là headline; LAM và TT là secondary. Direction trong bảng báo số âm/dương/0; đơn vị TT theo core là samples/line points.

| Sensitivity | Setting | Metric | Median Δ | Bootstrap 95% CI | r_rb | Direction | p | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RR | RR=0.01 | DET | -0.015214 | [-0.033764, 0.002064] | -0.4476 | 14/20 negative; 6 positive; 0 zero | 0.082550 | ROBUST |
| RR | RR=0.01 | LAM | 0.014242 | [-0.005819, 0.057725] | 0.3905 | 7/20 negative; 13 positive; 0 zero | 0.132727 | ROBUST |
| RR | RR=0.01 | TT | 0.000343 | [-0.000043, 0.004808] | 0.3529 | 6/20 negative; 10 positive; 4 zero | 0.214602 | MODERATELY SENSITIVE |
| RR | RR=0.02 | DET | -0.018645 | [-0.036354, -0.006899] | -0.5810 | 15/20 negative; 5 positive; 0 zero | 0.021484 | ROBUST |
| RR | RR=0.02 | LAM | 0.016509 | [-0.004361, 0.063484] | 0.3810 | 7/20 negative; 13 positive; 0 zero | 0.142906 | ROBUST |
| RR | RR=0.02 | TT | 0.009515 | [-0.003444, 0.015962] | 0.3333 | 6/20 negative; 14 positive; 0 zero | 0.202450 | MODERATELY SENSITIVE |
| RR | RR=0.03 | DET | -0.017813 | [-0.033859, -0.007863] | -0.5810 | 15/20 negative; 5 positive; 0 zero | 0.021484 | ROBUST |
| RR | RR=0.03 | LAM | 0.020281 | [-0.005463, 0.051395] | 0.4476 | 7/20 negative; 13 positive; 0 zero | 0.082550 | ROBUST |
| RR | RR=0.03 | TT | 0.022063 | [-0.007639, 0.033264] | 0.2762 | 6/20 negative; 14 positive; 0 zero | 0.294252 | MODERATELY SENSITIVE |
| Theiler | W=0.75× | DET | -0.019191 | [-0.036836, -0.006809] | -0.5810 | 15/20 negative; 5 positive; 0 zero | 0.021484 | ROBUST |
| Theiler | W=0.75× | LAM | 0.019785 | [-0.003072, 0.062855] | 0.4000 | 7/20 negative; 13 positive; 0 zero | 0.123093 | ROBUST |
| Theiler | W=0.75× | TT | 0.009809 | [-0.003114, 0.015962] | 0.3429 | 6/20 negative; 14 positive; 0 zero | 0.189348 | ROBUST |
| Theiler | W=1.00× | DET | -0.018645 | [-0.036354, -0.006899] | -0.5810 | 15/20 negative; 5 positive; 0 zero | 0.021484 | ROBUST |
| Theiler | W=1.00× | LAM | 0.016509 | [-0.004361, 0.063484] | 0.3810 | 7/20 negative; 13 positive; 0 zero | 0.142906 | ROBUST |
| Theiler | W=1.00× | TT | 0.009515 | [-0.003444, 0.015962] | 0.3333 | 6/20 negative; 14 positive; 0 zero | 0.202450 | ROBUST |
| Theiler | W=1.25× | DET | -0.019033 | [-0.037873, -0.007730] | -0.6000 | 15/20 negative; 5 positive; 0 zero | 0.017181 | ROBUST |
| Theiler | W=1.25× | LAM | 0.019372 | [-0.005161, 0.062616] | 0.3905 | 8/20 negative; 12 positive; 0 zero | 0.132727 | ROBUST |
| Theiler | W=1.25× | TT | 0.009844 | [-0.002347, 0.017601] | 0.3524 | 6/20 negative; 14 positive; 0 zero | 0.176853 | ROBUST |

**DET robust với RR và Theiler**: median Δ giữ âm ở cả sáu settings. RR=0.01 có CI chứa 0 và p=0.082550; RR=0.02/0.03 có CI dưới 0. Theiler settings đều giữ 15/20 session có ΔDET âm, CI dưới 0 và p≈0.017181–0.021484.

**LAM giữ hướng dương** ở cả hai thí nghiệm, nhưng tất cả CI chứa 0 và p>0.05; assessment ROBUST phản ánh độ bền direction/magnitude, không xác nhận khác biệt có ý nghĩa thống kê. **TT giữ hướng dương**, robust với Theiler nhưng **MODERATELY SENSITIVE** về magnitude theo RR (`+0.000343` đến `+0.022063`); tất cả CI TT chứa 0.

### 5.2. Window QC, epsilon và achieved RR

Epsilon được chọn riêng mỗi window sau Theiler exclusion; không freeze một epsilon chung. RR tolerance giữ **5×10⁻⁵**. Bảng dưới giữ precision hiển thị của window-summary output.

| Factor | Setting | Max RR error | Median epsilon | Q25 epsilon | Q75 epsilon | Min epsilon | Max epsilon |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RR | 0.01 | 4.400000e-07 | 424.180104 | 337.054218 | 501.436007 | 39.564400 | 1114.965281 |
| RR | 0.02 | 1.100000e-07 | 526.382588 | 425.174793 | 619.009515 | 48.140057 | 1336.246326 |
| RR | 0.03 | 3.600000e-07 | 604.984222 | 494.092016 | 710.111793 | 54.658203 | 1498.780248 |
| Theiler | 0.75 | 4.800000e-07 | 526.655097 | 424.822335 | 618.117227 | 48.275175 | 1337.283133 |
| Theiler | 1.00 | 1.100000e-07 | 526.382588 | 425.174793 | 619.009515 | 48.140057 | 1336.246326 |
| Theiler | 1.25 | 3.900000e-07 | 527.218230 | 425.024942 | 621.600881 | 48.305091 | 1342.578164 |

Theiler samples/seconds theo nhóm fs (870 windows ở nhóm 25 Hz; 31 ở 50 Hz):

| Multiplier | fs group (Hz) | Windows | W samples | Median W (s) | Q25 W (s) | Q75 W (s) |
| --- | --- | --- | --- | --- | --- | --- |
| 0.75 | 25 | 870 | 21 | 0.840137 | 0.84 | 0.840214 |
| 0.75 | 50 | 31 | 42 | 0.840000 | 0.84 | 0.840000 |
| 1.00 | 25 | 870 | 28 | 1.120182 | 1.12 | 1.120286 |
| 1.00 | 50 | 31 | 56 | 1.120000 | 1.12 | 1.120000 |
| 1.25 | 25 | 870 | 35 | 1.400228 | 1.40 | 1.400357 |
| 1.25 | 50 | 31 | 70 | 1.400000 | 1.40 | 1.400000 |

### 5.3. Reproducibility và cache provenance

Audit 7 đại diện bao phủ 25/50 Hz và session có tie: wrapper khớp public core **max difference=0**, admissible-mask mismatch=0, tau/W mismatch=0. Audit mẫu có một window không khớp cache cũ; dùng linear-quantile threshold cũ tái tạo cache chính xác.

Hai nhánh nominal RR=0.02 và Theiler=1.00× khớp trên toàn bộ 901 windows cho epsilon, achieved RR, DET, LAM, TT: **max absolute difference=0; mismatch=0**. So với legacy nominal cache:

| Quantity | Max absolute difference so legacy cache | Mismatch >1e-12 |
| --- | --- | --- |
| epsilon | 4.923334e-02 | 55 |
| achieved_rr | 9.611660e-07 | 55 |
| DET | 6.939362e-05 | 55 |
| LAM | 8.888236e-05 | 55 |
| TT | 3.870879e-05 | 17 |

**55 mismatch windows, chỉ ở sample_12**; TT có 17 mismatch theo quantity. Nguyên nhân là former linear-quantile epsilon tại tie boundary, không phải dữ liệu/embedding/metric khác. Legacy cache giữ cho provenance; current tie-safe public core là verification reference.

**RQA verification status: COMPLETE.** Giữ RR=0.02 và nominal Theiler rule. Kết luận method-specific này không loại bỏ sensitivity của DET với embedding delay đã ghi ở mục 3.

## 6. Verification Rosenstein LLE

Nguồn: [verification_lle.ipynb](verification_ntsa_parameter/verification_lle.ipynb).

Cohort primary gồm 901 windows/20 sessions, nominal QC giữ **872/901 (96.8%)**, gồm **579 Awake /293 Drowsy**. Cấu hình: m=8, τ=0.16 s, Euclidean nearest admissible neighbour, per-window spectral-mean-period Theiler, fit **0.80–1.30 s**, maximum follow **5 s**, tối thiểu **50 initial pairs/30 fit pairs**, **R²≥0.90**.

### 6.1. Fit-range, QC và Theiler sensitivity

Mọi setting giữ **20 paired sessions**. ΔLLE có đơn vị s⁻¹; fit-range và Theiler experiments mỗi nhánh lưu 2.703 rows, QC dùng cached nominal estimates.

| Sensitivity | Setting | Valid windows | Median ΔLLE | Bootstrap 95% CI | r_rb | Direction | p | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fit interval | F1: 0.60–1.10 s | 802/901 | -0.034980 | [-0.064607, -0.019121] | -0.8571 | 18/20 negative; 2 positive; 0 zero | 0.000261 | ROBUST |
| Fit interval | F2: 0.80–1.30 s (nominal) | 872/901 | -0.037570 | [-0.053698, -0.022976] | -0.8095 | 16/20 negative; 4 positive; 0 zero | 0.000708 | ROBUST |
| Fit interval | F3: 1.00–1.50 s | 889/901 | -0.030357 | [-0.045778, -0.003941] | -0.6571 | 15/20 negative; 5 positive; 0 zero | 0.008308 | ROBUST |
| QC threshold | Q1: R² ≥ 0.90 (nominal) | 872/901 | -0.037570 | [-0.053698, -0.022976] | -0.8095 | 16/20 negative; 4 positive; 0 zero | 0.000708 | MODERATELY SENSITIVE |
| QC threshold | Q2: R² ≥ 0.95 | 734/901 | -0.030618 | [-0.041701, -0.013987] | -0.7429 | 16/20 negative; 4 positive; 0 zero | 0.002325 | MODERATELY SENSITIVE |
| Theiler window | T1: 0.75× | 872/901 | -0.037570 | [-0.053698, -0.022976] | -0.8095 | 16/20 negative; 4 positive; 0 zero | 0.000708 | ROBUST |
| Theiler window | T2: 1.00× (nominal) | 872/901 | -0.037570 | [-0.053698, -0.022976] | -0.8095 | 16/20 negative; 4 positive; 0 zero | 0.000708 | ROBUST |
| Theiler window | T3: 1.25× | 874/901 | -0.029763 | [-0.056095, -0.016331] | -0.7429 | 16/20 negative; 4 positive; 0 zero | 0.002325 | ROBUST |

- Fit interval: median ΔLLE luôn âm, CI đều dưới 0; assessment **ROBUST**.
- Siết QC từ R²≥0.90 lên ≥0.95: retention giảm **96.8%→81.5%** (15.3 percentage points), giữ 20 cặp và 16/20 session có Δ âm. Assessment **MODERATELY SENSITIVE về retention**, không đảo kết luận.
- Theiler 0.75/1.00/1.25×: giữ hướng âm, CI dưới 0 và đủ cặp; assessment **ROBUST**.

Các diagnostics regression/pair support đã lưu:

| Factor | Setting | Awake valid | Drowsy valid | Median fit R² | IQR fit R² | Median minimum fit pairs | IQR minimum fit pairs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fit range | F1: 0.60–1.10 s | 542 | 260 | 0.951375 | 0.040480 | 1423.0 | 18.0 |
| Fit range | F2: 0.80–1.30 s (nominal) | 579 | 293 | 0.973094 | 0.028651 | 1414.0 | 21.0 |
| Fit range | F3: 1.00–1.50 s | 588 | 301 | 0.981668 | 0.019367 | 1405.0 | 23.0 |
| QC | Q1: R² ≥ 0.90 (nominal) | 579 | 293 | 0.973094 | 0.028651 | 1414.0 | 21.0 |
| QC | Q2: R² ≥ 0.95 | 500 | 234 | 0.973094 | 0.028651 | 1414.0 | 21.0 |
| Theiler | T1: 0.75× | 579 | 293 | 0.973094 | 0.028639 | 1414.0 | 21.0 |
| Theiler | T2: 1.00× (nominal) | 579 | 293 | 0.973094 | 0.028651 | 1414.0 | 21.0 |
| Theiler | T3: 1.25× | 580 | 294 | 0.973318 | 0.028363 | 1413.0 | 22.0 |

### 6.2. Theiler distribution và thay đổi QC status

Theiler nominal là **quy tắc spectral mean period riêng mỗi window**, không phải một số giây chung. Output public không lưu đầy đủ nearest-neighbour identities cho toàn batch; bảng báo số window thay đổi exclusion boundary và valid/QC status.

| Setting | fs group (Hz) | Windows | Median W (s) | Q25 W (s) | Q75 W (s) | Median W samples | Q25 samples | Q75 samples | Boundary changed | QC status changed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1: 0.75× | 25 | 870 | 0.3601 | 0.3201 | 0.4001 | 9.0 | 8.0 | 10.0 | 870 | 0 |
| T1: 0.75× | 50 | 31 | 0.4200 | 0.4200 | 0.4400 | 21.0 | 21.0 | 22.0 | 31 | 0 |
| T2: 1.00× (nominal) | 25 | 870 | 0.4960 | 0.4471 | 0.5471 | 12.0 | 11.0 | 14.0 | 0 | 0 |
| T2: 1.00× (nominal) | 50 | 31 | 0.5604 | 0.5473 | 0.5927 | 28.0 | 27.0 | 30.0 | 0 | 0 |
| T3: 1.25× | 25 | 870 | 0.6003 | 0.5601 | 0.6802 | 15.0 | 14.0 | 17.0 | 870 | 2 |
| T3: 1.25× | 50 | 31 | 0.7000 | 0.6800 | 0.7400 | 35.0 | 34.0 | 37.0 | 31 | 0 |

0.75× và 1.25× đều đổi boundary ở toàn bộ 901 windows. 0.75× không đổi final valid status; 1.25× đổi status ở **2 windows thuộc nhóm 25 Hz**, retention tăng 872→874.

### 6.3. Pair-support và reproducibility

Pair support nominal lớn hơn nhiều ngưỡng freeze:

| Statistic | Initial pairs | Minimum fit-region pairs |
| --- | --- | --- |
| minimum | 1471.0 | 1366.0 |
| Q1 | 1472.0 | 1403.0 |
| median | 1472.0 | 1414.0 |

Không có primary window nào có initial pairs≤100 hoặc fit pairs≤60 (hai lần ngưỡng nominal).

Audit deterministic trên **6 windows đại diện nhóm 25/50 Hz** khớp tau samples, Theiler samples, selected neighbours, divergence curves, pair-support trajectories, fit indices, LLE và R². Repeated LLE/R² và đối chiếu nominal cache đều **max absolute difference=0**; neighbour/pair-support/fit-index mismatches đều **0**.

**LLE verification status: COMPLETE.** Kết luận âm ổn định trên fit intervals, QC thresholds và local Theiler perturbations đã khảo sát; giữ nguyên cấu hình nominal.

## 7. Cấu hình estimator đã chốt

### 7.1. Cấu hình chung

| Thành phần | Giá trị / quy tắc |
|---|---|
| Primary signal và window | Processed PPG; 60 s |
| Primary cohort | 901 windows; 20 sessions; analysis_included=True cùng SQI/processed-stationarity mask |
| State labels | Awake=0; Drowsy=1 |
| Embedding | m=8; τ=0.16 s |
| Delay conversion | round(τ×fs): 4 samples ở 25 Hz; 8 ở 50 Hz |
| State-space distance | Euclidean |
| Aggregation | Window metric → median valid windows trong session×state → Δ=Drowsy−Awake; prediction mean horizons trước median windows |
| Freeze principle | Nominal không chọn lại theo p-value hoặc Awake–Drowsy effect |

### 7.2. Simplex Projection

| Thành phần | Frozen setting |
|---|---|
| Input scaling | Z-score trong từng window; numpy.std ddof=0 |
| Neighbours | k=m+1=9 |
| Mode | Leave-one-out state-space prediction |
| Temporal exclusion | Chấp nhận neighbour khi \|t_neighbor−t_query\|>W; W=1 s |
| W samples | 25 tại 25 Hz; 50 tại 50 Hz |
| Weights | Normalized exp(−d_i/d_1); exact matches tại 0 được chia đều trọng số |
| Horizons (s) | 0.04, 0.08, 0.12, 0.16, 0.20, 0.28, 0.40, 0.60, 0.80, 1.00, 1.20, 1.60, 2.00, 2.40, 2.80, 3.20, 3.60, 4.00 |
| Horizons conversion | round(h×fs), numpy.rint; ở 25 Hz: 1,2,3,4,5,7,10,15,20,25,30,40,50,60,70,80,90,100 samples; ở 50 Hz nhân đôi |
| Maximum horizon | 4 s |
| Window metrics | Pearson CC, RMSE, NRMSE; z-score nên NRMSE=RMSE/1.0 |

### 7.3. RQA

| Thành phần | Frozen setting |
|---|---|
| Distance | Pairwise Euclidean |
| Threshold | Per-window epsilon, fixed target RR=0.02, tie-safe thresholding |
| RR tolerance | 5×10⁻⁵ |
| Nominal Theiler | W=(m−1)×tau_samples; 28/56 samples ở 25/50 Hz |
| Exclusion | Loại line of identity và pairs có \|i−j\|≤W trước metric |
| Minimum line lengths | l_min=v_min=2 |
| Diagonal metrics | DET, Lmean, ENTR, Lmax |
| Vertical metrics | LAM, TT, Vmax |
| Verification metrics | Headline DET; secondary LAM/TT |
| Epsilon | Recompute mỗi window theo admissible region; current src/rqa/rqa.py là reference |

### 7.4. Rosenstein LLE

| Thành phần | Frozen setting |
|---|---|
| Neighbour | Một nearest admissible neighbour trong Euclidean space |
| Theiler | Spectral mean period mỗi window; nghịch đảo spectral centroid của one-sided power spectrum, bỏ DC |
| W conversion | max(round(W_seconds×fs),1); chấp nhận neighbour khi \|j−i\|>W_samples |
| Divergence | Mean log Euclidean distance khi neighbour pairs cùng tiến theo lag |
| Nominal fit | 0.80–1.30 s; đưa hai đầu vào fit nếu thỏa sampled support/QC |
| Follow time | 5 s |
| Regression / units | Linear regression mean log-distance theo thời gian; slope là LLE (s⁻¹) |
| Pair thresholds | Initial≥50; mỗi fit lag≥30 |
| Fit points | Ít nhất 3 usable points |
| Nominal QC | LLE hữu hạn, đủ support/fit points và R²≥0.90 |
| Negative LLE | Không tự động xóa row; computation success và QC flags báo riêng |

## 8. Ma trận tổng hợp finding và giới hạn kết luận

| Finding | Label rules T30/T60/S3/S5 | Delay τ=0.12/0.16/0.20 | Dimension m=7/8/9 | Method-specific verification |
|---|---|---|---|---|
| Mean_CC ↓ | 4/4 rules cùng hướng; q<0.05 cả 4; T60 CI chứa 0 | 3/3 cùng hướng; CI chứa 0 ở τ=0.12/0.16 | 3/3 cùng hướng; CI chứa 0 cả 3 | Theiler stability/support được ghi nhận; per-window reproduction exact |
| Mean_NRMSE ↑ | 4/4 cùng hướng; CI không chứa 0 và q<0.05 cả 4 | 3/3 cùng hướng; τ=0.12 CI chứa 0 | 3/3 cùng hướng; m=7 CI chứa 0 | Cùng Simplex verification và aggregation audit |
| DET ↓ | 4/4 cùng hướng; CI dưới 0 và q<0.05 cả 4 | **Nhạy với delay**: chỉ nominal âm; hai mức còn lại gần 0/dương | 3/3 cùng hướng; q<0.05 chỉ ở m=8 | Robust với RR/Theiler; RR=0.01 CI chứa 0; current-core reproduction PASS |
| LLE ↓ | 4/4 cùng hướng; q<0.05 cả 4; T30 CI chứa 0 | 3/3 cùng hướng; τ=0.12 CI chứa 0 | 3/3 cùng hướng; CI dưới 0 cả 3; magnitude biến thiên | Fit/Theiler robust; QC moderately sensitive về retention; audit exact |

**Kết luận chung:** label verification đã hoàn thành và hỗ trợ cả bốn finding dưới các conservative label rules. CC/NRMSE/LLE có direction ổn định trong vùng embedding đã kiểm tra; DET có robustness phụ thuộc reconstruction choice, đặc biệt τ. Method-specific verification hỗ trợ giữ nominal Simplex/RQA/LLE, nhưng trạng thái COMPLETE của notebook không đồng nghĩa mọi metric bất biến với tất cả tham số.

Các kết quả trên là session-level contrasts; chưa có kết quả subject-level strict sensitivity/cluster bootstrap, window-length robustness 30/120/180 s, full Cartesian embedding grid hoặc minimum-line-length perturbation trong tám notebook này. `overview.md` là kế hoạch; các hạng mục chỉ có trong kế hoạch không được tính là verification đã đạt.

## 9. Bảng coverage theo session

Bảng dưới giữ primary included windows từ phase-space notebook và included windows của từng label rule từ B0. Mỗi ô là **Awake / Drowsy**; sampling/segmentation của từng rule có thể tạo window khác primary.

| Session | Primary | T30 | T60 | S3 | S5 |
| --- | --- | --- | --- | --- | --- |
| 01 | 24 / 7 | 21 / 6 | 18 / 2 | 21 / 5 | 17 / 2 |
| 04 | 29 / 17 | 28 / 14 | 27 / 13 | 30 / 16 | 27 / 13 |
| 05 | 33 / 16 | 33 / 16 | 32 / 12 | 34 / 16 | 34 / 16 |
| 06 | 31 / 17 | 32 / 15 | 29 / 12 | 32 / 15 | 32 / 15 |
| 07 | 34 / 11 | 33 / 7 | 32 / 8 | 34 / 9 | 34 / 9 |
| 08 | 36 / 10 | 36 / 8 | 35 / 7 | 35 / 10 | 35 / 6 |
| 09 | 47 / 18 | 43 / 20 | 46 / 17 | 49 / 18 | 45 / 18 |
| 10 | 27 / 9 | 28 / 7 | 26 / 6 | 27 / 9 | 27 / 5 |
| 11 | 20 / 18 | 20 / 17 | 18 / 15 | 21 / 18 | 21 / 18 |
| 12 | 20 / 35 | 17 / 31 | 15 / 28 | 20 / 35 | 20 / 32 |
| 13 | 25 / 23 | 25 / 20 | 23 / 20 | 26 / 23 | 26 / 23 |
| 14 | 31 / 17 | 31 / 14 | 26 / 13 | 30 / 16 | 30 / 13 |
| 15 | 28 / 6 | 30 / 4 | 28 / 2 | 30 / 3 | 27 / 0 |
| 17 | 28 / 14 | 27 / 12 | 26 / 10 | 28 / 13 | 28 / 10 |
| 18 | 19 / 21 | 18 / 23 | 17 / 20 | 20 / 22 | 20 / 22 |
| 19 | 34 / 10 | 33 / 10 | 31 / 8 | 34 / 11 | 34 / 11 |
| 21 | 25 / 15 | 24 / 14 | 21 / 11 | 26 / 12 | 22 / 12 |
| 22 | 29 / 13 | 29 / 13 | 25 / 10 | 30 / 12 | 27 / 12 |
| 23 | 49 / 13 | 50 / 10 | 50 / 10 | 53 / 13 | 53 / 13 |
| 25 | 27 / 15 | 28 / 13 | 26 / 12 | 29 / 15 | 22 / 15 |

## 10. Hồ sơ kết quả và nguồn đối chiếu

| Notebook | Kết quả được giữ trong notebook |
|---|---|
| [verification_data](verification_data/verification_data.ipynb) | Integrity/lineage, segment/transition/oscillation, masks và retained intervals, retention, feasibility, audit sessions 09/13, 5 figures inline |
| [create_data_label_sensitive](verification_data/create_data_label_sensitive.ipynb) | Boundary checks; master/per-session retention; 80 saved-file checks; query window; B0 COMPLETE |
| [ntsa_data_label_sensitive](verification_data/ntsa_data_label_sensitive.ipynb) | Per-rule input coverage, execution counts, method/QC counts, technical validation; T30/T60/S3/S5 complete |
| [label_sensitive_validation](verification_data/label_sensitive_validation.ipynb) | Metric validity/paired coverage, 16 statistical rows, P0 comparison/effect ratios, direction/BH summary, figure 2×2 inline; label COMPLETE |
| [verification_phase_space_reconstruction](verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb) | Primary coverage, FNN τ×m, τ/m inference, magnitude/CI/q summary, nominal audit; 3 figures inline; conditional robustness |
| [verification_prediction](verification_ntsa_parameter/verification_prediction.ipynb) | Markdown summary của completed Simplex Theiler/support/reproducibility evidence; COMPLETE |
| [verification_rqa](verification_ntsa_parameter/verification_rqa.ipynb) | RR/Theiler inference, epsilon/RR/window QC, Theiler distribution, current/legacy cache audit, 2 figures inline; COMPLETE |
| [verification_lle](verification_ntsa_parameter/verification_lle.ipynb) | Fit/QC/Theiler inference và diagnostics, support và reproducibility audits, 3 figures inline; COMPLETE |

Các figure, bảng chi tiết row-level và per-session đầy đủ tiếp tục nằm trong notebook nguồn. Những đường dẫn output `phase1/results/...` được nêu theo hồ sơ lần chạy đã lưu trong notebook; việc lập summary không tạo lại hoặc xác nhận sự hiện diện của các output bên ngoài notebook.

Nguồn estimator/production dùng để đối chiếu cấu hình đã chốt: [simplex_projection.ipynb](../notebook/simplex_projection.ipynb), [rqa.ipynb](../notebook/rqa.ipynb), [lyapunov.ipynb](../notebook/lyapunov.ipynb), [simplex_projection.py](../src/prediction/simplex_projection.py), [rqa.py](../src/rqa/rqa.py), [lyapunov.py](../src/chaos/lyapunov.py).
