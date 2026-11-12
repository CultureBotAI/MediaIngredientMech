"""#1151: a provenance correction cannot confer identity or role approval."""

from pathlib import Path

import pytest
import yaml

from mediaingredientmech.source_alias_refresh import verify_provenance_owner

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "field,value",
    [
        ("identifier", "CHEBI:777"),
        ("mapping_status", "MAPPED"),
        ("ontology_mapping", {"ontology_id": "CHEBI:777"}),
        ("synonyms", []),
        ("physicochemical_roles", []),
        ("occurrence_statistics", {"total_occurrences": 7}),
    ],
)
def test_provenance_projection_preserves_all_scientific_assertions(field, value):
    before = (
        ROOT / "reports/kgm_unmapped_chemicals_20261107/methylacetate/write/owner-before.yaml"
    ).read_bytes()
    after = (ROOT / "data/ingredients/unmapped/3-methylacetate.yaml").read_bytes()
    verify_provenance_owner(before, after)
    changed = yaml.safe_load(after)
    changed[field] = value
    with pytest.raises(ValueError):
        verify_provenance_owner(before, yaml.safe_dump(changed).encode())
