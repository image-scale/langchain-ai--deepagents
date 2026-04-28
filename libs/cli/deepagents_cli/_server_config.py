"""Server configuration."""

from typing import Any


def _normalize_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _read_env_bool(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _read_env_json(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _read_env_optional_bool(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _read_env_str(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


class ServerConfig:
    """Server configuration."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError
