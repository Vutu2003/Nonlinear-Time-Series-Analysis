"""Rebuild processed PPG sessions from the raw dataset."""

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

from dataloader.loader import load_session  # noqa: E402
from preprocessing.filter import preprocess_ppg  # noqa: E402
from preprocessing.sqi import detect_motion_artifacts  # noqa: E402


LOWCUT_HZ = 0.5
HIGHCUT_HZ = 8.0
FILTER_ORDER = 2
SQI_WINDOW_S = 5.0
SQI_THRESHOLD = 4.5
OUTPUT_COLUMNS = (
    "Time (s)",
    "IR Value raw",
    "PPG processed",
    "Label",
    "SQI",
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


def count_invalid_windows(
    mask: np.ndarray,
    fs: float,
    window_s: float,
) -> int:
    """Count complete SQI windows marked invalid."""
    window_samples = max(2, int(round(window_s * fs)))
    starts = range(0, len(mask) - window_samples + 1, window_samples)
    return sum(
        bool(mask[start:start + window_samples].any())
        for start in starts
    )


def validate_processed_frame(
    source: pd.DataFrame,
    output: pd.DataFrame,
) -> None:
    """Validate one processed session before export."""
    if tuple(output.columns) != OUTPUT_COLUMNS:
        raise ValueError("Processed output has an invalid column schema")
    if len(output) != len(source):
        raise ValueError("Preprocessing changed the sample count")
    if output["SQI"].dtype != bool:
        raise TypeError("SQI must have boolean dtype")

    aligned_columns = ("Time (s)", "IR Value raw", "Label")
    for column in aligned_columns:
        if not output[column].equals(source[column]):
            raise ValueError(f"Preprocessing changed '{column}'")

    processed = output["PPG processed"].to_numpy(dtype=float)
    if not np.isfinite(processed).all():
        raise ValueError("Processed PPG contains NaN or Inf")


def process_session(source_path: Path, staging_dir: Path) -> dict[str, object]:
    """Process and stage one raw session."""
    frame, metadata = load_session(source_path)
    time_s = pd.to_numeric(
        frame["Time (s)"], errors="raise"
    ).to_numpy(dtype=float)
    ppg_raw = pd.to_numeric(
        frame["IR Value raw"], errors="raise"
    ).to_numpy(dtype=float)
    labels = pd.to_numeric(frame["Label"], errors="raise").to_numpy(
        dtype=float
    )
    if not np.isfinite(ppg_raw).all():
        raise ValueError("Raw PPG contains NaN or Inf")
    if not np.isfinite(labels).all():
        raise ValueError("Labels contain NaN or Inf")

    fs = estimate_sampling_rate(time_s)
    _, processed = preprocess_ppg(
        ppg_raw,
        fs,
        lowcut=LOWCUT_HZ,
        highcut=HIGHCUT_HZ,
        order=FILTER_ORDER,
    )
    sqi_mask = detect_motion_artifacts(
        processed,
        fs,
        window_s=SQI_WINDOW_S,
        threshold=SQI_THRESHOLD,
    )
    if sqi_mask.shape != ppg_raw.shape:
        raise ValueError("SQI mask length does not match the signal")
    if sqi_mask.dtype != np.bool_:
        raise TypeError("SQI mask must have boolean dtype")

    output = pd.DataFrame({
        "Time (s)": frame["Time (s)"].copy(),
        "IR Value raw": frame["IR Value raw"].copy(),
        "PPG processed": processed,
        "Label": frame["Label"].copy(),
        "SQI": sqi_mask,
    })
    validate_processed_frame(frame, output)

    staged_path = staging_dir / source_path.name
    output.to_csv(staged_path, index=False)
    reloaded = pd.read_csv(staged_path)
    if len(reloaded) != len(output):
        raise ValueError("Exported CSV changed the sample count")
    if tuple(reloaded.columns) != OUTPUT_COLUMNS:
        raise ValueError("Exported CSV changed the column schema")

    return {
        "session": metadata["file_name"],
        "fs": fs,
        "n_samples": len(output),
        "invalid_samples": int(sqi_mask.sum()),
        "invalid_windows": count_invalid_windows(
            sqi_mask, fs, SQI_WINDOW_S
        ),
    }


def run_pipeline(input_dir: Path, output_dir: Path) -> list[dict[str, object]]:
    """Run preprocessing for every raw session."""
    csv_paths = sorted(input_dir.glob("*.csv"), key=natural_file_key)
    if not csv_paths:
        raise FileNotFoundError(f"No CSV files found in {input_dir}")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    expected_names = {path.name for path in csv_paths}
    existing_names = {path.name for path in output_dir.glob("*.csv")}
    unexpected = sorted(existing_names - expected_names)
    if unexpected:
        raise ValueError(
            f"Output directory contains unexpected CSV files: {unexpected}"
        )

    summaries = []
    failures = []
    with TemporaryDirectory(
        prefix="preprocessing-",
        dir=output_dir.parent,
    ) as temporary_dir:
        staging_dir = Path(temporary_dir)
        for source_path in csv_paths:
            try:
                summary = process_session(source_path, staging_dir)
                summaries.append(summary)
                LOGGER.info(
                    "%s: fs=%.3f Hz, invalid samples=%d, windows=%d",
                    summary["session"],
                    summary["fs"],
                    summary["invalid_samples"],
                    summary["invalid_windows"],
                )
            except (OSError, TypeError, ValueError) as exc:
                failures.append((source_path.name, str(exc)))
                LOGGER.error("%s: %s", source_path.name, exc)

        if failures:
            LOGGER.info(
                "Completed: success=%d, failed=%d",
                len(summaries),
                len(failures),
            )
            raise RuntimeError(
                f"Preprocessing failed for {len(failures)} session(s)"
            )

        for source_path in csv_paths:
            staged_path = staging_dir / source_path.name
            staged_path.replace(output_dir / source_path.name)

    exported_names = {path.name for path in output_dir.glob("*.csv")}
    if exported_names != expected_names:
        raise ValueError("Exported session set does not match the raw dataset")

    LOGGER.info(
        "Completed: success=%d, failed=0, invalid samples=%d, "
        "invalid windows=%d",
        len(summaries),
        sum(int(row["invalid_samples"]) for row in summaries),
        sum(int(row["invalid_windows"]) for row in summaries),
    )
    return summaries


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Rebuild processed PPG sessions."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=PHASE1_ROOT / "dataset" / "dhdata",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PHASE1_ROOT / "data_processed" / "dhdata",
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
        run_pipeline(args.input_dir.resolve(), args.output_dir.resolve())
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        LOGGER.error("Pipeline stopped: %s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
