"""Media utilities."""

import logging
from typing import Any, TypedDict

logger = logging.getLogger(__name__)


class ImageData(TypedDict, total=False):
    """Image data."""
    data: str
    media_type: str


class VideoData(TypedDict, total=False):
    """Video data."""
    data: str
    media_type: str


def _detect_video_format(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def create_multimodal_content(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def encode_to_base64(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_clipboard_image(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_image_from_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_video_from_path(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_clipboard_via_osascript(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _get_macos_clipboard_image(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
