"""Guard tests: the curator's role/citation validation sets must match the schema.

Historically the sets were hand-maintained copies of the schema permissible values;
a drift bug shipped once (REDOX_INDICATOR / PH_INDICATOR / SELECTIVE_AGENT /
SURFACTANT were in the schema but not the curator set) and these tests were the
guard against a recurrence.

The sets are now derived at import time from the schema via `SchemaView`, so
"drift" in the old sense is impossible — but these tests still guard against
regressions: SchemaView failing to load, the schema path resolving to the wrong
file (e.g., after a package restructure), or an enum being renamed on one side
only. The comparison uses a fresh YAML-load path instead of SchemaView so
that a SchemaView bug can't silently satisfy both sides of the assertion.
"""

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import (
    VALID_CELLULAR_METABOLIC_ROLES,
    VALID_CITATION_TYPES,
    VALID_COMMUNITY_ORGANISM_ROLES,
    VALID_NUTRITIONAL_ROLES,
    VALID_PHYSICOCHEMICAL_ROLES,
)

SCHEMA_PATH = (
    Path(__file__).parent.parent
    / "src"
    / "mediaingredientmech"
    / "schema"
    / "mediaingredientmech.yaml"
)


def _schema_enum(enum_name: str) -> set[str]:
    schema = yaml.safe_load(SCHEMA_PATH.read_text())
    return set(schema["enums"][enum_name]["permissible_values"].keys())


def test_flat_ingredient_role_enum_is_retired():
    """The flat enum, its assignment class, and its slot were removed in #128.

    Guards against a re-introduction that would revive the divergence window the
    facet migration closed: the same concept representable in two places at once.
    """
    schema = yaml.safe_load(SCHEMA_PATH.read_text())
    assert "IngredientRoleEnum" not in schema["enums"]
    assert "RoleAssignment" not in schema["classes"]
    assert "media_roles" not in schema["classes"]["IngredientRecord"]["attributes"]


def test_community_organism_roles_match_schema():
    assert VALID_COMMUNITY_ORGANISM_ROLES == _schema_enum("CommunityOrganismRoleEnum"), (
        "VALID_COMMUNITY_ORGANISM_ROLES is out of sync with CommunityOrganismRoleEnum. "
        "Update the set in curation/ingredient_curator.py to match the schema."
    )


def test_nutritional_roles_match_schema():
    assert VALID_NUTRITIONAL_ROLES == _schema_enum("NutritionalRoleEnum"), (
        "VALID_NUTRITIONAL_ROLES is out of sync with NutritionalRoleEnum."
    )


def test_physicochemical_roles_match_schema():
    assert VALID_PHYSICOCHEMICAL_ROLES == _schema_enum("PhysicochemicalRoleEnum"), (
        "VALID_PHYSICOCHEMICAL_ROLES is out of sync with PhysicochemicalRoleEnum."
    )


def test_cellular_metabolic_roles_match_schema():
    assert VALID_CELLULAR_METABOLIC_ROLES == _schema_enum("CellularMetabolicRoleEnum"), (
        "VALID_CELLULAR_METABOLIC_ROLES is out of sync with CellularMetabolicRoleEnum."
    )


def test_citation_types_match_schema():
    assert VALID_CITATION_TYPES == _schema_enum("CitationTypeEnum"), (
        "VALID_CITATION_TYPES is out of sync with CitationTypeEnum. "
        "Update the set in curation/ingredient_curator.py to match the schema."
    )


# --- #222: DEFINED_MEDIUM -> NAMED_MEDIUM ---------------------------------
def test_ingredient_type_uses_the_renamed_medium_value():
    """`DEFINED` read as the microbiology term of art "chemically defined
    medium"; the value has always denoted record granularity (#168, #216, #222)."""
    values = _schema_enum("IngredientTypeEnum")

    assert "NAMED_MEDIUM" in values
    assert "DEFINED_MEDIUM" not in values, (
        "the retired spelling is back in IngredientTypeEnum")


def test_no_record_carries_the_retired_ingredient_type():
    """The schema and the corpus have to move together — a value the schema no
    longer offers is an instance-validation failure waiting for the next run."""
    root = Path(__file__).parent.parent
    stale = [
        path.relative_to(root)
        for directory in ("data/ingredients/mapped", "data/ingredients/unmapped")
        for path in (root / directory).rglob("*.yaml")
        if (yaml.safe_load(path.read_text(encoding="utf-8")) or {})
        .get("ingredient_type") == "DEFINED_MEDIUM"
    ]

    assert not stale, f"{len(stale)} record(s) still typed DEFINED_MEDIUM: {stale[:5]}"


def test_component_parent_types_match_the_schema():
    """`COMPONENT_PARENT_TYPES` is a hand-written copy of three schema values.
    Renaming one side only makes every decomposition on that type violate the
    partonomy gate — 23 NAMED_MEDIUM records carry components today."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from mediaingredientmech.validation.component_partonomy import (
        COMPONENT_PARENT_TYPES,
    )

    assert COMPONENT_PARENT_TYPES <= _schema_enum("IngredientTypeEnum"), (
        "COMPONENT_PARENT_TYPES names a value the schema does not offer: "
        f"{COMPONENT_PARENT_TYPES - _schema_enum('IngredientTypeEnum')}")


def test_the_legacy_classification_event_is_retained():
    """91 recorded events say CLASSIFIED_DEFINED_MEDIUM. An event log states
    what was done at the time, so the old token stays valid and only new events
    use the new one — unlike the ingredient_type value, which is a claim about
    the record now and was migrated."""
    events = _schema_enum("CurationActionEnum")

    assert "CLASSIFIED_NAMED_MEDIUM" in events
    assert "CLASSIFIED_DEFINED_MEDIUM" in events, (
        "retiring this would invalidate 91 historical curation events")


def test_the_legacy_event_count_in_the_schema_matches_the_corpus():
    """The description justifies keeping CLASSIFIED_DEFINED_MEDIUM by naming a
    count. #479 shipped 91 -- a raw textual grep that double-counted every event,
    because each appears in both the per-record file and the curated aggregate.
    The real figure is 43 records. A number used as a justification should be
    checkable, so this pins it rather than trusting the prose (#480).
    """
    root = Path(__file__).parent.parent
    with open(SCHEMA_PATH, encoding="utf-8") as fh:
        schema = yaml.safe_load(fh)
    described = schema["enums"]["CurationActionEnum"]["permissible_values"][
        "CLASSIFIED_DEFINED_MEDIUM"]["description"]

    actual = sum(
        1
        for directory in ("data/ingredients/mapped", "data/ingredients/unmapped")
        for path in (root / directory).rglob("*.yaml")
        if any(event.get("action") == "CLASSIFIED_DEFINED_MEDIUM"
               for event in
               ((yaml.safe_load(path.read_text(encoding="utf-8")) or {})
                .get("curation_history") or []))
    )

    # Parsed as a number, not matched as a substring: `f"{actual} recorded
    # events" in described` passes when the true count is a *suffix* of the
    # documented one, so 3 would satisfy a schema claiming 43 -- and 43 -> 3 is
    # exactly what a bulk record merge produces (#483). This is the #259 and
    # #476 defect, which this file exists to guard against.
    stated = re.search(r"(\d+) recorded events", described)
    assert stated, f"the description no longer states a count: {described!r}"
    assert int(stated.group(1)) == actual, (
        f"schema claims {stated.group(1)} recorded events; the corpus has "
        f"{actual} records carrying a CLASSIFIED_DEFINED_MEDIUM event")
