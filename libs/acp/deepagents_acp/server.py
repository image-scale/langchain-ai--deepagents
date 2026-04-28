"""ACP Server implementation."""

from typing import Any


class AgentSessionContext:
    """Context for an agent session."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


class AgentServerACP:
    """ACP server for agent communication."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError
