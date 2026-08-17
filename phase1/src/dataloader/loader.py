"""CSV session loading without preprocessing."""

from pathlib import Path
from typing import Any

import pandas as pd

from .models import SessionLoadError


def _normalize_columns(columns: pd.Index) -> list[Any]:
    """Trim surrounding whitespace from text column names."""
    return [column.strip() if isinstance(column, str) else column
            for column in columns]


def load_session(path: str | Path) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Load one CSV and return unchanged values with file metadata."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise SessionLoadError(f"File does not exist: {csv_path}")
    if not csv_path.is_file():
        raise SessionLoadError(f"Path is not a file: {csv_path}")

    try:
        dataframe = pd.read_csv(csv_path)
    except (OSError, UnicodeError, pd.errors.ParserError,
            pd.errors.EmptyDataError) as exc:
        message = f"Cannot read CSV '{csv_path.name}': {exc}"
        raise SessionLoadError(message) from exc

    normalized_columns = _normalize_columns(dataframe.columns)
    if len(normalized_columns) != len(set(normalized_columns)):
        raise SessionLoadError(
            f"Duplicate columns after normalization: {csv_path.name}"
        )
    dataframe.columns = normalized_columns

    metadata = {
        "file_name": csv_path.name,
        "file_path": str(csv_path),
        "file_size_bytes": csv_path.stat().st_size,
    }
    return dataframe, metadata
