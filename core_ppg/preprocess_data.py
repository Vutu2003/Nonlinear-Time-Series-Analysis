import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def preprocess_ppg(file_path=None, data=None, label_array=None, fs=50.0, lowcut=0.5, highcut=8.0, order=2):
    """
    Tiền xử lý tín hiệu PPG: trích xuất, đảo pha, lọc zero-phase và trực quan hóa.
    Đã vá lỗi: Tự động trích xuất nhãn từ file CSV.
    """
    # 1. Trích xuất dữ liệu
    if file_path:
        df = pd.read_csv(file_path)
        # Xóa khoảng trắng ẩn ở tên cột (phòng ngừa rủi ro Pandas không nhận diện được)
        df.columns = df.columns.str.strip()
        
        time_s = df['Time (s)'].values
        ir_raw = df['IR Value raw'].values
        
        # Bắt buộc lấy Label từ file CSV (Chìa khóa sửa lỗi)
        if 'Label' in df.columns:
            labels = df['Label'].values
        else:
            raise KeyError("Trong file CSV không có cột 'Label'!")
            
    elif data is not None:
        ir_raw = np.array(data)
        time_s = np.arange(len(ir_raw)) / fs
        # Nếu truyền mảng ngoài vào, phải đảm bảo có truyền cả mảng label
        labels = np.array(label_array) if label_array is not None else np.full(len(ir_raw), np.nan)
    else:
        raise ValueError("Yêu cầu cung cấp file_path hoặc mảng data.")

    # 2. Đảo pha quang học
    ir_inverted = -1.0 * ir_raw

    # 3. Lọc Zero-phase Butterworth Bandpass
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')

    ir_filtered = filtfilt(b, a, ir_inverted)

    # 4. Trực quan hóa 15 giây đầu tiên
    plt.figure(figsize=(7, 7))

    plt.subplot(2, 1, 1)
    plt.plot(time_s, ir_inverted, color='gray', linewidth=1.5, label='Inverted PPG')
    plt.title("Tín hiệu PPG đã đảo pha (chưa lọc đường nền)")
    plt.ylabel("Biên độ")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(0, 15)

    plt.subplot(2, 1, 2)
    plt.plot(time_s, ir_filtered, color='blue', linewidth=1.5,
             label=f'Bandpass ({lowcut} - {highcut} Hz)')
    plt.title("Tín hiệu PPG sau bộ lọc Zero-phase")
    plt.xlabel("Thời gian (s)")
    plt.ylabel("Biên độ chuẩn hóa")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(0, 15)

    plt.tight_layout()
    plt.show()

    # 5. Tạo DataFrame output có cột Label ĐÃ ĐƯỢC LẤY CHUẨN XÁC
    output_df = pd.DataFrame({
        "Time (s)": time_s,
        "IR_Inverted": ir_inverted,
        "IR_Filtered": ir_filtered,
        "Label": labels
    })

    return output_df

# ==========================================
# TEST THỰC THI CHUỖI XỬ LÝ
# ==========================================
file_path = "../data/ppg_dataset/mydataset/sample_1.csv"

# 1. Gọi hàm tiền xử lý (Bây giờ nó sẽ tự động lấy Label từ file)
df_ppg = preprocess_ppg(file_path=file_path, lowcut=0.5, highcut=4.0)

# 2. Kiểm tra xem Label đã hết bị None chưa
print("\nKiểm tra dữ liệu nhãn sau khi tiền xử lý:")
print(df_ppg['Label'].value_counts(dropna=False))

# 3. Chạy hàm cắt frame (Dùng hàm V2 ở trên)
# frames_dict = extract_contiguous_frames_v2(df_ppg, signal_col="IR_Filtered", min_length=1000, fs=50.0)

def extract_contiguous_frames_with_time(
    ppg_df: pd.DataFrame,
    time_col: str = "Time (s)",
    signal_col: str = "IR_Filtered",
    min_length: int = 1000,
    fs: float = 50.0
):
    """
    Tách DataFrame thành 2 mảng numpy riêng biệt cho nhãn 0 và nhãn 1.
    Mỗi frame đầu ra là một mảng 2D chứa cả Thời gian (Cột 0) và Tín hiệu (Cột 1).
    """
    if ppg_df.empty:
        raise ValueError("Lỗi: DataFrame đầu vào trống.")
    
    df_clean = ppg_df.copy()
    
    # Kỹ thuật gom nhóm Bulletproof
    group_ids = (df_clean["Label"] != df_clean["Label"].shift(1)).cumsum()
    
    frames_0 = []
    frames_1 = []
    
    for block_id, block in df_clean.groupby(group_ids):
        current_label = block["Label"].iloc[0] 
        
        # Trích xuất riêng rẽ cột Time và cột Tín hiệu
        time_array = block[time_col].values
        signal_array = block[signal_col].values
        
        # Lọc theo độ dài tối thiểu
        if len(signal_array) >= min_length:
            
            # Gộp Time và Signal thành mảng 2D (N hàng x 2 cột)
            frame_data = np.column_stack((time_array, signal_array))
            
            # Ép kiểu an toàn về float để so sánh 
            try:
                numeric_label = float(current_label)
                if numeric_label == 0.0:
                    frames_0.append(frame_data)
                elif numeric_label == 1.0:
                    frames_1.append(frame_data)
            except (ValueError, TypeError):
                continue
            
    # Chuyển đổi thành mảng object numpy
    np_frames_0 = np.array(frames_0, dtype=object)
    np_frames_1 = np.array(frames_1, dtype=object)
            
    # ==================================================
    # IN THỐNG KÊ
    # ==================================================
    def print_stats(frames, label_name):
        print(f"\n{'='*60}")
        print(f"FRAME LABEL = {label_name}")
        print(f"{'='*60}")
        if len(frames) == 0:
            print(f"Không có frame nào đạt yêu cầu > {min_length} điểm.")
            return
            
        info = pd.DataFrame({
            "Frame_ID": np.arange(1, len(frames) + 1),
            "Samples": [len(f) for f in frames],
            "Duration_s": [len(f) / fs for f in frames]
        })
        
        print(info.to_string(index=False))
        total_s = info['Duration_s'].sum()
        print(f"\nTổng số frame: {len(frames)} | Tổng thời gian: {total_s:.2f} s ({total_s/60:.2f} phút)")

    print_stats(np_frames_0, "0 (AWAKE)")
    print_stats(np_frames_1, "1 (DROWSY)")

    return np_frames_0, np_frames_1

# ==========================================
# CÁCH SỬ DỤNG VÀ TRÍCH XUẤT DỮ LIỆU
# ==========================================
frames_awake, frames_drowsy = extract_contiguous_frames_with_time(
    df_ppg, 
    time_col="Time (s)",
    signal_col="IR_Filtered", 
    min_length=100, 
    fs=50.0
)

# Lấy thử frame tỉnh táo đầu tiên để chạy NTSA
if len(frames_awake) > 0:
    first_awake_frame = frames_awake[0]
    
    # Cách bóc tách dữ liệu ra từ mảng 2D:
    # Lấy toàn bộ hàng (:), và lấy cột số 0 cho thời gian
    t_awake = first_awake_frame[:, 0]  
    
    # Lấy toàn bộ hàng (:), và lấy cột số 1 cho tín hiệu
    sig_awake = first_awake_frame[:, 1]
    
    print("\nKiểm tra bóc tách frame đầu tiên:")
    print(f"- Thời gian bắt đầu: {t_awake[0]:.2f}s, Thời gian kết thúc: {t_awake[-1]:.2f}s")
    print(f"- Số điểm dữ liệu tín hiệu: {len(sig_awake)}")


def create_sub_windows(frame_data, window_size, step_size=None):
    """
    Cắt mảng dữ liệu frame lớn thành các cửa sổ con (sub-window).
    
    Args:
        frame_data (np.ndarray): Mảng 2D chứa dữ liệu (ví dụ: N hàng x 2 cột).
        window_size (int): Số điểm dữ liệu cho mỗi cửa sổ.
        step_size (int, optional): Bước trượt của cửa sổ. 
                                   Mặc định bằng window_size (không đè lấp).
        
    Returns:
        list: Danh sách các mảng numpy 2D, mỗi mảng có shape (window_size, 2).
    """
    if step_size is None:
        step_size = window_size
        
    num_samples = len(frame_data)
    sub_windows = []
    
    # Lặp qua mảng dữ liệu và cắt thành các đoạn có kích thước cố định
    for start_idx in range(0, num_samples - window_size + 1, step_size):
        end_idx = start_idx + window_size
        window_data = frame_data[start_idx:end_idx]
        sub_windows.append(window_data)
        
    return sub_windows

# Cấu hình cửa sổ: 1000 điểm (20 giây ở fs=50Hz)
WINDOW_SIZE = 3000

all_awake_sub_windows = []
all_drowsy_sub_windows = []

# Xử lý toàn bộ frame Tỉnh táo
for frame in frames_awake:
    sub_wins = create_sub_windows(frame, window_size=WINDOW_SIZE)
    all_awake_sub_windows.extend(sub_wins)

# Xử lý toàn bộ frame Buồn ngủ
for frame in frames_drowsy:
    sub_wins = create_sub_windows(frame, window_size=WINDOW_SIZE)
    all_drowsy_sub_windows.extend(sub_wins)

# Chuyển thành mảng numpy 3D: (Số lượng cửa sổ, Kích thước cửa sổ, 2 cột)
np_awake_sub_windows = np.array(all_awake_sub_windows)
np_drowsy_sub_windows = np.array(all_drowsy_sub_windows)

print(f"Tổng số snapshots AWAKE thu được: {len(np_awake_sub_windows)}")
print(f"Tổng số snapshots DROWSY thu được: {len(np_drowsy_sub_windows)}")
print(f"Kích thước một snapshot: {np_awake_sub_windows[0].shape}")

ts_data = np_awake_sub_windows[0]
ts_data_drowsiness = np_drowsy_sub_windows[1]
print(f'Len of data: {len(ts_data)}')

time_array = ts_data[:, 0]
ppg_data_awake = ts_data[:, 1]
signal_array = ts_data[:, 1]
time_array_drowsiness = ts_data_drowsiness[:, 0]
ppg_data_drowsiness = ts_data_drowsiness[:, 1]
signal_array_drowsiness = ts_data_drowsiness[:, 1]