"""Protocol definitions for backends."""

from typing import Any, Protocol, TypedDict, runtime_checkable
from typing_extensions import TypeAlias


class EditResult(TypedDict, total=False):
    """Result from an edit operation."""
    success: bool
    error: str
    path: str


class ExecuteResponse(TypedDict, total=False):
    """Response from an execute operation."""
    output: str
    exit_code: int
    error: str


class FileDownloadResponse(TypedDict, total=False):
    """Response from a file download operation."""
    content: str
    path: str
    error: str


class FileUploadResponse(TypedDict, total=False):
    """Response from a file upload operation."""
    success: bool
    path: str
    error: str


class GlobResult(TypedDict, total=False):
    """Result from a glob operation."""
    matches: list[str]
    error: str


class GrepResult(TypedDict, total=False):
    """Result from a grep operation."""
    matches: list[dict[str, Any]]
    error: str


class LsResult(TypedDict, total=False):
    """Result from an ls operation."""
    entries: list[dict[str, Any]]
    error: str


class ReadResult(TypedDict, total=False):
    """Result from a read operation."""
    content: str
    path: str
    error: str
    line_count: int


class WriteResult(TypedDict, total=False):
    """Result from a write operation."""
    success: bool
    path: str
    error: str


@runtime_checkable
class BackendProtocol(Protocol):
    """Protocol for file system backends."""

    def read(self, path: str, **kwargs: Any) -> ReadResult:
        ...

    def write(self, path: str, content: str, **kwargs: Any) -> WriteResult:
        ...

    def edit(self, path: str, old_string: str, new_string: str, **kwargs: Any) -> EditResult:
        ...

    def ls(self, path: str, **kwargs: Any) -> LsResult:
        ...

    def glob(self, pattern: str, **kwargs: Any) -> GlobResult:
        ...

    def grep(self, pattern: str, **kwargs: Any) -> GrepResult:
        ...


@runtime_checkable
class SandboxBackendProtocol(BackendProtocol, Protocol):
    """Protocol for sandbox backends with execution support."""

    def execute(self, command: str, **kwargs: Any) -> ExecuteResponse:
        ...


def execute_accepts_timeout(backend: Any) -> bool:
    """Check if a backend's execute method accepts a timeout parameter."""
    raise NotImplementedError
