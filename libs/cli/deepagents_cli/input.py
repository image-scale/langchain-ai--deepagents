"""Input handling module."""

from typing import Any

INPUT_HIGHLIGHT_PATTERN = r"@\w+"


class MediaTracker:
    """Tracker for media files."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def extract_leading_pasted_file_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def normalize_pasted_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def parse_file_mentions(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def parse_pasted_file_paths(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def parse_pasted_path_payload(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def parse_single_pasted_file_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
