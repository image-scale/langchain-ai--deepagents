"""Editor utilities."""

from typing import Any

GUI_WAIT_FLAG = "--wait"
VIM_EDITORS = ["vim", "nvim", "vi"]


def _prepare_command(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def open_in_editor(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def resolve_editor(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
