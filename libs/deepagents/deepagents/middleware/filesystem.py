"""Filesystem middleware implementation."""

from typing import Any, TypedDict


EMPTY_CONTENT_WARNING = "Warning: File has empty content"
WRITE_FILE_TOOL_DESCRIPTION = "Write content to a file at the specified path"
NUM_CHARS_PER_TOKEN = 4


class FileData(TypedDict, total=False):
    """File data structure."""
    content: str
    encoding: str
    line_count: int
    file_type: str


class FilesystemState(TypedDict, total=False):
    """State for filesystem middleware."""
    files: dict[str, FileData]


def _build_evicted_content(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _create_content_preview(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _extract_text_from_message(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _supports_execution(backend: Any) -> bool:
    """Check if backend supports execution."""
    raise NotImplementedError


class FilesystemMiddleware:
    """Middleware for file system operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError
