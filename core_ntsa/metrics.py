import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.spatial.distance import pdist, squareform, cdist
from scipy.stats import linregress
from scipy.spatial import cKDTree
from scipy.spatial.distance import euclidean

# Correlation Dimension: Grassberger 1983
# def calculate_correlation_dimension(signal, tau, min_d, max_d, w=None, n_radii=50):
#     """
#     Tính toán và trực quan hóa Chiều tương quan (Correlation Dimension - D2) 
#     bằng thuật toán Grassberger-Procaccia có tích hợp cửa sổ Theiler.

#     Parameters:
#     -----------
#     signal  : array_like, chuỗi tín hiệu 1D (ví dụ: PPG_clean).
#     tau     : int, độ trễ thời gian (Time delay).
#     min_d   : int, số chiều nhúng tối thiểu.
#     max_d   : int, số chiều nhúng tối đa.
#     w       : int, kích thước cửa sổ Theiler. Mặc định là w = tau.
#     n_radii : int, số lượng điểm bán kính l khảo sát.

#     Returns:
#     --------
#     dimensions : list, mảng chứa các giá trị v(d) tương ứng với từng chiều nhúng.
#     """
#     signal = np.asarray(signal)
#     N = len(signal)
    
#     if w is None:
#         w = tau  # Khuyến nghị chuẩn: Cửa sổ Theiler bằng với độ trễ tau
        
#     dimensions = []
    
#     # Thiết lập đồ thị (2 Subplots)
#     fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
#     colors = plt.cm.viridis(np.linspace(0, 1, max_d - min_d + 1))
    
#     for idx, d in enumerate(range(min_d, max_d + 1)):
#         # 1. Tái tạo không gian pha (Phase Space Reconstruction)
#         Nm = N - (d - 1) * tau
#         if Nm <= 0:
#             raise ValueError(f"Dữ liệu quá ngắn để nhúng vào không gian {d} chiều với tau={tau}.")
            
#         # Tạo ma trận vector trạng thái (Nm x d)
#         X = np.array([signal[i : i + (d - 1) * tau + 1 : tau] for i in range(Nm)])
        
#         # 2. Tính ma trận khoảng cách Chebyshev (Maximum norm)
#         # pdist trả về mảng nén 1D, squareform bung nó thành ma trận đối xứng 2D
#         dist_matrix = squareform(pdist(X, metric='chebyshev'))
        
#         # 3. Áp dụng Cửa sổ Theiler
#         # Tạo một mask tam giác trên (triu) bỏ qua đường chéo chính và vùng lân cận Theiler (k = w + 1)
#         mask = np.triu(np.ones((Nm, Nm), dtype=bool), k=w + 1)
#         valid_distances = dist_matrix[mask]
        
#         # Lọc bỏ các khoảng cách bằng 0 (nếu có) để tránh lỗi log(0)
#         valid_distances = valid_distances[valid_distances > 0]
        
#         if len(valid_distances) == 0:
#             dimensions.append(np.nan)
#             continue
            
#         # 4. Xác định dải bán kính l (log-spaced)
#         # Loại bỏ 1% nhiễu ở hai đầu để dải l tập trung vào vùng phân bố chính
#         r_min = np.percentile(valid_distances, 1)
#         r_max = np.percentile(valid_distances, 99)
#         radii = np.logspace(np.log10(r_min), np.log10(r_max), n_radii)
        
#         # 5. Tính Tích phân tương quan C(l) cực nhanh bằng Binary Search
#         sorted_dists = np.sort(valid_distances)
#         # searchsorted đếm xem có bao nhiêu khoảng cách nhỏ hơn từng giá trị trong radii
#         C_l = np.searchsorted(sorted_dists, radii) / len(valid_distances)
        
#         # Loại bỏ các giá trị C(l) = 0 để có thể tính log
#         valid_idx = C_l > 0
#         r_valid = radii[valid_idx]
#         C_valid = C_l[valid_idx]
        
#         log_r = np.log10(r_valid)
#         log_C = np.log10(C_valid)
        
#         # 6. Ước lượng tự động Vùng tuyến tính (Scaling Region)
#         # Heuristic: Thường vùng tuyến tính nằm ở 30% - 70% của đồ thị log-log
#         start_idx = int(len(log_r) * 0.3)
#         end_idx = int(len(log_r) * 0.7)
        
#         if end_idx > start_idx + 2:
#             # Hồi quy tuyến tính trên vùng đã chọn
#             slope, intercept, r_value, p_value, std_err = linregress(
#                 log_r[start_idx:end_idx], log_C[start_idx:end_idx]
#             )
#         else:
#             slope = np.nan
            
#         dimensions.append(slope)
        
#         # --- Trực quan hóa Subplot 1: log(C(l)) vs log(l) ---
#         axes[0].plot(log_r, log_C, marker='.', markersize=4, linestyle='-', 
#                      color=colors[idx], label=f'd={d} (v={slope:.2f})')
        
#         # Vẽ đoạn thẳng tiếp tuyến mô tả độ dốc (Slope)
#         if not np.isnan(slope):
#             fit_r = log_r[start_idx:end_idx]
#             fit_C = slope * fit_r + intercept
#             axes[0].plot(fit_r, fit_C, color='black', linewidth=2, linestyle='--')

#     # Thiết lập hiển thị cho Subplot 1
#     axes[0].set_title(r"1. Tích phân tương quan: $\log C(l)$ vs $\log l$")
#     axes[0].set_xlabel(r"$\log_{10} l$ (Bán kính)")
#     axes[0].set_ylabel(r"$\log_{10} C(l)$ (Xác suất láng giềng)")
#     axes[0].grid(True, linestyle='--', alpha=0.6)
#     axes[0].legend(loc='upper left', fontsize='small')
    
#     # --- Trực quan hóa Subplot 2: Chiều tương quan v(d) vs d ---
#     d_range = range(min_d, max_d + 1)
#     axes[1].plot(d_range, dimensions, marker='o', linestyle='-', color='red', linewidth=2, label=r'Ước lượng $\nu(d)$')
#     axes[1].plot(d_range, d_range, linestyle='--', color='gray', alpha=0.7, label='Nhiễu lý tưởng (v = d)')
    
#     axes[1].set_title(r"2. Sự bão hòa Chiều tương quan: $\nu(d)$ vs $d$")
#     axes[1].set_xlabel(r"Số chiều nhúng $d$")
#     axes[1].set_ylabel(r"Chiều tương quan $\nu(d)$")
#     axes[1].set_xticks(d_range)
#     axes[1].grid(True, linestyle='--', alpha=0.6)
#     axes[1].legend()
    
#     plt.tight_layout()
#     plt.show()
    
#     return dimensions

def calculate_correlation_dimension(signal, tau, min_d, max_d, w=None, n_radii=50, plot_true=1):
    """
    Tính toán và trực quan hóa Chiều tương quan (Correlation Dimension - D2) 
    bằng thuật toán Grassberger-Procaccia có tích hợp cửa sổ Theiler.

    Parameters:
    -----------
    signal    : array_like, chuỗi tín hiệu 1D (ví dụ: PPG_clean).
    tau       : int, độ trễ thời gian (Time delay).
    min_d     : int, số chiều nhúng tối thiểu.
    max_d     : int, số chiều nhúng tối đa.
    w         : int, kích thước cửa sổ Theiler. Mặc định là w = tau.
    n_radii   : int, số lượng điểm bán kính l khảo sát.
    plot_true : int, 1 để hiển thị đồ thị, 0 để ẩn đồ thị và chỉ trả về mảng.

    Returns:
    --------
    dimensions : list, mảng chứa các giá trị v(d) tương ứng với từng chiều nhúng.
    """
    signal = np.asarray(signal)
    N = len(signal)
    
    if w is None:
        w = tau  # Khuyến nghị chuẩn: Cửa sổ Theiler bằng với độ trễ tau
        
    dimensions = []
    
    # Thiết lập đồ thị nếu plot_true = 1
    if plot_true:
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        colors = plt.cm.viridis(np.linspace(0, 1, max_d - min_d + 1))
        
    for idx, d in enumerate(range(min_d, max_d + 1)):
        # 1. Tái tạo không gian pha (Phase Space Reconstruction)
        Nm = N - (d - 1) * tau
        if Nm <= 0:
            raise ValueError(f"Dữ liệu quá ngắn để nhúng vào không gian {d} chiều với tau={tau}.")
            
        # Tạo ma trận vector trạng thái (Nm x d)
        X = np.array([signal[i : i + (d - 1) * tau + 1 : tau] for i in range(Nm)])
        
        # 2. Tính ma trận khoảng cách Chebyshev (Maximum norm)
        dist_matrix = squareform(pdist(X, metric='chebyshev'))
        
        # 3. Áp dụng Cửa sổ Theiler
        mask = np.triu(np.ones((Nm, Nm), dtype=bool), k=w + 1)
        valid_distances = dist_matrix[mask]
        
        # Lọc bỏ các khoảng cách bằng 0 (nếu có) để tránh lỗi log(0)
        valid_distances = valid_distances[valid_distances > 0]
        
        if len(valid_distances) == 0:
            dimensions.append(np.nan)
            continue
            
        # 4. Xác định dải bán kính l (log-spaced)
        r_min = np.percentile(valid_distances, 1)
        r_max = np.percentile(valid_distances, 99)
        radii = np.logspace(np.log10(r_min), np.log10(r_max), n_radii)
        
        # 5. Tính Tích phân tương quan C(l) cực nhanh bằng Binary Search
        sorted_dists = np.sort(valid_distances)
        C_l = np.searchsorted(sorted_dists, radii) / len(valid_distances)
        
        # Loại bỏ các giá trị C(l) = 0 để có thể tính log
        valid_idx = C_l > 0
        r_valid = radii[valid_idx]
        C_valid = C_l[valid_idx]
        
        log_r = np.log10(r_valid)
        log_C = np.log10(C_valid)
        
        # 6. Ước lượng tự động Vùng tuyến tính (Scaling Region)
        start_idx = int(len(log_r) * 0.3)
        end_idx = int(len(log_r) * 0.7)
        
        if end_idx > start_idx + 2:
            # Hồi quy tuyến tính trên vùng đã chọn
            slope, intercept, r_value, p_value, std_err = linregress(
                log_r[start_idx:end_idx], log_C[start_idx:end_idx]
            )
        else:
            slope = np.nan
            
        dimensions.append(slope)
        
        # --- Trực quan hóa Subplot 1 nếu plot_true = 1 ---
        if plot_true:
            axes[0].plot(log_r, log_C, marker='.', markersize=4, linestyle='-', 
                         color=colors[idx], label=f'd={d} (v={slope:.2f})')
            
            # Vẽ đoạn thẳng tiếp tuyến mô tả độ dốc (Slope)
            if not np.isnan(slope):
                fit_r = log_r[start_idx:end_idx]
                fit_C = slope * fit_r + intercept
                axes[0].plot(fit_r, fit_C, color='black', linewidth=2, linestyle='--')

    # Thiết lập hiển thị cho các Subplots nếu plot_true = 1
    if plot_true:
        axes[0].set_title(r"1. Tích phân tương quan: $\log C(l)$ vs $\log l$")
        axes[0].set_xlabel(r"$\log_{10} l$ (Bán kính)")
        axes[0].set_ylabel(r"$\log_{10} C(l)$ (Xác suất láng giềng)")
        axes[0].grid(True, linestyle='--', alpha=0.6)
        axes[0].legend(loc='upper left', fontsize='small')
        
        # --- Trực quan hóa Subplot 2: Chiều tương quan v(d) vs d ---
        d_range = range(min_d, max_d + 1)
        axes[1].plot(d_range, dimensions, marker='o', linestyle='-', color='red', linewidth=2, label=r'Ước lượng $\nu(d)$')
        axes[1].plot(d_range, d_range, linestyle='--', color='gray', alpha=0.7, label='Nhiễu lý tưởng (v = d)')
        
        axes[1].set_title(r"2. Sự bão hòa Chiều tương quan: $\nu(d)$ vs $d$")
        axes[1].set_xlabel(r"Số chiều nhúng $d$")
        axes[1].set_ylabel(r"Chiều tương quan $\nu(d)$")
        axes[1].set_xticks(list(d_range))
        axes[1].grid(True, linestyle='--', alpha=0.6)
        axes[1].legend()
        
        plt.tight_layout()
        plt.show()
        
    return dimensions

# Largest Lyapunov Exponent: Rosenstein 1993

def calculate_rosenstein_divergence(signal, tau, m_list, t_min, t_max, w=None):
    """
    Tính toán đường cong phân kỳ y(i) theo thuật toán Rosenstein (1993).
    
    Parameters:
    -----------
    signal : array_like, chuỗi tín hiệu 1D đầu vào.
    tau    : int, độ trễ thời gian (time delay).
    m_list : list of int, mảng chứa các số chiều nhúng cần khảo sát.
    t_min  : int, bước tiến hóa thời gian tối thiểu.
    t_max  : int, bước tiến hóa thời gian tối đa.
    w      : int, cửa sổ Theiler (Theiler window). Nếu None, tự động tính bằng FFT.
    
    Returns:
    --------
    t_steps : ndarray, trục thời gian tiến hóa.
    results : dict, từ điển chứa mảng y(i) tương ứng với từng chiều nhúng m.
    """
    signal = np.asarray(signal)
    N = len(signal)
    
    # --- CẬP NHẬT: Tự động tính Cửa sổ Theiler (w) bằng Phổ FFT ---
    if w is None:
        # Loại bỏ thành phần DC (trung bình) để tránh làm nhiễu phổ
        signal_zero_mean = signal - np.mean(signal)
        
        # Tính toán FFT (chỉ lấy phần thực rfft để tối ưu tốc độ)
        fft_vals = np.fft.rfft(signal_zero_mean)
        fft_freqs = np.fft.rfftfreq(N)
        
        # Tính Tần số Trung bình (Mean Frequency) có trọng số theo biên độ
        amplitudes = np.abs(fft_vals)
        total_amplitude = np.sum(amplitudes)
        
        if total_amplitude == 0:
            w = tau  # Fallback an toàn nếu tín hiệu là một đường thẳng tuyệt đối
        else:
            mean_freq = np.sum(fft_freqs * amplitudes) / total_amplitude
            # Chu kỳ trung bình là nghịch đảo của tần số trung bình
            w = int(np.round(1.0 / mean_freq))
            
        print(f"Hệ thống tự động thiết lập Cửa sổ Theiler (w) = {w} bước")
    # --------------------------------------------------------------
        
    results = {}
    t_steps = np.arange(t_min, t_max + 1)
    
    plt.figure(figsize=(10, 6))
    
    for m in m_list:
        # 1. Tái cấu trúc không gian pha
        M = N - (m - 1) * tau
        if M <= t_max:
            raise ValueError(f"Dữ liệu quá ngắn để nhúng m={m} và tiến hóa t_max={t_max}")
            
        X = np.array([signal[i : i + (m - 1) * tau + 1 : tau] for i in range(M)])
        
        # Giới hạn vùng tìm kiếm để đảm bảo các điểm có thể tiến hóa đủ t_max bước
        M_eval = M - t_max
        X_eval = X[:M_eval]
        
        # 2. Tìm láng giềng gần nhất (Nearest Neighbors)
        dist_matrix = cdist(X_eval, X_eval, metric='euclidean')
        
        # Áp dụng cửa sổ Theiler: gạt bỏ các láng giềng quá gần về mặt thời gian
        for j in range(M_eval):
            lower_bound = max(0, j - w)
            upper_bound = min(M_eval, j + w + 1)
            dist_matrix[j, lower_bound:upper_bound] = np.inf
            
        # Trích xuất chỉ số của láng giềng gần nhất cho mỗi điểm j
        nearest_neighbors = np.argmin(dist_matrix, axis=1)
        
        # 3. Tiến hóa và trung bình hóa Logarit (Divergence tracking)
        y_i = np.zeros(len(t_steps))
        
        for idx, i in enumerate(t_steps):
            # Cập nhật vị trí của toàn bộ các cặp điểm sau i bước
            idx_j = np.arange(M_eval) + i
            idx_hat_j = nearest_neighbors + i
            
            # Tính khoảng cách mới của các cặp điểm
            d_i = np.linalg.norm(X[idx_j] - X[idx_hat_j], axis=1)
            
            # Lọc các giá trị khoảng cách bằng 0 để tránh lỗi toán học khi tính log
            valid_mask = d_i > 0
            if np.any(valid_mask):
                y_i[idx] = np.mean(np.log(d_i[valid_mask]))
            else:
                y_i[idx] = np.nan
                
        results[m] = y_i
        
        # 4. Vẽ đồ thị đè lên cho từng m
        plt.plot(t_steps, y_i, marker='.', markersize=4, linestyle='-', label=f'm={m}')
    
    # Thiết lập hiển thị đồ thị trực quan
    plt.title("Thuật toán Rosenstein: Hàm phân kỳ $y(i)$ theo $\Delta t$")
    plt.xlabel("Thời gian tiến hóa $\Delta t$ (số bước)")
    plt.ylabel(r"$\langle \ln d_j(i) \rangle$")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()
    
    return t_steps, results


def extract_lle_rosenstein(t_steps, results, dt, fit_start, fit_end):
    """
    Trích xuất Số mũ Lyapunov lớn nhất (LLE) từ hàm phân kỳ y(i) 
    thông qua hồi quy tuyến tính trên vùng tỷ lệ (scaling region).

    Parameters:
    -----------
    t_steps   : ndarray, mảng các bước tiến hóa (đầu ra từ hàm core).
    results   : dict, từ điển chứa mảng y(i) cho từng m (đầu ra từ hàm core).
    dt        : float, chu kỳ lấy mẫu của tín hiệu (tính bằng giây).
    fit_start : int, bước bắt đầu của vùng tuyến tính (quan sát từ đồ thị).
    fit_end   : int, bước kết thúc của vùng tuyến tính (quan sát từ đồ thị).

    Returns:
    --------
    lles : dict, từ điển chứa giá trị LLE (lambda_1) tương ứng với từng m.
    """
    # Tìm chỉ số tương đối của fit_start và fit_end trong mảng t_steps
    try:
        idx_start = np.where(t_steps == fit_start)[0][0]
        idx_end = np.where(t_steps == fit_end)[0][0]
    except IndexError:
        raise ValueError("fit_start hoặc fit_end không tồn tại trong t_steps.")

    # Trục thời gian thực tế để tính đạo hàm (tính bằng giây)
    t_fit_real = t_steps[idx_start:idx_end] * dt
    lles = {}

    plt.figure(figsize=(10, 6))

    print("Kết quả trích xuất LLE (lambda_1):")
    print("-" * 40)

    for m, y_i in results.items():
        # Vẽ lại đường cong gốc (trục x giữ nguyên là số bước để dễ đối chiếu)
        plt.plot(t_steps, y_i, marker='.', markersize=4, linestyle='-', alpha=0.6, label=f'm={m}')

        # Trích xuất đoạn dữ liệu thuộc vùng tuyến tính
        y_fit = y_i[idx_start:idx_end]

        if np.isnan(y_fit).any():
            print(f"m={m:2d}: Thất bại (dữ liệu chứa NaN)")
            lles[m] = np.nan
            continue

        # Hồi quy tuyến tính trên trục thời gian vật lý
        slope, intercept, r_value, _, _ = linregress(t_fit_real, y_fit)
        lles[m] = slope

        print(f"m={m:2d}: lambda_1 = {slope:7.4f} (R^2 = {r_value**2:.4f})")

        # Tính toán đường hồi quy để vẽ đè lên đồ thị (quy đổi lại trục x là số bước)
        t_fit_steps = t_steps[idx_start:idx_end]
        fit_line = slope * (t_fit_steps * dt) + intercept
        
        # Vẽ đường đứt nét màu đen đè lên đoạn được lấy để hồi quy
        plt.plot(t_fit_steps, fit_line, color='black', linestyle='--', linewidth=2.5)

    plt.title(f"Hồi quy tuyến tính trích xuất LLE (Vùng: {fit_start} đến {fit_end})")
    plt.xlabel("Thời gian tiến hóa $\Delta t$ (số bước)")
    plt.ylabel(r"$\langle \ln d_j(i) \rangle$")
    plt.axvline(x=fit_start, color='red', linestyle=':', alpha=0.5)
    plt.axvline(x=fit_end, color='red', linestyle=':', alpha=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()

    return lles


# ==========================================
# Bước 1: Chạy hàm core để lấy dữ liệu và quan sát đồ thị
# t_steps, results = calculate_rosenstein_divergence(signal, tau=10, m_list=[3,4,5], t_min=0, t_max=100)

# Bước 2: Dựa vào mắt nhìn, thấy đoạn từ bước 20 đến 60 là thẳng nhất
# lles = extract_lle_rosenstein(t_steps, results, dt=0.01, fit_start=20, fit_end=60)

# Largest Lyapunov Exponent: Kantz 1994
# def calculate_kantz_divergence(signal, delay, m_list, eps_list, t_max, w=None):
#     """
#     Tính toán đường cong S(t) theo thuật toán Kantz (1994) với hiển thị phân cụm.
    
#     Parameters:
#     -----------
#     signal   : array_like, chuỗi tín hiệu 1D đầu vào.
#     delay    : int, độ trễ thời gian (time delay).
#     m_list   : list of int, danh sách các chiều nhúng m.
#     eps_list : list of float, danh sách các bán kính epsilon.
#     t_max    : int, số bước tiến hóa tối đa.
#     w        : int, cửa sổ Theiler. Tự động tính bằng FFT nếu None.
    
#     Returns:
#     --------
#     t_steps  : ndarray, trục thời gian tiến hóa.
#     results  : dict, từ điển chứa S(t). Cấu trúc: results[m][eps] = S_array
#     """
#     signal = np.asarray(signal)
#     N = len(signal)
    
#     # 1. Tự động thiết lập cửa sổ Theiler bằng FFT
#     if w is None:
#         signal_zm = signal - np.mean(signal)
#         fft_vals = np.fft.rfft(signal_zm)
#         fft_freqs = np.fft.rfftfreq(N)
#         amplitudes = np.abs(fft_vals)
#         total_amp = np.sum(amplitudes)
        
#         if total_amp == 0:
#             w = delay
#         else:
#             mean_freq = np.sum(fft_freqs * amplitudes) / total_amp
#             w = int(np.round(1.0 / mean_freq))
#         print(f"Hệ thống tự động thiết lập Cửa sổ Theiler (w) = {w} bước\n")

#     t_steps = np.arange(1, t_max + 1)
#     results = {m: {} for m in m_list}
    
#     # Thiết lập bảng màu cho epsilon và hình khối cho m
#     plt.figure(figsize=(12, 8))
#     colors = plt.cm.viridis(np.linspace(0, 0.9, len(eps_list)))
#     markers = ['o', 's', '^', 'D', 'v', 'p', '*']
    
#     for m_idx, m in enumerate(m_list):
#         M = N - (m - 1) * delay
#         if M <= t_max:
#             raise ValueError(f"Dữ liệu quá ngắn để tiến hóa t_max={t_max} với m={m}")
            
#         M_eval = M - t_max
#         X_eval = np.array([signal[i : i + m * delay : delay] for i in range(M_eval)])
        
#         tree = cKDTree(X_eval)
#         current_marker = markers[m_idx % len(markers)]
        
#         for eps_idx, eps in enumerate(eps_list):
#             current_color = colors[eps_idx]
#             neighbors_list = tree.query_ball_tree(tree, r=eps)
            
#             valid_refs = []
#             valid_neighs = []
            
#             # Lọc Theiler window
#             for j, neighbors in enumerate(neighbors_list):
#                 filtered = [n for n in neighbors if abs(n - j) > w]
#                 if filtered:
#                     valid_refs.append(j)
#                     valid_neighs.append(filtered)
            
#             if not valid_refs:
#                 results[m][eps] = np.full(t_max, np.nan)
#                 continue
                
#             S_t = np.zeros(t_max)
            
#             # Tiến hóa thời gian
#             for step_idx, i in enumerate(t_steps):
#                 local_logs = []
                
#                 for j, neighs in zip(valid_refs, valid_neighs):
#                     idx_j = j + (m - 1) * delay + i
#                     idx_neighs = np.array(neighs) + (m - 1) * delay + i
                    
#                     dists = np.abs(signal[idx_j] - signal[idx_neighs])
#                     dists = dists[dists > 0]
                    
#                     if len(dists) > 0:
#                         local_mean = np.mean(dists)
#                         local_logs.append(np.log(local_mean))
                
#                 if local_logs:
#                     S_t[step_idx] = np.mean(local_logs)
#                 else:
#                     S_t[step_idx] = np.nan
                    
#             results[m][eps] = S_t
            
#             # Vẽ đường thẳng
#             plt.plot(t_steps, S_t, color=current_color, marker=current_marker, 
#                      markersize=4, linestyle='-', linewidth=1.5, alpha=0.7)
            
#     # 2. Xây dựng Custom Legend (Chú thích phân tách riêng Epsilon và m)
#     legend_elements = []
    
#     # Nhóm Epsilon (Màu sắc)
#     legend_elements.append(Line2D([0], [0], marker='none', linestyle='none', label='--- Bán kính $\epsilon$ ---'))
#     for eps_idx, eps in enumerate(eps_list):
#         legend_elements.append(Line2D([0], [0], color=colors[eps_idx], lw=2, label=f'$\epsilon$ = {eps}'))
        
#     # Nhóm m (Hình khối)
#     legend_elements.append(Line2D([0], [0], marker='none', linestyle='none', label='\n--- Chiều nhúng m ---'))
#     for m_idx, m in enumerate(m_list):
#         current_marker = markers[m_idx % len(markers)]
#         legend_elements.append(Line2D([0], [0], color='gray', marker=current_marker, 
#                                       linestyle='None', markersize=6, label=f'm = {m}'))
                                      
#     plt.title("Thuật toán Kantz: Đánh giá sự hội tụ của hàm $S(t)$")
#     plt.xlabel("Thời gian tiến hóa $t$ (số bước)")
#     plt.ylabel(r"$S(t) = \langle \ln \langle \text{dist} \rangle_{\mathcal{U}} \rangle_t$")
#     plt.grid(True, linestyle='--', alpha=0.6)
    
#     # Đặt legend ở ngoài đồ thị để không che khuất dữ liệu
#     plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
#     plt.tight_layout()
#     plt.show()
    
#     return t_steps, results

def calculate_kantz_divergence(signal, delay, m_list, eps_list, t_max, w=None):
    """
    Tính toán đường cong S(t) theo thuật toán Kantz sửa đổi (Euclidean m-D).
    
    Parameters:
    -----------
    signal   : array_like, chuỗi tín hiệu 1D đầu vào.
    delay    : int, độ trễ thời gian (time delay).
    m_list   : list of int, danh sách các chiều nhúng m.
    eps_list : list of float, danh sách các bán kính epsilon.
    t_max    : int, số bước tiến hóa tối đa.
    w        : int, cửa sổ Theiler. Nếu None, mặc định w = 2 * delay.
    
    Returns:
    --------
    t_steps  : ndarray, trục thời gian tiến hóa.
    results  : dict, từ điển chứa S(t). Cấu trúc: results[m][eps] = S_array
    """
    signal = np.asarray(signal)
    N = len(signal)
    
    # Thiết lập cửa sổ Theiler chuẩn (decorrelation time)
    if w is None:
        w = 2 * delay
        print(f"Hệ thống thiết lập Cửa sổ Theiler mặc định (w) = {w} bước\n")

    t_steps = np.arange(1, t_max + 1)
    results = {m: {} for m in m_list}
    
    # Thiết lập trực quan hóa
    plt.figure(figsize=(12, 8))
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(eps_list)))
    markers = ['o', 's', '^', 'D', 'v', 'p', '*']
    
    for m_idx, m in enumerate(m_list):
        M = N - (m - 1) * delay
        if M <= t_max:
            raise ValueError(f"Dữ liệu quá ngắn để tiến hóa t_max={t_max} với m={m}")
            
        M_eval = M - t_max
        # Không gian nhúng tại thời điểm ban đầu để xây dựng KD-Tree
        X_eval = np.array([signal[i : i + m * delay : delay] for i in range(M_eval)])
        
        tree = cKDTree(X_eval)
        current_marker = markers[m_idx % len(markers)]
        
        for eps_idx, eps in enumerate(eps_list):
            current_color = colors[eps_idx]
            neighbors_list = tree.query_ball_tree(tree, r=eps)
            
            valid_refs = []
            valid_neighs = []
            
            # Lọc Theiler window
            for j, neighbors in enumerate(neighbors_list):
                filtered = [n for n in neighbors if abs(n - j) > w]
                if filtered:
                    valid_refs.append(j)
                    valid_neighs.append(filtered)
            
            if not valid_refs:
                results[m][eps] = np.full(t_max, np.nan)
                continue
                
            S_t = np.zeros(t_max)
            
            # Quá trình tiến hóa theo không gian đa chiều
            for step_idx, i in enumerate(t_steps):
                local_logs = []
                
                for j, neighs in zip(valid_refs, valid_neighs):
                    # Trích xuất vector nhúng m-chiều của điểm tham chiếu tại t+i
                    ref_vector = signal[j + i : j + i + m * delay : delay]
                    
                    # Trích xuất ma trận vector nhúng m-chiều của láng giềng tại t+i
                    neigh_vectors = np.array([
                        signal[n + i : n + i + m * delay : delay] 
                        for n in neighs
                    ])
                    
                    # Tính khoảng cách Euclidean thực sự trong không gian pha
                    dists = np.linalg.norm(neigh_vectors - ref_vector, axis=1)
                    
                    # Bỏ các khoảng cách bằng 0
                    dists = dists[dists > 0]
                    if len(dists) > 0:
                        local_mean = np.mean(dists)
                        local_logs.append(np.log(local_mean))
                
                if local_logs:
                    S_t[step_idx] = np.mean(local_logs)
                else:
                    S_t[step_idx] = np.nan
                    
            results[m][eps] = S_t
            
            plt.plot(t_steps, S_t, color=current_color, marker=current_marker, 
                     markersize=4, linestyle='-', linewidth=1.5, alpha=0.7)
            
    # Xây dựng bảng chú thích (Legend)
    legend_elements = []
    legend_elements.append(Line2D([0], [0], marker='none', linestyle='none', label='--- Bán kính epsilon ---'))
    for eps_idx, eps in enumerate(eps_list):
        legend_elements.append(Line2D([0], [0], color=colors[eps_idx], lw=2, label=f'eps = {eps:.4f}'))
        
    legend_elements.append(Line2D([0], [0], marker='none', linestyle='none', label='\n--- Chiều nhúng m ---'))
    for m_idx, m in enumerate(m_list):
        current_marker = markers[m_idx % len(markers)]
        legend_elements.append(Line2D([0], [0], color='gray', marker=current_marker, 
                                      linestyle='None', markersize=6, label=f'm = {m}'))
                                      
    plt.title("Thuật toán Kantz (Modified m-D): Đánh giá sự hội tụ của hàm S(t)")
    plt.xlabel("Thời gian tiến hóa t (số bước)")
    plt.ylabel("S(t) = < ln < dist_mD >_U >_t")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
    plt.tight_layout()
    plt.show()
    
    return t_steps, results

def extract_kantz_slopes(t_steps, results_kantz, fit_start, fit_end, sampling_rate=1.0):
    """
    Trích xuất hệ số góc (LLE), phân nhóm theo Epsilon và chuẩn hóa theo thời gian thực.
    
    Parameters:
    -----------
    t_steps       : ndarray, mảng thời gian tiến hóa (trục X).
    results_kantz : dict, từ điển chứa S(t) (đầu ra từ calculate_kantz_divergence).
    fit_start     : int, bước thời gian bắt đầu vùng tuyến tính.
    fit_end       : int, bước thời gian kết thúc vùng tuyến tính.
    sampling_rate : float, tần số lấy mẫu Fs (Hz) hoặc 1/dt. Mặc định là 1.0 (cho hệ rời rạc).
    
    Returns:
    --------
    slopes_info   : dict, từ điển chứa cấu trúc slopes_info[eps][m] = {slope, r_squared}.
    """
    try:
        start_idx = np.where(t_steps == fit_start)[0][0]
        end_idx = np.where(t_steps == fit_end)[0][0]
    except IndexError:
        raise ValueError(f"Khoảng {fit_start}-{fit_end} không nằm trong t_steps.")
        
    t_fit = t_steps[start_idx:end_idx + 1]
    slopes_info = {}
    
    m_list = sorted(list(results_kantz.keys()))
    eps_set = set()
    for m in m_list:
        eps_set.update(results_kantz[m].keys())
    eps_list = sorted(list(eps_set))
    
    print(f"--- KẾT QUẢ TRÍCH XUẤT LLE (t = {fit_start} đến {fit_end}, Fs = {sampling_rate} Hz) ---")
    
    for eps in eps_list:
        slopes_info[eps] = {}
        print(f"\n>> Bán kính Epsilon = {eps:<6.4f}")
        print(f"{'Chiều nhúng m':<15} | {'lambda_1 (1/s)':<15} | {'R^2':<10}")
        print("-" * 48)
        
        for m in m_list:
            if eps not in results_kantz[m]:
                continue
                
            S_t = results_kantz[m][eps]
            S_fit = S_t[start_idx:end_idx + 1]
            
            if np.isnan(S_fit).any():
                slopes_info[eps][m] = {'slope': np.nan, 'r_squared': np.nan}
                print(f"m={m:<13} | {'NaN':<15} | {'NaN':<10}")
                continue
                
            # Hồi quy tuyến tính trên số bước tiến hóa
            slope_discrete, intercept, r_value, _, _ = linregress(t_fit, S_fit)
            r_squared = r_value ** 2
            
            # CHUẨN HÓA: Nhân hệ số góc với tần số lấy mẫu để ra LLE thực
            slope_continuous = slope_discrete * sampling_rate
            
            slopes_info[eps][m] = {
                'slope': slope_continuous,
                'r_squared': r_squared,
                'intercept': intercept
            }
            
            print(f"m={m:<13} | {slope_continuous:<15.4f} | {r_squared:<10.4f}")
            
    return slopes_info

def calculate_wolf_lle(signal, delay, m, evolve_steps, dt=1.0, max_angle=0.3):
    """
    Tính Số mũ Lyapunov lớn nhất (LLE) theo thuật toán Wolf (1985).
    
    Parameters:
    -----------
    signal       : array_like, chuỗi tín hiệu 1D.
    delay        : int, độ trễ thời gian tau.
    m            : int, số chiều nhúng không gian pha.
    evolve_steps : int, số bước tiến hóa trước khi thực hiện thay thế (replacement).
    dt           : float, bước thời gian (1/Fs) để chuẩn hóa LLE ra đơn vị 1/s.
    max_angle    : float, hình phạt góc tối đa (radians) khi tìm láng giềng mới.
    
    Returns:
    --------
    lle          : float, Số mũ Lyapunov lớn nhất.
    """
    signal = np.asarray(signal)
    N = len(signal)
    M = N - (m - 1) * delay
    
    # Tái cấu trúc không gian pha m-chiều
    X = np.array([signal[i : i + m * delay : delay] for i in range(M)])
    
    sum_lyap = 0.0
    num_replacements = 0
    
    # Bước 1: Khởi tạo tại điểm đầu tiên
    current_idx = 0
    
    # Tìm láng giềng gần nhất ban đầu (loại trừ chính nó)
    dists = np.linalg.norm(X - X[current_idx], axis=1)
    dists[current_idx] = np.inf 
    neighbor_idx = np.argmin(dists)
    
    # Quá trình bám đuôi dọc theo quỹ đạo
    while current_idx + evolve_steps < M and neighbor_idx + evolve_steps < M:
        # Tọa độ sau khi tiến hóa
        curr_next = current_idx + evolve_steps
        neigh_next = neighbor_idx + evolve_steps
        
        # Vector khoảng cách trước và sau tiến hóa
        vec_start = X[neighbor_idx] - X[current_idx]
        vec_end = X[neigh_next] - X[curr_next]
        
        L_start = np.linalg.norm(vec_start)
        L_end = np.linalg.norm(vec_end)
        
        # Bỏ qua nếu khoảng cách chạm 0 (gặp nhiễu bất thường)
        if L_start == 0 or L_end == 0:
            current_idx += evolve_steps
            continue
            
        # Cộng dồn tốc độ phân kỳ
        sum_lyap += np.log(L_end / L_start)
        num_replacements += 1
        
        # Bước Thay thế (Replacement)
        # Tìm láng giềng mới quanh curr_next sao cho bảo toàn khoảng cách và hướng
        dists_new = np.linalg.norm(X - X[curr_next], axis=1)
        
        # Chỉ xét các điểm có thể tiến hóa tiếp
        valid_mask = np.arange(M) < (M - evolve_steps)
        # Loại trừ điểm hiện tại để không tự nhận chính mình
        valid_mask[curr_next] = False 
        
        best_penalty = np.inf
        best_neighbor = -1
        
        # Lọc thô các ứng viên trong bán kính cục bộ (tối ưu tốc độ)
        local_radius = L_end * 2.0
        candidate_indices = np.where(valid_mask & (dists_new < local_radius))[0]
        
        if len(candidate_indices) == 0:
            # Nếu không tìm thấy ai trong bán kính nhỏ, lấy toàn bộ
            candidate_indices = np.where(valid_mask)[0]
            
        for k in candidate_indices:
            vec_new = X[k] - X[curr_next]
            L_new = np.linalg.norm(vec_new)
            
            if L_new == 0:
                continue
                
            # Tính góc giữa vector cũ (vec_end) và vector ứng viên mới
            cos_theta = np.dot(vec_end, vec_new) / (L_end * L_new)
            # Khống chế lỗi float domain [-1, 1]
            cos_theta = np.clip(cos_theta, -1.0, 1.0) 
            angle = np.arccos(cos_theta)
            
            # Hàm hình phạt (Penalty function): Ưu tiên khoảng cách nhỏ và góc nhỏ
            # Trọng số có thể tinh chỉnh, Wolf ưu tiên bảo toàn góc (angle)
            if angle < max_angle:
                penalty = L_new + angle * L_new 
                if penalty < best_penalty:
                    best_penalty = penalty
                    best_neighbor = k
                    
        # Nếu không tìm được ai thỏa mãn góc, giữ nguyên láng giềng cũ (nếu không quá xa)
        # hoặc buộc phải lấy điểm có hình phạt thấp nhất
        if best_neighbor != -1:
            neighbor_idx = best_neighbor
        else:
            neighbor_idx = neigh_next
            
        current_idx = curr_next
        
    # Tính LLE trung bình và chuẩn hóa theo thời gian
    if num_replacements > 0:
        total_time = num_replacements * evolve_steps * dt
        lle = sum_lyap / total_time
        return lle
    else:
        return np.nan
    
def calculate_kantz_derivative(t_steps, results_kantz, smoothing_window=3):
    """
    Tính đạo hàm bậc 1 của đường cong S(t) để nhận diện vùng tuyến tính.
    
    Parameters:
    -----------
    t_steps          : ndarray, mảng trục thời gian tiến hóa.
    results_kantz    : dict, từ điển chứa S(t) từ hàm calculate_kantz_divergence.
    smoothing_window : int, kích thước cửa sổ trung bình trượt làm mượt đạo hàm.
                       Sử dụng số lẻ (vd: 3, 5). Đặt bằng 1 nếu không muốn làm mượt.
                       
    Returns:
    --------
    derivatives      : dict, chứa mảng đạo hàm S'(t). Cấu trúc: derivatives[m][eps].
    """
    derivatives = {m: {} for m in results_kantz.keys()}
    
    # Trích xuất danh sách m và epsilon để đồng bộ màu sắc/marker
    m_list = sorted(list(results_kantz.keys()))
    eps_set = set()
    for m in m_list:
        eps_set.update(results_kantz[m].keys())
    eps_list = sorted(list(eps_set))
    
    # Thiết lập trực quan hóa
    plt.figure(figsize=(12, 8))
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(eps_list)))
    markers = ['o', 's', '^', 'D', 'v', 'p', '*']
    
    for m_idx, m in enumerate(m_list):
        current_marker = markers[m_idx % len(markers)]
        
        for eps_idx, eps in enumerate(eps_list):
            if eps not in results_kantz[m]:
                continue
                
            current_color = colors[eps_idx]
            S_t = results_kantz[m][eps]
            
            # Bỏ qua nếu mảng chứa toàn NaN
            if np.all(np.isnan(S_t)):
                derivatives[m][eps] = np.full_like(t_steps, np.nan)
                continue
                
            # Tính đạo hàm trung tâm (central difference)
            dS_dt = np.gradient(S_t, t_steps)
            
            # Làm mượt đạo hàm bằng convolution (trung bình trượt)
            if smoothing_window > 1:
                pad_size = smoothing_window // 2
                padded_dS = np.pad(dS_dt, (pad_size, pad_size), mode='edge')
                window = np.ones(smoothing_window) / smoothing_window
                dS_dt = np.convolve(padded_dS, window, mode='valid')
                
            derivatives[m][eps] = dS_dt
            
            plt.plot(t_steps, dS_dt, color=current_color, marker=current_marker,
                     markersize=4, linestyle='-', linewidth=1.5, alpha=0.7)
                     
    # Xây dựng bảng chú thích (Legend)
    legend_elements = [
        Line2D([0], [0], marker='none', linestyle='none', label='--- Bán kính epsilon ---')
    ]
    for eps_idx, eps in enumerate(eps_list):
        legend_elements.append(
            Line2D([0], [0], color=colors[eps_idx], lw=2, label=f'eps = {eps:.4f}')
        )
        
    legend_elements.append(
        Line2D([0], [0], marker='none', linestyle='none', label='\n--- Chiều nhúng m ---')
    )
    for m_idx, m in enumerate(m_list):
        current_marker = markers[m_idx % len(markers)]
        legend_elements.append(
            Line2D([0], [0], color='gray', marker=current_marker, 
                   linestyle='None', markersize=6, label=f'm = {m}')
        )
                                      
    plt.title("Đạo hàm S'(t): Nhận diện Vùng tuyến tính (Plateau)")
    plt.xlabel("Thời gian tiến hóa t (số bước)")
    plt.ylabel("Tốc độ giãn nở S'(t)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
    plt.tight_layout()
    plt.show()
    
    return derivatives
