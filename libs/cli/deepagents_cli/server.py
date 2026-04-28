"""Server module."""

from typing import Any


class ServerProcess:
    """Server process management."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _build_server_cmd(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _build_server_env(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _scoped_env_overrides(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _find_free_port(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _port_in_use(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def wait_for_server_healthy(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def generate_langgraph_json(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
