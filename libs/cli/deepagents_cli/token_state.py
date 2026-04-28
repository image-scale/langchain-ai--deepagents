"""Token state module."""

from typing import Any, TypedDict


class TokenTrackingState(TypedDict, total=False):
    """State for token tracking."""
    input_tokens: int
    output_tokens: int
    total_tokens: int


class TokenStateMiddleware:
    """Middleware for token state tracking."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError
