"""Classe de base pour les modèles NLP de tokeh.

Toutes les classes de modèles concrètes du paquet :mod:`tokeh.models`
doivent hériter de :class:`BaseModel`.
"""

from __future__ import annotations


class BaseModel:
    """Classe de base pour tous les modèles NLP de tokeh.

    Attributes:
        name: Identifiant lisible du modèle.
    """

    def __init__(self, name: str = "BaseModel") -> None:
        """Initialise le modèle.

        Args:
            name: Identifiant lisible pour cette instance de modèle.
        """
        self.name: str = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"
