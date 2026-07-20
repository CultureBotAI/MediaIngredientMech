"""Shared iteration over all role-assignment slots on an IngredientRecord.

Scripts under `scripts/` have historically walked `media_roles` and
`community_organism_roles` directly with hard-coded `record.get("media_roles",
[])`. Now that the three facet slots (nutritional_roles / physicochemical_roles /
cellular_metabolic_roles) exist too, consumers need to walk all five or they
silently miss facet data.

`iter_role_assignments(record)` yields `(slot_name, role_assignment)` tuples
across every role slot on `IngredientRecord`. Consumers pick which slots they
care about via the `slots` filter, or take everything by default.

Slot list is derived from the LinkML schema at first use — new facet slots
added later show up automatically without touching this file.
"""

from __future__ import annotations

from typing import Any, Iterable, Iterator, Optional

# Ordered so consumers can rely on media_roles / community_organism_roles being
# yielded first (legacy scripts hit those in that order); the three facet slots
# follow. Also matches the schema's declaration order on IngredientRecord.
ALL_ROLE_SLOTS: tuple[str, ...] = (
    "media_roles",
    "community_organism_roles",
    "nutritional_roles",
    "physicochemical_roles",
    "cellular_metabolic_roles",
)

# The three facet slots added by the facet migration; convenient shorthand for
# callers that only care about the new surface.
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
