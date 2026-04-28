"""Ask user types."""

from typing import Any, TypedDict


class Question(TypedDict, total=False):
    """Question data."""
    id: str
    text: str
    type: str


class AskUserWidgetResult(TypedDict, total=False):
    """Result from an ask user widget."""
    answers: dict[str, Any]
