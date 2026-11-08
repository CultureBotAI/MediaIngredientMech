"""#1265 freshness exemption never hides prior drift or later scientific edits."""
import base64
import gzip

import pytest

from mediaingredientmech import identity_projection as ip
from mediaingredientmech import identity_projection_frozen as frozen
from tests.test_identity_projection import fixture


def frozen_fixture():
    manifest, before, after, name = fixture()
    proof = ip.Proof(None, manifest, before, after, {}, {ip.MANIFEST: ip.encode(manifest)})
    raw = frozen.frozen_products(proof)[frozen.FROZEN]
    return manifest, before, after, name, raw


def test_frozen_initial_transition_independent_of_subsequent_current_edits():
    manifest, before, after, name, raw = frozen_fixture()
    preserved, transition = frozen.decode_frozen(ip.encode(manifest), before, raw)
    assert preserved == after
    assert transition["owners"] == {"MIM:0000001": name}
    assert frozen.identity_only_matches(before, after, {name: after[name]}, {name: before[name]}) == {name}
    assert frozen.identity_only_matches(before, after, {name: after[name] + b"# later curation\n"}, {name: before[name]}) == set()
    assert frozen.identity_only_matches(before, after, {name: after[name]}, {name: before[name] + b"# prior stale scientific drift\n"}) == set()
    assert frozen.identity_only_matches(before, after, {name: after[name]}, {}) == set()
    assert frozen.identity_only_matches(before, after, {}, {name: before[name]}) == set()


@pytest.mark.parametrize("attack", ["biology", "missing", "authority"])
def test_rehashed_frozen_archive_cannot_hide_scientific_or_scope_changes(attack):
    manifest, before, after, name, raw = frozen_fixture()
    archive = ip.document(gzip.decompress(raw))
    if attack == "biology":
        after[name] = after[name].replace(b"CHEBI:15377", b"CHEBI:99999")
        manifest["records"][0]["after_sha256"] = ip.sha(after[name])
        archive["files"][name] = base64.b64encode(after[name]).decode()
        archive["manifest_sha256"] = ip.sha(ip.encode(manifest))
    elif attack == "missing":
        del archive["files"][name]
    else:
        archive["source_commit"] = "a" * 40
    with pytest.raises(ValueError):
        frozen.decode_frozen(ip.encode(manifest), before, gzip.compress(ip.encode(archive), mtime=0))


def test_actual_stamp_digest_is_required_even_when_revision_matches():
    manifest, before, after, name, raw = frozen_fixture()
    actual_stamp = dict(before)
    actual_stamp[name] = before[name].replace(b'CHEBI:15377', b'CHEBI:99999')
    digest, count = frozen.input_snapshot_digest(actual_stamp)
    assert frozen.stamped_snapshot(before, after, digest, count) is None
    before_digest, before_count = frozen.input_snapshot_digest(before)
    assert frozen.stamped_snapshot(before, after, before_digest, before_count) == before
    assert frozen.stamped_snapshot(before, after, before_digest, before_count + 1) is None
    after_digest, after_count = frozen.input_snapshot_digest(after)
    assert frozen.stamped_snapshot(before, after, after_digest, after_count) == after
    assert frozen.identity_only_matches(before, after, {name: after[name]}, after) == {name}


def test_snapshot_digest_agrees_with_native_stamper(tmp_path):
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location('freshness_digest_test', Path(__file__).resolve().parents[1] / 'scripts/check_unified_freshness.py')
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    _, before, _, _, _ = frozen_fixture()
    for name, raw in before.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    assert frozen.input_snapshot_digest(before) == gate.inputs_digest(tmp_path / 'data/ingredients')


def test_exemption_wrapper_refuses_a_different_actual_stamped_snapshot(tmp_path, monkeypatch):
    manifest, before, after, name, raw = frozen_fixture()
    for path, content in {**after, ip.MANIFEST: ip.encode(manifest), frozen.FROZEN: raw}.items():
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    monkeypatch.setattr(frozen, 'record_paths', lambda root, historical=False: [name])
    monkeypatch.setattr(frozen, 'git_files', lambda root, names: before)
    actual_stamp = dict(before)
    actual_stamp[name] = before[name].replace(b'CHEBI:15377', b'CHEBI:99999')
    digest, count = frozen.input_snapshot_digest(actual_stamp)
    assert frozen.eligible_identity_paths(tmp_path, [name], stamped_digest=digest, stamped_count=count) == set()
    digest, count = frozen.input_snapshot_digest(before)
    assert frozen.eligible_identity_paths(tmp_path, [name], stamped_digest=digest, stamped_count=count) == {name}
