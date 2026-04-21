"""Text cleaning and tokenisation utilities.

This module provides functions to clean raw text (lowercasing, punctuation
removal, etc.) and to split text into tokens.  It is intentionally kept
dependency-light so that it works without optional heavy libraries such as
spaCy or NLTK being installed.
"""

from __future__ import annotations

import re
import string


def clean_text(text: str, *, lower: bool = True, remove_punctuation: bool = True) -> str:
    """Clean a raw text string.

    Args:
        text: The raw input text.
        lower: If ``True`` (default) convert the text to lower-case.
        remove_punctuation: If ``True`` (default) strip punctuation characters.

    Returns:
        The cleaned text string.

    Example:
        >>> clean_text("Hello, World!")
        'hello world'
    """
    if lower:
        text = text.lower()
    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def simple_tokenize(text: str) -> list[str]:
    """Split a (pre-cleaned) text string into whitespace-separated tokens.

    Args:
        text: The text to tokenise.

    Returns:
        A list of token strings.

    Example:
        >>> simple_tokenize("hello world")
        ['hello', 'world']
    """
    return text.split()


def remove_stopwords(tokens: list[str], stopwords: set[str] | None = None) -> list[str]:
    """Remove stop-words from a list of tokens.

    Args:
        tokens: The input list of tokens.
        stopwords: A set of stop-word strings to remove.  If ``None`` a small
            built-in English stop-word list is used.

    Returns:
        A filtered list of tokens with stop-words removed.

    Example:
        >>> remove_stopwords(["the", "quick", "brown", "fox"])
        ['quick', 'brown', 'fox']
    """
    if stopwords is None:
        stopwords = _DEFAULT_STOPWORDS
    return [tok for tok in tokens if tok not in stopwords]


_DEFAULT_STOPWORDS: set[str] = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to",
    "for", "of", "with", "by", "from", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "will", "would", "could", "should", "may", "might", "shall", "can",
    "it", "its", "this", "that", "these", "those", "i", "you", "he",
    "she", "we", "they", "me", "him", "her", "us", "them",
}
