"""Utilitaires de représentation vectorielle (embeddings).

Ce module fournit des helpers pour créer des représentations vectorielles
simples au niveau du mot et de la phrase.  Pour des usages plus avancés,
consultez le sous-paquet :mod:`tokeh.models` pour les abstractions de modèles
de base.
"""

from __future__ import annotations

from collections import Counter

import math


def build_vocab(
    corpus: list[list[str]], min_freq: int = 1
) -> dict[str, int]:
    """Construit un vocabulaire mot→indice à partir d'un corpus tokenisé.

    Args:
        corpus: Une liste de documents tokenisés, où chaque document est une
            liste de tokens (chaînes).
        min_freq: Fréquence minimale d'un token pour être inclus dans le
            vocabulaire.  Défaut : ``1``.

    Returns:
        Un dictionnaire associant chaque token à un indice entier unique
        démarrant à ``0``.  Le token spécial ``"<UNK>"`` est toujours inclus
        à l'indice ``0``.

    Example:
        >>> build_vocab([["bonjour", "monde"], ["bonjour"]])
        {'<UNK>': 0, 'bonjour': 1, 'monde': 2}
    """
    counts: Counter[str] = Counter(tok for doc in corpus for tok in doc)
    vocab: dict[str, int] = {"<UNK>": 0}
    for token, freq in sorted(counts.items()):
        if freq >= min_freq:
            vocab[token] = len(vocab)
    return vocab


def one_hot_encode(token: str, vocab: dict[str, int]) -> list[int]:
    """Retourne un vecteur one-hot pour *token* selon *vocab*.

    Args:
        token: Le token à encoder.
        vocab: Un dictionnaire mot→indice produit par :func:`build_vocab`.

    Returns:
        Une liste d'entiers de longueur ``len(vocab)`` avec un ``1`` à
        l'indice correspondant à *token* (ou l'indice ``"<UNK>"`` si *token*
        est absent du vocabulaire) et ``0`` ailleurs.

    Example:
        >>> vocab = {"<UNK>": 0, "bonjour": 1, "monde": 2}
        >>> one_hot_encode("bonjour", vocab)
        [0, 1, 0]
    """
    vec = [0] * len(vocab)
    idx = vocab.get(token, vocab["<UNK>"])
    vec[idx] = 1
    return vec


def tfidf_vectorize(
    corpus: list[list[str]], vocab: dict[str, int]
) -> list[list[float]]:
    """Calcule une matrice TF-IDF simple pour un corpus tokenisé.

    Args:
        corpus: Une liste de documents tokenisés.
        vocab: Un dictionnaire mot→indice (p. ex. issu de :func:`build_vocab`).

    Returns:
        Une liste 2D de forme ``(nb_docs, taille_vocab)`` contenant les scores
        TF-IDF.

    Example:
        >>> vocab = {"<UNK>": 0, "bonjour": 1, "monde": 2}
        >>> tfidf_vectorize([["bonjour", "monde"], ["bonjour"]], vocab)
        [[...], [...]]
    """
    n_docs = len(corpus)
    vocab_size = len(vocab)
    matrix: list[list[float]] = []

    # Fréquence documentaire pour chaque token
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
