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


