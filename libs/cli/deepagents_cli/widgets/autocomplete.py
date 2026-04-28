"""Autocomplete widget."""

from typing import Any

MAX_SUGGESTIONS = 10


class CompletionController:
    """Controller for completions."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class FuzzyFileController:
    """Controller for fuzzy file completion."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class MultiCompletionManager:
    """Manager for multiple completion sources."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class SlashCommandController:
    """Controller for slash command completion."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _fuzzy_score(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _fuzzy_search(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _is_dotpath(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _path_depth(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
