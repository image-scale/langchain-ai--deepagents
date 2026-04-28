"""Model configuration module."""

from typing import Any, TypedDict


PROVIDER_API_KEY_ENV: dict[str, str] = {
    "openai": "OPENAI_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "google": "GOOGLE_API_KEY",
}
THREAD_COLUMN_DEFAULTS = ["name", "created_at", "updated_at"]


class ModelConfigError(Exception):
    """Error during model configuration."""
    pass


class ModelConfig:
    """Model configuration."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ModelProfileEntry:
    """Model profile entry."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ModelSpec:
    """Model specification."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class ThreadConfig(TypedDict, total=False):
    """Thread configuration."""
    columns: list[str]
    relative_time: bool
    sort_order: str


def clear_caches(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_builtin_providers(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_provider_profile_modules(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _load_provider_profiles(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _profile_module_from_class_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def clear_default_model(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_available_models(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_model_profiles(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def has_provider_credentials(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def is_warning_suppressed(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_thread_columns(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def save_recent_model(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def save_thread_columns(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def suppress_warning(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_thread_relative_time(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def save_thread_relative_time(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_thread_sort_order(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def save_thread_sort_order(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_thread_config(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


_thread_config_cache: dict[str, Any] = {}


def resolve_env_var(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def save_default_model(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_default_model_spec(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
