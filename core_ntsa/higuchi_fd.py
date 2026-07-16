import warnings
import numpy as np
from scipy.stats import linregress

def higuchi_crossover_fd(series, k_input=None, min_points_per_segment=4):
    """
    Tính HFD, phát hiện Crossover và xuất dữ liệu tọa độ Log-Log.
    
    Args:
        series (array-like): Chuỗi thời gian 1D.
        k_input (int hoặc array-like, optional): 
            - Nếu int: Đặt làm k_max, mảng k sẽ chạy tuyến tính từ 1 đến k_max.
            - Nếu array: Sử dụng trực tiếp mảng k này (hữu ích cho scale cấp số nhân).
            - Nếu None: Tự động dùng k_max = N // 10.
        min_points_per_segment (int): Số điểm tối thiểu cho mỗi đoạn hồi quy.
        
    Returns:
        dict: Chứa các tham số HFD và mảng dữ liệu thô ('k_array', 'L_k_array') để vẽ đồ thị.
    """
    X = np.asarray(series)
    N = len(X)
    
    # --- 1. Xử lý k_input linh hoạt ---
    safe_k_max = N // 10
    
    if k_input is None:
        k_values = np.arange(1, safe_k_max + 1)
    elif isinstance(k_input, (int, np.integer)):
        if k_input > safe_k_max:
            warnings.warn(f"k_max={k_input} lớn hơn ngưỡng an toàn {safe_k_max}.")
        k_values = np.arange(1, k_input + 1)
    else:
        # Nhận mảng tùy chỉnh (loại bỏ trùng lặp và sắp xếp)
        k_values = np.sort(np.unique(np.asarray(k_input, dtype=int)))
        k_values = k_values[k_values > 0]
        
    L_k_values = np.zeros(len(k_values))
    
    # --- 2. Phân rã đa pha và đo chiều dài ---
    for idx, k in enumerate(k_values):
        L_m_k = np.zeros(k)
        for m in range(k):
            n_steps = (N - 1 - m) // k
            if n_steps > 0:
                sum_diff = np.sum(np.abs(np.diff(X[m::k])))
                L_m_k[m] = (sum_diff * (N - 1)) / (n_steps * k**2)
                
        valid_Lm = L_m_k[L_m_k > 0]
        if len(valid_Lm) > 0:
            L_k_values[idx] = np.mean(valid_Lm)
        else:
            L_k_values[idx] = np.nan
            
    # --- 3. Xử lý an toàn logarit ---
    valid_indices = (L_k_values > 0) & ~np.isnan(L_k_values)
    if np.sum(valid_indices) < min_points_per_segment * 2:
        warnings.warn("Không đủ điểm hợp lệ để dò crossover.")
        return {"HFD": np.nan, "Scaling": "error"}
        
    valid_k = k_values[valid_indices]
    valid_Lk = L_k_values[valid_indices]
    
    log_k = np.log(valid_k)
    log_L_k = np.log(valid_Lk)
    
    # --- 4. Hồi quy toàn cục ---
    global_slope, intercept, r_val, _, _ = linregress(log_k, log_L_k)
    global_D = -global_slope
    
    # --- 5. Quét điểm gãy (Crossover) ---
    best_score = -1
    best_split_idx = None
    best_D1, best_D2, best_R2_1, best_R2_2 = None, None, None, None
    
    n_points = len(log_k)
    for i in range(min_points_per_segment, n_points - min_points_per_segment + 1):
        slope1, _, r1, _, _ = linregress(log_k[:i], log_L_k[:i])
        slope2, _, r2, _, _ = linregress(log_k[i:], log_L_k[i:])
        
        score = r1**2 + r2**2
        if score > best_score:
            best_score = score
            best_split_idx = i
            best_D1, best_D2 = -slope1, -slope2
            best_R2_1, best_R2_2 = r1**2, r2**2
            
    is_crossover = (best_score / 2.0 > r_val**2 + 0.01) and (abs(best_D1 - best_D2) > 0.05)
    
    # --- 6. Đóng gói Kết quả (Bao gồm Data thô) ---
    result = {
        "HFD": round(global_D, 4),
        "R2": round(r_val**2, 4),
        "Intercept": intercept,
        "k_array": valid_k,      # <--- Xuất dữ liệu trục hoành
        "L_k_array": valid_Lk    # <--- Xuất dữ liệu trục tung
    }
    
    if is_crossover:
        result.update({
            "Scaling": "crossover",
            "Breakpoint_k": int(valid_k[best_split_idx]),
            "D1_small_scale": round(best_D1, 4), "R2_1": round(best_R2_1, 4),
            "D2_large_scale": round(best_D2, 4), "R2_2": round(best_R2_2, 4)
        })
    else:
        result.update({"Scaling": "single"})
        
    return result