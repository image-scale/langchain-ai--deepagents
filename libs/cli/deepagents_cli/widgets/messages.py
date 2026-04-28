"""Message widgets."""

from typing import Any


class AppMessage:
    """Application message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class AssistantMessage:
    """Assistant message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class DiffMessage:
    """Diff message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ErrorMessage:
    """Error message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class QueuedUserMessage:
    """Queued user message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class SkillMessage:
    """Skill message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class SummarizationMessage:
    """Summarization message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ToolCallMessage:
    """Tool call message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class UserMessage:
    """User message widget."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _show_timestamp_toast(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _strip_frontmatter(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _strip_success_exit_line(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _mode_color(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
