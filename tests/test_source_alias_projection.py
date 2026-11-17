"""#1149: preserve the entire mapping/owner and reject scientific scope changes."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.source_alias_refresh import verify_owner, verify_row

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/kgm_unmapped_chemicals_20261107"
SPEC = importlib.util.spec_from_file_location(
    "publish_acetate", ROOT / "scripts/publish_mediadive_acetate_alias.py"
)
publisher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publisher)


def proof():
    return json.loads((REPORT / "sodium-acetate/publication/projection.json").read_text())[
        "row_projection"
    ]


def test_projection_preserves_every_unselected_physical_row():
    before = (REPORT / "sodium-acetate/publication/canonical-before.tsv").read_bytes()
    candidate = (REPORT / "native-generation/native-candidate.sssom.tsv").read_bytes()
    after, audit = publisher.project(before, candidate)
    old_lines, new_lines = before.splitlines(), after.splitlines()
    assert len(old_lines) == len(new_lines)
    changed = [(a, b) for a, b in zip(old_lines, new_lines, strict=True) if a != b]
    assert len(changed) == 1
    assert changed[0][0].startswith(b"MIM:Sodium_Acetate_Trihydrate\t")
    assert audit == proof()
    verify_row(audit["before"], audit["after"])


@pytest.mark.parametrize(
    "field,value",
    [
        ("object_id", "CHEBI:32954"),
        ("predicate_id", "skos:closeMatch"),
        ("confidence", "0.99"),
        ("validation_method", ""),
        ("comment", "new assertion"),
        ("other", "Na acetate x 3 H2O|acetate"),
        ("source", "replacement history"),
    ],
)
def test_row_proof_rejects_unreviewed_changes(field, value):
    row = proof()
    changed = copy.deepcopy(row["after"])
    changed[field] = value
    with pytest.raises(ValueError, match="unaccounted row change"):
        verify_row(row["before"], changed)


def test_producer_alias_and_identity_cannot_be_substituted():
    before = (REPORT / "sodium-acetate/publication/canonical-before.tsv").read_bytes()
    candidate = (REPORT / "native-generation/native-candidate.sssom.tsv").read_bytes()
    for bad in (
        candidate.replace(b"Na acetate x 3 H2O", b"Na acetate"),
        candidate.replace(b"CHEBI:32138", b"CHEBI:32954"),
    ):
        with pytest.raises(ValueError):
            publisher.project(before, bad)


@pytest.mark.parametrize(
    "field,value",
    [
        ("identifier", "CHEBI:32954"),
        ("mapping_status", "REVIEWED"),
        ("occurrence_statistics", {"total_occurrences": 1, "media_count": 1}),
        ("physicochemical_roles", []),
    ],
)
def test_owner_proof_cannot_approve_other_fields(field, value):
    before = (REPORT / "sodium-acetate/write/owner-before.yaml").read_bytes()
    after = (ROOT / "data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml").read_bytes()
    verify_owner(before, after)
    bad = yaml.safe_load(after)
    bad[field] = value
    with pytest.raises(ValueError, match="unaccounted owner change"):
        verify_owner(before, yaml.safe_dump(bad).encode())
