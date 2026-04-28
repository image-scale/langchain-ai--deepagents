"""QuickJS Middleware for LangChain."""

from typing import Any


class QuickJSMiddleware:
    """Middleware for executing JavaScript code via QuickJS."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError
