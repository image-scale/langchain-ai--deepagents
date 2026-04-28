"""Subagent middleware implementation."""

from typing import Any


GENERAL_PURPOSE_SUBAGENT = "general-purpose"
TASK_SYSTEM_PROMPT = "You are a helpful assistant."


class SubAgent:
    """Definition of a sub-agent."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class CompiledSubAgent:
    """Compiled sub-agent ready for execution."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class SubAgentMiddleware:
    """Middleware for sub-agent operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError
