"""#1409: literal real-Git paths must reach the unchanged freshness proof."""

from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import identity_projection as projection
from mediaingredientmech import identity_projection_frozen as frozen
from mediaingredientmech.curie import mim_curie_for_stem
from tests.test_identity_projection import fixture as identity_fixture

_spec = importlib.util.spec_from_file_location(
    "unified_freshness_literal_paths",
    Path(__file__).resolve().parents[1] / "scripts/check_unified_freshness.py",
)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, check=True, timeout=30
    ).stdout


def write(repo, name, raw):
    path = repo / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


@pytest.fixture(params=["true", "false"], ids=["quoted", "unquoted"])
def repo(tmp_path, request):
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-q")
    git(root, "config", "user.name", "Fixture")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "config", "core.quotePath", request.param)
    return root


@pytest.mark.parametrize("tracked", [True, False], ids=["changed", "untracked"])
def test_literal_paths_reach_the_proof_for_both_git_commands(repo, monkeypatch, tracked):
    names = {
        "data/ingredients/mapped/L-α-phosphatidylinositol.yaml",
        "data/ingredients/mapped/Α-lipoic_Acid.yaml",
        "data/ingredients/unmapped/Poly-ß-hydroxybutyric_Acid.yaml",
        "data/ingredients/mapped/ space and trailing space .yaml",
        "data/ingredients/unmapped/line\nbreak.yaml",
        "data/ingredients/mapped/tab\tname.yaml",
        'data/ingredients/mapped/quote"name.yaml',
        "data/ingredients/unmapped/back\\slash.yaml",
    }
    write(repo, "seed.txt", b"seed\n")
    if tracked:
        for name in names:
            write(repo, name, b"before\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "literal path baseline")
    rev = git(repo, "rev-parse", "HEAD").decode().strip()
    for name in names:
        write(repo, name, b"after\n")
    # Inspect the boundary, then delegate to the unchanged native proof. This
    # fixture has no migration artifacts, so no path may be exempted.
    real_proof = frozen.eligible_identity_paths
    seen = []

    def inspect_paths(root, candidates, *, stamped_digest, stamped_count):
        assert set(candidates) == names
        seen.append(candidates)
        return real_proof(
            root, candidates, stamped_digest=stamped_digest, stamped_count=stamped_count
        )

    monkeypatch.setattr(frozen, "eligible_identity_paths", inspect_paths)
    assert gate.drift_since(
        rev, repo / "data/ingredients", repo, stamped_digest="0" * 64, stamped_count=0
    ) == len(names)
    assert len(seen) == 1


@pytest.fixture
def migrated_unicode(repo, monkeypatch):
    """Real Git baseline plus the complete native one-owner frozen proof.

    Only the fixed historical commit constant is bound to this private fixture;
    record/blob enumeration, migration verification and stamp matching are real.
    """
    manifest, before, after, old_name = identity_fixture()
    name = "data/ingredients/mapped/Water_α.yaml"
    legacy = mim_curie_for_stem(Path(name).stem)
    before[name] = before.pop(old_name)
    new = yaml.safe_load(after.pop(old_name))
    new["legacy_identifiers"] = [legacy, "CHEBI:15377"]
    after[name] = yaml.safe_dump(new).encode()
    before[projection.SOURCE] = before[projection.SOURCE].replace(
        b"MIM:Water\t", legacy.encode() + b"\t"
    )
    manifest["records"][0].update(
        path=name,
        legacy_identifiers=new["legacy_identifiers"],
        before_sha256=projection.sha(before[name]),
        after_sha256=projection.sha(after[name]),
    )
    manifest["before_sssom_sha256"] = projection.sha(before[projection.SOURCE])
    for path, raw in before.items():
        write(repo, path, raw)
    artifact = repo / "snapshot.tsv"
    artifact.write_text("name\tid\nWater\tCHEBI:15377\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "before administrative identity migration")
    rev = git(repo, "rev-parse", "HEAD").decode().strip()
    monkeypatch.setattr(projection, "BASE_COMMIT", rev)
    monkeypatch.setattr(frozen, "BASE_COMMIT", rev)
    manifest["source_commit"] = rev
    provenance = repo / "snapshot.provenance.json"
    stamp = gate.stamp(artifact, provenance, repo / "data/ingredients")
    stamp["mim_rev"] = rev
    provenance.write_text(json.dumps(stamp))
    proof = projection.Proof(
        None, manifest, before, after, {}, {projection.MANIFEST: projection.encode(manifest)}
    )
    for path, raw in {
        **after,
        projection.MANIFEST: projection.encode(manifest),
        **frozen.frozen_products(proof),
    }.items():
        write(repo, path, raw)
    return artifact, provenance, repo / "data/ingredients", repo, name, stamp


def test_unicode_postimage_exemption_preserves_the_default_drift_budget(migrated_unicode):
    artifact, provenance, inputs, repo, name, stamp = migrated_unicode

    def drift():
        return gate.drift_since(
            stamp["mim_rev"], inputs, repo,
            stamped_digest=stamp["mim_inputs_digest"], stamped_count=stamp["mim_record_count"],
        )

    assert drift() == 0  # Actual native frozen proof, no exemption stub.
    original_artifact, original_stamp = artifact.read_bytes(), provenance.read_bytes()
    with (repo / name).open("ab") as handle:
        handle.write(b"# later scientific curation\n")
    assert drift() == 1  # Same literal Unicode path, now genuinely non-exempt.
    for i in range(24):
        write(repo, f"data/ingredients/unmapped/new_ß_{i}\nrecord.yaml", b"new\n")
    assert drift() == 25
    assert gate.check(artifact, provenance, inputs, repo=repo) == []
    write(repo, "data/ingredients/unmapped/one_more_α.yaml", b"new\n")
    assert drift() == 26
    assert any("26 record files have changed" in p and "budget 25" in p
               for p in gate.check(artifact, provenance, inputs, repo=repo))
    assert artifact.read_bytes() == original_artifact
    assert provenance.read_bytes() == original_stamp


def test_deleted_unicode_postimage_is_genuine_drift(migrated_unicode):
    artifact, provenance, inputs, repo, name, stamp = migrated_unicode
    (repo / name).unlink()
    assert gate.drift_since(
        stamp["mim_rev"], inputs, repo,
        stamped_digest=stamp["mim_inputs_digest"], stamped_count=stamp["mim_record_count"],
    ) == 1
    assert any("1 record files have changed" in p
               for p in gate.check(artifact, provenance, inputs, max_drift=0, repo=repo))
