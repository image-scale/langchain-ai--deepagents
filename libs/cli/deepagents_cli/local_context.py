"""Local context middleware."""

from typing import Any

_DETECT_SCRIPT_TIMEOUT = 5.0
_TOOL_NAME_DISPLAY_LIMIT = 50
DETECT_CONTEXT_SCRIPT = ""


class LocalContextState:
    """State for local context."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class LocalContextMiddleware:
    """Middleware for local context."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class _AsyncExecutableBackend:
    """Async executable backend."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class _ExecutableBackend:
    """Executable backend."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _build_mcp_context(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_files(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_git(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_header(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_makefile(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_package_managers(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_project(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_runtimes(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_test_command(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _section_tree(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def build_detect_script(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
