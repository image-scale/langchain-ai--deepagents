"""Ask user middleware."""

from typing import Any


class AskUserMiddleware:
    """Middleware for asking user questions."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _parse_answers(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _validate_questions(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
