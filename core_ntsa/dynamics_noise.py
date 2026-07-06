import numpy as np
from typing import Tuple

def simulate_lorenz_sde(
    initial_state: Tuple[float, float, float] = (1.0, 1.0, 1.0),
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    t_span: float = 100.0,
    dt: float = 0.01,
    transient_drop: int = 1000,
    noise_intensity: float = 1.0,  # Tham số alpha kiểm soát cường độ nhiễu nội sinh
    seed: int = None
) -> np.ndarray:
    """
    Generate a time series from the Lorenz chaotic attractor with dynamical (internal) noise
    using the Euler-Maruyama integration method.

    Args:
        initial_state: A tuple (x0, y0, z0) representing the starting coordinates.
        sigma: Prandtl number parameter.
        rho: Rayleigh number parameter.
        beta: Geometric factor parameter.
        t_span: Total time of simulation.
        dt: Time step for evaluation.
        transient_drop: Number of initial data points to discard to remove transients.
        noise_intensity: Amplitude of the dynamical noise (alpha). Set to 0.0 for deterministic.
        seed: Random seed for reproducible stochastic generation.

    Returns:
        A numpy array of shape (3, N) containing the x, y, z trajectories.
    """
    if seed is not None:
        np.random.seed(seed)
        
    num_steps = int(t_span / dt)
    
    # Khởi tạo ma trận lưu trữ toàn bộ quỹ đạo
    trajectory = np.zeros((3, num_steps))
    x, y, z = initial_state
    
    # Pre-compute căn bậc hai của dt để tối ưu tốc độ trong vòng lặp
    sqrt_dt = np.sqrt(dt)
    
    for i in range(num_steps):
        # Lưu trạng thái hiện tại
        trajectory[0, i] = x
        trajectory[1, i] = y
        trajectory[2, i] = z
        
        # 1. Tính toán các thành phần tất định (Deterministic drift)
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        
        # 2. Tính toán các bước nhảy ngẫu nhiên Wiener (Stochastic diffusion)
        # dW tuân theo phân phối chuẩn N(0, dt)
        dW_x = np.random.normal(0, 1) * sqrt_dt
        dW_y = np.random.normal(0, 1) * sqrt_dt
        dW_z = np.random.normal(0, 1) * sqrt_dt
        
        # 3. Cập nhật trạng thái bằng Euler-Maruyama
        x += dx_dt * dt + noise_intensity * dW_x
        y += dy_dt * dt + noise_intensity * dW_y
        z += dz_dt * dt + noise_intensity * dW_z
        
    # Loại bỏ phần dữ liệu quá độ (transient) ban đầu
    if transient_drop >= num_steps:
        raise ValueError("transient_drop must be less than the total number of simulated steps.")
        
    return trajectory[:, transient_drop:]