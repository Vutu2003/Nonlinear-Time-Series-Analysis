# Resolve and freeze primary Simplex aggregation — Mean CC / Mean NRMSE

Ngày: 2026-09-30. Phạm vi: Processed PPG, P0, 60 s, 20 **session**. Đây là kết quả kiểm chứng và đóng băng hai vector prediction; **không chạy** pseudo-subject/adversarial pairing. Mọi delta là Drowsy − Awake, inference ở cấp session.

## A. Provenance finding

Giá trị manuscript cũ (`Mean_CC Δ=−0.03387057`, `Mean_NRMSE Δ=+0.02942366`) đi theo chuỗi `notebook/simplex_projection.ipynb` → `results/simplex_projection/summary/processed_simplex_summary.csv` → `main/prediction_nonlinear.ipynb` cell 7 → `outputs/prediction/prediction_state_paired_values_60s_processed.csv` → `outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv`. Notebook đầu tạo **median của window cho từng horizon**; cell 7 lấy **mean của 18 median** trong mỗi session-state. Đây là estimand B: `mean_h(median_w(CC_{w,h}))`, không phải estimand cuối A: `median_w(mean_h(CC_{w,h}))`. NRMSE cũng vậy. Tái gộp 720 hàng summary cũ theo B khớp paired cũ trong khoảng `<5e-9` (CSV paired bị làm tròn).

Bảng per-window × horizon P0 trước đây chỉ nằm trong biến `processed_window_results` của notebook và trong cache RAM của `verification_result/verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb`; không thấy file CSV hoàn chỉnh trên disk. Mốc nominal `−0.027705/+0.031855` trong notebook verification **không được chấp nhận chỉ vì trùng dự kiến**: mã verification lấy `Mean_CC`/`Mean_NRMSE` của từng window rồi median trong session-state, và kết quả mới bên dưới độc lập tái tính từ 20 NPZ P0 bằng estimator Simplex gốc. Bảng `results/simplex_projection/summary/simplex_rq2_final_inference.csv` là nhánh cũ/estimand khác, không phải nguồn primary mới.

## B. Correct aggregation verification

Producer [freeze_primary_simplex_windowfirst_v1.py](../freeze_primary_simplex_windowfirst_v1.py) tải trực tiếp 20 file `segmentated_data/dhdata/sample_*.npz` qua `get_data(..., window_sizes=(60,), stationarity='processed')`; đối chiếu đủ 901 key `(session, state, window_id)` với `segments_index.csv`. Mã dùng đúng `standardize_signal`, `build_embedding`, `simplex_all_theiler` của `notebook/simplex_projection.ipynb` cell 4 và `prediction_metrics(..., nrmse_scale=1.0)` từ core. Nó giữ m=8, τ=0.16 s, k=9, Euclidean, exponential weights, leave-one-out, W=1.0 s và 18 horizons được freeze. Không cần xấp xỉ từ các median theo horizon.

Kiểm chứng quyết định: tính lại **toàn bộ 720 median theo horizon** của `processed_simplex_summary.csv` từ 16.218 kết quả window–horizon: sai số tuyệt đối tối đa CC `5.55e-16`, NRMSE `2.22e-16`; số window từng cell cũng khớp. Vì thế dữ liệu P0 và estimator tái hiện nhánh nguồn cũ ở cấp chi tiết, còn chênh lệch paired là do đổi **thứ tự aggregation** đúng như protocol. Bảng mới cũng tái hiện mốc nominal và CI/p/r_rb của notebook phase-space verification, nhưng q trong notebook đó thuộc **family 4 metric**; q primary mới phải tính trên **7 metric** ở mục F.

## C. Prediction data integrity

- **Session IDs:** `01, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25`; đúng cùng tập 20 session RQA/LLE, mỗi session đủ Awake và Drowsy.
- **QC và P0:** 951 candidate window 60 s; 901 window pass processed-stationarity/SQI/segmentation theo index P0, gồm **596 Awake, 305 Drowsy**; 50 candidate không vào estimator. Tập 901 key loader bằng tập 901 key index; nhãn 0=Awake, 1=Drowsy. Chỉ dùng 60 s Processed, không đọc Raw, 30/120/180 s hoặc T30/T60/S3/S5.
- **Horizon:** đúng 18 giá trị `{0.04, 0.08, 0.12, 0.16, 0.20, 0.28, 0.40, 0.60, 0.80, 1.00, 1.20, 1.60, 2.00, 2.40, 2.80, 3.20, 3.60, 4.00}` s trên **mọi** window; 16.218 hàng quan sát = 901 × 18. Không thiếu horizon, không duplicate `(session,state,window_id,horizon_s)`, CC/NRMSE hữu hạn, minimum prediction support=1.0. Không đưa window có metric lỗi vào median.
- **Số window theo session-state:**

| Session | Awake | Drowsy | Session | Awake | Drowsy |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 01 | 24 | 7 | 12 | 20 | 35 |
| 04 | 29 | 17 | 13 | 25 | 23 |
| 05 | 33 | 16 | 14 | 31 | 17 |
| 06 | 31 | 17 | 15 | 28 | 6 |
| 07 | 34 | 11 | 17 | 28 | 14 |
| 08 | 36 | 10 | 18 | 19 | 21 |
| 09 | 47 | 18 | 19 | 34 | 10 |
| 10 | 27 | 9 | 21 | 25 | 15 |
| 11 | 20 | 18 | 22 | 29 | 13 |
|  |  |  | 23 | 49 | 13 |
|  |  |  | 25 | 27 | 15 |

## D. Corrected 20-session vectors

Bảng canonical 7 cột, 20 dòng, **full precision**: [primary_simplex_session_paired_60s_processed_P0_v1.csv](../primary_simplex_windowfirst_v1/primary_simplex_session_paired_60s_processed_P0_v1.csv). Hai bảng kiểm tra sâu: [901 window means](../primary_simplex_windowfirst_v1/primary_simplex_window_means_60s_processed_P0_v1.csv) và [16.218 horizon records](../primary_simplex_windowfirst_v1/primary_simplex_window_horizons_60s_processed_P0_v1.csv). Thứ tự ID được sắp số tăng dần; mỗi delta được tính trực tiếp từ hai giá trị session-state chưa làm tròn và sai số identity `delta − (Drowsy−Awake)` bằng 0 trong dữ liệu nội bộ.

| Session | Mean CC Δ | Mean NRMSE Δ | Session | Mean CC Δ | Mean NRMSE Δ |
| --- | ---: | ---: | --- | ---: | ---: |
| 01 | +0.025775 | −0.001334 | 12 | −0.048485 | +0.034647 |
| 04 | +0.023996 | −0.010741 | 13 | +0.005639 | +0.003293 |
| 05 | −0.027775 | +0.027246 | 14 | −0.057059 | +0.052961 |
| 06 | −0.023599 | +0.035298 | 15 | +0.007161 | −0.002846 |
| 07 | −0.059648 | +0.055072 | 17 | +0.090211 | −0.086758 |
| 08 | −0.045343 | +0.038842 | 18 | −0.068587 | +0.061852 |
| 09 | +0.011624 | +0.000874 | 19 | −0.047498 | +0.059709 |
| 10 | −0.067121 | +0.051107 | 21 | −0.007622 | −0.006387 |
| 11 | −0.027636 | +0.029064 | 22 | −0.115594 | +0.080391 |
|  |  |  | 23 | +0.011589 | −0.000488 |
|  |  |  | 25 | −0.053311 | +0.052634 |

## E. Corrected primary statistics

| Metric | Median paired Δ | Wilcoxon p (two-sided) | `r_rb` | Percentile bootstrap 95% CI | Direction |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean CC | −0.027705109373 | 0.026641845703 | −0.561904761905 | [−0.050898179942, +0.006400153115] | 13/20 âm |
| Mean NRMSE | +0.031855105488 | 0.015312194824 | +0.609523809524 | [+0.000193193215, +0.051870844998] | 14/20 dương |

Quy ước giống `main/prediction_nonlinear.ipynb` cell 8: Wilcoxon **exact two-sided subset-sum**, thống kê là rank nhỏ hơn, loại zero theo `np.isclose(atol=1e-12, rtol=0)` (`zero_method='wilcox'` tương đương); tie của `abs(Δ)` dùng average ranks rồi nhân 2 để liệt kê exact. `r_rb=(W+−W−)/(W++W−)`. Cả hai vector không có zero hoặc tie trị tuyệt đối. Bootstrap paired-session `np.random.default_rng(seed).integers(0,20,size=(20000,20))`, median và `np.quantile([.025,.975])`; seed CC `20260829`, NRMSE `20260830`. Tolerance kiểm chứng 720 median nguồn là `1e-12` tuyệt đối; delta tính bằng cùng phép trừ trong bộ nhớ, không làm tròn trước inference. Không dùng window làm đơn vị inference.

## F. Updated seven-metric BH-FDR

Dùng hai raw p mới ở mục E và **năm raw p primary đã lưu** trong `outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv`; BH monotone đúng mã `main/bh_fdr.ipynb` trên 7 test. File kết quả: [primary_bh_fdr_7metrics_windowfirst_P0_v1.csv](../primary_simplex_windowfirst_v1/primary_bh_fdr_7metrics_windowfirst_P0_v1.csv). Sai số chữ số cuối đối với các p cũ phản ánh độ chính xác CSV nguồn.

| Metric | Raw p | q_BH mới | q<0.05? |
| --- | ---: | ---: | :---: |
| Mean CC | 0.0266418457 | 0.0466232300 | Có |
| Mean NRMSE | 0.0153121948 | 0.0466232300 | Có |
| DET | 0.0214843750 | 0.0466232300 | Có |
| Lmean | 0.0582580566 | 0.0815612793 | Không |
| LAM | 0.1429061890 | 0.1667238872 | Không |
| TT | 0.2024497986 | 0.2024497986 | Không |
| LLE | 0.0007076263 | 0.0049533844 | Có |

Tập BH-supported **không đổi**: Mean CC, Mean NRMSE, DET, LLE. q của DET đổi dù giá trị DET và raw p giữ nguyên, vì BH được tính lại trên cả family.

## G. Old vs corrected comparison

| Metric | Old manuscript Δ | Corrected Δ | Old p | Corrected p | Old `r_rb` | Corrected `r_rb` | Old CI 95% | Corrected CI 95% | Old q | Corrected q |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: |
| Mean CC | −0.03387057 | −0.02770511 | 0.02148438 | 0.02664185 | −0.580952 | −0.561905 | [−0.05946483, −0.00434826] | [−0.05089818, +0.00640015] | 0.03759767 | 0.04662323 |
| Mean NRMSE | +0.02942366 | +0.03185511 | 0.00729561 | 0.01531219 | +0.666667 | +0.609524 | [+0.00465115, +0.05302103] | [+0.00019319, +0.05187084] | 0.02553464 | 0.04662323 |

**Classification: materially changes inferential support.** Hướng của cả hai metric vẫn như dự kiến, nhưng độ lớn |Δ| của CC giảm **18.2%**, NRMSE tăng **8.3%**; `r_rb` yếu hơn và q của cả hai tiến sát 0.05. Đặc biệt, percentile CI của **Mean CC hiện chứa 0** dù Wilcoxon q<0.05; hai số đo nói về đối tượng thống kê khác nhau và không được diễn giải như cùng một phép kiểm định. Mean NRMSE CI vẫn trên 0 nhưng cận dưới chỉ `+0.000193`. Vì vậy phải cập nhật bảng và câu chữ manuscript; không được giữ CI/p/q cũ.

## H. Downstream impact audit

| Phạm vi / file cụ thể | Cách gộp hoặc phụ thuộc | Quyết định |
| --- | --- | --- |
| `results/simplex_projection/summary/processed_simplex_summary.csv` | Median per horizon, nguồn trung gian; không phải bảng primary session-state. | **Definitely unaffected** như dữ liệu horizon cũ; không dùng trực tiếp làm canonical paired input. |
| `main/prediction_nonlinear.ipynb`; `outputs/prediction/prediction_state_paired_values_60s_processed.csv`, `prediction_state_comparison_60s_processed.csv` | B ở bước paired; chứa mọi số prediction primary cũ. | **Must be regenerated** theo A từ bảng window mới; giữ file cũ làm legacy cho đến khi propagation được duyệt/triển khai. |
| `main/bh_fdr.ipynb`; `outputs/bh_fdr/rq2_primary_bh_fdr_60s_processed.csv`, `rq2_primary_bh_fdr_conclusion.md` | Dùng hai raw p và hai paired vector cũ. | **Must be regenerated**; bảng 7 p/q mới đã lưu riêng ở mục F. |
| `outputs/bh_fdr/rq2_reverse_direction_sessions_60s_processed.csv`, `rq2_sensitivity_excluding_sessions_09_13_60s_processed.csv`; các cell liên quan trong `main/bh_fdr.ipynb` | Dùng paired Δ cũ; reverse-session nhóm có thể đổi. | **Must be regenerated** nếu giữ các phân tích này trong manuscript. |
| `main/summary_result.ipynb`; `outputs/final/paired_awake_drowsy_7metrics_final.png/.pdf` | Figure đọc paired CSV cũ. | **Must be regenerated**. |
| `main/robust_window.ipynb`; `outputs/robust_window/robust_window_{session_state_values,session_deltas,summary,cross_duration_summary,final_evidence}*`, figure/conclusion và nhánh exclude S09/S13 | Prediction 60/120/180 s dùng B; 30 s đã dùng A. | **Must be regenerated** cho prediction 60/120/180 và các kết luận/figure đối chiếu duration; 30 s estimator **definitely unaffected**. RQA/LLE không cần tính estimator lại. |
| `verification_result/verification_data/label_sensitive_validation.ipynb`; phần P0, tỷ lệ magnitude, plot và `verification_result/summary.md` | T30/T60/S3/S5 có `Mean_CC`/`Mean_NRMSE` theo A; P0 tải paired **B** và còn assert số cũ. | **Must be regenerated** ở baseline/comparison/plot/text; các estimator và p/q của 4 rule **definitely unaffected**. Không dùng q family 4 để thay q primary family 7. |
| `verification_result/verification_ntsa_parameter/verification_phase_space_reconstruction.ipynb`, `verification_prediction.ipynb` | Delay τ và dimension m dùng A: mean trong window rồi median session-state; nominal khớp bảng mới. | **Definitely unaffected** cho estimator và statistics trong family 4; **must be checked** khi diễn giải hoặc sao chép q sang bảng primary family 7. Không cần rerun estimator. |
| `results/simplex_projection/theiler_sensitive/processed_theiler_sensitivity_summary.csv`; phần calibration trong `notebook/simplex_projection.ipynb` | Chọn W từ thay đổi các đường CC/NRMSE theo horizon và support; **không tính paired metric theo A hoặc B**. | **Definitely unaffected** về lựa chọn W=1.0 s; không rerun Theiler calibration. Các state-effect cũ khác trong notebook là **obsolete/deprecated** cho primary mới. |
| `phase1/conclusion/RQ2.md`, `outputs/robust_window/robust_window_conclusion.md`, `verification_result/summary.md`, các bảng/text manuscript ngoài repo | Có câu khẳng định độ bền qua duration hoặc các số P0 cũ. Không tìm thấy file manuscript `.docx`/`.tex` trong workspace; chỉ thấy kết quả xuất PDF/Markdown/CSV. | **Must be checked/updated** theo corrected primary và robustness sau khi propagation; không thể sửa bản thảo ngoài workspace tại bước này. |
| `outputs/prediction/prediction_horizon_60s_processed.*`, `outputs/rqa/*`, `outputs/lle/*` | Đường theo horizon hoặc estimator không thuộc hai paired prediction metric. | **Definitely unaffected** bởi đổi aggregation. |

Kết luận về rerun robustness: **window-length prediction 60/120/180 s phải tính lại theo A** trước khi tiếp tục dùng kết luận so sánh duration; **label-rule estimators** và **embedding τ/m estimators** đã theo A nên không cần chạy lại, nhưng baseline P0/diễn giải phải sửa; **Theiler calibration** không dùng A/B và không cần chạy lại. Phân loại này dựa trên code/nguồn đã kiểm tra, không dựa vào p-value.

## I. Canonical prediction source

Dùng duy nhất [primary_simplex_session_paired_60s_processed_P0_v1.csv](../primary_simplex_windowfirst_v1/primary_simplex_session_paired_60s_processed_P0_v1.csv) cho hai vector prediction của sensitivity experiment. Không lấy hai cột prediction từ ba bảng legacy trong audit cũ. [manifest.json](../primary_simplex_windowfirst_v1/manifest.json) ghi 28 source SHA-256 (gồm producer, notebook/core, index và 20 NPZ), 5 output SHA-256, protocol, 18 horizons, QC, seed, thống kê, session ordering, tolerance, môi trường và UTC timestamp. SHA-256 bảng canonical: `58d33e413b4f7582ebb0b8627efd3712ab218ed8b210c2263abc06fd361ce90c`. Mã producer chỉ ghi vào thư mục version `primary_simplex_windowfirst_v1`, từ chối overwrite bản đã freeze.

## J. Final readiness verdict

**Are Mean CC and Mean NRMSE now sufficiently validated and frozen for use in the unknown repeated-session dependence sensitivity experiment? YES.** Hai vector dùng đúng estimand A, đầy đủ 20 session, QC/P0/horizon được xác minh và có provenance tới mức window và source hash. Đây là quyết định về **data readiness của hai metric prediction**; các output manuscript/robustness bị ảnh hưởng còn phải được cập nhật, và protocol ngẫu nhiên cho sensitivity experiment phải được pre-register trước khi chạy. Chưa thực hiện ghép cặp pseudo-subject.
