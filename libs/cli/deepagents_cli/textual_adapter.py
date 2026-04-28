"""Textual adapter module."""

from typing import Any


class ModelStats:
    """Model statistics."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class SessionStats:
    """Session statistics."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class TextualUIAdapter:
    """Adapter for Textual UI."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _build_interrupted_ai_message(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _handle_interrupt_cleanup(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _is_summarization_chunk(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def execute_task_textual(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def format_token_count(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def print_usage_table(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _persist_context_tokens(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
