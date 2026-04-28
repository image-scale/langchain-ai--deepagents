"""Message store."""

from typing import Any, TypedDict
from enum import Enum


class MessageType(Enum):
    """Message type enum."""
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
    SYSTEM = "system"
    ERROR = "error"
    SKILL = "skill"
    APP = "app"
    SUMMARIZATION = "summarization"


class ToolStatus(Enum):
    """Tool status enum."""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"


class MessageData(TypedDict, total=False):
    """Message data."""
    id: str
    type: str
    content: str


class MessageStore:
    """Store for messages."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError
