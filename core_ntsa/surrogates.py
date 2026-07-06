import numpy as np

def generate_aaft_surrogates(signal, M=10, random_seed=None):
    """
    Sinh dữ liệu đối chứng (Surrogate Data) bằng thuật toán AAFT.
    
    Args:
        signal (np.ndarray): Mảng 1D chứa tín hiệu thực nghiệm.
        M (int): Số lượng chuỗi surrogate cần tạo.
        random_seed (int): Hạt giống ngẫu nhiên để đảm bảo tính tái lập.
        
    Returns:
        np.ndarray: Ma trận 2D kích thước (M, N) chứa các chuỗi surrogate.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
        
    signal = np.asarray(signal)
    N = len(signal)
    surrogates = np.zeros((M, N))
    
    # Tiền xử lý cho Bước 4: Lưu giá trị và thứ hạng của chuỗi gốc
    sorted_x = np.sort(signal)
    ranks_x = np.argsort(np.argsort(signal))
    
    for i in range(M):
        # Bước 1: Khởi tạo Gaussian
        r = np.random.normal(0, 1, N)
        sorted_r = np.sort(r)
        
        # Bước 2: Ánh xạ thứ hạng thuận (Forward Rank-ordering)
        y = sorted_r[ranks_x]
        
        # Bước 3: Ngẫu nhiên hóa pha (Phase Randomization)
        # Sử dụng rfft để trích xuất phổ nửa dương
        Y_k = np.fft.rfft(y)
        
        # Tạo góc pha ngẫu nhiên phân phối đều
        random_phases = np.random.uniform(0, 2 * np.pi, len(Y_k))
        
        # Xáo trộn pha nhưng giữ nguyên biên độ
        Y_k_surr = np.abs(Y_k) * np.exp(1j * random_phases)
        
        # Biến đổi ngược về miền thời gian (irfft tự động nội suy đối xứng)
        y_prime = np.fft.irfft(Y_k_surr, n=N)
        
        # Bước 4: Ánh xạ thứ hạng nghịch (Inverse Rank-ordering)
        # Tính thứ hạng của chuỗi Gaussian đã xáo trộn pha
        ranks_y_prime = np.argsort(np.argsort(y_prime))
        
        # Ép phân phối của chuỗi gốc vào đúng thứ hạng mới
        surrogates[i, :] = sorted_x[ranks_y_prime]
        
    return surrogates


def generate_iaaft_surrogates(signal, M=10, max_iter=100, random_seed=None):
    """
    Sinh dữ liệu đối chứng (Surrogate Data) bằng thuật toán IAAFT.
    
    Args:
        signal (np.ndarray): Mảng 1D chứa tín hiệu thực nghiệm.
        M (int): Số lượng chuỗi surrogate cần tạo.
        max_iter (int): Số vòng lặp tối đa để tránh lặp vô hạn.
        random_seed (int): Hạt giống ngẫu nhiên để đảm bảo tính tái lập.
        
    Returns:
        np.ndarray: Ma trận 2D kích thước (M, N) chứa các chuỗi surrogate.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
        
    signal = np.asarray(signal)
    N = len(signal)
    surrogates = np.zeros((M, N))
    
    # BƯỚC 0: Khởi tạo và Lưu trữ nguyên liệu
    sorted_s = np.sort(signal)
    
    # Biến đổi rfft để lấy biên độ tuyệt đối lý tưởng (chỉ lấy nửa phổ dương)
    S_k_ideal = np.abs(np.fft.rfft(signal))
    
    for m_idx in range(M):
        # Khởi tạo chuỗi giả bằng cách xáo trộn ngẫu nhiên chuỗi gốc
        s_curr = np.random.permutation(signal)
        
        # VÒNG LẶP ĐỆ QUY
        for _ in range(max_iter):
            s_prev = s_curr.copy()
            
            # BƯỚC 1: Khớp Phổ năng lượng
            S_k_curr = np.fft.rfft(s_curr)
            phases = np.angle(S_k_curr)
            
            # Thay thế biên độ lý tưởng, giữ nguyên góc pha
            S_k_new = S_k_ideal * np.exp(1j * phases)
            
            # Biến đổi ngược về miền thời gian (irfft tự nội suy phần đối xứng)
            s_tilde = np.fft.irfft(S_k_new, n=N)
            
            # BƯỚC 2: Khớp Phân phối
            # Tính thứ hạng của chuỗi trung gian s_tilde
            ranks_tilde = np.argsort(np.argsort(s_tilde))
            
            # Thay thế bằng giá trị gốc tương ứng với cùng thứ hạng
            s_curr = sorted_s[ranks_tilde]
            
            # BƯỚC 3: Kiểm tra Hội tụ
            # Nếu thứ hạng không đổi (s_curr giống hệt s_prev), dừng vòng lặp
            if np.array_equal(s_curr, s_prev):
                break
                
        # Lưu kết quả cuối cùng của chuỗi thứ m_idx
        surrogates[m_idx, :] = s_curr
        
    return surrogates


def generate_iid_surrogates(data, num_surrogates=1, random_seed=None):
    """
    Sinh dữ liệu Surrogate cho giả thuyết Null IID bằng thuật toán Shuffling.
    
    Args:
        data (array-like): Chuỗi thời gian gốc (1D).
        num_surrogates (int): Số lượng chuỗi Surrogate cần sinh (mặc định là 1).
        random_seed (int, optional): Hạt giống ngẫu nhiên để tái lập kết quả.
        
    Returns:
        numpy.ndarray: Ma trận kích thước (num_surrogates, len(data)) chứa các chuỗi Surrogate.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
        
    # Chuẩn hóa đầu vào thành mảng numpy 1 chiều
    data_array = np.asarray(data).flatten()
    n_samples = len(data_array)
    
    # Khởi tạo ma trận chứa các chuỗi Surrogate
    surrogates = np.zeros((num_surrogates, n_samples))
    
    # Thực hiện xáo trộn độc lập cho từng chuỗi
    for i in range(num_surrogates):
        surrogates[i, :] = np.random.permutation(data_array)
        
    return surrogates