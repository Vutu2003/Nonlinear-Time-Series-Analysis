"""Minimal CSV session loader without preprocessing or auditing."""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "Time (s)",
    "IR Value raw",
    "Label",
]


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