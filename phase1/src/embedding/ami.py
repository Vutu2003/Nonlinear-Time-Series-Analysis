import numpy as np
from scipy.spatial import cKDTree
from scipy.special import digamma

# ksg_mi_1: 

def ksg_mi(x, y, k=3, jitter=0.0, random_state=None): 
    """
    Estimate mutual information using KSG Algorithm 1.

    Parameters
    ----------
    x, y : array-like
        Two 1D variables with equal length.
    k : int, default=3
        Number of nearest neighbors.
    jitter : float, default=0.0
        Relative Gaussian noise used to break exact ties.
    random_state : int or None
        Random seed used when jitter is enabled.

    Returns
    -------
    float
        Estimated mutual information in nats.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("x and y must be 1D arrays.")
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("x and y must contain only finite values.")
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)):
        raise TypeError("k must be an integer.")
    if k < 1:
        raise ValueError("k must be at least 1.")
    if len(x) <= k:
        raise ValueError("Number of samples must be greater than k.")
    if np.std(x) <= np.finfo(float).eps:
        raise ValueError("x must have non-zero variance.")
    if np.std(y) <= np.finfo(float).eps:
        raise ValueError("y must have non-zero variance.")
    if jitter < 0:
        raise ValueError("jitter must be non-negative.")

    if jitter > 0:
        rng = np.random.default_rng(random_state)
        x = x + rng.normal(0.0, jitter * np.std(x), size=len(x))
        y = y + rng.normal(0.0, jitter * np.std(y), size=len(y))

    samples = np.column_stack((x, y))
    joint_tree = cKDTree(samples)

    distances, _ = joint_tree.query(
        samples,
        k=k + 1,
        p=np.inf,
    )
    epsilon = distances[:, -1]

    # Enforce strict marginal distance: |dx| < epsilon.
    epsilon = np.nextafter(epsilon, 0.0)

    x_tree = cKDTree(x[:, None])
    y_tree = cKDTree(y[:, None])

    nx_plus_one = x_tree.query_ball_point(
        x[:, None],
        epsilon,
        p=np.inf,
        return_length=True,
    )
    ny_plus_one = y_tree.query_ball_point(
        y[:, None],
        epsilon,
        p=np.inf,
        return_length=True,
    )

    n_samples = len(x)

    mi = (
        digamma(k)
        + digamma(n_samples)
        - np.mean(
            digamma(nx_plus_one)
            + digamma(ny_plus_one)
        )
    )

    return float(mi)


def auto_mutual_information(
    signal,
    max_lag,
    k=3,
    jitter=0.0,
    random_state=None,
):
    """
    Compute auto-mutual information and select the first local minimum.

    Parameters
    ----------
    signal : array-like
        One-dimensional time series.
    max_lag : int
        Maximum lag in samples.
    k : int, default=3
        Number of neighbors for KSG-1.

    Returns
    -------
    tau : int or None
        First local minimum of AMI, in samples.
    lags : ndarray
        Evaluated lags.
    ami : ndarray
        Mutual information at each lag, in nats.
    """
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be a 1D array.")
    if not np.isfinite(signal).all():
        raise ValueError("signal must contain only finite values.")
    if isinstance(max_lag, bool) or not isinstance(
        max_lag, (int, np.integer)
    ):
        raise TypeError("max_lag must be an integer.")
    if max_lag < 2:
        raise ValueError("max_lag must be at least 2.")
    if max_lag >= len(signal):
        raise ValueError("max_lag must be smaller than signal length.")

    lags = np.arange(1, max_lag + 1)
    ami = np.empty(len(lags), dtype=float)

    for index, lag in enumerate(lags):
        x = signal[:-lag]
        y = signal[lag:]

        ami[index] = ksg_mi(
            x,
            y,
            k=k,
            jitter=jitter,
            random_state=random_state,
        )

    tau = None

    # Select the first strict local minimum.
    for index in range(1, len(ami) - 1):
        if ami[index] < ami[index - 1] and ami[index] < ami[index + 1]:
            tau = int(lags[index])
            break

    return tau, lags, ami