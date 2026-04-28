"""Local shell backend implementation."""

from typing import Any
from deepagents.backends.protocol import ExecuteResponse


DEFAULT_EXECUTE_TIMEOUT = 120


class LocalShellBackend:
    """Backend for executing commands locally."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def execute(self, command: str, **kwargs: Any) -> ExecuteResponse:
        raise NotImplementedError

    async def aexecute(self, command: str, **kwargs: Any) -> ExecuteResponse:
        raise NotImplementedError
