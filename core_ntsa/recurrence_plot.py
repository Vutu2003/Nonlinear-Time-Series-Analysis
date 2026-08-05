"""
Implementation of:
Zbilut, J.P. & Webber, C.L.
Embeddings and Delays as Derived from Quantification of Recurrence Plots
(1992)

This implementation faithfully reproduces the methodology described in the
original paper, focusing on functional purity, mathematical mapping, and 
strict separation of core algorithms from visualization.
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform
import warnings
from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# ==========================================
# 1. PHASE SPACE MODULE
# ==========================================

def reconstruct_phase_space(u: np.ndarray, d: int, tau: int) -> np.ndarray:
    if d < 1:
        raise ValueError("Embedding dimension 'd' must be at least 1.")
    if tau < 1:
        raise ValueError("Time delay 'tau' must be at least 1.")
        
    n_samples = len(u)
    n_vectors = n_samples - (d - 1) * tau
    
    if n_vectors <= 0:
        raise ValueError("Time series is too short for the given 'd' and 'tau'.")
    
    X = np.array([u[i : i + d * tau : tau] for i in range(n_vectors)])
    
    return X


# ==========================================
# 2. MATRIX MODULE
# ==========================================

def compute_distance_matrix(X: np.ndarray) -> np.ndarray:
    """
    Computes the pairwise Euclidean distance matrix for the state vectors.
    
    Parameters
    ----------
    X : np.ndarray
        2D array of state vectors.
        
    Returns
    -------
    np.ndarray
        2D symmetric array representing the distance matrix.
    """
    distances = pdist(X, metric="euclidean")
    return squareform(distances)


def estimate_baseline_radius(D_baseline: np.ndarray, radius_ratio: float = 0.1) -> float:
    """
    Estimates the fixed radius threshold based on the baseline embedding.
    
    Note: This implements the empirical radius selection strategy described 
    by Zbilut & Webber (1992, "typically no more than 10%..."), rather than 
    a mathematically derived optimum. It calculates the mean of the upper 
    triangle distances to avoid artificially deflating the mean with diagonal zeros.
    
    Parameters
    ----------
    D_baseline : np.ndarray
        2D distance matrix of the baseline embedding (e.g., d=1).
    radius_ratio : float
        The percentage of the mean distance to use. Default is 0.1 (10%).
        
    Returns
    -------
    float
        Estimated empirical radius threshold.
    """
    n_samples = D_baseline.shape[0]
    
    upper_tri_indices = np.triu_indices(n_samples, k=1)
    mean_distance = np.mean(D_baseline[upper_tri_indices])
    
    return float(radius_ratio * mean_distance)


def compute_recurrence_matrix(D: np.ndarray, r: float) -> np.ndarray:
    """
    Binarizes the distance matrix based on the fixed radius threshold
    using the Heaviside step function.
    
    Parameters
    ----------
    D : np.ndarray
        2D distance matrix.
    r : float
        Radius threshold.
        
    Returns
    -------
    np.ndarray
        2D binary recurrence matrix (1 for recurrence, 0 otherwise).
        dtype is np.uint8 to heavily optimize memory usage.
    """
    return (D <= r).astype(np.uint8)

# ==========================================
# 3. QUANTIFICATION MODULE (Zbilut & Webber, 1992)
# ==========================================

def remove_loi(R: np.ndarray) -> np.ndarray:
    """
    Removes the Line of Identity (LOI) from the recurrence matrix.
    
    Parameters
    ----------
    R : np.ndarray
        2D binary recurrence matrix.
        
    Returns
    -------
    np.ndarray
        A copy of the recurrence matrix with the main diagonal set to 0.
        
    Raises
    ------
    ValueError
        If the input matrix is not 2-dimensional.
    """
    if R.ndim != 2:
        raise ValueError("Recurrence matrix must be 2-dimensional.")
        
    R_no_loi = R.copy()
    np.fill_diagonal(R_no_loi, 0)
    return R_no_loi


def calculate_percent_recurrence(R: np.ndarray) -> float:
    """
    Calculates Percent Recurrence (%REC).
    Faithful to Zbilut & Webber (1992), this is computed strictly on the 
    upper triangle of the recurrence matrix to avoid redundancy.
    
    Time Complexity: O(N^2)
    Memory Complexity: O(N^2)
    
    Parameters
    ----------
    R : np.ndarray
        2D binary recurrence matrix.
        
    Returns
    -------
    float
        The %REC value (0.0 to 100.0).
    """
    n_samples = R.shape[0]
    
    # Strictly possible points in the upper triangle
    possible_points_upper = (n_samples * (n_samples - 1)) / 2.0
    
    if possible_points_upper == 0:
        return 0.0
        
    # Extract only the upper triangle (k=1 excludes LOI natively)
    upper_tri = np.triu(R, k=1)
    recurrence_points_upper = np.sum(upper_tri)
    
    return float((recurrence_points_upper / possible_points_upper) * 100.0)


def _extract_diagonal_line_lengths(R: np.ndarray, min_length: int = 2) -> np.ndarray:
    """
    Extracts the lengths of all diagonal lines formed by recurrence points.
    Scans only the upper triangle (k > 0) due to matrix symmetry.
    Uses vectorized Run-Length Encoding logic for O(N^2) performance.
    
    Time Complexity: ~O(N^2)
    Memory Complexity: O(N) for storing lengths
    
    Parameters
    ----------
    R : np.ndarray
        2D binary recurrence matrix.
    min_length : int
        Minimum number of points required to define a valid line.
        
    Returns
    -------
    np.ndarray
        1D array containing the lengths of valid diagonal lines from the upper triangle.
    """
    n_samples = R.shape[0]
    lengths = []
    
    for k in range(1, n_samples):
        diag = np.diagonal(R, offset=k)
        
        if not np.any(diag):
            continue
            
        padded_diag = np.pad(diag, pad_width=1, mode='constant', constant_values=0)
        diffs = np.diff(padded_diag)
        starts = np.where(diffs == 1)[0]
        ends = np.where(diffs == -1)[0]
        
        line_lengths = ends - starts
        valid_lengths = line_lengths[line_lengths >= min_length]
        
        if valid_lengths.size > 0:
            lengths.extend(valid_lengths)
            
    return np.array(lengths, dtype=np.int32)


def calculate_percent_line(R: np.ndarray, min_length: int = 2) -> float:
    """
    Calculates Percent Line Segments (%LINE).
    
    This implementation follows Zbilut & Webber (1992), computing the ratio 
    of points in line segments to total recurrence points strictly within 
    the upper triangle.
    
    Note
    ----
    This is NOT the DET (Determinism) measure introduced in later literature.
    It is the faithful 1992 %LINE formulation.
    
    Time Complexity: O(N^2)
    Memory Complexity: O(N)
    
    Parameters
    ----------
    R : np.ndarray
        2D binary recurrence matrix.
    min_length : int
        Minimum length of a diagonal line. Default is 2.
        
    Returns
    -------
    float
        The %LINE value (0.0 to 100.0).
    """
    upper_tri = np.triu(R, k=1)
    total_recurrence_points_upper = np.sum(upper_tri)
    
    if total_recurrence_points_upper == 0:
        return 0.0
        
    lengths_upper = _extract_diagonal_line_lengths(R, min_length)
    points_in_lines_upper = np.sum(lengths_upper)
    
    return float((points_in_lines_upper / total_recurrence_points_upper) * 100.0)


# ==========================================
# 4. QUANTIFICATION PIPELINE
# ==========================================

@dataclass
class QuantificationResult:
    """Data container for the results of a single configuration run."""
    d: int
    tau: int
    r: float
    X: np.ndarray
    D: np.ndarray
    R: np.ndarray
    REC: float
    LINE: float


def quantify_single_configuration(u: np.ndarray, d: int, tau: int, r: float) -> QuantificationResult:
    """
    Executes the quantification pipeline for a single set of embedding parameters.
    Returns intermediate matrices (X, D, R) to assist in debugging and 
    response surface mapping as described in the 1992 paper.
    
    Parameters
    ----------
    u : np.ndarray
        1D time series array.
    d : int
        Embedding dimension.
    tau : int
        Time delay.
    r : float
        Radius threshold.
        
    Returns
    -------
    QuantificationResult
        Dataclass containing all parameters, matrices, and metrics.
    """
    X = reconstruct_phase_space(u, d, tau)
    D = compute_distance_matrix(X)
    R = compute_recurrence_matrix(D, r)
    
    rec = calculate_percent_recurrence(R)
    line = calculate_percent_line(R)
    
    return QuantificationResult(
        d=d, tau=tau, r=r, X=X, D=D, R=R, REC=rec, LINE=line
    )


def parameter_sweep(u: np.ndarray, d_list: list, tau_list: list, r: float) -> dict:
    """
    Performs a grid sweep over multiple embedding dimensions and time delays
    to observe the topological unfolding of the attractor.
    
    Parameters
    ----------
    u : np.ndarray
        1D time series array.
    d_list : list of int
        List of embedding dimensions to sweep.
    tau_list : list of int
        List of time delays to sweep.
    r : float
        Fixed radius threshold applied across all configurations.
        
    Returns
    -------
    dict
        Dictionary containing the parameter grids and the resulting metric matrices.
    """
    n_d = len(d_list)
    n_tau = len(tau_list)
    
    rec_matrix = np.zeros((n_d, n_tau), dtype=float)
    line_matrix = np.zeros((n_d, n_tau), dtype=float)
    
    for i, d in enumerate(d_list):
        for j, tau in enumerate(tau_list):
            try:
                result = quantify_single_configuration(u, d, tau, r)
                rec_matrix[i, j] = result.REC
                line_matrix[i, j] = result.LINE
            except ValueError as exc:
                warnings.warn(
                    f"Skipping configuration (d={d}, tau={tau}): {exc}",
                    category=UserWarning
                )
                rec_matrix[i, j] = np.nan
                line_matrix[i, j] = np.nan
                
    return {
        "REC_matrix": rec_matrix,
        "LINE_matrix": line_matrix,
        "d_grid": d_list,
        "tau_grid": tau_list
    }

# ==========================================
# 5. VISUALIZATION MODULE (Scientific Figures)
# ==========================================

def plot_recurrence_plot(R: np.ndarray, title: str = "Recurrence Plot") -> None:
    """
    Visualizes the binary recurrence matrix as a Recurrence Plot.
    
    Uses aspect="equal" to ensure the N x N physical dimensions of the 
    attractor are strictly preserved visually, and origin="lower" to map 
    the progression of time correctly.
    """
    plt.figure(figsize=(6, 6))
    
    # Custom binary colormap ensures strict black/white rendering
    cmap = ListedColormap(['white', 'black'])
    
    # aspect="equal" is strictly required for Recurrence Plots
    plt.imshow(R, cmap=cmap, origin='lower', interpolation='none', aspect='equal')
    plt.title(title)
    plt.xlabel("Time index (j)")
    plt.ylabel("Time index (i)")
    
    plt.tight_layout()
    plt.show()


def plot_percent_rec_surface(d_grid: list, tau_grid: list, rec_matrix: np.ndarray) -> None:
    """
    Plots the 3D response surface of Percent Recurrence (%REC).
    Forces a fixed view angle for strict scientific reproducibility across runs.
    """
    T, D_mesh = np.meshgrid(tau_grid, d_grid)
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(T, D_mesh, rec_matrix, cmap='viridis', edgecolor='none')
    
    # Fix the viewing angle for reproducible figures
    ax.view_init(elev=30, azim=-135)
    
    ax.set_title("Response Surface: Percent Recurrence (%REC)")
    ax.set_xlabel("Time Delay (\u03c4)")
    ax.set_ylabel("Embedding Dimension (d)")
    ax.set_zlabel("%REC")
    fig.colorbar(surf, shrink=0.5, aspect=10, label="%REC")
    
    plt.tight_layout()
    plt.show()


def plot_percent_line_surface(d_grid: list, tau_grid: list, line_matrix: np.ndarray) -> None:
    """
    Plots the 3D response surface of Percent Line Segments (%LINE).
    Forces a fixed view angle for strict scientific reproducibility across runs.
    """
    T, D_mesh = np.meshgrid(tau_grid, d_grid)
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(T, D_mesh, line_matrix, cmap='plasma', edgecolor='none')
    
    # Fix the viewing angle for reproducible figures
    ax.view_init(elev=30, azim=-135)
    
    ax.set_title("Response Surface: Percent Line Segments (%LINE)")
    ax.set_xlabel("Time Delay (\u03c4)")
    ax.set_ylabel("Embedding Dimension (d)")
    ax.set_zlabel("%LINE")
    fig.colorbar(surf, shrink=0.5, aspect=10, label="%LINE")
    
    plt.tight_layout()
    plt.show()


def plot_heatmap(matrix: np.ndarray, title: str, x_labels: list, y_labels: list) -> None:
    """
    Generates a strictly bound 2D heatmap (0-100 scale) for cross-experiment 
    comparability of percentage-based metrics.
    """
    plt.figure(figsize=(7, 5))
    
    # Enforce vmin=0 and vmax=100 since both %REC and %LINE are percentages
    plt.imshow(matrix, cmap='inferno', origin='lower', aspect='auto', vmin=0, vmax=100)
    plt.colorbar(label="Metric Value (%)")
    
    plt.title(title)
    plt.xlabel("Time Delay (\u03c4)")
    plt.ylabel("Embedding Dimension (d)")
    
    plt.xticks(ticks=np.arange(len(x_labels)), labels=x_labels)
    plt.yticks(ticks=np.arange(len(y_labels)), labels=y_labels)
    
    plt.tight_layout()
    plt.show()


# ==========================================
# 6. PAPER WRAPPER MODULE (Executable Paper)
# ==========================================

from dataclasses import dataclass

"""
This wrapper reproduces the experimental workflow reported in 
Zbilut & Webber (1992). 

The implementation strictly follows the original publication's approach 
to topological unfolding, rather than later Recurrence Quantification 
Analysis (RQA) conventions.
"""

DEFAULT_RADIUS_RATIO = 0.1

@dataclass
class SweepResult:
    """
    Data container for the parameter sweep results, representing 
    the topological unfolding response surfaces.
    """
    REC_matrix: np.ndarray
    LINE_matrix: np.ndarray
    d_grid: list
    tau_grid: list
    radius: float
    radius_ratio: float


def run_zbilut1992(
    u: np.ndarray, 
    d_list: list, 
    tau_list: list, 
    radius_ratio: float = DEFAULT_RADIUS_RATIO,
    plot: bool = True
) -> SweepResult:
    """
    Entry point to reproduce the topological unfolding analysis.
    
    Automatically determines the baseline empirical radius, sweeps the 
    specified parameter grids, and optionally generates the resulting 
    topological surfaces. Decoupled from plotting for batch processing.
    
    Parameters
    ----------
    u : np.ndarray
        1D time series array.
    d_list : list of int
        List of embedding dimensions to sweep.
    tau_list : list of int
        List of time delays to sweep.
    radius_ratio : float
        Ratio of the baseline mean distance used to set the threshold.
    plot : bool
        If True, generates and displays the response surface figures.
        
    Returns
    -------
    SweepResult
        Dataclass containing all parameter grids and output matrices.
    """
    if plot:
        print("Initializing Zbilut & Webber (1992) Reproduction Pipeline...")
    
    # 1. Establish Baseline Radius
    X_baseline = reconstruct_phase_space(u, d=1, tau=1)
    D_baseline = compute_distance_matrix(X_baseline)
    r = estimate_baseline_radius(D_baseline, radius_ratio=radius_ratio)
    
    if plot:
        print(f"Empirical radius calculated at {radius_ratio*100}% of baseline mean distance: {r:.4f}")
        print("Executing parameter sweep for topological unfolding...")
        
    # 2. Execute Parameter Sweep
    raw_sweep = parameter_sweep(u, d_list, tau_list, r)
    
    rec_matrix = raw_sweep["REC_matrix"]
    line_matrix = raw_sweep["LINE_matrix"]
    
    # 3. Visualization Pipeline (Decoupled)
    if plot:
        # Target the Peak Configuration for %LINE
        flat_idx = np.nanargmax(line_matrix)
        row_idx, col_idx = np.unravel_index(flat_idx, line_matrix.shape)
        
        peak_d = d_list[row_idx]
        peak_tau = tau_list[col_idx]
        peak_line_val = line_matrix[row_idx, col_idx]
        
        print("Generating response surfaces...")
        print(f"Plotting optimal RP at %LINE Peak (d={peak_d}, \u03c4={peak_tau}) with %LINE={peak_line_val:.2f}%...")
        
        peak_config = quantify_single_configuration(u, peak_d, peak_tau, r)
        
        plot_recurrence_plot(
            peak_config.R, 
            title=f"Recurrence Plot at %LINE Peak (d={peak_d}, \u03c4={peak_tau})"
        )
        
        plot_percent_rec_surface(d_list, tau_list, rec_matrix)
        plot_percent_line_surface(d_list, tau_list, line_matrix)
        
        plot_heatmap(rec_matrix, "Heatmap: %REC", x_labels=tau_list, y_labels=d_list)
        plot_heatmap(line_matrix, "Heatmap: %LINE", x_labels=tau_list, y_labels=d_list)
        
        print("Pipeline execution complete.")
    
    # 4. Return Scientific Data Object
    return SweepResult(
        REC_matrix=rec_matrix,
        LINE_matrix=line_matrix,
        d_grid=d_list,
        tau_grid=tau_list,
        radius=r,
        radius_ratio=radius_ratio
    )