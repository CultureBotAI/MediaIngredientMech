"""#1325 keeps historical proof and current ordinary science separate.

Small fixture judgments are explicitly synthetic. Two integration cases invoke
the real complete historical checker; bounded unit cases stub only that already
covered subprocess, never current mapping/companion admission.
"""

import json
import subprocess
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import identity_projection as projection
from mediaingredientmech.export import reviewed_sssom
from mediaingredientmech.ingredient_bundle_contract import stable_id
from mediaingredientmech.validation import reviewed_export_route as route
from tests.test_reviewed_sssom import reviewed_fixture, write_json

ROOT = Path(__file__).resolve().parents[1]


def git(root, *args):
    return (
        subprocess.check_output(
            ["git", "--no-optional-locks", *args], cwd=root, stderr=subprocess.PIPE
        )
        .decode()
        .strip()
    )


def commit(root):
    git(
        root,
        "-c",
        "user.name=Synthetic fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "add",
        ".",
    )
    git(
        root,
        "-c",
        "user.name=Synthetic fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "commit",
        "-m",
        "Explicit synthetic routing test",
    )
    return git(root, "rev-parse", "HEAD")


@pytest.fixture
def current(tmp_path):
    root = tmp_path / "current"
    root.mkdir()
    root, review_path, _ = reviewed_fixture.__wrapped__(root)
    review = json.loads(review_path.read_text())
    metadata, fields, rows = reviewed_sssom.read_sssom(root / "source.sssom.tsv")
    metadata["curie_map"][
        "MIM"
    ] = "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_"
    metadata["curie_map"]["skos"] = "http://www.w3.org/2004/02/skos/core#"
    metadata["curie_map"]["semapv"] = "https://w3id.org/semapv/vocab/"
    fields.append("mapping_justification")
    evidence = json.loads((root / "evidence.json").read_text())
    for i, (row, decision) in enumerate(zip(rows, review["decisions"], strict=True), 1):
        row["mapping_justification"] = "semapv:ManualMappingCuration"
        owner = decision["owner_record"]
        record = yaml.safe_load((root / owner).read_text())
        record["mim_id"] = row["subject_id"] = f"MIM:{i:07d}"
        (root / owner).write_text(yaml.safe_dump(record))
        review["record_inputs"][owner] = reviewed_sssom.digest(root / owner)
        decision["row_sha256"] = reviewed_sssom.row_sha256(row)
        evidence["entries"][str(i)].update(
            row_sha256=decision["row_sha256"], owner_record_sha256=review["record_inputs"][owner]
        )
    source = root / projection.SOURCE
    source.parent.mkdir()
    source.write_bytes(
        "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines()).encode()
        + reviewed_sssom._tsv(fields, rows)
    )
    write_json(root / "evidence.json", evidence)
    review.update(source_sssom=projection.SOURCE, source_sha256=reviewed_sssom.digest(source))
    review["inputs"]["evidence.json"] = reviewed_sssom.digest(root / "evidence.json")
    write_json(review_path, review)
    (root / "scope-evidence.txt").write_text(
        "Synthetic scope fixture, not real chemical approval.\n"
    )
    payload = dict(
        rows[0],
        ext_subject_scope="mimscope:defined_substance",
        ext_object_scope="mimscope:defined_substance",
        ext_subject_composition="mimscope:single_component",
        ext_object_composition="mimscope:single_component",
        ext_scope_profile="mimprofile:ingredient-scope/v1",
        ext_scope_review_status="SUPPORTED",
        ext_identity_authorized="true",
        ext_scope_evidence="sha256:" + reviewed_sssom.digest(root / "scope-evidence.txt"),
    )
    owner = review["decisions"][0]["owner_record"]
    claim = {
        "claim_id": stable_id(
            "mapping", [payload[x] for x in ("subject_id", "predicate_id", "object_id")]
        ),
        "kind": "mapping",
        "owner_record": owner,
        "payload": payload,
    }
    decision = {
        "claim_id": claim["claim_id"],
        "row_sha256": reviewed_sssom.row_sha256(claim),
        "owner_record": owner,
        "disposition": "SUPPORTED",
        "review_reason": "Synthetic current scope judgment",
        "review_evidence": "scope-proof.json",
        "evidence_key": "scope",
    }
    proof = {
        key: decision[key] for key in ("row_sha256", "owner_record", "disposition", "review_reason")
    }
    proof["owner_record_sha256"] = review["record_inputs"][owner]
    write_json(root / "scope-proof.json", {"entries": {"scope": proof}})
    write_json(root / "claims.json", {"schema_version": 1, "claims": [claim]})
    companion = {
        "schema_version": 1,
        "base_review": "review.json",
        "base_review_sha256": reviewed_sssom.digest(review_path),
        "claims_file": "claims.json",
        "claims_sha256": reviewed_sssom.digest(root / "claims.json"),
        "record_inputs": {owner: review["record_inputs"][owner]},
        "decisions": [decision],
        "inputs": {
            name: reviewed_sssom.digest(root / name)
            for name in (
                projection.SOURCE,
                "evidence.json",
                "scope-proof.json",
                "scope-evidence.txt",
            )
        },
    }
    write_json(root / "companion.json", companion)
    return root


@pytest.fixture
def history(tmp_path):
    root = tmp_path / "historical"
    root.mkdir()
    git(root, "init")
    (root / "retained.txt").write_text("Explicit test-only Git bytes, not a migration proof.\n")
    return root, commit(root)


@pytest.fixture
def native_unit(monkeypatch):
    calls = []

    def checked(root):
        calls.append(root)
        return {"checked": True, "scientific_approval_added": False}

    monkeypatch.setattr(route, "_projection_check", checked)
    return calls


def ordinary(current, history):
    return route.check_route(
        current,
        Path("review.json"),
        companion_review=Path("companion.json"),
        route="ordinary",
        historical_root=history[0],
        historical_revision=history[1],
    )


def test_ordinary_checks_complete_current_native_partitions(current, history, native_unit):
    result = ordinary(current, history)
    assert result["source_rows"] == 2
    assert result["companion_counts"] == {
        "mappings": 1,
        "identifiers": 0,
        "products": 0,
        "occurrences": 0,
    }
    assert result["production_authorized"] is result["scientific_approval_added"] is False
    assert native_unit == [history[0]]
    loaded = reviewed_sssom.load_review(current, current / "review.json")
    assert [d["disposition"] for d in loaded["decisions"]] == ["SUPPORTED", "WITHHOLD"]
    assert not (current / "output").exists()


def test_1326_later_companion_hash_cannot_replace_mapping_snapshot(
    current, history, native_unit, monkeypatch
):
    original_load = reviewed_sssom.load_review
    observed = {}

    def mutate_after_mapping_validation(root, review_path):
        loaded = original_load(root, review_path)
        second = loaded["decisions"][1]["owner_record"]
        owner = root / second
        observed["before"] = reviewed_sssom.digest(owner)
        observed["expected"] = loaded["review"]["record_inputs"][second]
        owner.write_bytes(owner.read_bytes() + b"\nnotes: Changed after mapping validation\n")
        observed["after"] = reviewed_sssom.digest(owner)
        companion_path = root / "companion.json"
        companion = json.loads(companion_path.read_text())
        assert second not in companion["record_inputs"]
        companion["inputs"][second] = observed["after"]
        write_json(companion_path, companion)
        return loaded

    monkeypatch.setattr(reviewed_sssom, "load_review", mutate_after_mapping_validation)
    with pytest.raises(ValueError, match="conflicting validated input snapshots"):
        ordinary(current, history)
    assert observed["before"] == observed["expected"] != observed["after"]
    assert not (current / "output").exists()


def test_1326_snapshot_merge_preserves_matching_bindings_and_rejects_conflicts(tmp_path):
    first, second = tmp_path / "first", tmp_path / "second"
    snapshots = {first: "a" * 64}
    route._merge_snapshots(snapshots, {first: "a" * 64, second: "b" * 64})
    assert snapshots == {first: "a" * 64, second: "b" * 64}
    before = snapshots.copy()
    with pytest.raises(ValueError, match="conflicting validated input snapshots"):
        route._merge_snapshots(snapshots, {tmp_path / "third": "c" * 64, first: "d" * 64})
    assert snapshots == before


@pytest.mark.parametrize(
    "changed", ["row", "owner", "evidence", "incomplete", "companion", "source_subset"]
)
def test_current_native_guards_are_not_bypassed(current, history, native_unit, changed):
    review = json.loads((current / "review.json").read_text())
    if changed == "row":
        p = current / projection.SOURCE
        p.write_bytes(p.read_bytes().replace(b"CHEBI:1", b"CHEBI:999"))
    elif changed == "owner":
        p = current / review["decisions"][0]["owner_record"]
        p.write_text(p.read_text() + "new_scientific_flag: true\n")
    elif changed == "evidence":
        (current / "evidence.json").write_text("{}\n")
    elif changed == "incomplete":
        review["decisions"].pop()
        write_json(current / "review.json", review)
    elif changed == "source_subset":
        review["source_sssom"] = "source.sssom.tsv"
        review["source_sha256"] = reviewed_sssom.digest(current / "source.sssom.tsv")
        write_json(current / "review.json", review)
    else:
        companion = json.loads((current / "companion.json").read_text())
        companion["base_review_sha256"] = "0" * 64
        write_json(current / "companion.json", companion)
    with pytest.raises(ValueError):
        ordinary(current, history)


@pytest.mark.parametrize("where", ["review", "proof_top", "proof_entry", "companion"])
def test_ordinary_refuses_projected_or_stripped_proofs(current, history, native_unit, where):
    name = {"review": "review.json", "companion": "companion.json"}.get(where, "evidence.json")
    value = json.loads((current / name).read_text())
    target = value["entries"]["1"] if where == "proof_entry" else value
    target["identity_projection"] = {
        "kind": projection.PROJECTION_KIND,
        "scientific_approval_added": False,
    }
    write_json(current / name, value)
    if name == "evidence.json":
        review = json.loads((current / "review.json").read_text())
        review["inputs"][name] = reviewed_sssom.digest(current / name)
        write_json(current / "review.json", review)
    with pytest.raises(ValueError, match="project|inherited"):
        ordinary(current, history)


def test_missing_projected_header_never_silently_switches_route(current, native_unit):
    with pytest.raises(ValueError, match="proof is missing"):
        route.check_route(current, Path("review.json"))
    assert not native_unit


@pytest.mark.parametrize("missing", ["root", "revision", "companion"])
def test_ordinary_needs_explicit_history_and_pair(current, history, native_unit, missing):
    kwargs = dict(
        route="ordinary",
        companion_review=Path("companion.json"),
        historical_root=history[0],
        historical_revision=history[1],
    )
    kwargs[
        {
            "root": "historical_root",
            "revision": "historical_revision",
            "companion": "companion_review",
        }[missing]
    ] = None
    with pytest.raises(ValueError):
        route.check_route(current, Path("review.json"), **kwargs)
    assert not native_unit


@pytest.mark.parametrize("mutation", ["bytes", "mode", "symlink", "head", "index"])
def test_historical_git_pin_binds_actual_bytes_and_modes(history, mutation):
    root, revision = history
    path = root / "retained.txt"
    if mutation == "bytes":
        path.write_text("Changed actual bytes\n")
    elif mutation == "mode":
        path.chmod(0o755)
    elif mutation == "symlink":
        path.unlink()
        path.symlink_to("missing")
    elif mutation == "head":
        path.write_text("Later committed bytes\n")
        commit(root)
    else:
        git(root, "rm", "--cached", "retained.txt")
    with pytest.raises(ValueError):
        route._historical_checkout(root, revision)


def test_historical_pin_accepts_literal_committed_symlink_without_following(history):
    root, _ = history
    (root / "link").symlink_to("retained.txt")
    revision = commit(root)
    assert route._historical_checkout(root, revision)["tracked_files"] == 2


@pytest.mark.parametrize("spelling", ["same", "nested", "traversal", "symlink"])
def test_roots_cannot_alias_or_overlap(current, history, native_unit, spelling):
    root, revision = history
    if spelling == "same":
        root = current
    elif spelling == "nested":
        root = current / "nested"
        root.mkdir()
    elif spelling == "traversal":
        root = current / ".." / "historical"
    else:
        alias = current.parent / "history-alias"
        alias.symlink_to(root, target_is_directory=True)
        root = alias
    with pytest.raises(ValueError):
        ordinary(current, (root, revision))
    assert not native_unit


def test_late_historical_drift_is_refused(current, history, monkeypatch):
    def changed(root):
        (root / "retained.txt").write_text("late drift\n")
        return {"checked": True, "scientific_approval_added": False}

    monkeypatch.setattr(route, "_projection_check", changed)
    with pytest.raises(ValueError, match="committed bytes"):
        ordinary(current, history)


@pytest.fixture(scope="module")
def real_history(tmp_path_factory):
    destination = tmp_path_factory.mktemp("native-history") / "checkout"
    subprocess.run(
        [
            "git",
            "clone",
            "--no-hardlinks",
            "--dissociate",
            "--no-checkout",
            str(ROOT),
            str(destination),
        ],
        check=True,
        capture_output=True,
    )
    revision = git(ROOT, "rev-parse", "HEAD")
    git(destination, "checkout", "--detach", revision)
    assert not (destination / ".git/objects/info/alternates").exists()
    return destination, revision


def test_real_native_projected_default_keeps_complete_proof(real_history):
    result = route.check_route(real_history[0], companion_review=route.DEFAULT_COMPANION)
    assert result["route"] == "projected"
    assert result["native_projection"]["rows"] == result["source_rows"]
    assert result["native_projection"]["scientific_approval_added"] is False


def test_real_native_history_and_different_current_science(current, real_history):
    result = ordinary(current, real_history)
    assert result["source_rows"] == 2
    assert result["native_projection"]["rows"] > result["source_rows"]
    assert result["historical_checkout"]["revision"] == real_history[1]
    assert result["companion_counts"]["mappings"] == 1


def test_real_native_checker_rejects_a_committed_scientific_change(tmp_path, real_history):
    destination = tmp_path / "corrupted-historical-checkout"
    subprocess.run(
        ["git", "clone", "--no-hardlinks", "--dissociate", str(real_history[0]), str(destination)],
        check=True,
        capture_output=True,
    )
    owner = next((destination / "data/ingredients/mapped").glob("*.yaml"))
    owner.write_bytes(owner.read_bytes() + b"\nsynthetic_scientific_corruption: true\n")
    revision = commit(destination)
    # An authentic new Git commit is still not the fixed historical proof.
    assert route._historical_checkout(destination, revision)["revision"] == revision
    with pytest.raises(ValueError, match="native historical projection failed"):
        route._projection_check(destination)


def test_default_route_selectors_match_native_export_commands():
    workflow = yaml.safe_load((ROOT / ".github/workflows/qc-reviewed-sssom.yaml").read_text())
    runs = [x.get("run", "") for x in workflow["jobs"]["reviewed-sssom"]["steps"]]
    checks = [x for x in runs if "mediaingredientmech.validation.reviewed_export_route" in x]
    assert len(checks) == 1
    assert "--route projected" in checks[0]
    assert f"--review {route.DEFAULT_REVIEW}" in checks[0]
    assert f"--companion-review {route.DEFAULT_COMPANION}" in checks[0]
    assert any(
        f"--review {route.DEFAULT_REVIEW}" in x and "export.reviewed_sssom" in x for x in runs
    )
    assert any(
        f"--review {route.DEFAULT_COMPANION}" in x and "export.ingredient_bundle export" in x
        for x in runs
    )
