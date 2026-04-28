"""Server manager module."""

from typing import Any


def _apply_server_config(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _write_pyproject(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def server_session(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def start_server_and_get_agent(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
