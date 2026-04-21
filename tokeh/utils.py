"""Utilitaires partagés pour le paquet tokeh.

Ce module fournit des helpers communs — configuration des logs, entrées/sorties
de fichiers et autres petites commodités — utilisés dans l'ensemble du code
tokeh.
"""

from __future__ import annotations

import logging
from pathlib import Path


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Crée et retourne un logger nommé.

    Args:
        name: Le nom du logger, typiquement ``__name__`` du module appelant.
        level: Le niveau de journalisation minimum.  Défaut : ``logging.INFO``.

    Returns:
        Une instance :class:`logging.Logger` configurée.
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
    """Crée un répertoire (et ses parents manquants) s'il n'existe pas.

    Args:
        path: Le chemin du répertoire à créer.

    Returns:
        Le :class:`pathlib.Path` du répertoire.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def read_text_file(path: str | Path, encoding: str = "utf-8") -> str:
    """Lit et retourne le contenu complet d'un fichier texte.

    Args:
        path: Chemin vers le fichier.
        encoding: Encodage du fichier.  Défaut : ``"utf-8"``.

    Returns:
        Le contenu du fichier sous forme de chaîne.

    Raises:
        FileNotFoundError: Si *path* n'existe pas.
    """
    return Path(path).read_text(encoding=encoding)
