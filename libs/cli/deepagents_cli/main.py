"""Main module for deepagents_cli."""

from typing import Any

_DEFAULT_AGENT_NAME = "default"


def parse_args(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def cli_main(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def apply_stdin_pipe(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _ripgrep_install_hint(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def check_optional_tools(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def format_tool_warning_cli(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def format_tool_warning_tui(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def run_textual_cli_async(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
