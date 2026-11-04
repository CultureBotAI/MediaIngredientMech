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
    manifest[policy.UPDATE] = [*old_manifest.get(policy.UPDATE, []), update]  # #1134
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


@pytest.mark.parametrize(
    "role",
    [
        PLAN,
        INVENTORY,
        *policy.ARTIFACTS,
        policy.MANIFEST,
        "data/ingredients/mapped/Subject_0.yaml",
        "data/ingredients/mapped/Credit_0.yaml",
        "data/curated/mapped_ingredients.yaml",
        "UNIFIED_INGREDIENT_MAPPING.tsv",
        "docs/data/label_index.csv",
        *(
            "reports/suppression/generation/" + name
            for name in ("candidate", "sidecar", "manifest", "receipt")
        ),
        NEW_RECEIPT,
        RECEIPTS_DIR + "/prefix-1.json",
        *HISTORICAL_CONTEXT,
        BASE_REVIEW,
        EVIDENCE,
        policy.VERIFIERS[0],
        policy.SCHEMA,
    ],
)
def test_issue1132_publication_log_cannot_reuse_another_proof_role(case, role):
    case["manifest"][policy.UPDATE][-1]["publication_log"] = role
    repin(case)
    with pytest.raises(ValueError, match="publication log reuses another proof role"):
        verify(case)


@pytest.mark.parametrize("role", [PLAN, policy.SSSOM_SOURCE, BASE_REVIEW, policy.VERIFIERS[0]])
def test_issue1132_publication_log_cannot_hard_link_another_proof_role(case, role):
    log = case["root"] / PUBLOG
    log.unlink()
    log.hardlink_to(case["root"] / role)
    with pytest.raises(ValueError, match="publication log aliases another proof role"):
        verify(case)


def test_issue1132_distinct_log_binds_actual_bytes_without_claiming_transition_proof(case):
    # Equal bytes are allowed; a separate inode and role are required.
    raw = (case["root"] / PLAN).read_bytes()
    write(case["root"], PUBLOG, raw)
    proof = verify(case)
    assert proof["input_sha256"][PUBLOG] == content_sha256(raw)
    assert proof["scientific_approval_added"] is False
    assert not (case["root"] / PUBLOG).samefile(case["root"] / PLAN)
    policy.recheck_inventory(case["root"], proof)


def test_issue1132_post_reservation_recheck_rejects_same_byte_hard_link(case):
    raw = (case["root"] / PLAN).read_bytes()
    write(case["root"], PUBLOG, raw)
    proof = verify(case)
    log = case["root"] / PUBLOG
    log.unlink()
    log.hardlink_to(case["root"] / PLAN)
    assert content_sha256(log.read_bytes()) == proof["input_sha256"][PUBLOG]
    with pytest.raises(ValueError, match="publication log aliases another proof role"):
        policy.recheck_inventory(case["root"], proof)


def issue1132_cli_setup(case, monkeypatch):
    """Isolate CLI role plumbing while retaining real native context replay and publication."""
    root = case["root"]
    prior_path, loaded_path = "reports/prior-companion.json", "reports/loaded-review-input.json"
    case["prior"]["record_inputs"] = {}
    write(root, prior_path, encoded(case["prior"]))
    write(root, loaded_path, b'{"synthetic_loaded_input":true}\n')
    subprocess.run(["git", "add", prior_path, loaded_path], cwd=root, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "#1132 CLI fixture inputs",
        ],
        cwd=root,
        check=True,
        capture_output=True,
    )
    baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    case["baseline"] = case["plan"]["baseline"] = baseline
    inventory = read_json((root / INVENTORY).read_bytes())
    inventory["baseline"] = baseline
    write(root, INVENTORY, encoded(inventory))
    case["plan"]["unchanged_inventory"]["sha256"] = content_sha256(encoded(inventory))
    case["manifest"][policy.UPDATE][-1]["baseline"] = baseline
    repin(case, plan=True)

    # The synthetic fixture has no companion claims. Only those unrelated outer
    # loaders are stubbed; the new context, Git history, receipts and writer run.
    monkeypatch.setattr(refresh, "source_names", lambda prior: set(case["before"]))
    monkeypatch.setattr(
        refresh,
        "load_review",
        lambda root, path: {
            "input_snapshot": {
                root / loaded_path: content_sha256((root / loaded_path).read_bytes())
            }
        },
    )

    def real_context(prior, before, current, old_contracts, new_contracts, **contexts):
        assert old_contracts == new_contracts
        assert all(
            value is None for key, value in contexts.items() if key != "owned_name_suppression"
        )
        proof = policy.verify_owned_name_suppression(
            prior, before, current, contexts["owned_name_suppression"]
        )
        return deepcopy(prior), {"owned_name_suppression": proof, "claim_counts": {}}

    monkeypatch.setattr(refresh, "verify_unchanged_cohort", real_context)
    return prior_path, loaded_path


def issue1132_cli_argv(case):
    return [
        "--root",
        str(case["root"]),
        "--baseline",
        case["baseline"],
        "--prior-review",
        "reports/prior-companion.json",
        "--output",
        "reports/successor.json",
        "--receipt",
        "reports/refresh.json",
        "--prior-copy",
        "reports/prior-copy.json",
        "--owned-name-suppression-manifest-sha256",
        content_sha256(case["current"][policy.MANIFEST]),
    ]


@pytest.mark.parametrize("target", ["prior", "loaded"])
def test_issue1132_cli_rejects_caller_only_proof_role_reuse(case, monkeypatch, target):
    prior_path, loaded_path = issue1132_cli_setup(case, monkeypatch)
    case["manifest"][policy.UPDATE][-1]["publication_log"] = (
        prior_path if target == "prior" else loaded_path
    )
    repin(case)
    with pytest.raises(ValueError, match="publication log reuses another proof role"):
        refresh.main(issue1132_cli_argv(case))
    assert all(
        not (case["root"] / ("reports/" + name)).exists()
        for name in ("successor.json", "refresh.json", "prior-copy.json")
    )


@pytest.mark.parametrize("option", ["--output", "--receipt", "--prior-copy"])
def test_issue1132_cli_rejects_publication_log_as_output(case, monkeypatch, option):
    issue1132_cli_setup(case, monkeypatch)
    argv = issue1132_cli_argv(case)
    argv[argv.index(option) + 1] = PUBLOG
    old_log = (case["root"] / PUBLOG).read_bytes()
    with pytest.raises(ValueError, match="Output collides with a source input"):
        refresh.main(argv)
    assert (case["root"] / PUBLOG).read_bytes() == old_log
    assert all(
        not (case["root"] / ("reports/" + name)).exists()
        for name in ("successor.json", "refresh.json", "prior-copy.json")
    )


def test_issue1132_cli_publishes_with_distinct_log_and_real_native_proof(case, monkeypatch):
    prior_path, _ = issue1132_cli_setup(case, monkeypatch)
    refresh.main(issue1132_cli_argv(case))
    audit = read_json((case["root"] / "reports/refresh.json").read_bytes())
    proof = audit["owned_name_suppression"]
    assert proof["scientific_approval_added"] is False
    assert proof["input_sha256"][PUBLOG] == content_sha256((case["root"] / PUBLOG).read_bytes())
    assert (case["root"] / "reports/prior-copy.json").read_bytes() == (
        case["root"] / prior_path
    ).read_bytes()
    assert read_json((case["root"] / "reports/successor.json").read_bytes()) == case["prior"]


def test_issue1132_cli_rechecks_prior_companion_alias_after_reservation(case, monkeypatch):
    prior_path, _ = issue1132_cli_setup(case, monkeypatch)
    write(case["root"], PUBLOG, (case["root"] / prior_path).read_bytes())
    real_publish = refresh.publish_new_files

    def publish(outputs, verify_snapshot):
        def alias_then_verify():
            log = case["root"] / PUBLOG
            log.unlink()
            log.hardlink_to(case["root"] / prior_path)
            verify_snapshot()

        real_publish(outputs, alias_then_verify)

    monkeypatch.setattr(refresh, "publish_new_files", publish)
    with pytest.raises(ValueError, match="publication log aliases another proof role"):
        refresh.main(issue1132_cli_argv(case))
    assert all(
        not (case["root"] / ("reports/" + name)).exists()
        for name in ("successor.json", "refresh.json", "prior-copy.json")
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


def issue1133_form_case(case):
    """Add one historical fixture authority; real Git/native replay still governs the suffix."""
    root = case["root"]
    owner = "data/ingredients/mapped/Unselected.yaml"
    owner_hash = content_sha256((root / owner).read_bytes())
    prefix = RECEIPTS_DIR + "/prefix-1.json"
    first = read_json((root / prefix).read_bytes())
    first["records"] = [
        {
            "source_record": owner,
            "before_yaml_sha256": owner_hash,
            "after_yaml_sha256": owner_hash,
            "shape": "synthetic_historical_form",
        }
    ]
    write(root, prefix, encoded(first))
    native_paths = [
        "reports/form-fixture/review.yaml",
        "reports/form-fixture/review.md",
        "reports/form-fixture/evidence.json",
    ]
    for name in native_paths:
        write(root, name, b"Synthetic immutable fixture; no real scientific approval.\n")
    proof = policy.verify_mapping_chain(root)
    row = proof["state"][23]
    checkpoint = {
        "sequence": 1,
        "path": prefix,
        "sha256": content_sha256(encoded(first)),
        "after_sha256": first["after_sha256"],
    }
    claim = {
        "claim_kind": "primary_identity",
        "source_position": 24,
        "mapping": row,
        "row_sha256": content_sha256(refresh.canonical_json(row)),
        "disposition": "SUPPORTED",
        "reason": "Preserve the historical synthetic fixture decision.",
        "assessment_id": "synthetic-assessment",
        "prior_basis": None,
    }
    authority_path = "reports/form-fixture/authority.json"
    authority = {
        "schema_version": 1,
        "owner_record": owner,
        "owner_record_sha256": owner_hash,
        "checkpoint": checkpoint,
        "decisions": [claim],
        "evidence_inputs": {native_paths[2]: content_sha256((root / native_paths[2]).read_bytes())},
        "native_review": {
            "path": native_paths[0],
            "sha256": content_sha256((root / native_paths[0]).read_bytes()),
            "markdown_sha256": content_sha256((root / native_paths[1]).read_bytes()),
        },
    }
    write(root, authority_path, encoded(authority))

    def continuation(chain):
        return [
            {
                "sequence": r["sequence"],
                "path": path,
                "sha256": chain["receipt_inputs"][path],
                "before_position": 24,
                "after_position": 24,
            }
            for r, path in zip(chain["receipts"][1:], chain["receipt_paths"][1:], strict=True)
        ]

    form = {
        "file": authority_path,
        "claim_kind": claim["claim_kind"],
        "row_sha256": claim["row_sha256"],
        "native_review": authority["native_review"],
        "assessment_id": claim["assessment_id"],
        "checkpoint": checkpoint,
        "prior_basis": None,
        "continuation": continuation(proof)[:-1],
    }
    old = {
        "row_sha256": claim["row_sha256"],
        "owner_record": owner,
        "owner_record_sha256": owner_hash,
        "disposition": claim["disposition"],
        "review_reason": claim["reason"],
        "basis": {
            "form_followup": form,
            "superseded_scoped_review": {
                "reason": "Historical fixture concern stays unchanged.",
                "receipt_inputs": {
                    p: proof["receipt_inputs"][p] for p in proof["receipt_paths"][:-1]
                },
            },
        },
    }
    evidence = read_json(case["before"][EVIDENCE])
    evidence["entries"]["24"] = old
    review = read_json(case["before"][BASE_REVIEW])
    review["decisions"][-1].update(
        disposition=claim["disposition"],
        row_sha256=claim["row_sha256"],
        review_reason=claim["reason"],
    )
    for name, doc in [(EVIDENCE, evidence), (BASE_REVIEW, review)]:
        case["before"][name] = case["current"][name] = encoded(doc)
        write(root, name, encoded(doc))
    subprocess.run(
        ["git", "add", prefix, authority_path, *native_paths, EVIDENCE, BASE_REVIEW],
        cwd=root,
        check=True,
    )
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "#1133 historical form fixture",
        ],
        cwd=root,
        check=True,
        capture_output=True,
    )
    baseline = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    case["baseline"] = case["plan"]["baseline"] = baseline
    inventory = read_json((root / INVENTORY).read_bytes())
    inventory["baseline"] = baseline
    write(root, INVENTORY, encoded(inventory))
    case["plan"]["unchanged_inventory"]["sha256"] = content_sha256(encoded(inventory))
    case["manifest"][policy.UPDATE][-1]["baseline"] = baseline
    repin(case, plan=True)
    proof = policy.verify_mapping_chain(root)
    new = deepcopy(old)
    new["basis"]["form_followup"]["continuation"] = continuation(proof)
    new["basis"]["superseded_scoped_review"]["receipt_inputs"] = dict(proof["receipt_inputs"])
    evidence["entries"]["24"] = new
    case["current"][EVIDENCE] = encoded(evidence)
    write(root, EVIDENCE, encoded(evidence))
    return old, new, proof, owner_hash


def test_issue1133_native_context_continues_existing_form_without_new_approval(case):
    old, new, proof, _ = issue1133_form_case(case)
    result = verify(case)
    assert result["scientific_approval_added"] is False
    assert old["disposition"] == new["disposition"] == "SUPPORTED"
    assert (
        new["basis"]["form_followup"]["continuation"][:-1]
        == old["basis"]["form_followup"]["continuation"]
    )
    assert new["basis"]["superseded_scoped_review"]["receipt_inputs"] == proof["receipt_inputs"]


@pytest.mark.parametrize(
    "mutation",
    [
        "reason",
        "owner",
        "row",
        "approval",
        "native_authority",
        "extra_field",
        "old_reason",
        "old_continuation",
        "old_receipt_inputs",
        "old_checkpoint",
        "authority_claim",
        "authority_hash",
        "suffix_sequence",
        "suffix_path",
        "suffix_hash",
        "suffix_before",
        "suffix_after",
        "missing_suffix",
        "extra_suffix",
        "missing_receipt_input",
        "wrong_receipt_input",
        "extra_receipt_input",
        "new_supersession",
        "new_authority",
        "touched_row",
        "removed_row",
        "owner_chain_changed",
    ],
)
def test_issue1133_provenance_permission_preserves_every_other_boundary(case, mutation):
    old, new, proof, owner_hash = issue1133_form_case(case)
    suffix = new["basis"]["form_followup"]["continuation"][-1]
    if mutation in {"reason", "owner", "row", "approval"}:
        key = {
            "reason": "review_reason",
            "owner": "owner_record",
            "row": "row_sha256",
            "approval": "disposition",
        }[mutation]
        new[key] = "fabricated"
    elif mutation == "native_authority":
        new["basis"]["form_followup"]["assessment_id"] = "new authority"
    elif mutation == "extra_field":
        new["basis"]["fabricated"] = True
    elif mutation == "old_reason":
        old["review_reason"] = new["review_reason"] = "altered historical reason"
    elif mutation == "old_continuation":
        old["basis"]["form_followup"]["continuation"][0]["after_position"] = 1
        new["basis"]["form_followup"]["continuation"][0]["after_position"] = 1
    elif mutation == "old_receipt_inputs":
        key = proof["receipt_paths"][0]
        old["basis"]["superseded_scoped_review"]["receipt_inputs"][key] = "0" * 64
    elif mutation == "old_checkpoint":
        old["basis"]["form_followup"]["checkpoint"] = {"sequence": 0}
    elif mutation.startswith("authority_"):
        name = old["basis"]["form_followup"]["file"]
        doc = read_json((case["root"] / name).read_bytes())
        if mutation == "authority_claim":
            doc["decisions"][0]["disposition"] = "WITHHOLD"
        else:
            doc["evidence_inputs"][next(iter(doc["evidence_inputs"]))] = "0" * 64
        write(case["root"], name, encoded(doc))
    elif mutation.startswith("suffix_"):
        key = {
            "sequence": "sequence",
            "path": "path",
            "hash": "sha256",
            "before": "before_position",
            "after": "after_position",
        }[mutation.removeprefix("suffix_")]
        suffix[key] = "forged" if key in {"path", "sha256"} else 999
    elif mutation == "missing_suffix":
        new["basis"]["form_followup"]["continuation"].pop()
    elif mutation == "extra_suffix":
        new["basis"]["form_followup"]["continuation"].append(deepcopy(suffix))
    elif mutation == "missing_receipt_input":
        new["basis"]["superseded_scoped_review"]["receipt_inputs"].pop(NEW_RECEIPT)
    elif mutation == "wrong_receipt_input":
        new["basis"]["superseded_scoped_review"]["receipt_inputs"][NEW_RECEIPT] = "0" * 64
    elif mutation == "extra_receipt_input":
        new["basis"]["superseded_scoped_review"]["receipt_inputs"]["unknown.json"] = "0" * 64
    elif mutation == "new_supersession":
        old["basis"].pop("superseded_scoped_review")
    elif mutation == "new_authority":
        old["basis"].pop("form_followup")
    elif mutation == "touched_row":
        proof["receipts"][-1]["changes"].append({"before_position": 24})
    elif mutation == "removed_row":
        proof["receipts"][-1]["position_map"][23] = None
    else:
        proof["owner_chains"][old["owner_record"]].append(
            {"sequence": 4, "before_sha256": owner_hash, "after_sha256": "0" * 64}
        )
    with pytest.raises(ValueError):
        policy._continued_form_evidence(
            old, new, 24, owner_hash, proof, lambda p: (case["root"] / p).read_bytes()
        )


def test_issue1133_real_six_rows_replay_immutable_prefix_without_feature_history(tmp_path):
    directory = ROOT / "reports/owned_name_deferred_669_20261103"
    raw = (
        directory / "review-findings/native-continuation-refusal-v1/evidence-diffs.json"
    ).read_bytes()
    assert content_sha256(raw) == "98226f65e92df0ba75e6f9bf5ba169bde096856fc1ed7b297dcd9e71142b174b"
    examples = [item for item in read_json(raw) if not item["selected"]]
    assert [item["position"] for item in examples] == [926, 927, 2610, 2611, 3013, 3014]
    root = tmp_path / "native-replay"
    for name in HISTORICAL_CONTEXT:
        write(root, name, (ROOT / name).read_bytes())
    final = read_json((ROOT / RECEIPTS_DIR / "issue669-deferred-owned-aliases.json").read_bytes())
    for path in (ROOT / RECEIPTS_DIR).glob("*.json"):
        if read_json(path.read_bytes())["sequence"] <= final["sequence"]:
            write(root, path.relative_to(ROOT).as_posix(), path.read_bytes())
    write(
        root,
        policy.SSSOM_SOURCE,
        (directory / "proposed/ingredient_mappings.sssom.tsv").read_bytes(),
    )
    proof = policy.verify_mapping_chain(root)
    for item in examples:
        policy._continued_form_evidence(
            item["before"],
            item["after"],
            item["position"],
            item["before"]["owner_record_sha256"],
            proof,
            lambda p: (ROOT / p).read_bytes(),
        )
        assert item["before"]["disposition"] == item["after"]["disposition"] == "SUPPORTED"


def issue1134_prefix_case(tmp_path, monkeypatch, populated):
    original = Path.read_bytes
    source = ROOT / policy.MANIFEST
    manifest = read_json(original(source))
    history = deepcopy(manifest[policy.UPDATE]) if populated else []
    if populated:
        assert history  # The published deferred-alias update is immutable history.
    manifest[policy.UPDATE] = history
    raw = encoded(manifest)
    monkeypatch.setattr(Path, "read_bytes", lambda path: raw if path == source else original(path))
    case = build_case(tmp_path / "prefix-case")
    return case, history


@pytest.mark.parametrize("populated", [False, True])
def test_issue1134_fixture_appends_to_empty_or_complete_existing_prefix(
    tmp_path, monkeypatch, populated
):
    case, history = issue1134_prefix_case(tmp_path, monkeypatch, populated)
    assert read_json(case["before"][policy.MANIFEST])[policy.UPDATE] == history
    assert case["manifest"][policy.UPDATE][:-1] == history
    assert len(case["manifest"][policy.UPDATE]) == len(history) + 1
    assert verify(case)["scientific_approval_added"] is False


@pytest.mark.parametrize("mutation", ["delete", "alter"])
def test_issue1134_deleted_or_altered_prefix_still_rejects(tmp_path, monkeypatch, mutation):
    case, history = issue1134_prefix_case(tmp_path, monkeypatch, True)
    if mutation == "delete":
        del case["manifest"][policy.UPDATE][0]
    else:
        case["manifest"][policy.UPDATE][0]["scope"] = "altered historical scope"
    repin(case)
    assert read_json(case["before"][policy.MANIFEST])[policy.UPDATE] == history
    with pytest.raises(ValueError, match="expected one manifest history append"):
        verify(case)
