"""CLI context management."""

from typing import Any


class CLIContext:
    """Context for CLI operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError
