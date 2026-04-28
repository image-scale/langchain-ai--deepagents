"""Sessions management."""

from typing import Any, TypedDict


class ThreadInfo(TypedDict, total=False):
    """Thread information."""
    id: str
    name: str
    created_at: str
    updated_at: str


def get_thread_limit(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
