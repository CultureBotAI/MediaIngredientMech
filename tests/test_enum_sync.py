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
