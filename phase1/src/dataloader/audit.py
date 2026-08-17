"""Session-level acquisition audit."""

from typing import Any

import numpy as np
import pandas as pd

from .schema import (
    DT_ABS_TOLERANCE,
    EXPECTED_DT,
    EXPECTED_FS,
    FILTERED_PPG_COLUMN,
    FS_ABS_TOLERANCE,
    FS_REL_TOLERANCE,
    LABEL_COLUMN,
    LABEL_MAP,
    NUMERIC_COLUMNS,
    OPTIONAL_COLUMNS,
    RAW_PPG_COLUMN,
    REQUIRED_COLUMNS,
    STATUS_FAIL,
    STATUS_PASS,
    STATUS_WARNING,
    TIME_COLUMN,
    TIME_GAP_FACTOR,
    ZERO_DT_TOLERANCE,
)
from .segments import (
    calculate_window_availability,
    extract_label_segments,
    summarize_segments,
)


def _number(value: Any) -> int | float | None:
    """Convert numeric scalars to JSON-safe values."""
    if value is None or not np.isfinite(value):
        return None
    if isinstance(value, (np.integer, int)):
        return int(value)
    return float(value)


def _numeric_statistics(series: pd.Series | None) -> dict[str, Any]:
    """Calculate descriptive statistics on finite numeric values."""
    names = ("count", "min", "max", "range", "mean", "median",
             "std", "q1", "q3", "iqr", "n_unique")
    if series is None:
        return {name: None for name in names}

    numeric = pd.to_numeric(series, errors="coerce")
    finite = numeric[np.isfinite(numeric)]
    if finite.empty:
        result = {name: None for name in names}
        result["count"] = 0
        result["n_unique"] = 0
        return result

    q1 = finite.quantile(0.25)
    q3 = finite.quantile(0.75)
    return {
        "count": int(finite.count()),
        "min": _number(finite.min()),
        "max": _number(finite.max()),
        "range": _number(finite.max() - finite.min()),
        "mean": _number(finite.mean()),
        "median": _number(finite.median()),
        "std": _number(finite.std()),
        "q1": _number(q1),
        "q3": _number(q3),
        "iqr": _number(q3 - q1),
        "n_unique": int(finite.nunique()),
    }


def _time_audit(series: pd.Series | None) -> dict[str, Any]:
    """Audit the canonical time axis."""
    result = {
        "start_time_s": None,
        "end_time_s": None,
        "duration_s": None,
        "dt_min": None,
        "dt_max": None,
        "dt_mean": None,
        "dt_median": None,
        "dt_std": None,
        "estimated_fs": None,
        "n_duplicate_timestamps": 0,
        "n_non_monotonic_timestamps": 0,
        "n_negative_dt": 0,
        "n_zero_dt": 0,
        "n_time_gaps": 0,
    }
    if series is None:
        return result

    numeric = pd.to_numeric(series, errors="coerce")
    finite = numeric[np.isfinite(numeric)]
    if finite.empty:
        return result

    result["start_time_s"] = _number(finite.iloc[0])
    result["end_time_s"] = _number(finite.iloc[-1])
    result["duration_s"] = _number(finite.iloc[-1] - finite.iloc[0])
    result["n_duplicate_timestamps"] = int(finite.duplicated().sum())

    diffs = numeric.diff()
    finite_diffs = diffs[np.isfinite(diffs)]
    if finite_diffs.empty:
        return result

    result.update({
        "dt_min": _number(finite_diffs.min()),
        "dt_max": _number(finite_diffs.max()),
        "dt_mean": _number(finite_diffs.mean()),
        "dt_median": _number(finite_diffs.median()),
        "dt_std": _number(finite_diffs.std()),
        "n_non_monotonic_timestamps": int((finite_diffs < 0).sum()),
        "n_negative_dt": int((finite_diffs < 0).sum()),
        "n_zero_dt": int(
            (finite_diffs.abs() <= ZERO_DT_TOLERANCE).sum()
        ),
        "n_time_gaps": int(
            (finite_diffs > EXPECTED_DT * TIME_GAP_FACTOR).sum()
        ),
    })
    median_dt = float(finite_diffs.median())
    if median_dt > ZERO_DT_TOLERANCE:
        result["estimated_fs"] = 1.0 / median_dt
    return result


def _label_audit(
    series: pd.Series | None,
    n_rows: int,
    sample_dt: float,
) -> dict[str, Any]:
    """Audit fixed external labels without changing them."""
    result: dict[str, Any] = {
        "unique_labels": [],
        "invalid_labels": [],
        "null_labels": n_rows if series is None else int(series.isna().sum()),
    }
    numeric = (pd.Series(dtype=float) if series is None
               else pd.to_numeric(series, errors="coerce"))
    valid = numeric.isin(LABEL_MAP)
    non_null_original = (pd.Series(False, index=numeric.index)
                         if series is None else series.notna())
    invalid_mask = non_null_original & ~valid
    invalid_values = (
        series[invalid_mask].unique().tolist()
        if series is not None else []
    )
    result["invalid_labels"] = sorted(
        (_json_scalar(value) for value in invalid_values),
        key=str,
    )
    result["unique_labels"] = sorted(
        int(value) for value in numeric[valid].unique()
    )

    for label, state in LABEL_MAP.items():
        name = state.lower()
        count = int((numeric == label).sum())
        result[f"{name}_samples"] = count
        result[f"{name}_percentage"] = (
            100.0 * count / n_rows if n_rows else 0.0
        )
        result[f"{name}_duration_s"] = count * sample_dt
    return result


def _json_scalar(value: Any) -> Any:
    """Convert a scalar to a stable built-in type."""
    if pd.isna(value):
        return None
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def audit_session(
    df: pd.DataFrame,
    session_id: str,
    file_name: str,
) -> dict[str, Any]:
    """Create a factual audit record for one loaded session."""
    issues: list[str] = []
    failures: list[str] = []
    n_rows = len(df)
    columns = list(df.columns)
    missing_columns = [name for name in REQUIRED_COLUMNS
                       if name not in columns]
    unexpected_columns = [name for name in columns
                          if name not in REQUIRED_COLUMNS + OPTIONAL_COLUMNS]
    empty_columns = [name for name in columns if df[name].isna().all()]

    if n_rows == 0:
        failures.append("CSV contains no data rows")
    for name in missing_columns:
        failures.append(f"Missing required column: {name}")
    for name in unexpected_columns:
        issues.append(f"Unexpected column: {name}")
    for name in empty_columns:
        issues.append(f"Empty column: {name}")

    missing_values = {}
    for name in columns:
        count = int(df[name].isna().sum())
        missing_values[name] = {
            "null_count": count,
            "null_percentage": 100.0 * count / n_rows if n_rows else 0.0,
        }
        if count and name not in empty_columns:
            issues.append(f"{count} null values in column: {name}")

    infinity_counts = {}
    invalid_numeric_counts = {}
    for name in columns:
        if (name in NUMERIC_COLUMNS
                or pd.api.types.is_numeric_dtype(df[name])):
            numeric = pd.to_numeric(df[name], errors="coerce")
            invalid = int((df[name].notna() & numeric.isna()).sum())
            positive = int(np.isposinf(numeric).sum())
            negative = int(np.isneginf(numeric).sum())
            invalid_numeric_counts[name] = invalid
            infinity_counts[name] = {
                "positive_inf": positive,
                "negative_inf": negative,
            }
            if invalid:
                issues.append(
                    f"{invalid} non-numeric values in column: {name}"
                )
            if positive or negative:
                issues.append(
                    f"{positive + negative} infinite values in column: {name}"
                )

    time_series = df.get(TIME_COLUMN)
    raw_series = df.get(RAW_PPG_COLUMN)
    label_series = df.get(LABEL_COLUMN)
    time_numeric = (None if time_series is None
                    else pd.to_numeric(time_series, errors="coerce"))
    raw_numeric = (None if raw_series is None
                   else pd.to_numeric(raw_series, errors="coerce"))
    label_numeric = (None if label_series is None
                     else pd.to_numeric(label_series, errors="coerce"))

    if time_series is not None and (
        time_numeric is None or not np.isfinite(time_numeric).any()
    ):
        failures.append(f"{TIME_COLUMN} is completely invalid")
    if raw_series is not None and (
        raw_numeric is None or not np.isfinite(raw_numeric).any()
    ):
        failures.append(f"{RAW_PPG_COLUMN} is completely missing or invalid")
    if label_series is not None and (
        label_numeric is None or not label_numeric.notna().any()
    ):
        failures.append(f"{LABEL_COLUMN} is completely missing or invalid")

    duplicate_rows = int(df.duplicated().sum())
    if duplicate_rows:
        issues.append(f"{duplicate_rows} duplicate rows")

    time_audit = _time_audit(time_series)
    if time_audit["n_duplicate_timestamps"]:
        issues.append(
            f"{time_audit['n_duplicate_timestamps']} duplicated timestamps"
        )
    if time_audit["n_non_monotonic_timestamps"]:
        count = time_audit["n_non_monotonic_timestamps"]
        issues.append(
            f"{count} non-monotonic timestamps"
        )
    if time_audit["n_time_gaps"]:
        issues.append(f"{time_audit['n_time_gaps']} time gaps")
    estimated_fs = time_audit["estimated_fs"]
    if estimated_fs is not None and not np.isclose(
        estimated_fs,
        EXPECTED_FS,
        rtol=FS_REL_TOLERANCE,
        atol=FS_ABS_TOLERANCE,
    ):
        issues.append(
            f"Estimated sampling rate {estimated_fs:.6g} Hz differs from "
            f"expected {EXPECTED_FS:g} Hz"
        )

    positive_dt = EXPECTED_DT
    if time_numeric is not None:
        diffs = time_numeric.diff()
        valid_diffs = diffs[
            np.isfinite(diffs) & (diffs > ZERO_DT_TOLERANCE)
        ]
        if not valid_diffs.empty:
            positive_dt = float(valid_diffs.median())
    label_audit = _label_audit(label_series, n_rows, positive_dt)
    if label_audit["null_labels"] and label_series is not None:
        issues.append(f"{label_audit['null_labels']} null labels")
    if label_audit["invalid_labels"]:
        issues.append(
            f"Invalid labels: {label_audit['invalid_labels']}"
        )

    segments = []
    if time_series is not None and label_series is not None and n_rows:
        segments = extract_label_segments(time_series, label_series)
    segment_summary = summarize_segments(segments)
    availability = calculate_window_availability(segments)
    raw_statistics = _numeric_statistics(raw_series)
    filtered_statistics = _numeric_statistics(df.get(FILTERED_PPG_COLUMN))

    status = STATUS_FAIL if failures else (
        STATUS_WARNING if issues else STATUS_PASS
    )
    all_issues = failures + issues
    record: dict[str, Any] = {
        "session_id": session_id,
        "file_name": file_name,
        "status": status,
        "issues": all_issues,
        "n_rows": n_rows,
        "n_columns": len(columns),
        "column_names": columns,
        "missing_required_columns": missing_columns,
        "unexpected_columns": unexpected_columns,
        "empty_columns": empty_columns,
        "duplicate_rows": duplicate_rows,
        "missing_values": missing_values,
        "invalid_numeric_counts": invalid_numeric_counts,
        "infinity_counts": infinity_counts,
        "time_axis": time_audit,
        "raw_statistics": raw_statistics,
        "filtered_statistics": filtered_statistics,
        "label_audit": label_audit,
        "segments": segments,
        "segment_summary": segment_summary,
        "window_availability": availability,
    }
    record.update(time_audit)
    record.update({f"raw_{key}": value
                   for key, value in raw_statistics.items()})
    record.update(label_audit)
    record.update(segment_summary)
    record.update(availability)
    return record
