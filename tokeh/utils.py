"""General-purpose utility helpers for the tokeh package.

This module provides shared helpers — logging configuration, file I/O, and
other small conveniences — used across the rest of the tokeh codebase.
"""

from __future__ import annotations

import logging
from pathlib import Path


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Create and return a named logger.

    Args:
        name: The logger name, typically ``__name__`` of the calling module.
        level: The minimum logging level.  Defaults to ``logging.INFO``.

    Returns:
        A configured :class:`logging.Logger` instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        )
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def ensure_dir(path: str | Path) -> Path:
    """Create a directory (and any missing parents) if it does not exist.

    Args:
        path: The directory path to create.

    Returns:
        The resolved :class:`pathlib.Path` of the directory.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def read_text_file(path: str | Path, encoding: str = "utf-8") -> str:
    """Read and return the entire contents of a text file.

    Args:
        path: Path to the file.
        encoding: File encoding.  Defaults to ``"utf-8"``.

    Returns:
        The file contents as a plain string.

    Raises:
        FileNotFoundError: If *path* does not exist.
    """
    return Path(path).read_text(encoding=encoding)
