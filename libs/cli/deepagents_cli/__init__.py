"""Deep Agents CLI - The batteries-included agent CLI."""

__version__ = "0.5.0a3"

from deepagents_cli import agent
from deepagents_cli import integrations
from deepagents_cli.main import cli_main

__all__ = [
    "__version__",
    "agent",
    "integrations",
    "cli_main",
]
