import warnings
import numpy as np
from typing import Callable, Union, Dict, Any

# Sử dụng relative import cho cấu trúc package
from .sampen import sampen


# =============================================================================
# 1. INTERNAL UTILITIES
# =============================================================================

def _validate_length(signal_length: int, max_scale: int, min_length: int = 100) -> None:
    """
    Validates if the coarse-grained signal at max_scale meets the minimum length.
    """
    if signal_length // max_scale < min_length:
        warnings.warn(
            f"Coarse-grained series length at max_scale ({max_scale}) is "
            f"{signal_length // max_scale} (< {min_length}). "
            "Statistical confidence may be compromised.",
            stacklevel=2
        )


def _coarse_grain(signal: np.ndarray, tau: int, method: str = "mean") -> np.ndarray:
    """
    Performs coarse-graining on the signal for a given scale factor tau.
    """
    if tau == 1:
        # Return a copy to prevent accidental modification of the original signal
        return signal.copy()
    
    usable_length = (len(signal) // tau) * tau
    if usable_length == 0:
        raise ValueError(f"Scale {tau} is too large for the given signal length.")
        
    reshaped_signal = signal[:usable_length].reshape(-1, tau)
    
    if method == "mean":
        return reshaped_signal.mean(axis=1)
    elif method == "median":
        return np.median(reshaped_signal, axis=1)
    else:
        raise ValueError(f"Unsupported coarse-graining method: {method}")


# =============================================================================
# 2. THE MULTISCALE FRAMEWORK (GENERAL ENGINE)
# =============================================================================

def multiscale(signal: Union[list, np.ndarray], entropy_func: Callable, 
               max_scale: int = 20, min_length: int = 100, 
               coarse_method: str = "mean", **entropy_kwargs: Any) -> Dict[str, np.ndarray]:
    """
    A generalized multiscale framework agnostic to the underlying entropy engine.
    
    Parameters:
    -----------
    signal         : 1D array-like time series.
    entropy_func   : Callable entropy function returning a float.
    max_scale      : Maximum scale factor to analyze (default: 20).
    min_length     : Minimum allowed length for the coarse-grained signal (default: 100).
    coarse_method  : Method for coarse-graining, e.g., 'mean', 'median' (default: 'mean').
    entropy_kwargs : Additional keyword arguments passed to entropy_func.
    
    Returns:
    --------
    Dictionary containing 'scale' and 'entropy' arrays.
    """
    # Ép kiểu chuẩn xác để đồng bộ toàn bộ package
    signal = np.asarray(signal, dtype=np.float64)
    _validate_length(len(signal), max_scale, min_length)
    
    scales = np.arange(1, max_scale + 1)
    # Dùng np.nan để theo dõi các scale bị lỗi (fail-safe)
    entropy_values = np.full(max_scale, np.nan)
    
    for i, tau in enumerate(scales):
        coarse_signal = _coarse_grain(signal, tau, method=coarse_method)
        
        # Bắt lỗi từng scale để không làm hỏng toàn bộ profile
        try:
            # Framework assume entropy_func luôn trả về một scalar (float)
            entropy_values[i] = entropy_func(coarse_signal, **entropy_kwargs)
        except Exception:
            entropy_values[i] = np.nan
            
    return {
        "scale": scales,
        "entropy": entropy_values
    }


# =============================================================================
# 3. THE CLASSIC WRAPPER (COSTA ET AL. 2002)
# =============================================================================

def mse(signal: Union[list, np.ndarray], max_scale: int = 20, 
        m: int = 2, r_coeff: float = 0.15, metric: str = 'chebyshev', 
        min_length: int = 100) -> Dict[str, np.ndarray]:
    """
    Computes the classic Multiscale Entropy (MSE) based on Costa et al. (2002).
    
    Parameters:
    -----------
    signal     : 1D array-like time series.
    max_scale  : Maximum scale factor (default: 20).
    m          : Embedding dimension (default: 2).
    r_coeff    : Tolerance coefficient (default: 0.15).
    metric     : Distance metric passed to SampEn (default: 'chebyshev').
    min_length : Minimum allowed length for the signal at max_scale (default: 100).
    
    Returns:
    --------
    Dictionary containing 'scale' and 'entropy' arrays.
    """
    signal = np.asarray(signal, dtype=np.float64)
    
    # Khóa Standard Deviation từ chuỗi gốc
    std_orig = np.std(signal, ddof=0)
    fixed_r = r_coeff * std_orig
    
    return multiscale(
        signal=signal,
        entropy_func=sampen,
        max_scale=max_scale,
        min_length=min_length,
        coarse_method="mean",
        m=m,
        r=fixed_r,
        metric=metric
    )