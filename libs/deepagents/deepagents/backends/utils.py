"""Backend utility functions."""

from typing import Any, TypedDict


TOOL_RESULT_TOKEN_LIMIT = 100000
TRUNCATION_GUIDANCE = "Output truncated. Use specific file paths or commands to view remaining content."

_EXTENSION_TO_FILE_TYPE: dict[str, str] = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".md": "markdown",
    ".txt": "text",
}


class FileData(TypedDict, total=False):
    """File data structure."""
    content: str
    encoding: str
    line_count: int
    file_type: str


def _get_file_type(path: str) -> str:
    """Get file type from path extension."""
    raise NotImplementedError


def _glob_search_files(pattern: str, root: str = ".") -> list[str]:
    """Search for files matching a glob pattern."""
    raise NotImplementedError


def _to_legacy_file_data(data: dict[str, Any]) -> dict[str, Any]:
    """Convert to legacy file data format."""
    raise NotImplementedError


def create_file_data(content: str, **kwargs: Any) -> dict[str, Any]:
    """Create file data from content."""
    raise NotImplementedError


def file_data_to_string(data: dict[str, Any]) -> str:
    """Convert file data to string."""
    raise NotImplementedError


def format_content_with_line_numbers(content: str, **kwargs: Any) -> str:
    """Format content with line numbers."""
    raise NotImplementedError


def format_read_response(result: dict[str, Any], **kwargs: Any) -> str:
    """Format a read response for display."""
    raise NotImplementedError


def grep_matches_from_files(pattern: str, files: list[str], **kwargs: Any) -> list[dict[str, Any]]:
    """Find grep matches from files."""
    raise NotImplementedError


def sanitize_tool_call_id(tool_call_id: str) -> str:
    """Sanitize a tool call ID."""
    raise NotImplementedError


def truncate_if_too_long(content: str, max_length: int = TOOL_RESULT_TOKEN_LIMIT) -> str:
    """Truncate content if it's too long."""
    raise NotImplementedError


def update_file_data(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    """Update file data."""
    raise NotImplementedError


def validate_path(path: str) -> bool:
    """Validate a file path."""
    raise NotImplementedError
