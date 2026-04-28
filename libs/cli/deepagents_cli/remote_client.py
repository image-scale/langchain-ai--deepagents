"""Remote client module."""

from typing import Any


class RemoteAgent:
    """Remote agent client."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _convert_ai_message(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _convert_human_message(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _convert_interrupts(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _convert_message_data(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _convert_tool_message(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _prepare_config(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
