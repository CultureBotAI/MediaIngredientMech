"""#875 couples exact-form identity, rejection scope and auditable mapping changes."""

import csv
import importlib.util
import io
import json
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("heptahydrate_writer", ROOT / "scripts/promote_heptahydrate_ncit.py")
writer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writer)
FIELDS = ["subject_id", "subject_label", "predicate_id", "object_id", "object_label",
          "object_source", "mapping_justification", "source", "mapping_date", "confidence",
          "comment", "other", "validation_method"]


def tsv(rows, date="2026-08-27"):
    out = io.StringIO()
    out.write(f'# mapping_set_version: "{date}"\n# mapping_date: "{date}"\n')
    table = csv.DictWriter(out, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
    table.writeheader()
    for row in rows:
        table.writerow(dict.fromkeys(FIELDS, "") | row)
    return out.getvalue().encode()


class MemoryTransaction:
    """Dependency double; native integration runs separately when installed."""

    def __init__(self, root, validator, journal):
        self.root, self.validator, self.staged = root, validator, {}

    def stage(self, path, text):
        self.staged[self.root / path] = text

    def commit(self, apply=False):
        for path, text in self.staged.items():
            self.validator(path, text)
        if apply:
            for path, text in self.staged.items():
                path.write_text(text)
        return self

    def as_dict(self):
        return {"test_double": True, "changed": [str(p) for p in self.staged]}


@pytest.fixture
def case(tmp_path, monkeypatch):
    before = (ROOT / "tests/fixtures/issue875-owner-before.yaml").read_bytes()
    assert writer.digest(before) == writer.OWNER_BEFORE
    ledger = (
        "ingredient_name\trejected_id\tmim_id\treason\n"
        "Unrelated label\tCHEBI:999\t\tKeep exact source hold\n"
        f"{writer.NAME}\t{writer.PARENT}\t{writer.OLD}\t{writer.OLD_REASON}\n"
    ).encode()
    unrelated = {"subject_id": "MIM:Unrelated", "object_id": "CHEBI:1",
                 "predicate_id": "skos:exactMatch", "source": "must|stay", "mapping_date": "2026-08-27"}
    parent = {"subject_id": writer.SUBJECT, "subject_label": writer.NAME,
              "object_id": writer.PARENT, "predicate_id": "skos:closeMatch",
              "source": "MIM:old-curator|kgm:old-lineage", "mapping_date": "2026-08-27"}
    registry = parent | {"object_id": writer.OLD, "predicate_id": "skos:exactMatch",
                         "comment": "Obsolete registry explanation"}
    canonical = tsv([unrelated, parent, registry, unrelated | {"subject_id": "MIM:After"}])
    for rel, payload in {writer.OWNER: before, writer.LEDGER: ledger, writer.SSSOM: canonical,
                         writer.EVIDENCE: (ROOT / writer.EVIDENCE).read_bytes()}.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    monkeypatch.setattr(writer, "LEDGER_BEFORE", writer.digest(ledger))
    monkeypatch.setattr(writer, "SSSOM_BEFORE", writer.digest(canonical))
    monkeypatch.setattr(writer, "new_transaction", MemoryTransaction)
    return tmp_path, tmp_path / "evidence/apply.json", {
        writer.OWNER: before, writer.LEDGER: ledger, writer.SSSOM: canonical}


def candidate_for(root):
    record = yaml.safe_load((root / writer.OWNER).read_bytes())
    return tsv([{
        "subject_id": writer.SUBJECT, "subject_label": writer.NAME,
        "predicate_id": "skos:exactMatch", "object_id": writer.NEW,
        "object_label": writer.LABEL, "object_source": "obo:ncit.owl",
        "mapping_justification": "semapv:LexicalMatching", "confidence": "0.99",
        "source": "|".join([f"MIM:{e['source']}" for e in record["ontology_mapping"]["evidence"]] + ["MIM:curator=Codex"]),
        "mapping_date": record["curation_history"][-1]["timestamp"][:10],
        "other": "Na2HPO4.7H2O|Na2HPO4•7H2O|CAS:7782-85-6",
    }])


def test_sources_dry_run_is_nonmutating(case):
    root, log, before = case
    result = writer.apply_sources(root, log)
    assert result["changed"] and not result["applied"]
    assert {p: (root / p).read_bytes() for p in before} == before
    assert not log.parent.exists()


def test_sources_preserve_history_fields_and_coupled_scope(case):
    root, log, before = case
    result = writer.apply_sources(root, log, apply=True)
    old = yaml.safe_load(before[writer.OWNER])
    new = yaml.safe_load((root / writer.OWNER).read_bytes())
    assert new["identifier"] == new["ontology_mapping"]["ontology_id"] == writer.NEW
    assert new["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["curator"] == "Codex" and event["llm_assisted"] is True and event["llm_model"] == "gpt-6"
    assert new["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"]
    for key in old.keys() - {"identifier", "ontology_mapping", "curation_history"}:
        assert old[key] == new[key], key
    ledger = (root / writer.LEDGER).read_bytes()
    assert ledger.splitlines()[:2] == before[writer.LEDGER].splitlines()[:2]
    assert f"{writer.NAME}\t{writer.PARENT}\t{writer.NEW}\t".encode() in ledger
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]
    assert result["approval"].startswith("NONE")
    saved = json.loads(log.read_text())
    assert saved["state"] == "complete" and saved["applied"]
    assert saved["records"][0]["after_yaml_sha256"] == writer.digest((root / writer.OWNER).read_bytes())
    assert log.with_suffix(".before.yaml").read_bytes() == before[writer.OWNER]
    assert log.with_suffix(".before-ledger.tsv").read_bytes() == before[writer.LEDGER]
    assert log.with_suffix(".before.sssom.tsv").read_bytes() == before[writer.SSSOM]


def test_source_repeat_is_a_true_noop(case):
    root, log, _ = case
    writer.apply_sources(root, log, apply=True)
    snapshots = {p: (root / p).read_bytes() for p in (writer.OWNER, writer.LEDGER)}
    receipt = log.read_bytes()
    assert writer.apply_sources(root, log, apply=True)["changed"] is False
    assert {p: (root / p).read_bytes() for p in snapshots} == snapshots
    assert log.read_bytes() == receipt


@pytest.mark.parametrize("phase", ["owner", "ledger"])
def test_partial_source_migration_refuses(case, phase):
    root, log, before = case
    path, payload = ((writer.OWNER, writer.corrected_record(before[writer.OWNER])) if phase == "owner"
                     else (writer.LEDGER, writer.corrected_ledger(before[writer.LEDGER])))
    (root / path).write_bytes(payload)
    with pytest.raises(ValueError, match="migrate together"):
        writer.apply_sources(root, log, apply=True)
    assert not log.exists()


@pytest.mark.parametrize("suffix", [None, ".before.yaml", ".before-ledger.tsv", ".before.sssom.tsv"])
@pytest.mark.parametrize("symlink", [False, True])
def test_receipt_collisions_preserve_all_sources(case, suffix, symlink):
    root, log, before = case
    occupied = log if suffix is None else log.with_suffix(suffix)
    occupied.parent.mkdir()
    if symlink:
        victim = root / "victim"
        victim.write_bytes(b"existing evidence")
        occupied.symlink_to(victim)
    else:
        occupied.write_bytes(b"existing evidence")
    with pytest.raises(FileExistsError):
        writer.apply_sources(root, log, apply=True)
    assert occupied.read_bytes() == b"existing evidence"
    assert {p: (root / p).read_bytes() for p in before} == before


@pytest.mark.parametrize("path", [writer.OWNER, writer.LEDGER, writer.SSSOM, writer.EVIDENCE])
def test_changed_input_refuses_before_apply(case, path):
    root, log, before = case
    (root / path).write_bytes((root / path).read_bytes() + b"\n")
    with pytest.raises(ValueError):
        writer.apply_sources(root, log, apply=True)
    assert not log.exists()
    assert all((root / p).read_bytes() == b for p, b in before.items() if p != path)


def test_ignored_nested_destination_owner_refuses(case):
    root, log, before = case
    path = root / "data/ingredients/.ignored-backups/owner.yaml"
    path.parent.mkdir()
    path.write_text("identifier: NCIT:C61946\n")
    with pytest.raises(ValueError, match="already held"):
        writer.apply_sources(root, log, apply=True)
    assert (root / writer.OWNER).read_bytes() == before[writer.OWNER]


def test_input_race_after_reservation_refuses(case, monkeypatch):
    root, log, before = case
    original = writer.reserve_receipt_outputs

    @contextmanager
    def race(*args, **kwargs):
        with original(*args, **kwargs) as handles:
            (root / writer.LEDGER).write_bytes(before[writer.LEDGER] + b"concurrent change\n")
            yield handles
    monkeypatch.setattr(writer, "reserve_receipt_outputs", race)
    with pytest.raises(ValueError, match="frozen input changed"):
        writer.apply_sources(root, log, apply=True)
    assert (root / writer.OWNER).read_bytes() == before[writer.OWNER]
    assert (root / writer.LEDGER).read_bytes().endswith(b"concurrent change\n")


def test_changed_content_cannot_hide_in_a_completed_correction(case):
    root, log, _ = case
    writer.apply_sources(root, log, apply=True)
    record = yaml.safe_load((root / writer.OWNER).read_bytes())
    record["chemical_properties"]["cas_rn"] = "7558-79-4"
    with pytest.raises(ValueError, match="unreviewed owner content"):
        writer.corrected_record(writer.render(record))


def test_invalid_prior_correction_timestamp_is_not_a_noop(case):
    root, log, _ = case
    writer.apply_sources(root, log, apply=True)
    record = yaml.safe_load((root / writer.OWNER).read_bytes())
    record["curation_history"][-1]["timestamp"] = "not a date"
    with pytest.raises(ValueError, match="timestamp"):
        writer.corrected_record(yaml.safe_dump(record, sort_keys=False).encode())


def test_schema_failure_writes_neither_source(case, monkeypatch):
    root, log, before = case

    def refuse(*args, **kwargs):
        raise ValueError("simulated native schema refusal")
    monkeypatch.setattr(writer, "write_validated_ingredient", refuse)
    with pytest.raises(ValueError, match="schema refusal"):
        writer.apply_sources(root, log, apply=True)
    assert {p: (root / p).read_bytes() for p in before} == before
    assert not log.exists()


def test_same_destination_grounding_on_another_identity_refuses(case):
    root, log, before = case
    (root / "data/ingredients/mapped/Other.yaml").write_text(
        "identifier: cas:7782-85-6\nmapping_status: MAPPED\n"
        "ontology_mapping:\n  ontology_id: NCIT:C61946\n")
    with pytest.raises(ValueError, match="already held"):
        writer.apply_sources(root, log, apply=True)
    assert (root / writer.OWNER).read_bytes() == before[writer.OWNER]


def test_native_candidate_promotion_preserves_other_rows_and_source_lineage(case):
    root, log, before = case
    writer.apply_sources(root, log, apply=True)
    candidate = root / "candidate.tsv"
    candidate.write_bytes(candidate_for(root))
    promotion_log = log.with_name("promotion.json")
    report = writer.promote(root, promotion_log, log, candidate, writer.digest(candidate.read_bytes()), apply=True)
    _, rows = writer.table((root / writer.SSSOM).read_bytes())
    target = [r for r in rows if r["subject_id"] == writer.SUBJECT]
    assert len(target) == 1 and target[0]["object_id"] == writer.NEW
    assert target[0]["predicate_id"] == "skos:exactMatch" and target[0]["validation_method"] == ""
    assert "MIM:old-curator|kgm:old-lineage" in target[0]["source"]
    assert "MIM:curator=Codex" in target[0]["source"] and writer.URL in target[0]["source"]
    assert report["approval"].startswith("NONE")
    assert report["changed_rows"] == report["removed_rows"] == 1
    assert [r for r in rows if r["subject_id"] != writer.SUBJECT] == [
        r for r in writer.table(before[writer.SSSOM])[1] if r["subject_id"] != writer.SUBJECT]
    for line in before[writer.SSSOM].splitlines(keepends=True):
        if line.startswith((b"MIM:Unrelated\t", b"MIM:After\t")):
            assert line in (root / writer.SSSOM).read_bytes()
    date = target[0]["mapping_date"]
    assert f'# mapping_set_version: "{date}"'.encode() in (root / writer.SSSOM).read_bytes()
    saved = promotion_log.read_bytes()
    assert writer.promote(root, promotion_log, log, candidate, writer.digest(candidate.read_bytes()), apply=True)["changed"] is False
    assert promotion_log.read_bytes() == saved


@pytest.mark.parametrize("field,value", [
    ("predicate_id", "skos:closeMatch"), ("object_id", writer.PARENT),
    ("object_label", "disodium hydrogenphosphate"), ("object_source", "obo:chebi.owl"),
    ("validation_method", "OAK+OLS:chebi|CONFIRMED|2026-07-07"),
    ("other", "Na2HPO4 x 2 H2O"), ("mapping_date", "2026-08-27"),
    ("source", "MIM:curator=Codex"), ("confidence", "0.9"),
])
def test_unreviewed_candidate_payload_is_refused(case, field, value):
    root, log, before = case
    writer.apply_sources(root, log, apply=True)
    rows = writer.table(candidate_for(root))[1]
    rows[0][field] = value
    with pytest.raises(ValueError):
        writer.promoted_sssom(before[writer.SSSOM], tsv(rows), (root / writer.OWNER).read_bytes())


def test_candidate_hash_and_source_receipt_are_required(case):
    root, log, before = case
    writer.apply_sources(root, log, apply=True)
    candidate = root / "candidate.tsv"
    candidate.write_bytes(candidate_for(root))
    with pytest.raises(ValueError, match="candidate hash changed"):
        writer.promote(root, log.with_name("promote.json"), log, candidate, "wrong", apply=True)
    source = json.loads(log.read_text())
    source["records"][0]["after_yaml_sha256"] = "stale"
    log.write_text(json.dumps(source))
    with pytest.raises(ValueError, match="does not bind"):
        writer.promote(root, log.with_name("promote.json"), log, candidate, writer.digest(candidate.read_bytes()), apply=True)
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]


def test_native_transaction_integration_when_claw_available(case, monkeypatch):
    native = pytest.importorskip("kg_microbe_write")
    root, log, _ = case
    monkeypatch.setattr(writer, "new_transaction", lambda root, validator, journal: native.ValidatedWriteTransaction(root, validator=validator, journal_dir=journal))
    result = writer.apply_sources(root, log, apply=True)
    journal = json.loads(Path(result["transaction"]["journal"]).read_text())
    assert journal["status"] == "complete"
    assert set(journal["changed"]) == {str(root / writer.OWNER), str(root / writer.LEDGER)}


@pytest.mark.parametrize("phase", ["sources", "promote"])
def test_valid_competing_owner_after_reservation_blocks_original_paths(case, monkeypatch, phase):
    """#1033: every publishing path rechecks the exact destination owner."""
    native = pytest.importorskip("kg_microbe_write")
    root, source_log, _ = case
    monkeypatch.setattr(writer, "new_transaction", lambda root, validator, journal: native.ValidatedWriteTransaction(
        root, validator=validator, journal_dir=journal))
    if phase == "promote":
        writer.apply_sources(root, source_log, apply=True)
        candidate = root / "candidate.tsv"
        candidate.write_bytes(candidate_for(root))
        log = source_log.with_name("promotion.json")

        def apply():
            return writer.promote(root, log, source_log, candidate, writer.digest(candidate.read_bytes()), apply=True)
    else:
        log = source_log

        def apply():
            return writer.apply_sources(root, log, apply=True)

    before = {p: (root / p).read_bytes() for p in (writer.OWNER, writer.LEDGER, writer.SSSOM)}
    corrected = yaml.safe_load(writer.corrected_record(before[writer.OWNER]))
    corrected["preferred_term"] = "Competing phosphate heptahydrate owner"
    validated = writer.render(corrected)
    competitor = root / "data/ingredients/mapped/.ignored-backup/competing.yaml"
    original = writer.reserve_receipt_outputs

    @contextmanager
    def reserve(*args, **kwargs):
        with original(*args, **kwargs) as handles:
            competitor.parent.mkdir()
            competitor.write_bytes(validated)
            yield handles

    monkeypatch.setattr(writer, "reserve_receipt_outputs", reserve)
    with pytest.raises(native.ValidationFailed, match="Destination identity already held"):
        apply()
    assert competitor.read_bytes() == validated
    assert {p: (root / p).read_bytes() for p in before} == before
    receipt = json.loads(log.read_text())
    assert receipt["state"] == "failed" and receipt["applied"] is not True
    backups = ({".before.yaml": writer.OWNER, ".before-ledger.tsv": writer.LEDGER,
                ".before.sssom.tsv": writer.SSSOM} if phase == "sources" else {".before.tsv": writer.SSSOM})
    for suffix, path in backups.items():
        assert log.with_suffix(suffix).read_bytes() == before[path]
    assert not list((log.parent / f"{log.stem}-journal").glob("write-*.json"))


@pytest.mark.parametrize("completed", [False, True])
def test_promotion_refuses_preexisting_valid_competing_owner(case, monkeypatch, completed):
    """A completed-byte no-op also must not hide a competing active identity."""
    native = pytest.importorskip("kg_microbe_write")
    root, source_log, _ = case
    monkeypatch.setattr(writer, "new_transaction", lambda root, validator, journal: native.ValidatedWriteTransaction(
        root, validator=validator, journal_dir=journal))
    writer.apply_sources(root, source_log, apply=True)
    candidate = root / "candidate.tsv"
    candidate.write_bytes(candidate_for(root))
    if completed:
        writer.promote(root, source_log.with_name("first-promotion.json"), source_log,
                       candidate, writer.digest(candidate.read_bytes()), apply=True)
    before = {p: (root / p).read_bytes() for p in (writer.OWNER, writer.LEDGER, writer.SSSOM)}
    competitor = root / "data/ingredients/mapped/.ignored-backup/competing.yaml"
    competitor.parent.mkdir()
    validated = writer.render(yaml.safe_load(before[writer.OWNER]))
    competitor.write_bytes(validated)
    log = source_log.with_name("conflicted-promotion.json")
    with pytest.raises(ValueError, match="Destination identity already held"):
        writer.promote(root, log, source_log, candidate, writer.digest(candidate.read_bytes()), apply=True)
    assert competitor.read_bytes() == validated
    assert {p: (root / p).read_bytes() for p in before} == before
    assert not log.exists()


@pytest.mark.parametrize("phase,suffix", [
    ("sources", None), ("sources", ".before.yaml"),
    ("sources", ".before-ledger.tsv"), ("sources", ".before.sssom.tsv"),
    ("promote", None), ("promote", ".before.tsv"),
])
@pytest.mark.parametrize("symlink", [False, True])
@pytest.mark.parametrize("timing", ["reserved", "prepared", "after_commit", "completion"])
def test_reserved_evidence_replacement_refuses_with_native_transaction(
        case, monkeypatch, phase, suffix, symlink, timing):
    """#1029: no success with lost receipt/backup; never erase competing bytes."""
    native = pytest.importorskip("kg_microbe_write")
    root, source_log, _ = case
    native_factory = lambda root, validator, journal: native.ValidatedWriteTransaction(  # noqa: E731
        root, validator=validator, journal_dir=journal)
    monkeypatch.setattr(writer, "new_transaction", native_factory)
    if phase == "promote":
        writer.apply_sources(root, source_log, apply=True)
        candidate = root / "candidate.tsv"
        candidate.write_bytes(candidate_for(root))
        log = source_log.with_name("promotion.json")

        def apply():
            return writer.promote(root, log, source_log, candidate,
                                  writer.digest(candidate.read_bytes()), apply=True)
    else:
        log = source_log

        def apply():
            return writer.apply_sources(root, log, apply=True)

    before = {path: (root / path).read_bytes() for path in (writer.OWNER, writer.LEDGER, writer.SSSOM)}
    replaced = log if suffix is None else log.with_suffix(suffix)
    competitor = b"competing evidence must survive\n"
    victim = root / "competing-writer-evidence"
    victim.write_bytes(competitor)
    did_replace = False

    def replace():
        nonlocal did_replace
        assert not did_replace
        replaced.unlink()
        if symlink:
            replaced.symlink_to(victim)
        else:
            replaced.write_bytes(competitor)
        did_replace = True

    original_reserve = writer.reserve_receipt_outputs

    class ReceiptProxy:
        def __init__(self, handle):
            self.handle = handle

        def __getattr__(self, name):
            return getattr(self.handle, name)

        def write(self, text):
            result = self.handle.write(text)
            state = json.loads(text).get("state")
            if (timing == "prepared" and state == "prepared"
                    or timing == "completion" and state == "complete"):
                replace()
            return result

    @contextmanager
    def reserve(*args, **kwargs):
        with original_reserve(*args, **kwargs) as handles:
            if timing == "reserved":
                replace()
            yield (ReceiptProxy(handles[0]), *handles[1:])

    class RacingTransaction(native.ValidatedWriteTransaction):
        def commit(self, *, apply=False):
            result = super().commit(apply=apply)
            if apply and timing == "after_commit":
                replace()
            return result

    monkeypatch.setattr(writer, "reserve_receipt_outputs", reserve)
    monkeypatch.setattr(writer, "new_transaction", lambda root, validator, journal: RacingTransaction(
        root, validator=validator, journal_dir=journal))
    with pytest.raises(ValueError, match="Reserved evidence output was replaced or removed"):
        apply()
    assert did_replace
    assert replaced.is_symlink() is symlink
    assert replaced.read_bytes() == victim.read_bytes() == competitor
    applied = timing in {"after_commit", "completion"}
    assert any((root / path).read_bytes() != data for path, data in before.items()) is applied
    if not applied:
        assert all((root / path).read_bytes() == data for path, data in before.items())
    if suffix is not None:
        receipt = json.loads(log.read_text())
        assert receipt["state"] == "failed" and receipt["applied"] is applied
    journals = list((log.parent / f"{log.stem}-journal").glob("write-*.json"))
    assert len(journals) == int(applied)
    if applied:
        journal = json.loads(journals[0].read_text())
        assert journal["status"] == "complete"
        for path, data in before.items():
            if str(root / path) in journal["previous"]:
                assert journal["previous"][str(root / path)].encode() == data


def test_issue875_committed_surfaces_use_exact_ncit_identity():
    """Becomes green only after root applies, synchronizes and regenerates."""
    record = yaml.safe_load((ROOT / writer.OWNER).read_bytes())
    before = yaml.safe_load((ROOT / "tests/fixtures/issue875-owner-before.yaml").read_bytes())
    assert record["identifier"] == record["ontology_mapping"]["ontology_id"] == writer.NEW
    assert record["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert record["curation_history"][:-1] == before["curation_history"]
    assert record["chemical_properties"] == before["chemical_properties"]
    assert record["physicochemical_roles"] == before["physicochemical_roles"]
    ledger = list(csv.DictReader((ROOT / writer.LEDGER).open(), delimiter="\t"))
    held = [r for r in ledger if r["ingredient_name"] == writer.NAME]
    assert len(held) == 1 and held[0]["mim_id"] == writer.NEW and held[0]["rejected_id"] == writer.PARENT
    _, mappings = writer.table((ROOT / writer.SSSOM).read_bytes())
    target = [r for r in mappings if r["subject_id"] == writer.SUBJECT]
    assert len(target) == 1
    assert (target[0]["predicate_id"], target[0]["object_id"]) == ("skos:exactMatch", writer.NEW)
    assert target[0]["validation_method"] == ""
    rows = {r["ingredient_name"]: r for r in csv.DictReader(
        (ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv").open(), delimiter="\t")}
    for name in ("Na2HPO4 x 7 H2O", "Na2HPO4.7H2O", "Na2HPO4·7H2O"):
        row = rows[name]
        assert row["mim_id"] == writer.NEW and row["mapping_status"] == "MAPPED", name
        assert row["chebi_id"] == "" and row["culturemech_term_id"] != writer.PARENT, name
        assert row["cas_rn"] == "7782-85-6" and row["kg_microbe_node_id"] == "", name
        assert int(row["occurrence_count"]) > 0 and row["example_media"], name
