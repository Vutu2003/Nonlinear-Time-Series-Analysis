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

# ==========================================
# MODULE 3: QUANTIFICATION (RQA)
# ==========================================

def _extract_diagonal_lengths(R: np.ndarray) -> np.ndarray:
    """
    Helper: Trích xuất độ dài của tất cả các đường chéo (diagonal lines)
    trong phần tam giác trên của ma trận hồi quy.
    """
    n = R.shape[0]
    lengths = []
    
    for k in range(1, n):
        # Ép kiểu int32 để đảm bảo np.diff() nhận diện đúng 1 -> 0 thành -1
        diag = np.diag(R, k=k).astype(np.int32)
        padded = np.pad(diag, (1, 1), mode='constant', constant_values=0)
        diff = np.diff(padded)
        
        starts = np.where(diff == 1)[0]
        ends = np.where(diff == -1)[0]
        
        lengths.extend(ends - starts)
        
    return np.array(lengths)

def calculate_percent_recurrence(R: np.ndarray) -> float:
    """
    REC: Tỷ lệ phần trăm các điểm hồi quy trong nửa tam giác trên.
    """
    n = R.shape[0]
    if n <= 1:
        return 0.0
        
    upper_tri = np.triu(R, k=1)
    total_points = (n * (n - 1)) / 2.0
    rec_points = np.sum(upper_tri)
    
    return (rec_points / total_points) * 100.0

def calculate_percent_determinism(diag_lengths: np.ndarray, l_min: int = 2) -> float:
    """
    DET: Tỷ lệ phần trăm các điểm hồi quy tạo thành đường chéo có chiều dài >= l_min.
    """
    if len(diag_lengths) == 0:
        return 0.0
        
    # diag_lengths bao gồm cả line có độ dài 1
    # Do đó, sum(diag_lengths) chính bằng tổng số recurrence points
    total_rec_points = np.sum(diag_lengths)
    if total_rec_points == 0:
        return 0.0
        
    valid_lengths = diag_lengths[diag_lengths >= l_min]
    det_points = np.sum(valid_lengths)
    
    return (det_points / total_rec_points) * 100.0

def calculate_entropy(diag_lengths: np.ndarray, l_min: int = 2) -> float:
    """
    ENT: Entropy Shannon (bits) của phân phối độ dài các đường chéo (>= l_min).
    """
    valid_lengths = diag_lengths[diag_lengths >= l_min]
    if len(valid_lengths) == 0:
        return 0.0
        
    _, counts = np.unique(valid_lengths, return_counts=True)
    probabilities = counts / np.sum(counts)
    
    return -np.sum(probabilities * np.log2(probabilities))

def calculate_ratio(det: float, rec: float) -> float:
    """
    RATIO: Tỷ lệ giữa %DET và %REC.
    """
    if rec == 0.0:
        return 0.0
        
    return det / rec

def calculate_trend(R: np.ndarray) -> float:
    """
    TREND: Độ dốc của hồi quy tuyến tính mật độ điểm hồi quy
    theo khoảng cách cách xa đường chéo chính.
    """
    n = R.shape[0]
    if n <= 1:
        return 0.0
        
    displacements = np.arange(1, n)
    
    densities_pct = np.array([
        (np.sum(np.diag(R, k=k)) / (n - k)) * 100.0
        for k in displacements
    ])
    
    mean_x = np.mean(displacements)
    mean_y = np.mean(densities_pct)
    
    numerator = np.sum((displacements - mean_x) * (densities_pct - mean_y))
    denominator = np.sum((displacements - mean_x) ** 2)
    
    if denominator == 0:
        return 0.0
        
    slope = numerator / denominator
    
    # Nhân 1000 là historical scaling factor để dễ đọc 
    # và đồng nhất với RQA.EXE / CRP Toolbox / PyRQA
    return slope * 1000.0

# ==========================================
# MODULE 4: WRAPPER
# ==========================================

@dataclass
class RQAResult:
    """
    Cấu trúc dữ liệu lưu trữ 5 chỉ số RQA cốt lõi theo Webber & Zbilut (1994).
    Được thiết kế tối ưu để lưu trữ danh sách kết quả từ Sliding Window.
    """
    REC: float
    DET: float
    ENT: float
    RATIO: float
    TREND: float

def run_webber1994(
    signal: np.ndarray, 
    d: int, 
    tau: int, 
    radius: float, 
    l_min: int = 2, 
    metric: str = 'euclidean'
) -> RQAResult:
    """
    Hàm wrapper thực thi toàn bộ luồng phân tích RQA theo Webber & Zbilut (1994).
    
    Args:
        signal: Mảng 1D chứa chuỗi thời gian đầu vào.
        d: Chiều không gian nhúng (embedding dimension).
        tau: Độ trễ thời gian (time delay).
        radius: Ngưỡng bán kính lân cận (r).
        l_min: Độ dài đường chéo tối thiểu để tính DET và ENT (mặc định = 2).
        metric: Loại khoảng cách sử dụng để tính toán.
        
    Returns:
        RQAResult: Dataclass chứa 5 chỉ số REC, DET, ENT, RATIO, TREND.
    """
    # 1. Tái dựng không gian pha
    X = reconstruct_phase_space(signal, d, tau)
    
    # 2. Xây dựng ma trận khoảng cách và ma trận hồi quy
    D = compute_distance_matrix(X, metric=metric)
    R = compute_recurrence_matrix(D, radius)
    
    # 3. Trích xuất phân phối đường chéo
    diag_lengths = _extract_diagonal_lengths(R)
    
    # 4. Định lượng các chỉ số RQA
    rec = calculate_percent_recurrence(R)
    det = calculate_percent_determinism(diag_lengths, l_min=l_min)
    ent = calculate_entropy(diag_lengths, l_min=l_min)
    ratio = calculate_ratio(det, rec)
    trend = calculate_trend(R)
    
    return RQAResult(
        REC=rec,
        DET=det,
        ENT=ent,
        RATIO=ratio,
        TREND=trend
    )