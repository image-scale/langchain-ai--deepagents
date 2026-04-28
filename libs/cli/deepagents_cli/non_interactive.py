"""Non-interactive mode module."""

from typing import Any


class ThreadUrlLookupState:
    """State for thread URL lookup."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _build_non_interactive_header(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _collect_action_request_warnings(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _make_hitl_decision(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _start_langsmith_thread_url_lookup(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def run_non_interactive(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
