import numpy as np
from scipy.spatial.distance import cdist

# ==========================================
# MODULE 1: PHASE SPACE
# ==========================================

def reconstruct_phase_space(signal: np.ndarray, d: int, tau: int) -> np.ndarray:
    """
    Tái dựng không gian pha từ chuỗi tín hiệu 1D bằng phương pháp nhúng trễ.
    """
    if d < 1:
        raise ValueError("Chiều không gian nhúng (d) phải lớn hơn hoặc bằng 1.")
    if tau < 1:
        raise ValueError("Độ trễ thời gian (tau) phải lớn hơn hoặc bằng 1.")

    n = len(signal)
    n_vectors = n - (d - 1) * tau
    
    if n_vectors <= 0:
        raise ValueError("Chiều dài tín hiệu không đủ để nhúng với d và tau đã cho.")
        
    X = np.column_stack([signal[i * tau : n_vectors + i * tau] for i in range(d)])
    
    return X


# ==========================================
# MODULE 2: RECURRENCE MATRIX
# ==========================================

def compute_distance_matrix(X: np.ndarray, metric: str = 'euclidean') -> np.ndarray:
    """
    Tính ma trận khoảng cách chéo (pairwise distance matrix) giữa các vector.
    """
    D = cdist(X, X, metric=metric)
    
    return D

def compute_recurrence_matrix(D: np.ndarray, radius: float) -> np.ndarray:
    """
    Tạo ma trận hồi quy nhị phân từ ma trận khoảng cách dựa trên ngưỡng radius.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
        
    R = (D <= radius).astype(np.int32)
    
    return R