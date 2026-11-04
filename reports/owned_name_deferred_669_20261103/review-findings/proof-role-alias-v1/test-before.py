"""#669: exact export-only suppression never renews scientific authority."""

import csv
import io
import json
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import ingredient_bundle_refresh as refresh
from mediaingredientmech import owned_name_suppression_refresh as policy
from mediaingredientmech.ingredient_bundle_contract import content_sha256, read_json
from mediaingredientmech.validation.mapping_change_receipts import HISTORICAL_CONTEXT, RECEIPTS_DIR

ROOT = Path(__file__).resolve().parents[1]
PLAN = "reports/suppression/plan.json"
INVENTORY = "reports/suppression/inventory.json"
BASE_REVIEW = "reports/base.json"
EVIDENCE = "reports/evidence.json"
PUBLOG = "reports/suppression/application.json"
NEW_RECEIPT = RECEIPTS_DIR + "/suppression.json"
FIELDS = list(policy._SCHEMA["$defs"]["row"]["properties"])


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def tsv(fields, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def canonical(rows):
    return (
        b"# mapping_set_id: https://example.invalid/test\n# predicate_semantics: skos\n# mapping_date: 2026-01-01\n# mapping_set_version: 2026-01-01\n"
        + tsv(FIELDS, rows)
    )


def write(root, name, raw):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def artifact_hashes(values):
    return {name: content_sha256(values[name]) for name in policy.ARTIFACTS}


def receipt(number, before, after, changes, records=()):
    return {
        "schema_version": 1,
        "batch": "fixture-" + str(number),
        "sequence": number,
        "issue": policy.ISSUE,
        "scope": policy.SCOPE,
        "approval": policy.APPROVAL,
        "before_sha256": content_sha256(canonical(before)),
        "after_sha256": content_sha256(canonical(after)),
        "before_row_count": len(before),
        "after_row_count": len(after),
        "position_map": list(range(1, len(before) + 1)),
        "changed_rows": len(changes),
        "added_rows": 0,
        "removed_rows": 0,
        "records": list(records),
        "changes": changes,
        "touched_subjects": sorted({c["after"]["subject_id"] for c in changes}),
    }


def change(position, before, after):
    return {
        "kind": "changed",
        "before_position": position,
        "after_position": position,
        "before": before,
        "after": after,
    }


def build_case(root, *, multiple_credits=False):
    """Real local Git baseline and native four-link payload replay; no mocked proof."""
    root.mkdir()
    sources, obligations, rows, label_rows = {}, [], [], []
    for i in range(23):
        subject, owner, token = f"MIM:Subject_{i}", f"MIM:Credit_{i}", f"preferred {i}"
        for stem, term in ((f"Subject_{i}", f"subject {i}"), (f"Credit_{i}", token)):
            sources[f"data/ingredients/mapped/{stem}.yaml"] = yaml.safe_dump(
                {
                    "preferred_term": term,
                    "identifier": f"CHEBI:{10000+i}",
                    "mapping_status": "MAPPED",
                    "synonyms": [],
                }
            ).encode()
        row = dict.fromkeys(FIELDS, "")
        row.update(
            subject_id=subject,
            subject_label=f"subject {i}",
            predicate_id="skos:exactMatch",
            object_id=f"CHEBI:{10000+i}",
            object_label=f"subject {i}",
            object_source="CHEBI",
            mapping_date="2026-01-01",
            other=f"keep-{i}|{token}|tail-{i}",
        )
        rows.append(row)
        obligations.append(
            {"subject_id": subject, "token": token, "owned_by": owner, "disposition": "UNREVIEWED"}
        )
        label_rows.append(
            {"label": token, "match_type": "preferred_term", "identifier": f"CHEBI:{10000+i}"}
        )
    unselected = dict.fromkeys(FIELDS, "")
    unselected.update(
        subject_id="MIM:Unselected",
        subject_label="unselected",
        predicate_id="skos:exactMatch",
        object_id="CHEBI:99999",
        object_label="unselected",
        object_source="CHEBI",
        mapping_date="2026-01-01",
    )
    rows.append(unselected)
    sources["data/ingredients/mapped/Unselected.yaml"] = (
        b"preferred_term: unselected\nidentifier: CHEBI:99999\nmapping_status: MAPPED\n"
    )
    if multiple_credits:
        sources["data/ingredients/mapped/Credit_extra.yaml"] = sources[
            "data/ingredients/mapped/Credit_0.yaml"
        ]
    sources["data/curated/mapped_ingredients.yaml"] = b"ingredients: []\n"
    sources["data/curated/unmapped_ingredients.yaml"] = b"ingredients: []\n"
    for name in policy.PROTECTED:
        sources[name] = (ROOT / name).read_bytes()
    label_stream = io.StringIO()
    labels = csv.DictWriter(label_stream, fieldnames=list(label_rows[0]), lineterminator="\n")
    labels.writeheader()
    labels.writerows(label_rows)
    sources["docs/data/label_index.csv"] = label_stream.getvalue().encode()
    for name in (*policy.VERIFIERS, policy.SCHEMA):
        sources[name] = (ROOT / name).read_bytes()
    initial = deepcopy(rows)
    start_sha = content_sha256(canonical(initial))
    sources[HISTORICAL_CONTEXT[0]] = encoded(
        {"schema_version": 1, "source_sha256": start_sha, "rows": initial}
    )
    for name in HISTORICAL_CONTEXT[1:]:
        sources[name] = encoded(
            {
                "schema_version": 1,
                "before_sha256": start_sha,
                "after_sha256": start_sha,
                "row_count": len(rows),
                "changed_rows": 0,
                "changes": [],
            }
        )
    checkpoint = None
    for sequence in range(1, 4):
        old_rows = deepcopy(rows)
        rows[0]["comment"] = "historical link " + str(sequence)
        link = receipt(sequence, old_rows, rows, [change(1, old_rows[0], rows[0])])
        sources[f"{RECEIPTS_DIR}/prefix-{sequence}.json"] = encoded(link)
        if sequence == 1:
            checkpoint = link["after_sha256"]
    sources[policy.SSSOM_SOURCE] = canonical(rows)
    sources[policy.SIDECAR] = (ROOT / policy.SIDECAR).read_bytes()
    sources[policy.BASELINE] = tsv(["subject_id", "token", "owned_by", "disposition"], obligations)
    old_manifest = read_json((ROOT / policy.MANIFEST).read_bytes())
    old_manifest["artifacts"] = artifact_hashes(sources)
    old_manifest["artifacts"][policy.SSSOM_SOURCE] = checkpoint
    sources[policy.MANIFEST] = encoded(old_manifest)
    decisions = [
        {
            "source_position": i,
            "disposition": "WITHHOLD",
            "review_evidence": EVIDENCE,
            "evidence_key": str(i),
            "owner_record": f"data/ingredients/mapped/Subject_{i-1}.yaml",
        }
        for i in range(1, 25)
    ]
    decisions[-1]["owner_record"] = "data/ingredients/mapped/Unselected.yaml"
    sources[BASE_REVIEW] = encoded({"source_sssom": policy.SSSOM_SOURCE, "decisions": decisions})
    sources[EVIDENCE] = encoded(
        {"entries": {str(i): {"disposition": "WITHHOLD"} for i in range(1, 25)}}
    )
    for name, raw in sources.items():
        write(root, name, raw)
    for args in (
        ("init", "-q"),
        ("add", "."),
        (
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "native baseline",
        ),
    ):
        subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)
    baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    before = {
        name: sources[name] for name in (*policy.ARTIFACTS, policy.MANIFEST, BASE_REVIEW, EVIDENCE)
    }
    current = dict(before)
    inventory = {
        "schema_version": 1,
        "operation": "owned-name-suppression-inventory-v1",
        "baseline": baseline,
        "ingredient_sha256": {
            p: content_sha256(b) for p, b in sources.items() if p.startswith("data/ingredients/")
        },
        "aggregate_sha256": {
            p: content_sha256(b) for p, b in sources.items() if p.startswith("data/curated/")
        },
        "protected_sha256": {p: content_sha256(sources[p]) for p in policy.PROTECTED},
    }
    write(root, INVENTORY, encoded(inventory))
    after_rows = deepcopy(rows)
    pairs = []
    before_hashes = artifact_hashes(before)
    for i, obligation in enumerate(obligations, 1):
        source = f"data/ingredients/mapped/Subject_{i-1}.yaml"
        credits = [f"MIM:Credit_{i-1}"] + (
            ["MIM:Credit_extra"] if multiple_credits and i == 1 else []
        )
        pair = {
            "baseline_row": obligation,
            "token_key": obligation["token"].casefold(),
            "source_position": i,
            "selector": {
                **{k: rows[i - 1][k] for k in ("subject_id", "predicate_id", "object_id")},
                "field": "other",
            },
            "before_row": rows[i - 1],
            "after_other": f"keep-{i-1}|tail-{i-1}",
            "source_owner": {"path": source, "sha256": content_sha256(sources[source])},
            "credited_owners": [
                {
                    "subject_id": x,
                    "path": f"data/ingredients/mapped/{x.removeprefix('MIM:')}.yaml",
                    "sha256": content_sha256(
                        sources[f"data/ingredients/mapped/{x.removeprefix('MIM:')}.yaml"]
                    ),
                }
                for x in sorted(credits)
            ],
            "source_ref": "pending",
            "input_surfaces": ["prior_sssom"],
            "disposition": "SUPPRESS",
            "review_disposition": "WITHHOLD",
        }
        pair["source_ref"] = policy.source_reference(pair, before_hashes[policy.SSSOM_SOURCE])
        pairs.append(pair)
        after_rows[i - 1]["other"] = pair["after_other"]
    current[policy.SSSOM_SOURCE] = canonical(after_rows)
    current[policy.BASELINE] = before[policy.BASELINE].splitlines(keepends=True)[0]
    _, sidecar = policy._table(before[policy.SIDECAR])
    evidence = policy.ISSUE + "#issuecomment-12345"
    for pair in pairs:
        sidecar.append(
            {
                "subject_id": pair["before_row"]["subject_id"],
                "token_key": pair["token_key"],
                "token": pair["baseline_row"]["token"],
                "disposition": "SUPPRESS",
                **{
                    key: json.dumps(value, separators=(",", ":"))
                    for key, value in {
                        "owner_subject_ids": [p["subject_id"] for p in pair["credited_owners"]],
                        "input_surfaces": ["prior_sssom"],
                        "source_refs": [pair["source_ref"]],
                        "evidence_refs": [evidence],
                    }.items()
                },
            }
        )
    current[policy.SIDECAR] = tsv(policy._SIDECAR_FIELDS, sidecar)
    generation = {"producer_revision": "e" * 40}
    generated = {
        "candidate": current[policy.SSSOM_SOURCE],
        "sidecar": tsv(policy._SIDECAR_FIELDS, []),
    }
    generated["manifest"] = encoded(
        {
            "source_revisions": {"claw": generation["producer_revision"]},
            "external_sssom_validation": "passed",
            "artifacts": [
                {
                    "path": "/historical/output/" + key,
                    "role": role,
                    "sha256": content_sha256(generated[key]),
                }
                for key, role in (("candidate", "sssom"), ("sidecar", "suppressed_aliases"))
            ],
        }
    )
    generated["receipt"] = encoded(
        {
            "producer_revision": generation["producer_revision"],
            "candidate_sha256": content_sha256(generated["candidate"]),
            "sidecar_sha256": content_sha256(generated["sidecar"]),
            "native_generation_manifest_sha256": content_sha256(generated["manifest"]),
            "prior_sha256": before_hashes[policy.SSSOM_SOURCE],
            "input_bytes_unchanged": True,
            "scientific_approval_added": False,
        }
    )
    for key, raw in generated.items():
        name = "reports/suppression/generation/" + key
        write(root, name, raw)
        generation[key] = {"path": name, "sha256": content_sha256(raw)}
    plan = {
        "schema_version": 1,
        "operation": "owned-name-suppression-plan-v1",
        "issue": 669,
        "issue_url": policy.ISSUE,
        "scope": policy.SCOPE,
        "approval": policy.APPROVAL,
        "baseline": baseline,
        "policy_evidence": evidence,
        "artifacts_before": before_hashes,
        "artifacts_after": artifact_hashes(current),
        "unchanged_inventory": {"path": INVENTORY, "sha256": content_sha256(encoded(inventory))},
        "generation": generation,
        "receipt_sequence": 4,
        "pairs": pairs,
    }
    write(root, PLAN, encoded(plan))
    plan_ref = {"path": PLAN, "sha256": content_sha256(encoded(plan))}
    new_receipt = receipt(
        4,
        rows,
        after_rows,
        [change(i, rows[i - 1], after_rows[i - 1]) for i in range(1, 24)],
        [policy.expected_record(p, plan_ref) for p in pairs],
    )
    write(root, NEW_RECEIPT, encoded(new_receipt))
    update = {
        "schema_version": 1,
        "operation": "owned-name-suppression-update-v1",
        "issue": 669,
        "scope": policy.SCOPE,
        "approval": policy.APPROVAL,
        "baseline": baseline,
        "prior_manifest_sha256": content_sha256(before[policy.MANIFEST]),
        "plan": plan_ref,
        **{
            k: plan[k]
            for k in ("unchanged_inventory", "artifacts_before", "artifacts_after", "generation")
        },
        "historical_checkpoint": {
            "sequence": 1,
            "sssom_sha256": checkpoint,
            "bridge_sequences": [2, 3],
        },
        "mapping_receipt": {
            "path": NEW_RECEIPT,
            "sha256": content_sha256(encoded(new_receipt)),
            "sequence": 4,
        },
        "publication_log": PUBLOG,
    }
    manifest = deepcopy(old_manifest)
    manifest["artifacts"] = artifact_hashes(current)
    manifest[policy.UPDATE] = [update]
    current[policy.MANIFEST] = encoded(manifest)
    write(root, PUBLOG, b'{"synthetic_test_attribution":true}\n')
    for name, raw in current.items():
        write(root, name, raw)
    return {
        "root": root,
        "baseline": baseline,
        "prior": {"base_review": BASE_REVIEW},
        "before": before,
        "current": current,
        "plan": plan,
        "manifest": manifest,
        "receipt": new_receipt,
    }


@pytest.fixture
def case(tmp_path):
    return build_case(tmp_path / "case")


def context(case):
    return refresh.OwnedNameSuppressionContext(
        case["root"], case["baseline"], content_sha256(case["current"][policy.MANIFEST])
    )


def verify(case, ctx=None):
    return policy.verify_owned_name_suppression(
        case["prior"], case["before"], case["current"], context(case) if ctx is None else ctx
    )


def repin(case, *, plan=False, receipt=False):
    root, manifest = case["root"], case["manifest"]
    update = manifest[policy.UPDATE][-1]
    if plan:
        raw = encoded(case["plan"])
        write(root, PLAN, raw)
        update["plan"]["sha256"] = content_sha256(raw)
        # Rebinding all dependent attribution must not bypass independent derivation.
        for record in case["receipt"]["records"]:
            record["verification"] = (
                f"Owned-name export policy #669; preferred-name credits and prior-only provenance are frozen in {PLAN} sha256={content_sha256(raw)}."
            )
        receipt = True
    if receipt:
        raw = encoded(case["receipt"])
        write(root, NEW_RECEIPT, raw)
        update["mapping_receipt"]["sha256"] = content_sha256(raw)
    case["current"][policy.MANIFEST] = encoded(manifest)
    for name, raw in case["current"].items():
        write(root, name, raw)


def test_real_native_bridge_and_exact_export_only_transition(case):
    proof = verify(case)
    assert proof["scientific_approval_added"] is False
    assert proof["appended_update"]["historical_checkpoint"]["bridge_sequences"] == [2, 3]
    assert len(proof["receipt_paths"]) == 4
    assert len(proof["source_paths"]["data/ingredients"]) == 47
    assert proof["input_sha256"][policy.SSSOM_SOURCE] == content_sha256(
        case["current"][policy.SSSOM_SOURCE]
    )


def test_complete_native_credits_need_not_be_a_singleton(tmp_path):
    case = build_case(tmp_path / "multiple", multiple_credits=True)
    assert len(case["plan"]["pairs"][0]["credited_owners"]) == 2
    assert case["plan"]["pairs"][0]["baseline_row"]["owned_by"] == "MIM:Credit_0"
    assert verify(case)["scientific_approval_added"] is False


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "duplicate",
        "position",
        "payload",
        "credit",
        "origin",
        "source_ref",
        "unknown",
    ],
)
def test_repinned_plan_cannot_change_scope(case, mutation):
    pairs = case["plan"]["pairs"]
    if mutation == "missing":
        pairs.pop()
    elif mutation == "extra":
        pairs.append(deepcopy(pairs[0]))
    elif mutation == "duplicate":
        pairs[-1] = deepcopy(pairs[0])
    elif mutation == "position":
        pairs[0]["source_position"] = 2
    elif mutation == "payload":
        pairs[0]["before_row"]["comment"] = "guessed"
    elif mutation == "credit":
        pairs[0]["credited_owners"][0]["subject_id"] = "MIM:Credit_1"
    elif mutation == "origin":
        pairs[0]["input_surfaces"] = ["mim.synonym"]
    elif mutation == "source_ref":
        pairs[0]["source_ref"] += "-fabricated"
    else:
        case["plan"]["allowed_mutations"] = ["anything"]
    repin(case, plan=True)
    with pytest.raises(ValueError):
        verify(case)


@pytest.mark.parametrize(
    "failure",
    [
        "owner",
        "aggregate",
        "label_index",
        "unified",
        "pin",
        "hidden_owner",
        "owner_symlink",
        "code",
    ],
)
def test_source_and_protected_inventories_fail_closed(case, failure):
    root = case["root"]
    targets = {
        "owner": "data/ingredients/mapped/Subject_0.yaml",
        "aggregate": "data/curated/mapped_ingredients.yaml",
        "label_index": "docs/data/label_index.csv",
        "unified": "UNIFIED_INGREDIENT_MAPPING.tsv",
        "pin": "scripts/.vendored_canon_ref",
        "code": policy.VERIFIERS[0],
    }
    if failure == "hidden_owner":
        write(root, "data/ingredients/mapped/.ignored/new.yaml", b"preferred_term: stolen\n")
    elif failure == "owner_symlink":
        (root / "data/ingredients/mapped/Alias.yaml").symlink_to(root / targets["owner"])
    else:
        (root / targets[failure]).write_bytes((root / targets[failure]).read_bytes() + b"\n")
    with pytest.raises(ValueError):
        verify(case)


@pytest.mark.parametrize(
    "failure",
    [
        "history",
        "owner_map",
        "checkpoint",
        "bridge",
        "prefix",
        "extra_receipt",
        "unknown_update",
        "approval",
    ],
)
def test_manifest_and_receipt_history_cannot_be_rebound(case, failure):
    update = case["manifest"][policy.UPDATE][-1]
    if failure == "history":
        case["manifest"]["scope"] = "rewritten historical claim"
    elif failure == "owner_map":
        case["manifest"]["source_owner_sha256"] = {}
    elif failure == "checkpoint":
        update["historical_checkpoint"]["sssom_sha256"] = "0" * 64
    elif failure == "bridge":
        update["historical_checkpoint"]["bridge_sequences"] = [3]
    elif failure == "prefix":
        p = case["root"] / RECEIPTS_DIR / "prefix-1.json"
        doc = read_json(p.read_bytes())
        doc["scope"] = "rewrite"
        p.write_bytes(encoded(doc))
    elif failure == "extra_receipt":
        write(case["root"], RECEIPTS_DIR + "/.hidden/copy.json", encoded(case["receipt"]))
    elif failure == "unknown_update":
        update["allow_unreviewed"] = True
    else:
        case["receipt"]["approval"] = "APPROVED: borrowed review"
    repin(case, receipt=failure == "approval")
    with pytest.raises(ValueError):
        verify(case)


@pytest.mark.parametrize(
    "failure",
    [
        "comment",
        "header",
        "other_order",
        "leftover",
        "baseline_header",
        "sidecar_history",
        "sidecar_origin",
        "candidate_origin",
    ],
)
def test_exact_artifact_transition_rejects_consistently_repinned_edits(case, failure):
    current = case["current"]
    if failure in {"comment", "header", "other_order", "leftover"}:
        a, b = {
            "comment": (b"historical link 3", b"unrelated edit"),
            "header": (b"# mapping_date: 2026-01-01", b"# mapping_date: 2026-01-02"),
            "other_order": (b"keep-0|tail-0", b"tail-0|keep-0"),
            "leftover": (b"keep-0|tail-0", b"keep-0|preferred 0|tail-0"),
        }[failure]
        current[policy.SSSOM_SOURCE] = current[policy.SSSOM_SOURCE].replace(a, b, 1)
    elif failure == "baseline_header":
        current[policy.BASELINE] = current[policy.BASELINE].replace(b"owned_by", b"owner")
    elif failure == "sidecar_history":
        current[policy.SIDECAR] = current[policy.SIDECAR].replace(b"Vibriostat", b"fabricated", 1)
    elif failure == "sidecar_origin":
        current[policy.SIDECAR] = current[policy.SIDECAR].replace(b"prior_sssom", b"mim.synonym")
    else:
        g = case["plan"]["generation"]
        raw = (
            (case["root"] / g["candidate"]["path"])
            .read_bytes()
            .replace(b"keep-0|tail-0", b"keep-0|preferred 0|tail-0", 1)
        )
        write(case["root"], g["candidate"]["path"], raw)
        g["candidate"]["sha256"] = content_sha256(raw)
        m = read_json((case["root"] / g["manifest"]["path"]).read_bytes())
        m["artifacts"][0]["sha256"] = content_sha256(raw)
        write(case["root"], g["manifest"]["path"], encoded(m))
        g["manifest"]["sha256"] = content_sha256(encoded(m))
        r = read_json((case["root"] / g["receipt"]["path"]).read_bytes())
        r["candidate_sha256"] = content_sha256(raw)
        r["native_generation_manifest_sha256"] = content_sha256(encoded(m))
        write(case["root"], g["receipt"]["path"], encoded(r))
        g["receipt"]["sha256"] = content_sha256(encoded(r))
    hashes = artifact_hashes(current)
    case["plan"]["artifacts_after"] = hashes
    case["manifest"]["artifacts"] = hashes
    case["manifest"][policy.UPDATE][-1]["artifacts_after"] = hashes
    repin(case, plan=True)
    with pytest.raises(ValueError):
        verify(case)


def test_actual_supported_affected_row_is_rejected(case):
    for values in (case["before"], case["current"]):
        base = read_json(values[BASE_REVIEW])
        base["decisions"][0]["disposition"] = "SUPPORTED"
        values[BASE_REVIEW] = encoded(base)
    # Commit the changed historical decision so this tests the scientific guard,
    # not only the durable-before hash comparison.
    root = case["root"]
    write(root, BASE_REVIEW, case["before"][BASE_REVIEW])
    subprocess.run(["git", "add", BASE_REVIEW], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "supported preimage",
        ],
        cwd=root,
        check=True,
    )
    baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    case["baseline"] = baseline
    case["plan"]["baseline"] = baseline
    case["manifest"][policy.UPDATE][-1]["baseline"] = baseline
    inventory = read_json((root / INVENTORY).read_bytes())
    inventory["baseline"] = baseline
    write(root, INVENTORY, encoded(inventory))
    case["plan"]["unchanged_inventory"]["sha256"] = content_sha256(encoded(inventory))
    repin(case, plan=True)
    with pytest.raises(ValueError, match="affected mapping is not withheld"):
        verify(case)


def test_native_replay_capture_cannot_be_replaced_after_restoration(case, monkeypatch):
    original = policy.verify_mapping_chain
    path = case["root"] / RECEIPTS_DIR / "prefix-1.json"
    saved = path.read_bytes()

    def substituted(root):
        doc = read_json(saved)
        doc["scope"] = "transient replay input"
        path.write_bytes(encoded(doc))
        try:
            return original(root)
        finally:
            path.write_bytes(saved)

    monkeypatch.setattr(policy, "verify_mapping_chain", substituted)
    with pytest.raises(ValueError, match="conflicting|changed"):
        verify(case)
    assert path.read_bytes() == saved


@pytest.mark.parametrize("kind", ["dict", "wrong_type", "wrong_pin", "alias"])
def test_explicit_typed_context_and_pin_required(case, kind):
    ctx = context(case)
    if kind == "dict":
        ctx = vars(ctx)
    elif kind == "wrong_type":
        ctx = refresh.FormProjectionContext(ctx.root, ctx.baseline, ctx.manifest_sha256)
    elif kind == "wrong_pin":
        ctx = refresh.OwnedNameSuppressionContext(ctx.root, ctx.baseline, "0" * 64)
    else:
        alias = ctx.root.parent / "alias"
        alias.symlink_to(ctx.root, target_is_directory=True)
        ctx = refresh.OwnedNameSuppressionContext(alias, ctx.baseline, ctx.manifest_sha256)
    with pytest.raises(ValueError):
        verify(case, ctx)


@pytest.mark.parametrize("kind", ["decision", "evidence"])
def test_unrelated_scientific_basis_cannot_move(case, kind):
    path = BASE_REVIEW if kind == "decision" else EVIDENCE
    value = read_json(case["current"][path])
    if kind == "decision":
        value["decisions"][-1]["review_reason"] = "new unrelated judgment"
    else:
        value["entries"]["24"]["basis"] = "invented unrelated support"
    case["current"][path] = encoded(value)
    write(case["root"], path, encoded(value))
    with pytest.raises(ValueError, match="unrelated base"):
        verify(case)


@pytest.mark.parametrize("kind", ["owner", "receipt"])
def test_post_reservation_exhaustive_membership_recheck(case, kind):
    proof = verify(case)
    policy.recheck_inventory(case["root"], proof)
    path = (
        "data/ingredients/mapped/.ignored/new.yaml"
        if kind == "owner"
        else RECEIPTS_DIR + "/.ignored/new.json"
    )
    write(case["root"], path, b"{}\n")
    with pytest.raises(ValueError):
        policy.recheck_inventory(case["root"], proof)
    assert (case["root"] / path).read_bytes() == b"{}\n"


def test_new_context_is_mutually_exclusive_with_every_legacy_context(case):
    for key, cls in (
        ("form_projection", refresh.FormProjectionContext),
        ("registry_correction", refresh.RegistryCorrectionContext),
        ("stock_cas_removal", refresh.StockCasRemovalContext),
    ):
        ctx = context(case)
        with pytest.raises(ValueError, match="mutually exclusive"):
            refresh.verify_unchanged_cohort(
                None,
                None,
                None,
                None,
                None,
                owned_name_suppression=ctx,
                **{key: cls(ctx.root, ctx.baseline, ctx.manifest_sha256)},
            )


def test_cli_rejects_mixed_context_flags_before_reading_inputs(case):
    with pytest.raises(SystemExit) as failure:
        refresh.main(
            [
                "--root",
                str(case["root"]),
                "--baseline",
                case["baseline"],
                "--prior-review",
                "absent.json",
                "--output",
                "new.json",
                "--receipt",
                "receipt.json",
                "--prior-copy",
                "prior.json",
                "--owned-name-suppression-manifest-sha256",
                "0" * 64,
                "--stock-cas-removal-manifest-sha256",
                "0" * 64,
            ]
        )
    assert failure.value.code == 2
    assert not (case["root"] / "new.json").exists()


@pytest.mark.parametrize("field", ["issue", "receipt_sequence"])
def test_integer_fields_do_not_accept_equal_floats(case, field):
    case["plan"][field] = float(case["plan"][field])
    repin(case, plan=True)
    with pytest.raises(ValueError, match="integer"):
        verify(case)


def test_verifier_imports_from_installed_package_layout(tmp_path):
    import shutil
    import sys

    installed = tmp_path / "site-packages"
    shutil.copytree(
        ROOT / "src/mediaingredientmech",
        installed / "mediaingredientmech",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    result = subprocess.run(
        [
            sys.executable,
            "-I",
            "-c",
            "import sys; sys.path.insert(0, sys.argv[1]); from mediaingredientmech import owned_name_suppression_refresh as p; assert len(p._LOADED) == len(p.VERIFIERS) + 1",
            str(installed),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
