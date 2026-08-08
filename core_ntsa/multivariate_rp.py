# =============================================================================
# MULTIVARIATE RECURRENCE PLOT — Romano et al. (2004)
#
# Architecture:
#   1. Independent Phase Spaces
#   2. Independent Recurrence Geometry
#   3. Joint Recurrence
#   4. Joint Diagonal Statistics
#   5. K2 Estimation
#   6. Result / Wrapper
#   7. Historical Automation
#
# Core flow:
#   X, Y -> Rx, Ry -> JR -> diagonal lengths -> P(l) -> K2
# =============================================================================


import numpy as np
from scipy.spatial.distance import pdist, squareform


# ==========================================
# 1. TẦNG INDEPENDENT PHASE SPACE
# ==========================================

def embed_time_series(signal: np.ndarray, m: int, tau: int) -> np.ndarray:
    """
    Tái dựng chuỗi 1D thành quỹ đạo không gian pha m chiều.
    Quy ước (Convention): Mỗi trạng thái (embedded state) được neo (anchored) 
    tại mẫu đầu tiên của nó. Nghĩa là X[i] tương ứng với thời điểm i của chuỗi gốc.
    """
    if m < 1 or tau < 1:
        raise ValueError("Chiều nhúng m và độ trễ tau phải >= 1.")
        
    signal = np.asarray(signal)
    n_points = len(signal) - (m - 1) * tau
    
    if n_points <= 0:
        raise ValueError("Chiều dài tín hiệu không đủ để nhúng.")
    
    row_indices = np.arange(n_points).reshape(-1, 1)
    col_indices = np.arange(m) * tau
    
    return signal[row_indices + col_indices]


def align_embedded_trajectories(
    X: np.ndarray, Y: np.ndarray, tx_start: int, ty_start: int
):
    """
    Cắt (trim) hai quỹ đạo để chúng chia sẻ chung một lưới thời gian rời rạc.
    Giả định: Cả hai quỹ đạo có cùng tần số lấy mẫu (sampling interval) 
    và các tham số tx_start, ty_start dùng chung một đơn vị.
    """
    tx_end = tx_start + X.shape[0]
    ty_end = ty_start + Y.shape[0]
    
    common_start = max(tx_start, ty_start)
    common_end = min(tx_end, ty_end)
    
    if common_start >= common_end:
        raise ValueError("Hai quỹ đạo không có khoảng thời gian chồng lấp.")
        
    idx_x_start = common_start - tx_start
    idx_x_end = common_end - tx_start
    idx_y_start = common_start - ty_start
    idx_y_end = common_end - ty_start
    
    X_aligned = X[idx_x_start:idx_x_end]
    Y_aligned = Y[idx_y_start:idx_y_end]
    
    if X_aligned.shape[0] != Y_aligned.shape[0]:
        raise RuntimeError("Alignment thất bại. Độ dài hai quỹ đạo không khớp.")
        
    return X_aligned, Y_aligned


# ==========================================
# 2. TẦNG INDEPENDENT GEOMETRY
# ==========================================

def compute_auto_distance_matrix(
    trajectory: np.ndarray, metric: str = 'euclidean'
) -> np.ndarray:
    """Tính ma trận khoảng cách tự thân cho một quỹ đạo."""
    return squareform(pdist(trajectory, metric=metric))


def find_threshold_for_rr(D: np.ndarray, target_rr: float) -> float:
    """
    Tìm xấp xỉ ngưỡng epsilon cho tỷ lệ hồi quy (RR) mục tiêu.
    Tính toán dựa trên toàn bộ N^2 khoảng cách, bao gồm cả đường chéo chính,
    tuân theo định nghĩa RR của Romano et al. (2004).
    Lưu ý: Do hiện tượng khoảng cách trùng lặp (ties), giá trị RR 
    đạt được thực tế có thể sai lệch nhẹ so với target_rr.
    """
    if not (0.0 < target_rr <= 1.0):
        raise ValueError("target_rr phải nằm trong khoảng (0, 1].")
        
    return float(np.quantile(D, target_rr))


def compute_recurrence_matrix(D: np.ndarray, epsilon: float) -> np.ndarray:
    """Nhị phân hóa ma trận khoảng cách thành ma trận hồi quy."""
    if epsilon < 0:
        raise ValueError("Ngưỡng epsilon không được âm.")
        
    return (D <= epsilon).astype(np.uint8)


# ==========================================
# 3. TẦNG JOINT RECURRENCE
# ==========================================

def compute_joint_recurrence_matrix(
    Rx: np.ndarray, Ry: np.ndarray
) -> np.ndarray:
    """
    Tạo ma trận Joint Recurrence bằng phép giao (logical AND) giữa Rx và Ry.
    """
    if Rx.shape != Ry.shape:
        raise ValueError("Kích thước hai ma trận Rx và Ry không khớp.")
        
    return np.logical_and(Rx, Ry).astype(np.uint8)