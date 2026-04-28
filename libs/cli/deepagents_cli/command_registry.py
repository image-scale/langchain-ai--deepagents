"""Command registry."""

from typing import Any

SLASH_COMMANDS: dict[str, Any] = {}
ALL_CLASSIFIED: list[str] = []
ALWAYS_IMMEDIATE: list[str] = []
BYPASS_WHEN_CONNECTING: list[str] = []
COMMANDS: dict[str, Any] = {}
IMMEDIATE_UI: list[str] = []
QUEUE_BOUND: list[str] = []
SIDE_EFFECT_FREE: list[str] = []
_STATIC_SKILL_ALIASES: dict[str, str] = {}


def build_skill_commands(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def parse_skill_command(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
