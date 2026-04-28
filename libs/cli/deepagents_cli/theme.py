"""Theme configuration."""

from typing import Any

_BUILTIN_NAMES = ["dark", "light"]
DEFAULT_THEME = "dark"


class ThemeColors:
    """Theme colors."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ThemeEntry:
    """Theme entry."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


DARK_COLORS = ThemeColors()
LIGHT_COLORS = ThemeColors()


def _build_registry(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _builtin_themes(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _load_user_themes(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_css_variable_defaults(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_theme_colors(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
