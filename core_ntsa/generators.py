"""
Nonlinear Time Series Generators

This module provides functions to simulate standard chaotic dynamical systems,
including continuous-time systems (Lorenz, Rossler) and discrete-time maps (Henon).
All functions return multi-dimensional numpy arrays representing phase space trajectories.
"""

import numpy as np
from scipy.integrate import solve_ivp
from typing import Tuple


def simulate_lorenz(
    initial_state: Tuple[float, float, float] = (1.0, 1.0, 1.0),
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    t_span: float = 100.0,
    dt: float = 0.01,
    transient_drop: int = 1000
) -> np.ndarray:
    """
    Generate a time series from the Lorenz chaotic attractor.

    Args:
        initial_state: A tuple (x0, y0, z0) representing the starting coordinates.
        sigma: Prandt number parameter.
        rho: Rayleigh number parameter.
        beta: Geometric factor parameter.
        t_span: Total time of simulation.
        dt: Time step for evaluation.
        transient_drop: Number of initial data points to discard to remove transients.

    Returns:
        A numpy array of shape (3, N) containing the x, y, z trajectories.
    """
    def lorenz_derivatives(t: float, state: np.ndarray) -> Tuple[float, float, float]:
        x, y, z = state
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return dx_dt, dy_dt, dz_dt

    t_eval = np.arange(0, t_span, dt)
    solution = solve_ivp(
        fun=lorenz_derivatives,
        t_span=(0, t_span),
        y0=initial_state,
        t_eval=t_eval,
        method='RK45'
    )
    
    return solution.y[:, transient_drop:]


def simulate_rossler(
    initial_state: Tuple[float, float, float] = (1.0, 1.0, 1.0),
    a: float = 0.2,
    b: float = 0.2,
    c: float = 5.7,
    t_span: float = 500.0,
    dt: float = 0.1,
    transient_drop: int = 1000
) -> np.ndarray:
    """
    Generate a time series from the Rossler chaotic attractor.

    Args:
        initial_state: A tuple (x0, y0, z0) representing the starting coordinates.
        a: Parameter a.
        b: Parameter b.
        c: Parameter c.
        t_span: Total time of simulation.
        dt: Time step for evaluation.
        transient_drop: Number of initial data points to discard.

    Returns:
        A numpy array of shape (3, N) containing the x, y, z trajectories.
    """
    def rossler_derivatives(t: float, state: np.ndarray) -> Tuple[float, float, float]:
        x, y, z = state
        dx_dt = -y - z
        dy_dt = x + a * y
        dz_dt = b + z * (x - c)
        return dx_dt, dy_dt, dz_dt

    t_eval = np.arange(0, t_span, dt)
    solution = solve_ivp(
        fun=rossler_derivatives,
        t_span=(0, t_span),
        y0=initial_state,
        t_eval=t_eval,
        method='RK45'
    )
    
    return solution.y[:, transient_drop:]


def simulate_henon(
    initial_state: Tuple[float, float] = (0.1, 0.1),
    a: float = 1.4,
    b: float = 0.3,
    n_iterations: int = 10000,
    transient_drop: int = 1000
) -> np.ndarray:
    """
    Generate a time series from the Henon discrete chaotic map.

    Args:
        initial_state: A tuple (x0, y0) representing the starting coordinates.
        a: Parameter a (governs the nonlinearity).
        b: Parameter b (governs the dissipation).
        n_iterations: Total number of discrete steps to simulate.
        transient_drop: Number of initial iterations to discard.

    Returns:
        A numpy array of shape (2, N) containing the x, y sequences.
    """
    total_steps = n_iterations + transient_drop
    x = np.zeros(total_steps)
    y = np.zeros(total_steps)
    
    x[0], y[0] = initial_state
    
    for i in range(total_steps - 1):
        x[i + 1] = 1.0 - a * (x[i] ** 2) + y[i]
        y[i + 1] = b * x[i]
        
    trajectory = np.vstack((x, y))
    return trajectory[:, transient_drop:]



# SMALL 2001: PPS Algorithm
