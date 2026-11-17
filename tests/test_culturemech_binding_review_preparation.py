"""Exact-snapshot publication tests for diagnostic review preparation (#1461)."""

import importlib.util
import json
from pathlib import Path

import pytest

from mediaingredientmech.intake import culturemech as intake
from tests.test_culturemech_intake import handoff, prepared  # noqa: F401
from tests.test_reviewed_sssom import reviewed_fixture  # noqa: F401

HELPER = Path(__file__).parents[1] / "scripts/adhoc/prepare_culturemech_binding_review_1453.py"
SPEC = importlib.util.spec_from_file_location("binding_review_preparation", HELPER)
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)
SPLIT_SPEC = importlib.util.spec_from_file_location(
    "binding_review_split", HELPER.with_name("split_culturemech_binding_review_1453.py")
)
split_helper = importlib.util.module_from_spec(SPLIT_SPEC)
SPLIT_SPEC.loader.exec_module(split_helper)


def test_unchanged_snapshot_publishes_exact_packet_binding(handoff):  # noqa: F811
    root, source, manifest, pin = prepared(handoff)
    output = root / "diagnostic"
    summary = helper.prepare(source, pin, output, root=root)
    assert summary == json.loads((output / "summary.json").read_text())
    assert summary["review_packet_sha256"] == manifest["files"]["review-packet.json"]["sha256"]
    assert summary["status"] == "DIAGNOSTIC_REVIEW_PREPARATION_ONLY"
    assert summary["cases"] == manifest["counts"]["cases"]
    for name, expected in summary["products"].items():
        assert intake.fingerprint(output / name) == expected


@pytest.mark.parametrize("changed", ["packet", "owner"])
def test_late_input_change_cannot_publish_accepted_profiles(
    handoff, monkeypatch, changed  # noqa: F811
):
    root, source, manifest, pin = prepared(handoff)
    output = root / "diagnostic"
    original = intake.write_json
    target = (
        source / "review-packet.json"
        if changed == "packet"
        else root / next(iter(manifest["mim_record_inputs"]))
    )
    before = target.read_bytes()

    def mutate_after_summary(path, value):
        original(path, value)
        if path.name == "summary.json":
            target.write_bytes(before + b"\n")

    monkeypatch.setattr(intake, "write_json", mutate_after_summary)
    with pytest.raises(ValueError, match="changed|differs"):
        helper.prepare(source, pin, output, root=root)
    assert target.read_bytes() != before
    assert not output.exists()


def test_packet_read_is_bound_to_verified_bytes(handoff, monkeypatch):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    output = root / "diagnostic"
    original = intake.verify_intake
    target = source / "review-packet.json"

    def mutate_after_verification(*args):
        result = original(*args)
        target.write_bytes(target.read_bytes() + b"\n")
        return result

    monkeypatch.setattr(intake, "verify_intake", mutate_after_verification)
    with pytest.raises(ValueError, match="hash|digest|SHA|pin"):
        helper.prepare(source, pin, output, root=root)
    assert not output.exists()


def test_split_retains_every_complete_eligible_case_and_coordinates(handoff):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    profiles, output = root / "diagnostic", root / "review-partitions"
    helper.prepare(source, pin, profiles, root=root)
    result = split_helper.prepare(
        source,
        pin,
        profiles,
        intake.fingerprint(profiles / "summary.json")["sha256"],
        output,
        root=root,
    )
    original = json.loads((source / "review-packet.json").read_text())["cases"]
    expected = {
        case["case_id"]: case for case in original if case["candidate"]["supported_canonical_rows"]
    }
    observed = {}
    for path in output.glob("owner-*.json"):
        value = json.loads(path.read_text())
        for case in value["cases"]:
            assert case["case_id"] not in observed
            assert value["case_payload_sha256"][case["case_id"]] == intake.payload_sha256(case)
            observed[case["case_id"]] = case
    assert observed == expected  # Includes long quoted notes and every occurrence coordinate.
    assert result["eligible_cases"] + result["canonical_gated_cases"] == len(original)
    assert result["first_owner_count"] + result["second_owner_count"] == result["eligible_owners"]


def test_split_rejects_cross_intake_profile(handoff):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    profiles, output = root / "diagnostic", root / "review-partitions"
    helper.prepare(source, pin, profiles, root=root)
    path = profiles / "summary.json"
    value = json.loads(path.read_text())
    value["review_packet_sha256"] = "a" * 64
    path.write_text(json.dumps(value))
    with pytest.raises(ValueError, match="another intake"):
        split_helper.prepare(
            source, pin, profiles, intake.fingerprint(path)["sha256"], output, root=root
        )
    assert not output.exists()
