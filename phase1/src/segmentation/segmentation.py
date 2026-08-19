# Segmentation core workflow
#
# 1. Nhận đầu vào của một processed session:
#    time, raw PPG, processed PPG, label, SQI mask, fs.
#
# 2. Với từng window size:
#    60, 120, 180, 240, 300 s.
#
# 3. Chia session thành các non-overlapping full windows.
#    Bỏ phần cuối nếu không đủ đúng window length.
#
# 4. Với mỗi candidate window, kiểm tra:
#    - đủ đúng số sample;
#    - chỉ chứa một label;
#    - không chứa acquisition gap;
#    - SQI mask không có bất kỳ True nào.
#
# 5. Reject ngay nếu fail một điều kiện.
#
# 6. Với window hợp lệ, giữ cùng một interval cho:
#    - time;
#    - raw PPG;
#    - processed PPG.
#
# 7. Lưu metadata:
#    session, window_id, start, end, duration, fs, label.
#
# 8. Trả về:
#    {
#        60:  [valid windows],
#        120: [valid windows],
#        180: [valid windows],
#        240: [valid windows],
#        300: [valid windows],
#    }
#
# 9. Quasi-stationarity validation thực hiện sau segmentation,
#    không đặt logic đó bên trong segmentation core.

import numpy as np


def segment_session(
    time_s: np.ndarray,
    ppg_raw: np.ndarray,
    ppg_processed: np.ndarray,
    labels: np.ndarray,
    sqi_mask: np.ndarray,
    fs: float,
    session_id: str = "",
    window_sizes: tuple[int, ...] = (60, 120, 180),
    gap_factor: float = 1.5,
) -> dict[int, list[dict]]:
    """
    Segment one PPG session into valid single-state analysis windows.

    Continuous label segments are identified first. Each segment is then
    divided independently into complete, non-overlapping windows for every
    requested duration. Any incomplete remainder at the end of a label
    segment is discarded.

    A candidate window is retained only if it contains no acquisition gap
    and no SQI-invalid samples. Raw and processed PPG are always extracted
    from the same time interval.

    Parameters
    ----------
    time_s : np.ndarray
        Time axis in seconds.
    ppg_raw : np.ndarray
        Raw PPG signal.
    ppg_processed : np.ndarray
        Processed PPG signal aligned with the raw signal.
    labels : np.ndarray
        Sample-level state labels.
    sqi_mask : np.ndarray
        Boolean mask where True marks an SQI-invalid region.
    fs : float
        Sampling rate in Hz.
    session_id : str, optional
        Session identifier stored in each retained window.
    window_sizes : tuple[int, ...], optional
        Analysis-window durations in seconds.
    gap_factor : float, optional
        Maximum allowed interval relative to the expected interval 1 / fs.

    Returns
    -------
    dict[int, list[dict]]
        Dictionary keyed by window duration. Each value contains the valid
        windows for that duration. Empty lists are kept when no valid window
        exists for a requested size.
    """

    time_s = np.asarray(time_s, dtype=float)
    ppg_raw = np.asarray(ppg_raw, dtype=float)
    ppg_processed = np.asarray(ppg_processed, dtype=float)
    labels = np.asarray(labels)
    sqi_mask = np.asarray(sqi_mask, dtype=bool)

    arrays = (
        time_s,
        ppg_raw,
        ppg_processed,
        labels,
        sqi_mask,
    )

    if any(array.ndim != 1 for array in arrays):
        raise ValueError("All inputs must be 1D arrays.")

    if len({len(array) for array in arrays}) != 1:
        raise ValueError("All input arrays must have the same length.")

    if fs <= 0:
        raise ValueError("fs must be greater than 0.")

    if gap_factor <= 1:
        raise ValueError("gap_factor must be greater than 1.")

    if any(size <= 0 for size in window_sizes):
        raise ValueError("window_sizes must contain positive values.")

    if not np.isfinite(time_s).all():
        raise ValueError("time_s must contain only finite values.")

    if not np.isfinite(ppg_raw).all():
        raise ValueError("ppg_raw must contain only finite values.")

    if not np.isfinite(ppg_processed).all():
        raise ValueError("ppg_processed must contain only finite values.")

    results = {size: [] for size in window_sizes}
    expected_dt = 1.0 / fs

    # Find continuous label segments.
    change_points = np.flatnonzero(labels[1:] != labels[:-1]) + 1
    boundaries = np.concatenate(([0], change_points, [len(labels)]))

    window_ids = {size: 0 for size in window_sizes}

    for segment_start, segment_end in zip(
        boundaries[:-1],
        boundaries[1:],
    ):
        segment_label = labels[segment_start]

        for window_s in window_sizes:
            window_samples = int(round(window_s * fs))
            segment_length = segment_end - segment_start

            if segment_length < window_samples:
                continue

            # Use complete non-overlapping windows only.
            n_windows = segment_length // window_samples

            for index in range(n_windows):
                start = segment_start + index * window_samples
                end = start + window_samples

                time_window = time_s[start:end]
                sqi_window = sqi_mask[start:end]

                # Safety check for label consistency.
                if np.any(labels[start:end] != segment_label):
                    continue

                if sqi_window.any():
                    continue

                dt = np.diff(time_window)
                if np.any(dt > expected_dt * gap_factor):
                    continue

                window_ids[window_s] += 1

                results[window_s].append({
                    "session": session_id,
                    "window_id": window_ids[window_s],
                    "window_size_s": window_s,
                    "start_time": float(time_window[0]),
                    "end_time": float(time_window[-1]),
                    "duration_s": window_s,
                    "fs": float(fs),
                    "label": int(segment_label),
                    "time": time_window.copy(),
                    "ppg_raw": ppg_raw[start:end].copy(),
                    "ppg_processed": ppg_processed[start:end].copy(),
                })

    return results