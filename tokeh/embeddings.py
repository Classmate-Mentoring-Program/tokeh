"""Vector representation utilities (embeddings).

This module provides helpers for creating simple word-level and sentence-level
vector representations of text.  For production workloads consider using the
:mod:`tokeh.models` sub-package which wraps transformer-based encoders.
"""

from __future__ import annotations

from collections import Counter

import math


def build_vocab(
    corpus: list[list[str]], min_freq: int = 1
) -> dict[str, int]:
    """Build a word-to-index vocabulary from a tokenised corpus.

    Args:
        corpus: A list of tokenised documents, where each document is a list
            of string tokens.
        min_freq: Minimum token frequency to be included in the vocabulary.
            Defaults to ``1``.

    Returns:
        A dictionary mapping each token to a unique integer index, starting
        at ``0``.  The special ``"<UNK>"`` token is always included at index
        ``0``.

    Example:
        >>> build_vocab([["hello", "world"], ["hello"]])
        {'<UNK>': 0, 'hello': 1, 'world': 2}
    """
    counts: Counter[str] = Counter(tok for doc in corpus for tok in doc)
    vocab: dict[str, int] = {"<UNK>": 0}
    for token, freq in sorted(counts.items()):
        if freq >= min_freq:
            vocab[token] = len(vocab)
    return vocab


def one_hot_encode(token: str, vocab: dict[str, int]) -> list[int]:
    """Return a one-hot vector for *token* using *vocab*.

    Args:
        token: The token to encode.
        vocab: A word-to-index mapping produced by :func:`build_vocab`.

    Returns:
        A list of integers of length ``len(vocab)`` with a ``1`` at the index
        corresponding to *token* (or the ``"<UNK>"`` index if *token* is not
        in the vocabulary) and ``0`` elsewhere.

    Example:
        >>> vocab = {"<UNK>": 0, "hello": 1, "world": 2}
        >>> one_hot_encode("hello", vocab)
        [0, 1, 0]
    """
    vec = [0] * len(vocab)
    idx = vocab.get(token, vocab["<UNK>"])
    vec[idx] = 1
    return vec


def tfidf_vectorize(
    corpus: list[list[str]], vocab: dict[str, int]
) -> list[list[float]]:
    """Compute a simple TF-IDF matrix for a tokenised corpus.

    Args:
        corpus: A list of tokenised documents.
        vocab: A word-to-index mapping (e.g. from :func:`build_vocab`).

    Returns:
        A 2-D list of shape ``(num_docs, vocab_size)`` containing TF-IDF
        scores.

    Example:
        >>> vocab = {"<UNK>": 0, "hello": 1, "world": 2}
        >>> tfidf_vectorize([["hello", "world"], ["hello"]], vocab)
        [[...], [...]]
    """
    n_docs = len(corpus)
    vocab_size = len(vocab)
    matrix: List[List[float]] = []

    # Document frequency for each token
    df: Counter[int] = Counter()
    for doc in corpus:
        for idx in {vocab.get(tok, 0) for tok in doc}:
            df[idx] += 1

    for doc in corpus:
        tf: Counter[int] = Counter(vocab.get(tok, 0) for tok in doc)
        doc_len = len(doc) or 1
        row: list[float] = [0.0] * vocab_size
        for idx, count in tf.items():
            term_freq = count / doc_len
            idf = math.log((1 + n_docs) / (1 + df[idx])) + 1.0
            row[idx] = term_freq * idf
        matrix.append(row)

    return matrix
