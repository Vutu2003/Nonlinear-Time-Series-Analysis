# Ghi chú sau Data Audit

- Mapping nhãn cố định:
  - `0 = Awake`
  - `1 = Drowsy`

- Các cột chính `Time (s)`, `IR Value raw`, `Label` không có null đáng kể trong các session đã kiểm tra.

- Không phát hiện:
  - duplicate rows;
  - duplicate timestamps;
  - non-monotonic timestamps;
  - invalid labels.

- Sampling rate không đồng nhất:
  - `sample_1.csv`: khoảng `50 Hz`;
  - phần lớn session còn lại: khoảng `25 Hz`.

- Không được hard-code một sampling rate duy nhất cho toàn bộ dataset.

- Các session 25 Hz có một số ít time gaps (`~2–8` gaps/session).
  - Cần kiểm tra vị trí và độ lớn gap trước preprocessing.
  - Không để window NTSA đi qua acquisition gap.
  - Không tự động interpolate gap nếu chưa có rule rõ ràng.

- `sample_1.csv` có cột `Unnamed: 2` rỗng hoàn toàn; không ảnh hưởng các cột dữ liệu chính.

- `sample_2.csv` được loại khỏi primary analysis do sampling rate bất thường.

- Window availability hiện được đánh giá tại:
  - `60 s`
  - `120 s`
  - `180 s`
  - `240 s`
  - `300 s`

- Trước preprocessing cần chốt:
  1. cách sử dụng / harmonize sampling rate;
  2. cách xử lý time gaps;
  3. rule loại window chứa acquisition anomaly.