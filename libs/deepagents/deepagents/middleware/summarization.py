"""Summarization middleware implementation."""

from typing import Any


def create_summarization_middleware(*args: Any, **kwargs: Any) -> Any:
    """Create a summarization middleware."""
    raise NotImplementedError


def create_summarization_tool_middleware(*args: Any, **kwargs: Any) -> Any:
    """Create a summarization tool middleware."""
    raise NotImplementedError


class SummarizationMiddleware:
    """Middleware for summarization operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError


class SummarizationToolMiddleware:
    """Middleware for summarization tool operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError
