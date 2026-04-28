"""Configurable model middleware."""

from typing import Any


class ConfigurableModelMiddleware:
    """Middleware for configurable model support."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _is_anthropic_model(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
