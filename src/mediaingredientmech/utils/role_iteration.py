"""Shared iteration over all role-assignment slots on an IngredientRecord.

Scripts under `scripts/` historically walked the flat `media_roles` slot
directly with a hard-coded `record.get("media_roles", [])`. That slot, along
with `IngredientRoleEnum` and `RoleAssignment`, was retired in #128 once its
assignments were rehomed onto the three role facets, so consumers must walk the
facet slots or they silently miss every role in the corpus.

`iter_role_assignments(record)` yields `(slot_name, role_assignment)` tuples
across every role slot on `IngredientRecord`. Consumers pick which slots they
care about via the `slots` filter, or take everything by default.
"""

from __future__ import annotations

from typing import Any, Iterable, Iterator, Optional

# Matches the schema's declaration order on IngredientRecord: the
# organism-level slot first, then the three ingredient-role facets.
ALL_ROLE_SLOTS: tuple[str, ...] = (
    "community_organism_roles",
    "nutritional_roles",
    "physicochemical_roles",
    "cellular_metabolic_roles",
)

# The three ingredient-role facets; convenient shorthand for callers that want
# ingredient roles only, without the organism-in-community slot.
FACET_ROLE_SLOTS: tuple[str, ...] = (
    "nutritional_roles",
    "physicochemical_roles",
    "cellular_metabolic_roles",
)


def iter_role_assignments(
    record: dict[str, Any],
    slots: Optional[Iterable[str]] = None,
) -> Iterator[tuple[str, dict[str, Any]]]:
    """Yield (slot_name, role_assignment) for every role-assignment dict on `record`.

    Args:
        record: An IngredientRecord dict (as loaded from YAML).
        slots: Optional iterable of slot names to restrict iteration to. Defaults
            to `ALL_ROLE_SLOTS`. Unknown slot names are silently skipped so
            callers can pass literals like `FACET_ROLE_SLOTS` without guarding
            for schema evolution.

    Yields:
        Two-tuples of `(slot_name, role_assignment_dict)`. A record with no
        role assignments yields nothing. Slots present but set to `None` or
        `[]` yield nothing.

    Example:
        >>> for slot, assignment in iter_role_assignments(record):
        ...     if not is_plausible(assignment["role"]):
        ...         print(f"suspect {slot} value: {assignment['role']}")
    """
    target_slots = tuple(slots) if slots is not None else ALL_ROLE_SLOTS
    for slot in target_slots:
        assignments = record.get(slot) or []
        for assignment in assignments:
            yield slot, assignment
