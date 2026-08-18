import numpy as np

# Định nghĩa toán học
#
# Gọi x_i[n] là mẫu thứ n trong cửa sổ PPG cục bộ thứ i,
# với i = 1, 2, ..., N và n là chỉ số mẫu trong cửa sổ đó.
#
# 1. Biên độ robust của cửa sổ
#
# A_i = Q_0.95(x_i) - Q_0.05(x_i)
#
# Trong đó:
#   A_i      = biên độ robust của cửa sổ i
#   Q_0.95   = phân vị 95%
#   Q_0.05   = phân vị 5%
#
# Dùng phân vị thay cho max-min để giảm ảnh hưởng của
# một vài mẫu cực trị đơn lẻ.
#
# 2. Độ gồ ghề cục bộ của waveform
#
# R_i = sqrt(mean((x_i[n] - x_i[n - 1])^2))
#
# Trong đó:
#   R_i      = RMS của sai phân bậc nhất trong cửa sổ i
#   x_i[n]   = mẫu PPG hiện tại
#   x_i[n-1] = mẫu PPG trước đó
#
# R_i lớn cho thấy waveform thay đổi cục bộ nhanh bất thường.
#
# 3. Chuẩn hóa robust theo từng session
#
# Với mỗi đặc trưng F_i, trong đó F là A hoặc R:
#
# median_F = median(F_1, F_2, ..., F_N)
#
# MAD_F = median(|F_i - median_F|)
#
# z_i = 0.6745 * (F_i - median_F) / MAD_F
#
# Trong đó:
#   MAD_F = median absolute deviation của đặc trưng F
#   z_i   = modified robust z-score của cửa sổ i
#
# Hằng số 0.6745 giúp điểm MAD-based có thang đo gần tương đương
# với z-score chuẩn khi dữ liệu xấp xỉ phân phối chuẩn.
#
# 4. Quy tắc phát hiện motion artifact
#
# Cửa sổ i được đánh dấu artifact nếu:
#
#     z_A,i > threshold
#     hoặc
#     z_R,i > threshold
#
# Ngược lại:
#
#     artifact_i = False
#
# Chỉ xét các sai lệch dương lớn vì giả thuyết hiện tại là
# motion artifact làm tăng bất thường biên độ cục bộ và/hoặc
# độ gồ ghề của waveform.
#
# Cuối cùng, tất cả các sample thuộc cửa sổ artifact
# được đánh dấu True trong sample-level artifact mask.

def detect_motion_artifacts(
    signal: np.ndarray,
    fs: float,
    window_s: float = 5.0,
    threshold: float = 3.5,
) -> np.ndarray:
    """Detect motion-artifact regions using robust local features."""

    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be a 1D array.")

    if fs <= 0 or window_s <= 0:
        raise ValueError("fs and window_s must be greater than 0.")

    if not np.isfinite(signal).all():
        raise ValueError("signal must contain only finite values.")

    window_samples = max(2, int(round(window_s * fs)))
    windows = []

    # Extract local amplitude and roughness.
    for start in range(0, len(signal), window_samples):
        end = min(start + window_samples, len(signal))
        segment = signal[start:end]

        if len(segment) < 2:
            continue

        amplitude = np.quantile(segment, 0.95) - np.quantile(segment, 0.05)
        roughness = np.sqrt(np.mean(np.diff(segment) ** 2))

        windows.append((start, end, amplitude, roughness))

    features = np.array([
        [amplitude, roughness]
        for _, _, amplitude, roughness in windows
    ])

    median = np.median(features, axis=0)
    mad = np.median(np.abs(features - median), axis=0)
    mad = np.maximum(mad, np.finfo(float).eps)

    # Modified robust z-score.
    scores = 0.6745 * (features - median) / mad

    artifact_windows = np.any(scores > threshold, axis=1)

    artifact_mask = np.zeros(len(signal), dtype=bool)

    for (start, end, _, _), is_artifact in zip(
        windows,
        artifact_windows,
    ):
        if is_artifact:
            artifact_mask[start:end] = True

    return artifact_mask