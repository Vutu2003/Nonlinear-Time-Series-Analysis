"""Continuous label segment characterization."""

from collections.abc import Sequence
from typing import Any

import numpy as np
import pandas as pd

from .schema import LABEL_MAP, WINDOW_DURATIONS


def _clean_label(value: Any) -> Any:
    """Convert labels to stable Python scalar values."""
    if pd.isna(value):
        return None
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def _same_label(left: Any, right: Any) -> bool:
    """Compare labels while treating missing labels as equal."""
    if left is None or right is None:
        return left is right
    return bool(left == right)


def _time_value(value: Any) -> float | None:
    """Return a finite timestamp or None."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if np.isfinite(number) else None


def extract_label_segments(
    time_s: Sequence[Any] | pd.Series,
    labels: Sequence[Any] | pd.Series,
) -> list[dict[str, Any]]:
    """Extract contiguous runs of unchanged labels."""
    times = list(time_s)
    clean_labels = [_clean_label(value) for value in labels]
    if len(times) != len(clean_labels):
        raise ValueError("time_s and labels must have equal lengths")
    if not clean_labels:
        return []

    boundaries = [0]
    for index in range(1, len(clean_labels)):
        if not _same_label(clean_labels[index], clean_labels[index - 1]):
            boundaries.append(index)
    boundaries.append(len(clean_labels))

    segments = []
    for segment_id, (start, stop) in enumerate(
        zip(boundaries, boundaries[1:]),
        start=1,
    ):
        end = stop - 1
        label = clean_labels[start]
        start_time = _time_value(times[start])
        end_time = _time_value(times[end])
        duration = None
        if start_time is not None and end_time is not None:
            duration = max(end_time - start_time, 0.0)
        segments.append({
            "segment_id": segment_id,
            "label": label,
            "state": LABEL_MAP.get(label, "Unknown"),
            "start_index": start,
            "end_index": end,
            "start_time_s": start_time,
            "end_time_s": end_time,
            "n_samples": stop - start,
            "duration_s": duration,
        })
    return segments


def summarize_segments(segments: Sequence[dict[str, Any]]) -> dict[str, Any]:
    """Summarize valid Awake and Drowsy segments."""
    summary: dict[str, Any] = {
        "n_segments": len(segments),
        "n_transitions": max(len(segments) - 1, 0),
    }
    for label, state in LABEL_MAP.items():
        name = state.lower()
        state_segments = [item for item in segments
                          if item["label"] == label]
        durations = [item["duration_s"] for item in state_segments
                     if item["duration_s"] is not None]
        summary[f"n_{name}_segments"] = len(state_segments)
        summary[f"longest_{name}_segment_s"] = (
            max(durations) if durations else 0.0
        )
        summary[f"median_{name}_segment_s"] = (
            float(np.median(durations)) if durations else 0.0
        )
    return summary


def calculate_window_availability(
    segments: Sequence[dict[str, Any]],
) -> dict[str, bool | int]:
    """Check window eligibility without creating windows."""
    result: dict[str, bool | int] = {}
    for duration in WINDOW_DURATIONS:
        eligible_by_state = {}
        for label, state in LABEL_MAP.items():
            name = state.lower()
            count = sum(
                item["label"] == label
                and item["duration_s"] is not None
                and item["duration_s"] >= duration
                for item in segments
            )
            result[f"n_{name}_segments_ge_{duration}"] = count
            result[f"{name}_ge_{duration}"] = count > 0
            eligible_by_state[label] = count > 0
        result[f"paired_{duration}"] = all(eligible_by_state.values())
    return result
