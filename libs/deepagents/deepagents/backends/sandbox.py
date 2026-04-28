"""Sandbox backend implementation."""

from typing import Any
from deepagents.backends.protocol import (
    EditResult,
    ExecuteResponse,
    FileDownloadResponse,
    FileUploadResponse,
    GlobResult,
    GrepResult,
    LsResult,
    ReadResult,
    WriteResult,
)


_EDIT_COMMAND_TEMPLATE = "edit {path}"
_EDIT_INLINE_MAX_BYTES = 4096
_EDIT_TMPFILE_TEMPLATE = "edit_tmpfile_{}"
_GLOB_COMMAND_TEMPLATE = "glob {pattern}"
_READ_COMMAND_TEMPLATE = "read {path}"
_WRITE_CHECK_TEMPLATE = "write_check {path}"


class BaseSandbox:
    """Base class for sandbox backends."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def read(self, path: str, **kwargs: Any) -> ReadResult:
        raise NotImplementedError

    def write(self, path: str, content: str, **kwargs: Any) -> WriteResult:
        raise NotImplementedError

    def edit(self, path: str, old_string: str, new_string: str, **kwargs: Any) -> EditResult:
        raise NotImplementedError

    def ls(self, path: str, **kwargs: Any) -> LsResult:
        raise NotImplementedError

    def glob(self, pattern: str, **kwargs: Any) -> GlobResult:
        raise NotImplementedError

    def grep(self, pattern: str, **kwargs: Any) -> GrepResult:
        raise NotImplementedError

    def execute(self, command: str, **kwargs: Any) -> ExecuteResponse:
        raise NotImplementedError

    def download_file(self, path: str, **kwargs: Any) -> FileDownloadResponse:
        raise NotImplementedError

    def upload_file(self, path: str, content: str, **kwargs: Any) -> FileUploadResponse:
        raise NotImplementedError
