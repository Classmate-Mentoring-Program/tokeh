"""Utilitaires de nettoyage et de tokenisation du texte.

Ce module fournit des fonctions pour nettoyer le texte brut (mise en minuscules,
suppression de la ponctuation, etc.) et pour découper le texte en tokens.
Il est volontairement léger en dépendances afin de fonctionner sans les
bibliothèques optionnelles telles que spaCy ou NLTK.
"""

from __future__ import annotations

import re
import string


def clean_text(text: str, *, lower: bool = True, remove_punctuation: bool = True) -> str:
    """Nettoie une chaîne de texte brut.

    Args:
        text: Le texte brut en entrée.
        lower: Si ``True`` (défaut), convertit le texte en minuscules.
        remove_punctuation: Si ``True`` (défaut), supprime les caractères de ponctuation.

    Returns:
        La chaîne de texte nettoyée.

    Example:
        >>> clean_text("Bonjour, le Monde !")
        'bonjour le monde '
    """
    if lower:
        text = text.lower()
    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))
    # Réduction des espaces multiples
    text = re.sub(r"\s+", " ", text).strip()
    return text


def simple_tokenize(text: str) -> list[str]:
    """Découpe une chaîne de texte (pré-nettoyée) en tokens séparés par des espaces.

    Args:
        text: Le texte à tokeniser.

    Returns:
        Une liste de chaînes de tokens.

    Example:
        >>> simple_tokenize("bonjour monde")
        ['bonjour', 'monde']
    """
    return text.split()


def remove_stopwords(tokens: list[str], stopwords: set[str] | None = None) -> list[str]:
    """Supprime les mots vides d'une liste de tokens.

    Args:
        tokens: La liste de tokens en entrée.
        stopwords: Un ensemble de mots vides à supprimer.  Si ``None``, une
            petite liste de mots vides anglais intégrée est utilisée.

    Returns:
        Une liste filtrée de tokens sans les mots vides.

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
