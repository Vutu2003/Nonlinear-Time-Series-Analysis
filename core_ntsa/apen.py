import numpy as np
from typing import Tuple

def calculate_tolerance(u: np.ndarray, k: float = 0.2) -> Tuple[float, float]:
    """
    Stage 1: Initialization & Preprocessing
    Compute the tolerance radius r = k * SD(U) following Pincus (1991).
    
    References
    ----------
    Pincus (1991), Eq. (1) - Parameter initialization.
    
    Args:
        u (np.ndarray): 1D input time series.
        k (float): Tolerance multiplier.
        
    Returns:
        Tuple[float, float]: (sd, r) where sd is the intermediate standard deviation 
                             and r is the normalized tolerance radius.
    """
    # Use ddof=0 for population standard deviation as per standard ApEn definition
    sd = np.std(u, ddof=0)
    r = k * sd
    
    return float(sd), float(r)

def embed_phase_space(u: np.ndarray, m: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Stage 2: Phase Space Reconstruction
    Reconstruct the phase space matrices for dimensions m and m+1 using sliding windows.
    
    References
    ----------
    Pincus (1991), Eq. (2) - Vector sequence construction.
    
    Args:
        u (np.ndarray): 1D input time series.
        m (int): Target embedding dimension.
        
    Returns:
        Tuple[np.ndarray, np.ndarray]: (X_m, X_m_plus_1) matrices.
        
    Raises:
        ValueError: If m is invalid or the time series is too short for embedding.
    """
    # Input validation for robust debugging
    if m < 1:
        raise ValueError("Embedding dimension 'm' must be at least 1.")
    if len(u) <= m:
        raise ValueError("Time series length 'N' must be strictly greater than 'm'.")
        
    # Shape: (N - m + 1, m)
    X_m = np.lib.stride_tricks.sliding_window_view(u, window_shape=m)
    
    # Shape: (N - m, m + 1)
    X_m_plus_1 = np.lib.stride_tricks.sliding_window_view(u, window_shape=m + 1)
    
    return X_m, X_m_plus_1

def compute_distance_matrices(
    X_m: np.ndarray, 
    X_m_plus_1: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Stage 3: Distance Matrix Computation
    Compute the Chebyshev distance between all pairs of vectors in the phase space 
    using NumPy broadcasting for O(1) loop-level time complexity.
    
    References
    ----------
    Pincus (1991), Eq. (3) - Distance definition d[x(i), x(j)].
    
    Args:
        X_m (np.ndarray): Phase space matrix for dimension m. 
                          Shape: (N - m + 1, m).
        X_m_plus_1 (np.ndarray): Phase space matrix for dimension m+1. 
                                 Shape: (N - m, m + 1).
        
    Returns:
        Tuple[np.ndarray, np.ndarray]: (D_m, D_m_plus_1) square pairwise distance matrices.
                                       Shapes: (N - m + 1, N - m + 1) and (N - m, N - m).
    """
    # Broadcasting for dimension m
    # X_m[:, np.newaxis, :] shape: (N-m+1, 1, m)
    # X_m[np.newaxis, :, :] shape: (1, N-m+1, m)
    # np.max(..., axis=-1) reduces the m-dimension, returning the max absolute difference
    D_m = np.max(
        np.abs(X_m[:, np.newaxis, :] - X_m[np.newaxis, :, :]), 
        axis=-1
    )
    
    # Broadcasting for dimension m+1
    # Applying the exact same vectorization logic for the higher dimension
    D_m_plus_1 = np.max(
        np.abs(X_m_plus_1[:, np.newaxis, :] - X_m_plus_1[np.newaxis, :, :]), 
        axis=-1
    )
    
    return D_m, D_m_plus_1

def compute_pattern_probabilities(
    D_m: np.ndarray, 
    D_m_plus_1: np.ndarray, 
    r: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Stage 4: Pattern Matching & Probability (The Boolean Mask)
    Filter similar patterns using the tolerance radius r and calculate 
    the repetition probability for each vector.
    
    References
    ----------
    Pincus (1991), Eq. (4) & (5) - C_i^m(r) definition.
    
    Args:
        D_m (np.ndarray): Square distance matrix for dimension m.
        D_m_plus_1 (np.ndarray): Square distance matrix for dimension m+1.
        r (float): Normalized tolerance radius.
        
    Returns:
        Tuple[np.ndarray, np.ndarray]: (C_m, C_m_plus_1) 1D probability arrays.
    """
    # Extract the number of vectors (denominator for probability normalization)
    N_m = D_m.shape[0]
    N_m_plus_1 = D_m_plus_1.shape[0]
    
    # 1. Thresholding: Create Boolean Mask (D <= r)
    # 2. Neighbor Counting: Sum True values along the rows (axis=1)
    # 3. Probability Normalization: Divide by total vectors
    C_m = np.sum(D_m <= r, axis=1) / N_m
    
    C_m_plus_1 = np.sum(D_m_plus_1 <= r, axis=1) / N_m_plus_1
    
    return C_m, C_m_plus_1


def compute_approximate_entropy(
    C_m: np.ndarray, 
    C_m_plus_1: np.ndarray
) -> float:
    """
    Stage 5: Logarithmic Aggregation & Complexity Extraction
    Compute the final Approximate Entropy (ApEn) value.
    
    References
    ----------
    Pincus (1991), Eq. (6) & (7) - Phi_m and ApEn definition.
    
    Args:
        C_m (np.ndarray): Probability array for dimension m.
        C_m_plus_1 (np.ndarray): Probability array for dimension m+1.
        
    Returns:
        float: The computed ApEn value.
    """
    # np.mean implicitly calculates (1 / N) * sum(...)
    phi_m = np.mean(np.log(C_m))
    phi_m_plus_1 = np.mean(np.log(C_m_plus_1))
    
    # ApEn is the difference between the logarithmic averages
    apen_value = phi_m - phi_m_plus_1
    
    return float(apen_value)


def approx_entropy(u: np.ndarray, m: int = 2, k: float = 0.2) -> float:
    """
    Compute the Approximate Entropy (ApEn) of a time series.
    
    This function acts as a unified wrapper that orchestrates the 5-stage 
    pipeline based on the exact definitions by Pincus (1991).
    
    References
    ----------
    Pincus, S. M. (1991). Approximate entropy as a measure of system complexity.
    
    Args:
        u (np.ndarray, list): 1D input time series signal.
        m (int, optional): Embedding dimension. Defaults to 2.
        k (float, optional): Tolerance multiplier (r = k * SD). Defaults to 0.2.
        
    Returns:
        float: The computed Approximate Entropy value.
        
    Raises:
        ValueError: If the input signal is not a 1D array.
    """
    # -----------------------------------------------------------------
    # Input Validation & Normalization (Fail-Fast)
    # -----------------------------------------------------------------
    u = np.asarray(u, dtype=float)
    if u.ndim != 1:
        raise ValueError(f"Input signal must be 1-dimensional. Got {u.ndim}D array instead.")
    
    # -----------------------------------------------------------------
    # Stage 1: Initialization & Preprocessing
    # -----------------------------------------------------------------
    sd, r = calculate_tolerance(u, k)  # Retained 'sd' for easier debugging/logging
    
    # -----------------------------------------------------------------
    # Stage 2: Phase Space Reconstruction
    # -----------------------------------------------------------------
    X_m, X_m_plus_1 = embed_phase_space(u, m)
    
    # -----------------------------------------------------------------
    # Stage 3: Distance Matrix Computation
    # -----------------------------------------------------------------
    D_m, D_m_plus_1 = compute_distance_matrices(X_m, X_m_plus_1)
    
    # -----------------------------------------------------------------
    # Stage 4: Pattern Matching & Probability
    # -----------------------------------------------------------------
    C_m, C_m_plus_1 = compute_pattern_probabilities(D_m, D_m_plus_1, r)
    
    # -----------------------------------------------------------------
    # Stage 5: Logarithmic Aggregation
    # -----------------------------------------------------------------
    apen_val = compute_approximate_entropy(C_m, C_m_plus_1)
    
    return apen_val