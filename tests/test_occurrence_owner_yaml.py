"""#1463: native shared owner evidence is distinct from companion YAML syntax."""

import hashlib

import pytest
import yaml

from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.occurrence_coverage import (
    _load_document,
    _load_owner_document,
    content_sha256,
    load_coverage,
)
from tests.test_occurrence_coverage import save, write_bundle

# Exact shared evidence structure read from the three affected native records.
# These are synthetic owner fixtures, not new role or identity assertions.
SHARED_ROLES = """nutritional_roles:
- role: {first}
  confidence: 1.0
  evidence: &id001
  - reference_type: DATABASE_ENTRY
    reference_text: Imported from CultureMech pipeline
    curator_note: 'Original role text: Mineral'
- role: {second}
  confidence: 1.0
  evidence: *id001
"""


@pytest.mark.parametrize(
    "record_name,first,second",
    [
        ("Fepo4", "IRON_SOURCE", "PHOSPHATE_SOURCE"),
        ("Magnesium_Acetate", "CARBON_SOURCE", "MINERAL_SOURCE"),
        ("Chalcopyrite", "TRACE_ELEMENT", "IRON_SOURCE"),
    ],
)
@pytest.mark.parametrize("selected", [True, False])
def test_native_shared_role_evidence_on_selected_and_unselected_owners(
    tmp_path, record_name, first, second, selected
):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    if not selected:
        owner = root / "mapped" / (record_name + ".yaml")
        record = {**record, "mim_id": "MIM:0000002"}
    raw = yaml.safe_dump(record) + SHARED_ROLES.format(first=first, second=second)
    native = _load_yaml(raw)
    assert native["nutritional_roles"][0]["evidence"] is native["nutritional_roles"][1]["evidence"]
    assert _load_owner_document(raw.encode()) == native
    # The guarded writer's actual underlying serializer emits shared aliases.
    encoded = yaml.safe_dump(native).encode()
    assert b"&id001" in encoded and b"*id001" in encoded
    owner.write_bytes(encoded)
    if selected:
        doc["declarations"][0].update(
            owner_sha256=hashlib.sha256(encoded).hexdigest(),
            owner_content_sha256=content_sha256(native),
        )
        save(bundle, doc)
    before = owner.read_bytes()
    coverage = load_coverage(bundle, root)
    assert set(coverage.declarations) == {"MIM:0000001"}
    assert owner.read_bytes() == before
    if selected:
        assert coverage.for_record(native)["state"] == "UNKNOWN"


@pytest.mark.parametrize("selected", [True, False])
@pytest.mark.parametrize(
    "extra",
    [
        "mapping_status: REJECTED\n",  # cannot hide an earlier status
        "nutritional_roles:\n- evidence: &shared\n  - reference_text: first\n    reference_text: second\n- evidence: *shared\n",
        "defaults: &defaults {mapping_status: REJECTED}\n<<: *defaults\n",
        "occurrence_statistics: {<<: {media_count: 0}, total_occurrences: 0}\n",
        "notes: !!python/object/apply:builtins.str [unsafe]\n",
        "notes: !!str explicit-type\n",
        "notes: &recursive [*recursive]\n",
        "notes: *undefined\n",
        "notes: &same first\nother: &same second\n",
        "42: non-string-key\n",
        "notes: {42: nested-non-string-key}\n",
        "---\nmim_id: MIM:0000003\n",
    ],
)
def test_ambiguous_owner_yaml_refused_even_outside_selected_set(tmp_path, selected, extra):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    if not selected:
        owner = root / "mapped" / "other.yaml"
        record = {**record, "mim_id": "MIM:0000002"}
    owner.write_text(yaml.safe_dump(record) + extra)
    if selected:
        doc["declarations"][0]["owner_sha256"] = hashlib.sha256(owner.read_bytes()).hexdigest()
        save(bundle, doc)
    # Refusal is at YAML loading, before any owner-hash/content comparison.
    with pytest.raises(ValueError, match="owner YAML"):
        load_coverage(bundle, root)


@pytest.mark.parametrize(
    "raw",
    [
        b"reason: &shared exact\n",
        b"reason: &shared exact\nother: *shared\n",
        b"reason: !!str exact\n",
        b"reason: held\nreason: approved\n",
    ],
)
def test_companion_parser_remains_strict(raw):
    with pytest.raises(ValueError):
        _load_document(raw)


def test_shared_evidence_does_not_change_owner_content_binding(tmp_path):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    raw = yaml.safe_dump(record) + SHARED_ROLES.format(
        first="IRON_SOURCE", second="PHOSPHATE_SOURCE"
    )
    owner.write_text(raw)
    doc["declarations"][0].update(
        owner_sha256=hashlib.sha256(owner.read_bytes()).hexdigest(),
        owner_content_sha256=content_sha256(_load_yaml(raw)),
    )
    save(bundle, doc)
    load_coverage(bundle, root)
    owner.write_text(raw.replace("Original role text: Mineral", "Changed evidence context"))
    # Rebinding file bytes alone still cannot bless changed semantic content.
    doc["declarations"][0]["owner_sha256"] = hashlib.sha256(owner.read_bytes()).hexdigest()
    save(bundle, doc)
    with pytest.raises(ValueError, match="stale occurrence owner content"):
        load_coverage(bundle, root)
