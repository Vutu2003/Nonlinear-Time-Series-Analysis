"""Load source sessions and exported segmented windows."""

from collections.abc import Sequence
from pathlib import Path

import numpy as np
import pandas as pd


REQUIRED_COLUMNS = [
    "Time (s)",
    "IR Value raw",
    "Label",
]

PRIMARY_WINDOW_SIZES = (60, 120, 180)
SEGMENTED_INDEX_COLUMNS = [
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
]
LABEL_CODES = {
    "awake": 0,
    "drowsy": 1,
    "drowsiness": 1,
}


# Reproducibility use:
# Load a session CSV before analysis-specific filtering or window selection.
# Signal values and row order are preserved; only column names are stripped.
#
# Example:
# data, metadata = load_session("phase1/dataset/dhdata/sample_5.csv")
# time_s = data["Time (s)"].to_numpy()
# ppg_raw = data["IR Value raw"].to_numpy()
# labels = data["Label"].to_numpy()
#
# Use this loader to reproduce preprocessing, SQI, or segmentation. Record
# metadata["file_path"] and all analysis parameters with the results.

def load_session(path: str | Path) -> tuple[pd.DataFrame, dict]:
    """
    Load one PPG session CSV without modifying signal values.

    Parameters
    ----------
    path : str | Path
        Path to the session CSV file.

    Returns
    -------
    dataframe : pd.DataFrame
        Original CSV data with column names stripped of surrounding spaces.

    metadata : dict
        Minimal file metadata.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.

    ValueError
        If the path is not a file, the CSV cannot be read,
        required columns are missing, or duplicate columns exist.
    """
    csv_path = Path(path)

    # 1. Basic path validation
    if not csv_path.exists():
        raise FileNotFoundError(f"File does not exist: {csv_path}")

    if not csv_path.is_file():
        raise ValueError(f"Path is not a file: {csv_path}")

    # 2. Read CSV
    try:
        dataframe = pd.read_csv(csv_path)
    except (
        OSError,
        UnicodeError,
        pd.errors.ParserError,
        pd.errors.EmptyDataError,
    ) as exc:
        raise ValueError(
            f"Cannot read CSV '{csv_path.name}': {exc}"
        ) from exc

    # 3. Normalize column names only
    dataframe.columns = [
        column.strip() if isinstance(column, str) else column
        for column in dataframe.columns
    ]

    # 4. Check duplicated column names
    if dataframe.columns.duplicated().any():
        duplicates = dataframe.columns[
            dataframe.columns.duplicated()
        ].tolist()

        raise ValueError(
            f"Duplicate columns in '{csv_path.name}': {duplicates}"
        )

    # 5. Check required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns in '{csv_path.name}': "
            f"{missing_columns}"
        )

    # 6. Minimal metadata
    metadata = {
        "file_name": csv_path.name,
        "file_path": str(csv_path.resolve()),
        "file_size_bytes": csv_path.stat().st_size,
        "n_rows": len(dataframe),
        "n_columns": len(dataframe.columns),
    }

    return dataframe, metadata


def _default_segmented_data_dir() -> Path:
    """Return the default exported dataset directory."""
    return Path(__file__).resolve().parents[2] / "segmentated_data" / "dhdata"


def _normalize_window_sizes(
    window_sizes: int | Sequence[int] | None,
) -> tuple[int, ...]:
    """Validate requested analysis-window sizes."""
    if window_sizes is None:
        return PRIMARY_WINDOW_SIZES

    if isinstance(window_sizes, (int, np.integer)) and not isinstance(
        window_sizes, (bool, np.bool_)
    ):
        values = [int(window_sizes)]
    else:
        try:
            values = list(window_sizes)
        except TypeError as exc:
            raise TypeError(
                "window_sizes must be an integer, a sequence, or None"
            ) from exc

    if not values:
        raise ValueError("window_sizes cannot be empty")

    normalized = []
    for value in values:
        if isinstance(value, (bool, np.bool_)) or not isinstance(
            value, (int, np.integer)
        ):
            raise TypeError("Every window size must be an integer")
        size = int(value)
        if size not in PRIMARY_WINDOW_SIZES:
            raise ValueError(
                f"Unsupported window size {size}; "
                f"choose from {PRIMARY_WINDOW_SIZES}"
            )
        if size not in normalized:
            normalized.append(size)

    return tuple(normalized)


def _normalize_labels(
    labels: int | str | Sequence[int | str] | None,
) -> tuple[int, ...] | None:
    """Convert label names or codes to integer codes."""
    if labels is None:
        return None

    if isinstance(labels, (str, int, np.integer)) and not isinstance(
        labels, (bool, np.bool_)
    ):
        values = [labels]
    else:
        try:
            values = list(labels)
        except TypeError as exc:
            raise TypeError(
                "labels must be a code, a name, a sequence, or None"
            ) from exc

    if not values:
        raise ValueError("labels cannot be empty")

    normalized = []
    for value in values:
        if isinstance(value, str):
            key = value.strip().lower()
            if key not in LABEL_CODES:
                raise ValueError(f"Unsupported label: {value}")
            code = LABEL_CODES[key]
        elif isinstance(value, (int, np.integer)) and not isinstance(
            value, (bool, np.bool_)
        ):
            code = int(value)
            if code not in (0, 1):
                raise ValueError(f"Unsupported label code: {code}")
        else:
            raise TypeError("Every label must be an integer code or a name")

        if code not in normalized:
            normalized.append(code)

    return tuple(normalized)


def _read_segmented_index(index_path: Path) -> pd.DataFrame:
    """Read and validate the global segmented-window index."""
    try:
        index = pd.read_csv(index_path)
    except (
        OSError,
        UnicodeError,
        pd.errors.ParserError,
        pd.errors.EmptyDataError,
    ) as exc:
        raise ValueError(f"Cannot read segmented index: {exc}") from exc

    if index.columns.duplicated().any():
        raise ValueError("Segmented index contains duplicate columns")

    missing = [
        column for column in SEGMENTED_INDEX_COLUMNS
        if column not in index.columns
    ]
    if missing:
        raise ValueError(f"Segmented index is missing columns: {missing}")

    for column in (
        "stationarity_pass_raw",
        "stationarity_pass_processed",
    ):
        if pd.api.types.is_bool_dtype(index[column]):
            continue
        normalized = index[column].astype(str).str.strip().str.lower()
        mapping = {"true": True, "false": False, "1": True, "0": False}
        invalid = normalized[~normalized.isin(mapping)]
        if not invalid.empty:
            raise ValueError(
                f"Invalid boolean values in '{column}': "
                f"{invalid.unique().tolist()}"
            )
        index[column] = normalized.map(mapping).astype(bool)

    return index


# Reproducibility use:
# Load aligned exported windows for NTSA and statistical comparisons. Defaults
# select Processed PPG windows that passed processed-signal stationarity.
#
# Example:
# windows, metadata = load_segmented_session(
#     "sample_5.csv",
#     window_sizes=60,
#     representation="processed",
#     labels="awake",
# )
# signal = windows[60]["signal"]
# labels = windows[60]["label"]
#
# For matched Raw/Processed analysis, set representation="both" and
# stationarity_only=False, then filter with each representation's pass flag.
# Use metadata["array_index"] for returned arrays and metadata["row_index"]
# for the original .npz row; these indices are not interchangeable. Preserve
# metadata and metadata.attrs so the selected cohort can be reconstructed.

def load_segmented_session(
    session: str,
    data_dir: str | Path | None = None,
    window_sizes: int | Sequence[int] | None = None,
    representation: str = "processed",
    labels: int | str | Sequence[int | str] | None = None,
    stationarity_only: bool = True,
) -> tuple[dict[int, dict[str, object]], pd.DataFrame]:
    """Load aligned segmented windows for one session."""
    if not isinstance(session, str) or not session.strip():
        raise TypeError("session must be a non-empty string")

    if not isinstance(representation, str):
        raise TypeError("representation must be a string")
    representation = representation.strip().lower()
    if representation not in {"raw", "processed", "both"}:
        raise ValueError(
            "representation must be 'raw', 'processed', or 'both'"
        )

    if not isinstance(stationarity_only, (bool, np.bool_)):
        raise TypeError("stationarity_only must be boolean")
    if representation == "both" and stationarity_only:
        raise ValueError(
            "Use stationarity_only=False with representation='both'; "
            "filter each representation with its own pass flag"
        )

    selected_sizes = _normalize_window_sizes(window_sizes)
    selected_labels = _normalize_labels(labels)
    dataset_dir = (
        _default_segmented_data_dir()
        if data_dir is None
        else Path(data_dir)
    )
    if not dataset_dir.exists():
        raise FileNotFoundError(
            f"Segmented dataset directory does not exist: {dataset_dir}"
        )
    if not dataset_dir.is_dir():
        raise ValueError(
            f"Segmented dataset path is not a directory: {dataset_dir}"
        )

    session_stem = Path(session.strip()).stem
    archive_path = dataset_dir / f"{session_stem}.npz"
    index_path = dataset_dir / "segments_index.csv"
    if not archive_path.is_file():
        raise FileNotFoundError(
            f"Session archive does not exist: {archive_path}"
        )
    if not index_path.is_file():
        raise FileNotFoundError(
            f"Segmented index does not exist: {index_path}"
        )

    index = _read_segmented_index(index_path)
    session_rows = index[index["npz_file"] == archive_path.name].copy()
    if session_rows.empty:
        raise ValueError(
            f"Session archive is absent from the index: {archive_path.name}"
        )

    results = {}
    metadata_chunks = []
    try:
        with np.load(archive_path, allow_pickle=False) as archive:
            fs = float(archive["fs"])
            if not np.isfinite(fs) or fs <= 0:
                raise ValueError(
                    f"Invalid sampling rate in {archive_path.name}"
                )

            for window_size in selected_sizes:
                prefix = str(window_size)
                required_keys = {
                    f"{prefix}/raw",
                    f"{prefix}/processed",
                    f"{prefix}/window_id",
                    f"{prefix}/label",
                    f"{prefix}/start_time",
                    f"{prefix}/end_time",
                    f"{prefix}/stationarity_score_raw",
                    f"{prefix}/stationarity_pass_raw",
                    f"{prefix}/stationarity_score_processed",
                    f"{prefix}/stationarity_pass_processed",
                }
                missing_keys = required_keys.difference(archive.files)
                if missing_keys:
                    raise ValueError(
                        f"{archive_path.name} is missing keys: "
                        f"{sorted(missing_keys)}"
                    )

                raw = archive[f"{prefix}/raw"]
                processed = archive[f"{prefix}/processed"]
                if raw.ndim != 2 or raw.shape != processed.shape:
                    raise ValueError(
                        f"Raw/processed shape mismatch for {window_size} s"
                    )

                size_rows = session_rows[
                    session_rows["window_size_s"] == window_size
                ].sort_values("row_index")
                if len(size_rows) != raw.shape[0]:
                    raise ValueError(
                        f"Index length mismatch for {window_size} s"
                    )

                archive_ids = archive[f"{prefix}/window_id"]
                if not np.array_equal(
                    archive_ids,
                    size_rows["window_id"].to_numpy(dtype=int),
                ):
                    raise ValueError(
                        f"Window IDs do not match for {window_size} s"
                    )

                selected = size_rows
                if selected_labels is not None:
                    selected = selected[
                        selected["label"].isin(selected_labels)
                    ]
                if stationarity_only:
                    pass_column = f"stationarity_pass_{representation}"
                    selected = selected[selected[pass_column]]
                selected = selected.sort_values("row_index").copy()
                row_indices = selected["row_index"].to_numpy(dtype=int)

                batch = {
                    "representation": representation,
                    "fs": fs,
                    "n_samples": int(raw.shape[1]),
                    "row_index": row_indices.copy(),
                    "window_id": archive_ids[row_indices].copy(),
                    "label": archive[f"{prefix}/label"][row_indices].copy(),
                    "start_time": archive[
                        f"{prefix}/start_time"
                    ][row_indices].copy(),
                    "end_time": archive[
                        f"{prefix}/end_time"
                    ][row_indices].copy(),
                }

                if representation == "both":
                    batch.update({
                        "raw": raw[row_indices].copy(),
                        "processed": processed[row_indices].copy(),
                        "stationarity_score_raw": archive[
                            f"{prefix}/stationarity_score_raw"
                        ][row_indices].copy(),
                        "stationarity_pass_raw": archive[
                            f"{prefix}/stationarity_pass_raw"
                        ][row_indices].copy(),
                        "stationarity_score_processed": archive[
                            f"{prefix}/stationarity_score_processed"
                        ][row_indices].copy(),
                        "stationarity_pass_processed": archive[
                            f"{prefix}/stationarity_pass_processed"
                        ][row_indices].copy(),
                    })
                else:
                    signal = raw if representation == "raw" else processed
                    batch.update({
                        "signal": signal[row_indices].copy(),
                        "stationarity_score": archive[
                            f"{prefix}/stationarity_score_{representation}"
                        ][row_indices].copy(),
                        "stationarity_pass": archive[
                            f"{prefix}/stationarity_pass_{representation}"
                        ][row_indices].copy(),
                    })

                selected["array_index"] = np.arange(len(selected), dtype=int)
                selected["representation"] = representation
                metadata_chunks.append(selected)
                results[window_size] = batch
    except (OSError, KeyError, ValueError) as exc:
        if isinstance(exc, ValueError) and str(exc).startswith((
            "Invalid sampling rate",
            "Raw/processed shape mismatch",
            "Index length mismatch",
            "Window IDs do not match",
        )):
            raise
        raise ValueError(
            f"Cannot load segmented session '{archive_path.name}': {exc}"
        ) from exc

    metadata = pd.concat(metadata_chunks, ignore_index=True)
    metadata.attrs = {
        "session": session_rows["session"].iat[0],
        "archive_path": str(archive_path.resolve()),
        "index_path": str(index_path.resolve()),
        "fs": fs,
        "representation": representation,
        "stationarity_only": bool(stationarity_only),
    }

    return results, metadata


# Load analysis-ready windows with a simple interface.
#
# Example:
# data_awake, data_drowsy = get_data("sample_1.csv")
# awake_60 = data_awake[60]
#
# Each state is keyed by window size. Every batch contains aligned
# ``raw``, ``processed``, and ``time`` arrays with shape
# (n_windows, n_samples). Exported windows have already passed SQI.
# ``stationarity`` selects a pass flag or disables stationarity filtering.

def get_data(
    session: str,
    data_dir: str | Path | None = None,
    window_sizes: int | Sequence[int] | None = None,
    stationarity: str = "processed",
) -> tuple[
    dict[int, dict[str, object]],
    dict[int, dict[str, object]],
]:
    """Return stationary Awake and Drowsy window batches."""
    if not isinstance(stationarity, str):
        raise TypeError("stationarity must be a string")

    stationarity = stationarity.strip().lower()
    if stationarity not in {"raw", "processed", "both", "none"}:
        raise ValueError(
            "stationarity must be 'raw', 'processed', 'both', or 'none'"
        )

    # Exported segmented windows have already passed SQI.
    batches, _ = load_segmented_session(
        session,
        data_dir=data_dir,
        window_sizes=window_sizes,
        representation="both",
        stationarity_only=False,
    )
    state_data = {0: {}, 1: {}}

    for window_size, batch in batches.items():
        if stationarity == "none":
            stationary = np.ones(len(batch["label"]), dtype=bool)
        elif stationarity == "both":
            stationary = (
                batch["stationarity_pass_raw"]
                & batch["stationarity_pass_processed"]
            )
        else:
            stationary = batch[f"stationarity_pass_{stationarity}"]

        sample_offsets = np.arange(
            batch["n_samples"],
            dtype=float,
        ) / batch["fs"]

        for label in state_data:
            selected = stationary & (batch["label"] == label)
            start_time = batch["start_time"][selected].copy()
            time = start_time[:, None] + sample_offsets

            state_data[label][window_size] = {
                "raw": batch["raw"][selected].copy(),
                "processed": batch["processed"][selected].copy(),
                "time": time,
                "window_id": batch["window_id"][selected].copy(),
                "start_time": start_time,
                "end_time": batch["end_time"][selected].copy(),
                "fs": batch["fs"],
                "n_samples": batch["n_samples"],
            }

    return state_data[0], state_data[1]
