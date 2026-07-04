import numpy as np

def one_sided_rank_test(t_orig, t_surr_array, test_direction='less'):
    """
    Kiem dinh hang phi tham so (One-sided rank test) cho du lieu surrogate.
    
    Args:
        t_orig (float): Gia tri thong ke (statistic) cua tin hieu goc.
        t_surr_array (np.ndarray): Mang 1D chua gia tri thong ke cua cac surrogates.
        test_direction (str): 'less' (vi du: RMSE, LLE) hoac 'greater' (vi du: CC).
        
    Returns:
        p_value (float): Gia tri p-value thuc nghiem.
        C (int): So luong surrogate danh bai hoac hoa duoc tin hieu goc.
    """
    t_surr_array = np.asarray(t_surr_array)
    M = len(t_surr_array)

    if test_direction == 'less':
        # Tin hieu goc phai nho hon surrogate (vi du: Sai so du bao thap hon)
        C = np.sum(t_surr_array <= t_orig)
    elif test_direction == 'greater':
        # Tin hieu goc phai lon hon surrogate (vi du: He so tuong quan cao hon)
        C = np.sum(t_surr_array >= t_orig)
    else:
        raise ValueError("test_direction chi nhan gia tri 'less' hoac 'greater'")

    p_value = (1.0 + C) / (M + 1.0)
    
    return p_value, C


def run_surrogate_pipeline(signal, surrogate_generator, evaluator, 
                           M=39, test_direction='less', 
                           surrogate_kwargs=None, evaluator_kwargs=None):
    """
    Ham dieu phoi tong chay toan bo quy trinh kiem dinh NTSA.
    
    Args:
        signal (np.ndarray): Tin hieu goc 1D.
        surrogate_generator (callable): Ham sinh surrogate (vd: generate_iaaft_surrogates).
        evaluator (callable): Ham tinh toan dai luong (vd: predict_zeroth_order_wrapper).
        M (int): So luong surrogate data can tao.
        test_direction (str): Chieu kiem dinh ('less' hoac 'greater').
        surrogate_kwargs (dict): Tham so bo sung cho ham surrogate_generator.
        evaluator_kwargs (dict): Tham so bo sung cho ham evaluator.
        
    Returns:
        dict: Tu dien chua ket qua thong ke va p-value.
    """
    if surrogate_kwargs is None:
        surrogate_kwargs = {}
    if evaluator_kwargs is None:
        evaluator_kwargs = {}

    # 1. Tinh toan dai luong thong ke cho tin hieu goc
    t_orig = evaluator(signal, **evaluator_kwargs)
    
    # 2. Sinh tap du lieu surrogate
    surrogates = surrogate_generator(signal, M=M, **surrogate_kwargs)
    
    # 3. Tinh toan dai luong thong ke cho tung chuoi surrogate
    t_surr_array = np.zeros(M)
    for i in range(M):
        t_surr_array[i] = evaluator(surrogates[i], **evaluator_kwargs)
        
    # 4. Kiem dinh thong ke phan hang
    p_value, count_beat = one_sided_rank_test(t_orig, t_surr_array, test_direction)
    
    # Dong goi ket qua
    results = {
        't_orig': float(t_orig),
        't_surr_mean': float(np.mean(t_surr_array)),
        't_surr_std': float(np.std(t_surr_array)),
        'p_value': float(p_value),
        'surrogates_beat_orig': int(count_beat),
        'M': M,
        'test_direction': test_direction
    }
    
    return results