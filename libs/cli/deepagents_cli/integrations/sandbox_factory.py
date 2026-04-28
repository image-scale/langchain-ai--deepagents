"""Sandbox factory."""

from typing import Any


def _get_provider(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_default_working_dir(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def verify_sandbox_deps(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
