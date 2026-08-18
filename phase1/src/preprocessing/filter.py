import numpy as np
from scipy.signal import butter, filtfilt


def preprocess_ppg(
    signal,
    fs,
    lowcut=0.5,
    highcut=8.0,
    order=2,
):
    """Invert and zero-phase bandpass filter a PPG signal."""
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be a 1D array.")

    if fs <= 0:
        raise ValueError("fs must be greater than 0.")

    nyquist = fs / 2.0

    if not 0 < lowcut < highcut < nyquist:
        raise ValueError(
            "Require 0 < lowcut < highcut < Nyquist frequency."
        )

    # Optical inversion
    inverted = -signal

    # Zero-phase Butterworth bandpass
    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(
        order,
        [low, high],
        btype="bandpass",
    )

    filtered = filtfilt(b, a, inverted)

    return inverted, filtered