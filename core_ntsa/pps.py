import numpy as np
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

# ==========================================
# CÁC HÀM NỘI BỘ (KHÔNG GỌI TRỰC TIẾP)
# ==========================================

def _embed_phase_space(ts, tau, m):
    """Hàm nội bộ: Tái cấu trúc không gian pha (Takens' Embedding)."""
    N = len(ts)
    N_embedded = N - (m - 1) * tau
    
    if N_embedded <= 0:
        raise ValueError("Chuỗi thời gian quá ngắn so với tham số tau và m.")
        
    Z = np.array([ts[i : i + (m - 1) * tau + 1 : tau] for i in range(N_embedded)])
    return Z

def _generate_pps_indices(Z, tree, rho, cutoff_factor=10.0):
    """Hàm nội bộ: Lõi thuật toán sinh mảng chỉ số PPS."""
    N_embedded = len(Z)
    indices = np.zeros(N_embedded, dtype=int)
    
    current_idx = np.random.randint(0, N_embedded)
    indices[0] = current_idx
    
    search_radius = cutoff_factor * rho + 1e-12
    
    for i in range(1, N_embedded):
        neighbors = tree.query_ball_point(Z[current_idx], r=search_radius)
        
        if not neighbors:
            neighbors = [current_idx]
            
        neighbors = np.array(neighbors)
        diffs = Z[neighbors] - Z[current_idx]
        distances = np.linalg.norm(diffs, axis=1)
        
        rho_safe = max(rho, 1e-12)
        weights = np.exp(-distances / rho_safe)
        
        weight_sum = np.sum(weights)
        if weight_sum == 0 or not np.isfinite(weight_sum):
            prob = np.ones(len(weights)) / len(weights)
        else:
            prob = weights / weight_sum
            
        chosen_neighbor = np.random.choice(neighbors, p=prob)
        
        if chosen_neighbor + 1 < N_embedded:
            current_idx = chosen_neighbor + 1
        else:
            current_idx = np.random.randint(0, N_embedded)
            
        indices[i] = current_idx
        
    return indices

def _count_matching_segments(indices, min_length=2):
    """Hàm nội bộ: Đếm số phân đoạn giữ nguyên cấu trúc nhịp."""
    count = 0
    current_length = 1
    
    for i in range(1, len(indices)):
        if indices[i] == indices[i - 1] + 1:
            current_length += 1
        else:
            if current_length >= min_length:
                count += 1
            current_length = 1
            
    if current_length >= min_length:
        count += 1
        
    return count

# ==========================================
# CÁC HÀM GIAO DIỆN NGƯỜI DÙNG (API CHÍNH)
# ==========================================

def optimize_rho(signal, tau, m, rho_candidates, trials=10, min_length=2, cutoff_factor=10.0):
    """
    Quét Grid Search để tìm tham số rho tối ưu trực tiếp từ tín hiệu gốc.
    
    Parameters:
        signal (np.ndarray): Chuỗi tín hiệu 1D ban đầu.
        tau (int): Độ trễ thời gian.
        m (int): Số chiều nhúng.
        rho_candidates (np.ndarray): Mảng các giá trị rho cần quét.
        trials (int): Số lần chạy ngẫu nhiên cho mỗi rho để lấy kỳ vọng.
        min_length (int): Chiều dài tối thiểu của đoạn trùng khớp.
        cutoff_factor (float): Hệ số bán kính tìm kiếm láng giềng.
        
    Returns:
        float: Giá trị rho đạt số đoạn trùng khớp kỳ vọng cao nhất.
    """
    # Tính toán Z và tree ĐÚNG 1 LẦN để tối ưu hiệu năng
    Z = _embed_phase_space(signal, tau, m)
    tree = cKDTree(Z)
    
    max_segments = -1
    optimal_rho = rho_candidates[0]
    
    for rho in rho_candidates:
        total_segments = 0
        for _ in range(trials):
            indices = _generate_pps_indices(Z, tree, rho, cutoff_factor)
            total_segments += _count_matching_segments(indices, min_length)
            
        expected_segments = total_segments / trials
        
        if expected_segments > max_segments:
            max_segments = expected_segments
            optimal_rho = rho
            
    return optimal_rho

def generate_pps_signal(signal, tau, m, rho, cutoff_factor=10.0):
    """
    Tạo chuỗi surrogate vô hướng 1D trực tiếp từ tín hiệu gốc.
    
    Parameters:
        signal (np.ndarray): Chuỗi tín hiệu 1D ban đầu.
        tau (int): Độ trễ thời gian.
        m (int): Số chiều nhúng.
        rho (float): Bán kính nhiễu.
        cutoff_factor (float): Hệ số bán kính tìm kiếm láng giềng.
        
    Returns:
        np.ndarray: Tín hiệu surrogate 1D.
    """
    # Tính toán Z và tree tại chỗ
    Z = _embed_phase_space(signal, tau, m)
    tree = cKDTree(Z)
    
    indices = _generate_pps_indices(Z, tree, rho, cutoff_factor)
    return signal[indices]


# def _generate_pps_indices_update(Z, safe_tree, rho, N_original, cutoff_factor=10.0):
#     """
#     Lõi thuật toán sinh mảng chỉ số PPS.
#     Khắc phục lỗi hụt chiều dài và bẫy vòng lặp biên (Boundary Trap).
    
#     Parameters:
#         Z (np.ndarray): Không gian pha.
#         safe_tree (cKDTree): Cây tìm kiếm láng giềng đã loại bỏ điểm cuối.
#         rho (float): Bán kính nhiễu.
#         N_original (int): Chiều dài tín hiệu gốc.
#         cutoff_factor (float): Hệ số cắt cụt bán kính tìm kiếm.
        
#     Returns:
#         np.ndarray: Mảng chỉ số của chuỗi surrogate.
#     """
#     safe_max_idx = len(Z) - 2
#     indices = np.zeros(N_original, dtype=int)
    
#     current_idx = np.random.randint(0, safe_max_idx + 1)
#     indices[0] = current_idx
    
#     search_radius = cutoff_factor * rho + 1e-12
    
#     for i in range(1, N_original):
#         # Chốt chặn an toàn: Bẻ gãy bẫy vòng lặp vô hạn ở điểm cuối
#         if current_idx > safe_max_idx:
#             current_idx = np.random.randint(0, safe_max_idx + 1)
#             indices[i] = current_idx
#             continue
            
#         neighbors = safe_tree.query_ball_point(Z[current_idx], r=search_radius)
        
#         if not neighbors:
#             neighbors = [current_idx]
            
#         neighbors = np.array(neighbors)
#         diffs = Z[neighbors] - Z[current_idx]
#         distances = np.linalg.norm(diffs, axis=1)
        
#         rho_safe = max(rho, 1e-12)
#         weights = np.exp(-distances / rho_safe)
        
#         weight_sum = np.sum(weights)
#         if weight_sum == 0 or not np.isfinite(weight_sum):
#             prob = np.ones(len(weights)) / len(weights)
#         else:
#             prob = weights / weight_sum
            
#         chosen_neighbor = np.random.choice(neighbors, p=prob)
        
#         # Bước nhảy động lực học
#         current_idx = chosen_neighbor + 1
#         indices[i] = current_idx
        
#     return indices

# def optimize_rho_update(signal, tau, m, rho_candidates, trials=10, min_length=2, cutoff_factor=10.0):
#     """
#     Quét Grid Search để tìm tham số rho tối ưu trực tiếp từ tín hiệu gốc.
    
#     Parameters:
#         signal (np.ndarray): Chuỗi tín hiệu 1D ban đầu.
#         tau (int): Độ trễ thời gian.
#         m (int): Số chiều nhúng.
#         rho_candidates (np.ndarray): Mảng các giá trị rho cần quét.
#         trials (int): Số lần chạy ngẫu nhiên cho mỗi rho để lấy kỳ vọng.
#         min_length (int): Chiều dài tối thiểu của đoạn trùng khớp.
#         cutoff_factor (float): Hệ số bán kính tìm kiếm láng giềng.
        
#     Returns:
#         float: Giá trị rho tối ưu.
#     """
#     N_original = len(signal)
#     Z = _embed_phase_space(signal, tau, m)
    
#     # Xây dựng safe_tree loại bỏ điểm cuối cùng để tránh lỗi tràn chỉ số
#     safe_tree = cKDTree(Z[:-1])
    
#     max_segments = -1
#     optimal_rho = rho_candidates[0]
    
#     for rho in rho_candidates:
#         total_segments = 0
#         for _ in range(trials):
#             indices = _generate_pps_indices_update(Z, safe_tree, rho, N_original, cutoff_factor)
#             total_segments += _count_matching_segments(indices, min_length)
            
#         expected_segments = total_segments / trials
        
#         if expected_segments > max_segments:
#             max_segments = expected_segments
#             optimal_rho = rho
            
#     return optimal_rho


# def generate_pps_signal_update(signal, tau, m, rho, cutoff_factor=10.0):
#     """
#     Tạo chuỗi surrogate vô hướng 1D trực tiếp từ tín hiệu gốc.
    
#     Parameters:
#         signal (np.ndarray): Chuỗi tín hiệu 1D ban đầu.
#         tau (int): Độ trễ thời gian.
#         m (int): Số chiều nhúng.
#         rho (float): Bán kính nhiễu.
#         cutoff_factor (float): Hệ số bán kính tìm kiếm láng giềng.
        
#     Returns:
#         np.ndarray: Tín hiệu surrogate 1D (độ dài bằng signal gốc).
#     """
#     N_original = len(signal)
#     Z = _embed_phase_space(signal, tau, m)
    
#     # Xây dựng safe_tree loại bỏ điểm cuối cùng
#     safe_tree = cKDTree(Z[:-1])
    
#     indices = _generate_pps_indices_update(Z, safe_tree, rho, N_original, cutoff_factor)
    
#     # Trích xuất tín hiệu vô hướng từ thành phần đầu tiên của vector nhúng
#     return Z[indices, 0]


def _generate_pps_indices_update(Z, rho, N_original):
    """
    Lõi thuật toán sinh mảng chỉ số PPS (Thuần túy Toán học - Vectorized).
    Đã vá lỗi Underflow tại biên không gian pha theo giới hạn láng giềng gần nhất.
    
    Parameters:
        Z (np.ndarray): Không gian pha.
        rho (float): Bán kính nhiễu.
        N_original (int): Chiều dài tín hiệu gốc.
        
    Returns:
        np.ndarray: Mảng chỉ số của chuỗi surrogate (độ dài N_original).
    """
    N_embedded = len(Z)
    indices = np.zeros(N_original, dtype=int)

    # Tập ứng viên loại bỏ điểm cuối cùng để luôn tồn tại bước nhảy t+1
    valid_candidates = np.arange(N_embedded - 1)
    Z_candidates = Z[:-1]

    # Chọn điểm bắt đầu ngẫu nhiên
    current_idx = np.random.choice(valid_candidates)
    indices[0] = current_idx

    rho_safe = max(rho, 1e-12)

    for i in range(1, N_original):
        current_state = Z[current_idx]

        # 1. Tính khoảng cách Euclid tới TOÀN BỘ ứng viên
        distances = np.linalg.norm(Z_candidates - current_state, axis=1)

        # 2. Tính trọng số láng giềng theo phương trình hàm mũ
        weights = np.exp(-distances / rho_safe)
        weight_sum = np.sum(weights)

        # 3. Bắt lỗi Float Underflow khi current_state ở biên (hoặc rho quá nhỏ)
        if weight_sum == 0 or np.isnan(weight_sum):
            # Hệ suy biến về Nearest Neighbor
            prob = np.zeros(len(valid_candidates))
            nearest_idx = np.argmin(distances)
            prob[nearest_idx] = 1.0
        else:
            prob = weights / weight_sum

        # 4. Đổ xúc xắc có trọng số
        chosen_idx = np.random.choice(valid_candidates, p=prob)

        # 5. Bước nhảy động lực học: Trượt tới t+1
        current_idx = chosen_idx + 1
        indices[i] = current_idx

    return indices


def optimize_rho_update(signal, tau, m, rho_candidates, trials=10, min_length=2):
    """
    Quét Grid Search để tìm tham số rho tối ưu trực tiếp từ tín hiệu gốc.
    
    Parameters:
        signal (np.ndarray): Chuỗi tín hiệu 1D ban đầu.
        tau (int): Độ trễ thời gian.
        m (int): Số chiều nhúng.
        rho_candidates (np.ndarray): Mảng các giá trị rho cần quét.
        trials (int): Số lần chạy ngẫu nhiên cho mỗi rho để lấy kỳ vọng.
        min_length (int): Chiều dài tối thiểu của đoạn trùng khớp.
        
    Returns:
        float: Giá trị rho tối ưu.
    """
    N_original = len(signal)
    Z = _embed_phase_space(signal, tau, m)
    
    max_segments = -1
    optimal_rho = rho_candidates[0]
    
    for rho in rho_candidates:
        total_segments = 0
        for _ in range(trials):
            indices = _generate_pps_indices_update(Z, rho, N_original)
            total_segments += _count_matching_segments(indices, min_length)
            
        expected_segments = total_segments / trials
        
        if expected_segments > max_segments:
            max_segments = expected_segments
            optimal_rho = rho
            
    return optimal_rho


def generate_pps_signal_update(signal, tau, m, rho):
    """
    Tạo chuỗi surrogate vô hướng 1D trực tiếp từ tín hiệu gốc.
    
    Parameters:
        signal (np.ndarray): Chuỗi tín hiệu 1D ban đầu.
        tau (int): Độ trễ thời gian.
        m (int): Số chiều nhúng.
        rho (float): Bán kính nhiễu.
        
    Returns:
        np.ndarray: Tín hiệu surrogate 1D (độ dài bằng signal gốc).
    """
    N_original = len(signal)
    Z = _embed_phase_space(signal, tau, m)
    
    indices = _generate_pps_indices_update(Z, rho, N_original)
    
    return Z[indices, 0]


def plot_phase_space(original_ts, surrogate_ts, delay, optimal_rho):
    """
    Vẽ đối chiếu quỹ đạo 2D bằng biểu đồ phân tán (scatter plot).
    """
    orig_x = original_ts[:-delay]
    orig_y = original_ts[delay:]
    
    surr_x = surrogate_ts[:-delay]
    surr_y = surrogate_ts[delay:]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=100)
    fig.suptitle("Tái tạo Hình 1: Bảo toàn Đa tạp (Scatter Plot)", fontsize=16, fontweight='bold', y=1.05)
    
    # Đồ thị dữ liệu gốc
    axes[0].scatter(orig_x, orig_y, s=0.5, color='#1f77b4', alpha=0.3)
    axes[0].set_title("Hệ Rössler (Dữ liệu gốc)", fontsize=14)
    axes[0].set_xlabel(r"$x(t)$", fontsize=12)
    axes[0].set_ylabel(r"$x(t - \tau)$", fontsize=12)
    axes[0].grid(True, linestyle='--', alpha=0.5)
    axes[0].set_aspect('equal', adjustable='datalim')
    
    # Đồ thị dữ liệu surrogate
    axes[1].scatter(surr_x, surr_y, s=0.5, color='#d62728', alpha=0.3)
    axes[1].set_title(rf"PPS Surrogate ($\rho = {optimal_rho:.4f}$)", fontsize=14)
    axes[1].set_xlabel(r"$x(t)$", fontsize=12)
    axes[1].set_ylabel(r"$x(t - \tau)$", fontsize=12)
    axes[1].grid(True, linestyle='--', alpha=0.5)
    axes[1].set_aspect('equal', adjustable='datalim')
    
    plt.tight_layout()
    plt.show()

def plot_time_domain(original_ts, surrogate_ts, n_samples=1000):
    """
    Vẽ đối chiếu chuỗi thời gian của dữ liệu gốc và dữ liệu surrogate.
    """
    fig, axes = plt.subplots(2, 1, figsize=(12, 8), dpi=100, sharex=True)
    fig.suptitle("So sánh miền thời gian: Gốc vs PPS Surrogate", fontsize=16, fontweight='bold')
    
    # Đồ thị dữ liệu gốc
    axes[0].plot(original_ts[:n_samples], color='#1f77b4', linewidth=0.8, label='Gốc')
    axes[0].set_title("Dữ liệu gốc", fontsize=12)
    axes[0].set_ylabel("Biên độ", fontsize=10)
    axes[0].grid(True, linestyle='--', alpha=0.5)
    axes[0].legend(loc='upper right')
    
    # Đồ thị dữ liệu surrogate
    axes[1].plot(surrogate_ts[:n_samples], color='#d62728', linewidth=0.8, label='Surrogate')
    axes[1].set_title("PPS Surrogate (Tái tạo)", fontsize=12)
    axes[1].set_xlabel("Chỉ số mẫu", fontsize=10)
    axes[1].set_ylabel("Biên độ", fontsize=10)
    axes[1].grid(True, linestyle='--', alpha=0.5)
    axes[1].legend(loc='upper right')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def plot_phase_space_3D(original_ts, surrogate_ts, delay, optimal_rho):
    """
    Vẽ đối chiếu quỹ đạo 3D bằng biểu đồ phân tán (scatter plot).
    Không gian pha được tái tạo với m=3 (trục x, y, z tương ứng với các độ trễ).
    """
    # Cắt mảng để tạo bộ 3 tọa độ: x(t), x(t - tau), x(t - 2*tau)
    orig_x = original_ts[:-2 * delay]
    orig_y = original_ts[delay:-delay]
    orig_z = original_ts[2 * delay:]
    
    surr_x = surrogate_ts[:-2 * delay]
    surr_y = surrogate_ts[delay:-delay]
    surr_z = surrogate_ts[2 * delay:]
    
    # Thiết lập khung đồ thị
    fig = plt.figure(figsize=(10, 6), dpi=100)
    fig.suptitle("Bảo toàn Đa tạp trong Không gian Pha 3D", fontsize=16, fontweight='bold', y=1.05)
    
    # 1. Đồ thị dữ liệu gốc (3D Scatter)
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.scatter(orig_x, orig_y, orig_z, s=0.5, color='#1f77b4', alpha=0.3)
    ax1.set_title("Dữ liệu gốc", fontsize=14)
    ax1.set_xlabel(r"$x(t)$", fontsize=12, labelpad=10)
    ax1.set_ylabel(r"$x(t - \tau)$", fontsize=12, labelpad=10)
    ax1.set_zlabel(r"$x(t - 2\tau)$", fontsize=12, labelpad=10)
    
    # Làm trong suốt nền của các mặt phẳng lưới 3D để dễ nhìn quỹ đạo
    ax1.xaxis.pane.fill = False
    ax1.yaxis.pane.fill = False
    ax1.zaxis.pane.fill = False
    
    # 2. Đồ thị dữ liệu surrogate (3D Scatter)
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.scatter(surr_x, surr_y, surr_z, s=0.5, color='#d62728', alpha=0.3)
    ax2.set_title(rf"PPS Surrogate ($\rho = {optimal_rho:.4f}$)", fontsize=14)
    ax2.set_xlabel(r"$x(t)$", fontsize=12, labelpad=10)
    ax2.set_ylabel(r"$x(t - \tau)$", fontsize=12, labelpad=10)
    ax2.set_zlabel(r"$x(t - 2\tau)$", fontsize=12, labelpad=10)
    
    ax2.xaxis.pane.fill = False
    ax2.yaxis.pane.fill = False
    ax2.zaxis.pane.fill = False
    
    plt.tight_layout()
    plt.show()