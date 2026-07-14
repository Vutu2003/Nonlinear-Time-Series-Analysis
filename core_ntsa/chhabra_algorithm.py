import numpy as np
from scipy.stats import linregress

def chhabra_jensen_spectrum(probabilities_dict, q_range, scale_slice=None):
    """
    Tính toán trực tiếp phổ kỳ dị đa phân dạng f(alpha) 
    theo thuật toán Chhabra & Jensen (1989).
    Đã tích hợp Log-Sum-Exp chống tràn số và tự chọn vùng tỷ lệ.
    
    Args:
        probabilities_dict (dict): Dictionary {L: mảng P_i}.
        q_range (array-like): Mảng các giá trị q cần quét.
        scale_slice (slice, optional): Vùng tuyến tính cần trích xuất (Scaling region).
        
    Returns:
        tuple: (mảng alpha_q, mảng f_q).
    """
    # 1. Sắp xếp kích thước L để đảm bảo tính nhất quán của trục hoành
    scales = np.sort(list(probabilities_dict.keys()))
    
    # 2. Cắt vùng Scaling Region để loại bỏ nhiễu ở L quá nhỏ hoặc quá lớn
    if scale_slice is not None:
        scales = scales[scale_slice]
        
    log_L = np.log(scales)
    n_q = len(q_range)
    
    alpha_q = np.zeros(n_q)
    f_q = np.zeros(n_q)
    
    for idx, q in enumerate(q_range):
        entropy_scale = np.zeros(len(scales))
        weighted_singularity = np.zeros(len(scales))
        
        for j, L in enumerate(scales):
            P = probabilities_dict[L]
            P = P[P > 0] 
            
            log_P = np.log(P)
            
            # 3. Kỹ thuật Log-Sum-Exp ổn định hóa số học cho q âm lớn
            log_mu_unnorm = q * log_P
            log_mu_unnorm -= np.max(log_mu_unnorm)
            
            mu_unnorm = np.exp(log_mu_unnorm)
            mu = mu_unnorm / np.sum(mu_unnorm)
            
            # 4. Trích xuất Entropy (cho f) và Kỳ vọng (cho alpha)
            entropy_scale[j] = np.sum(mu * np.log(mu))
            weighted_singularity[j] = np.sum(mu * log_P)
            
        # Hồi quy tuyến tính để tìm giới hạn lim (L -> 0)
        slope_f, intercept_f, r_f, p_f, err_f = linregress(log_L, entropy_scale)
        f_q[idx] = slope_f
        
        slope_alpha, intercept_a, r_a, p_a, err_a = linregress(log_L, weighted_singularity)
        alpha_q[idx] = slope_alpha
        
    return alpha_q, f_q
