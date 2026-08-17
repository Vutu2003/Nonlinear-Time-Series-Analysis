"""Dataset-level audit orchestration and outputs."""

import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from .audit import audit_session
from .loader import load_session
from .models import DatasetAuditResult
from .schema import STATUS_FAIL, STATUS_PASS, STATUS_WARNING, WINDOW_DURATIONS

LOGGER = logging.getLogger(__name__)

NESTED_FIELDS = {
    "missing_values",
    "invalid_numeric_counts",
    "infinity_counts",
    "time_axis",
    "raw_statistics",
    "filtered_statistics",
    "label_audit",
    "segments",
    "segment_summary",
    "window_availability",
}


def _natural_key(path: Path) -> list[str | int]:
    """Return a deterministic human-order file key."""
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r"(\d+)", path.name)]


def _json_safe(value: Any) -> Any:
    """Recursively convert pandas and NumPy values for strict JSON."""
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, np.generic):
        value = value.item()
    if value is pd.NA or (isinstance(value, float) and not np.isfinite(value)):
        return None
    return value


def _write_json(path: Path, value: dict[str, Any]) -> None:
    """Write stable, strict JSON."""
    content = json.dumps(
        _json_safe(value),
        indent=2,
        sort_keys=True,
        allow_nan=False,
    )
    path.write_text(f"{content}\n", encoding="utf-8")


def _failed_report(
    session_id: str,
    file_name: str,
    exc: Exception,
) -> dict[str, Any]:
    """Build a controlled audit record for an unreadable file."""
    report = audit_session(pd.DataFrame(), session_id, file_name)
    report["issues"] = [f"{type(exc).__name__}: {exc}"]
    report["status"] = STATUS_FAIL
    return report


def _median(values: list[Any]) -> float | None:
    """Return the median of finite values."""
    finite = [float(value) for value in values
              if value is not None and np.isfinite(value)]
    return float(np.median(finite)) if finite else None


def _minimum(values: list[Any]) -> float | None:
    """Return the minimum of finite values."""
    finite = [float(value) for value in values
              if value is not None and np.isfinite(value)]
    return min(finite) if finite else None


def _maximum(values: list[Any]) -> float | None:
    """Return the maximum of finite values."""
    finite = [float(value) for value in values
              if value is not None and np.isfinite(value)]
    return max(finite) if finite else None


def _dataset_summary(reports: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate dataset-level characterization statistics."""
    rates = [item.get("estimated_fs") for item in reports]
    durations = [item.get("duration_s") for item in reports]
    awake_duration = sum(item.get("awake_duration_s", 0.0) or 0.0
                         for item in reports)
    drowsy_duration = sum(item.get("drowsy_duration_s", 0.0) or 0.0
                          for item in reports)
    labeled_duration = awake_duration + drowsy_duration
    summary = {
        "total_sessions": len(reports),
        "total_samples": sum(item.get("n_rows", 0) for item in reports),
        "total_recording_duration_s": sum(
            value for value in durations if value is not None
        ),
        "sessions_pass": sum(item["status"] == STATUS_PASS
                             for item in reports),
        "sessions_warning": sum(item["status"] == STATUS_WARNING
                                for item in reports),
        "sessions_fail": sum(item["status"] == STATUS_FAIL
                             for item in reports),
        "sampling_rate_min": _minimum(rates),
        "sampling_rate_max": _maximum(rates),
        "sampling_rate_median": _median(rates),
        "session_duration_min": _minimum(durations),
        "session_duration_max": _maximum(durations),
        "session_duration_median": _median(durations),
        "total_awake_duration_s": awake_duration,
        "total_drowsy_duration_s": drowsy_duration,
        "awake_percentage": (
            100.0 * awake_duration / labeled_duration
            if labeled_duration else 0.0
        ),
        "drowsy_percentage": (
            100.0 * drowsy_duration / labeled_duration
            if labeled_duration else 0.0
        ),
        "total_state_transitions": sum(
            item.get("n_transitions", 0) for item in reports
        ),
        "sessions_with_awake": sum(
            item.get("awake_samples", 0) > 0 for item in reports
        ),
        "sessions_with_drowsy": sum(
            item.get("drowsy_samples", 0) > 0 for item in reports
        ),
        "sessions_with_both_states": sum(
            item.get("awake_samples", 0) > 0
            and item.get("drowsy_samples", 0) > 0
            for item in reports
        ),
        "sessions_with_missing_values": sum(
            any(detail["null_count"] > 0
                for detail in item.get("missing_values", {}).values())
            for item in reports
        ),
        "sessions_with_time_gaps": sum(
            item.get("n_time_gaps", 0) > 0 for item in reports
        ),
        "sessions_with_invalid_labels": sum(
            bool(item.get("invalid_labels")) for item in reports
        ),
    }
    summary["total_recording_hours"] = (
        summary["total_recording_duration_s"] / 3600.0
    )
    for duration in WINDOW_DURATIONS:
        summary[f"sessions_paired_{duration}"] = sum(
            bool(item.get(f"paired_{duration}")) for item in reports
        )
    return summary


def _inventory_row(report: dict[str, Any]) -> dict[str, Any]:
    """Flatten one report for the one-row-per-session inventory."""
    row = {key: value for key, value in report.items()
           if key not in NESTED_FIELDS}
    for key in ("issues", "column_names", "missing_required_columns",
                "unexpected_columns", "empty_columns", "unique_labels",
                "invalid_labels"):
        if key in row:
            row[key] = json.dumps(_json_safe(row[key]), sort_keys=True)
    return row


def audit_dataset(
    dataset_dir: str | Path,
    output_dir: str | Path,
) -> DatasetAuditResult:
    """Audit every CSV while allowing individual files to fail."""
    dataset_path = Path(dataset_dir)
    output_path = Path(output_dir)
    if not dataset_path.is_dir():
        raise ValueError(f"Dataset directory does not exist: {dataset_path}")

    files = sorted(
        (path for path in dataset_path.iterdir()
         if path.is_file() and path.suffix.lower() == ".csv"),
        key=_natural_key,
    )
    sessions_path = output_path / "sessions"
    sessions_path.mkdir(parents=True, exist_ok=True)
    run_timestamp = datetime.now(timezone.utc).isoformat()
    LOGGER.info("Audit started at %s", run_timestamp)
    LOGGER.info("Dataset path: %s", dataset_path)
    LOGGER.info("CSV files discovered: %d", len(files))

    reports = []
    for index, csv_path in enumerate(files, start=1):
        session_id = f"session_{index:03d}"
        try:
            dataframe, _ = load_session(csv_path)
            report = audit_session(dataframe, session_id, csv_path.name)
        except Exception as exc:  # Batch processing must continue.
            LOGGER.exception("Failed to audit %s", csv_path.name)
            report = _failed_report(session_id, csv_path.name, exc)
        reports.append(report)
        _write_json(sessions_path / f"{session_id}.json", report)

    inventory = pd.DataFrame(_inventory_row(item) for item in reports)
    inventory_path = output_path / "dataset_inventory.csv"
    inventory.to_csv(inventory_path, index=False)
    summary = _dataset_summary(reports)
    summary_path = output_path / "dataset_summary.json"
    _write_json(summary_path, summary)

    LOGGER.info("Files processed: %d", len(reports))
    LOGGER.info(
        "Audit status counts: pass=%d warning=%d fail=%d",
        summary["sessions_pass"],
        summary["sessions_warning"],
        summary["sessions_fail"],
    )
    LOGGER.info("Inventory output: %s", inventory_path)
    LOGGER.info("Summary output: %s", summary_path)
    return DatasetAuditResult(
        inventory=inventory,
        summary=summary,
        session_reports=tuple(reports),
        output_paths={
            "inventory": inventory_path,
            "summary": summary_path,
            "sessions": sessions_path,
        },
    )
