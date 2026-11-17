"""Literal quantities and field-specific source holds survive the v3 boundary."""

import json
import tarfile

import pytest

from mediaingredientmech.intake import culturemech as intake
from tests.test_culturemech_intake import (
    FIELDS,
    handoff,  # noqa: F401
    prepared,
    write_binding_review,
)
from tests.test_reviewed_sssom import reviewed_fixture  # noqa: F401


def upgrade_to_v3(fixture):
    root, source, _pin, review, positive, ledger = fixture
    for row in (positive[1], ledger[0]):
        descriptor = json.loads(row["ingredient_json"])
        descriptor.pop("concentration")
        row["ingredient_json"] = json.dumps(descriptor)
        row["change_action"] = "SET_AMOUNT"
        row["change_json"] = json.dumps(
            {
                "action": "SET_AMOUNT",
                "ingredient": descriptor,
                "amount": {
                    "value": "0.25",
                    "unit": "G",
                    "basis": "PER_BATCH",
                    "basis_statement": "Literal source batch amount; final volume unasserted.",
                },
            }
        )
    bundle = source / "bundle"
    for name, fields, rows in (
        ("ingredient_occurrences.tsv", FIELDS, positive),
        ("variant_ingredient_changes.tsv", FIELDS + ["counts_as_presence"], ledger),
    ):
        (bundle / name).unlink()
        intake.write_tsv(bundle / name, fields, rows)
    held_rows = []
    for index, (label, dimensions) in enumerate(
        (
            ("Alpha", ["QUANTITY"]),
            ("Alpha", ["IDENTITY_FORM"]),
            ("Unknown mixture", ["SOURCE_CLAIM"]),
        )
    ):
        mention = {
            "source_label": label,
            "reported_action": "ADD",
            "stage": "source stage unknown",
            "source_modification_index": index,
            "source_text": "Add " + label + " according to source.",
            "reason": "Synthetic field-specific uncertainty",
            "reported_quantity": "literal source dose",
            "held_fields": dimensions,
            "evidence": [],
        }
        row = dict.fromkeys(intake.HELD_FIELDS, "")
        row.update(
            recipe_id="CultureMech:000001",
            recipe_label="Synthetic",
            recipe_category="ALGAE",
            source_path="algae/synthetic.yaml",
            variant_index="0",
            variant_name="Synthetic exposure",
            mention_index=str(index),
            descriptor_path=f"/variants/0/ingredient_mentions/{index}",
            **{
                field: str(value)
                for field, value in mention.items()
                if field not in {"held_fields", "evidence"}
            },
            held_fields_json=json.dumps(dimensions),
            evidence_json="[]",
            mention_json=json.dumps(mention),
            review_status="WITHHELD",
            counts_as_presence="false",
        )
        held_rows.append(row)
    intake.write_tsv(bundle / intake.HELD_PRODUCT, intake.HELD_FIELDS, held_rows)
    manifest = json.loads((bundle / "manifest.json").read_text())
    manifest["contract"] = "culturemech-direct-ingredients-v3"
    manifest["counts"].update(variant_held_mentions=3, variant_held_labels=2)
    manifest["counts"]["variant_changes_by_action"] = {
        "ADD": 1,
        "SET_AMOUNT": 1,
        "REPLACE": 1,
        "REMOVE": 1,
    }
    producer = root / "producer"
    script = producer / "scripts/ingredient_release_bundle.py"
    script.write_text(
        "import json\nprint(json.dumps("
        + repr(
            {
                "status": "VERIFIED_CANDIDATE",
                "assurance": "externally_pinned_manifest",
                "counts": manifest["counts"],
            }
        )
        + "))\n"
    )
    manifest["dependencies"]["scripts/ingredient_release_bundle.py"] = intake.fingerprint(script)
    manifest["products"] = {
        name: intake.fingerprint(bundle / name) for name in intake.PRODUCTS | {intake.HELD_PRODUCT}
    }
    (bundle / "manifest.json").write_text(json.dumps(manifest))
    archive = source / "producer-source.tar.gz"
    with tarfile.open(archive, "w:gz") as output:
        output.add(producer, arcname="producer")
    receipt_path = source / "handoff.json"
    receipt = json.loads(receipt_path.read_text())
    coverage_path = source / "coverage/summary.json"
    coverage = json.loads(coverage_path.read_text())
    coverage["held_mentions"] = len(held_rows)
    coverage_path.write_text(json.dumps(coverage))
    receipt.update(
        contract=manifest["contract"],
        manifest_sha256=intake.fingerprint(bundle / "manifest.json")["sha256"],
        source_archive_sha256=intake.fingerprint(archive)["sha256"],
        coverage_summary_sha256=intake.fingerprint(coverage_path)["sha256"],
    )
    receipt_path.write_text(json.dumps(receipt))
    return root, source, intake.fingerprint(receipt_path)["sha256"], review, positive, ledger


@pytest.mark.parametrize("reported", [None, 2])
def test_v3_coverage_must_bind_held_mention_count(handoff, reported):  # noqa: F811
    _root, source, _pin, _review, _positive, _ledger = upgrade_to_v3(handoff)
    coverage_path = source / "coverage/summary.json"
    coverage = json.loads(coverage_path.read_text())
    if reported is None:
        coverage.pop("held_mentions")
    else:
        coverage["held_mentions"] = reported
    coverage_path.write_text(json.dumps(coverage))
    receipt_path = source / "handoff.json"
    receipt = json.loads(receipt_path.read_text())
    receipt["coverage_summary_sha256"] = intake.fingerprint(coverage_path)["sha256"]
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="held-mention/coverage"):
        intake.verify_handoff(source, intake.fingerprint(receipt_path)["sha256"])


def test_v3_amounts_and_field_specific_holds_stay_lossless(handoff):  # noqa: F811
    root, output, manifest, pin = prepared(upgrade_to_v3(handoff))
    assert manifest["counts"]["held_source_mentions"] == 3
    packet = json.loads((output / "review-packet.json").read_text())
    amount_case = next(
        case for case in packet["cases"] if case["context"]["change_action"] == "SET_AMOUNT"
    )
    change = next(iter(amount_case["change_payloads"].values()))
    assert change["amount"]["value"] == "0.25" and change["amount"]["unit"] == "G"
    assert change["amount"]["basis"] == "PER_BATCH"
    assert "concentration" not in next(iter(amount_case["descriptors"].values()))
    review = write_binding_review(root, output, pin)
    result = intake.finalize(output, pin, "binding-review.json", root / "reviewed", root=root)
    assert result["counts"] == {"SUPPORTED": 4, "WITHHOLD": 5}
    with intake.csv_reader(root / "reviewed/supported-bindings.tsv") as reader:
        quantity = next(row for row in reader if row["descriptor_role"] == "held_mention")
    assert json.loads(quantity["held_fields_json"]) == ["QUANTITY"]
    assert quantity["held_source_mentions"] == "1"
    assert quantity["positive_occurrences"] == quantity["context_only_mentions"] == "0"
    identity = next(
        case for case in packet["cases"] if case["context"].get("held_fields") == ["IDENTITY_FORM"]
    )
    decision = next(item for item in review["decisions"] if item["case_id"] == identity["case_id"])
    decision["disposition"] = "SUPPORTED"
    decision["canonical_row_sha256"] = identity["candidate"]["supported_canonical_rows"][0][
        "row_sha256"
    ]
    evidence_path = root / "binding-evidence.json"
    evidence = json.loads(evidence_path.read_text())
    evidence["entries"][identity["case_id"]]["disposition"] = "SUPPORTED"
    evidence_path.write_text(json.dumps(evidence))
    review["inputs"]["binding-evidence.json"] = intake.fingerprint(evidence_path)["sha256"]
    (root / "binding-review.json").write_text(json.dumps(review))
    with pytest.raises(ValueError, match="identity uncertainty"):
        intake.finalize(output, pin, "binding-review.json", root / "refused", root=root)


@pytest.mark.parametrize("mutation", ["presence", "grounding", "source_text", "dimension"])
def test_v3_held_assertions_cannot_escape_quarantine(handoff, mutation):  # noqa: F811
    root, source, _pin, _review, _positive, _ledger = upgrade_to_v3(handoff)
    path = source / "bundle" / intake.HELD_PRODUCT
    with intake.csv_reader(path) as reader:
        rows = list(reader)
    if mutation == "presence":
        rows[0]["counts_as_presence"] = "true"
    elif mutation == "grounding":
        mention = json.loads(rows[0]["mention_json"])
        mention["identifier"] = "CHEBI:1"
        rows[0]["mention_json"] = json.dumps(mention)
    elif mutation == "source_text":
        rows[0]["source_text"] = "Different source"
    else:
        rows[0]["held_fields_json"] = "[]"
    path.unlink()
    intake.write_tsv(path, intake.HELD_FIELDS, rows)
    target = root / "held-parse-only"
    target.mkdir()
    with pytest.raises(ValueError):
        intake.collect_held_cases(
            source / "bundle", target, json.loads((source / "bundle/manifest.json").read_text())
        )
