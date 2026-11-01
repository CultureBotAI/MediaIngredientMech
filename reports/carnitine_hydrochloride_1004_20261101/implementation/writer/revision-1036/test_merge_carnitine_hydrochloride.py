"""The #1004 migration binds historical inputs without freezing future cohorts."""

import copy
import csv
import importlib.util
import io
import json
import os
import shutil
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("carnitine_writer", ROOT / "scripts/merge_carnitine_hydrochloride.py")
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
STAMP = "2026-11-01T09:00:00+00:00"


@pytest.fixture(scope="module")
def before():
    return {p: writer.frozen_bytes(p) for p in writer.BEFORE}


@pytest.fixture(scope="module")
def proposal(before):
    return writer.propose_sources({p: before[p] for p in writer.OWNERS}, before[writer.LEDGER],
                                  before[writer.MEMBERSHIP], timestamp=STAMP)


@pytest.fixture
def case(tmp_path, before):
    pytest.importorskip("kg_microbe_write")
    for path, payload in before.items():
        dest = tmp_path / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(payload)
    evidence = tmp_path / writer.EVIDENCE
    shutil.copytree(ROOT / writer.EVIDENCE, evidence)
    return tmp_path, evidence, tmp_path / "receipts/apply.json"


def apply(case):
    root, evidence, log = case
    return writer.apply_sources(root, evidence, log, apply=True)


def tsv(fields, rows):
    out = io.StringIO(newline="")
    stream = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    stream.writeheader()
    stream.writerows(rows)
    return out.getvalue().encode()


def candidate_for(root, before):
    """Expected native rows: independently explicit assertions, not writer output."""
    fields, rows = writer.table(before[writer.SSSOM])
    result = []
    for path, subject in ((writer.SURVIVOR, writer.SUBJECT), (writer.COMPONENT_OWNER, writer.COMPONENT_SUBJECT)):
        record = yaml.safe_load((root / path).read_bytes())
        row = (dict.fromkeys(fields, "") | {
            "subject_id": subject, "subject_label": "Carnitine Hydrochloride",
            "object_id": "NCIT:C216679", "object_label": "DL-Carnitine Hydrochloride",
            "predicate_id": "skos:exactMatch", "object_source": "obo:ncit.owl",
            "mapping_justification": "semapv:LexicalMatching", "confidence": "0.99",
            "other": "Carnitine (Dl) Hydrochloride|CAS:461-05-2",
        } if path == writer.SURVIVOR else dict(next(r for r in rows if r["subject_id"] == subject)))
        row.update(source="|".join(["MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"]]
                                  + ["MIM:curator=Codex"]),
                   mapping_date=record["curation_history"][-1]["timestamp"][:10], validation_method="")
        result.append(row)
    return tsv(fields, result)


def promoted_case(case, before):
    root, _, log = case
    apply(case)
    candidate = root / "candidate.tsv"
    candidate.write_bytes(candidate_for(root, before))
    return root, candidate, log, log.with_name("promote.json")


def test_exact_source_proposal_preserves_history_and_scientific_boundaries(before, proposal):
    old = {p: yaml.safe_load(before[p]) for p in writer.OWNERS}
    new = {p: yaml.safe_load(proposal[p]) for p in writer.OWNERS}
    assert set(proposal) == set(writer.SOURCE_PATHS)
    for path in writer.OWNERS:
        assert new[path]["curation_history"][:-1] == old[path]["curation_history"]
        event = new[path]["curation_history"][-1]
        assert event["timestamp"] == STAMP and event["curator"] == "Codex"
        assert event["llm_assisted"] is True and event["llm_model"] == "gpt-6"
        assert "no approval" in event["changes"].lower() or "No scientific/release approval" in event["changes"]
        assert new[path]["occurrence_statistics"] == old[path]["occurrence_statistics"]
    active, retired, mixture = (new[p] for p in writer.OWNERS)
    for record in (active, retired):
        assert record["identifier"] == record["ontology_mapping"]["ontology_id"] == "NCIT:C216679"
        assert record["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
        assert record["ontology_mapping"]["ontology_label"] == "DL-Carnitine Hydrochloride"
    assert active["mapping_status"] == "MAPPED"
    assert active["chemical_properties"]["pubchem_cid"] == 5970
    assert active["chemical_properties"]["cas_rn"] == "461-05-2"
    assert active["chemical_properties"]["molecular_formula"] == "C7H16ClNO3"
    assert active["chemical_properties"]["smiles"].endswith(".[Cl-]")
    assert ".ClH/" in active["chemical_properties"]["inchi"]
    assert retired["mapping_status"] == "REJECTED" and retired["representative"] == "NCIT:C216679"
    assert "chemical_properties" not in retired
    assert json.dumps(old[writer.TOMBSTONE]["chemical_properties"], sort_keys=True) in retired["curation_history"][-1]["changes"]
    assert "2026-07-05" in active["curation_history"][-1]["changes"]
    assert {s["synonym_text"] for s in active["synonyms"] if s["synonym_type"] == "REJECTED_LABEL"} == {writer.FREE_NAME, writer.AMIDE_NAME}
    assert all(s["source"] == "chebi_synonym_review" for s in active["synonyms"] if s["synonym_type"] == "REJECTED_LABEL")
    assert {"synonym_text": writer.RAW_NAME, "synonym_type": "RAW_TEXT", "source": "CultureBotHT"} in active["synonyms"]
    for path in (writer.SURVIVOR, writer.TOMBSTONE):
        assert new[path]["ontology_mapping"]["evidence"][:-1] == old[path]["ontology_mapping"]["evidence"]
    expected_component = copy.deepcopy(old[writer.COMPONENT_OWNER])
    expected_component["components"][58]["component_id"] = "NCIT:C216679"
    assert {k: v for k, v in mixture.items() if k != "curation_history"} == {
        k: v for k, v in expected_component.items() if k != "curation_history"}


def test_historical_membership_migration_preserves_exact_pairs_and_unrelated_bytes(before, proposal):
    before_rows = writer.table(before[writer.MEMBERSHIP])[1]
    after_rows = writer.table(proposal[writer.MEMBERSHIP])[1]
    old = [r for r in before_rows if r["mim_identifier"] == writer.OLD]
    new = [r for r in after_rows if r["mim_identifier"] == writer.NEW]
    assert len(old) == len(new) == 14
    assert {r["recipe_id"] for r in old} == writer.RECIPES
    assert new == [r | {"mim_identifier": writer.NEW} for r in old]
    assert [r for r in before_rows if r["mim_identifier"] != writer.OLD] == [
        r for r in after_rows if r["mim_identifier"] != writer.NEW]
    assert [x for x in before[writer.MEMBERSHIP].splitlines() if x.startswith(b"#")] == [
        x for x in proposal[writer.MEMBERSHIP].splitlines() if x.startswith(b"#")]
    assert [(r["mim_identifier"], r["recipe_id"]) for r in after_rows] == sorted(
        (r["mim_identifier"], r["recipe_id"]) for r in after_rows)


def test_ledger_preserves_other_bytes_and_scopes_both_rejections(before, proposal):
    old = before[writer.LEDGER].splitlines(keepends=True)
    new = proposal[writer.LEDGER].splitlines(keepends=True)
    prefix = (writer.NAME + "\t").encode()
    assert [r for r in old if not r.startswith(prefix)] == [r for r in new if not r.startswith(prefix)]
    selected = [r for r in writer.table(proposal[writer.LEDGER])[1] if r["ingredient_name"] == writer.NAME]
    assert {(r["rejected_id"], r["mim_id"]) for r in selected} == {("CHEBI:91318", writer.NEW), ("CHEBI:48601", writer.NEW)}
    assert all(writer.NCI_URL in r["reason"] for r in selected)


@pytest.mark.parametrize("defect", ["collision", "duplicate", "missing", "count", "recipe"])
def test_membership_inner_contract_rejects_invalid_reviewed_cohort(before, monkeypatch, defect):
    raw = before[writer.MEMBERSHIP]
    row = next(line for line in raw.splitlines(keepends=True) if line.startswith(writer.OLD.encode() + b"\t"))
    changed = {
        "collision": raw + row.replace(writer.OLD.encode(), writer.NEW.encode(), 1),
        "duplicate": raw + row,
        "missing": raw.replace(row, b"", 1),
        "count": raw.replace(row, row.rsplit(b"\t", 1)[0] + b"\t2\n", 1),
        "recipe": raw.replace(row, row.replace(b"CultureMech:015654", b"CultureMech:999999"), 1),
    }[defect]
    # Exercise the independent structural/cohort checks after a valid file-hash
    # check; this does not alter the production migration's fixed preimage.
    monkeypatch.setitem(writer.BEFORE, writer.MEMBERSHIP, writer.digest(changed))
    with pytest.raises(ValueError, match="membership|cohort"):
        writer.corrected_membership(changed)


@pytest.mark.parametrize("path", writer.SOURCE_PATHS)
def test_pure_proposal_refuses_drift(before, path):
    changed = before | {path: before[path] + b"\n"}
    with pytest.raises(ValueError):
        writer.propose_sources({p: changed[p] for p in writer.OWNERS}, changed[writer.LEDGER], changed[writer.MEMBERSHIP], timestamp=STAMP)


@pytest.mark.parametrize("timestamp", ["invalid", "2026-11-01T09:00:00", "2026-10-01T09:00:00+00:00", "2026-11-01T09:00:00+01:00"])
def test_timestamp_must_bind_actual_utc_post_evidence(before, timestamp):
    with pytest.raises(ValueError, match="timestamp"):
        writer.propose_sources({p: before[p] for p in writer.OWNERS}, before[writer.LEDGER], before[writer.MEMBERSHIP], timestamp=timestamp)


def test_native_source_dryrun_and_apply_then_noop(case, before):
    root, evidence, log = case
    dry = writer.apply_sources(root, evidence, log)
    assert dry["changed"] and not dry["applied"] and not log.exists()
    assert {p: (root / p).read_bytes() for p in before} == before
    result = apply(case)
    assert result["applied"] and result["transaction"]
    receipt = log.read_bytes()
    saved = json.loads(receipt)
    assert saved["state"] == "complete" and len(saved["records"]) == 3
    assert saved["approval"].startswith("NONE")
    for path, backup in writer.backup_paths(log, before).items():
        assert backup.read_bytes() == before[path]
    current = {p: (root / p).read_bytes() for p in writer.SOURCE_PATHS}
    assert writer.complete_sources(current) == current
    assert writer.apply_sources(root, evidence, log, apply=True)["changed"] is False
    assert log.read_bytes() == receipt
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]
    assert (root / writer.BASELINE).read_bytes() == before[writer.BASELINE]


@pytest.mark.parametrize("path", writer.SOURCE_PATHS)
def test_partial_source_state_refuses(case, before, proposal, path):
    root, evidence, log = case
    (root / path).write_bytes(proposal[path])
    with pytest.raises(ValueError):
        writer.apply_sources(root, evidence, log, apply=True)
    assert not log.exists()
    assert all((root / p).read_bytes() == b for p, b in before.items() if p != path)


@pytest.mark.parametrize("name", ["manifest.json", "ncit-c216679.json", "pubchem-5970-properties.json", "chebi-48601-primary.json", "approved-decision.md"])
def test_evidence_drift_refuses_before_any_source_change(case, before, name):
    root, evidence, log = case
    path = evidence / name
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="manifest|evidence"):
        apply(case)
    assert {p: (root / p).read_bytes() for p in before} == before
    assert not log.exists()


@pytest.mark.parametrize("path", [writer.SSSOM, writer.BASELINE])
def test_changed_canonical_anchor_refuses(case, before, path):
    root, _, log = case
    (root / path).write_bytes(before[path] + b"\n")
    with pytest.raises(ValueError, match="anchor"):
        apply(case)
    assert not log.exists()


def native_competitor(root):
    path = root / "data/ingredients/.ignored/nested/Competitor.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    writer.write_validated_ingredient({"identifier": writer.NEW, "preferred_term": "Competing valid NCIT owner",
        "mapping_status": "MAPPED", "ingredient_type": "SINGLE_INGREDIENT", "ontology_mapping": dict(writer.MAPPING)}, path)
    return path


@pytest.mark.parametrize("phase", ["sources", "promote"])
@pytest.mark.parametrize("late", [False, True])
def test_native_valid_competing_owner_is_rechecked_before_commit(case, before, monkeypatch, phase, late):
    from kg_microbe_write.transaction import ValidationFailed
    root, evidence, log = case
    if phase == "promote":
        args = promoted_case(case, before)
        log = args[3]
        def call():
            return writer.promote(*args, apply=True)
    else:
        def call():
            return writer.apply_sources(root, evidence, log, apply=True)
    snapshots = {p: (root / p).read_bytes() for p in before}
    if late:
        original = writer.guarded.reserve_receipt_outputs
        @contextmanager
        def race(*args, **kwargs):
            with original(*args, **kwargs) as handles:
                native_competitor(root)
                yield handles
        monkeypatch.setattr(writer.guarded, "reserve_receipt_outputs", race)
    else:
        native_competitor(root)
    with pytest.raises((ValueError, ValidationFailed), match="already held"):
        call()
    assert {p: (root / p).read_bytes() for p in before} == snapshots
    assert (root / "data/ingredients/.ignored/nested/Competitor.yaml").exists()
    if log.exists():
        assert json.loads(log.read_text())["state"] == "failed"


@pytest.mark.parametrize("phase,replaced_path", [
    *(('sources', p) for p in (None, *writer.SOURCE_PATHS, writer.SSSOM, writer.BASELINE)),
    *(('promote', p) for p in (None, writer.SSSOM, writer.BASELINE)),
])
@pytest.mark.parametrize("symlink", [False, True])
@pytest.mark.parametrize("after_commit", [False, True])
def test_native_reservation_replacements_never_false_complete(case, before, monkeypatch, phase, replaced_path, symlink, after_commit):
    from kg_microbe_write.transaction import ValidationFailed
    root, evidence, source_log = case
    if phase == "promote":
        args = promoted_case(case, before)
        log = args[3]
        def call():
            return writer.promote(*args, apply=True)
    else:
        log = source_log
        def call():
            return writer.apply_sources(root, evidence, log, apply=True)
    snapshots = {p: (root / p).read_bytes() for p in before}
    replaced = log if replaced_path is None else writer.backup_paths(log, (replaced_path,))[replaced_path]
    original = writer.guarded.new_transaction
    victim = root / "competitor-evidence"
    victim.write_bytes(b"competing evidence")
    def replace():
        replaced.unlink()
        if symlink:
            replaced.symlink_to(victim)
        else:
            replaced.write_bytes(b"competing evidence")
    def transaction(*args, **kwargs):
        native = original(*args, **kwargs)
        commit = native.commit
        def racing_commit(apply=False):
            if apply and not after_commit:
                replace()
            result = commit(apply=apply)
            if apply and after_commit:
                replace()
            return result
        native.commit = racing_commit
        return native
    monkeypatch.setattr(writer.guarded, "new_transaction", transaction)
    with pytest.raises((ValueError, ValidationFailed), match="Reserved evidence"):
        call()
    assert replaced.read_bytes() == victim.read_bytes() == b"competing evidence"
    if replaced != log:
        assert json.loads(log.read_text())["state"] == "failed"
    assert all(p.exists() for p in writer.backup_paths(log, writer.SOURCE_PATHS if phase == "sources" else (writer.SSSOM, writer.BASELINE)).values())
    if not after_commit:
        assert {p: (root / p).read_bytes() for p in before} == snapshots
    else:
        assert (log.parent / (log.stem + "-journal")).exists()


@pytest.mark.parametrize("path", [None, *writer.SOURCE_PATHS, writer.SSSOM, writer.BASELINE])
@pytest.mark.parametrize("symlink", [False, True])
def test_every_reserved_source_output_collision_preserves_competitor(case, before, path, symlink):
    root, _, log = case
    dest = log if path is None else writer.backup_paths(log, (path,))[path]
    dest.parent.mkdir(parents=True)
    if symlink:
        victim = root / "old-evidence"
        victim.write_bytes(b"keep")
        dest.symlink_to(victim)
    else:
        dest.write_bytes(b"keep")
    with pytest.raises(FileExistsError):
        apply(case)
    assert dest.read_bytes() == b"keep"
    assert {p: (root / p).read_bytes() for p in before} == before


def test_completed_state_cannot_hide_changed_history_or_chemistry(proposal):
    for path, edit in ((writer.SURVIVOR, "chemistry"), (writer.TOMBSTONE, "history")):
        changed = dict(proposal)
        record = yaml.safe_load(changed[path])
        if edit == "chemistry":
            record["chemical_properties"]["pubchem_cid"] = 288
        else:
            record["curation_history"][0]["changes"] = "rewritten historical event"
        changed[path] = writer.render(record)
        with pytest.raises(ValueError, match="Partial source"):
            writer.complete_sources(changed)


def test_native_promotion_is_bounded_and_preserves_old_source_lineage(case, before):
    args = promoted_case(case, before)
    root, candidate, source_log, log = args
    dry = writer.promote(*args)
    assert dry["changed"] and not dry["applied"]
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]
    result = writer.promote(*args, apply=True, candidate_sha256=writer.digest(candidate.read_bytes()))
    assert result["changed_rows"] == 2 and result["removed_rows"] == 4
    old = writer.table(before[writer.SSSOM])[1]
    new = writer.table((root / writer.SSSOM).read_bytes())[1]
    assert len(new) == len(old) - 4
    assert [r for r in old if r["subject_id"] not in writer.SUBJECTS] == [r for r in new if r["subject_id"] not in writer.SUBJECTS]
    assert not any(r["subject_id"] == writer.RETIRED_SUBJECT for r in new)
    salt = next(r for r in new if r["subject_id"] == writer.SUBJECT)
    assert salt["object_id"] == writer.NEW and salt["predicate_id"] == "skos:exactMatch"
    assert salt["other"] == "Carnitine (Dl) Hydrochloride|CAS:461-05-2"
    assert salt["comment"] == salt["validation_method"] == ""
    for subject in (writer.SUBJECT, writer.COMPONENT_SUBJECT):
        sources = {s for r in old if r["subject_id"] == subject for s in r["source"].split("|")}
        assert sources <= set(next(r for r in new if r["subject_id"] == subject)["source"].split("|"))
    assert len(writer.table(before[writer.BASELINE])[1]) - len(writer.table((root / writer.BASELINE).read_bytes())[1]) == 2
    assert (root / writer.BASELINE).read_bytes() == writer.retired_baseline(before[writer.BASELINE])
    receipt = log.read_bytes()
    assert writer.promote(*args, apply=True)["changed"] is False
    assert log.read_bytes() == receipt
    assert json.loads(source_log.read_text())["records"] == json.loads(receipt)["records"]


@pytest.mark.parametrize("field,value", [("other", "DL-carnitine"), ("object_id", "CHEBI:48601"),
    ("object_id", "cas:461-06-3"), ("predicate_id", "skos:broadMatch"), ("comment", "obsolete registry"),
    ("source", "MIM:unreviewed"), ("mapping_date", "2020-01-01")])
def test_bad_native_candidate_refuses_before_promotion(case, before, field, value):
    args = promoted_case(case, before)
    root, candidate, _, log = args
    fields, rows = writer.table(candidate.read_bytes())
    rows[0][field] = value
    candidate.write_bytes(tsv(fields, rows))
    with pytest.raises(ValueError, match="Candidate"):
        writer.promote(*args, apply=True)
    assert not log.exists()
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]
    assert (root / writer.BASELINE).read_bytes() == before[writer.BASELINE]


def test_candidate_must_exclude_tombstone_and_bind_nldm(case, before):
    args = promoted_case(case, before)
    root, candidate, _, _ = args
    fields, rows = writer.table(candidate.read_bytes())
    candidate.write_bytes(tsv(fields, rows + [rows[0] | {"subject_id": writer.RETIRED_SUBJECT}]))
    with pytest.raises(ValueError, match="no tombstone"):
        writer.promote(*args, apply=True)
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]


def test_requested_candidate_hash_is_enforced(case, before):
    args = promoted_case(case, before)
    with pytest.raises(ValueError, match="candidate hash"):
        writer.promote(*args, apply=True, candidate_sha256="0" * 64)
    assert not args[3].exists()
    assert (args[0] / writer.SSSOM).read_bytes() == before[writer.SSSOM]


def test_source_receipt_must_include_all_three_owner_transitions(case, before):
    args = promoted_case(case, before)
    root, _, source, log = args
    data = json.loads(source.read_text())
    data["records"] = data["records"][:2]
    source.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="all current"):
        writer.promote(*args, apply=True)
    assert not log.exists() and (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]


def test_promotion_rejects_partial_baseline_state(case, before):
    args = promoted_case(case, before)
    root = args[0]
    (root / writer.BASELINE).write_bytes(writer.retired_baseline(before[writer.BASELINE]))
    with pytest.raises(ValueError, match="partial"):
        writer.promote(*args, apply=True)
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]


@pytest.mark.parametrize("phase", ["sources", "promote"])
def test_completed_noop_still_rejects_a_competing_owner(case, before, phase):
    args = promoted_case(case, before)
    if phase == "promote":
        writer.promote(*args, apply=True)
    root, evidence, source_log = case
    native_competitor(root)
    with pytest.raises(ValueError, match="already held"):
        if phase == "sources":
            writer.apply_sources(root, evidence, source_log, apply=True)
        else:
            writer.promote(*args, apply=True)


def test_source_noop_accepts_complete_promotion_but_rejects_canonical_drift(case, before):
    args = promoted_case(case, before)
    root, evidence, source_log = case
    writer.promote(*args, apply=True)
    assert writer.apply_sources(root, evidence, source_log, apply=True)["changed"] is False
    canonical = root / writer.SSSOM
    canonical.write_bytes(canonical.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="canonical anchor"):
        writer.apply_sources(root, evidence, source_log, apply=True)


@pytest.mark.parametrize("defect", ["timestamps", "missing_receipt", "failed_receipt", "missing_nldm", "changed_receipt_hash", "receipt_symlink",
                                  *writer.SOURCE_PATHS, writer.SSSOM, writer.BASELINE])
def test_completed_source_noop_requires_original_receipt_and_all_preimages(case, before, defect):
    root, evidence, log = case
    apply(case)
    if defect == "timestamps":
        revised = writer.propose_sources({p: before[p] for p in writer.OWNERS}, before[writer.LEDGER],
                                          before[writer.MEMBERSHIP], timestamp="2026-11-02T00:00:00+00:00")
        for p in writer.OWNERS:
            (root / p).write_bytes(revised[p])
    elif defect == "missing_receipt":
        log.unlink()
    elif defect == "receipt_symlink":
        competitor = log.with_name("competitor.json")
        log.rename(competitor)
        log.symlink_to(competitor)
    elif isinstance(defect, Path):
        backup = writer.backup_paths(log, (defect,))[defect]
        backup.write_bytes(backup.read_bytes() + b"changed preimage\n")
    else:
        receipt = json.loads(log.read_text())
        if defect == "failed_receipt":
            receipt["state"] = "failed"
        elif defect == "missing_nldm":
            receipt["records"] = receipt["records"][:2]
        else:
            receipt["output_sha256"][str(writer.SURVIVOR)] = "0" * 64
        log.write_text(json.dumps(receipt))
    snapshots = {p: (root / p).read_bytes() for p in before}
    evidence_before = {p: p.read_bytes() for p in log.parent.iterdir() if p.is_file()}
    with pytest.raises((ValueError, FileNotFoundError), match="receipt|preimage"):
        writer.apply_sources(root, evidence, log, apply=True)
    assert {p: (root / p).read_bytes() for p in before} == snapshots
    assert {p: p.read_bytes() for p in log.parent.iterdir() if p.is_file()} == evidence_before


@pytest.mark.parametrize("phase", ["sources", "promote"])
def test_input_drift_after_reservation_stops_native_commit(case, before, monkeypatch, phase):
    from kg_microbe_write.transaction import ValidationFailed
    root, evidence, source_log = case
    args = promoted_case(case, before) if phase == "promote" else None
    snapshots = {p: (root / p).read_bytes() for p in before}
    original = writer.guarded.reserve_receipt_outputs
    @contextmanager
    def race(*a, **kwargs):
        with original(*a, **kwargs) as handles:
            path = root / writer.LEDGER
            path.write_bytes(path.read_bytes() + b"concurrent input\n")
            yield handles
    monkeypatch.setattr(writer.guarded, "reserve_receipt_outputs", race)
    with pytest.raises((ValueError, ValidationFailed), match="frozen input changed"):
        if args:
            writer.promote(*args, apply=True)
        else:
            writer.apply_sources(root, evidence, source_log, apply=True)
    assert all((root / p).read_bytes() == b for p, b in snapshots.items() if p != writer.LEDGER)
    assert (root / writer.LEDGER).read_bytes().endswith(b"concurrent input\n")


def test_real_native_builder_emits_the_bounded_claims(case, before, monkeypatch):
    source_root = os.environ.get("CLAW_ROOT")
    if not source_root:
        pytest.skip("Native Claw producer source is not configured")
    path = Path(source_root) / "scripts/build_mim_ingredient_sssom.py"
    monkeypatch.syspath_prepend(str(path.parent))
    spec = importlib.util.spec_from_file_location("native_carnitine_sssom", path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    apply(case)
    root = case[0]
    rows = []
    for owner in writer.OWNERS:
        rows += native._row_from_yaml(root / owner, {}, {}, {}, {})
    expected = writer.table(candidate_for(root, before))[1]
    assert rows == expected
    fields = writer.table(before[writer.SSSOM])[0]
    candidate = tsv(fields, rows)
    result = writer.promoted_sssom(before[writer.SSSOM], candidate, {p: (root / p).read_bytes() for p in writer.OWNERS})
    assert len(writer.table(result)[1]) == len(writer.table(before[writer.SSSOM])[1]) - 4
