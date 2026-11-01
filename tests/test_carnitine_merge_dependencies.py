"""Native downstream behavior of the bounded #1004 three-owner proposal.

Historical counts and approvals are replayed from immutable source excerpts;
none of these fixtures restamps a live review or grants a new approval.
"""

from __future__ import annotations

import copy
import csv
import gzip
import hashlib
import importlib.util
import io
import json
import os
import sys
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export.reviewed_sssom import _owners
from mediaingredientmech.utils.culturemech_occurrences import membership_counts
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path(os.environ.get("MIM_DEPENDENCY_TEST_SOURCE_ROOT", ROOT))
FIXTURES = ROOT / "tests/fixtures"
OWNER = Path("data/ingredients/mapped/NLDM_metabolites.yaml")
SURVIVOR = Path("data/ingredients/mapped/Carnitine_Hydrochloride.yaml")
TOMBSTONE = Path("data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml")
NEW = "NCIT:C216679"
OLD = "kgmicrobe.compound:carnitine_hydrochloride"
STAMP = "2026-11-01T12:00:00+00:00"


def load(relative):
    spec = importlib.util.spec_from_file_location("carnitine_deps_" + Path(relative).stem, SOURCE_ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha(content):
    return hashlib.sha256(content).hexdigest()


def put(root, path, content):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    return target


def put_json(root, path, value):
    return put(root, path, (json.dumps(value, indent=2) + "\n").encode())


@pytest.fixture
def evidence():
    path = FIXTURES / "issue1004-routing-dependencies.json.gz"
    manifest = json.loads((FIXTURES / "issue1004-routing-manifest.json").read_text())
    compressed = path.read_bytes()
    assert sha(compressed) == manifest["fixtures"][path.name]["sha256"]
    raw = gzip.decompress(compressed)
    assert sha(raw) == manifest["fixtures"][path.name]["uncompressed_sha256"]
    return json.loads(raw)


@pytest.fixture
def proposal():
    writer = load("scripts/merge_carnitine_hydrochloride.py")
    directory = FIXTURES / "issue1004-before"
    manifest = json.loads((directory / "manifest.json").read_text())
    inputs = {}
    for name, entry in manifest["files"].items():
        raw = (directory / entry["file"]).read_bytes()
        assert sha(raw) == entry["archive_sha256"]
        content = gzip.decompress(raw) if entry["file"].endswith(".gz") else raw
        assert sha(content) == entry["sha256"]
        inputs[Path(name)] = content
    owners = {path: inputs[path] for path in writer.OWNERS}
    frozen = copy.deepcopy(inputs)
    outputs = writer.propose_sources(owners, inputs[writer.LEDGER], inputs[writer.MEMBERSHIP], timestamp=STAMP)
    assert inputs == frozen
    return writer, inputs, outputs


def test_three_owner_proposal_keeps_one_active_salt_owner_and_valid_partonomy(proposal, evidence):
    writer, before, after = proposal
    records = {path: yaml.safe_load(after[path]) for path in writer.OWNERS}
    active = [r for r in records.values() if r.get("identifier") == NEW and r["mapping_status"] != "REJECTED"]
    assert len(active) == 1 and active[0]["preferred_term"] == "Carnitine Hydrochloride"
    tombstone = records[TOMBSTONE]
    assert tombstone["identifier"] == tombstone["representative"] == NEW
    assert tombstone["ontology_mapping"]["ontology_id"] == NEW
    assert tombstone["mapping_status"] == "REJECTED"
    assert not tombstone.get("chemical_properties")
    all_records = [*evidence["partonomy_context"], *records.values()]
    assert validate_component_partonomy(all_records) == []
    stale_owner = yaml.safe_load(before[OWNER])
    broken = [*evidence["partonomy_context"], records[SURVIVOR], records[TOMBSTONE], stale_owner]
    assert any(OLD in str(v) and "no active MIM record" in str(v) for v in validate_component_partonomy(broken))
    # A representative-linked tombstone is not an active partonomy target by itself.
    tombstone_only = [*evidence["partonomy_context"], records[TOMBSTONE], records[OWNER]]
    assert any(NEW in str(v) and "no active MIM record" in str(v) for v in validate_component_partonomy(tombstone_only))


def test_native_browser_and_label_index_expose_corrected_salt_and_preserve_siblings(proposal, evidence, tmp_path):
    writer, before, after = proposal
    browser = load("scripts/browser_export.py")
    lists = load("scripts/export_lists.py")
    records = {path: yaml.safe_load(after[path]) for path in writer.OWNERS}
    controls = copy.deepcopy(evidence["distinct_controls"])
    path = put(tmp_path, writer.MEMBERSHIP, after[writer.MEMBERSHIP])
    counts = membership_counts(path)
    for owner in (SURVIVOR, TOMBSTONE):
        public = browser.extract_ingredient_for_browser(records[owner], owner.name, counts)
        assert public["id"] == public["ontology_id"] == NEW
        assert "461-06-3" not in public["searchable"]
        assert OLD not in public["searchable"]
        expected = (0, 0) if owner == TOMBSTONE else counts[NEW]
        assert (public["media_count"], public["total_occurrences"]) == expected
    output = tmp_path / "label_index.csv"
    lists.export_label_index([*records.values(), *controls.values()], output)
    with output.open() as stream:
        rows = list(csv.DictReader(stream))
    for name in ("Carnitine Hydrochloride", "Carnitine (Dl) Hydrochloride"):
        matches = [r for r in rows if r["label"].casefold() == name.casefold()]
        assert matches and {r["identifier"] for r in matches} == {NEW}
    for original in controls.values():
        selected = next(r for r in rows if r["label"].casefold() == original["preferred_term"].casefold())
        assert selected["identifier"] == original["identifier"]
    for owner in (SURVIVOR, TOMBSTONE):
        rejected = {s["synonym_text"].casefold() for s in records[owner].get("synonyms", []) if s["synonym_type"] == "REJECTED_LABEL"}
        assert not [r for r in rows if r["identifier"] == NEW and r["label"].casefold() in rejected]
    assert controls == evidence["distinct_controls"]


def test_native_mapping_owner_selection_excludes_the_rejected_duplicate(proposal, tmp_path):
    writer, before, after = proposal
    for path in writer.OWNERS:
        put(tmp_path, path, after[path])
    survivor_row = {"subject_id": "MIM:Carnitine_Hydrochloride", "subject_label": "Carnitine Hydrochloride",
                    "predicate_id": "skos:exactMatch", "object_id": NEW, "object_label": "DL-Carnitine Hydrochloride"}
    owners, records = _owners(tmp_path, [survivor_row])
    assert owners == [str(SURVIVOR)]
    assert str(TOMBSTONE) not in records
    with pytest.raises(ValueError, match="No unique independent owner"):
        _owners(tmp_path, [{**survivor_row, "subject_id": "MIM:Carnitine_Dl_Hydrochloride", "subject_label": "Carnitine (Dl) Hydrochloride"}])


def test_nldm_payload_changes_only_one_component_but_every_owner_hash_changes(proposal):
    writer, before, after = proposal
    builder = load("reports/semantic_review_20260921/resolution/build_review.py")
    old = yaml.safe_load(before[OWNER])
    new = yaml.safe_load(after[OWNER])
    original_parts, updated_parts = old["components"], new["components"]
    expected = copy.deepcopy(original_parts)
    assert expected[58]["component_id"] == OLD
    expected[58]["component_id"] = NEW
    assert updated_parts == expected
    assert updated_parts[58]["component_name"] == original_parts[58]["component_name"]
    assert updated_parts[58]["reference_scope"] == "MIM_CATALOG"
    assert updated_parts[58]["concentration_value"] == original_parts[58]["concentration_value"]
    assert updated_parts[58]["concentration_unit"] == original_parts[58]["concentration_unit"]
    assert new["curation_history"][:-1] == old["curation_history"]
    owner = str(OWNER)
    old_claims = builder.current_assertions({owner: old}, [], {owner: sha(before[OWNER])}, "unused")
    new_claims = builder.current_assertions({owner: new}, [], {owner: sha(after[OWNER])}, "unused")
    def by_position(rows):
        return {(r["assertion_type"], r["source_position"]): r for r in rows}
    prior, current = by_position(old_claims), by_position(new_claims)
    assert len(prior) == len(current) == 68
    assert [key for key in prior if prior[key]["assertion_sha256"] != current[key]["assertion_sha256"]] == [("component", "59")]
    assert all(prior[key]["source_record_sha256"] != current[key]["source_record_sha256"] for key in prior)


def historical_eligibility(builder, evidence, root, owner_hash):
    owner = str(OWNER)
    original = evidence["historical_original_record"]
    archive = root / "archive.json"
    put_json(root, "archive.json", {"reports": {original["review_report"]: evidence["historical_report"]}})
    eligible = builder.archive_historical_reviews(root, evidence["historical_assertions"], {owner: original}, {owner: owner_hash}, archive)
    for row in eligible:
        row["historical_review_sha256"] = evidence["historical_report"]["sha256"]
    return eligible


def test_native_nldm_all_68_nonmapping_approvals_are_withdrawn(proposal, evidence, tmp_path):
    writer, before, after = proposal
    builder = load("reports/semantic_review_20260921/resolution/build_review.py")
    owner = str(OWNER)
    old_hash, new_hash = sha(before[OWNER]), sha(after[OWNER])
    eligible = historical_eligibility(builder, evidence, tmp_path / "before", old_hash)
    assert eligible
    assert historical_eligibility(builder, evidence, tmp_path / "after", new_hash) == []
    assert len(evidence["graph_edges"]) == 68
    approved_counts = {}
    for edge in evidence["graph_edges"]:
        assertion = json.loads(edge["assertion_json"])
        payload = json.dumps(assertion, sort_keys=True, separators=(",", ":"))
        payload_sha = sha(payload.replace("|", "\\u007c").encode())
        args = (owner, edge["assertion_type"], payload_sha, edge, assertion, evidence["inherited_role_reviews"])
        assert builder.inherited_approval(eligible, {owner: old_hash}, *args)
        assert not builder.inherited_approval(eligible, {owner: new_hash}, *args)
        approved_counts[edge["assertion_type"]] = approved_counts.get(edge["assertion_type"], 0) + 1
    assert approved_counts == {"component": 64, "nutritional_roles": 4}


@pytest.mark.parametrize("plan_kind", ["component_plan", "component_disposition"])
def test_native_explicit_plan_guard_remains_strict_without_nldm_bypass(proposal, evidence, plan_kind):
    writer, before, after = proposal
    builder = load("reports/semantic_review_20260921/resolution/build_review.py")
    records = {path: yaml.safe_load(content) for path, content in evidence["explicit_plan_owner_bytes"].items()}
    hashes = {path: sha(content.encode()) for path, content in evidence["explicit_plan_owner_bytes"].items()}
    records[str(OWNER)] = yaml.safe_load(after[OWNER])
    hashes[str(OWNER)] = sha(after[OWNER])
    plan, disposition = evidence["component_plan"], evidence["component_disposition"]
    plan_owner = plan.get("after_path", plan["source_record"])
    assert str(OWNER) not in {plan_owner, disposition["current_record"]}
    builder.validate_explicit_plans(records, hashes, [], {}, [plan], [disposition])
    wrong = dict(hashes)
    wrong[plan_owner if plan_kind == "component_plan" else disposition["current_record"]] = "stale fixture proof"
    with pytest.raises(ValueError, match="Component plan no longer|Stale component disposition"):
        builder.validate_explicit_plans(records, wrong, [], {}, [plan], [disposition])


def mapping_fixture(tmp_path, monkeypatch, proposal, evidence):
    writer, before, after = proposal
    assembler = load("reports/sssom_completion_20260921/assemble_review.py")
    maker = load("reports/sssom_completion_20260921/mapping_changes/make_receipt.py")
    here = tmp_path / "reports/sssom_completion_20260921"
    owner = str(OWNER)
    for path in writer.OWNERS:
        put(tmp_path, path, after[path])
    mapping = evidence["mapping_row"]
    text = io.StringIO()
    text.write("# mapping_set_id: https://example.test/issue1004-owner-only\n# predicate_semantics: skos\n")
    table = csv.DictWriter(text, fieldnames=list(mapping), delimiter="\t", lineterminator="\n")
    table.writeheader()
    table.writerow(mapping)
    source = put(tmp_path, assembler.SOURCE, text.getvalue().encode())
    source_sha = sha(source.read_bytes())
    def document(relative, value):
        put_json(here, relative, value)
    # A reduced replay of the frozen positive NLDM review, not a new approval.
    assert evidence["mapping_decision"]["disposition"] == "SUPPORTED"
    document("baseline-mapping-review.json", {"schema_version": 1, "source_sha256": source_sha, "rows": [mapping], "record_inputs": {owner: sha(before[OWNER])},
        "decisions": [{"source_position": 1, "resolution_status": "APPROVED", "review_reason": evidence["mapping_decision"]["review_reason"],
                       "review_evidence": "prior-review.md"}]})
    for name in ("trait_synonyms", "parent_names"):
        document(f"{name}/decisions.json", {"records": []})
    for name in ("trait-synonym-refresh.json", "parent-name-refresh.json"):
        document(name, {"schema_version": 1, "before_sha256": source_sha, "after_sha256": source_sha,
                        "row_count": 1, "changed_rows": 0, "changes": [], "records": []})
    for name in ("concern_cohorts", "nonmapping_cohorts", "changed-owner-review"):
        document(f"mapping_review/{name}.json", {"rows": []})
    document("mapping_review/issue-intersections.json", {"issue_669_all_baseline_intersections": [],
             "issue_232_conflicting_label_intersections": [], "findings": []})
    for name in ("adversarial-findings", "synonym-adversarial-findings"):
        document(f"mapping_review/{name}.json", {"findings": []})
    document("mapping_review/kgmicrobe-followup.json", {"decisions": []})
    put(tmp_path, "reports/semantic_review_20260921/records.tsv", f"source_record\treview_report\n{owner}\tprior-review.md\n".encode())
    put(tmp_path, "prior-review.md", evidence["historical_report"]["text"].encode())
    for name in ("MAPPING_SEMANTICS.md", "src/mediaingredientmech/export/reviewed_sssom.py",
                 "src/mediaingredientmech/review_claims.py", "src/mediaingredientmech/synonym_policy.py",
                 "src/mediaingredientmech/record_refresh.py", "scripts/validate_reviewed_sssom_schema.py",
                 "src/mediaingredientmech/validation/mapping_change_receipts.py",
                 "src/mediaingredientmech/validation/semantic_release.py"):
        put(tmp_path, name, (SOURCE_ROOT / name).read_bytes())
    put_json(tmp_path, "reports/semantic_review_20260921/resolution/historical-review-evidence.json",
             {"reports": {evidence["historical_original_record"]["review_report"]: evidence["historical_report"]}})
    log = put_json(tmp_path, "source-log.json", {"records": [
        {"source_record": str(path), "before_yaml_sha256": sha(before[path]), "after_yaml_sha256": sha(after[path]),
         "shape": "owner-only fixture", "change": "#1004 proposal", "verification": "native dependency fixture"}
        for path in writer.OWNERS]})
    before_sssom = put(tmp_path, "before.tsv", source.read_bytes())
    receipts = here / "mapping_changes"
    receipts.mkdir()
    monkeypatch.setattr(maker, "ROOT", tmp_path)
    monkeypatch.setattr(maker, "HERE", receipts)
    monkeypatch.setattr(maker, "SOURCE", source)
    monkeypatch.setattr(sys, "argv", ["make_receipt", "--batch", "issue1004-fixture", "--sequence", "1", "--issue", "1004",
                                     "--scope", "owner-only dependency replay", "--before-sssom", str(before_sssom), "--apply-log", str(log)])
    maker.main()
    receipt = receipts / "issue1004-fixture.json"
    monkeypatch.setattr(assembler, "ROOT", tmp_path)
    monkeypatch.setattr(assembler, "HERE", here)
    monkeypatch.setattr(assembler, "REVIEWED_SOURCE", source_sha)
    return assembler, receipt, source, before[OWNER]


def test_native_owner_only_receipt_withdraws_nldm_mapping_approval(proposal, evidence, tmp_path, monkeypatch):
    assembler, receipt, source, old_owner = mapping_fixture(tmp_path, monkeypatch, proposal, evidence)
    before = source.read_bytes()
    document = json.loads(receipt.read_text())
    assert document["changes"] == [] and document["position_map"] == [1]
    assert {r["source_record"] for r in document["records"]} == {str(OWNER), str(SURVIVOR), str(TOMBSTONE)}
    assert document["approval"].startswith("NONE:")
    products = assembler.assemble()
    review = json.loads(products["review.json"])
    assert review["decisions"][0]["disposition"] == "WITHHOLD"
    assert source.read_bytes() == before
    receipt.unlink()
    with pytest.raises(ValueError, match="Owner changed after scientific review"):
        assembler.assemble()
    # The original frozen owner still earns the captured approval with no correction receipt.
    put(tmp_path, OWNER, old_owner)
    assert json.loads(assembler.assemble()["review.json"])["decisions"][0]["disposition"] == "SUPPORTED"


@pytest.mark.parametrize("document_name,field,message", [
    ("baseline-mapping-review.json", "schema_version", "Unsupported baseline schema"),
    ("baseline-mapping-review.json", "source_sha256", "Invalid SHA256"),
    ("trait-synonym-refresh.json", "before_sha256", "Invalid SHA256"),
    ("parent-name-refresh.json", "schema_version", "Unsupported synonym refresh schema"),
])
def test_owner_only_mapping_fixture_requires_complete_native_history(
    proposal, evidence, tmp_path, monkeypatch, document_name, field, message,
):
    assembler, receipt, source, old_owner = mapping_fixture(tmp_path, monkeypatch, proposal, evidence)
    canonical = source.read_bytes()
    path = assembler.HERE / document_name
    document = json.loads(path.read_text())
    document.pop(field)
    path.write_text(json.dumps(document))
    with pytest.raises(ValueError, match=message):
        assembler.assemble()
    assert source.read_bytes() == canonical


@pytest.mark.parametrize("name", ["Carnitine Hydrochloride", "Carnitine (Dl) Hydrochloride"])
@pytest.mark.parametrize("rejected", ["CHEBI:91318", "CHEBI:48601"])
def test_native_unified_gate_rejects_leaks_with_the_owner_identity_anchor(proposal, tmp_path, name, rejected):
    writer, before, after = proposal
    gate = load("scripts/check_unified_rejections.py")
    ledger = put(tmp_path, writer.LEDGER, after[writer.LEDGER])
    artifact = tmp_path / "unified.tsv"
    fields = ["ingredient_name", *gate.IDENTITY_COLUMNS]
    def check(**extra):
        with artifact.open("w", newline="") as stream:
            table = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
            table.writeheader()
            table.writerow(dict.fromkeys(fields, "") | {"ingredient_name": name, "mim_id": NEW} | extra)
        return gate.check(artifact, ledger)
    assert check() == []
    for column in gate.IDENTITY_COLUMNS:
        # An alias is identity-scoped through mim_id; the gate cannot infer an
        # alias owner after that anchor itself has been replaced. Native producer
        # replay separately verifies both salt names resolve to the NCIT owner.
        if column == "mim_id" and name != "Carnitine Hydrochloride":
            continue
        assert any("republishes rejected" in error or "curated identity" in error
                   for error in check(**{column: rejected}))
    # The same ontology accession remains valid for an independently owned substance.
    assert check(ingredient_name="independent amide or free-form control", mim_id=rejected, chebi_id=rejected) == []
