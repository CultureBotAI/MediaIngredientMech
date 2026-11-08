"""Curation tools for ingredient ontology mapping."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from mediaingredientmech.curation.ingredient_curator import IngredientCurator
    from mediaingredientmech.curation.synonym_manager import SynonymManager

__all__ = ["IngredientCurator", "SynonymManager"]


def __getattr__(name: str) -> Any:
    """Load the heavyweight curator only when its public export is requested.

    Lightweight helpers such as ``solution_matcher`` should not need to parse
    the LinkML schema merely because Python initializes this package.
    """
    if name == "IngredientCurator":
        from mediaingredientmech.curation.ingredient_curator import IngredientCurator

        return IngredientCurator
    if name == "SynonymManager":
        from mediaingredientmech.curation.synonym_manager import SynonymManager

        return SynonymManager
    raise AttributeError(name)
