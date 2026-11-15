"""Explicit secondary assertions preserve identity and cannot bypass review (#1418)."""

import json
from copy import deepcopy
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech import additional_mappings as extra
from mediaingredientmech.curate import stable_sssom_publication as pub
from mediaingredientmech.export import reviewed_sssom as reviewed
from mediaingredientmech.export.source_bindings import expand_mim, graph_id
from mediaingredientmech.stable_ids import MIM_PREFIX
from mediaingredientmech.validation.write_validated import validate_ingredient
from tests.test_reconcile_sssom import COLS, _row, _stub_resolver, _write_sssom
from tests.test_reconcile_sssom import mod as reconcile


@pytest.fixture
def owner():
    return {
        "mim_id": "MIM:0000001",
        "identifier": "mesh:M1234567",
        "preferred_term": "Synthetic material",
        "mapping_status": "MAPPED",
        "legacy_identifiers": ["MIM:Historical_name"],
        "ontology_mapping": {
            "ontology_id": "mesh:M1234567",
            "ontology_label": "Synthetic material",
            "ontology_source": "MESH",
            "mapping_quality": "EXACT_MATCH",
            "evidence": [{"evidence_type": "DATABASE_MATCH", "source": "primary-source"}],
        },
        "synonyms": [{"synonym_text": "Rejected name", "synonym_type": "REJECTED_LABEL"}],
        "notes": "Unchanged source and role holds; fixture only",
        "additional_ontology_mappings": [
            {
                "subject_id": "MIM:0000001",
                "ontology_id": "mesh:D123456",
                "ontology_label": "Synthetic broader concept",
                "ontology_source": "MESH",
                "predicate_id": "skos:broadMatch",
                "review_status": "SUPPORTED",
                "reviewed_by": "synthetic-reviewer",
                "reviewed_at": "2026-11-14T12:00:00Z",
                "review_note": "Synthetic independently assessed relation; not a scientific approval",
                "llm_assisted": True,
                "mapping_justification": "semapv:ManualMappingCuration",
                "evidence": [
                    {
                        "evidence_type": "DATABASE_MATCH",
                        "source": "extra-source",
                        "supports": "SUPPORT",
                        "explanation": "Synthetic source supports precisely the broader relation",
                    }
                ],
            }
        ],
    }


def rows(owner):
    primary = dict.fromkeys(COLS, "")
    primary.update(
        subject_id=owner["mim_id"],
        subject_label=owner["preferred_term"],
        predicate_id="skos:exactMatch",
        object_id=owner["identifier"],
        object_label=owner["preferred_term"],
        source="MIM:primary-source",
        mapping_date="2026-11-14",
    )
    additional = [
        {
            **primary,
            "object_id": item["ontology_id"],
            "object_label": item["ontology_label"],
            "predicate_id": item["predicate_id"],
            "source": "|".join(
                [
                    *("MIM:" + entry["source"] for entry in item["evidence"]),
                    "MIM:curator=" + item["reviewed_by"],
                ]
            ),
            "mapping_justification": item["mapping_justification"],
            "comment": extra.assertion_comment(item),
        }
        for item in owner[extra.FIELD]
    ]
    return [primary, *additional]


def table(items):
    return (
        b"# mapping_set_id: https://example.org/synthetic\n# predicate_semantics: skos\n"
        + f"# curie_map:\n#   MIM: {MIM_PREFIX}\n".encode()
        + reviewed._tsv(COLS, items)
    )


def test_schema_accepts_independent_assertion_without_owner_changes(owner):
    before = deepcopy(owner)
    assert validate_ingredient(owner) == []
    assert extra.assertions(owner) == owner[extra.FIELD]
    assert owner == before
    assert expand_mim(graph_id(owner["mim_id"])) == expand_mim(owner["mim_id"])
    assert expand_mim(owner["mim_id"]) == MIM_PREFIX + "0000001"


@pytest.mark.parametrize(
    "field,value",
    [
        ("subject_id", "MIM:0000002"),
        ("ontology_id", "mesh:M1234567"),
        ("predicate_id", "rdfs:subClassOf"),
        ("ontology_source", "CHEBI"),
        ("evidence", []),
        ("reviewed_by", ""),
        ("reviewed_at", "2026-11-14"),
        ("review_status", "UNREVIEWED"),
    ],
)
def test_native_write_gate_refuses_incomplete_or_conflicting_claim(owner, field, value):
    owner[extra.FIELD][0][field] = value
    assert validate_ingredient(owner)


def test_withheld_contradiction_retained_but_never_supported(owner):
    item = owner[extra.FIELD][0]
    item["evidence"][0]["supports"] = "REFUTE"
    assert validate_ingredient(owner)
    item["review_status"] = "WITHHOLD"
    assert validate_ingredient(owner) == []
    assert extra.row_assertion(owner, rows(owner)[1])["review_status"] == "WITHHOLD"


def test_no_extras_does_not_bypass_or_crash_existing_primary_schema_validation(owner):
    owner.pop(extra.FIELD)
    owner["ontology_mapping"] = ["invalid primary shape"]
    assert validate_ingredient(owner)


def test_invalid_primary_target_with_extras_returns_validation_errors(owner):
    owner["ontology_mapping"]["ontology_id"] = ["invalid target shape"]
    assert validate_ingredient(owner)


def test_later_forged_supported_payload_cannot_hide_current_withheld_owner(owner):
    owner[extra.FIELD][0]["review_status"] = "WITHHOLD"
    row = rows(owner)[1]
    forged = deepcopy(owner[extra.FIELD][0])
    forged["review_status"] = "SUPPORTED"
    row["comment"] += " " + extra.assertion_comment(forged)
    with pytest.raises(ValueError, match="evidence differs"):
        extra.row_assertion(owner, row)


def test_exact_extra_cannot_excuse_close_primary_or_duplicate_target(owner):
    owner["ontology_mapping"]["mapping_quality"] = "CLOSE_MATCH"
    assert (
        validate_ingredient(owner) == []
    )  # close primary plus separately justified broad relation
    owner[extra.FIELD][0]["predicate_id"] = "skos:exactMatch"
    assert validate_ingredient(owner)
    owner[extra.FIELD][0]["predicate_id"] = "skos:broadMatch"
    owner[extra.FIELD].append(deepcopy(owner[extra.FIELD][0]))
    assert validate_ingredient(owner)


@pytest.mark.parametrize(
    "field,value",
    [
        ("predicate_id", "skos:exactMatch"),
        ("object_label", "changed"),
        ("subject_id", "MIM:0000002"),
        ("other", "Rejected name"),
        ("object_id", "mesh:D999999"),
        ("comment", "unbound evidence"),
    ],
)
def test_full_row_binding_refuses_tampering(owner, field, value):
    row = rows(owner)[1]
    row[field] = value
    with pytest.raises(ValueError, match="Additional ontology mapping"):
        extra.row_assertion(owner, row)


def selection_input(owner):
    """Bounded in-memory inputs exercise the real complete selection derivation."""
    raw = yaml.safe_dump(owner).encode()
    path = "data/ingredients/mapped/Owner.yaml"
    prior = rows(owner)[1].copy()
    prior.update(
        source="historical-source",
        comment="historical review and hold",
        validation_method="historical stamp",
    )
    sidecar = pub._tsv(pub.SIDECAR_FIELDS, [])
    return SimpleNamespace(
        records={path: owner},
        owners={path: SimpleNamespace(content=raw)},
        before={
            pub.CANONICAL: SimpleNamespace(content=table([prior])),
            pub.SUPPRESSIONS: SimpleNamespace(content=sidecar),
        },
        candidate=table(rows(owner)),
        sidecar=sidecar,
        manifest={},
        generation={"adoption": {"synthetic": True}},
        request={"generation": {"synthetic": True}, "historical_reviews": []},
        inputs=SimpleNamespace(read=lambda name: b"synthetic identity closure"),
        successor=None,
        history=[{"source_hold": "unchanged", "role_hold": "unchanged"}],
    )


def test_native_selection_keeps_full_history_and_forces_withheld(owner):
    owner[extra.FIELD][0]["review_status"] = "WITHHOLD"
    loaded = selection_input(owner)
    selected = pub._selection(loaded)
    entry = selected["rows"][1]
    assert entry["mandatory_disposition"] == "INSTALL_WITHHOLD"
    assert entry["candidate_row"] == rows(owner)[1]
    assert entry["before_rows"][0]["row"]["validation_method"] == "historical stamp"
    assert "historical review and hold" in entry["proposed_row"]["comment"]
    assert entry["proposed_row"]["validation_method"] == ""
    assert selected["history"] == loaded.history
    # Changing a reviewed claim cannot be excused by updating a row hash.
    owner[extra.FIELD][0]["evidence"][0]["explanation"] = "changed rationale"
    with pytest.raises(ValueError, match="evidence differs"):
        pub._selection(loaded)


def test_native_selection_cannot_omit_additional_claim(owner):
    loaded = selection_input(owner)
    loaded.candidate = table(rows(owner)[:1])
    with pytest.raises(ValueError, match="complete additional assertion"):
        pub._selection(loaded)


def test_native_selection_cannot_add_unreviewed_triple(owner):
    loaded = selection_input(owner)
    selection = pub._selection(loaded)
    for entry in selection["rows"]:
        entry.update(disposition="INSTALL_SUPPORTED", reason="Synthetic review")
    selection["rows"][0]["proposed_row"]["object_id"] = "mesh:D999999"
    content = json.dumps(selection).encode()
    loaded.inputs = SimpleNamespace(read=lambda name, digest=None: content)
    loaded.request["selection"] = {"path": "selection.json", "sha256": "0" * 64}
    with pytest.raises(ValueError, match="no arbitrary candidate edits"):
        pub._outputs(loaded)


def test_reconcile_preserves_extra_target_and_refuses_missing_claim(owner, tmp_path, monkeypatch):
    source = tmp_path / "candidate.tsv"
    data = rows(owner)
    _write_sssom(source, [_row(**row) for row in data])
    monkeypatch.setattr(reconcile, "SSSOM", source)
    _stub_resolver(monkeypatch, {})
    curated = {"ingredients": [owner]}
    assert not any(reconcile.find_drift(curated, data).values())
    assert reconcile.apply_reconcile(curated, "2026-11-14") == (0, 0, 0, 0)
    assert reconcile._read_sssom()[3] == data
    with pytest.raises(ValueError, match="one current native row"):
        reconcile.find_drift(curated, data[:1])
    owner.pop(extra.FIELD)
    with pytest.raises(ValueError, match="no current owner claim"):
        reconcile.apply_reconcile(curated, "2026-11-14")


def review_fixture(root, owner, disposition):
    path = root / "data/ingredients/mapped/Owner.yaml"
    path.parent.mkdir(parents=True)
    (root / "data/ingredients/unmapped").mkdir()
    path.write_text(yaml.safe_dump(owner))
    ids = root / "data/ids"
    ids.mkdir()
    (ids / "mim_id_registry.tsv").write_text(
        "mim_id\tlabel_at_minting\tminted_on\tstatus\treplaced_by\n"
        "MIM:0000001\tSynthetic material\t2026-11-14\tactive\t\n"
    )
    (ids / "mim_id_lifecycle.tsv").write_text("mim_id\tstatus\treplaced_by\tchanged_at\treason\n")
    data = rows(owner)
    source = root / "source.tsv"
    source.write_bytes(table(data))
    owner_path = path.relative_to(root).as_posix()
    decisions, entries = [], {}
    for number, row in enumerate(data, 1):
        decision = {
            "source_position": number,
            "row_sha256": reviewed.row_sha256(row),
            "owner_record": owner_path,
            "disposition": "SUPPORTED" if number == 1 else disposition,
            "review_reason": "Synthetic full-row review",
            "review_evidence": "evidence.json",
            "evidence_key": str(number),
        }
        decisions.append(decision)
        entries[str(number)] = {
            **{k: decision[k] for k in ("row_sha256", "disposition", "review_reason")},
            "owner_record_sha256": reviewed.digest(path),
        }
    evidence = root / "evidence.json"
    evidence.write_text(json.dumps({"entries": entries}))
    review = {
        "schema_version": 1,
        "source_sssom": "source.tsv",
        "source_sha256": reviewed.digest(source),
        "record_inputs": {owner_path: reviewed.digest(path)},
        "decisions": decisions,
        "inputs": {
            "evidence.json": reviewed.digest(evidence),
            **{p.relative_to(root).as_posix(): reviewed.digest(p) for p in ids.iterdir()},
        },
    }
    request = root / "review.json"
    request.write_text(json.dumps(review))
    return request


@pytest.mark.parametrize("status,decision", [("SUPPORTED", "SUPPORTED"), ("WITHHOLD", "WITHHOLD")])
def test_ordinary_export_keeps_extra_assertion_disposition(owner, tmp_path, status, decision):
    owner[extra.FIELD][0]["review_status"] = status
    request = review_fixture(tmp_path, owner, decision)
    output = tmp_path / "output"
    manifest = reviewed.export_reviewed(tmp_path, request, output)
    assert manifest["counts"]["supported"] == (2 if status == "SUPPORTED" else 1)
    product = reviewed.PRODUCTS[0 if status == "SUPPORTED" else 1]
    selected = reviewed.read_sssom(output / product)[2]
    assert selected[-1] == rows(owner)[1]
    assert reviewed.validate_reviewed(tmp_path, request, output) == manifest


def test_ordinary_review_cannot_upgrade_owner_hold(owner, tmp_path):
    owner[extra.FIELD][0]["review_status"] = "WITHHOLD"
    request = review_fixture(tmp_path, owner, "SUPPORTED")
    with pytest.raises(ValueError, match="held by the current owner"):
        reviewed.export_reviewed(tmp_path, request, tmp_path / "output")


@pytest.mark.parametrize("missing", [True, False])
def test_ownerless_or_ineligible_held_canonical_rows_keep_native_refusal(owner, tmp_path, missing):
    owner[extra.FIELD][0]["review_status"] = "WITHHOLD"
    request = review_fixture(tmp_path, owner, "WITHHOLD")
    path = tmp_path / "data/ingredients/mapped/Owner.yaml"
    if missing:
        path.unlink()
    else:
        owner["mapping_status"] = "UNMAPPED"
        path.write_text(yaml.safe_dump(owner))
    document = json.loads(request.read_text())
    # Remove stale-byte failures so this tests actual independent owner resolution.
    document["record_inputs"] = (
        {} if missing else {path.relative_to(tmp_path).as_posix(): reviewed.digest(path)}
    )
    request.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="No unique independent owner"):
        reviewed.load_review(tmp_path, request)


def test_full_graph_retains_held_claim_but_release_and_supported_subset_refuse_upgrade(
    owner, tmp_path
):
    from mediaingredientmech.export import kgx, supported_kgx
    from mediaingredientmech.validation import semantic_release

    owner[extra.FIELD][0]["review_status"] = "WITHHOLD"
    close = deepcopy(owner[extra.FIELD][0])
    close.update(
        ontology_id="mesh:D654321",
        ontology_label="Synthetic close concept",
        predicate_id="skos:closeMatch",
        review_status="SUPPORTED",
    )
    close["evidence"][0]["source"] = "independent-close-source"
    close["evidence"][0]["explanation"] = "Synthetic source supports precisely the close relation"
    owner[extra.FIELD].append(close)
    review_fixture(tmp_path, owner, "WITHHOLD")
    curated = tmp_path / "data/curated"
    curated.mkdir()
    (curated / "mapped_ingredients.yaml").write_text(yaml.safe_dump({"ingredients": [owner]}))
    unresolved = {
        "mim_id": "MIM:0000002",
        "identifier": "UNMAPPED_2",
        "preferred_term": "Unresolved fixture",
        "mapping_status": "UNMAPPED",
    }
    (tmp_path / "data/ingredients/unmapped/Unresolved.yaml").write_text(yaml.safe_dump(unresolved))
    (curated / "unmapped_ingredients.yaml").write_text(
        yaml.safe_dump({"ingredients": [unresolved]})
    )
    mapping = tmp_path / "mappings/ingredient_mappings.sssom.tsv"
    mapping.parent.mkdir()
    mapping.write_bytes(
        table(rows(owner)).replace(
            b"# curie_map:\n", b"# curie_map:\n#   mesh: http://id.nlm.nih.gov/mesh/\n"
        )
    )
    graph, _, excluded = kgx.build_graph(tmp_path)
    assert not excluded and len(graph.edges) == 3
    assert {edge["subject"] for edge in graph.edges} == {owner["mim_id"]}
    assert not any(edge["predicate"] == "biolink:subclass_of" for edge in graph.edges)
    supported_kgx._supported(next(edge for edge in graph.edges if edge["object"] == "mesh:D654321"))
    assert expand_mim(graph_id(owner["mim_id"])) == expand_mim(owner["mim_id"])
    secondary = next(edge for edge in graph.edges if edge["object"] == "mesh:D123456")
    assert (
        extra.embedded_assertion(json.loads(secondary["assertion_json"]))["review_status"]
        == "WITHHOLD"
    )
    with pytest.raises(ValueError, match="withheld additional"):
        supported_kgx._supported(secondary)
    records = {"data/ingredients/mapped/Owner.yaml": owner}
    current = semantic_release.current_assertions(
        records, rows(owner), {next(iter(records)): "owner-hash"}, "sssom-hash"
    )
    decisions = [{**row, "resolution_status": "OPEN"} for row in current]
    holds = semantic_release.additional_mapping_holds(current, rows(owner))
    assert semantic_release.adjudicate_assertions(current, decisions, {}, mandatory_open=holds)
    held = next(row for row in decisions if row["assertion_id"] in holds)
    held.update(
        resolution_status="APPROVED",
        review_reason="Attempted hold bypass",
        review_evidence="evidence",
    )
    with pytest.raises(ValueError, match="requires OPEN"):
        semantic_release.adjudicate_assertions(
            current, decisions, {"evidence": "hash"}, mandatory_open=holds
        )
