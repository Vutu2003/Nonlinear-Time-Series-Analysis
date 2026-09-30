# Data readiness audit — unknown repeated-session dependence

> **Cập nhật 2026-09-30:** Kết luận NOT READY bên dưới là snapshot trước khi sửa thứ tự gộp Simplex. Hai vector Mean CC/Mean NRMSE đã được tái tính, kiểm chứng và đóng băng trong [báo cáo resolution](primary_simplex_windowfirst_resolution.md), với [bảng canonical mới](../primary_simplex_windowfirst_v1/primary_simplex_session_paired_60s_processed_P0_v1.csv). Không dùng ba paired CSV legacy ở mục B làm nguồn prediction cho sensitivity experiment; protocol ngẫu nhiên của thí nghiệm vẫn cần được chốt riêng.

Ngày kiểm tra: 2026-09-30. Phạm vi: phân tích chính P0, Processed PPG, cửa sổ 60 s, 20 **session** và 7 metric. Audit chỉ đọc dữ liệu và tái tính thống kê gốc để kiểm chứng; chưa ghép pseudo-subject, chưa chạy sensitivity experiment.

## A. Readiness verdict

**NOT READY.** Cả 7 kết quả đã lưu tái hiện được từ 20 cặp session, nhưng hai bảng `Mean_CC`/`Mean_NRMSE` chính được tạo bằng **mean của 18 median theo horizon**, khác thứ tự gộp được chỉ định: **mean 18 horizons trong từng window, rồi median các window theo session-state**. Chênh lệch này liên quan trực tiếp đến 2 trong 4 headline metrics; project còn ghi một mốc prediction nominal khác. Cần xác định và đóng băng đúng vector Δ của hai metric này trước khi coi dữ liệu là đầu vào hợp lệ cho thí nghiệm mới.

## B. Canonical data source hiện có

Ba bảng paired đang được `main/bh_fdr.ipynb` và `main/summary_result.ipynb` dùng để dựng kết quả chính; mỗi bảng có 20 dòng, 20 session giống nhau, một dòng/session, đủ Awake, Drowsy và Δ:

| File, cột nguồn | Metric bản thảo | Nguồn sâu hơn / quy tắc đang dùng |
| --- | --- | --- |
| `outputs/prediction/prediction_state_paired_values_60s_processed.csv`: `mean_cc_awake`, `mean_cc_drowsy`, `delta_mean_cc` | Mean CC | `results/simplex_projection/summary/processed_simplex_summary.csv`: `median_cc` theo 18 `horizon_seconds` → **mean của các median** (`main/prediction_nonlinear.ipynb`, cell 7). |
| Cùng file: `mean_nrmse_awake`, `mean_nrmse_drowsy`, `delta_mean_nrmse` | Mean NRMSE | Cùng nguồn, `median_nrmse` → **mean của các median**. |
| `outputs/rqa/rqa_state_paired_values_60s_processed.csv`: `{DET,Lmean,LAM,TT}_{awake,drowsy,delta}` | DET, Lmean, LAM, TT | `results/rqa/rqa_window_level.csv`: median từng metric qua window 60 s Processed theo session-state (`main/rqa_main.ipynb`, cells 4, 9). |
| `outputs/lle/lle_session_paired_deltas_60s_processed.csv`: `lle_awake`, `lle_drowsy`, `delta_lle_drowsy_minus_awake` | LLE, s⁻¹ | 20 file `results/lle/processed/session_*_processed_rosenstein_lle.csv`: median `lle_1_per_s` qua window hợp lệ theo session-state (`main/lle_main.ipynb`, cells 1, 4, 6). |

Không có **một** bảng 20 × 22 cột đã đóng băng theo schema được yêu cầu. Bảng `outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv` chỉ là tổng hợp **7 metric**, không chứa vector Δ từng session nên không dùng làm input ghép cặp. Trong ba bảng paired, Δ có sẵn và là Drowsy − Awake; sai khác lớn nhất giữa Δ lưu và hiệu hai giá trị trạng thái là `1.0e-8` do làm tròn CSV.

SHA-256 của ba paired CSV tại thời điểm audit, theo thứ tự prediction/RQA/LLE trong bảng trên: `75f2cc733de8edf42a8af2c6c1740152f639c09556d28bb67052e6988a56ad33`, `b7c3206322ffbb5ff1ef7a16f0e54e8ab73946c4bdb7260732eb85198754f7dc`, `1385247cce74beceee7c7dc1e874593ab5b38d4563be5894ff35ee423f5ec62a`.

## C. Primary-result reproduction

Tính lại từ **Awake và Drowsy của ba bảng paired**, sắp theo ID session số tăng dần; Wilcoxon hai phía, `r_rb` từ tổng signed ranks, BH trên đúng 7 p. Cột “bản thảo p/q” để `—` ở p vì yêu cầu đầu vào chỉ cung cấp q; p nguồn nằm trong bảng kết quả đã lưu. Sai khác q ở chữ số cuối là do p được làm tròn khi ghi CSV.

| Metric | Manuscript Δ | Reproduced Δ | Manuscript p/q | Reproduced p/q | Match? |
| --- | ---: | ---: | ---: | ---: | :---: |
| Mean CC | −0.0339 | −0.03387057 | — / 0.0376 | 0.02148438 / 0.03759766 | Có¹ |
| Mean NRMSE | +0.0294 | +0.02942366 | — / 0.0255 | 0.00729561 / 0.02553463 | Có¹ |
| DET | −0.0186 | −0.01864472 | — / 0.0376 | 0.02148438 / 0.03759766 | Có |
| Lmean | −0.0630 | −0.06299104 | — / 0.0816 | 0.05825806 / 0.08156128 | Có |
| LAM | +0.0165 | +0.01650909 | — / 0.1667 | 0.14290619 / 0.16672389 | Có |
| TT | +0.0095 | +0.00951548 | — / 0.2024 | 0.20244980 / 0.20244980 | Có |
| LLE | −0.0376 | −0.03757036 | — / 0.0050 | 0.00070763 / 0.00495338 | Có |

¹ **Chỉ khớp số đã công bố, chưa khớp định nghĩa gộp metric đã nêu.** `verification_result/summary.md` còn ghi mốc prediction nominal khác: Mean CC `−0.027705`, Mean NRMSE `+0.031855`; bảng cũ `results/simplex_projection/summary/simplex_rq2_final_inference.csv` cũng dùng một estimand/kiểm định khác và không thay thế bảng primary. Phải giải quyết nguồn kết quả cuối bằng provenance, không chọn phiên bản theo hiệu ứng quan sát.

`r_rb` tái tính lần lượt: `−0.580952`, `+0.666667`, `−0.580952`, `−0.485714`, `+0.380952`, `+0.333333`, `−0.809524`; tất cả khớp bảng nguồn ở 6 chữ số. CI percentile 95% với 20.000 lần resample và seed/thuật toán của từng notebook cũng khớp sau làm tròn: Mean CC `[−0.0595, −0.0043]`, Mean NRMSE `[0.0047, 0.0530]`, DET `[−0.0364, −0.0069]`, Lmean `[−0.1247, −0.0139]`, LAM `[−0.0044, 0.0635]`, TT `[−0.0034, 0.0160]`, LLE `[−0.0537, −0.0230]`. Các Δ hiện tại đều khác 0 và không có tie trị tuyệt đối, nên nhánh xử lý zero/tie chưa bị kích hoạt trong n=20.

## D. Data integrity checks

| Kiểm tra | Kết quả | Bằng chứng / giới hạn |
| --- | --- | --- |
| Đúng 20 session duy nhất; không gồm session bị loại | **PASS** | Cả ba bảng paired có đúng tập ID `01, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25`, khớp 20 file `segmentated_data/dhdata/sample_*.npz`. |
| Hai state và đủ 7 metric mỗi session | **PASS** | 20 cặp/bảng; toàn bộ 140 Δ hữu hạn; RQA/LLE có cột `Processed`, `60`; prediction tách từ summary Processed 60 s. |
| Không duplicate session-state / window key | **PASS** | Không trùng session trong paired; 901 key window RQA và 901 key LLE duy nhất; summary prediction 720 key = 20 × 2 × 18 horizons. |
| Đúng nhánh P0, 60 s không chồng lấn | **PASS cho RQA/LLE; provenance prediction cần đóng băng** | `segments_index.csv` và tài liệu `segmentated_data/dhdata/infomation.md` xác nhận 60 s non-overlap, label 0/1 và processed-stationarity. 901 RQA window khớp 1:1 `(session, window_id, state)` với 901 window P0 eligible: 596 Awake, 305 Drowsy. Prediction summary có tổng `n_windows=901` và cùng số theo session-state, nhưng thiếu window ID để đối chiếu từng hàng. |
| Valid-window QC | **PASS cho RQA/LLE; chưa truy vết đủ cho prediction** | RQA dùng 901 finite processed windows. LLE có 901 record, 872 `valid=True` (579 Awake, 293 Drowsy), 29 bị loại; `valid` đúng với `analysis_included`, finite và `fit_r2 ≥ 0.90`. Prediction summary chỉ ghi `n_windows`/valid fraction, không có bảng primary 60 s per-window hoặc QC flag từng window. |
| Định nghĩa 7 metric | **FAIL cho Mean CC/Mean NRMSE; PASS cho 5 metric còn lại** | Tái gộp RQA window → state sai khác tối đa `<5e-10`, LLE `<5e-11`; mean 18 `median_cc`/`median_nrmse` → prediction state sai khác `<5e-9`. Mean(median theo horizon) không đồng nhất với median(mean theo window). |
| Frozen parameters và đơn vị | **PASS một phần** | Code/config: m=8, τ=0.16 s; Simplex Theiler=1.0 s, 18 horizons; RQA RR=0.02, `l_min=v_min=2`, Theiler `(m−1)×tau_samples` = 28/56 samples; LLE s⁻¹, Theiler theo spectral mean period, fit 0.80–1.30 s, R²≥0.90. RQA CSV ghi `target_rr`, `tau_samples`, `theiler_samples`; LLE CSV ghi m, τ, fit, QC. Prediction paired và RQA paired không mang đầy đủ parameter/provenance hash. |
| Session ordering deterministic | **PASS nếu áp đặt quy tắc; chưa freeze trong input chung** | Cả ba paired hiện xếp ID số tăng dần; các notebook cũng parse và sort numeric ID. Cần ghi quy tắc trong manifest/canonical table, không dựa vào thứ tự CSV ngẫu nhiên. |

Các nhánh khác hiện diện và phải tránh trộn: `results/30s_window`, `outputs/robust_window` (30/60/120/180 s), `results/data_label_sensitive`/`results/ntsa_label_sensitive` (T30/T60/S3/S5), RQA `Raw`, LLE R²≥0.95 sensitivity, và `outputs/statistic/rq1_pps_*` (đối chứng PPS, không phải Awake–Drowsy). `phase1/README.md` nhắc các script preprocessing/segmentation không còn thấy ở `phase1/main`, nên README không đủ làm chứng cứ về phiên bản cuối.

## E. Missing requirements

1. **Giải quyết discrepancy Mean CC/Mean NRMSE trước khi chạy thí nghiệm.** Xác định estimand cuối theo protocol đã định, xuất/kiểm chứng dữ liệu **primary 60 s per-window** chứa 18 horizons hoặc `Mean_CC`/`Mean_NRMSE` của mỗi window, valid/QC flag và `(session, state, window_id)`. Sau đó tính median theo session-state, so lại cả 7 thống kê và xác định có cần sửa bảng manuscript hay không. Không dùng output T30/T60/S3/S5 hoặc 30 s để thay P0.
2. Đóng băng **một** bảng canonical 20 dòng cùng manifest nguồn: phiên bản/sha256 của ba nguồn, định nghĩa metric, nhánh P0, tham số, QC, đơn vị, quy tắc chuẩn hóa/sort ID và sai số đối chiếu khi đọc CSV. Hiện các paired CSV thiếu metadata này; có nhiều output prediction với estimand khác nhau.
3. Trước sensitivity experiment, pre-register seed ghép cặp ngẫu nhiên, số partition, thuật toán sinh partition, cách xử lý zero/tie có thể phát sinh ở n=10, quy tắc kiểm định/BH/CI cho pseudo-cluster và tolerance. Những thứ này **chưa được freeze cho thí nghiệm mới**.

| Thành phần tái lập | Trạng thái hiện tại |
| --- | --- |
| Random seed cho pseudo-subject pairing | **Thiếu; phải freeze**. |
| Ordering session | **Suy ra từ code**: parse ID số rồi sort tăng; cần ghi cố định trong canonical input. |
| Wilcoxon | **Đã freeze cho primary**: prediction dùng exact subset-sum trong `main/prediction_nonlinear.ipynb`; RQA/LLE dùng `scipy.stats.wilcoxon`, `alternative='two-sided'`, `zero_method='wilcox'`, `correction=False`, `method='auto'`. |
| Zero/tie và `r_rb` | **Suy ra từ code**: bỏ zero (prediction `atol=1e-12`; RQA/LLE zero hóa bằng `isclose(rtol=1e-9, atol=1e-12)`), average ranks của `abs(Δ)`, `r_rb=(W+−W−)/(W++W−)`. Cần chọn một quy ước cho n=10. |
| BH-FDR | **Đã freeze cho primary**: `main/bh_fdr.ipynb` tính BH monotone một lần trên 7 raw p. |
| Bootstrap seed/count | **Đã freeze cho primary**: 20.000; prediction seeds 20260829/20260830, RQA `SeedSequence(20260829).spawn(4)`, LLE 20260829. Seed/CI cho n=10 **thiếu**. |
| Numerical tolerance | **Một phần suy ra từ code** (`isclose`/`allclose` khác nhau); **thiếu** tolerance chung cho bảng canonical/experiment. |

## F. Recommended canonical input

Sau khi xử lý điểm nghẽn prediction, tạo **một** CSV trong `sensitivy_data` từ ba nguồn ở mục B, với 20 dòng sort theo ID số và schema:

```text
session_id,
Mean_CC_Awake,Mean_CC_Drowsy,Mean_CC_delta,
Mean_NRMSE_Awake,Mean_NRMSE_Drowsy,Mean_NRMSE_delta,
DET_Awake,DET_Drowsy,DET_delta,
Lmean_Awake,Lmean_Drowsy,Lmean_delta,
LAM_Awake,LAM_Drowsy,LAM_delta,
TT_Awake,TT_Drowsy,TT_delta,
LLE_Awake,LLE_Drowsy,LLE_delta
```

`session_id` nên là `session_01`, `session_04`, …, `session_25`; mọi `_delta` tính lại bằng Drowsy − Awake từ giá trị **chưa làm tròn** rồi đối chiếu với delta lưu. Prediction phải lấy từ estimator window → state đã được xác nhận; RQA và LLE lấy từ hai bảng paired nêu trên. Không tạo CSV này trong audit vì chưa giải quyết discrepancy. Vector Δ sau khi freeze và sort là đủ để phân hoạch ngẫu nhiên 20 session thành 10 cặp rời nhau, lấy trung bình số học từng cặp và mô tả n=10 pseudo-cluster; **không cần participant ID hoặc liên kết subject thật**, cũng không suy ra participant-level inference.

## G. Final decision

**Is the current dataset sufficient to proceed with the unknown repeated-session dependence sensitivity experiment? NO.** Dữ liệu hiện tại đủ để lặp lại **bảng số đã lưu**, nhưng chưa bảo đảm hai vector prediction tuân thủ định nghĩa primary được yêu cầu. Khi hai metric này và provenance của bảng canonical được xác nhận/đóng băng, có thể tiến hành phép sensitivity ở cấp session giả định mà không cần nhận dạng participant.
