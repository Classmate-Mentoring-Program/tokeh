"""Base model abstraction for tokeh NLP models.

All concrete model classes in the :mod:`tokeh.models` package should inherit
from :class:`BaseModel` and implement its abstract methods.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseModel(ABC):
    """Abstract base class for all tokeh NLP models.

    Sub-classes must implement :meth:`fit` and :meth:`predict`.  Optionally
    they may override :meth:`save` / :meth:`load` to persist trained weights.

    Attributes:
        name: A human-readable identifier for the model.
        is_fitted: ``True`` after :meth:`fit` has been called successfully.
    """

    def __init__(self, name: str = "BaseModel") -> None:
        """Initialise the model.

        Args:
            name: A human-readable identifier for this model instance.
        """
        self.name: str = name
        self.is_fitted: bool = False

    # ------------------------------------------------------------------
    # Abstract interface
    # ------------------------------------------------------------------

    @abstractmethod
    def fit(self, X: Any, y: Any = None, **kwargs: Any) -> "BaseModel":
        """Train the model on data *X* (and optional labels *y*).

        Args:
            X: Training input data.
            y: Training labels / targets.  May be ``None`` for unsupervised
                models.
            **kwargs: Additional keyword arguments passed to the trainer.

        Returns:
            ``self`` to allow method chaining.
        """

    @abstractmethod
    def predict(self, X: Any, **kwargs: Any) -> Any:
        """Generate predictions for input data *X*.

        Args:
            X: Input data to predict on.
            **kwargs: Additional keyword arguments.

        Returns:
            Model predictions — the exact type depends on the sub-class.
        """

    # ------------------------------------------------------------------
    # Optional persistence helpers
    # ------------------------------------------------------------------

    def save(self, path: str) -> None:
        """Persist the model to *path*.

        Args:
            path: Filesystem path (file or directory) to save the model.

        Raises:
            NotImplementedError: Sub-classes that support persistence must
                override this method.
        """
        raise NotImplementedError(f"{self.name}.save() is not implemented.")

    def load(self, path: str) -> "BaseModel":
        """Load model weights / state from *path*.

        Args:
            path: Filesystem path to load the model from.

        Returns:
            ``self`` with loaded state.

        Raises:
            NotImplementedError: Sub-classes that support persistence must
                override this method.
        """
        raise NotImplementedError(f"{self.name}.load() is not implemented.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, is_fitted={self.is_fitted})"
