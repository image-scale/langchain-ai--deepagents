"""Offload utilities."""

from typing import Any


class OffloadModelError(Exception):
    """Error during model offload."""
    pass


class OffloadResult:
    """Result from offloading."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class OffloadThresholdNotMet(Exception):
    """Offload threshold not met."""
    pass


def format_offload_limit(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def offload_messages_to_backend(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
