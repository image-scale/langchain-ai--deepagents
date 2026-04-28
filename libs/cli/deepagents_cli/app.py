"""Application module."""

from typing import Any


_ITERM_CURSOR_GUIDE_OFF = "\x1b]1337;HighlightCursorLine=no\x07"
_ITERM_CURSOR_GUIDE_ON = "\x1b]1337;HighlightCursorLine=yes\x07"
_TYPING_IDLE_THRESHOLD_SECONDS = 1.0


class DeferredAction:
    """Deferred action for the app."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class QueuedMessage:
    """Message queued for processing."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class TextualSessionState:
    """State for textual session."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class AppResult:
    """Result from running the app."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class DeepAgentsApp:
    """Main Textual application."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _write_iterm_escape(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _extract_model_params_flag(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


class _ThreadHistoryPayload:
    """Thread history payload."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def run_textual_app(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
