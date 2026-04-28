"""Async subagent middleware implementation."""

from typing import Any, TypedDict


class AsyncTask(TypedDict, total=False):
    """Async task data."""
    id: str
    status: str
    result: Any


class AsyncSubAgentState(TypedDict, total=False):
    """State for async sub-agent middleware."""
    tasks: dict[str, AsyncTask]


def _build_async_subagent_tools(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _resolve_headers(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _tasks_reducer(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


class AsyncSubAgent:
    """Async sub-agent definition."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class AsyncSubAgentMiddleware:
    """Middleware for async sub-agent operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError
