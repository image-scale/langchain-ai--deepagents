"""Backend utility functions."""

from __future__ import annotations

import base64
import fnmatch
import os
import re
import warnings
from datetime import datetime, timezone
from typing import Any, TypedDict


TOOL_RESULT_TOKEN_LIMIT = 100000
TRUNCATION_GUIDANCE = "Output truncated. Use specific file paths or commands to view remaining content."

_EXTENSION_TO_FILE_TYPE: dict[str, str] = {
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".gif": "image",
    ".webp": "image",
    ".svg": "image",
    ".bmp": "image",
    ".ico": "image",
    ".pdf": "file",
}


class FileData(TypedDict, total=False):
    """File data structure."""
    content: str | list[str]
    encoding: str
    line_count: int
    file_type: str
    created_at: str
    modified_at: str


class GrepResult:
    """Result from grep operation."""

    def __init__(self, matches: list[dict[str, Any]] | None = None, error: str | None = None) -> None:
        self.matches = matches
        self.error = error


def _get_file_type(path: str) -> str:
    """Get file type from path extension.

    Returns 'text' for unknown extensions.
    """
    ext = os.path.splitext(path)[1].lower()
    return _EXTENSION_TO_FILE_TYPE.get(ext, "text")


def _glob_search_files(
    files: dict[str, Any],
    pattern: str,
    path: str = "/",
) -> str:
    """Search for files matching a glob pattern.

    Args:
        files: Dictionary mapping file paths to file data
        pattern: Glob pattern to match against
        path: Base path to scope the search

    Returns:
        Newline-separated file paths sorted by modification time (most recent first),
        or "No files found" if no matches.
    """
    # Validate path doesn't have traversal
    if ".." in path or path.startswith("~"):
        return "No files found"

    # Normalize path
    if not path.endswith("/"):
        path = path + "/"

    # Strip leading slash from pattern for matching
    pattern = pattern.lstrip("/")

    matches: list[tuple[str, str]] = []  # (path, modified_at)

    for file_path, file_data in files.items():
        # Check if file is under the specified path
        if not file_path.startswith(path) and path != "/":
            continue

        # Get the relative path for pattern matching
        if path == "/":
            relative_path = file_path.lstrip("/")
        else:
            if not file_path.startswith(path):
                continue
            relative_path = file_path[len(path):]

        # Handle recursive glob
        if "**" in pattern:
            # For ** patterns, match against the full relative path
            if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(file_path.lstrip("/"), pattern):
                modified_at = file_data.get("modified_at", "")
                matches.append((file_path, modified_at))
        else:
            # For non-recursive patterns, only match files in the current directory
            if "/" not in relative_path:
                if fnmatch.fnmatch(relative_path, pattern):
                    modified_at = file_data.get("modified_at", "")
                    matches.append((file_path, modified_at))

    if not matches:
        return "No files found"

    # Sort by modification time (most recent first)
    matches.sort(key=lambda x: x[1], reverse=True)

    return "\n".join(m[0] for m in matches)


def _to_legacy_file_data(data: dict[str, Any]) -> dict[str, Any]:
    """Convert to legacy file data format (list[str] content)."""
    content = data.get("content", "")
    if isinstance(content, list):
        return data.copy()

    result = data.copy()
    if isinstance(content, str):
        result["content"] = content.split("\n")
    result.pop("encoding", None)
    return result


def create_file_data(content: str, encoding: str = "utf-8", **kwargs: Any) -> dict[str, Any]:
    """Create file data from content.

    Args:
        content: The file content as a string
        encoding: The encoding type ('utf-8' or 'base64')
        **kwargs: Additional fields to include

    Returns:
        A dictionary with content, encoding, and optional additional fields
    """
    now = datetime.now(timezone.utc).isoformat()
    result: dict[str, Any] = {
        "content": content,
        "encoding": encoding,
        "created_at": kwargs.get("created_at", now),
        "modified_at": kwargs.get("modified_at", now),
    }
    for key, value in kwargs.items():
        if key not in result:
            result[key] = value
    return result


def file_data_to_string(data: dict[str, Any]) -> str:
    """Convert file data to string.

    Handles both new format (str content) and legacy format (list[str] content).
    Emits DeprecationWarning for legacy format.
    """
    content = data.get("content", "")

    if isinstance(content, list):
        warnings.warn(
            "File data with list[str] content is deprecated. Use str content instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return "\n".join(content)

    return content


def format_content_with_line_numbers(content: str, start_line: int = 1, **kwargs: Any) -> str:
    """Format content with line numbers."""
    lines = content.split("\n")
    max_line_num = start_line + len(lines) - 1
    width = len(str(max_line_num))

    formatted_lines = []
    for i, line in enumerate(lines, start=start_line):
        formatted_lines.append(f"{i:>{width}}| {line}")

    return "\n".join(formatted_lines)


def format_read_response(result: dict[str, Any], **kwargs: Any) -> str:
    """Format a read response for display."""
    if "error" in result and result["error"]:
        return f"Error: {result['error']}"

    content = result.get("content", "")
    if not content:
        file_data = result.get("file_data", {})
        content = file_data_to_string(file_data) if file_data else ""

    return content


def grep_matches_from_files(
    files: dict[str, Any],
    pattern: str,
    path: str = "/",
    **kwargs: Any,
) -> GrepResult:
    """Find grep matches from files.

    Args:
        files: Dictionary mapping file paths to file data
        pattern: Regex pattern to search for
        path: Base path to scope the search

    Returns:
        GrepResult with list of matches containing line, text, and file path
    """
    try:
        regex = re.compile(pattern)
    except re.error as e:
        return GrepResult(error=str(e))

    matches: list[dict[str, Any]] = []

    for file_path, file_data in files.items():
        # Check if file is under the specified path
        if path != "/" and not file_path.startswith(path):
            continue

        # Get content as string
        content = file_data_to_string(file_data)

        # Search for matches
        lines = content.split("\n")
        for i, line in enumerate(lines, start=1):
            if regex.search(line):
                matches.append({
                    "file": file_path,
                    "line": i,
                    "text": line,
                })

    return GrepResult(matches=matches)


def sanitize_tool_call_id(tool_call_id: str) -> str:
    """Sanitize a tool call ID by removing invalid characters."""
    # Keep only alphanumeric, underscore, and hyphen
    return re.sub(r"[^a-zA-Z0-9_-]", "", tool_call_id)


def truncate_if_too_long(content: str, max_length: int = TOOL_RESULT_TOKEN_LIMIT) -> str:
    """Truncate content if it's too long.

    Args:
        content: The content to potentially truncate
        max_length: Maximum length in characters

    Returns:
        The original content or truncated content with guidance message
    """
    if len(content) <= max_length:
        return content

    truncated = content[:max_length]
    return f"{truncated}\n\n{TRUNCATION_GUIDANCE}"


def update_file_data(data: dict[str, Any], content: str | None = None, **kwargs: Any) -> dict[str, Any]:
    """Update file data with new content or metadata.

    Args:
        data: The existing file data
        content: New content (optional)
        **kwargs: Additional fields to update

    Returns:
        Updated file data dictionary
    """
    result = data.copy()

    if content is not None:
        result["content"] = content

    result["modified_at"] = datetime.now(timezone.utc).isoformat()

    for key, value in kwargs.items():
        result[key] = value

    return result


def validate_path(path: str, allowed_prefixes: list[str] | None = None) -> str:
    """Validate and normalize a file path.

    Args:
        path: The path to validate
        allowed_prefixes: Optional list of allowed path prefixes

    Returns:
        Normalized absolute path starting with /

    Raises:
        ValueError: If path contains traversal or invalid patterns
    """
    # Convert backslashes to forward slashes
    path = path.replace("\\", "/")

    # Check for Windows absolute paths
    if len(path) >= 2 and path[1] == ":":
        raise ValueError("Windows absolute paths are not supported")

    # Check for home directory expansion
    if path.startswith("~"):
        raise ValueError("Path traversal not allowed: home directory expansion")

    # Normalize the path
    normalized = os.path.normpath(path)

    # Convert backslashes again after normpath (for Windows compatibility)
    normalized = normalized.replace("\\", "/")

    # Check for path traversal
    parts = normalized.split("/")
    for part in parts:
        if part == "..":
            raise ValueError("Path traversal not allowed: contains '..'")

    # Ensure path starts with /
    if not normalized.startswith("/"):
        normalized = "/" + normalized

    # Check allowed prefixes if specified
    if allowed_prefixes:
        # Check for exact prefix match (must be at directory boundary)
        valid = False
        for prefix in allowed_prefixes:
            if normalized.startswith(prefix):
                # Ensure it's a proper prefix (not just string prefix)
                # e.g., /workspace-evil should not match /workspace/
                if normalized == prefix.rstrip("/") or normalized.startswith(prefix.rstrip("/") + "/"):
                    valid = True
                    break
                elif normalized.startswith(prefix):
                    valid = True
                    break

        if not valid:
            raise ValueError(f"Path must start with one of: {allowed_prefixes}")

    return normalized
