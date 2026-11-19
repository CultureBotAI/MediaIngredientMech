"""#1431: both integrated native reports bind generic evidence, including holds."""

import csv
import json
from pathlib import Path

import pytest

from mediaingredientmech.export import culturemech_replay as replay
from mediaingredientmech.export import source_bindings as binding
from tests.culturemech_replay_fixture import fingerprint, make_package, write_json
from tests.test_source_bindings import Fixture


def _extras(current):
    directory = current.root / "synthetic-integration"
    directory.mkdir()
    member = directory / "member.tsv"
    member.write_text("id\tlabel\nSYNTHETIC:1\tSynthetic evidence only\n")
    receipt = directory / "receipt.json"
    write_json(receipt, {"diagnostic_only": True, "files": {"member.tsv": fingerprint(member)}})
    reconciliation = directory / "reconciliation.tsv"
    reconciliation.write_text("source\ttarget\nSYNTHETIC:1\tSOURCE:1\n")
    return {
        path.relative_to(current.root).as_posix(): fingerprint(path)["sha256"]
        for path in (receipt, member, reconciliation)
    }


def _seal(current, extras, *, omit=None, all_withheld=False):
    held = tuple(range(1, 5)) if all_withheld else (1,)
    for number, case in enumerate(current.review["cases"], 1):
        case["holds"] = (
            ["Synthetic unresolved identity at source " + str(number)] if number in held else []
        )

    def bind_extras(role, report):
        names = [item["path"] for item in report["source"]["inputs"]]
        names.extend(name for name in extras if (role, name) != omit)
        report["source"] = current.native.inspect_source(current.root, report["targets"], names)[
            "source"
        ]

    # The existing fixture clears request inputs during report preparation.
    # Add the exact generic inventory after both reports have been authored.
    current.seal(withheld=held, alter=bind_extras)
    current.review["inputs"].update(extras)
    current.save()


@pytest.fixture
def integrated(tmp_path):
    current = Fixture(tmp_path)
    package = make_package(current.root)
    current.review["culturemech_intake_replay"] = package["reference"]
    return current, _extras(current)


def _rows(path):
    return list(
        csv.DictReader(
            (line for line in path.read_text().splitlines() if not line.startswith("#")),
            delimiter="\t",
        )
    )


def test_complete_inputs_preserve_current_holds_and_both_partitions(integrated):
    current, extras = integrated
    _seal(current, extras)
    hold = current.review["cases"][0]["holds"][:]
    inspection = binding.inspect_candidates(current.root, current.review_path)
    assert all(inspection["inputs"][name] == digest for name, digest in extras.items())
    for case in current.review["cases"]:
        for role in ("primary", "skeptic"):
            path = case[role]["path"]
            assert path not in inspection["inputs"]
            assert str(Path(path).with_name("review.md")) not in inspection["inputs"]
    manifest = binding.export_candidate(current.root, current.review_path, current.output)
    assert binding.validate_candidate(current.root, current.review_path, current.output) == manifest
    assert replay.CAPABILITY in manifest["required_capabilities"]
    assert manifest["production_authorized"] is False
    assert manifest["counts"] == {
        "source_entities": 4,
        "source_occurrences": 5,
        "supported": 3,
        "withheld": 1,
        "withheld_without_owner": 0,
    }
    assert manifest["culturemech_intake_replay"]["counts"] == {
        "positive_inventory": 2,
        "context_only": 1,
        "held": 1,
        "supported_bindings": 2,
        "withheld_bindings": 2,
    }
    decisions = json.loads((current.output / "source-decisions.json").read_text())
    assert decisions[0]["payload"]["holds"] == hold
    assert decisions[0]["disposition"] == "WITHHOLD"
    assert {row["subject_id"] for row in _rows(current.output / "source-bindings.sssom.tsv")} == {
        "SOURCE:2",
        "SOURCE:3",
        "SOURCE:4",
    }
    assert [
        row["subject_id"] for row in _rows(current.output / "withheld-source-bindings.sssom.tsv")
    ] == ["SOURCE:1"]
    for report in current.reports:
        declared = {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        assert all(
            declared[name] == digest == manifest["inputs"][name] for name, digest in extras.items()
        )


@pytest.mark.parametrize("role", ["primary", "skeptic"])
@pytest.mark.parametrize("member", ["receipt.json", "member.tsv", "reconciliation.tsv"])
@pytest.mark.parametrize("all_withheld", [False, True], ids=["mixed", "all-held"])
def test_each_report_requires_every_generic_input_even_when_all_held(
    integrated, role, member, all_withheld
):
    current, extras = integrated
    omitted = "synthetic-integration/" + member
    _seal(current, extras, omit=(role, omitted), all_withheld=all_withheld)
    assert current.review["inputs"][omitted] == extras[omitted]
    if all_withheld:
        assert all(case["holds"] for case in current.review["cases"])
        assert all(
            dimension["value"] == "withhold"
            for report in current.reports
            for assessment in report["assessments"]
            for dimension in assessment["dimensions"]
            if dimension["name"] == "source_identity_disposition"
        )
    with pytest.raises(
        ValueError, match="native report omits current source/occurrence/owner/ledger inputs"
    ):
        binding.export_candidate(current.root, current.review_path, current.output)
    assert not current.output.exists()


def test_inspection_requires_generic_inputs_before_reports_exist(integrated):
    current, extras = integrated
    current.review["inputs"] = extras
    for case in current.review["cases"]:
        case["primary"] = case["skeptic"] = None
    current.save()
    inspection = binding.inspect_candidates(current.root, current.review_path)
    assert all(inspection["inputs"][name] == digest for name, digest in extras.items())
    assert all(
        case["primary"] is None and case["skeptic"] is None for case in current.review["cases"]
    )


@pytest.mark.parametrize("suffix", ["review.yaml", "review.md"])
def test_unreferenced_report_shaped_evidence_remains_required(integrated, suffix):
    current, extras = integrated
    name = "reviews/structured/unreferenced-evidence/" + suffix
    path = current.root / name
    path.parent.mkdir()
    path.write_text("Synthetic source evidence; not a referenced report pair.\n")
    extras[name] = fingerprint(path)["sha256"]
    _seal(current, extras, omit=("skeptic", name))
    assert (
        binding.inspect_candidates(current.root, current.review_path)["inputs"][name]
        == extras[name]
    )
    with pytest.raises(
        ValueError, match="native report omits current source/occurrence/owner/ledger inputs"
    ):
        binding.export_candidate(current.root, current.review_path, current.output)
    assert not current.output.exists()


@pytest.mark.parametrize("attack", ["unpinned-markdown", "changed-markdown", "noncanonical-path"])
def test_only_valid_referenced_native_pairs_can_avoid_cycles(integrated, attack):
    current, extras = integrated
    _seal(current, extras)
    path = current.review["cases"][0]["primary"]["path"]
    markdown = str(Path(path).with_name("review.md"))
    if attack == "unpinned-markdown":
        current.review["inputs"].pop(markdown)
        expected = "native report pair must be pinned"
    elif attack == "changed-markdown":
        (current.root / markdown).write_text("Unreviewed replacement text\n")
        current.review["inputs"][markdown] = fingerprint(current.root / markdown)["sha256"]
        expected = "Markdown does not match"
    else:
        replacement = "synthetic-integration/not-canonical.yaml"
        replacement_md = "synthetic-integration/review.md"
        (current.root / replacement).write_bytes((current.root / path).read_bytes())
        (current.root / replacement_md).write_bytes((current.root / markdown).read_bytes())
        for name in (replacement, replacement_md):
            current.review["inputs"][name] = fingerprint(current.root / name)["sha256"]
        current.review["cases"][0]["primary"]["path"] = replacement
        expected = "canonical structured bundle"
    current.save()
    with pytest.raises(ValueError, match=expected):
        binding.export_candidate(current.root, current.review_path, current.output)
    assert not current.output.exists()


def test_ordinary_request_does_not_gain_integrated_input_contract(tmp_path):
    current = Fixture(tmp_path)
    extras = _extras(current)
    current.review["inputs"].update(extras)
    current.save()
    assert all(
        not set(extras) & {item["path"] for item in report["source"]["inputs"]}
        for report in current.reports
    )
    manifest = binding.export_candidate(current.root, current.review_path, current.output)
    assert replay.CAPABILITY not in manifest["required_capabilities"]
    assert all(manifest["inputs"][name] == digest for name, digest in extras.items())
