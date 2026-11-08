"""Synthetic failure controls for the worker's isolated validation wrapper."""
import hashlib
import importlib.util
import json
from pathlib import Path
import pytest
import yaml

spec = importlib.util.spec_from_file_location('worker_validator', Path(__file__).with_name('validate_proposals.py'))
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def fixture(tmp_path, monkeypatch, record, *, existing=None):
    root = tmp_path / 'repo'
    out = root / 'reports/worker'
    out.mkdir(parents=True)
    target = 'data/ingredients/mapped/example.yaml'
    path = root / target
    path.parent.mkdir(parents=True)
    before = None
    if existing is not None:
        path.write_text(yaml.safe_dump(existing))
        before = hashlib.sha256(path.read_bytes()).hexdigest()
    payload = out / 'after.yaml'
    payload.write_text(yaml.safe_dump(record))
    proposal = {'proposal_id': 'synthetic', 'kind': 'edit_existing_owner' if existing else 'new_owner',
                'owner_path': target, 'before_sha256': before,
                'after_capture': {'path': 'after.yaml', 'sha256': hashlib.sha256(payload.read_bytes()).hexdigest()}}
    (out / 'proposals.json').write_text(json.dumps({'proposals': [proposal]}))
    monkeypatch.setattr(validator, 'ROOT', root)
    monkeypatch.setattr(validator, 'OUT', out)
    return root


def record():
    return {'identifier': 'kgmicrobe.ingredient:synthetic', 'preferred_term': 'Synthetic fixture',
            'mapping_status': 'UNMAPPED', 'ingredient_type': 'STOCK_SOLUTION',
            'curation_history': [{'timestamp': '2026-11-08T00:00:00Z', 'curator': 'synthetic test',
                                  'action': 'CREATED', 'changes': 'Synthetic test only.', 'llm_assisted': False}]}


def test_valid_fixture(tmp_path, monkeypatch):
    fixture(tmp_path, monkeypatch, record())
    assert validator.main() == 0


def test_unknown_field_fails(tmp_path, monkeypatch):
    r = record()
    r['unsupported_field'] = True
    fixture(tmp_path, monkeypatch, r)
    assert validator.main() == 1


def test_duplicate_identity_fails(tmp_path, monkeypatch):
    r = record()
    root = fixture(tmp_path, monkeypatch, r)
    (root / 'data/ingredients/mapped/another.yaml').write_text(yaml.safe_dump(r))
    assert validator.main() == 1


def test_rejected_owner_is_not_an_active_identity_collision(tmp_path, monkeypatch):
    r = record()
    r['mapping_status'] = 'REJECTED'
    root = fixture(tmp_path, monkeypatch, r)
    (root / 'data/ingredients/mapped/another.yaml').write_text(yaml.safe_dump(record()))
    assert validator.main() == 0


def test_history_cannot_be_silently_replaced(tmp_path, monkeypatch):
    fixture(tmp_path, monkeypatch, record(), existing=record())
    with pytest.raises(AssertionError, match='history not appended'):
        validator.main()


def test_self_component_fails(tmp_path, monkeypatch):
    r = record()
    r['components'] = [{'component_name': r['preferred_term'], 'component_id': r['identifier'], 'reference_scope': 'MIM_CATALOG'}]
    r['component_assertion'] = {'method': 'RECIPE_TRANSCRIPTION', 'completeness': 'COMPLETE',
                               'evidence': [{'evidence_type': 'RECIPE_SOURCE', 'source': 'synthetic fixture'}]}
    fixture(tmp_path, monkeypatch, r)
    assert validator.main() == 1
