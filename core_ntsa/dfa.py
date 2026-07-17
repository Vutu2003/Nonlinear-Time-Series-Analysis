import numpy as np

def compute_dfa_core(signal, scales, order=1):
    """
    Core computation for Detrended Fluctuation Analysis (DFA).
    
    Parameters:
        signal (np.ndarray): 1D array of the original time series.
        scales (array-like): Array of window sizes (n).
        order (int): Polynomial order for local detrending (default is 1 for DFA-1).
        
    Returns:
        valid_scales (np.ndarray): The scales that were actually processed.
        F_n (np.ndarray): The RMS fluctuation for each scale.
    """
    signal = np.asarray(signal)
    N = len(signal)
    
    # Step 1: Create Profile (Integration)
    # y(k) = sum(x(i) - mean(x))
    y = np.cumsum(signal - np.mean(signal))
    
    F_n = np.zeros(len(scales))
    valid_scales = []
    
    for idx, n in enumerate(scales):
        n = int(n)
        # Ensure window size is meaningful
        if n < order + 2 or n > N:
            continue
            
        # Step 2: Windowing
        # Truncate profile to be an exact multiple of n
        n_windows = N // n
        y_trunc = y[:n_windows * n]
        
        # Reshape into (n_windows, n) for vectorized processing
        y_reshaped = y_trunc.reshape(n_windows, n)
        
        # Create a local time axis for the window
        t = np.arange(n)
        
        # Step 3: Local Detrending
        # Fit polynomial to each window simultaneously using matrix operations
        # np.polyfit handles 2D arrays by fitting each column, so we transpose y_reshaped
        coeffs = np.polyfit(t, y_reshaped.T, order)
        
        # Evaluate the polynomial trends for all windows
        # trend shape will be (n, n_windows), so we transpose it back
        trend = np.polyval(coeffs, t).T
        
        # Extract the intrinsic residual
        residual = y_reshaped - trend
        
        # Step 4: Fluctuation (RMS)
        # Calculate the Root Mean Square of the residual energy
        F_n[idx] = np.sqrt(np.mean(residual ** 2))
        valid_scales.append(n)
        
    return np.array(valid_scales), F_n[:len(valid_scales)]