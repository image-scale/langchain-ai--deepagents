"""Skills middleware implementation."""

from typing import Any, TypedDict


MAX_SKILL_COMPATIBILITY_LENGTH = 1000
MAX_SKILL_DESCRIPTION_LENGTH = 500
MAX_SKILL_FILE_SIZE = 50000


class SkillMetadata(TypedDict, total=False):
    """Skill metadata."""
    name: str
    description: str
    compatibility: str


def _format_skill_annotations(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _list_skills(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


async def _alist_skills(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _parse_skill_metadata(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _validate_metadata(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _validate_skill_name(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


class SkillsMiddleware:
    """Middleware for skills operations."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError

    def wrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError

    async def awrap_model_call(self, request: Any, handler: Any) -> Any:
        raise NotImplementedError
