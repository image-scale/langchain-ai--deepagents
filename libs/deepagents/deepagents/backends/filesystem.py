"""Filesystem backend implementation."""

from typing import Any
from deepagents.backends.protocol import (
    BackendProtocol,
    EditResult,
    GlobResult,
    GrepResult,
    LsResult,
    ReadResult,
    WriteResult,
)


def _map_exception_to_standard_error(exc: Exception) -> str:
    """Map exception to a standard error message."""
    raise NotImplementedError


class FilesystemBackend:
    """Backend for file system operations."""

    def __init__(
        self,
        root_dir: str | None = None,
        virtual_mode: bool = False,
        **kwargs: Any,
    ) -> None:
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

    async def aread(self, path: str, **kwargs: Any) -> ReadResult:
        raise NotImplementedError

    async def awrite(self, path: str, content: str, **kwargs: Any) -> WriteResult:
        raise NotImplementedError

    async def aedit(self, path: str, old_string: str, new_string: str, **kwargs: Any) -> EditResult:
        raise NotImplementedError
