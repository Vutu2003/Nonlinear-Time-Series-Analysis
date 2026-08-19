import matplotlib.pyplot as plt
import numpy as np


def reconstruct_phase_space(signal, m, tau, plot=False):
    """Reconstruct phase space using time-delay embedding."""
    signal = np.asarray(signal, dtype=float)

    if signal.ndim != 1:
        raise ValueError("signal must be a 1D array.")
    if not np.isfinite(signal).all():
        raise ValueError("signal must contain only finite values.")
    if isinstance(m, bool) or not isinstance(m, (int, np.integer)):
        raise TypeError("m must be an integer.")
    if isinstance(tau, bool) or not isinstance(tau, (int, np.integer)):
        raise TypeError("tau must be an integer.")
    if m < 2:
        raise ValueError("m must be at least 2.")
    if tau < 1:
        raise ValueError("tau must be at least 1.")

    n_vectors = len(signal) - (m - 1) * tau
    if n_vectors <= 0:
        raise ValueError("signal is too short for the requested m and tau.")

    phase_space = np.column_stack([
        signal[offset:offset + n_vectors]
        for offset in range(0, m * tau, tau)
    ])

    if plot:
        if m == 2:
            fig, ax = plt.subplots(figsize=(4.5, 4.0), dpi=150)

            ax.plot(
                phase_space[:, 0],
                phase_space[:, 1],
                linewidth=0.8,
            )

            ax.set_xlabel(r"$x(t)$", fontsize=11)
            ax.set_ylabel(rf"$x(t + {tau}\tau_s)$", fontsize=11)
            ax.tick_params(labelsize=9)

            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.set_box_aspect(1)

        elif m == 3:
            fig = plt.figure(figsize=(5.2, 4.6), dpi=150)
            ax = fig.add_subplot(111, projection="3d")

            ax.plot(
                phase_space[:, 0],
                phase_space[:, 1],
                phase_space[:, 2],
                linewidth=0.7,
            )

            ax.set_xlabel(r"$x(t)$", fontsize=10, labelpad=8)
            ax.set_ylabel(
                rf"$x(t + {tau}\tau_s)$",
                fontsize=10,
                labelpad=8,
            )
            ax.set_zlabel(
                rf"$x(t + {2 * tau}\tau_s)$",
                fontsize=10,
                labelpad=8,
            )
            ax.tick_params(labelsize=8)

            ax.grid(False)
            ax.view_init(elev=25, azim=45)

        else:
            raise ValueError("plot=True supports only m=2 or m=3.")

        fig.tight_layout()
        plt.show()

    return phase_space