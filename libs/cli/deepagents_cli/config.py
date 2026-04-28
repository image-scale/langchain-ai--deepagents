"""Configuration module."""

from typing import Any

RECOMMENDED_SAFE_SHELL_COMMANDS = ["ls", "cat", "head", "tail", "grep", "find", "pwd"]
SHELL_ALLOW_ALL = "*"
MODE_PREFIXES = {"assistant": "[A]", "user": "[U]"}
_ASCII_BANNER = "Deep Agents"
_UNICODE_BANNER = "🤖 Deep Agents"
ASCII_GLYPHS = {"check": "[x]", "cross": "[ ]"}
UNICODE_GLYPHS = {"check": "✓", "cross": "✗"}


class CharsetMode:
    """Charset mode enum."""
    ASCII = "ascii"
    UNICODE = "unicode"


class Glyphs:
    """Glyph configuration."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ModelResult:
    """Result from model creation."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class Settings:
    """Application settings."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


settings: Settings = None  # type: ignore


def _create_model_from_class(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _create_model_via_init(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_provider_kwargs(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def build_langsmith_thread_url(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def create_model(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def detect_provider(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def fetch_langsmith_project_url(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_langsmith_project_name(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def newline_shortcut(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def parse_shell_allow_list(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def reset_langsmith_url_cache(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def validate_model_capabilities(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_glyphs(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _detect_charset_mode(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_banner(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def is_ascii_mode(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def reset_glyphs_cache(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def build_stream_config(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_settings(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_console(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _ensure_bootstrap(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _load_dotenv(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _find_dotenv_from_start_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def contains_dangerous_patterns(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def is_shell_command_allowed(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


__version__ = "0.5.0a3"
