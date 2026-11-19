"""#1882: genuine synthetic source and both native historical replay stages."""

import io
import json
import os
import sys
import tarfile
import types
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import culturemech_replay as replay
from mediaingredientmech.export import source_bindings as binding
from tests.culturemech_replay_fixture import (
    FixtureInputs,
    fingerprint,
    make_binding_review,
    make_package,
    refresh_canonical_review_reference,
    reseal_package_inventory,
    write_json,
)
from tests.test_source_bindings import Fixture


@pytest.fixture
def native_package(tmp_path):
    current = Fixture(tmp_path)
    package = make_package(current.root)
    return current, package


def test_genuine_source_and_both_historical_stages_replay_exactly(native_package):
    current, package = native_package
    counts = package["cm"]["manifest"]["counts"]
    assert counts["scanned_records"] == 1
    assert counts["occurrences"] == 2
    assert counts["variant_context_only_mentions"] == 1
    assert counts["variant_held_mentions"] == 1
    assert counts["errors"] == 0
    assert package["intake"]["consumer_implementation"] == {
        "sha256": replay.PREPARATION_SHA,
        "bytes": 47572,
    }
    assert package["final"]["counts"] == {"SUPPORTED": 2, "WITHHOLD": 2}
    assert fingerprint(package["modules"]["review"].__file__)["sha256"] == replay.VERIFICATION_SHA
    inputs = FixtureInputs(current.root)
    selected = replay.Selection(inputs, package["reference"])
    proof = replay.replay(selected)
    assert set(proof) == {
        "source_manifest",
        "prepared_intake",
        "reviewed_intake",
        "binding_review",
        "counts",
    }
    assert proof["counts"] == {
        "positive_inventory": 2,
        "context_only": 1,
        "held": 1,
        "supported_bindings": 2,
        "withheld_bindings": 2,
    }
    for name, declaration in proof.items():
        if name != "counts":
            assert inputs.hashes[declaration["path"]] == declaration["sha256"]


def test_optional_route_binds_replay_into_both_reviews_and_native_export(native_package):
    current, package = native_package
    current.review["culturemech_intake_replay"] = package["reference"]
    current.seal()
    manifest = binding.export_candidate(current.root, current.review_path, current.output)
    assert replay.CAPABILITY in manifest["required_capabilities"]
    assert manifest["production_authorized"] is False
    assert manifest["culturemech_intake_replay"]["counts"]["held"] == 1
    assert manifest["counts"]["source_entities"] == 4
    assert manifest["counts"]["source_occurrences"] == 5
    selected_path = package["reference"]["path"]
    for report in current.reports:
        pinned = {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        assert pinned[selected_path] == package["reference"]["sha256"]
    for name, declaration in manifest["culturemech_intake_replay"].items():
        if name != "counts":
            assert manifest["inputs"][declaration["path"]] == declaration["sha256"]
    assert binding.validate_candidate(current.root, current.review_path, current.output) == manifest
    data = json.loads((current.output / "source-decisions.json").read_text())
    assert len(data) == 4


def test_ordinary_request_keeps_its_original_contract(tmp_path):
    current = Fixture(tmp_path)
    manifest = binding.export_candidate(current.root, current.review_path, current.output)
    assert replay.CAPABILITY not in manifest["required_capabilities"]
    assert "culturemech_intake_replay" not in manifest
    assert manifest["counts"]["source_entities"] == 4
    assert manifest["counts"]["source_occurrences"] == 5
    assert not any(name.startswith("cm-package/") for name in manifest["inputs"])


@pytest.mark.parametrize(
    ("stage", "artifact"),
    [("prepared", "review-cases.tsv"), ("reviewed", "binding-dispositions.tsv")],
)
def test_rehashed_artifact_still_requires_exact_native_reconstruction(
    native_package, stage, artifact
):
    current, package = native_package
    path = package[stage] / artifact
    path.write_bytes(path.read_bytes() + b"\n")
    reseal_package_inventory(package)
    selected = replay.Selection(FixtureInputs(current.root), package["reference"])
    # Selection succeeds with the new pins; real generation must reject the bytes.
    with pytest.raises(
        ValueError, match="native reconstruction differs from accepted artifact bytes/membership"
    ):
        replay.replay(selected)


@pytest.mark.parametrize("role", ["primary", "skeptic"])
def test_each_native_review_must_bind_historical_closure(native_package, role):
    current, package = native_package
    current.review["culturemech_intake_replay"] = package["reference"]
    omitted = "cm-package/consumer/data/ingredients/mapped/Water.yaml"

    def omit_one_historical_input(actual_role, report):
        if actual_role == role:
            names = [item["path"] for item in report["source"]["inputs"]]
            assert omitted in names
            report["source"] = current.native.inspect_source(
                current.root, report["targets"], [name for name in names if name != omitted]
            )["source"]

    current.seal(alter=omit_one_historical_input)
    with pytest.raises(
        ValueError, match="native report omits current source/occurrence/owner/ledger inputs"
    ):
        binding.export_candidate(current.root, current.review_path, current.output)
    assert not current.output.exists()


def test_source_identity_hold_cannot_be_promoted_by_binding_review(native_package):
    _, package = native_package
    path = package["consumer"] / "reviews/binding-review.json"
    review = json.loads(path.read_bytes())
    packet = json.loads((package["prepared"] / "review-packet.json").read_bytes())
    held = next(
        case
        for case in packet["cases"]
        if "IDENTITY_FORM" in case["context"].get("held_fields", [])
    )
    supported = next(
        decision for decision in review["decisions"] if decision["disposition"] == "SUPPORTED"
    )
    decision = next(item for item in review["decisions"] if item["case_id"] == held["case_id"])
    decision["disposition"] = "SUPPORTED"
    decision["canonical_row_sha256"] = supported["canonical_row_sha256"]
    evidence_path = package["consumer"] / decision["review_evidence"]
    evidence = json.loads(evidence_path.read_bytes())
    evidence["entries"][decision["evidence_key"]]["disposition"] = "SUPPORTED"
    write_json(evidence_path, evidence)
    review["inputs"][decision["review_evidence"]] = fingerprint(evidence_path)["sha256"]
    write_json(path, review)
    output = package["consumer"] / ".temp/invalid-held-approval"
    with pytest.raises(
        ValueError, match="Source identity uncertainty cannot be approved by mapping review"
    ):
        package["modules"]["review"].finalize(
            package["prepared"],
            fingerprint(package["prepared"] / "intake.json")["sha256"],
            "reviews/binding-review.json",
            output,
            root=package["consumer"],
        )
    assert not output.exists()


@pytest.mark.parametrize(
    "member",
    ["src/culturemech/hidden_extra.py", "data/normalized_yaml/bacterial/hidden_extra.yaml"],
)
def test_extra_archived_code_or_recipe_is_not_suppressed_by_extraction(native_package, member):
    current, package = native_package
    path = package["prepared"] / "source/producer-source.tar.gz"
    original = path.read_bytes()
    with tarfile.open(fileobj=io.BytesIO(original), mode="r:gz") as old:
        with tarfile.open(path, "w:gz") as new:
            for item in old.getmembers():
                new.addfile(item, old.extractfile(item) if item.isfile() else None)
            extra = tarfile.TarInfo("producer/" + member)
            content = b"# Extra synthetic archive member; not declared in source manifest.\n"
            extra.size = len(content)
            new.addfile(extra, io.BytesIO(content))
    handoff_path = package["prepared"] / "source/handoff.json"
    handoff = json.loads(handoff_path.read_bytes())
    handoff["source_archive_sha256"] = fingerprint(path)["sha256"]
    write_json(handoff_path, handoff)
    intake_path = package["prepared"] / "intake.json"
    intake = json.loads(intake_path.read_bytes())
    intake["handoff_sha256"] = fingerprint(handoff_path)["sha256"]
    write_json(intake_path, intake)
    reseal_package_inventory(package)
    selected = replay.Selection(FixtureInputs(current.root), package["reference"])
    assert selected.source == package["cm"]["manifest"]
    with pytest.raises(
        ValueError, match="archived source/dependency membership differs from manifest"
    ):
        replay.replay(selected)


def test_public_module_cache_cannot_replace_private_historical_helpers(native_package, monkeypatch):
    current, package = native_package
    sentinel = types.ModuleType("mediaingredientmech.curie")
    monkeypatch.setitem(sys.modules, "mediaingredientmech.curie", sentinel)
    proof = replay.replay(replay.Selection(FixtureInputs(current.root), package["reference"]))
    assert proof["counts"]["supported_bindings"] == 2
    assert proof["counts"]["withheld_bindings"] == 2
    assert sys.modules["mediaingredientmech.curie"] is sentinel


def replace_with_identical_bytes(path, mode, spare):
    original = path.read_bytes()
    identity = path.stat()
    spare.parent.mkdir(parents=True, exist_ok=True)
    spare.write_bytes(original)
    if mode == "replacement":
        spare.replace(path)
    else:
        path.unlink()
        if mode == "symlink":
            path.symlink_to(spare)
        else:
            assert mode == "hardlink"
            os.link(spare, path)
    assert path.read_bytes() == original
    assert path.is_symlink() or path.stat().st_ino != identity.st_ino


@pytest.mark.parametrize("target", ["owner", "dependency"])
@pytest.mark.parametrize("mode", ["replacement", "symlink", "hardlink"])
def test_same_byte_materialized_closure_change_after_real_prepare_is_refused(
    native_package, monkeypatch, target, mode
):
    current, package = native_package
    real_loader = replay.load_historical_modules
    mutations = []

    def loader(inputs, directory, process):
        modules = real_loader(inputs, directory, process)
        real_prepare = modules["prepare"].prepare

        def prepare_then_change(*args, **kwargs):
            result = real_prepare(*args, **kwargs)
            path = (
                kwargs["root"] / "data/ingredients/mapped/Water.yaml"
                if target == "owner"
                else kwargs["producer_root"] / "scripts/record_kinds.py"
            )
            replace_with_identical_bytes(path, mode, current.root / ".temp/mutation-spare")
            mutations.append(path)
            return result

        modules["prepare"].prepare = prepare_then_change
        return modules

    monkeypatch.setattr(replay, "load_historical_modules", loader)
    expected = {
        "replacement": "materialized member identity changed",
        "symlink": "symlink materialized member",
        "hardlink": "aliased source file",
    }[mode]
    with pytest.raises(ValueError, match=expected):
        replay.replay(replay.Selection(FixtureInputs(current.root), package["reference"]))
    assert len(mutations) == 1


@pytest.mark.parametrize("mode", ["symlink", "hardlink"])
def test_initial_package_member_alias_is_refused(native_package, mode):
    current, package = native_package
    path = package["consumer"] / "data/ingredients/mapped/Water.yaml"
    replace_with_identical_bytes(path, mode, current.root / ".temp/initial-alias-spare")
    expected = "nonregular/symlink file" if mode == "symlink" else "aliased source file"
    with pytest.raises(ValueError, match=expected):
        replay.Selection(FixtureInputs(current.root), package["reference"])


def test_scratch_alias_refused_before_creating_any_directory(native_package):
    current, package = native_package
    selected = replay.Selection(FixtureInputs(current.root), package["reference"])
    preserved = current.root / "preserved-temp"
    (current.root / ".temp").rename(preserved)
    (current.root / ".temp").symlink_to(preserved, target_is_directory=True)
    before = sorted(path.relative_to(preserved).as_posix() for path in preserved.rglob("*"))
    with pytest.raises(ValueError, match="aliased scratch root"):
        replay.replay(selected)
    assert not (preserved / "native-culturemech-replay").exists()
    assert sorted(path.relative_to(preserved).as_posix() for path in preserved.rglob("*")) == before


def test_scratch_overlap_with_selected_package_refused_before_write(native_package):
    current, package = native_package
    destination = current.root / ".temp/native-culturemech-replay"
    package["package"].rename(destination)
    reference = {**package["reference"], "path": ".temp/native-culturemech-replay/package.json"}
    selected = replay.Selection(FixtureInputs(current.root), reference)
    before = sorted(path.relative_to(destination).as_posix() for path in destination.rglob("*"))
    with pytest.raises(ValueError, match="scratch overlaps selected input package"):
        replay.replay(selected)
    assert (
        sorted(path.relative_to(destination).as_posix() for path in destination.rglob("*"))
        == before
    )


def test_historical_capsule_same_byte_replacement_after_prepare_is_refused(
    native_package, monkeypatch
):
    current, package = native_package
    real_loader = replay.load_historical_modules
    mutated = []

    def loader(inputs, directory, process):
        modules = real_loader(inputs, directory, process)
        real_prepare = modules["prepare"].prepare

        def prepare_then_replace(*args, **kwargs):
            result = real_prepare(*args, **kwargs)
            path = Path(modules["prepare"].__file__)
            replace_with_identical_bytes(
                path, "replacement", current.root / ".temp/capsule-replacement"
            )
            mutated.append(path)
            return result

        modules["prepare"].prepare = prepare_then_replace
        return modules

    monkeypatch.setattr(replay, "load_historical_modules", loader)
    with pytest.raises(ValueError, match="frozen file or ancestor changed"):
        replay.replay(replay.Selection(FixtureInputs(current.root), package["reference"]))
    assert len(mutated) == 1


def test_semantic_case_tamper_with_regenerated_review_is_refused(native_package):
    current, package = native_package
    source = package["prepared"] / "source"
    original_source = {
        path.relative_to(source).as_posix(): path.read_bytes()
        for path in source.rglob("*")
        if path.is_file()
    }
    packet_path = package["prepared"] / "review-packet.json"
    packet = json.loads(packet_path.read_bytes())
    case = next(
        case for case in packet["cases"] if case["context"]["change_action"] == "SET_AMOUNT"
    )
    assert len(case["change_payloads"]) == 1
    payload = next(iter(case["change_payloads"].values()))
    assert payload["amount"]["value"] == "0.25"
    payload["amount"]["value"] = "9.75"
    later = package["modules"]["review"]
    case["change_payloads"] = {later.payload_sha256(payload): payload}
    write_json(packet_path, packet)
    reseal_package_inventory(package)
    pin = fingerprint(package["prepared"] / "intake.json")["sha256"]
    review = make_binding_review(package["consumer"], package["prepared"], pin, later)
    # Preserve the original reviewed artifact, then produce a genuinely valid
    # later-stage review of the forged prepared case. Only original source replay
    # can establish that this amount did not come from the fixed source bytes.
    package["reviewed"].rename(current.root / ".temp/preserved-semantic-reviewed")
    final = later.finalize(
        package["prepared"], pin, review, package["reviewed"], root=package["consumer"]
    )
    assert final["counts"] == {"SUPPORTED": 2, "WITHHOLD": 2}
    reseal_package_inventory(package)
    selected = replay.Selection(FixtureInputs(current.root), package["reference"])
    assert selected.intake["source_manifest_sha256"] == package["intake"]["source_manifest_sha256"]
    assert {
        path.relative_to(source).as_posix(): path.read_bytes()
        for path in source.rglob("*")
        if path.is_file()
    } == original_source
    with pytest.raises(
        ValueError, match="native reconstruction differs from accepted artifact bytes/membership"
    ):
        replay.replay(selected)


def test_rehashed_historical_owner_semantics_require_native_owner_resolution(native_package):
    current, package = native_package
    owner = "data/ingredients/mapped/Water.yaml"
    owner_path = package["consumer"] / owner
    record = yaml.safe_load(owner_path.read_bytes())
    record["preferred_term"] = "Synthetic changed material"
    owner_path.write_text(yaml.safe_dump(record))
    owner_pin = fingerprint(owner_path)
    intake_path = package["prepared"] / "intake.json"
    intake = json.loads(intake_path.read_bytes())
    intake["mim_record_inputs"][owner] = owner_pin
    write_json(intake_path, intake)
    evidence_path = package["consumer"] / "reviews/canonical-evidence.json"
    evidence = json.loads(evidence_path.read_bytes())
    evidence["entries"]["water"]["owner_record_sha256"] = owner_pin["sha256"]
    write_json(evidence_path, evidence)
    canonical_path = package["consumer"] / "reviews/canonical.json"
    canonical = json.loads(canonical_path.read_bytes())
    canonical["record_inputs"][owner] = owner_pin["sha256"]
    canonical["inputs"]["reviews/canonical-evidence.json"] = fingerprint(evidence_path)["sha256"]
    write_json(canonical_path, canonical)
    refresh_canonical_review_reference(package)
    selected = replay.Selection(FixtureInputs(current.root), package["reference"])
    assert selected.intake["mim_record_inputs"][owner] == owner_pin
    with pytest.raises(ValueError, match="No unique independent owner for MIM:Water"):
        replay.replay(selected)


def test_rehashed_canonical_evidence_requires_native_scientific_agreement(native_package):
    current, package = native_package
    evidence_path = package["consumer"] / "reviews/canonical-evidence.json"
    evidence = json.loads(evidence_path.read_bytes())
    assert evidence["entries"]["water"]["disposition"] == "SUPPORTED"
    evidence["entries"]["water"]["disposition"] = "WITHHOLD"
    write_json(evidence_path, evidence)
    canonical_path = package["consumer"] / "reviews/canonical.json"
    canonical = json.loads(canonical_path.read_bytes())
    canonical["inputs"]["reviews/canonical-evidence.json"] = fingerprint(evidence_path)["sha256"]
    assert canonical["decisions"][0]["disposition"] == "SUPPORTED"
    write_json(canonical_path, canonical)
    refresh_canonical_review_reference(package)
    selected = replay.Selection(FixtureInputs(current.root), package["reference"])
    with pytest.raises(ValueError, match="Scientific decision disagrees with exact evidence entry"):
        replay.replay(selected)
