"""Project utilities."""

from typing import Any


class ProjectContext:
    """Context for a project."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def find_project_agent_md(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def find_project_root(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_server_project_context(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
