"""Guard tests: the curator's hardcoded validation sets must stay in sync with
the LinkML schema enums.

`IngredientCurator` validates roles / citation types against module-level sets
(`VALID_MEDIA_ROLES`, `VALID_COMMUNITY_ORGANISM_ROLES`, `VALID_CITATION_TYPES`).
These are hand-maintained copies of the schema's permissible values; if a value
is added to the schema enum but not to the set, `add_media_role` /
`add_community_organism_role` raise ValueError on a perfectly valid value (this
exact drift bug shipped once — REDOX_INDICATOR / PH_INDICATOR / SELECTIVE_AGENT
/ SURFACTANT were in the schema but not the curator set). These tests fail
loudly when the two diverge.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import (
    VALID_CITATION_TYPES,
    VALID_COMMUNITY_ORGANISM_ROLES,
    VALID_MEDIA_ROLES,
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


def test_media_roles_match_schema():
    assert VALID_MEDIA_ROLES == _schema_enum("IngredientRoleEnum"), (
        "VALID_MEDIA_ROLES is out of sync with IngredientRoleEnum. "
        "Update the set in curation/ingredient_curator.py to match the schema."
    )


def test_community_organism_roles_match_schema():
    assert VALID_COMMUNITY_ORGANISM_ROLES == _schema_enum("CommunityOrganismRoleEnum"), (
        "VALID_COMMUNITY_ORGANISM_ROLES is out of sync with CommunityOrganismRoleEnum. "
        "Update the set in curation/ingredient_curator.py to match the schema."
    )


def test_citation_types_match_schema():
    assert VALID_CITATION_TYPES == _schema_enum("CitationTypeEnum"), (
        "VALID_CITATION_TYPES is out of sync with CitationTypeEnum. "
        "Update the set in curation/ingredient_curator.py to match the schema."
    )
