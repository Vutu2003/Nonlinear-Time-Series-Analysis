import numpy as np
from typing import Union, Dict, Tuple


def _validate_input(x: np.ndarray, m: int) -> Tuple[np.ndarray, int]:
    """
    Stage 1.1: Validate input data and length constraints.
    """
    x_array = np.asarray(x, dtype=np.float64)
    
    if x_array.ndim != 1:
        raise ValueError("Input signal must be a 1D array.")
    
    if np.isnan(x_array).any() or np.isinf(x_array).any():
        raise ValueError("Input signal contains NaN or Inf values.")
        
    n_samples = len(x_array)
    if n_samples <= m + 1:
        raise ValueError(f"Signal length ({n_samples}) must be greater than m + 1 ({m + 1}).")
        
    return x_array, n_samples


def _compute_tolerance(x: np.ndarray, r: Union[float, None]) -> float:
    """
    Stage 1.2: Compute or validate the tolerance radius r.
    Uses ddof=0 to ensure mathematical symmetry with ApEn.
    """
    if r is None:
        return 0.2 * np.std(x, ddof=0)
    
    if r <= 0:
        raise ValueError("Tolerance r must be strictly positive.")
        
    return float(r)


def _embed_phase_space(x: np.ndarray, m: int, n_samples: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Stage 2: State Space Embedding.
    Ensures identical template counts (N - m) in both embedding dimensions.
    """
    n_templates = n_samples - m
    
    # Create templates of dimension m
    templates_m = np.array([x[i : i + m] for i in range(n_templates)])
    
    # Create templates of dimension m + 1 using the EXACT same start indices
    templates_mp1 = np.array([x[i : i + m + 1] for i in range(n_templates)])
    
    return templates_m, templates_mp1


def _compute_distance(templates_m: np.ndarray, templates_mp1: np.ndarray, metric: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Stage 3: Pairwise Distance Engine.
    Computes distance matrix and rigorously removes self-matching (diagonal).
    """
    if metric != 'chebyshev':
        raise NotImplementedError("Currently only 'chebyshev' metric is supported.")
        
    # Broadcasting to compute pairwise differences: shape (N-m, N-m, dim)
    diff_m = np.abs(templates_m[:, None, :] - templates_m[None, :, :])
    dist_m = np.max(diff_m, axis=-1)
    
    diff_mp1 = np.abs(templates_mp1[:, None, :] - templates_mp1[None, :, :])
    dist_mp1 = np.max(diff_mp1, axis=-1)
    
    # Enforce zero self-matching constraint by setting diagonals to Infinity
    np.fill_diagonal(dist_m, np.inf)
    np.fill_diagonal(dist_mp1, np.inf)
    
    return dist_m, dist_mp1


def _count_matches(dist_m: np.ndarray, dist_mp1: np.ndarray, r: float) -> Tuple[int, int]:
    """
    Stage 4: Global Match Counter.
    Independently counts valid matches (distance <= r) across the whole network.
    """
    b_matches = np.sum(dist_m <= r)
    a_matches = np.sum(dist_mp1 <= r)
    
    return int(a_matches), int(b_matches)


def _estimate_entropy(a_matches: int, b_matches: int, verbose: bool) -> Union[float, Dict[str, Union[float, int]]]:
    """
    Stage 5: Entropy Estimator & Formatter.
    Applies non-linear logarithmic transformation and formats the output.
    """
    if b_matches == 0 or a_matches == 0:
        sampen_value = np.nan
    else:
        sampen_value = -np.log(a_matches / b_matches)
        
    if verbose:
        return {
            "sampen": sampen_value,
            "A": a_matches,
            "B": b_matches
        }
        
    return sampen_value


def sampen(x: Union[list, np.ndarray], m: int = 2, r: float = None, metric: str = 'chebyshev', verbose: bool = False) -> Union[float, dict]:
    """
    Stage 0: Configuration & Main Wrapper.
    Computes the Sample Entropy (SampEn) of a time series.
    
    Parameters:
    -----------
    x       : 1D array-like time series.
    m       : Embedding dimension (default: 2).
    r       : Tolerance radius (default: None -> auto-scales to 0.2 * std(x)).
    metric  : Distance metric (default: 'chebyshev').
    verbose : If True, returns a dictionary containing SampEn and global counts A, B.
    
    Returns:
    --------
    SampEn value (float) or Dictionary if verbose=True.
    """
    # Stage 1
    x_array, n_samples = _validate_input(x, m)
    r_val = _compute_tolerance(x_array, r)
    
    # Stage 2
    templates_m, templates_mp1 = _embed_phase_space(x_array, m, n_samples)
    
    # Stage 3
    dist_m, dist_mp1 = _compute_distance(templates_m, templates_mp1, metric)
    
    # Stage 4
    a_matches, b_matches = _count_matches(dist_m, dist_mp1, r_val)
    
    # Stage 5
    return _estimate_entropy(a_matches, b_matches, verbose)