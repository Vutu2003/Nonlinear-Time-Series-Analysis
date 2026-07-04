"""
Noise Generation and Signal Corruption Tools

This module provides utilities to add various types of realistic stochastic noise
and deterministic artifacts to time series data. It is specifically designed to 
stress-test nonlinear dynamical analysis algorithms.
"""

import numpy as np
from typing import Literal


def add_white_noise(signal: np.ndarray, snr_db: float) -> np.ndarray:
    """
    Add Gaussian white noise to a signal based on a target Signal-to-Noise Ratio (SNR).

    Args:
        signal: A 1D numpy array representing the original clean signal.
        snr_db: The desired Signal-to-Noise Ratio in decibels (dB).

    Returns:
        A 1D numpy array containing the corrupted signal.
    """
    signal_power = np.mean(signal ** 2)
    
    # Calculate required noise power to achieve target SNR
    target_noise_power = signal_power / (10.0 ** (snr_db / 10.0))
    
    # Generate Gaussian white noise
    noise = np.random.normal(0.0, np.sqrt(target_noise_power), size=signal.shape)
    
    return signal + noise


def add_colored_noise(
    signal: np.ndarray, 
    snr_db: float, 
    color: str = 'pink'
) -> np.ndarray:
    """
    Add power-law (colored) noise to a signal using frequency domain filtering.
    Pink noise (1/f) simulates physiological background noise.
    Brown noise (1/f^2) simulates random walk or wandering baselines.
    """
    n = len(signal)
    
    # 1. Sinh nhiễu trắng miền thời gian
    white_noise = np.random.normal(0.0, 1.0, n)
    
    # 2. Biến đổi Fourier sang miền tần số
    fft_noise = np.fft.rfft(white_noise)
    freqs = np.fft.rfftfreq(n)
    
    # 3. Tạo bộ lọc định hình (Shaping Filter)
    filter_weights = np.zeros_like(freqs)
    
    # Chỉ áp dụng lọc cho các tần số > 0 (bỏ qua index 0)
    if color == 'pink':
        filter_weights[1:] = 1.0 / np.sqrt(freqs[1:])
    elif color == 'brown':
        filter_weights[1:] = 1.0 / freqs[1:]
    else:
        raise ValueError("Invalid color. Choose 'pink' or 'brown'.")
        
    # 4. Nhân phổ nhiễu với bộ lọc và chuyển về miền thời gian
    fft_noise = fft_noise * filter_weights
    colored_noise = np.fft.irfft(fft_noise, n)
    
    # 5. Ép giá trị trung bình về 0 (Loại bỏ triệt để DC offset)
    colored_noise = colored_noise - np.mean(colored_noise)
    
    # 6. Chuẩn hóa năng lượng theo SNR
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(colored_noise ** 2)
    
    target_noise_power = signal_power / (10.0 ** (snr_db / 10.0))
    scaling_factor = np.sqrt(target_noise_power / noise_power)
    
    scaled_colored_noise = colored_noise * scaling_factor
    
    return signal + scaled_colored_noise


def add_motion_artifacts(
    signal: np.ndarray, 
    num_artifacts: int = 3, 
    max_length: int = 50, 
    amplitude_ratio: float = 3.0
) -> np.ndarray:
    """
    Simulate sudden motion artifacts (transient bursts) on the signal.

    Args:
        signal: A 1D numpy array representing the original clean signal.
        num_artifacts: Total number of artifact bursts to inject.
        max_length: Maximum duration (in sample points) of each artifact.
        amplitude_ratio: Ratio of artifact amplitude relative to signal standard deviation.

    Returns:
        A 1D numpy array containing the signal with localized artifacts.
    """
    corrupted_signal = signal.copy()
    n = len(signal)
    signal_std = np.std(signal)
    
    for _ in range(num_artifacts):
        # Random start point and length
        start_idx = np.random.randint(0, n - max_length)
        length = np.random.randint(max_length // 2, max_length)
        
        # Create a transient burst (windowed noise)
        window = np.hanning(length)
        burst_noise = np.random.normal(0, signal_std * amplitude_ratio, length)
        artifact = burst_noise * window
        
        # Inject into the signal
        corrupted_signal[start_idx:start_idx + length] += artifact
        
    return corrupted_signal


def add_baseline_wander(
    signal: np.ndarray, 
    frequency: float = 0.2, 
    sampling_rate: float = 100.0, 
    amplitude_ratio: float = 1.0
) -> np.ndarray:
    """
    Add low-frequency sinusoidal baseline wander to simulate respiration 
    or sensor drift.

    Args:
        signal: A 1D numpy array representing the original clean signal.
        frequency: The frequency of the baseline wander in Hz.
        sampling_rate: The sampling rate of the signal in Hz.
        amplitude_ratio: Peak amplitude of wander relative to signal standard deviation.

    Returns:
        A 1D numpy array containing the signal with baseline wander.
    """
    n = len(signal)
    t = np.arange(n) / sampling_rate
    
    signal_std = np.std(signal)
    wander_amplitude = signal_std * amplitude_ratio
    
    wander = wander_amplitude * np.sin(2 * np.pi * frequency * t)
    
    return signal + wander