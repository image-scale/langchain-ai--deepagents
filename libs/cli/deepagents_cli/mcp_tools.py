"""MCP tools module."""

from typing import Any, TypedDict


class MCPServerInfo(TypedDict, total=False):
    """MCP server information."""
    name: str
    command: str
    args: list[str]


class MCPToolInfo(TypedDict, total=False):
    """MCP tool information."""
    name: str
    description: str
    server: str


class MCPSessionManager:
    """Manager for MCP sessions."""

    def __init__(self, **kwargs: Any) -> None:
        raise NotImplementedError


def _check_remote_server(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _check_stdio_server(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def _filter_project_stdio_servers(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def classify_discovered_configs(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def discover_mcp_configs(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def extract_stdio_server_commands(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def get_mcp_tools(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_mcp_config(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def load_mcp_config_lenient(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def merge_mcp_configs(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError


def resolve_and_load_mcp_tools(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError
