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
        calc_spectrum (bool): Flag quyết định có tính phổ kỳ dị hay không.
        
    Returns:
        dict: Bộ kết quả toàn diện, chứa metadata, raw data, fit data và đặc trưng phân dạng.
    """
    data = np.asarray(data)
    q_array = np.asarray(q_array)
    N = len(data)
    
    # Validation: Kiểm tra đầu vào cho phổ đa phân dạng
    if calc_spectrum and len(q_array) < 2:
        raise ValueError("Cần ít nhất 2 giá trị q để tính đạo hàm số trong biến đổi Legendre.")
        
    # 1. Tính toán hàm thăng giáng cốt lõi (Raw data)
    raw_F_q_s, raw_scales = compute_mf_dfa_core(data, s_array, q_array, m=m)
    
    # 2. Lọc vùng scaling hợp lệ (Fit data)
    fit_scales, mask = select_scaling_region(raw_scales, N, min_scale=min_scale, max_scale_ratio=max_scale_ratio)
    fit_F_q_s = raw_F_q_s[mask, :]
    
    # 3. Hồi quy tìm số mũ h(q)
    fit_results = mf_dfa_fit(fit_scales, fit_F_q_s, q_array)
    
    # 4. Đóng gói Dictionary kết quả (API chuẩn)
    result = {
        # Metadata
        "method": "MF-DFA",
        "order": m,
        "N": N,
        "q_array": q_array,
        
        # Raw Data (Dùng để visualize toàn cảnh)
        "raw_scales": raw_scales,
        "raw_F_q_s": raw_F_q_s,
        
        # Fit Data (Dùng cho mô hình)
        "fit_scales": fit_scales,
        "fit_F_q_s": fit_F_q_s,
        
        # Nested Fit Results (Chứa hq, R2, intercept, stderr...)
        "fit": fit_results
    }
    
    # 5. Các thành phần Optional
    if calc_spectrum:
        # Tính số mũ khối lượng tau(q)
        tau = compute_tau(q_array, fit_results["hq"])
        
        # Tính phổ kỳ dị f(alpha) và các đặc trưng hình học
        spectrum_results = compute_singularity_spectrum(q_array, tau)
        
        result["tau"] = tau
        result["spectrum"] = spectrum_results
        
    return result


def plot_scaling(result, q_values=None, show_fit=True, use_raw=False, figsize=(8, 6), **kwargs):
    """
    Vẽ đồ thị Log-Log biểu diễn hành vi scaling của hàm thăng giáng F_q(s).
    
    Tham số:
        result (dict): Dictionary kết quả trả về từ hàm wrapper mf_dfa().
        q_values (list/array, optional): Các giá trị q cụ thể cần vẽ.
        show_fit (bool): Có hiển thị các đường hồi quy tuyến tính hay không.
        use_raw (bool): Nếu True, vẽ scatter toàn bộ dữ liệu thô để quan sát điểm gãy (crossover).
                        Nếu False, chỉ vẽ vùng dữ liệu fit đã được chọn.
        figsize (tuple): Kích thước khung hình.
        **kwargs: Các tham số từ khóa bổ sung truyền vào plt.plot() để tùy chỉnh điểm scatter.
    """
    q_array = result["q_array"]
    fit_results = result["fit"]
    
    # Trích xuất dữ liệu
    raw_scales = result["raw_scales"]
    raw_F_q_s = result["raw_F_q_s"]
    fit_scales = result["fit_scales"]
    fit_F_q_s = result["fit_F_q_s"]
    
    # Xử lý chọn index cho q và loại bỏ các giá trị trùng lặp
    if q_values is None:
        num_q = len(q_array)
        indices = np.linspace(0, num_q - 1, min(5, num_q), dtype=int)
    else:
        indices = [np.abs(q_array - q_val).argmin() for q_val in q_values]
        indices = np.unique(indices)
        
    plt.figure(figsize=figsize)
    colors = plt.cm.viridis(np.linspace(0, 1, len(indices)))
    
    # Cấu hình cơ bản cho các điểm scatter, có thể ghi đè bằng kwargs nếu có
    scatter_style = {
        'marker': 'o',
        'linestyle': '',
        'markersize': 5,
        'alpha': 0.7,
        'markeredgecolor': 'w',
        'markeredgewidth': 0.5
    }
    scatter_style.update(kwargs)
    
    for i, idx in enumerate(indices):
        q = q_array[idx]
        h_val = fit_results["hq"][idx]
        intercept = fit_results["intercept"][idx]
        r2_val = fit_results["R2"][idx] if "R2" in fit_results else np.nan
        
        # Bỏ qua không vẽ nếu h(q) không hợp lệ
        if np.isnan(h_val):
            continue
            
        # Xác định dữ liệu scatter dựa trên cờ use_raw
        x_scatter = np.log10(raw_scales) if use_raw else np.log10(fit_scales)
        y_scatter = np.log10(raw_F_q_s[:, idx]) if use_raw else np.log10(fit_F_q_s[:, idx])
        
        # Định dạng nhãn chú thích
        if not np.isnan(r2_val):
            label_str = rf"$q={q:.1f}, h(q)={h_val:.2f}, R^2={r2_val:.3f}$"
        else:
            label_str = rf"$q={q:.1f}, h(q)={h_val:.2f}$"
            
        # Vẽ các điểm scatter (dữ liệu thực nghiệm)
        plt.plot(x_scatter, y_scatter, color=colors[i], label=label_str if not show_fit else "", **scatter_style)
        
        # Vẽ đường hồi quy giới hạn nghiêm ngặt trong vùng fit_scales
        if show_fit:
            x_fit_log = np.log10(fit_scales)
            y_fit_log = h_val * x_fit_log + intercept
            
            plt.plot(x_fit_log, y_fit_log, '-', color=colors[i], linewidth=1.5, label=label_str)
            
    plt.xlabel(r"$\log_{10}(s)$", fontsize=12)
    plt.ylabel(r"$\log_{10}(F_q(s))$", fontsize=12)
    plt.title("MF-DFA: Fluctuation Function Scaling", fontsize=14)
    
    plt.legend(loc='best', fontsize=10, framealpha=0.9, edgecolor='inherit')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_hq(result, show_error=False, figsize=(8, 6), **kwargs):
    """
    Vẽ đồ thị biểu diễn số mũ Hurst tổng quát h(q) theo q.
    
    Đồ thị này giúp chẩn đoán tính đa phân dạng:
    - Nếu h(q) là đường nằm ngang: chuỗi thời gian là đơn phân dạng (monofractal).
    - Nếu h(q) giảm dần theo q: chuỗi thời gian là đa phân dạng (multifractal).
    
    Tham số:
        result (dict): Dictionary kết quả trả về từ hàm wrapper mf_dfa().
        show_error (bool): Có hiển thị thanh sai số (error bar) hay không, 
                           yêu cầu dictionary kết quả phải có key 'hq_se'.
        figsize (tuple): Kích thước khung hình.
        **kwargs: Các tham số bổ sung truyền vào plt.plot() hoặc plt.errorbar().
    """
    q_array = result["q_array"]
    fit_results = result["fit"]
    hq = fit_results["hq"]
    
    plt.figure(figsize=figsize)
    
    # Cấu hình phong cách mặc định, có thể ghi đè bằng kwargs
    plot_style = {
        'marker': 'o',
        'linestyle': '-',
        'color': None,
        'markersize': 6,
        'linewidth': 1.5,
        'markeredgecolor': 'w',
        'markeredgewidth': 1.0
    }
    plot_style.update(kwargs)
    
    # Vẽ đồ thị có kèm thanh sai số nếu được yêu cầu và có dữ liệu
    if show_error and "hq_se" in fit_results:
        hq_se = fit_results["hq_se"]
        # Loại bỏ các tham số không tương thích với errorbar nếu vô tình truyền vào
        plt.errorbar(q_array, hq, yerr=hq_se, capsize=4, capthick=1.5, **plot_style)
    else:
        plt.plot(q_array, hq, **plot_style)
        
    # Thêm đường tham chiếu h(q) = 0.5 (tiếng ồn trắng) để dễ so sánh
    plt.axhline(y=0.5, color='gray', linestyle=':', linewidth=1.5, 
                label="Uncorrelated (h = 0.5)", zorder=0)
        
    plt.xlabel(r"$q$", fontsize=12)
    plt.ylabel(r"$h(q)$", fontsize=12)
    plt.title("MF-DFA: Generalized Hurst Exponent", fontsize=14)
    
    plt.legend(loc='best', fontsize=10, framealpha=0.9)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_tau(result, figsize=(8, 6), **kwargs):
    """
    Vẽ đồ thị biểu diễn số mũ khối lượng tau(q) theo q.
    
    Mục đích: Vẽ hàm tau(q) theo q để đánh giá tính đa phân dạng.
    - Nếu tau(q) là một đường thẳng: chuỗi thời gian là đơn phân dạng.
    - Nếu tau(q) là một đường cong (phi tuyến): chuỗi thời gian là đa phân dạng.
    
    Đặc biệt, tau(q) đóng vai trò là đầu vào quan trọng cho phép biến đổi 
    Legendre để tính toán phổ kỳ dị f(alpha).
    
    Tham số:
        result (dict): Dictionary kết quả trả về từ hàm wrapper mf_dfa().
        figsize (tuple): Kích thước khung hình.
        **kwargs: Các tham số bổ sung truyền vào plt.plot().
    """
    # Kiểm tra an toàn xem tau có tồn tại trong result không
    if "tau" not in result:
        raise ValueError("Không tìm thấy 'tau' trong result. "
                         "Hãy đảm bảo hàm wrapper đã tính toán và lưu giá trị này.")
        
    q_array = result["q_array"]
    tau = result["tau"]
    
    plt.figure(figsize=figsize)
    
    # Cấu hình phong cách mặc định, dùng marker vuông và màu xanh lá
    plot_style = {
        'marker': 's',
        'linestyle': '-',
        'color': '#2ca02c',
        'markersize': 5,
        'linewidth': 1.5,
        'markeredgecolor': 'w',
        'markeredgewidth': 0.8
    }
    plot_style.update(kwargs)
    
    # Vẽ đường cong tau(q)
    plt.plot(q_array, tau, label=r"$\tau(q)$", **plot_style)
    
    # Định dạng hiển thị
    plt.xlabel(r"$q$", fontsize=12)
    plt.ylabel(r"$\tau(q)$", fontsize=12)
    plt.title("MF-DFA: Mass Exponent", fontsize=14)
    
    plt.legend(loc='best', fontsize=10, framealpha=0.9)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_singularity(result, figsize=(8, 6), **kwargs):
    """
    Vẽ đồ thị biểu diễn phổ kỳ dị f(alpha) theo alpha.
    
    Phổ kỳ dị cho cái nhìn toàn diện về cấu trúc đa phân dạng:
    - Bề rộng của phổ (width) thể hiện mức độ đa phân dạng.
    - Đỉnh của phổ (peak_alpha) tương ứng với chiều phân dạng chính của chuỗi.
    - Dạng vòm (parabola ngược) là đặc trưng của chuỗi đa phân dạng.
    
    Tham số:
        result (dict): Dictionary kết quả trả về từ hàm wrapper mf_dfa().
        figsize (tuple): Kích thước khung hình.
        **kwargs: Các tham số bổ sung truyền vào plt.plot().
    """
    # Kiểm tra tính hợp lệ của dữ liệu đầu vào
    if "spectrum" not in result or result["spectrum"] is None:
        raise ValueError("Không tìm thấy dữ liệu phổ 'spectrum' trong result. "
                         "Hãy đảm bảo quy trình tính phổ đa phân dạng đã được bật và thực thi.")
        
    spectrum = result["spectrum"]
    
    if "alpha" not in spectrum or "f_alpha" not in spectrum:
        raise ValueError("Dữ liệu 'alpha' hoặc 'f_alpha' bị thiếu trong result['spectrum'].")
        
    alpha = spectrum["alpha"]
    f_alpha = spectrum["f_alpha"]
    
    plt.figure(figsize=figsize)
    
    # Cấu hình phong cách mặc định: dùng marker hình thoi và màu đỏ
    plot_style = {
        'marker': 'D',
        'linestyle': '-',
        'color': '#d62728',
        'markersize': 5,
        'linewidth': 1.5,
        'markeredgecolor': 'w',
        'markeredgewidth': 0.8
    }
    plot_style.update(kwargs)
    
    # Tạo nhãn chứa các đặc trưng hình học nếu có (sử dụng chuẩn biến Python)
    label_str = r"$f(\alpha)$"
    features = []
    
    # Cập nhật đúng tên key từ hàm compute_singularity_spectrum
    if "width" in spectrum and not np.isnan(spectrum["width"]):
        features.append(rf"$\Delta\alpha = {spectrum['width']:.3f}$")
    if "peak_alpha" in spectrum and not np.isnan(spectrum["peak_alpha"]):
        features.append(rf"$\alpha_0 = {spectrum['peak_alpha']:.3f}$")
        
    if features:
        label_str += " (" + ", ".join(features) + ")"
    
    # Vẽ đường cong phổ kỳ dị
    plt.plot(alpha, f_alpha, label=label_str, **plot_style)
    
    # Đánh dấu đỉnh của phổ bằng một điểm nổi bật (ngôi sao vàng)
    if "peak_alpha" in spectrum and not np.isnan(spectrum["peak_alpha"]):
        # Tìm chỉ số tương ứng với giá trị f(alpha) lớn nhất
        peak_idx = np.nanargmax(f_alpha)
        plt.plot(alpha[peak_idx], f_alpha[peak_idx], 
                 marker='*', color='gold', markersize=12, 
                 markeredgecolor='black', markeredgewidth=0.8, 
                 linestyle='None', label=r"Peak ($\alpha_0$)")
    
    # Định dạng hiển thị
    plt.xlabel(r"$\alpha$", fontsize=12)
    plt.ylabel(r"$f(\alpha)$", fontsize=12)
    plt.title("MF-DFA: Singularity Spectrum", fontsize=14)
    
    plt.legend(loc='best', fontsize=10, framealpha=0.9)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_summary(result, figsize=(14, 10)):
    """
    Vẽ bảng điều khiển tổng hợp 2x2 thể hiện toàn cảnh kết quả MF-DFA (Version 0).
    Tương thích trực tiếp với API trả về từ mf_dfa().
    
    Bố cục:
    - [0, 0]: Fluctuation Function Scaling
    - [0, 1]: Generalized Hurst Exponent
    - [1, 0]: Mass Exponent
    - [1, 1]: Singularity Spectrum
    
    Tham số:
        result (dict): Dictionary kết quả trả về từ hàm wrapper mf_dfa().
        figsize (tuple): Kích thước khung hình, mặc định (14, 10).
    """
    fig, axs = plt.subplots(2, 2, figsize=figsize)
    
    # --- 1. Góc trên bên trái (Subplot 0, 0): Scaling ---
    ax = axs[0, 0]
    # Sửa 1: Đọc đúng key từ wrapper
    if all(k in result for k in ("raw_scales", "raw_F_q_s", "q_array")):
        raw_scales = result["raw_scales"]
        raw_F_q_s = result["raw_F_q_s"]
        q_array = result["q_array"]
        
        # Chọn 3 giá trị q đại diện: min, median, max
        indices = [0, len(q_array) // 2, len(q_array) - 1]
        colors = ['#1f77b4', '#ff7f0e', '#9467bd']
        
        for i, idx in enumerate(indices):
            q_val = q_array[idx]
            # Sửa 2: Truy xuất đúng shape (n_scales, n_q)
            fluc = raw_F_q_s[:, idx]
            
            ax.loglog(raw_scales, fluc, marker='o', linestyle='-', color=colors[i],
                      markersize=4, label=rf"$q = {q_val:.1f}$")
            
        ax.set_xlabel(r"$s$", fontsize=12)
        ax.set_ylabel(r"$F_q(s)$", fontsize=12)
        ax.set_title("Fluctuation Function Scaling", fontsize=14)  # Sửa 3: Cập nhật tên
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.5)
    else:
        ax.text(0.5, 0.5, "Thiếu dữ liệu Scaling", ha='center', va='center')
        ax.set_title("Fluctuation Function Scaling", fontsize=14)

    # --- 2. Góc trên bên phải (Subplot 0, 1): h(q) ---
    ax = axs[0, 1]
    # Sửa 4: Lấy hq từ result["fit"]["hq"]
    if "q_array" in result and "fit" in result and "hq" in result["fit"]:
        fit = result["fit"]
        hq = fit["hq"]
        
        ax.plot(result["q_array"], hq, marker='o', linestyle='-',
                color='#1f77b4', markersize=5, markeredgecolor='w', markeredgewidth=0.8,
                label=r"$h(q)$")
        ax.axhline(0.5, color='gray', linestyle='--', linewidth=1.5, label=r"$h=0.5$")
        
        ax.set_xlabel(r"$q$", fontsize=12)
        ax.set_ylabel(r"$h(q)$", fontsize=12)
        ax.set_title("Generalized Hurst Exponent", fontsize=14)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.5)
        
    # --- 3. Góc dưới bên trái (Subplot 1, 0): tau(q) ---
    ax = axs[1, 0]
    # Giữ nguyên do wrapper trực tiếp lưu result["tau"]
    if "q_array" in result and "tau" in result:
        ax.plot(result["q_array"], result["tau"], marker='s', linestyle='-',
                color='#2ca02c', markersize=5, markeredgecolor='w', markeredgewidth=0.8,
                label=r"$\tau(q)$")
        
        ax.set_xlabel(r"$q$", fontsize=12)
        ax.set_ylabel(r"$\tau(q)$", fontsize=12)
        ax.set_title("Mass Exponent", fontsize=14)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.5)

    # --- 4. Góc dưới bên phải (Subplot 1, 1): f(alpha) ---
    ax = axs[1, 1]
    if "spectrum" in result and result["spectrum"] is not None:
        spectrum = result["spectrum"]
        if "alpha" in spectrum and "f_alpha" in spectrum:
            alpha = spectrum["alpha"]
            f_alpha = spectrum["f_alpha"]
            
            label_str = r"$f(\alpha)$"
            features = []
            
            if "width" in spectrum and not np.isnan(spectrum["width"]):
                features.append(rf"$\Delta\alpha = {spectrum['width']:.3f}$")
            if "peak_alpha" in spectrum and not np.isnan(spectrum["peak_alpha"]):
                features.append(rf"$\alpha_0 = {spectrum['peak_alpha']:.3f}$")
            # Sửa 5: Thêm asymmetry (A) vào chú thích
            if "asymmetry" in spectrum and not np.isnan(spectrum["asymmetry"]):
                features.append(rf"$A = {spectrum['asymmetry']:.3f}$")
                
            if features:
                label_str += " (" + ", ".join(features) + ")"
            
            ax.plot(alpha, f_alpha, marker='D', linestyle='-', color='#d62728',
                    markersize=5, markeredgecolor='w', markeredgewidth=0.8, label=label_str)
            
            # Giữ nguyên logic tìm đỉnh bằng np.nanargmax
            if len(f_alpha) > 0:
                peak_idx = np.nanargmax(f_alpha)
                ax.plot(alpha[peak_idx], f_alpha[peak_idx], marker='*', color='gold',
                        markersize=12, markeredgecolor='black', markeredgewidth=0.8,
                        linestyle='None', label=r"Peak ($\alpha_0$)")
            
            ax.set_xlabel(r"$\alpha$", fontsize=12)
            ax.set_ylabel(r"$f(\alpha)$", fontsize=12)
            ax.set_title("Singularity Spectrum", fontsize=14)
            ax.legend(loc='best', fontsize=10)
            ax.grid(True, linestyle='--', alpha=0.5)
            
    # --- Căn chỉnh và hiển thị ---
    plt.tight_layout()
    plt.show()
