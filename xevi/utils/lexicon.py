from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from .text import strip_tones


class WEBLexicon:
    """
    Collection of word expressions.
    Read a list of word expressions and store them in a set for fast lookups.
    """

    def __init__(self, expressions: Iterable[tuple[str, ...]]):
        self._expressions = set(expressions)
        self.max_length = max(map(len, self._expressions), default=1)

    @classmethod
    def from_iterable(cls, expressions: Iterable[tuple[str, ...]]) -> WEBLexicon:
        return cls(expressions)

    @classmethod
    def from_file(cls, path: Path, *, encoding: str = "utf-8", tones: bool = False) -> WEBLexicon:
        if not path.exists():
            raise FileNotFoundError(path)
        with open(path, encoding=encoding) as f:
            # skip commented lines with (#) and empty lines
            expressions = [
                tuple(strip_tones(w) if tones else w for w in line.strip().split())
                for line in f
                if line.strip() and not line.startswith("#")
            ]
        return cls(expressions)

    def __contains__(self, w: str | tuple[str, ...]) -> bool:
        if isinstance(w, str):
            w = tuple(w.split())
        return w in self._expressions

    def __len__(self) -> int:
        return len(self._expressions)

    def __iter__(self) -> Iterable[tuple[str, ...]]:
        return iter(self._expressions)

    @property
    def expressions(self):
        return self._expressions
