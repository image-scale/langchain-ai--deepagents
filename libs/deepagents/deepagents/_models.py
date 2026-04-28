"""Model utilities for deepagents."""

from typing import Any

_OPENROUTER_APP_TITLE = "DeepAgents"
_OPENROUTER_APP_URL = "https://github.com/langchain-ai/deepagents"
OPENROUTER_MIN_VERSION = "0.3.0"


def _openrouter_attribution_kwargs(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _string_value(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def check_openrouter_version(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_model_identifier(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def model_matches_spec(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def resolve_model(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
