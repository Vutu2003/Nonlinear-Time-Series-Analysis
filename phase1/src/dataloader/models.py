"""Shared dataloader models."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

import pandas as pd


class SessionLoadError(RuntimeError):
    """Raised when a session CSV cannot be loaded."""


@dataclass(frozen=True)
class DatasetAuditResult:
    """Hold generated dataset audit results."""

    inventory: pd.DataFrame
    summary: dict[str, Any]
    session_reports: tuple[dict[str, Any], ...]
    output_paths: dict[str, Path]

    def __iter__(self) -> Iterator[Any]:
        """Support unpacking into inventory and summary."""
        yield self.inventory
        yield self.summary

    def __getitem__(self, key: str) -> Any:
        """Provide named access to result fields."""
        return getattr(self, key)
