# =============================================================================
# CRP 2002 CORE
# Historical implementation of Marwan & Kurths (2002).
#
# Architecture:
#   1. Phase Space      -> embed_time_series()
#   2. Cross Geometry   -> cross-distance / CR matrix
#   3. Lag Scanning     -> diagonal structures P_t(l)
#   4. Quantification   -> RR(t), DET(t), L(t)
#   5. Wrappers         -> run_crp_analysis(), analyze_lagged_interrelations()
#
# Principle: separate cross-recurrence geometry from lag-dependent statistics.
# =============================================================================

import numpy as np
from dataclasses import dataclass
from typing import Dict, Any

# ==========================================
# 1. TẦNG PHASE SPACE (KHÔNG GIAN PHA)
# ==========================================

def embed_time_series(signal: np.ndarray, m: int, tau: int) -> np.ndarray:
    """
    Tái dựng chuỗi thời gian 1D thành quỹ đạo không gian pha m chiều.
    
    Args:
        signal (np.ndarray): Chuỗi thời gian 1D.
        m (int): Chiều nhúng (embedding dimension).
        tau (int): Độ trễ thời gian (time delay).
        
    Returns:
        np.ndarray: Ma trận quỹ đạo kích thước (N - (m-1)*tau, m).
    """
    if m < 1:
        raise ValueError("Chiều nhúng m phải >= 1.")
    if tau < 1:
        raise ValueError("Độ trễ tau phải >= 1.")
        
    signal = np.asarray(signal)
    n_points = len(signal) - (m - 1) * tau
    
    if n_points <= 0:
        raise ValueError("Chiều dài tín hiệu không đủ để nhúng với m và tau đã chọn.")
    
    # Kỹ thuật vector hóa với advanced indexing
    row_indices = np.arange(n_points).reshape(-1, 1)
    col_indices = np.arange(m) * tau
    idx_matrix = row_indices + col_indices
    
    return signal[idx_matrix]


# ==========================================
# 2. TẦNG CROSS GEOMETRY (HÌNH HỌC CHÉO)
# ==========================================

def compute_cross_distance_matrix(X: np.ndarray, Y: np.ndarray, metric: str = 'euclidean') -> np.ndarray:
    """
    Tính ma trận khoảng cách chéo giữa hai quỹ đạo (phiên bản numpy thuần).
    
    Args:
        X (np.ndarray): Quỹ đạo hệ thống 1, kích thước (N_x, m).
        Y (np.ndarray): Quỹ đạo hệ thống 2, kích thước (N_y, m).
        metric (str): Loại khoảng cách.
        
    Returns:
        np.ndarray: Ma trận khoảng cách kích thước (N_x, N_y).
    """
    if X.shape[1] != Y.shape[1]:
        raise ValueError("Hai không gian pha không cùng số chiều (m), không thể so sánh.")
        
    if metric != 'euclidean':
        raise NotImplementedError("Phiên bản V1 chỉ hỗ trợ khoảng cách euclidean.")
    
    # Broadcasting khoảng cách: (N_x, 1, m) - (1, N_y, m) -> (N_x, N_y, m)
    diff = X[:, np.newaxis, :] - Y[np.newaxis, :, :]
    return np.linalg.norm(diff, axis=-1)


def compute_cross_recurrence_matrix(D: np.ndarray, epsilon: float, variable_radius: bool = False) -> np.ndarray:
    """
    Nhị phân hóa ma trận khoảng cách thành ma trận CRP.
    
    Args:
        D (np.ndarray): Ma trận khoảng cách.
        epsilon (float): Ngưỡng lân cận.
        variable_radius (bool): Chế độ bán kính biến thiên.
        
    Returns:
        np.ndarray: Ma trận nhị phân uint8.
    """
    if epsilon <= 0:
        raise ValueError("Ngưỡng epsilon phải lớn hơn 0.")
        
    if variable_radius:
        raise NotImplementedError("Tính năng variable_radius chưa được hỗ trợ trong phiên bản này.")
    
    return (D <= epsilon).astype(np.uint8)


# ==========================================
# 3. TẦNG LAG SCANNING (TRÍCH XUẤT ĐỘ TRỄ)
# ==========================================

def extract_lagged_diagonal_lengths(CR: np.ndarray, lag_t: int) -> np.ndarray:
    """
    Trích xuất mảng độ dài các đoạn đường chéo liên tục tại một mốc trễ t.
    Quy ước lag: t > 0 là nửa trên, t < 0 là nửa dưới của ma trận.
    
    Args:
        CR (np.ndarray): Ma trận hồi quy chéo nhị phân.
        lag_t (int): Khoảng cách (độ trễ) so với đường chéo chính.
        
    Returns:
        np.ndarray: Mảng 1D (int32) chứa các giá trị độ dài đường chéo.
    """
    # Ép kiểu sang int32 ngay khi trích xuất để tránh underflow uint8 ở bước np.diff
    diag = np.diagonal(CR, offset=lag_t).astype(np.int32)
    
    # Fast path: Nếu đường chéo không có điểm hồi quy nào
    if not np.any(diag):
        return np.array([], dtype=np.int32)
    
    # Padding 0 để đảm bảo phát hiện được cả điểm bắt đầu/kết thúc sát biên
    padded = np.pad(diag, (1, 1), mode='constant', constant_values=0)
    
    # np.diff trên mảng int32: 1 là bắt đầu, -1 là kết thúc
    diffs = np.diff(padded)
    
    starts = np.where(diffs == 1)[0]
    ends = np.where(diffs == -1)[0]
    
    lengths = ends - starts
    
    return lengths.astype(np.int32)

# ==========================================
# 4. TẦNG LAG QUANTIFICATION (LƯỢNG HÓA THEO ĐỘ TRỄ)
# ==========================================

def calculate_rr(diag_lengths: np.ndarray, N_t: int) -> float:
    """
    Tính Tỷ lệ hồi quy (Recurrence Rate) tại độ trễ t.
    
    Args:
        diag_lengths (np.ndarray): Mảng độ dài các đường chéo.
        N_t (int): Chiều dài tối đa của đường chéo tại độ trễ t.
        
    Returns:
        float: Giá trị RR(t).
    """
    if N_t <= 0:
        return 0.0
    return float(np.sum(diag_lengths) / N_t)


def calculate_det(diag_lengths: np.ndarray, l_min: int) -> float:
    """
    Tính Tính xác định (Determinism) tại độ trễ t.
    
    Args:
        diag_lengths (np.ndarray): Mảng độ dài các đường chéo.
        l_min (int): Độ dài tối thiểu của đường chéo hợp lệ.
        
    Returns:
        float: Giá trị DET(t).
    """
    total_points = np.sum(diag_lengths)
    if total_points == 0:
        return 0.0
    
    valid_lines = diag_lengths[diag_lengths >= l_min]
    return float(np.sum(valid_lines) / total_points)


def calculate_l(diag_lengths: np.ndarray, l_min: int) -> float:
    """
    Tính Độ dài đường chéo trung bình (L) tại độ trễ t.
    
    Args:
        diag_lengths (np.ndarray): Mảng độ dài các đường chéo.
        l_min (int): Độ dài tối thiểu của đường chéo hợp lệ.
        
    Returns:
        float: Giá trị L(t).
    """
    valid_lines = diag_lengths[diag_lengths >= l_min]
    if len(valid_lines) == 0:
        return 0.0
        
    return float(np.mean(valid_lines))


def compute_lagged_metrics(CR: np.ndarray, max_lag_T: int, l_min: int):
    """
    Quét qua các mốc trễ t và tính RR, DET, L.
    
    Args:
        CR (np.ndarray): Ma trận CRP nhị phân (vuông N x N).
        max_lag_T (int): Độ trễ tối đa cần khảo sát.
        l_min (int): Độ dài đường chéo tối thiểu.
        
    Returns:
        tuple: (lags, RR_curve, DET_curve, L_curve).
    """
    n_rows, n_cols = CR.shape
    if n_rows != n_cols:
        raise ValueError("Yêu cầu ma trận CRP vuông (equal-length).")
        
    N = n_rows
    if max_lag_T >= N:
        raise ValueError("max_lag_T phải nhỏ hơn kích thước ma trận N.")
    if max_lag_T < 0:
        raise ValueError("max_lag_T phải >= 0.")
    if l_min < 1:
        raise ValueError("l_min phải >= 1.")

    lags = np.arange(-max_lag_T, max_lag_T + 1)
    num_lags = len(lags)
    
    RR_curve = np.zeros(num_lags, dtype=np.float64)
    DET_curve = np.zeros(num_lags, dtype=np.float64)
    L_curve = np.zeros(num_lags, dtype=np.float64)
    
    for i, lag_t in enumerate(lags):
        N_t = N - abs(lag_t)
        
        # Trích xuất độ dài đường chéo
        diag_lengths = extract_lagged_diagonal_lengths(CR, lag_t)
        
        # Lượng hóa chỉ số (các hàm tự xử lý mảng rỗng)
        RR_curve[i] = calculate_rr(diag_lengths, N_t)
        DET_curve[i] = calculate_det(diag_lengths, l_min)
        L_curve[i] = calculate_l(diag_lengths, l_min)
            
    return lags, RR_curve, DET_curve, L_curve

# ==========================================
# 5. TẦNG RESULT (ĐÓNG GÓI KẾT QUẢ)
# ==========================================

@dataclass
class CRPResult:
    """
    Dataclass lưu trữ kết quả lượng hóa của phân tích CRP.
    """
    lags: np.ndarray
    RR: np.ndarray
    DET: np.ndarray
    L: np.ndarray
    metadata: Dict[str, Any]


# ==========================================
# 6. TẦNG WRAPPERS (GIAO DIỆN VẬN HÀNH)
# ==========================================

def run_crp_analysis(
    signal_x: np.ndarray, 
    signal_y: np.ndarray, 
    m: int, 
    tau: int, 
    epsilon: float, 
    l_min: int, 
    max_lag_T: int, 
    reverse_y: bool = False
) -> CRPResult:
    """
    Vận hành luồng phân tích CRP từ chuỗi thời gian thô đến các chỉ số RQA.
    
    Args:
        signal_x (np.ndarray): Chuỗi thời gian hệ thống 1.
        signal_y (np.ndarray): Chuỗi thời gian hệ thống 2.
        m (int): Chiều nhúng.
        tau (int): Độ trễ thời gian.
        epsilon (float): Ngưỡng lân cận.
        l_min (int): Độ dài đường chéo tối thiểu.
        max_lag_T (int): Giới hạn quét độ trễ.
        reverse_y (bool): Nếu True, đảo dấu chuỗi Y để quét liên kết nghịch.
        
    Returns:
        CRPResult: Đối tượng chứa trục lags, các đường cong chỉ số và metadata.
    """
    # 1. Tiền xử lý dấu (trước khi nhúng)
    sig_y = -np.asarray(signal_y) if reverse_y else np.asarray(signal_y)
    sig_x = np.asarray(signal_x)
    
    # 2. Nhúng không gian pha
    X = embed_time_series(sig_x, m, tau)
    Y = embed_time_series(sig_y, m, tau)
    
    # Validation tường minh thay vì tự động cắt (silent truncation)
    if X.shape[0] != Y.shape[0]:
        raise ValueError("Phiên bản CRP 2002 reproduction yêu cầu hai quỹ đạo có cùng độ dài.")
    
    N_phase_space = X.shape[0]
    
    # 3. Hình học chéo
    D = compute_cross_distance_matrix(X, Y)
    CR = compute_cross_recurrence_matrix(D, epsilon)
    
    # 4. Lượng hóa theo độ trễ
    lags, rr, det, l_avg = compute_lagged_metrics(CR, max_lag_T, l_min)
    
    # 5. Đóng gói kết quả
    metadata = {
        "m": m,
        "tau": tau,
        "epsilon": epsilon,
        "l_min": l_min,
        "max_lag_T": max_lag_T,
        "reverse_y": reverse_y,
        "N_phase_space": N_phase_space
    }
    
    return CRPResult(lags=lags, RR=rr, DET=det, L=l_avg, metadata=metadata)


def analyze_lagged_interrelations(
    signal_x: np.ndarray, 
    signal_y: np.ndarray, 
    config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Phân tích toàn diện các mối liên đới động lực học theo độ trễ (thuận và nghịch).
    
    Args:
        signal_x (np.ndarray): Chuỗi thời gian hệ thống 1.
        signal_y (np.ndarray): Chuỗi thời gian hệ thống 2.
        config (Dict[str, Any]): Chứa m, tau, epsilon, l_min, max_lag_T.
        
    Returns:
        Dict[str, Any]: Bộ kết quả chứa trục lags, các curves thuận/nghịch và metadata chung.
    """
    m = config['m']
    tau = config['tau']
    epsilon = config['epsilon']
    l_min = config['l_min']
    max_lag_T = config['max_lag_T']
    
    # Phân tích liên kết thuận
    result_pos = run_crp_analysis(
        signal_x, signal_y, m, tau, epsilon, l_min, max_lag_T, reverse_y=False
    )
    
    # Phân tích liên kết nghịch
    result_neg = run_crp_analysis(
        signal_x, signal_y, m, tau, epsilon, l_min, max_lag_T, reverse_y=True
    )
    
    # Hợp nhất metadata, loại bỏ trường reverse_y để tránh gây nhầm lẫn
    combined_metadata = {
        "m": m,
        "tau": tau,
        "epsilon": epsilon,
        "l_min": l_min,
        "max_lag_T": max_lag_T,
        "N_phase_space": result_pos.metadata["N_phase_space"]
    }
    
    return {
        "lags": result_pos.lags,
        "positive": {
            "RR": result_pos.RR,
            "DET": result_pos.DET,
            "L": result_pos.L
        },
        "negative": {
            "RR": result_neg.RR,
            "DET": result_neg.DET,
            "L": result_neg.L
        },
        "metadata": combined_metadata
    }