"""Rebuild the canonical segmented PPG dataset."""

import argparse
import logging
import re
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import pandas as pd


PHASE1_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PHASE1_ROOT / "src"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from dataloader.loader import (  # noqa: E402
    load_segmented_session,
    load_session,
)
from segmentation.segmentation import (  # noqa: E402
    segment_session,
    validate_quasi_stationarity,
)


WINDOW_SIZES = (60, 120, 180)
GAP_FACTOR = 1.5
SUBWINDOW_S = 10.0
STATIONARITY_THRESHOLD = 0.5
CANONICAL_COUNTS = {60: 951, 120: 432, 180: 254}
CANONICAL_RAW_PASS = 1398
CANONICAL_PROCESSED_PASS = 1544
INDEX_COLUMNS = (
    "session",
    "npz_file",
    "row_index",
    "window_id",
    "window_size_s",
    "label",
    "start_time",
    "end_time",
    "fs",
    "n_samples",
    "stationarity_score_raw",
    "stationarity_pass_raw",
    "stationarity_score_processed",
    "stationarity_pass_processed",
)
LOGGER = logging.getLogger(__name__)


def natural_file_key(path: Path) -> list[str | int]:
    """Return a natural numeric file-name key."""
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path.name)
    ]


def estimate_sampling_rate(time_s: np.ndarray) -> float:
    """Estimate sampling rate from positive time intervals."""
    if time_s.ndim != 1 or time_s.size < 2:
        raise ValueError("Time must contain at least two samples")
    if not np.isfinite(time_s).all():
        raise ValueError("Time must contain only finite values")

    intervals = np.diff(time_s)
    valid = intervals[np.isfinite(intervals) & (intervals > 0)]
    if valid.size == 0:
        raise ValueError("Time has no positive finite interval")
    return float(1.0 / np.median(valid))


def parse_sqi(values: pd.Series) -> np.ndarray:
    """Parse a boolean SQI artifact mask."""
    if pd.api.types.is_bool_dtype(values):
        return values.to_numpy(dtype=bool)
    if pd.api.types.is_numeric_dtype(values):
        numeric = values.to_numpy(dtype=float)
        if not np.isfinite(numeric).all() or not np.isin(
            numeric, (0.0, 1.0)
        ).all():
            raise ValueError("Numeric SQI values must be 0 or 1")
        return numeric.astype(bool)

    normalized = values.astype(str).str.strip().str.lower()
    mapping = {"true": True, "false": False, "1": True, "0": False}
    invalid = normalized[~normalized.isin(mapping)]
    if not invalid.empty:
        raise ValueError(f"Invalid SQI values: {invalid.unique().tolist()}")
    return normalized.map(mapping).to_numpy(dtype=bool)


def load_processed_arrays(
    csv_path: Path,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    """Load and validate arrays required by segmentation."""
    frame, _ = load_session(csv_path)
    required = {"PPG processed", "SQI"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing processed columns: {sorted(missing)}")

    time_s = pd.to_numeric(
        frame["Time (s)"], errors="raise"
    ).to_numpy(dtype=float)
    ppg_raw = pd.to_numeric(
        frame["IR Value raw"], errors="raise"
    ).to_numpy(dtype=float)
    ppg_processed = pd.to_numeric(
        frame["PPG processed"], errors="raise"
    ).to_numpy(dtype=float)
    label_values = pd.to_numeric(
        frame["Label"], errors="raise"
    ).to_numpy(dtype=float)
    if not np.isfinite(label_values).all():
        raise ValueError("Labels contain NaN or Inf")
    if not np.equal(label_values, np.round(label_values)).all():
        raise ValueError("Labels must be integer values")

    labels = label_values.astype(int)
    sqi_mask = parse_sqi(frame["SQI"])
    fs = estimate_sampling_rate(time_s)
    return time_s, ppg_raw, ppg_processed, labels, sqi_mask, fs


def empty_signal_array(n_samples: int) -> np.ndarray:
    """Return an empty two-dimensional signal array."""
    return np.empty((0, n_samples), dtype=float)


def build_session_payload(
    csv_path: Path,
) -> tuple[dict[str, np.ndarray], list[dict[str, object]]]:
    """Segment one session and build its archive payload."""
    arrays = load_processed_arrays(csv_path)
    time_s, ppg_raw, ppg_processed, labels, sqi_mask, fs = arrays
    segmented = segment_session(
        time_s=time_s,
        ppg_raw=ppg_raw,
        ppg_processed=ppg_processed,
        labels=labels,
        sqi_mask=sqi_mask,
        fs=fs,
        session_id=csv_path.name,
        window_sizes=WINDOW_SIZES,
        gap_factor=GAP_FACTOR,
    )

    payload = {"fs": np.array(fs, dtype=float)}
    index_rows = []
    for window_s in WINDOW_SIZES:
        windows = sorted(
            segmented[window_s], key=lambda item: item["window_id"]
        )
        n_samples = int(round(window_s * fs))
        if any(len(window["ppg_raw"]) != n_samples for window in windows):
            raise ValueError(f"Invalid sample count for {window_s} s")

        raw = (
            np.stack([window["ppg_raw"] for window in windows])
            if windows
            else empty_signal_array(n_samples)
        )
        processed = (
            np.stack([window["ppg_processed"] for window in windows])
            if windows
            else empty_signal_array(n_samples)
        )
        window_ids = np.array(
            [window["window_id"] for window in windows], dtype=int
        )
        window_labels = np.array(
            [window["label"] for window in windows], dtype=int
        )
        start_times = np.array(
            [window["start_time"] for window in windows], dtype=float
        )
        end_times = np.array(
            [window["end_time"] for window in windows], dtype=float
        )

        raw_results = [
            validate_quasi_stationarity(
                window,
                signal_key="ppg_raw",
                subwindow_s=SUBWINDOW_S,
                threshold=STATIONARITY_THRESHOLD,
            )
            for window in windows
        ]
        processed_results = [
            validate_quasi_stationarity(
                window,
                signal_key="ppg_processed",
                subwindow_s=SUBWINDOW_S,
                threshold=STATIONARITY_THRESHOLD,
            )
            for window in windows
        ]
        raw_scores = np.array(
            [result[0] for result in raw_results], dtype=float
        )
        raw_passes = np.array(
            [result[1] for result in raw_results], dtype=bool
        )
        processed_scores = np.array(
            [result[0] for result in processed_results], dtype=float
        )
        processed_passes = np.array(
            [result[1] for result in processed_results], dtype=bool
        )

        prefix = str(window_s)
        payload.update({
            f"{prefix}/raw": raw,
            f"{prefix}/processed": processed,
            f"{prefix}/window_id": window_ids,
            f"{prefix}/label": window_labels,
            f"{prefix}/start_time": start_times,
            f"{prefix}/end_time": end_times,
            f"{prefix}/stationarity_score_raw": raw_scores,
            f"{prefix}/stationarity_pass_raw": raw_passes,
            f"{prefix}/stationarity_score_processed": processed_scores,
            f"{prefix}/stationarity_pass_processed": processed_passes,
        })

        for row_index, window in enumerate(windows):
            index_rows.append({
                "session": csv_path.name,
                "npz_file": f"{csv_path.stem}.npz",
                "row_index": row_index,
                "window_id": window["window_id"],
                "window_size_s": window_s,
                "label": window["label"],
                "start_time": window["start_time"],
                "end_time": window["end_time"],
                "fs": fs,
                "n_samples": n_samples,
                "stationarity_score_raw": raw_scores[row_index],
                "stationarity_pass_raw": raw_passes[row_index],
                "stationarity_score_processed": (
                    processed_scores[row_index]
                ),
                "stationarity_pass_processed": (
                    processed_passes[row_index]
                ),
            })

    return payload, index_rows


def validate_dataset(
    data_dir: Path,
    expected_sessions: set[str],
    enforce_canonical: bool,
) -> pd.DataFrame:
    """Validate the complete segmented export."""
    index = pd.read_csv(data_dir / "segments_index.csv")
    if tuple(index.columns) != INDEX_COLUMNS:
        raise ValueError("segments_index.csv has an invalid schema")

    archive_names = {path.name for path in data_dir.glob("*.npz")}
    expected_archives = {
        f"{Path(session).stem}.npz" for session in expected_sessions
    }
    if archive_names != expected_archives:
        raise ValueError("Exported NPZ session set is inconsistent")
    if set(index["session"].unique()) != expected_sessions:
        raise ValueError("Index session set is inconsistent")
    if index.duplicated(
        ["session", "window_size_s", "window_id"]
    ).any():
        raise ValueError("Index contains duplicate window identifiers")

    metadata_tables = []
    for session in sorted(expected_sessions):
        batches, metadata = load_segmented_session(
            session,
            data_dir=data_dir,
            window_sizes=WINDOW_SIZES,
            representation="both",
            stationarity_only=False,
        )
        metadata_tables.append(metadata)
        for window_s, batch in batches.items():
            rows = metadata[
                metadata["window_size_s"] == window_s
            ].sort_values("row_index")
            count = len(rows)
            n_samples = int(round(window_s * batch["fs"]))
            if batch["raw"].shape != (count, n_samples):
                raise ValueError(f"Raw shape mismatch: {session}")
            if batch["processed"].shape != batch["raw"].shape:
                raise ValueError(f"Raw/processed mismatch: {session}")
            if not np.isfinite(batch["raw"]).all():
                raise ValueError(f"Non-finite Raw PPG: {session}")
            if not np.isfinite(batch["processed"]).all():
                raise ValueError(f"Non-finite Processed PPG: {session}")

            comparisons = {
                "row_index": rows["row_index"].to_numpy(dtype=int),
                "window_id": rows["window_id"].to_numpy(dtype=int),
                "label": rows["label"].to_numpy(dtype=int),
                "start_time": rows["start_time"].to_numpy(dtype=float),
                "end_time": rows["end_time"].to_numpy(dtype=float),
                "stationarity_score_raw": rows[
                    "stationarity_score_raw"
                ].to_numpy(dtype=float),
                "stationarity_pass_raw": rows[
                    "stationarity_pass_raw"
                ].to_numpy(dtype=bool),
                "stationarity_score_processed": rows[
                    "stationarity_score_processed"
                ].to_numpy(dtype=float),
                "stationarity_pass_processed": rows[
                    "stationarity_pass_processed"
                ].to_numpy(dtype=bool),
            }
            for field, expected in comparisons.items():
                if not np.allclose(batch[field], expected):
                    raise ValueError(
                        f"NPZ/index mismatch for {field}: {session}"
                    )

            if not np.all(rows["n_samples"].to_numpy() == n_samples):
                raise ValueError(f"Invalid n_samples: {session}")
            if not np.allclose(rows["fs"], batch["fs"]):
                raise ValueError(f"Index fs mismatch: {session}")

    metadata = pd.concat(metadata_tables, ignore_index=True)
    if len(metadata) != len(index):
        raise ValueError("NPZ and index window counts differ")

    counts = {
        size: int((metadata["window_size_s"] == size).sum())
        for size in WINDOW_SIZES
    }
    raw_pass = int(metadata["stationarity_pass_raw"].sum())
    processed_pass = int(metadata["stationarity_pass_processed"].sum())
    if enforce_canonical:
        if counts != CANONICAL_COUNTS:
            raise ValueError(f"Non-canonical window counts: {counts}")
        if raw_pass != CANONICAL_RAW_PASS:
            raise ValueError(f"Non-canonical Raw pass count: {raw_pass}")
        if processed_pass != CANONICAL_PROCESSED_PASS:
            raise ValueError(
                f"Non-canonical Processed pass count: {processed_pass}"
            )

    return pd.DataFrame({
        "window_size_s": WINDOW_SIZES,
        "windows": [counts[size] for size in WINDOW_SIZES],
    })


def run_pipeline(
    input_dir: Path,
    output_dir: Path,
    enforce_canonical: bool = True,
) -> pd.DataFrame:
    """Run segmentation and export the canonical dataset."""
    csv_paths = sorted(input_dir.glob("*.csv"), key=natural_file_key)
    if not csv_paths:
        raise FileNotFoundError(f"No CSV files found in {input_dir}")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_sessions = {path.name for path in csv_paths}
    expected_archives = {
        f"{path.stem}.npz" for path in csv_paths
    }
    existing_archives = {path.name for path in output_dir.glob("*.npz")}
    unexpected = sorted(existing_archives - expected_archives)
    if unexpected:
        raise ValueError(
            f"Output directory contains unexpected NPZ files: {unexpected}"
        )

    all_rows = []
    failures = []
    with TemporaryDirectory(
        prefix="segmentation-",
        dir=output_dir.parent,
    ) as temporary_dir:
        staging_dir = Path(temporary_dir)
        for csv_path in csv_paths:
            try:
                payload, rows = build_session_payload(csv_path)
                archive_path = staging_dir / f"{csv_path.stem}.npz"
                np.savez_compressed(archive_path, **payload)
                all_rows.extend(rows)
                counts = {
                    size: sum(
                        row["window_size_s"] == size for row in rows
                    )
                    for size in WINDOW_SIZES
                }
                LOGGER.info("%s: windows=%s", csv_path.name, counts)
            except (KeyError, OSError, TypeError, ValueError) as exc:
                failures.append((csv_path.name, str(exc)))
                LOGGER.error("%s: %s", csv_path.name, exc)

        if failures:
            LOGGER.info(
                "Completed: success=%d, failed=%d",
                len(csv_paths) - len(failures),
                len(failures),
            )
            raise RuntimeError(
                f"Segmentation failed for {len(failures)} session(s)"
            )

        index = pd.DataFrame(all_rows, columns=INDEX_COLUMNS)
        index = index.sort_values(
            ["session", "window_size_s", "window_id"]
        ).reset_index(drop=True)
        index.to_csv(staging_dir / "segments_index.csv", index=False)
        summary = validate_dataset(
            staging_dir,
            expected_sessions,
            enforce_canonical,
        )

        for archive_name in expected_archives:
            (staging_dir / archive_name).replace(output_dir / archive_name)
        (staging_dir / "segments_index.csv").replace(
            output_dir / "segments_index.csv"
        )

    validate_dataset(output_dir, expected_sessions, enforce_canonical)
    LOGGER.info(
        "Completed: success=%d, failed=0, windows=%d",
        len(expected_sessions),
        int(summary["windows"].sum()),
    )
    LOGGER.info(
        "Stationarity pass: Raw=%d, Processed=%d",
        int(index["stationarity_pass_raw"].sum()),
        int(index["stationarity_pass_processed"].sum()),
    )
    return summary


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Rebuild segmented PPG session archives."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=PHASE1_ROOT / "data_processed" / "dhdata",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PHASE1_ROOT / "segmentated_data" / "dhdata",
    )
    parser.add_argument(
        "--skip-canonical-counts",
        action="store_true",
        help="Validate structure without enforcing dhdata counts.",
    )
    return parser.parse_args()


def main() -> int:
    """Run the command-line pipeline."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )
    args = parse_args()
    try:
        run_pipeline(
            args.input_dir.resolve(),
            args.output_dir.resolve(),
            enforce_canonical=not args.skip_canonical_counts,
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        LOGGER.error("Pipeline stopped: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
