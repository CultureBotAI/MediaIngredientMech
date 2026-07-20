"""Route a role name to the ingredient-role facet that owns it.

The flat `IngredientRoleEnum` was retired in #128; roles now live on three
orthogonal facets (`nutritional_roles`, `physicochemical_roles`,
`cellular_metabolic_roles`), each with its own enum and its own curator writer
method. Inference scripts that used to call a single `add_media_role` need to
pick the right writer for the role they inferred.

Every permissible value in the three facet enums is unique across the facets, so
a role name determines its facet unambiguously. `FACET_BY_ROLE` is built from the
schema at first use, so a value added to any facet enum is routable here without
touching this module.

    >>> facet_slot_for("BUFFER")
    'physicochemical_roles'
    >>> add_role(curator, record, "CARBON_SOURCE", confidence=0.9)
"""

from __future__ import annotations

from typing import Any, Optional

from mediaingredientmech.curation.ingredient_curator import (
    VALID_CELLULAR_METABOLIC_ROLES,
    VALID_NUTRITIONAL_ROLES,
    VALID_PHYSICOCHEMICAL_ROLES,
)

NUTRITIONAL = "nutritional_roles"
PHYSICOCHEMICAL = "physicochemical_roles"
CELLULAR_METABOLIC = "cellular_metabolic_roles"

#: Curator writer method for each facet slot.
WRITER_BY_SLOT: dict[str, str] = {
    NUTRITIONAL: "add_nutritional_role",
    PHYSICOCHEMICAL: "add_physicochemical_role",
    CELLULAR_METABOLIC: "add_cellular_metabolic_role",
}


def _build_facet_index() -> dict[str, str]:
    index: dict[str, str] = {}
    collisions: dict[str, list[str]] = {}
    for slot, values in (
        (NUTRITIONAL, VALID_NUTRITIONAL_ROLES),
        (PHYSICOCHEMICAL, VALID_PHYSICOCHEMICAL_ROLES),
        (CELLULAR_METABOLIC, VALID_CELLULAR_METABOLIC_ROLES),
    ):
        for value in values:
            if value in index:
                collisions.setdefault(value, [index[value]]).append(slot)
            index[value] = slot
    if collisions:
        # A name shared by two facets makes routing ambiguous, so the caller
        # must name the facet explicitly rather than have one silently win.
        detail = "; ".join(f"{v}: {', '.join(s)}" for v, s in sorted(collisions.items()))
        raise RuntimeError(
            "Role names must be unique across the three facet enums for "
            f"name-based routing to work, but these are shared — {detail}. "
            "Rename one side, or route those roles with an explicit slot."
        )
    return index


#: Role name -> owning facet slot. Derived from the schema enums.
FACET_BY_ROLE: dict[str, str] = _build_facet_index()


def facet_slot_for(role: str) -> str:
    """Return the facet slot owning `role`.

    Raises:
        ValueError: If no facet enum declares `role` — most likely a retired
            `IngredientRoleEnum` value (e.g. MINERAL, SALT) that needs an
            explicit disposition rather than a mechanical rename.
    """
    try:
        return FACET_BY_ROLE[role]
    except KeyError:
        raise ValueError(
            f"Unknown role {role!r}: not a value of NutritionalRoleEnum, "
            "PhysicochemicalRoleEnum, or CellularMetabolicRoleEnum. If this is a "
            "retired IngredientRoleEnum value (MINERAL, SALT), map it to a facet "
            "value explicitly — see scripts/migrate_media_roles_to_facets.py."
        ) from None


def add_role(
    curator: Any,
    record: dict[str, Any],
    role: str,
    *,
    slot: Optional[str] = None,
    **kwargs: Any,
) -> dict[str, Any]:
    """Add `role` to `record` via the curator writer for its facet.

    Args:
        curator: An IngredientCurator.
        record: The ingredient record dict to update.
        role: A value of one of the three facet enums.
        slot: Optional explicit facet slot, bypassing name-based routing.
        **kwargs: Forwarded to the facet writer (confidence, doi, notes, ...).

    Returns:
        The updated record.
    """
    target = slot or facet_slot_for(role)
    return getattr(curator, WRITER_BY_SLOT[target])(record, role=role, **kwargs)
