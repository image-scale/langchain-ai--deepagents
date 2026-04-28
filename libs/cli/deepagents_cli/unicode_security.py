"""Unicode security utilities."""

from typing import Any, TypedDict

CONFUSABLES: dict[str, str] = {}


class UnicodeIssue(TypedDict, total=False):
    """Unicode issue data."""
    type: str
    message: str
    position: int


class UrlSafetyResult(TypedDict, total=False):
    """URL safety check result."""
    safe: bool
    issues: list[UnicodeIssue]


def check_url_safety(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def detect_dangerous_unicode(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def format_warning_detail(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def iter_string_values(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def looks_like_url_key(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def render_with_unicode_markers(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def strip_dangerous_unicode(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def summarize_issues(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
