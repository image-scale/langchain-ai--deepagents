"""Agent module for deepagents_cli."""

from typing import Any

DEFAULT_AGENT_NAME = "default"


def _format_edit_file_description(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _format_execute_description(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _format_fetch_url_description(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _format_task_description(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _format_web_search_description(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _format_write_file_description(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def build_model_identity_section(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def create_cli_agent(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_system_prompt(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def list_agents(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_async_subagents(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def reset_agent(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


class ShellAllowListMiddleware:
    """Middleware for shell command allow list."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError
