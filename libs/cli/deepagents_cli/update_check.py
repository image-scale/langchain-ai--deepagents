"""Update check utilities."""

from typing import Any

CACHE_TTL = 3600


def _latest_from_releases(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _parse_version(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_latest_version(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def is_auto_update_enabled(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def is_update_available(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def set_auto_update(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
