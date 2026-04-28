"""Welcome widget."""

from typing import Any

_TIPS = [
    "Press Ctrl+C to cancel a running operation",
    "Use Tab for autocomplete",
]


class WelcomeBanner:
    """Welcome banner widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def build_connecting_footer(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def build_failure_footer(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def build_welcome_footer(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
