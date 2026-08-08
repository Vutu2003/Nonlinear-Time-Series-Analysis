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
from dataclasses import dataclass
from typing import Dict, Any, Tuple, Optional


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

# ==========================================
# 4. TẦNG JOINT DIAGONAL STATISTICS
# ==========================================

def extract_all_diagonal_lengths(
    JR: np.ndarray, exclude_main_diagonal: bool = False
) -> np.ndarray:
    """
    Trích xuất toàn bộ độ dài đường chéo từ ma trận Joint Recurrence.
    Cho phép loại bỏ đường chéo chính (LOI) để phục vụ khảo sát finite-size effects.
    """
    n_rows, n_cols = JR.shape
    lengths = []
    
    for k in range(-(n_rows - 1), n_cols):
        if k == 0 and exclude_main_diagonal:
            continue
            
        diag = np.diagonal(JR, offset=k).astype(np.int32)
        if not np.any(diag):
            continue
            
        padded = np.pad(diag, (1, 1), mode='constant', constant_values=0)
        diffs = np.diff(padded)
        
        starts = np.where(diffs == 1)[0]
        ends = np.where(diffs == -1)[0]
        
        lengths.extend(ends - starts)
        
    return np.array(lengths, dtype=np.int32)


def compute_diagonal_probability(
    diag_lengths: np.ndarray, N: int, l_max: int = None
):
    """
    Tính xác suất P(l): xác suất tìm được đoạn chéo liên tục dài >= l.
    Sử dụng mảng tích lũy ngược (suffix sums) để đạt độ phức tạp O(L_max).
    """
    diag_lengths = np.asarray(diag_lengths, dtype=np.int32)
    
    if N <= 0:
        raise ValueError("N phải là số nguyên dương.")
        
    if diag_lengths.size == 0:
        empty = np.array([], dtype=np.float64)
        return empty, empty, empty
        
    actual_max = int(np.max(diag_lengths))
    
    if l_max is None:
        l_max = actual_max
    else:
        l_max = min(l_max, actual_max)
        
    counts = np.bincount(diag_lengths, minlength=actual_max + 1)
    lengths_arr = np.arange(len(counts))
    
    # Tính tổng tích lũy từ mảng đảo ngược (suffix sums)
    suffix_count = np.cumsum(counts[::-1])[::-1]
    suffix_weighted = np.cumsum((counts * lengths_arr)[::-1])[::-1]
    
    l_axis = np.arange(1, l_max + 1)
    
    # Tính số lượng đoạn dài l dựa trên tổng tích lũy
    segment_counts = (
        suffix_weighted[l_axis] - (l_axis - 1) * suffix_count[l_axis]
    )
    
    P_l = segment_counts.astype(np.float64) / (float(N) ** 2)
    valid = P_l > 0
    
    return l_axis[valid], P_l[valid], np.log(P_l[valid])


# ==========================================
# 5. TẦNG INVARIANT ESTIMATION
# ==========================================

def estimate_k2_entropy(
    l_axis: np.ndarray, ln_P_l: np.ndarray, delta_t: float, fit_range: tuple
) -> float:
    """
    Ước lượng K2 từ vùng tuyến tính của đồ thị ln P(l).
    
    Args:
        l_axis (np.ndarray): Trục độ dài l.
        ln_P_l (np.ndarray): Trục logarit tự nhiên của xác suất P(l).
        delta_t (float): Bước thời gian lấy mẫu.
        fit_range (tuple): Khoảng (l_min, l_max) để thực hiện hồi quy.
    """
    if delta_t <= 0:
        raise ValueError("delta_t phải là số dương.")
        
    l_min, l_max = fit_range
    
    if l_min > l_max:
        raise ValueError("fit_range phải thỏa mãn l_min <= l_max.")
        
    mask = (l_axis >= l_min) & (l_axis <= l_max)
    
    if np.sum(mask) < 2:
        raise ValueError("fit_range phải chứa ít nhất 2 điểm hợp lệ để hồi quy.")
        
    slope, _ = np.polyfit(l_axis[mask], ln_P_l[mask], 1)
    
    return float(-slope / delta_t)


# ==========================================
# 6. TẦNG RESULT & CORE WRAPPER
# ==========================================

@dataclass
class MRPResult:
    """Dataclass lưu trữ kết quả phân tích Multivariate Recurrence Plots."""
    JR: Optional[np.ndarray]
    diagonal_lengths: np.ndarray
    l_axis: np.ndarray
    P_l: np.ndarray
    ln_P_l: np.ndarray
    K2: Optional[float]
    metadata: Dict[str, Any]


def run_mrp_analysis(
    signal_x: np.ndarray, signal_y: np.ndarray,
    m_x: int, tau_x: int, tx_start: int,
    m_y: int, tau_y: int, ty_start: int,
    target_rr_x: float, target_rr_y: float,
    delta_t: float, fit_range: Optional[Tuple[int, int]] = None,
    l_max: Optional[int] = None, exclude_main_diagonal: bool = False,
    return_jr: bool = True
) -> MRPResult:
    """
    Vận hành luồng phân tích MRP lõi từ dữ liệu thô đến K2.
    """
    # 1. Nhúng và đồng bộ thời gian
    X_emb = embed_time_series(signal_x, m_x, tau_x)
    Y_emb = embed_time_series(signal_y, m_y, tau_y)
    X, Y = align_embedded_trajectories(X_emb, Y_emb, tx_start, ty_start)
    N = X.shape[0]
    
    # 2. Hình học độc lập
    D_x = compute_auto_distance_matrix(X)
    D_y = compute_auto_distance_matrix(Y)
    
    eps_x = find_threshold_for_rr(D_x, target_rr_x)
    eps_y = find_threshold_for_rr(D_y, target_rr_y)
    
    R_x = compute_recurrence_matrix(D_x, eps_x)
    R_y = compute_recurrence_matrix(D_y, eps_y)
    
    # 3. Hồi quy kết hợp và thống kê
    JR = compute_joint_recurrence_matrix(R_x, R_y)
    diag_lengths = extract_all_diagonal_lengths(JR, exclude_main_diagonal)
    l_axis, P_l, ln_P_l = compute_diagonal_probability(diag_lengths, N, l_max)
    
    # 4. Ước lượng K2 (nếu có fit_range)
    k2_val = None
    if fit_range is not None:
        k2_val = estimate_k2_entropy(l_axis, ln_P_l, delta_t, fit_range)
        
    metadata = {
        "m_x": m_x, "tau_x": tau_x, "eps_x": eps_x,
        "m_y": m_y, "tau_y": tau_y, "eps_y": eps_y,
        "target_rr_x": target_rr_x, "target_rr_y": target_rr_y,
        "delta_t": delta_t,
        "fit_range": fit_range,
        "l_max": l_max,
        "exclude_main_diagonal": exclude_main_diagonal,
        "N_aligned": N
    }
    
    return MRPResult(
        JR=JR if return_jr else None, 
        diagonal_lengths=diag_lengths, 
        l_axis=l_axis, P_l=P_l, ln_P_l=ln_P_l, 
        K2=k2_val, metadata=metadata
    )


# ==========================================
# 7. TẦNG HISTORICAL AUTOMATION (HEURISTICS XẤP XỈ)
# ==========================================

def identify_scaling_region(
    l_axis: np.ndarray, ln_P_l: np.ndarray, min_points: int = 5
) -> Tuple[int, int]:
    """
    Xấp xỉ phương pháp chọn vùng tuyến tính của bài báo thông qua phân chia
    chuỗi liên tục thành 2 đoạn thẳng (sequential two-segment linear split).
    
    Đây là một heuristic thực tiễn nhằm mô phỏng lại thuật toán 
    cluster-dissection nguyên thủy trong môi trường code hiện tại.
    """
    n = len(l_axis)
    if n == 0:
        raise ValueError("l_axis không được rỗng.")
    if n != len(ln_P_l):
        raise ValueError("l_axis và ln_P_l phải có cùng độ dài.")
        
    if n < min_points * 2:
        return (int(l_axis[0]), int(l_axis[-1]))
        
    best_ssr = np.inf
    best_split = min_points
    
    for i in range(min_points, n - min_points + 1):
        p1 = np.polyfit(l_axis[:i], ln_P_l[:i], 1, full=True)
        ssr1 = p1[1][0] if p1[1].size > 0 else 0
        
        p2 = np.polyfit(l_axis[i:], ln_P_l[i:], 1, full=True)
        ssr2 = p2[1][0] if p2[1].size > 0 else 0
        
        if ssr1 + ssr2 < best_ssr:
            best_ssr = ssr1 + ssr2
            best_split = i
            
    # Lựa chọn cụm chứa nhiều điểm dữ liệu hơn
    if best_split > (n - best_split):
        return (int(l_axis[0]), int(l_axis[best_split - 1]))
    else:
        return (int(l_axis[best_split]), int(l_axis[-1]))


def identify_k2_plateau(
    rr_levels: np.ndarray, k2_values: np.ndarray, window_size: int = 10
) -> float:
    """
    Xấp xỉ vùng cao nguyên K2 bằng cách tìm cửa sổ trượt (sliding window)
    có độ dốc tuyến tính tuyệt đối nhỏ nhất (minimum absolute slope).
    
    Đây là một heuristic thực tiễn mô phỏng quy trình 3-cluster dissection.
    """
    n = len(k2_values)
    if n != len(rr_levels):
        raise ValueError("rr_levels và k2_values phải có cùng độ dài.")
        
    if n < window_size:
        return float(np.mean(k2_values))
        
    min_slope = np.inf
    plateau_k2 = 0.0
    
    for i in range(n - window_size + 1):
        x_window = rr_levels[i:i + window_size]
        y_window = k2_values[i:i + window_size]
        
        slope, _ = np.polyfit(x_window, y_window, 1)
        if abs(slope) < min_slope:
            min_slope = abs(slope)
            plateau_k2 = float(np.mean(y_window))
            
    return plateau_k2


def analyze_automated_k2_vs_rr(
    signal_x: np.ndarray, signal_y: np.ndarray,
    m_x: int, tau_x: int, tx_start: int,
    m_y: int, tau_y: int, ty_start: int,
    delta_t: float, rr_levels: Optional[np.ndarray] = None
) -> Dict[str, Any]:
    """
    Xấp xỉ quy trình tự động phân tích K2-vs-RR của Romano et al. (2004).
    
    Việc quét mức RR tuân thủ logic của bài báo, nhưng các bước chọn scaling region 
    và xác định K2 plateau sử dụng các heuristics thực tiễn được định nghĩa ở trên.
    """
    if rr_levels is None:
        rr_levels = np.linspace(0.01, 0.95, 40)
        
    # 1. Tính toán không gian pha và ma trận khoảng cách MỘT LẦN DUY NHẤT
    X_emb = embed_time_series(signal_x, m_x, tau_x)
    Y_emb = embed_time_series(signal_y, m_y, tau_y)
    X, Y = align_embedded_trajectories(X_emb, Y_emb, tx_start, ty_start)
    N = X.shape[0]
    
    D_x = compute_auto_distance_matrix(X)
    D_y = compute_auto_distance_matrix(Y)
    
    # Tính trước toàn bộ danh sách threshold bằng vector hóa để tránh vòng lặp đắt đỏ
    eps_x_levels = np.quantile(D_x, rr_levels)
    eps_y_levels = np.quantile(D_y, rr_levels)
    
    k2_results = []
    
    # 2. Tái sử dụng ma trận khoảng cách; chỉ lặp qua phần nhị phân hóa & thống kê
    for eps_x, eps_y in zip(eps_x_levels, eps_y_levels):
        R_x = compute_recurrence_matrix(D_x, eps_x)
        R_y = compute_recurrence_matrix(D_y, eps_y)
        JR = compute_joint_recurrence_matrix(R_x, R_y)
        
        diag_lengths = extract_all_diagonal_lengths(JR, exclude_main_diagonal=False)
        l_axis, _, ln_P_l = compute_diagonal_probability(diag_lengths, N, l_max=400)
        
        # Guard an toàn (không phải tiêu chí finite-statistics 500-counts của paper)
        if len(l_axis) < 10:
            k2_results.append(np.nan)
            continue
            
        fit_range = identify_scaling_region(l_axis, ln_P_l)
        try:
            k2 = estimate_k2_entropy(l_axis, ln_P_l, delta_t, fit_range)
            k2_results.append(k2)
        except ValueError:
            k2_results.append(np.nan)
            
    k2_array = np.array(k2_results)
    
    valid_mask = ~np.isnan(k2_array)
    valid_rr = rr_levels[valid_mask]
    valid_k2 = k2_array[valid_mask]
    
    plateau_val = identify_k2_plateau(valid_rr, valid_k2) if len(valid_k2) > 0 else np.nan
    
    return {
        "rr_levels": rr_levels,
        "k2_curve": k2_array,
        "plateau_k2": plateau_val
    }