"""
============================================================
Recurrence Quantification Analysis (RQA) - Marwan et al. (2002)
============================================================

This module provides a minimal, faithful end-to-end implementation of the 
extended Recurrence Quantification Analysis (RQA) methodology introduced by 
Marwan et al. (2002).

Unlike the classic Webber & Zbilut (1994) framework that exclusively analyzes 
diagonal structures to quantify system predictability (evolution), this module 
introduces a paradigm shift by shifting the statistical object of interest to 
vertical structures in order to quantify laminarity (persistence).

It implements the three core vertical descriptors proposed in 2002:
    • Laminarity (LAM)
    • Trapping Time (TT)
    • Maximal Vertical Length (V_max)

To maintain historical and mathematical fidelity, the architecture explicitly 
branches into two orthogonal quantification paths (Diagonal vs. Vertical) 
derived from the same underlying geometric reservoir.

Data Flow & Conceptual Diagram:
------------------------------------------------------------
[Raw Time Series]
       │
       ▼
 ┌────────────────────────────────────────────────────────┐
 │ MODULE 1: PHASE SPACE RECONSTRUCTION                   │
 │ (Takens' Time Delay Embedding)                         │
 └─────────────────────────┬──────────────────────────────┘
                           │
 ┌─────────────────────────┴──────────────────────────────┐
 │ MODULE 2: RECURRENCE MATRIX                            │
 │ (Distance Matrix -> Heaviside Thresholding)            │
 └─────────────────────────┬──────────────────────────────┘
                           │
         ┌─────────────────┴─────────────────┐
         │ (Paradigm Branching)              │
         ▼                                   ▼
 ┌────────────────────┐              ┌────────────────────┐
 │ MODULE 3           │              │ MODULE 4           │
 │ DIAGONAL SCAN      │              │ VERTICAL SCAN      │
 │ (Webber 1994)      │              │ (Marwan 2002)      │
 ├────────────────────┤              ├────────────────────┤
 │ Extract: P(l)      │              │ Extract: P(v)      │
 │ Metrics:           │              │ Metrics:           │
 │ - DET              │              │ - LAM              │
 │ - L_mean           │              │ - TT               │
 │ - L_max            │              │ - V_max            │
 └───────┬────────────┘              └───────┬────────────┘
         │                                   │
 ┌───────┴────────────┐              ┌───────┴────────────┐
 │ MODULE 5           │              │ MODULE 5           │
 │ WebberResult       │              │ MarwanResult       │
 │ run_webber2002()   │              │ run_marwan2002()   │
 └────────────────────┘              └────────────────────┘

The module provides two wrappers, `run_webber2002()` and `run_marwan2002()`, 
allowing researchers to directly reproduce the comparative experiments 
(Evolution vs. Persistence) presented in Figure 3 of the original paper.
"""


import numpy as np
from scipy.spatial.distance import cdist
from dataclasses import dataclass
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


# =============================================================================
# MODULE 3: DIAGONAL QUANTIFICATION (WEBBER 1994)
# =============================================================================

def _extract_diagonal_lengths(R: np.ndarray) -> np.ndarray:
    """
    Trích xuất toàn bộ phân bố độ dài đường chéo P(l) từ nửa trên ma trận hồi quy.
    Không lọc ngưỡng tại bước này để duy trì tính thuần túy hình học.
    """
    n = R.shape[0]
    lengths = []
    
    for k in range(1, n):
        # Ép kiểu int32 để đảm bảo an toàn cho np.diff
        diag = np.diag(R, k=k).astype(np.int32)
        
        padded = np.pad(diag, (1, 1), mode='constant')
        diffs = np.diff(padded)
        
        starts = np.where(diffs == 1)[0]
        ends = np.where(diffs == -1)[0]
        
        lengths.extend(ends - starts)
            
    return np.array(lengths, dtype=np.int32)


def calculate_det(R: np.ndarray, diagonal_lengths: np.ndarray, l_min: int = 2) -> float:
    """
    Tính Determinism (DET) dựa trên nửa trên của ma trận.
    """
    total_recurrence = np.sum(np.triu(R, k=1))
    if total_recurrence == 0:
        return 0.0
        
    valid_lengths = diagonal_lengths[diagonal_lengths >= l_min]
    return float(np.sum(valid_lengths) / total_recurrence)


def calculate_lmean(diagonal_lengths: np.ndarray, l_min: int = 2) -> float:
    """
    Tính Average Diagonal Length (L_mean).
    """
    valid_lengths = diagonal_lengths[diagonal_lengths >= l_min]
    if len(valid_lengths) == 0:
        return 0.0
        
    return float(np.mean(valid_lengths))


def calculate_lmax(diagonal_lengths: np.ndarray, l_min: int = 2) -> int:
    """
    Tìm Maximal Diagonal Length (L_max).
    """
    valid_lengths = diagonal_lengths[diagonal_lengths >= l_min]
    if len(valid_lengths) == 0:
        return 0
        
    return int(np.max(valid_lengths))


# =============================================================================
# MODULE 4: VERTICAL QUANTIFICATION (MARWAN 2002)
# =============================================================================

def _extract_vertical_lengths(R: np.ndarray) -> np.ndarray:
    """
    Trích xuất toàn bộ phân bố độ dài đường dọc P(v) từ ma trận hồi quy.
    """
    n = R.shape[0]
    lengths = []
    
    # Bỏ qua đường chéo chính (Line of Identity)
    R_no_loi = R.copy()
    np.fill_diagonal(R_no_loi, 0)
    
    for col in range(n):
        col_data = R_no_loi[:, col].astype(np.int32)
        
        # Thêm padding tường minh với giá trị 0
        padded = np.pad(col_data, (1, 1), mode='constant', constant_values=0)
        diffs = np.diff(padded)
        
        starts = np.where(diffs == 1)[0]
        ends = np.where(diffs == -1)[0]
        
        lengths.extend(ends - starts)
            
    return np.array(lengths, dtype=np.int32)


def calculate_laminarity(vertical_lengths: np.ndarray, v_min: int = 2) -> float:
    """
    Tính Laminarity (LAM).
    Mẫu số lấy trực tiếp từ P(v) đúng theo công thức Marwan 2002.
    """
    total_recurrence = np.sum(vertical_lengths)
    if total_recurrence <= 0:
        return 0.0
        
    valid_lengths = vertical_lengths[vertical_lengths >= v_min]
    return float(np.sum(valid_lengths) / total_recurrence)


def calculate_trapping_time(vertical_lengths: np.ndarray, v_min: int = 2) -> float:
    """
    Tính Trapping Time (TT).
    """
    valid_lengths = vertical_lengths[vertical_lengths >= v_min]
    if len(valid_lengths) == 0:
        return 0.0
        
    return float(np.mean(valid_lengths))


def calculate_vmax(vertical_lengths: np.ndarray, v_min: int = 2) -> int:
    """
    Tìm Maximal Vertical Length (V_max).
    """
    valid_lengths = vertical_lengths[vertical_lengths >= v_min]
    if len(valid_lengths) == 0:
        return 0
        
    return int(np.max(valid_lengths))


# =============================================================================
# MODULE 5: DATACLASSES & WRAPPERS
# =============================================================================

@dataclass
class DiagonalResult:
    """
    RQA measures derived from diagonal line structures (Evolution).
    """
    DET: float
    L_MEAN: float
    L_MAX: int


@dataclass
class VerticalResult:
    """
    RQA measures derived from vertical line structures (Persistence).
    """
    LAM: float
    TT: float
    V_MAX: int


def run_webber2002(signal: np.ndarray, m: int, tau: int, epsilon: float, l_min: int = 2) -> DiagonalResult:
    """
    Đóng gói luồng tính toán RQA đường chéo (Webber 1994) để đối chứng.
    """
    X = reconstruct_phase_space(signal, m, tau)
    D = compute_distance_matrix(X)
    R = compute_recurrence_matrix(D, epsilon)
    
    diagonal_lengths = _extract_diagonal_lengths(R)
    
    return DiagonalResult(
        DET=calculate_det(R, diagonal_lengths, l_min=l_min),
        L_MEAN=calculate_lmean(diagonal_lengths, l_min=l_min),
        L_MAX=calculate_lmax(diagonal_lengths, l_min=l_min)
    )


def run_marwan2002(signal: np.ndarray, m: int, tau: int, epsilon: float, v_min: int = 2) -> VerticalResult:
    """
    Đóng gói luồng tính toán RQA đường dọc (Marwan 2002) - đóng góp cốt lõi.
    """
    X = reconstruct_phase_space(signal, m, tau)
    D = compute_distance_matrix(X)
    R = compute_recurrence_matrix(D, epsilon)
    
    vertical_lengths = _extract_vertical_lengths(R)
    
    return VerticalResult(
        LAM=calculate_laminarity(vertical_lengths, v_min=v_min),
        TT=calculate_trapping_time(vertical_lengths, v_min=v_min),
        V_MAX=calculate_vmax(vertical_lengths, v_min=v_min)
    )