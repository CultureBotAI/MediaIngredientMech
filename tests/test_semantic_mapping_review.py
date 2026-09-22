"""The graph gate must honor the exact, independently validated mapping review."""

import csv
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom as reviewed
from mediaingredientmech.export.kgx import export_graph
from mediaingredientmech.validation import semantic_release as gate

MAPPING_REVIEW = "reports/sssom_completion_20260921/review.json"
HOLD_ID = "MIM.hold:724-aromatic-trait-synonym"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n")


def write_table(path, rows):
    with path.open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def refresh_graph_report(root, path, **updates):
    report = json.loads(path.read_text())
    report.update(updates)
    report["inputs"] = {name: gate.sha(root / name) for name in report["inputs"]}
    write_json(path, report)


@pytest.fixture
def paired_review(tmp_path):
    """An actual one-row SSSOM loader paired with the actual complete graph gate."""
    module = load_module(
        "paired_review_fixture", Path(__file__).with_name("test_semantic_release.py")
    )
    root, report_path = module.reviewed_bundle.__wrapped__(tmp_path)
    report = json.loads(report_path.read_text())
    source = root / "mappings/ingredient_mappings.sssom.tsv"
    mapping = {
        "subject_id": "MIM:Water",
        "subject_label": "Water",
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:15377",
        "object_label": "water",
        "other": "",
    }
    source.write_bytes(
        b"# mapping_set_id: https://example.test/canonical\n# predicate_semantics: skos\n"
        b"# curie_map:\n#   MIM: https://example.test/mim/\n"
        b"#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_\n"
        + reviewed._tsv(list(mapping), [mapping])
    )
    (root / "bundle").rename(root / "original-fixture-bundle")
    export_graph(root, root / "bundle")
    owner = "data/ingredients/mapped/Water.yaml"
    scoped = {
        "source_position": 1,
        "row_sha256": reviewed.row_sha256(mapping),
        "owner_record": owner,
        "disposition": "WITHHOLD",
        "review_reason": "Synthetic exact row awaits source evidence",
        "review_evidence": "mapping-evidence.json",
        "evidence_key": "water",
    }
    proof = {key: scoped[key] for key in ("row_sha256", "disposition", "review_reason")}
    proof["owner_record_sha256"] = gate.sha(root / owner)
    write_json(root / "mapping-evidence.json", {"entries": {"water": proof}})
    mapping_review = {
        "schema_version": 1,
        "source_sssom": str(source.relative_to(root)),
        "source_sha256": gate.sha(source),
        "record_inputs": {owner: gate.sha(root / owner)},
        "inputs": {"mapping-evidence.json": gate.sha(root / "mapping-evidence.json")},
        "decisions": [scoped],
    }
    write_json(root / MAPPING_REVIEW, mapping_review)
    records = {name: yaml.safe_load((root / name).read_text()) for name in report["record_inputs"]}
    identities = gate.current_assertions(
        records, [mapping], report["record_inputs"], gate.sha(source)
    )
    decisions = [
        dict(
            identity,
            resolution_status="OPEN",
            review_reason=scoped["review_reason"],
            review_evidence=MAPPING_REVIEW,
        )
        for identity in identities
    ]
    write_table(root / "assertions.tsv", decisions)
    report["inputs"].update(
        {
            MAPPING_REVIEW: gate.sha(root / MAPPING_REVIEW),
            "mapping-evidence.json": gate.sha(root / "mapping-evidence.json"),
        }
    )
    report.update(
        mapping_review=MAPPING_REVIEW,
        blocking_assertion_ids=[d["assertion_id"] for d in decisions],
        release_verdict="FAIL",
    )
    write_json(report_path, report)
    refresh_graph_report(root, report_path)
    return root, report_path


def support_mapping(fixture):
    root, path = fixture
    document = json.loads((root / MAPPING_REVIEW).read_text())
    document["decisions"][0]["disposition"] = "SUPPORTED"
    proof = json.loads((root / "mapping-evidence.json").read_text())
    proof["entries"]["water"]["disposition"] = "SUPPORTED"
    write_json(root / "mapping-evidence.json", proof)
    document["inputs"]["mapping-evidence.json"] = gate.sha(root / "mapping-evidence.json")
    write_json(root / MAPPING_REVIEW, document)
    decisions = gate.rows(root / "assertions.tsv")
    decisions[0]["resolution_status"] = "APPROVED"
    write_table(root / "assertions.tsv", decisions)
    refresh_graph_report(root, path, release_verdict="PASS", blocking_assertion_ids=[])


@pytest.mark.parametrize("supported", [False, True])
def test_real_standalone_and_graph_gates_agree(paired_review, supported):
    root, path = paired_review
    if supported:
        support_mapping(paired_review)
    loaded = reviewed.load_review(root, root / MAPPING_REVIEW)
    assert loaded["decisions"][0]["disposition"] == ("SUPPORTED" if supported else "WITHHOLD")
    assert gate.validate(root, path)["semantic_release"] == ("PASS" if supported else "FAIL")


@pytest.mark.parametrize(
    "field,value",
    [
        ("resolution_status", "APPROVED"),
        ("review_reason", "Unreviewed replacement reasoning"),
        ("review_evidence", "evidence.md"),
    ],
)
def test_rehashed_graph_decision_cannot_override_mapping_review(paired_review, field, value):
    root, path = paired_review
    decisions = gate.rows(root / "assertions.tsv")
    decisions[0][field] = value
    write_table(root / "assertions.tsv", decisions)
    updates = (
        {"release_verdict": "PASS", "blocking_assertion_ids": []}
        if field == "resolution_status"
        else {}
    )
    refresh_graph_report(root, path, **updates)
    with pytest.raises(ValueError, match="overrides the mapping-specific review"):
        gate.validate(root, path)


def test_mapping_review_must_be_hash_bound_by_graph_report(paired_review):
    root, path = paired_review
    report = json.loads(path.read_text())
    report["inputs"].pop(MAPPING_REVIEW)
    write_json(path, report)
    with pytest.raises(ValueError, match="Missing bound mapping-specific review"):
        gate.validate(root, path)


@pytest.mark.parametrize(
    "field,value", [("object_id", "CHEBI:999999"), ("other", "A different reviewed alias")]
)
def test_valid_review_for_different_sssom_cannot_approve_graph_payload(paired_review, field, value):
    root, path = paired_review
    support_mapping(paired_review)
    source = root / "mappings/ingredient_mappings.sssom.tsv"
    metadata, fields, mappings = reviewed.read_sssom(source)
    mappings[0][field] = value
    alternate = root / "different-source.sssom.tsv"
    header = "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines())
    alternate.write_bytes(header.encode() + reviewed._tsv(fields, mappings))
    document = json.loads((root / MAPPING_REVIEW).read_text())
    document.update(source_sssom=alternate.name, source_sha256=gate.sha(alternate))
    document["decisions"][0]["row_sha256"] = reviewed.row_sha256(mappings[0])
    proof = json.loads((root / "mapping-evidence.json").read_text())
    proof["entries"]["water"]["row_sha256"] = reviewed.row_sha256(mappings[0])
    write_json(root / "mapping-evidence.json", proof)
    document["inputs"]["mapping-evidence.json"] = gate.sha(root / "mapping-evidence.json")
    write_json(root / MAPPING_REVIEW, document)
    refresh_graph_report(root, path)
    assert reviewed.load_review(root, root / MAPPING_REVIEW)["rows"] == mappings
    with pytest.raises(ValueError):
        gate.validate(root, path)


def test_real_mim_resolution_cannot_delete_its_pinned_mapping_review():
    module = load_module(
        "real_resolved_hold", Path(__file__).with_name("test_semantic_hold_resolution.py")
    )
    args = module.corrected_hold.__wrapped__()
    resolution = next(r for r in args["document"]["resolutions"] if r["hold_id"] == HOLD_ID)
    assert resolution["mapping_review"] == MAPPING_REVIEW
    resolution.pop("mapping_review")
    with pytest.raises(ValueError, match="altered or retargeted"):
        gate.validate_release_holds(**args)


@pytest.fixture
def paired_resolved_review(paired_review, monkeypatch):
    """Model the real MIM resolution's required path with synthetic exact row bytes."""
    root, path = paired_review
    report = json.loads(path.read_text())
    identity = gate.rows(root / "assertions.tsv")[0]
    edge = gate.rows(root / "bundle/mim_edges.tsv", kgx=True)[0]
    owner = "data/ingredients/mapped/Water.yaml"
    original = json.loads(edge["assertion_json"])
    original["other"] = "degradation: water"
    old_digest = hashlib.sha256(
        json.dumps(original, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    policy = {
        "hold_id": HOLD_ID,
        "owner_record": owner,
        "assertion_sha256": old_digest,
        "review_reason": "Synthetic original negative review",
        "disposition": "WITHHOLD",
    }
    resolved = {
        "assertion_id": identity["assertion_id"],
        "assertion_sha256": identity["assertion_sha256"],
        "owner_record": owner,
        "owner_record_sha256": report["record_inputs"][owner],
        "edge_id": edge["id"],
        "resolution": "SOURCE_CORRECTED",
        "mapping_review": MAPPING_REVIEW,
        "evidence": "evidence.md",
        "evidence_sha256": gate.sha(root / "evidence.md"),
    }
    monkeypatch.setitem(gate.FROZEN_RELEASE_HOLDS, HOLD_ID, policy)
    monkeypatch.setitem(gate.FROZEN_RELEASE_HOLD_RESOLUTIONS, HOLD_ID, resolved)
    write_json(
        root / "holds.json",
        {
            "schema_version": 1,
            "required_hold_ids": [HOLD_ID],
            "holds": [],
            "historical_holds": [dict(policy, assertion=original)],
            "resolutions": [dict(resolved, hold_id=HOLD_ID)],
        },
    )
    refresh_graph_report(root, path)
    return root, path


def test_resolved_negative_hold_and_mapping_review_can_both_validate(paired_resolved_review):
    root, path = paired_resolved_review
    assert gate.validate(root, path)["semantic_release"] == "FAIL"


@pytest.mark.parametrize(
    "mutation", ["remove_path", "substitute_path", "remove_resolution_requirement"]
)
def test_resolved_mim_hold_requires_its_mapping_review(paired_resolved_review, mutation):
    root, path = paired_resolved_review
    report = json.loads(path.read_text())
    if mutation == "remove_path":
        report.pop("mapping_review")
    elif mutation == "substitute_path":
        report["mapping_review"] = "another-review.json"
    else:
        document = json.loads((root / "holds.json").read_text())
        document["resolutions"][0].pop("mapping_review")
        write_json(root / "holds.json", document)
        report["inputs"]["holds.json"] = gate.sha(root / "holds.json")
    write_json(path, report)
    with pytest.raises(ValueError, match="mapping-specific review|altered or retargeted"):
        gate.validate(root, path)
