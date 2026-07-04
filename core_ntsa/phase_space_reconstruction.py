"""
Phase Space Construction Tools

This module provides foundational functions for reconstructing the phase space
from one-dimensional time series data based on Takens' Embedding Theorem.
"""

import numpy as np
from scipy.spatial import cKDTree
from scipy.special import digamma

def delay_embedding(time_series: np.ndarray, tau: int, m: int) -> np.ndarray:
    """
    Reconstruct the phase space from a 1D time series using delay coordinate embedding.

    According to Takens' theorem, a multi-dimensional state space can be 
    reconstructed from a single scalar observation by creating vectors of 
    time-delayed samples.

    Args:
        time_series: A 1D numpy array representing the scalar time series.
        tau: The time delay (integer, number of sample steps).
        m: The embedding dimension (integer).

    Returns:
        A 2D numpy array of shape (N - (m - 1) * tau, m) representing the 
        reconstructed phase space trajectory, where each row is a point in 
        the m-dimensional space.
    
    Raises:
        ValueError: If the time series is too short for the chosen tau and m.
    """
    n_samples = len(time_series)
    
    # Calculate the number of reconstructable vectors
    n_vectors = n_samples - (m - 1) * tau
    
    if n_vectors <= 0:
        raise ValueError(
            f"Time series of length {n_samples} is too short for "
            f"embedding dimension m={m} and delay tau={tau}."
        )
        
    # Initialize the phase space matrix
    phase_space = np.zeros((n_vectors, m))
    
    # Construct the embedding matrix using fast array slicing
    for i in range(m):
        phase_space[:, i] = time_series[i * tau : i * tau + n_vectors]
        
    return phase_space

def ksg_mi_1(x: np.ndarray, y: np.ndarray, k: int = 3) -> float:
    """
    Estimate Mutual Information (MI) using KSG Algorithm 1 (Hyper-cube).
    
    Best suited for variables with similar marginal distributions (e.g., auto-MI 
    for finding time delay tau). Uses a fixed-size hyper-cube max norm.

    Args:
        x: 1D numpy array of the first variable.
        y: 1D numpy array of the second variable.
        k: Number of nearest neighbors. Default is 3.

    Returns:
        Estimated Mutual Information in nats (floored at 0.0).
    """
    # 1. Standardize variables to ensure isotropic distance scaling
    x = (x - np.mean(x)) / np.std(x)
    y = (y - np.mean(y)) / np.std(y)

    # 2. Add tiny noise to break exact data degeneracy (e.g., ADC quantization)
    x += np.random.normal(0, 1e-10, size=x.shape)
    y += np.random.normal(0, 1e-10, size=y.shape)

    n_samples = len(x)
    z = np.column_stack((x, y))

    # 3. Find k-th neighbor distance in joint space using max norm (p=inf)
    tree_z = cKDTree(z)
    eps_half, _ = tree_z.query(z, k=k + 1, p=np.inf)
    eps_half = eps_half[:, -1]  # Extract distance to the k-th neighbor

    # 4. Strict inequality for marginal projection
    eps_strict = np.maximum(eps_half - 1e-15, 0)

    # 5. Count marginal neighbors
    tree_x = cKDTree(x.reshape(-1, 1))
    tree_y = cKDTree(y.reshape(-1, 1))
    
    nx_plus_1 = tree_x.query_ball_point(x.reshape(-1, 1), eps_strict, p=np.inf, return_length=True)
    ny_plus_1 = tree_y.query_ball_point(y.reshape(-1, 1), eps_strict, p=np.inf, return_length=True)

    # 6. Compute KSG 1 Equation
    mi = digamma(k) - np.mean(digamma(nx_plus_1) + digamma(ny_plus_1)) + digamma(n_samples)
    
    return max(0.0, float(mi))


def ksg_mi_2(x: np.ndarray, y: np.ndarray, k: int = 3) -> float:
    """
    Estimate Mutual Information (MI) using KSG Algorithm 2 (Hyper-rectangle).
    
    Best suited for heterogeneous variables with vastly different density 
    distributions (e.g., Transfer Entropy, continuous vs categorical data).

    Args:
        x: 1D numpy array of the first variable.
        y: 1D numpy array of the second variable.
        k: Number of nearest neighbors. Default is 3.

    Returns:
        Estimated Mutual Information in nats (floored at 0.0).
    """
    # 1. Standardize variables
    x = (x - np.mean(x)) / np.std(x)
    y = (y - np.mean(y)) / np.std(y)

    # 2. Add tiny noise to break exact degeneracy
    x += np.random.normal(0, 1e-10, size=x.shape)
    y += np.random.normal(0, 1e-10, size=y.shape)

    n_samples = len(x)
    z = np.column_stack((x, y))

    # 3. Find INDICES of the k-th neighbor in joint space
    tree_z = cKDTree(z)
    _, indices = tree_z.query(z, k=k + 1, p=np.inf)
    kth_idx = indices[:, -1]

    # 4. Calculate exact bounding box dimensions for each point
    eps_x = np.abs(x - x[kth_idx])
    eps_y = np.abs(y - y[kth_idx])

    eps_x_strict = np.maximum(eps_x - 1e-15, 0)
    eps_y_strict = np.maximum(eps_y - 1e-15, 0)

    # 5. Count marginal neighbors within dynamic rectangular bounds
    tree_x = cKDTree(x.reshape(-1, 1))
    tree_y = cKDTree(y.reshape(-1, 1))
    
    nx = tree_x.query_ball_point(x.reshape(-1, 1), eps_x_strict, p=np.inf, return_length=True)
    ny = tree_y.query_ball_point(y.reshape(-1, 1), eps_y_strict, p=np.inf, return_length=True)

    # 6. Compute KSG 2 Equation (includes -1/k penalty)
    mi = digamma(k) - (1.0 / k) - np.mean(digamma(nx) + digamma(ny)) + digamma(n_samples)
    
    return max(0.0, float(mi))



def false_nearest_neighbors(
    time_series: np.ndarray, 
    tau: int, 
    max_m: int = 10, 
    R_tol: float = 15.0, 
    A_tol: float = 2.0
) -> tuple:
    """
    Xác định số chiều nhúng tối thiểu (m) bằng thuật toán False Nearest Neighbors (Kennel, 1992).

    Args:
        time_series: Mảng 1D chứa tín hiệu chuỗi thời gian.
        tau: Độ trễ thời gian đã được xác định trước (ví dụ từ KSG).
        max_m: Số chiều không gian tối đa muốn kiểm tra.
        R_tol: Ngưỡng kéo giãn tương đối (Tiêu chí 1). Mặc định là 15.0.
        A_tol: Ngưỡng kích thước tuyệt đối để chống nhiễu (Tiêu chí 2). Mặc định là 2.0.

    Returns:
        dims: Mảng các số nguyên từ 1 đến max_m.
        fnn_percentages: Tỷ lệ láng giềng giả (%) tương ứng tại mỗi chiều.
    """
    # 1. Tính kích thước tổng thể của hệ thống (Bán kính R_A)
    R_A = np.std(time_series)
    
    fnn_percentages = []
    
    # 2. Vòng lặp tăng dần cấu trúc không gian từ d = 1 đến max_m
    for d in range(1, max_m + 1):
        # Bung mở không gian ở chiều d+1
        Y_d1 = delay_embedding(time_series, tau, d + 1)
        if Y_d1 is None:
            break
            
        N_valid = len(Y_d1)
        
        # Không gian d chiều chính là phần đầu của Y_d1
        Y_d = Y_d1[:, :-1]
        
        # Tọa độ mới được thêm vào khi nâng lên d+1 (Trục mới mọc ra)
        new_coord = Y_d1[:, -1]
        
        # 3. Tìm láng giềng gần nhất (k=2 vì láng giềng thứ 1 chính là bản thân nó với k/c = 0)
        tree = cKDTree(Y_d)
        distances, indices = tree.query(Y_d, k=2, p=2) # p=2 là chuẩn Euclid (Pytago)
        
        R_d = distances[:, 1]  # Khoảng cách tới láng giềng gần nhất
        nn_idx = indices[:, 1] # Index của láng giềng gần nhất
        
        # Ngăn chặn lỗi chia cho 0 nếu có 2 điểm trùng nhau hoàn toàn
        R_d_safe = np.maximum(R_d, 1e-15)
        
        # 4. Tính toán sự kéo giãn trên chiều không gian mới
        dist_new = np.abs(new_coord - new_coord[nn_idx])
        
        # Khoảng cách R_{d+1} mới theo Pytago
        R_d1 = np.sqrt(R_d**2 + dist_new**2)
        
        # 5. Phán quyết theo 2 Tiêu chí
        # Tiêu chí 1: Sự kéo giãn tương đối
        crit_1 = (dist_new / R_d_safe) > R_tol
        
        # Tiêu chí 2: Kích thước tuyệt đối (Chống nhiễu)
        crit_2 = (R_d1 / R_A) > A_tol
        
        # Láng giềng bị gắn mác "Giả" nếu vi phạm 1 trong 2 tiêu chí
        fnn_count = np.sum(crit_1 | crit_2)
        fnn_percent = (fnn_count / N_valid) * 100.0
        
        fnn_percentages.append(fnn_percent)
        
    return np.arange(1, len(fnn_percentages) + 1), np.array(fnn_percentages)


def cao_method(time_series: np.ndarray, tau: int, max_m: int = 10) -> tuple:
    """
    Xác định chiều nhúng tối thiểu bằng Phương pháp Cao (1997).
    
    Args:
        time_series: Mảng 1D tín hiệu đầu vào.
        tau: Độ trễ thời gian (được tính từ Mutual Information).
        max_m: Số chiều nhúng tối đa cần kiểm tra.
        
    Returns:
        dims: Mảng các chiều nhúng từ 1 đến max_m.
        E1: Mảng giá trị E1 (Đại lượng bão hòa không gian).
        E2: Mảng giá trị E2 (Đại lượng phân biệt nhiễu).
    """
    N = len(time_series)
    
    # Cần tính E và E_star tới max_m + 1 để lập tỷ số cho E1(max_m) và E2(max_m)
    E = np.zeros(max_m + 1)
    E_star = np.zeros(max_m + 1)
    
    for d in range(1, max_m + 2):
        N_valid = N - d * tau
        if N_valid <= 0:
            raise ValueError(f"Dữ liệu quá ngắn để tính tới chiều d={d} với tau={tau}")
            
        # 1. Tái tạo không gian d chiều cho các điểm hợp lệ (có thể mở rộng lên d+1)
        Y_d = np.zeros((N_valid, d))
        for i in range(d):
            Y_d[:, i] = time_series[i * tau : i * tau + N_valid]
            
        # 2. Tìm láng giềng gần nhất bằng Chuẩn Maximum (p=np.inf)
        tree = cKDTree(Y_d)
        distances, indices = tree.query(Y_d, k=2, p=np.inf)
        
        R_d = distances[:, 1]
        nn_idx = indices[:, 1]
        
        # Xử lý an toàn tránh lỗi chia cho 0 khi 2 điểm trùng nhau hoàn toàn
        R_d_safe = np.maximum(R_d, 1e-15)
        
        # 3. Tính toán trên trục tọa độ mới (chiều d+1)
        coord_new = time_series[d * tau : d * tau + N_valid]
        coord_new_nn = time_series[nn_idx + d * tau]
        
        # Độ chênh lệch tuyệt đối trên trục tương lai
        diff = np.abs(coord_new - coord_new_nn)
        
        # Tính E*(d) - Trung bình khoảng cách trên trục mới
        E_star[d - 1] = np.mean(diff)
        
        # Khoảng cách R_{d+1} theo chuẩn Maximum
        R_d1 = np.maximum(R_d, diff)
        
        # Tính tỷ lệ kéo giãn a(i, d)
        a_i_d = R_d1 / R_d_safe
        
        # Tính E(d) - Sức căng trung bình toàn hệ thống
        E[d - 1] = np.mean(a_i_d)
        
    # 4. Tính toán các đại lượng bão hòa E1 và E2
    E1 = E[1:] / E[:-1]
    
    E_star_safe = np.maximum(E_star[:-1], 1e-15)
    E2 = E_star[1:] / E_star_safe
    
    dims = np.arange(1, max_m + 1)
    
    return dims, E1, E2