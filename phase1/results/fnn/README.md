# Mô tả kết quả FNN

Bốn file dưới đây lưu kết quả False Nearest Neighbors (FNN) ở các mức phân
tích khác nhau. `label` gồm `Awake` và `Drowsy`; `representation` gồm `Raw`
và `Processed`.

## `fnn_curves.csv`

Lưu toàn bộ đường cong FNN của từng cửa sổ, mỗi dòng ứng với một embedding
dimension.

- Khóa cửa sổ: `session`, `window_id`, `window_size_s`, `label`,
  `representation`.
- `dimension`: embedding dimension đang kiểm tra.
- `fnn_percent`: tỷ lệ false nearest neighbors tại dimension đó, đơn vị `%`.
- `valid_count`: số điểm có láng giềng hợp lệ dùng để tính FNN.

## `fnn_sensitivity_results.csv`

Lưu kết quả kiểm tra độ nhạy trên cohort đại diện khi thay đổi từng tham số
FNN.

- `factor`, `factor_value`: tham số được thay đổi và giá trị thử nghiệm.
- `selected_m`: dimension đầu tiên đạt ngưỡng FNN; để trống nếu không tìm thấy.
- `m_found`: cho biết có tìm được `selected_m` trong phạm vi khảo sát hay không.
- Các cột còn lại xác định session, cửa sổ, trạng thái và representation.

## `fnn_session_summary.csv`

Tổng hợp kết quả ở cấp session cho từng tổ hợp kích thước cửa sổ, trạng thái
và representation.

- `n_windows`: tổng số cửa sổ hợp lệ.
- `n_m_found`: số cửa sổ tìm được embedding dimension.
- `median_m`, `iqr_m`, `mode_m`: trung vị, IQR và mode của `selected_m`.
- `m_found_rate_pct`: tỷ lệ cửa sổ tìm được `selected_m`, đơn vị `%`.

## `fnn_window_results.csv`

Kết quả chính ở cấp cửa sổ, mỗi dòng ứng với một cửa sổ và một representation.

- `fs`: tần số lấy mẫu, đơn vị Hz.
- `tau_samples`: embedding delay theo số mẫu.
- `max_m`: dimension lớn nhất được khảo sát.
- `selected_m`: dimension đầu tiên đạt ngưỡng FNN; để trống nếu không tìm thấy.
- `min_fnn_percent`: FNN nhỏ nhất trong phạm vi `1...max_m`, đơn vị `%`.
- `valid_count_at_selected_m`: số láng giềng hợp lệ tại `selected_m`.
- `m_found`: trạng thái tìm thấy `selected_m`.
