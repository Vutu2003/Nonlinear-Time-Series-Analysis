# Phase 1: Reproducible PPG Data Pipeline

Tài liệu này hướng dẫn tái tạo dữ liệu đã xử lý và dữ liệu segmentation từ
raw PPG. Người dùng chỉ cần chạy các script trong `main/`; toàn bộ xử lý khoa
học được thực hiện bởi các core đã freeze trong `src/`.

## 1. Pipeline

```text
dataset/dhdata/*.csv
        |
        v
main/run_preprocessing.py
        |
        v
data_processed/dhdata/*.csv
        |
        v
main/run_segmentation.py
        |
        v
segmentated_data/dhdata/*.npz
segmentated_data/dhdata/segments_index.csv
```

Hai script hiện có thể chạy:

| Script | Chức năng |
|---|---|
| `run_preprocessing.py` | Lọc PPG, phát hiện motion artifact và lưu SQI |
| `run_segmentation.py` | Segment, tính quasi-stationarity và export NPZ/index |

`run_ntsa.py` và `run_all.py` hiện là placeholder, chưa có workflow thực thi.
Không dùng hai file này để tái tạo dataset ở thời điểm hiện tại.

## 2. Yêu cầu môi trường

- Python 3.12 được khuyến nghị; pipeline đã được kiểm tra với Python 3.12.7.
- Raw dataset đã được đặt trong `phase1/dataset/dhdata/`.
- Chạy lệnh từ thư mục gốc của repository.

Ví dụ cấu trúc tối thiểu:

```text
Nonlinear-Time-Series-Analysis/
├── requirements.txt
└── phase1/
    ├── dataset/dhdata/
    │   ├── sample_1.csv
    │   └── ...
    ├── main/
    └── src/
```

Mỗi raw CSV phải có ít nhất các cột:

```text
Time (s)
IR Value raw
Label
```

Một file tương ứng với một session. `Label=0` là Awake và `Label=1` là
Drowsy.

## 3. Cài đặt

Mở PowerShell tại thư mục gốc của repository:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Kiểm tra Python đang dùng:

```powershell
python --version
python -c "import numpy, pandas, scipy; print('Dependencies OK')"
```

Nếu dùng Conda, có thể thay bước tạo môi trường bằng:

```powershell
conda create -n ntsa python=3.12
conda activate ntsa
python -m pip install -r requirements.txt
```

## 4. Bước 1: chạy preprocessing

Từ thư mục gốc của repository, chạy:

```powershell
python phase1/main/run_preprocessing.py
```

Script thực hiện độc lập trên từng session:

1. Load raw CSV bằng `load_session()`.
2. Ước lượng sampling rate từ `Time (s)`.
3. Chạy `preprocess_ppg()` trên `IR Value raw`.
4. Chạy `detect_motion_artifacts()` trên PPG đã xử lý.
5. Kiểm tra số sample, alignment, dữ liệu hữu hạn và kiểu boolean của SQI.
6. Export processed CSV.

Tham số đã freeze:

| Thành phần | Tham số |
|---|---|
| Butterworth bandpass | `0.5-8.0 Hz`, order `2`, zero-phase |
| SQI | window `5.0 s`, threshold `4.5` |

Output mặc định:

```text
phase1/data_processed/dhdata/*.csv
```

Mỗi processed CSV có đúng các cột:

```text
Time (s)
IR Value raw
PPG processed
Label
SQI
```

`SQI=True` đánh dấu sample thuộc vùng motion artifact. Script không thay đổi
số sample, `Time (s)`, `IR Value raw` hoặc `Label`.

Khi hoàn tất, log phải báo số session thành công/thất bại cùng tổng số sample
và local window bị SQI đánh dấu. Exit code `0` nghĩa là toàn bộ preprocessing
thành công; exit code `1` nghĩa là pipeline đã dừng do lỗi.

## 5. Bước 2: chạy segmentation

Chỉ chạy bước này sau khi preprocessing hoàn tất:

```powershell
python phase1/main/run_segmentation.py
```

Script thực hiện:

1. Load từng processed CSV.
2. Ước lượng sampling rate riêng cho session.
3. Chạy `segment_session()` cho window 60, 120 và 180 giây.
4. Reject window cross-label, overlap SQI hoặc chứa acquisition gap.
5. Tính quasi-stationarity riêng cho Raw và Processed PPG.
6. Export một NPZ cho mỗi session và tạo global index.
7. Đối chiếu toàn bộ NPZ với `segments_index.csv`.

Tham số đã freeze:

| Thành phần | Tham số |
|---|---|
| Analysis windows | `60`, `120`, `180 s` |
| Acquisition gap | factor `1.5` |
| Quasi-stationarity | sub-window `10.0 s`, threshold `0.5` |

Output mặc định:

```text
phase1/segmentated_data/dhdata/
├── sample_1.npz
├── sample_4.npz
├── ...
└── segments_index.csv
```

Raw và Processed PPG trong cùng một hàng luôn dùng cùng interval. Window không
bị xóa chỉ vì fail quasi-stationarity; score và pass flag được lưu riêng cho
hai representation để downstream NTSA tự lọc.

## 6. Kết quả canonical cần thu được

Với dataset `dhdata` gồm 20 session, `run_segmentation.py` mặc định chỉ thành
công khi kết quả khớp toàn bộ canonical counts:

| Window | Số lượng |
|---:|---:|
| 60 s | 951 |
| 120 s | 432 |
| 180 s | 254 |
| Tổng | 1637 |

Stationarity pass counts:

| Representation | Pass |
|---|---:|
| Raw PPG | 1398 |
| Processed PPG | 1544 |

Log cuối cùng cần chứa:

```text
Completed: success=20, failed=0, windows=1637
Stationarity pass: Raw=1398, Processed=1544
```

Nếu số liệu không khớp, script trả exit code `1` và không công nhận output là
canonical.

## 7. Chạy với đường dẫn khác

Cả hai script chấp nhận input/output tùy chỉnh. Đặt đường dẫn có khoảng trắng
trong dấu nháy kép.

```powershell
python phase1/main/run_preprocessing.py `
    --input-dir "path/to/raw" `
    --output-dir "path/to/processed"

python phase1/main/run_segmentation.py `
    --input-dir "path/to/processed" `
    --output-dir "path/to/segmented"
```

Xem toàn bộ CLI options:

```powershell
python phase1/main/run_preprocessing.py --help
python phase1/main/run_segmentation.py --help
```

Khi thử trên dataset không phải canonical `dhdata`, bỏ kiểm tra canonical
counts nhưng vẫn giữ validation schema và alignment:

```powershell
python phase1/main/run_segmentation.py `
    --input-dir "path/to/processed" `
    --output-dir "path/to/segmented" `
    --skip-canonical-counts
```

Không dùng `--skip-canonical-counts` khi mục tiêu là tái tạo kết quả chính thức
của nghiên cứu.

## 8. Cơ chế an toàn khi export

- Dữ liệu được tạo trong staging directory trước khi thay thế output chính.
- Nếu một session lỗi, staging output bị hủy và dataset chính không được cập
  nhật bởi lần chạy đó.
- File cùng tên được thay thế sau khi toàn bộ session pass validation.
- Script dừng nếu output directory chứa CSV hoặc NPZ không tương ứng với input.
- Script không padding, interpolation hoặc resampling tín hiệu.

Nếu cần giữ một phiên bản output cũ, hãy sao lưu directory đó trước khi chạy
lại pipeline.

## 9. Kiểm tra nhanh sau khi chạy

PowerShell:

```powershell
(Get-ChildItem phase1/data_processed/dhdata -Filter *.csv).Count
(Get-ChildItem phase1/segmentated_data/dhdata -Filter *.npz).Count
(Import-Csv phase1/segmentated_data/dhdata/segments_index.csv).Count
```

Kết quả canonical lần lượt phải là:

```text
20
20
1637
```

Schema chi tiết và cách sử dụng segmented dataset được mô tả tại
`segmentated_data/dhdata/infomation.md`.

## 10. Xử lý lỗi thường gặp

### `No CSV files found`

Kiểm tra raw/processed CSV đã nằm đúng directory hoặc truyền lại
`--input-dir`.

### `Missing required columns`

Kiểm tra chính xác tên cột, bao gồm `Time (s)`, `IR Value raw`, `Label`; ở bước
segmentation phải có thêm `PPG processed` và `SQI`.

### `Output directory contains unexpected ... files`

Output đang chứa session không có trong input. Di chuyển file dư sang nơi sao
lưu hoặc chọn một output directory trống, sau đó chạy lại.

### `Non-canonical ... count`

Kiểm tra đúng raw dataset, đủ 20 session, đúng phiên bản code và không thay đổi
tham số freeze. Không bỏ qua lỗi này khi tái tạo kết quả nghiên cứu.

### PowerShell không cho activate virtual environment

Có thể chạy trực tiếp bằng Python của Conda hoặc gọi Python trong virtual
environment bằng đường dẫn đầy đủ, thay vì thay đổi execution policy của máy.

## 11. Ghi nhận để đảm bảo tái tạo

Khi báo cáo hoặc chia sẻ một lần chạy, nên lưu cùng kết quả:

- Git commit hoặc phiên bản source code.
- Phiên bản Python và `requirements.txt`.
- Danh sách raw session đầu vào.
- Command đã chạy và toàn bộ log.
- `segments_index.csv` sau export.

Không sửa scientific logic trong `main/`. Thay đổi thuật toán phải được kiểm
định tại core tương ứng trong `src/` trước khi cập nhật pipeline freeze.
