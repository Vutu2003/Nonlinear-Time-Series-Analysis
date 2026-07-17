import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


def compute_dfa_core(signal, scales, order=1):
    """
    Core computation for Detrended Fluctuation Analysis (DFA) based on Peng (1994).
    """
    signal = np.asarray(signal)
    N = len(signal)
    
    # Step 1: Create Profile (Integration)
    y = np.cumsum(signal - np.mean(signal))
    
    valid_scales = []
    F_values = []
    
    for n in scales:
        n = int(n)
        
        # Ensure window size is mathematically meaningful for the given polynomial order
        if n < order + 2 or n > N:
            continue
            
        # Step 2: Windowing (Forward segmentation)
        n_windows = N // n
        y_trunc = y[:n_windows * n]
        
        # Reshape into (n_windows, n)
        y_reshaped = y_trunc.reshape(n_windows, n)
        
        # Create a local time axis for the window
        t = np.arange(n)
        
        # Step 3: Local Detrending
        coeffs = np.polyfit(t, y_reshaped.T, order)
        
        # BẢN VÁ LỖI BROADCASTING:
        # Ép t thành vector cột (n, 1) để broadcast chính xác với coeffs (order+1, n_windows)
        trend = np.polyval(coeffs, t.reshape(-1, 1)).T
        
        # Extract the intrinsic residual
        residual = y_reshaped - trend
        
        # Step 4: Fluctuation (RMS)
        rms = np.sqrt(np.mean(residual ** 2))
        
        valid_scales.append(n)
        F_values.append(rms)
        
    return np.asarray(valid_scales), np.asarray(F_values)

def dfa_fit(scales, fluctuations):
    """
    Thực hiện hồi quy tuyến tính trên không gian log-log để tìm số mũ alpha.
    
    Parameters:
        scales (array-like): Mảng kích thước cửa sổ l.
        fluctuations (array-like): Mảng độ thăng giáng F(l) tương ứng.
        
    Returns:
        dict: Chứa các tham số hồi quy (alpha, intercept, R2, stderr).
    """
    scales = np.asarray(scales)
    fluctuations = np.asarray(fluctuations)

    # Bảo vệ: Chỉ lấy các giá trị F(l) hợp lệ (> 0) để tính log
    valid = fluctuations > 0
    if not np.any(valid):
        return {"alpha": np.nan, "intercept": np.nan, "R2": np.nan, "stderr": np.nan}

    log_n = np.log10(scales[valid])
    log_F = np.log10(fluctuations[valid])

    slope, intercept, r_value, p_value, stderr = linregress(log_n, log_F)

    return {
        "alpha": slope,
        "intercept": intercept,
        "R2": r_value ** 2,
        "stderr": stderr
    }
    
def detect_crossover(scales, fluctuations, min_points=4, r2_gain=0.01, alpha_diff=0.05):
    """
    Quét qua các điểm dữ liệu để tìm điểm gãy khúc (crossover) tối ưu nhất.
    """
    N = len(scales)
    global_fit = dfa_fit(scales, fluctuations)

    best = None
    best_score = -np.inf

    # Không đủ dữ liệu để chia đôi
    if N < 2 * min_points:
        return {"is_crossover": False}

    for split in range(min_points, N - min_points):
        # Chia sẻ điểm split cho cả 2 mảng để đảm bảo tính liên tục của hệ thống
        left = dfa_fit(scales[:split + 1], fluctuations[:split + 1])
        right = dfa_fit(scales[split:], fluctuations[split:])

        # Đánh giá điểm rẽ nhánh dựa trên tổng R^2
        score = left["R2"] + right["R2"]

        if score > best_score:
            best_score = score
            best = {
                "breakpoint": scales[split],
                "alpha1": left["alpha"],
                "alpha2": right["alpha"],
                "intercept1": left["intercept"],
                "intercept2": right["intercept"],
                "R2_1": left["R2"],
                "R2_2": right["R2"]
            }

    # Đánh giá điều kiện để xác nhận crossover là có ý nghĩa
    avg_local_r2 = (best["R2_1"] + best["R2_2"]) / 2.0
    
    is_crossover = (
        (avg_local_r2 > global_fit["R2"] + r2_gain) and 
        (abs(best["alpha1"] - best["alpha2"]) > alpha_diff)
    )

    best["is_crossover"] = is_crossover
    return best   

def interpret_alpha(alpha):
    """
    Diễn giải ý nghĩa động lực học của số mũ alpha.
    """
    if np.isnan(alpha):
        return "Invalid / No data"
        
    if alpha < 0.5:
        return "Anti-persistent (Tương quan nghịch, dao động tự triệt tiêu)"
    elif np.isclose(alpha, 0.5, atol=0.05):
        return "White noise (Nhiễu trắng, không có bộ nhớ)"
    elif 0.5 < alpha < 1.0:
        return "Persistent (Tương quan dài hạn kiên định)"
    elif np.isclose(alpha, 1.0, atol=0.05):
        return "1/f noise (Trạng thái fractal cân bằng lý tưởng)"
    elif 1.0 < alpha < 1.5:
        return "Strong correlation (Tương quan mạnh, phi lũy thừa)"
    elif np.isclose(alpha, 1.5, atol=0.05):
        return "Brownian noise (Nhiễu Brown, quá mượt mà)"
    else:
        return "Non-stationary (Tính phi dừng cực đại)"
    

def dfa(signal, scales, order=1, detect_breakpoint=False):
    """
    Pipeline hoàn chỉnh chạy thuật toán DFA.
    (Yêu cầu đã import hàm compute_dfa_core ở trên).
    """
    # 1. Tính toán Core
    valid_scales, F_n = compute_dfa_core(signal, scales, order=order)
    
    if len(valid_scales) < 3:
        raise ValueError("Không đủ số lượng scales hợp lệ để thực hiện hồi quy tuyến tính.")

    # 2. Hồi quy toàn cục
    global_fit = dfa_fit(valid_scales, F_n)

    result = {
        "scales": valid_scales,
        "fluctuations": F_n,
        "global_alpha": global_fit["alpha"],
        "global_R2": global_fit["R2"],
        "global_intercept": global_fit["intercept"],
        "interpretation": interpret_alpha(global_fit["alpha"]),
        "has_crossover": False
    }

    # 3. Phân tích Crossover (Tuỳ chọn)
    if detect_breakpoint:
        crossover_info = detect_crossover(valid_scales, F_n)
        if crossover_info and crossover_info.get("is_crossover"):
            result["has_crossover"] = True
            result["crossover"] = crossover_info
            result["interpretation_1"] = interpret_alpha(crossover_info["alpha1"])
            result["interpretation_2"] = interpret_alpha(crossover_info["alpha2"])

    return result

def plot_dfa(dfa_result):
    """
    Trực quan hóa kết quả DFA trên đồ thị log-log.
    """
    scales = dfa_result["scales"]
    F_n = dfa_result["fluctuations"]
    
    log_n = np.log10(scales)
    log_F = np.log10(F_n)
    
    plt.figure(figsize=(8, 6))
    
    # Vẽ các điểm dữ liệu thực tế
    plt.scatter(log_n, log_F, facecolors='none', edgecolors='black', label="Data: F(n)", zorder=3)
    
    if dfa_result["has_crossover"]:
        cross = dfa_result["crossover"]
        bp = cross["breakpoint"]
        
        # Tách mảng để vẽ hai đường fit
        idx = np.where(scales == bp)[0][0]
        
        log_n_left = log_n[:idx+1]
        log_F_fit_left = cross["alpha1"] * log_n_left + cross["intercept1"]
        
        log_n_right = log_n[idx:]
        log_F_fit_right = cross["alpha2"] * log_n_right + cross["intercept2"]
        
        plt.plot(log_n_left, log_F_fit_left, color='blue', 
                 label=f"Short-range $\\alpha_1$: {cross['alpha1']:.2f}")
        plt.plot(log_n_right, log_F_fit_right, color='red', 
                 label=f"Long-range $\\alpha_2$: {cross['alpha2']:.2f}")
        
        # Đánh dấu điểm gãy khúc
        plt.axvline(x=np.log10(bp), color='gray', linestyle='--', label=f"Crossover n={bp}")
        
    else:
        # Vẽ đường fit toàn cục
        alpha = dfa_result["global_alpha"]
        intercept = dfa_result["global_intercept"]
        log_F_fit = alpha * log_n + intercept
        
        plt.plot(log_n, log_F_fit, color='blue', 
                 label=f"Global $\\alpha$: {alpha:.2f}")
    
    plt.xlabel(r"$\log_{10} n$ (Window Size)")
    plt.ylabel(r"$\log_{10} F(n)$ (Fluctuation)")
    plt.title("Detrended Fluctuation Analysis (DFA)")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.show()

