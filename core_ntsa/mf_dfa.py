import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import warnings

def compute_mf_dfa_core(data, s_array, q_array, m=1):
    """
    Tính toán hàm thăng giáng F_q(s) cho chuỗi dữ liệu gốc (Bản v1).
    
    Tham số:
        data (np.ndarray): Mảng dữ liệu chuỗi thời gian 1D.
        s_array (np.ndarray hoặc list): Danh sách các kích thước cửa sổ phân tích.
        q_array (np.ndarray hoặc list): Danh sách các bậc moment q.
        m (int): Bậc của đa thức dùng để khử xu hướng (mặc định = 1).
        
    Trả về:
        F_q_s (np.ndarray): Ma trận thăng giáng kích thước (len(valid_s), len(q_array)).
        valid_s (np.ndarray): Mảng các kích thước cửa sổ s hợp lệ thực tế đã dùng.
    """
    data = np.asarray(data)
    s_array = np.asarray(s_array, dtype=int)
    q_array = np.asarray(q_array, dtype=float)
    N = len(data)
    
    # (1) Bắt lỗi an toàn toán học chuẩn production
    if np.min(s_array) < m + 2:
        raise ValueError(f"Kích thước cửa sổ s tối thiểu phải >= m + 2 (hiện tại m={m}).")
        
    # (2) Lọc các cửa sổ s hợp lệ để tránh mảng rỗng sinh NaN
    valid_s = s_array[s_array <= N]
    if len(valid_s) == 0:
        raise ValueError("Không có kích thước cửa sổ s nào hợp lệ (tất cả đều lớn hơn N).")
    
    # (5) Sử dụng machine epsilon để chống lỗi log(0)
    eps = np.finfo(float).eps
    
    F_q_s = np.zeros((len(valid_s), len(q_array)))
    
    data_mean = np.mean(data)
    Y = np.cumsum(data - data_mean)
    
    for i_s, s in enumerate(valid_s):
        Ns = N // s
        
        Y_fwd = Y[:Ns * s].reshape((Ns, s))
        Y_bwd = Y[N - (Ns * s):].reshape((Ns, s))
        
        Y_segments = np.vstack((Y_fwd, Y_bwd))
        total_segments = 2 * Ns
        
        x_idx = np.arange(1, s + 1)
        F2_nu = np.zeros(total_segments)
        
        # (4) Nút thắt hiệu năng: Tính phương sai cục bộ
        for nu in range(total_segments):
            segment = Y_segments[nu, :]
            poly_coefs = np.polyfit(x_idx, segment, m)
            trend = np.polyval(poly_coefs, x_idx)
            F2_nu[nu] = np.mean((segment - trend) ** 2)
            
        F2_nu = np.maximum(F2_nu, eps)
        
        for i_q, q in enumerate(q_array):
            # (3) Xử lý an toàn sai số dấu phẩy động cho q = 0
            if np.isclose(q, 0.0):
                F_q_s[i_s, i_q] = np.exp(0.5 * np.mean(np.log(F2_nu)))
            else:
                F_q_s[i_s, i_q] = (np.mean(F2_nu ** (q / 2.0))) ** (1.0 / q)
                
    return F_q_s, valid_s

def mf_dfa_fit(scales, F_q_s, q_array):
    """
    Thực hiện hồi quy tuyến tính log-log để tìm mảng số mũ h(q) từ ma trận F_q_s.
    
    Parameters:
        scales (array-like): Mảng kích thước cửa sổ s hợp lệ (valid_s).
        F_q_s (np.ndarray): Ma trận thăng giáng 2D từ hàm core.
        q_array (array-like): Danh sách các bậc moment q tương ứng.
        
    Returns:
        dict: Chứa các mảng tham số hồi quy h(q), intercept, R2, stderr cho từng q,
              và mảng log_scales để tái sử dụng trực tiếp khi vẽ đồ thị.
    """
    scales = np.asarray(scales)
    F_q_s = np.asarray(F_q_s)
    
    num_q = len(q_array)
    
    hq = np.zeros(num_q)
    intercepts = np.zeros(num_q)
    R2 = np.zeros(num_q)
    stderr = np.zeros(num_q)
    
    # Tiền tính toán không gian logarit một lần duy nhất cho toàn bộ hệ thống
    log_s = np.log10(scales)
    
    for i_q in range(num_q):
        fluctuations = F_q_s[:, i_q]
        
        valid = fluctuations > 0
        if not np.any(valid):
            hq[i_q] = np.nan
            intercepts[i_q] = np.nan
            R2[i_q] = np.nan
            stderr[i_q] = np.nan
            continue
            
        log_F = np.log10(fluctuations[valid])
        
        # Hồi quy tuyến tính trên các điểm hợp lệ
        slope, inter, r_val, p_val, std_err = linregress(log_s[valid], log_F)
        
        hq[i_q] = slope
        intercepts[i_q] = inter
        R2[i_q] = r_val ** 2
        stderr[i_q] = std_err
        
    return {
        "hq": hq,
        "intercept": intercepts,
        "R2": R2,
        "stderr": stderr,
        "log_scales": log_s
    }

def select_scaling_region(scales, N, min_scale=10, max_scale_ratio=4):
    """
    Xác định vùng cửa sổ s hợp lệ để thực hiện hồi quy tuyến tính (Fit),
    nhằm loại bỏ nhiễu thống kê ở scale lớn và sai số overfit ở scale nhỏ.
    
    Parameters:
        scales (array-like): Mảng kích thước cửa sổ s ban đầu.
        N (int): Tổng số điểm dữ liệu của chuỗi tín hiệu gốc.
        min_scale (int): Ngưỡng dưới của s (thường là 10 hoặc m+2).
        max_scale_ratio (int): Tỷ lệ để xác định ngưỡng trên s <= N / max_scale_ratio 
                               (chuẩn bài báo là 4).
                               
    Returns:
        valid_scales (np.ndarray): Mảng các kích thước s nằm trong vùng an toàn.
        mask (np.ndarray): Mảng boolean dùng để lọc ma trận F_q_s tương ứng.
    """
    scales = np.asarray(scales)
    
    # Tính toán ngưỡng trên dựa trên chiều dài dữ liệu
    max_scale = N // max_scale_ratio
    
    # Tạo bộ lọc boolean thỏa mãn cả hai điều kiện (Lưu ý 1 & 2)
    mask = (scales >= min_scale) & (scales <= max_scale)
    
    valid_scales = scales[mask]
    
    if len(valid_scales) < 3:
        import warnings
        warnings.warn(
            f"Vùng tuyến tính quá hẹp (chỉ có {len(valid_scales)} điểm). "
            "Kết quả hồi quy log-log có thể không có ý nghĩa thống kê."
        )
        
    return valid_scales, mask

def compute_tau(q_array, hq):
    """
    Tính số mũ khối lượng (mass exponent) tau(q) từ mảng số mũ Hurst tổng quát h(q).
    
    Parameters:
        q_array (array-like): Mảng các bậc moment q.
        hq (array-like): Mảng số mũ h(q) thu được từ bước Fit.
        
    Returns:
        tau (np.ndarray): Mảng số mũ khối lượng.
    """
    q_array = np.asarray(q_array)
    hq = np.asarray(hq)
    
    # Tính toán vector hóa dựa trên công thức đại số
    tau = q_array * hq - 1
    
    return tau

def compute_singularity_spectrum(q_array, tau):
    """
    Thực hiện biến đổi Legendre để tính phổ kỳ dị và trích xuất các đặc trưng hình học.
    
    Parameters:
        q_array (array-like): Mảng các bậc moment q.
        tau (array-like): Mảng số mũ khối lượng tau(q).
        
    Returns:
        dict: Chứa mảng alpha, f_alpha và các đặc trưng (width, peak_alpha, asymmetry).
    """
    q_array = np.asarray(q_array)
    tau = np.asarray(tau)
    
    # 1. Đạo hàm số học: alpha = d(tau)/dq
    alpha = np.gradient(tau, q_array)
    
    # 2. Biến đổi Legendre: f(alpha) = q * alpha - tau
    f_alpha = q_array * alpha - tau
    
    # 3. Kiểm định tính đơn điệu của alpha(q)
    # alpha(q) theo lý thuyết phải giảm dần. Nếu sai phân > 0 (có du di sai số float), cảnh báo!
    if np.any(np.diff(alpha) > 1e-3):
        warnings.warn(
            "Cảnh báo: Hàm alpha(q) không đơn điệu giảm. "
            "Hiện tượng này thường do nhiễu khuếch đại khi đạo hàm h(q), "
            "vùng scaling region chọn chưa tối ưu, hoặc lưới q quá thưa."
        )
        
    # 4. Trích xuất các đặc trưng hình học của phổ
    alpha_min = np.min(alpha)
    alpha_max = np.max(alpha)
    width = alpha_max - alpha_min
    
    # Tìm alpha_0 tại đỉnh của f(alpha)
    idx_peak = np.argmax(f_alpha)
    peak_alpha = alpha[idx_peak]
    
    # Tính hệ số bất đối xứng (Asymmetry)
    # Dùng eps để bảo vệ phép chia cho 0 trong trường hợp phổ suy biến thành một điểm (đơn phân dạng)
    eps = np.finfo(float).eps
    asymmetry = (peak_alpha - alpha_min) / (alpha_max - peak_alpha + eps)
    
    return {
        "alpha": alpha,
        "f_alpha": f_alpha,
        "width": width,
        "peak_alpha": peak_alpha,
        "asymmetry": asymmetry
    }

def mf_dfa(data, s_array, q_array, m=1, min_scale=10, max_scale_ratio=4, calc_spectrum=True):
    """
    Hàm tổng hợp Pipeline thực hiện thuật toán MF-DFA.
    
    Parameters:
        data (array-like): Chuỗi tín hiệu thời gian 1D.
        s_array (array-like): Mảng kích thước cửa sổ s ban đầu.
        q_array (array-like): Mảng các bậc moment q.
        m (int): Bậc của đa thức khử xu hướng (m=1 là tuyến tính).
        min_scale (int): Ngưỡng dưới của s để hồi quy.
        max_scale_ratio (int): Tỷ lệ xác định ngưỡng trên của s (N / max_scale_ratio).
        calc_spectrum (bool): Cờ (flag) quyết định có tính phổ kỳ dị hay không.
        
    Returns:
        dict: Bộ kết quả toàn diện chứa toàn bộ dữ liệu từ Fit đến Spectrum (nếu có).
    """
    data = np.asarray(data)
    N = len(data)
    
    # 1. Tính toán hàm thăng giáng cốt lõi
    F_q_s, used_s = compute_mf_dfa_core(data, s_array, q_array, m=m)
    
    # 2. Lọc vùng scaling hợp lệ
    valid_s, mask = select_scaling_region(used_s, N, min_scale=min_scale, max_scale_ratio=max_scale_ratio)
    
    # Cắt ma trận F_q_s theo vùng hợp lệ
    F_q_s_filtered = F_q_s[mask, :]
    
    # 3. Hồi quy tuyến tính log-log để tìm h(q)
    fit_results = mf_dfa_fit(valid_s, F_q_s_filtered, q_array)
    hq = fit_results["hq"]
    
    # 4. Khởi tạo dictionary kết quả cơ bản
    result = {
        "q_array": q_array,
        "valid_s": valid_s,
        "F_q_s": F_q_s_filtered,
        "hq": hq,
        "R_squared": fit_results.get("R_squared", None), # Giả sử mf_dfa_fit có trả về R^2
        "log_s": np.log2(valid_s) if fit_results.get("log_s") is None else fit_results["log_s"],
        "log_F_q_s": np.log2(F_q_s_filtered) if fit_results.get("log_F_q_s") is None else fit_results["log_F_q_s"]
    }
    
    # 5. Tính toán các thành phần Optional (Tau & Singularity Spectrum)
    if calc_spectrum:
        # Tính số mũ khối lượng tau(q)
        tau = compute_tau(q_array, hq)
        
        # Tính phổ kỳ dị f(alpha)
        spectrum_results = compute_singularity_spectrum(q_array, tau)
        
        # Đóng gói kết quả phổ vào dict chính
        result["tau"] = tau
        result["spectrum"] = spectrum_results
        
    return result

def plot_scaling(result, num_lines=5):
    """
    Vẽ đồ thị Log-Log của hàm thăng giáng F_q(s) theo s với một vài giá trị q đại diện.
    """
    q_array = result["q_array"]
    log_s = result["log_s"]
    log_F_q_s = result["log_F_q_s"]
    hq = result["hq"]
    
    # Tự động chọn 4-5 chỉ số (index) dàn đều trong mảng q
    # Ví dụ mảng có 21 phần tử, num_lines=5 -> indices sẽ là [0, 5, 10, 15, 20]
    num_q = len(q_array)
    indices = np.linspace(0, num_q - 1, min(num_lines, num_q), dtype=int)
    
    plt.figure(figsize=(8, 6))
    
    # Sử dụng colormap để tạo dải màu đẹp từ lạnh (q âm) sang nóng (q dương)
    colors = plt.cm.viridis(np.linspace(0, 1, len(indices)))
    
    for i, idx in enumerate(indices):
        q = q_array[idx]
        h_val = hq[idx]
        y_actual = log_F_q_s[:, idx]
        
        # 1. Vẽ điểm dữ liệu thực tế
        plt.plot(log_s, y_actual, 'o', color=colors[i], markersize=5)
        
        # 2. Dựng lại đường thẳng Fit (y = ax + b) để vẽ
        # Vì hq là độ dốc (a), ta tính lại tung độ gốc (b) = mean(y) - a * mean(x)
        intercept = np.mean(y_actual) - h_val * np.mean(log_s)
        y_fit = h_val * log_s + intercept
        
        # Vẽ đường thẳng và gán label chứa h(q) cho Legend
        plt.plot(log_s, y_fit, '-', color=colors[i], 
                 label=r"$q = %.1f, h(q) = %.2f$" % (q, h_val))
                 
    plt.xlabel(r"$\log_2(s)$", fontsize=12)
    plt.ylabel(r"$\log_2(F_q(s))$", fontsize=12)
    plt.title("MF-DFA: Scaling Behavior", fontsize=14)
    plt.legend(loc='best', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def plot_singularity(result):
    """
    Vẽ phổ kỳ dị f(alpha) theo alpha và hiển thị các đặc trưng hình học.
    """
    if "spectrum" not in result:
        print("Lỗi: Không tìm thấy dữ liệu phổ. Hãy đảm bảo mf_dfa() chạy với calc_spectrum=True.")
        return
        
    spectrum = result["spectrum"]
    alpha = spectrum["alpha"]
    f_alpha = spectrum["f_alpha"]
    
    width = spectrum["width"]
    peak = spectrum["peak_alpha"]
    asym = spectrum.get("asymmetry", 0.0) # Lấy asymmetry nếu có
    
    plt.figure(figsize=(8, 6))
    
    # Vẽ đường phổ kỳ dị hình parabol
    plt.plot(alpha, f_alpha, 'o-', color='crimson', linewidth=2, markersize=5)
    
    # Đánh dấu sao vàng tại đỉnh phổ
    plt.plot(peak, np.max(f_alpha), '*', color='gold', markersize=15, 
             markeredgecolor='black', label='Peak')
    
    # Khởi tạo Text Box chứa các chỉ số đặc trưng
    textstr = '\n'.join((
        r'$\Delta\alpha \ (Width) = %.3f$' % (width, ),
        r'$\alpha_0 \ (Peak) = %.3f$' % (peak, ),
        r'$B \ (Asymmetry) = %.3f$' % (asym, )
    ))
    
    # Định dạng hộp thoại text
    props = dict(boxstyle='round,pad=0.5', facecolor='ivory', edgecolor='gray', alpha=0.8)
    
    # Đặt Text Box ở góc trên bên trái (x=0.05, y=0.95 của hệ tọa độ Axis)
    plt.gca().text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
                   verticalalignment='top', bbox=props)
    
    plt.xlabel(r"$\alpha$ (Singularity Strength)", fontsize=12)
    plt.ylabel(r"$f(\alpha)$ (Fractal Dimension)", fontsize=12)
    plt.title("Multifractal Singularity Spectrum", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()