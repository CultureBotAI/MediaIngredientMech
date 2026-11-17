"""Lossless source review, negative context, and exact native approval boundaries."""

import copy
import hashlib
import json
import sys
import tarfile
from contextlib import contextmanager
from pathlib import Path

import pytest

from mediaingredientmech.intake import culturemech as intake
from tests.test_reviewed_sssom import reviewed_fixture  # noqa: F401


def test_owner_snapshot_hash_and_candidate_share_exact_bytes(tmp_path, monkeypatch):
    """A rewrite between file reads must never mix an old pin with a new owner."""
    path = tmp_path / "data/ingredients/mapped/owner.yaml"
    path.parent.mkdir(parents=True)
    before = b"preferred_term: Alpha\nidentifier: CHEBI:1\nmapping_status: MAPPED\n"
    after = before.replace(b"Alpha", b"Changed").replace(b"CHEBI:1", b"CHEBI:2")
    path.write_bytes(before)
    original_open = Path.open
    first = True

    @contextmanager
    def rewriting_open(self, *args, **kwargs):
        nonlocal first
        mode = args[0] if args else kwargs.get("mode")
        rewrite = self == path and first and mode == "rb"
        if rewrite:
            first = False
        with original_open(self, *args, **kwargs) as stream:
            yield stream
        if rewrite:
            with original_open(path, "wb") as stream:
                stream.write(after)

    monkeypatch.setattr(Path, "open", rewriting_open)
    index, records, hashes = intake.mim_snapshot(tmp_path)
    name = path.relative_to(tmp_path).as_posix()
    assert path.read_bytes() == after  # The concurrent rewrite really occurred.
    assert records[name]["preferred_term"] == "Alpha"
    assert records[name]["identifier"] == "CHEBI:1"
    assert index["alpha"] == {name}
    assert "changed" not in index
    assert hashes[name] == {"sha256": hashlib.sha256(before).hexdigest(), "bytes": len(before)}


FIELDS = [
    "recipe_id",
    "recipe_label",
    "recipe_category",
    "source_path",
    "record_class",
    "component_field",
    "component_index",
    "preferred_term",
    "resolved_identifier",
    "concentration_value",
    "concentration_unit",
    "ingredient_json",
    *intake.VARIANT_FIELDS,
]


def source_row(
    name="Alpha",
    identifier="CHEBI:1",
    *,
    action="",
    index=0,
    role="ingredient",
    notes="Synthetic source context",
):
    row = dict.fromkeys(FIELDS, "")
    row.update(
        recipe_id="CultureMech:000001",
        recipe_label="Synthetic",
        recipe_category="ALGAE",
        source_path="algae/synthetic.yaml",
        record_class="MediaRecipe",
        component_field="ingredients",
        component_index="0",
        preferred_term=name,
        resolved_identifier=identifier,
        ingredient_json=json.dumps(
            {
                "preferred_term": name,
                "notes": notes,
                "concentration": {"value": "0", "unit": "MILLIMOLAR"},
            }
        ),
    )
    if action:
        row.update(
            variant_index="0",
            variant_name="Synthetic exposure",
            change_index=str(index),
            change_action=action,
            change_stage="exposure after stock culture",
            descriptor_role=role,
            descriptor_path=f"/variants/0/ingredient_changes/{index}/{role}",
            source_modification_index=str(index),
            source_text="Exact synthetic source text",
            evidence_json='[{"reference":"https://example.org/evidence","supports":"SUPPORT"}]',
            change_json=json.dumps({"action": action, "notes": notes}),
            component_field="variants/0/ingredient_changes",
            component_index=str(index),
        )
    return row


@pytest.fixture
def handoff(reviewed_fixture):  # noqa: F811 - pytest injects the imported native fixture.
    root, review, _output = reviewed_fixture
    folder = root / "handoff"
    bundle = folder / "bundle"
    bundle.mkdir(parents=True)
    long_note = 'Quoted "context"\twith a newline\n' + "x" * 140_000
    positive = [
        source_row(),
        source_row(action="ADD", notes=long_note),
        source_row(action="REPLACE", index=1),
        source_row("Beta", "CHEBI:2", action="ADD", index=3),
    ]
    ledger = [
        dict(positive[1], counts_as_presence="true"),
        dict(positive[2], counts_as_presence="true"),
        dict(
            source_row("Beta", "CHEBI:2", action="REPLACE", index=1, role="replaced_ingredient"),
            counts_as_presence="false",
        ),
        dict(
            source_row("Unresolved stock", "", action="REMOVE", index=2), counts_as_presence="false"
        ),
        dict(positive[3], counts_as_presence="true"),
    ]
    intake.write_tsv(bundle / "ingredient_occurrences.tsv", FIELDS, positive)
    intake.write_tsv(
        bundle / "variant_ingredient_changes.tsv", FIELDS + ["counts_as_presence"], ledger
    )
    intake.write_tsv(
        bundle / "ingredients_list.tsv",
        ["identifier", "occurrence_count"],
        [
            {"identifier": "CHEBI:1", "occurrence_count": 3},
            {"identifier": "CHEBI:2", "occurrence_count": 1},
        ],
    )
    intake.write_tsv(bundle / "ingredient_aggregation_errors.tsv", ["error"], [])
    for name in ("mapped_ingredients.yaml", "unmapped_ingredients.yaml"):
        (bundle / name).write_text("ingredients: []\n")
    counts = {
        "occurrences": 4,
        "base_direct_occurrences": 1,
        "variant_positive_occurrences": 3,
        "variant_context_only_mentions": 2,
        "variant_change_mentions": 5,
        "variant_change_events": 4,
        "variant_changes_by_action": {"ADD": 2, "REPLACE": 1, "REMOVE": 1},
    }
    producer = root / "producer"
    (producer / "scripts").mkdir(parents=True)
    script = producer / "scripts/ingredient_release_bundle.py"
    script.write_text(
        "import json\nprint(json.dumps("
        + repr(
            {
                "status": "VERIFIED_CANDIDATE",
                "assurance": "externally_pinned_manifest",
                "counts": counts,
            }
        )
        + "))\n"
    )
    recipe = producer / "data/normalized_yaml/algae/synthetic.yaml"
    recipe.parent.mkdir(parents=True)
    recipe.write_text("id: CultureMech:000001\n")
    archive = folder / "producer-source.tar.gz"
    with tarfile.open(archive, "w:gz") as output:
        output.add(producer, arcname="producer")
    manifest = {
        "contract": "culturemech-direct-ingredients-v2",
        "git": {"dirty": False, "commit": "a" * 40},
        "scope": "full_catalog_direct_ingredients",
        "counts": counts,
        "products": {name: intake.fingerprint(bundle / name) for name in intake.PRODUCTS},
        "inputs": {"algae/synthetic.yaml": intake.fingerprint(recipe)},
        "dependencies": {"scripts/ingredient_release_bundle.py": intake.fingerprint(script)},
    }
    intake.write_json(bundle / "manifest.json", manifest)
    coverage_dir = folder / "coverage"
    coverage_dir.mkdir()
    intake.write_tsv(
        folder / "original-review-queue.tsv",
        ["source_path", "source_sha256"],
        [{"source_path": "algae/synthetic.yaml", "source_sha256": "b" * 64}],
    )
    intake.write_tsv(coverage_dir / "coverage.tsv", ["status"], [{"status": "STRUCTURED"}])
    coverage = {
        "result": "PASS",
        "mode": "postapply",
        "applied_assertions": 4,
        "coverage_sha256": intake.fingerprint(coverage_dir / "coverage.tsv")["sha256"],
        "queue_sha256": intake.fingerprint(folder / "original-review-queue.tsv")["sha256"],
        "record_snapshots": [
            {
                "path": "data/normalized_yaml/algae/synthetic.yaml",
                "base_sha256": "b" * 64,
                "current_sha256": intake.fingerprint(recipe)["sha256"],
            }
        ],
        "queue_rows": 1,
        "queue_recipes": 1,
        "dispositions": {"STRUCTURED": 1},
    }
    intake.write_json(coverage_dir / "summary.json", coverage)
    receipt = {
        "status": "VERIFIED_SOURCE_CANDIDATE_PENDING_ADOPTION",
        "contract": manifest["contract"],
        "producer_commit": manifest["git"]["commit"],
        "manifest_sha256": intake.fingerprint(bundle / "manifest.json")["sha256"],
        "source_archive_sha256": intake.fingerprint(archive)["sha256"],
        "coverage_summary_sha256": intake.fingerprint(coverage_dir / "summary.json")["sha256"],
        "queue_sha256": coverage["queue_sha256"],
    }
    intake.write_json(folder / "handoff.json", receipt)
    return (
        root,
        folder,
        intake.fingerprint(folder / "handoff.json")["sha256"],
        review.name,
        positive,
        ledger,
    )


def prepared(handoff):
    root, source, pin, review, _positive, _ledger = handoff
    output = root / "prepared"
    result = intake.prepare(source, pin, output, Path(sys.executable), root=root, review=review)
    return root, output, result, intake.fingerprint(output / "intake.json")["sha256"]


def write_binding_review(root, output, pin, *, approve="Alpha"):
    packet = json.loads((output / "review-packet.json").read_text())
    decisions, entries = [], {}
    for case in packet["cases"]:
        candidate = case["candidate"]
        decision = {
            "case_id": case["case_id"],
            "row_sha256": intake.payload_sha256(case),
            "owner_record": candidate.get("owner_record", "source/bundle/manifest.json"),
            "disposition": (
                "SUPPORTED"
                if case["context"]["preferred_term"] == approve
                and not set(case["context"].get("held_fields", []))
                & {"SOURCE_CLAIM", "IDENTITY_FORM"}
                else "WITHHOLD"
            ),
            "review_reason": "Synthetic exact source review; unresolved identities explicitly withheld.",
            "review_evidence": "binding-evidence.json",
            "evidence_key": case["case_id"],
        }
        if decision["disposition"] == "SUPPORTED":
            supported = candidate["supported_canonical_rows"]
            decision["canonical_row_sha256"] = supported[0]["row_sha256"] if supported else "0" * 64
        entry = {
            key: decision[key]
            for key in ("row_sha256", "owner_record", "disposition", "review_reason")
        }
        entry["owner_record_sha256"] = candidate.get(
            "owner_record_sha256", packet["source_manifest_sha256"]
        )
        entries[case["case_id"]] = entry
        decisions.append(decision)
    intake.write_json(root / "binding-evidence.json", {"entries": entries})
    review = {
        "schema_version": 1,
        "intake_sha256": pin,
        "decisions": decisions,
        "inputs": {
            "binding-evidence.json": intake.fingerprint(root / "binding-evidence.json")["sha256"]
        },
    }
    intake.write_json(root / "binding-review.json", review)
    return review


def test_real_prepare_and_native_finalize_keep_all_context(handoff):
    root, output, manifest, pin = prepared(handoff)
    assert manifest["counts"]["source_occurrences"] == 4
    assert manifest["counts"]["context_only_mentions"] == 2
    assert manifest["canonical_sssom"]["counts"] == {"source": 2, "supported": 1, "withhold": 1}
    with intake.csv_reader(output / "source-mentions.tsv") as reader:
        mentions = list(reader)
    assert len(mentions) == 6
    assert sum(row["counts_as_presence"] == "true" for row in mentions) == 4
    exposure = next(
        row
        for row in mentions
        if row["change_action"] == "ADD" and row["preferred_term"] == "Alpha"
    )
    assert json.loads(exposure["ingredient_json"])["notes"].endswith("x" * 140_000)
    assert json.loads(exposure["ingredient_json"])["concentration"]["value"] == "0"
    assert exposure["change_stage"] == "exposure after stock culture"
    write_binding_review(root, output, pin)
    final = intake.finalize(output, pin, "binding-review.json", root / "reviewed", root=root)
    assert final["counts"] == {"SUPPORTED": 3, "WITHHOLD": 3}
    assert (root / "reviewed/reviewed-intake.json").is_file()
    with intake.csv_reader(root / "reviewed/withheld-bindings.tsv") as reader:
        withheld = list(reader)
    assert sum(int(row["context_only_mentions"]) for row in withheld) == 2
    final_pin = intake.fingerprint(root / "reviewed/reviewed-intake.json")["sha256"]
    assert (
        intake.verify_reviewed(
            output, pin, "binding-review.json", root / "reviewed", final_pin, root=root
        )["status"]
        == "VERIFIED_REVIEWED_SOURCE_INTAKE"
    )
    product = root / "reviewed/supported-bindings.tsv"
    product.write_bytes(product.read_bytes().replace(b"CHEBI:1", b"CHEBI:9"))
    final["files"]["supported-bindings.tsv"] = intake.fingerprint(product)
    receipt = root / "reviewed/reviewed-intake.json"
    receipt.write_text(json.dumps(final))
    with pytest.raises(ValueError, match="native replay"):
        intake.verify_reviewed(
            output,
            pin,
            "binding-review.json",
            root / "reviewed",
            intake.fingerprint(receipt)["sha256"],
            root=root,
        )


def test_canonical_withhold_cannot_be_overridden_by_source_review(handoff):
    root, output, _manifest, pin = prepared(handoff)
    write_binding_review(root, output, pin, approve="Beta")
    with pytest.raises(ValueError, match="supported native exact-identity"):
        intake.finalize(output, pin, "binding-review.json", root / "refused", root=root)
    assert not (root / "refused").exists()


def test_incomplete_source_review_is_not_completion(handoff):
    root, output, _manifest, pin = prepared(handoff)
    review = write_binding_review(root, output, pin)
    review["decisions"].pop()
    (root / "binding-review.json").write_text(json.dumps(review))
    with pytest.raises(ValueError, match="every intake case"):
        intake.finalize(output, pin, "binding-review.json", root / "refused", root=root)


def test_native_evidence_disagreement_and_source_payload_drift_are_rejected(handoff):
    root, output, _manifest, pin = prepared(handoff)
    review = write_binding_review(root, output, pin)
    review["decisions"][0]["review_reason"] = "Unreviewed replacement reason"
    (root / "binding-review.json").write_text(json.dumps(review))
    with pytest.raises(ValueError, match="disagrees"):
        intake.finalize(output, pin, "binding-review.json", root / "refused", root=root)
    with (output / "source/bundle/variant_ingredient_changes.tsv").open("a") as stream:
        stream.write("\n")
    with pytest.raises(ValueError, match="Input changed"):
        intake.verify_intake(output, pin, root)


def test_changed_mim_owner_or_added_owner_invalidates_prior_intake(handoff):
    root, output, _manifest, pin = prepared(handoff)
    path = root / "data/ingredients/mapped/Additional.yaml"
    path.write_text("identifier: CHEBI:3\npreferred_term: Alpha\nmapping_status: MAPPED\n")
    with pytest.raises(ValueError, match="membership/bytes changed"):
        intake.verify_intake(output, pin, root)


def test_unknown_contract_and_overlapping_output_refuse_before_writes(handoff):
    root, source, pin, review, _positive, _ledger = handoff
    with pytest.raises(ValueError, match="overlaps"):
        intake.prepare(
            source, pin, source / "child", Path(sys.executable), root=root, review=review
        )
    manifest_path = source / "bundle/manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["contract"] = "unrecognized-v99"
    manifest_path.write_text(json.dumps(manifest))
    receipt_path = source / "handoff.json"
    receipt = json.loads(receipt_path.read_text())
    receipt["manifest_sha256"] = intake.fingerprint(manifest_path)["sha256"]
    receipt_path.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="Unsupported"):
        intake.verify_handoff(source, intake.fingerprint(receipt_path)["sha256"])
    assert not (source / "child").exists()


@pytest.mark.parametrize(
    "mutation", ["presence", "missing_positive", "unknown_action", "duplicate_context"]
)
def test_ledger_semantics_are_not_inferred_from_not_remove(handoff, mutation):
    root, source, _pin, _review, _positive, ledger = handoff
    manifest = json.loads((source / "bundle/manifest.json").read_text())
    ledger = copy.deepcopy(ledger)
    if mutation == "presence":
        ledger[2]["counts_as_presence"] = "true"
    elif mutation == "missing_positive":
        ledger.pop(0)
    elif mutation == "unknown_action":
        ledger[3]["change_action"] = "NEW_UNREVIEWED_ACTION"
    else:
        ledger[3] = copy.deepcopy(ledger[2])
    path = source / "bundle/variant_ingredient_changes.tsv"
    path.unlink()
    intake.write_tsv(path, FIELDS + ["counts_as_presence"], ledger)
    target = root / "parse-only"
    target.mkdir()
    with pytest.raises(ValueError):
        intake.collect_cases(source / "bundle", target, manifest)


def test_corrupted_copy_never_publishes_intake(handoff, monkeypatch):
    root, source, pin, review, _positive, _ledger = handoff
    original = intake.shutil.copyfile

    def corrupt(src, dst):
        result = original(src, dst)
        Path(dst).write_bytes(b"corrupt")
        return result

    monkeypatch.setattr(intake.shutil, "copyfile", corrupt)
    with pytest.raises(ValueError, match="Copied source differs"):
        intake.prepare(
            source, pin, root / "refused", Path(sys.executable), root=root, review=review
        )
    assert not (root / "refused").exists()
