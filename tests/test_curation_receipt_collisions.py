"""An existing curation receipt or backup must prevent any owner mutation (#1006)."""

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def apply_case(tmp_path, monkeypatch):
    name = "reject_carnitinamide_synonym"
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    record = {
        "identifier": "kgmicrobe.compound:carnitine_hydrochloride",
        "preferred_term": "Carnitine Hydrochloride", "mapping_status": "MAPPED",
        "ontology_mapping": {"ontology_id": "CHEBI:17126", "ontology_label": "carnitine",
                             "ontology_source": "CHEBI", "mapping_quality": "NARROW_MATCH"},
        "synonyms": [{"synonym_text": module.ALIAS, "synonym_type": "EXACT_SYNONYM",
                      "source": "chebi_synonym_review"}],
    }
    before = yaml.safe_dump(record, sort_keys=False).encode()
    source = tmp_path / module.RECORD
    source.parent.mkdir(parents=True)
    source.write_bytes(before)
    log = tmp_path / "receipts" / "apply.json"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "BEFORE_SHA256", hashlib.sha256(before).hexdigest())
    monkeypatch.setattr(sys, "argv", [name, "--apply", "--log", str(log)])
    return module, source, before, log


@pytest.mark.parametrize("existing", ["receipt", "backup", "both"])
def test_existing_evidence_refuses_before_owner_write(apply_case, existing):
    module, source, before, log = apply_case
    backup = log.with_suffix(".before.yaml")
    log.parent.mkdir()
    occupied = {"receipt": [log], "backup": [backup], "both": [log, backup]}[existing]
    for path in occupied:
        path.write_bytes(b"original evidence must survive\n")
    with pytest.raises(FileExistsError):
        module.main()
    assert source.read_bytes() == before
    for path in occupied:
        assert path.read_bytes() == b"original evidence must survive\n"
    for path in {log, backup} - set(occupied):
        assert not path.exists()


def test_success_retains_original_backup_and_binds_written_owner(apply_case):
    module, source, before, log = apply_case
    assert module.main() == 0
    assert source.read_bytes() != before
    assert log.with_suffix(".before.yaml").read_bytes() == before
    receipt = json.loads(log.read_text())["records"][0]
    assert receipt["before_yaml_sha256"] == hashlib.sha256(before).hexdigest()
    assert receipt["after_yaml_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
