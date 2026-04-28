"""File operations tracking."""

from typing import Any


class FileOpTracker:
    """Tracker for file operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def build_approval_preview(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _safe_read(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
