"""#1439: actual ancestral CAS withdrawal survives an unrelated native correction.

All records and decisions are synthetic. The original adoption, correction,
review, generation, publication and semantic gates execute without replacements.
Only constructor input records are customized before their original acquisition.
"""

from __future__ import annotations

import copy
import gzip
import json
import os
import shutil
import types
from pathlib import Path

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as publication
from mediaingredientmech.validation import semantic_transition
from tests import stable_publication_fixture as fixtures
from tests.test_curation_successor import SuccessorFixture, ref
from tests.test_curation_successor_history import (
    assert_exact_evidence,
    commit_paths,
    receipt_evidence,
)
from tests.test_curation_successor_transition import maintained, prepared
from tests.test_semantic_transition_cas import semantic_case_inputs
from tests.test_stable_id_adoption import api, commit, initialize, write
from tests.test_stable_sssom_publication import PublicationFixture, current_outputs

CLAW_HEAD = "7070392fcb5e31282499a599f7147b56b96e5aca"
CAS_POLICY = "2e43b009231d8ec6b1b9047b89294f2b850e136ff413aa327e5d085bc221bdb3"
RETIRED = "cas:138-86-7"
HELD = "CAS:89471-28-0"
OLD_OWNER = "data/ingredients/mapped/Move.yaml"
RETIRED_OWNER = "data/ingredients/unmapped/Move.yaml"
HELD_OWNER = "data/ingredients/mapped/Exact.yaml"
SECOND_OWNER = "data/ingredients/unmapped/New.yaml"


def _source_fixture(tmp_path, monkeypatch):
    """Supply original source inputs before the actual native adoption runs."""
    original_constructor = fixtures.NativeReviewAdoptionFixture.__init__

    def constructor(self, *args, **kwargs):
        records = copy.deepcopy(kwargs["original_records"])
        records[0]["chemical_properties"] = {"cas_rn": HELD.removeprefix("CAS:")}
        records[1]["legacy_identifiers"] = [RETIRED]
        records[1]["chemical_properties"] = {"cas_rn": RETIRED.removeprefix("cas:")}
        kwargs["original_records"] = records
        original_constructor(self, *args, **kwargs)

    # This changes fixture inputs, never a validator, producer or writer.
    with pytest.MonkeyPatch.context() as inputs:
        inputs.setattr(fixtures.NativeReviewAdoptionFixture, "__init__", constructor)
        f = SuccessorFixture(tmp_path, monkeypatch, publication_baseline=True)

    # As in the existing CAS fixture, these are deliberately historical mapping
    # inputs, never a current approved candidate. Bind both real roots before
    # inspecting or assessing the first correction; no completed receipt changes.
    canonical = f.predecessor / publication.CANONICAL
    original_manifest = (f.original.stage / "manifest.json").read_bytes()
    original_receipt = (f.original.receipt / "application.json").read_bytes()
    adopted = json.loads(original_manifest)
    assert publication.CANONICAL not in adopted["inputs"]
    assert publication.CANONICAL not in adopted["outputs"]
    assert not api.git(f.predecessor, "ls-files", "--", publication.CANONICAL)
    _, columns, rows = publication.read_sssom(canonical)
    assert len(rows) == 1
    withdrawn = copy.deepcopy(rows[0])
    withdrawn.update(
        subject_id="MIM:Move",
        subject_label="Move",
        object_id=RETIRED,
        object_label="Synthetic invalid historical CAS assertion",
        object_source="CAS",
        other="",
        validation_method="synthetic-prior-retirement-stamp",
    )
    rows[0]["other"] += "|" + HELD
    rows.append(withdrawn)
    historical = publication._render_candidate(canonical.read_bytes(), columns, rows)
    canonical.write_bytes(historical)
    (f.target / publication.CANONICAL).write_bytes(historical)
    assert (f.original.stage / "manifest.json").read_bytes() == original_manifest
    assert (f.original.receipt / "application.json").read_bytes() == original_receipt
    f.endpoint["publication_beforeimages"] = successor._optional_hashes(
        successor._optional(f.predecessor, successor.PUBLICATION)
    )
    f.request["predecessor"] = copy.deepcopy(f.endpoint)

    before = api.load_yaml((f.target / OLD_OWNER).read_bytes())
    assert before["identifier"] == "UNMAPPED_1"
    assert RETIRED in before["legacy_identifiers"]
    assert before["chemical_properties"]["cas_rn"] == RETIRED.removeprefix("cas:")
    after = copy.deepcopy(before)
    after["legacy_identifiers"].remove(RETIRED)
    del after["chemical_properties"]["cas_rn"]
    if not after["chemical_properties"]:
        del after["chemical_properties"]
    after["notes"] = "Synthetic reviewed withdrawal; original invalid CAS remains in history."
    _event(after, f.stamp, "withdrawal-primary", "Withdraw the invalid CAS alias and property.")
    api.write_validated_ingredient(after, f.proposal, schema_path=f.target / api.SCHEMA)
    hold = {"issue_key": "retained-quantity", "reason": "Source quantity remains unassessed"}
    f.request["operations"] = [
        _operation(f, OLD_OWNER, RETIRED_OWNER, before, after, [hold], [RETIRED])
    ]
    write(f.path, f.request)
    return f, historical, rows


def _event(record, stamp, curator, summary):
    api.record_curation_event(
        record,
        curator=curator,
        timestamp=stamp,
        action="MANUAL_CURATION",
        changes=summary,
        previous_status=record["mapping_status"],
        new_status=record["mapping_status"],
        llm_assisted=True,
        llm_model="synthetic-fixture",
    )


def _operation(f, old_path, new_path, before, after, holds, rejected):
    return {
        "mim_id": before["mim_id"],
        "before": ref(f.target, f.target / old_path),
        "after_path": new_path,
        "proposal": ref(f.target, f.proposal),
        "delta": successor._delta(before, after),
        "issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1439"],
        "evidence": [ref(f.target, f.target / "primary.txt")],
        "inherited_holds": copy.deepcopy(holds),
        "residual_holds": copy.deepcopy(holds),
        "rejected_identifiers": rejected,
        "rejected_labels": [],
        "primary": None,
        "skeptic": None,
    }


def _complete_source(f, name):
    before = maintained(f.target)
    tracked = set(api.git(f.target, "ls-files", "-z").decode().split("\0")) - {""}
    stage, acceptance, manifest = prepared(f)
    destination = f.target / ".temp" / name
    dry = successor.apply(f.target, stage, acceptance, destination, enabled=False)
    assert dry["applied"] is False and not destination.exists()
    assert maintained(f.target) == before
    result = successor.apply(f.target, stage, acceptance, destination, enabled=True)
    assert result["state"] == "COMPLETE" and result["release_approval_added"] is False
    receipt = destination / "application.json"
    evidence = receipt_evidence(f.target, stage, receipt)
    # A relocation can delete a tracked path. The adoption fixture also has
    # uncommitted newly relocated paths, which never had a Git index entry.
    # Commit every actual tracked deletion without inventing such an entry.
    for old in manifest["moves"]:
        assert not (f.target / old).exists()
    commit_names = {*manifest["outputs"], *(set(manifest["moves"]) & tracked)}
    head = commit_paths(f.target, sorted(commit_names), "Commit synthetic #1439 " + name)
    verified = successor.verify_completed(f.target, stage, receipt)
    assert verified["status"] == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    assert verified["current_identity"]["head"] == head
    assert_exact_evidence(evidence)
    endpoint = f.path.with_name("endpoint.json")
    write(
        endpoint,
        {
            "schema_version": 1,
            "capability": successor.CAPABILITY,
            "root": str(f.target),
            "stage": str(stage.relative_to(f.target)),
            "manifest": ref(f.target, stage / "manifest.json"),
            "receipt": ref(f.target, receipt),
            "producer": manifest["producer"],
        },
    )
    return endpoint, evidence


def _second_source(f, first_endpoint, directory):
    first = f.target
    endpoint = json.loads(first_endpoint.read_bytes())
    f.endpoint = {
        **copy.deepcopy(f.endpoint),
        "kind": "successor",
        "identity": successor._identity(first),
        **{key: endpoint[key] for key in ("stage", "manifest", "receipt", "producer")},
    }
    f.predecessor = first
    f.target = directory
    shutil.copytree(first, directory, ignore=shutil.ignore_patterns(".temp"))
    f.review_prefix = "unrelated-second-correction-"
    f.path = directory / "second-correction/request.json"
    f.proposal = f.path.with_name("proposal.yaml")
    f.context_path = f.path.with_name("context.json")
    f.payloads_path = f.path.with_name("payloads.json")
    f.proposal.parent.mkdir()
    f.before = {
        name: raw
        for name, raw in maintained(directory).items()
        if name.startswith("data/ingredients/")
    }
    before = api.load_yaml(f.before[SECOND_OWNER])
    after = copy.deepcopy(before)
    after["notes"] = "Independent synthetic method clarification; original role hold retained."
    _event(after, f.stamp, "second-primary", "Document an unrelated method; preserve role hold.")
    api.write_validated_ingredient(after, f.proposal, schema_path=directory / api.SCHEMA)
    holds = [{"issue_key": "role-provisional", "reason": "role provisional"}]
    f.request.update(
        identity=successor._identity(directory),
        predecessor=copy.deepcopy(f.endpoint),
        target_inventory={name: api.sha(raw) for name, raw in f.before.items()},
        target_inputs={
            name: api.sha((directory / name).read_bytes())
            for name in (*api.AGGREGATES, *successor.LEDGERS)
        },
        operations=[_operation(f, SECOND_OWNER, SECOND_OWNER, before, after, holds, [])],
        context=None,
        payloads=None,
        review_inputs={},
    )
    write(f.path, f.request)


def _cas_request(p, endpoint, rows):
    entries = []
    for number, (row, name, action, token_field, token) in enumerate(
        (
            (rows[0], HELD_OWNER, "RETAIN_INVALID_CAS_WITHHOLD", "other", HELD),
            (rows[1], RETIRED_OWNER, "RETIRE_INVALID_CAS", "object_id", RETIRED),
        ),
        1,
    ):
        owner = p.root / name
        entries.append(
            {
                "entry_id": "held-annotation" if number == 1 else "inherited-withdrawal",
                "row_position": number,
                "row": row,
                "invalid_tokens": [{"field": token_field, "token": token}],
                "owner": {
                    **ref(p.root, owner),
                    "mim_id": api.load_yaml(owner.read_bytes())["mim_id"],
                },
                "action": action,
                "reason": "Synthetic diagnostic accounting of exact original evidence; no release approval.",
                "hold": (
                    {
                        "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1439",
                        "reason": "Synthetic unresolved CAS annotation",
                    }
                    if number == 1
                    else None
                ),
                "evidence": ["primary.txt"],
            }
        )
    path = p.root / "current-cas-claims.json"
    claims = {
        "schema_version": 1,
        "capability": "reviewed-invalid-cas-dispositions-v1",
        "scope": "diagnostic_candidate_only",
        "scientific_approval": False,
        "author": "synthetic-current-diagnostic-author",
        "head": api.git(p.root, "rev-parse", "HEAD").decode().strip(),
        "canonical": ref(p.root, p.root / publication.CANONICAL),
        "source_correction": ref(p.root, endpoint),
        "evidence_inputs": {"primary.txt": api.sha((p.root / "primary.txt").read_bytes())},
        "entries": entries,
    }
    write(path, claims)
    targets = [
        {
            "target_id": entry["entry_id"],
            "kind": "snapshot_row",
            "label": entry["entry_id"],
            "path": path.name,
            "selector": entry["entry_id"],
            "owner_paths": [
                {
                    "repository": api.REPOSITORY,
                    "path": entry["owner"]["path"],
                    "role": "Current owner",
                }
            ],
            "semantic_digest": {
                "algorithm": "sha256-canonical-json-v1",
                "sha256": api.digest(entry),
                "description": "Complete diagnostic CAS disposition",
            },
        }
        for entry in entries
    ]
    inputs = [
        path.name,
        publication.CANONICAL,
        str(endpoint.relative_to(p.root)),
        "primary.txt",
        "MAPPING_SEMANTICS.md",
        "schema/record_review.yaml",
        "scripts/record_review.py",
        *[e["owner"]["path"] for e in entries],
    ]
    request = {
        "schema_version": 1,
        "capability": claims["capability"],
        "claims": ref(p.root, path),
        "reviews": [],
        "review_inputs": {},
    }
    for role in ("primary", "skeptic"):
        report = p.adoption.report("current-chain-cas-" + role, targets, inputs)
        report["verdict"] = "pass_with_limitations"
        report["limitations"] = [
            "Synthetic diagnostic decisions only; retained CAS hold unresolved."
        ]
        report["assessments"] = [
            {
                "assessment_id": entry["entry_id"],
                "area": "identity",
                "topic": "Exact diagnostic scope",
                "outcome": "supported",
                "summary": "Synthetic scoped action, no release approval.",
                "target_ids": [entry["entry_id"]],
                "evidence_ids": ["primary"],
                "dimensions": [
                    {
                        "name": key,
                        "value": value,
                        "definition": "Exact synthetic diagnostic scope",
                        "evidence_ids": ["primary"],
                    }
                    for key, value in {
                        "cas_disposition": entry["action"],
                        "diagnostic_scope": "diagnostic_candidate_only",
                        "hold_disposition": "WITHHOLD" if entry["hold"] else "RETIRED_WITH_HISTORY",
                    }.items()
                ],
            }
            for entry in entries
        ]
        pair = p.adoption.save_report(report)
        assert p.adoption.native.read_review(p.root, str(pair.relative_to(p.root))) == report
        request["reviews"].append(ref(p.root, pair))
        request["review_inputs"].update(
            {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        )
        request["review_inputs"][str(pair.with_name("review.md").relative_to(p.root))] = api.sha(
            pair.with_name("review.md").read_bytes()
        )
    request_path = p.root / "current-cas-request.json"
    write(request_path, request)
    return request_path


def _publication(f, endpoint, rows, tmp_path):
    p = PublicationFixture.__new__(PublicationFixture)
    p.root, p.adoption, p.counter = f.target, f.original, 0
    p.adoption.root = f.target
    p.adoption.policy = f.target / "operational-policy.json"
    p.histories = [
        {
            "root": item["identity"]["root"],
            "head": item["identity"]["head"],
            "review": item["review"],
            "markdown_sha256": item["markdown_sha256"],
        }
        for item in f.endpoint["historical_reviews"]
    ]
    p.history = p.histories[0]
    p.producer = Path(os.environ["MIM_ADDITIONAL_ASSERTION_CLAW_SRC"]).resolve().parent
    assert api.git(p.producer, "rev-parse", "HEAD").decode().strip() == CLAW_HEAD
    assert api.sha((p.producer / "src/kg_microbe_utils/stable_mim.py").read_bytes()) == CAS_POLICY
    p.kg = tmp_path / "synthetic-kg"
    initialize(p.kg)
    mapping = p.kg / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    mapping.parent.mkdir()
    mapping.write_bytes(
        gzip.compress(
            b"subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tsource\n", mtime=0
        )
    )
    commit(p.kg)
    p.cas_request = _cas_request(p, endpoint, rows)
    for name in api.inventory(p.root):
        record = api.load_yaml((p.root / name).read_bytes())
        target = (record.get("ontology_mapping") or {}).get("ontology_id")
        assert target is None or target.startswith("NCIT:")
    p.generation_dir = p.root / ".temp/inherited-cas-generation"
    p.generated = publication.generate(
        p.root,
        p.producer,
        p.kg,
        None,
        None,
        p.generation_dir,
        curation_successor=endpoint,
        curation_successor_sha256=api.sha(endpoint.read_bytes()),
        cas_dispositions=p.cas_request,
        cas_dispositions_sha256=api.sha(p.cas_request.read_bytes()),
    )
    p.generation_receipt = p.generation_dir / "receipt.json"
    return p


def _completed_chain(tmp_path, monkeypatch):
    def completed(phase):
        with (tmp_path / "progress.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps({"completed": phase}) + "\n")
        print("#1439 native phase complete: " + phase, flush=True)

    f, historical, old_rows = _source_fixture(tmp_path / "source-chain", monkeypatch)
    adoption_root = f.predecessor
    adoption_before = maintained(adoption_root)
    held_before = (f.target / HELD_OWNER).read_bytes()
    source_context = (f.target / f.request["source_context"]["path"]).read_bytes()
    first_endpoint, first_evidence = _complete_source(f, "withdrawal-application")
    first_root = f.target
    first_before = maintained(first_root)
    first_request = json.loads(f.path.read_bytes())
    assert first_request["operations"][0]["rejected_identifiers"] == [RETIRED]
    withdrawn_bytes = (first_root / RETIRED_OWNER).read_bytes()
    assert not (first_root / OLD_OWNER).exists()
    completed("adoption_and_first_withdrawal_commit_verify")

    _second_source(f, first_endpoint, tmp_path / "second-successor")
    second_endpoint, second_evidence = _complete_source(f, "unrelated-application")
    assert f.request["operations"][0]["mim_id"] != first_request["operations"][0]["mim_id"]
    assert (f.target / RETIRED_OWNER).read_bytes() == withdrawn_bytes
    assert (f.target / HELD_OWNER).read_bytes() == held_before
    assert (f.target / publication.CANONICAL).read_bytes() == historical
    assert (f.target / f.request["source_context"]["path"]).read_bytes() == source_context
    owners_before = {name: frozen.content for name, frozen in api.inventory(f.target).items()}
    ledgers_before = {name: (f.target / name).read_bytes() for name in successor.LEDGERS}
    completed("unrelated_second_correction_commit_verify")

    p = _publication(f, second_endpoint, old_rows, tmp_path)
    assert p.generated["curation_successor"] == ref(f.target, second_endpoint)
    assert p.generated["claw"]["head"] == CLAW_HEAD
    completed("fresh_native_pair_and_claw707_generation")

    request, stage, _ = p.prepare()
    acceptance = p.accept(request, stage)
    destination = p.destination(request, "inherited-cas-application")
    previous = current_outputs(p.root)
    dry = publication.apply(p.root, stage, acceptance, destination, enabled=False)
    assert dry["applied"] is False and not destination.exists()
    assert current_outputs(p.root) == previous
    application = publication.apply(p.root, stage, acceptance, destination, enabled=True)
    assert application["state"] == "COMPLETE" and application["scientific_approval_added"] is False
    checked = publication.verify_completed(p.root, stage, destination / "application.json")
    assert checked["status"] == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    completed("canonical_prepare_dry_apply_verify")

    packet = semantic_transition.capture(
        p.root, stage, destination / "application.json", "inherited-cas-semantic"
    )
    arguments = semantic_case_inputs(p.root, packet)
    result = semantic_transition.verify(*arguments)
    assert result["scope"] == "semantic_reconstruction_not_transaction_reexecution"
    assert result["provenance"]["ordinary_release_review_required"] is True
    assert result["provenance"]["scientific_approval_added"] is False
    assert result["source"]["scientific_approval_added"] is False
    evidence = result["evidence"]
    assert [step["kind"] for step in evidence.packet["sources"]] == [
        "adoption",
        "curation",
        "curation",
    ]
    assert [step["root"] for step in evidence.packet["sources"]] == [
        str(adoption_root),
        str(first_root),
        str(p.root),
    ]
    assert len(result["source"]["retained_contexts"]) == 3
    assert result["source"]["retained_contexts"][0]["decisions"][0]["other_holds"] == [
        "role provisional"
    ]
    assert [step["operations"][0]["mim_id"] for step in result["source"]["corrections"]] == [
        first_request["operations"][0]["mim_id"],
        f.request["operations"][0]["mim_id"],
    ]

    installed = publication.read_sssom(p.root / publication.CANONICAL)[2]
    assert not any(row["object_id"] == RETIRED for row in installed)
    assert all(row["validation_method"] == "" for row in installed)
    selection = result["provenance"]["selection"]
    held = [
        entry
        for entry in selection["rows"]
        if entry.get("mandatory_disposition") == "INSTALL_WITHHOLD"
    ]
    assert len(held) == 1 and held[0]["disposition"] == "INSTALL_WITHHOLD"
    assert held[0]["cas_disposition"]["historical_row"] == old_rows[0]
    assert (
        held[0]["cas_disposition"]["historical_row"]["validation_method"] == "synthetic-prior-stamp"
    )
    assert HELD in held[0]["candidate_row"]["other"]
    removed = [
        entry
        for entry in selection["rows"]
        if any(item["row"] == old_rows[1] for item in entry["before_rows"])
    ]
    assert len(removed) == 1 and removed[0]["disposition"] == "REMOVE_WITH_HISTORY"
    assert removed[0]["candidate_position"] is None and removed[0]["proposed_row"] is None
    assert removed[0]["before_rows"][0]["row"] == old_rows[1]
    assert (
        removed[0]["before_rows"][0]["row"]["validation_method"]
        == "synthetic-prior-retirement-stamp"
    )
    assert arguments[3] == owners_before
    assert arguments[4] == ledgers_before
    assert maintained(first_root) == first_before
    assert maintained(adoption_root) == adoption_before
    assert_exact_evidence(first_evidence)
    assert_exact_evidence(second_evidence)
    completed("complete_three_step_semantic_reconstruction_with_retained_hold")

    write(
        p.root / "inherited-cas-case.json",
        {
            "root": str(p.root),
            "packet": packet,
            "endpoint": ref(p.root, second_endpoint),
            "first_endpoint": {"root": str(first_root), **ref(first_root, first_endpoint)},
            "generation": ref(p.root, p.generation_receipt),
            "application": ref(p.root, destination / "application.json"),
            "cas_request": ref(p.root, p.cas_request),
            "policy_sha256": CAS_POLICY,
            "summary": {
                "scope": result["scope"],
                "provenance_sha256": api.digest(result["provenance"]),
                "scientific_approval_added": False,
                "source_steps": 3,
                "retired_entries": 1,
                "retained_holds": 1,
            },
        },
    )
    return {
        "root": p.root,
        "publication": p,
        "source": f,
        "semantic_arguments": arguments,
        "semantic_result": result,
        "packet": packet,
        "historical_rows": old_rows,
        "first_endpoint": first_endpoint,
        "current_endpoint": second_endpoint,
        "owners": owners_before,
        "ledgers": ledgers_before,
    }


@pytest.fixture(scope="module")
def native_inherited_cas_chain(tmp_path_factory):
    """Run the real chain once; subsequent controls consume captured copies only."""
    if not os.environ.get("MIM_ADDITIONAL_ASSERTION_CLAW_SRC"):
        pytest.skip(
            "Explicit pinned707 producer required; CI supplies the additional-Claw selector"
        )
    with pytest.MonkeyPatch.context() as monkeypatch:
        yield _completed_chain(tmp_path_factory.mktemp("inherited-cas-chain"), monkeypatch)


def test_native_inherited_cas_withdrawal_publication_and_semantic_chain(native_inherited_cas_chain):
    """The completed fixture has exercised every native and semantic assertion above."""
    case = native_inherited_cas_chain
    assert (case["root"] / "inherited-cas-case.json").is_file()
    assert case["semantic_result"]["source"]["owners"] == case["owners"]


@pytest.fixture
def inherited_owner_case(native_inherited_cas_chain):
    """Private in-memory copies of actual captured native evidence, never receipts to install."""
    case = native_inherited_cas_chain
    evidence = case["semantic_result"]["evidence"]
    baseline = case["semantic_arguments"][2]["proof"].after
    return {
        "steps": copy.deepcopy(evidence.packet["sources"]),
        "captured": {
            key: evidence.read(key[0], {"path": key[1], "sha256": key[2]}) for key in evidence.files
        },
        "baseline_owners": {
            name: raw for name, raw in baseline.items() if name.startswith("data/ingredients/")
        },
        "baseline_ledgers": {name: baseline[name] for name in successor.LEDGERS},
        "current_owners": dict(case["owners"]),
        "current_ledgers": dict(case["ledgers"]),
        "schema_root": case["root"],
    }


@pytest.mark.parametrize("attack", ["missing_adoption", "missing_withdrawal", "reordered", "cycle"])
def test_actual_chain_requires_every_ordered_source_step(inherited_owner_case, attack):
    from tests.test_semantic_owner_transition import run

    case = inherited_owner_case
    if attack == "missing_adoption":
        case["steps"].pop(0)
    elif attack == "missing_withdrawal":
        case["steps"].pop(1)
    elif attack == "reordered":
        case["steps"][1:] = reversed(case["steps"][1:])
    else:
        case["steps"].insert(1, copy.deepcopy(case["steps"][0]))
    with pytest.raises(ValueError, match="bounded source chain|before-inventory|overlap or cycle"):
        run(case)


@pytest.mark.parametrize("attack", ["root", "kind", "manifest", "receipt", "producer", "stage"])
def test_rehashed_last_step_cannot_select_a_sibling_ancestor(inherited_owner_case, attack):
    from tests.test_semantic_owner_transition import document, rebind, run

    case = inherited_owner_case
    step = case["steps"][-1]
    request, manifest, receipt = (
        document(case, step, key) for key in ("request", "manifest", "receipt")
    )
    predecessor = request["predecessor"]
    if attack == "root":
        predecessor["identity"]["root"] += "-unrelated-sibling"
    elif attack == "kind":
        predecessor["kind"] = "adoption"
    elif attack == "producer":
        predecessor["producer"]["source_sha256"] = "0" * 64
    elif attack == "stage":
        predecessor["stage"] += "-unrelated"
    else:
        predecessor[attack]["sha256"] = "0" * 64
    manifest["predecessor"] = receipt["predecessor"] = copy.deepcopy(predecessor)
    rebind(case, step, request=request, manifest=manifest, receipt=receipt)
    with pytest.raises(ValueError, match="immediate selected source step"):
        run(case)


@pytest.mark.parametrize("attack", ["rejection", "context", "pair", "hold"])
def test_actual_withdrawal_keeps_original_pair_context_and_hold(inherited_owner_case, attack):
    from tests.test_semantic_owner_transition import document, rebind_correction, replace, run

    case = inherited_owner_case
    step = case["steps"][1]
    request, manifest = (document(case, step, key) for key in ("request", "manifest"))
    operation = request["operations"][0]
    if attack == "rejection":
        operation["rejected_identifiers"] = []
        expected = "removed resolving alias"
    elif attack == "context":
        reference = request["source_context"]
        raw = case["captured"][(step["root"], reference["path"], reference["sha256"])]
        context = json.loads(raw)
        context["invented_context"] = True
        request["source_context"] = replace(case, step["root"], reference, api.encoded(context))
        manifest["inputs"][reference["path"]] = request["source_context"]["sha256"]
        expected = "original source/hold context differs"
    elif attack == "pair":
        operation["primary"]["sha256"] = "0" * 64
        expected = "review input closure differs"
    else:
        operation["inherited_holds"] = operation["residual_holds"] = []
        expected = "stored corrective payloads differ|stored payloads differ|payload|hold"
    first_correction = {**case, "steps": case["steps"][:2]}
    rebind_correction(first_correction, request, manifest)
    with pytest.raises(ValueError, match=expected):
        run(case)


@pytest.mark.parametrize("attack", ["later_owner", "ledger", "marker"])
def test_actual_chain_preserves_later_owner_ledger_and_marker_bytes(inherited_owner_case, attack):
    from tests.test_semantic_owner_transition import document, rebind, replace, run

    case = inherited_owner_case
    if attack == "later_owner":
        case["current_owners"][RETIRED_OWNER] += b"\n"
        expected = "current owner/ledger endpoint differs"
    elif attack == "ledger":
        case["current_ledgers"][successor.LEDGERS[0]] += b"\n"
        expected = "current owner/ledger endpoint differs"
    else:
        step = case["steps"][-1]
        receipt = document(case, step, "receipt")
        reference = receipt["beforeimages"][successor.MARKER]
        receipt["beforeimages"][successor.MARKER] = replace(
            case, step["root"], reference, api.encoded({"wrong_ancestor": True})
        )
        manifest = document(case, step, "manifest")
        if successor.MARKER in manifest["inputs"]:
            manifest["inputs"][successor.MARKER] = receipt["beforeimages"][successor.MARKER][
                "sha256"
            ]
        rebind(case, step, receipt=receipt, manifest=manifest)
        expected = "preceding source marker differs"
    with pytest.raises(ValueError, match=expected):
        run(case)


def _cas_arguments(case):
    evidence = case["semantic_result"]["evidence"]
    root = str(case["root"])
    selected = evidence.packet["publication"]
    request = evidence.document(root, selected["request"])
    receipt = evidence.document(root, selected["receipt"])
    generation = evidence.document(root, request["generation"])
    diagnostic = evidence.document(root, generation["outputs"]["manifest"])
    candidate = publication.read_sssom(
        Path("candidate"), content=evidence.read(root, generation["outputs"]["sssom"])
    )[2]
    return (
        evidence,
        root,
        generation,
        diagnostic,
        evidence.read(root, receipt["beforeimages"][publication.CANONICAL]),
        candidate,
        case["owners"],
        case["semantic_result"]["source"],
    )


def test_actual_chain_cannot_omit_mandatory_cas_hold(native_inherited_cas_chain):
    args = list(_cas_arguments(native_inherited_cas_chain))
    args[3] = copy.deepcopy(args[3])
    args[3]["cas_dispositions"]["held_rows"] = []
    with pytest.raises(ValueError, match="mandatory held/retired accounting"):
        semantic_transition._cas(*args)


def test_actual_chain_never_skips_a_later_selected_owner(native_inherited_cas_chain):
    args = _cas_arguments(native_inherited_cas_chain)
    claims = args[3]["cas_dispositions"]["content"]
    steps = copy.deepcopy(args[-1]["corrections"])
    operation = copy.deepcopy(steps[0]["operations"][0])
    operation["rejected_identifiers"] = []
    steps[-1]["operations"].append(operation)
    steps[-1]["selected_before"][operation["mim_id"]] = steps[0]["selected_before"][
        operation["mim_id"]
    ]
    with pytest.raises(ValueError, match="actual reviewed corrective"):
        publication._cas_source_withdrawals(claims, steps)


def test_exact_old_consumers_refuse_the_authentic_two_hop_proof(
    native_inherited_cas_chain, inherited_owner_case
):
    """Execute complete f639 consumer files; never restamp or repeat native writes."""
    from tests.test_stable_id_adoption import ROOT

    original = "f63930804fe143cd0bd4eba0374d9d2be2dd66ba"
    pins = {
        "src/mediaingredientmech/curate/stable_sssom_publication.py": "8413367bbb9acd712e5c1216d3d78fcd4fbc7cd8390eca60ac506731d35b138e",
        "src/mediaingredientmech/validation/semantic_owner_transition.py": "06cdd5f0254cc51aa1b95552f646195ce1cd6671bb85d0151c750dc0b36606f9",
    }
    modules = []
    for name, pin in pins.items():
        raw = api.git(ROOT, "show", original + ":" + name)
        assert api.sha(raw) == pin
        module = types.ModuleType("_original_1439_" + Path(name).stem)
        module.__file__ = str(ROOT / name)
        module.__dict__["_PRODUCER_CAPTURE"] = publication._CAPTURE
        exec(compile(raw, module.__file__, "exec"), module.__dict__)
        modules.append(module)
    old_publisher, old_owner = modules
    case = native_inherited_cas_chain
    args = _cas_arguments(case)
    # The old component consumes the same exact final-operation projection that
    # its real native caller supplied; no ancestor operation is smuggled in.
    final = types.SimpleNamespace(
        loaded=types.SimpleNamespace(
            request={"operations": args[-1]["operations"]},
            predecessor=types.SimpleNamespace(
                owners={
                    name: types.SimpleNamespace(content=raw)
                    for name, raw in args[-1]["predecessor_owners"].items()
                }
            ),
        )
    )
    with pytest.raises(ValueError, match="actual reviewed corrective"):
        old_publisher._cas_source_correction(args[3], final, args[2]["curation_successor"])
    c = inherited_owner_case
    with pytest.raises(ValueError, match="not the selected adoption"):
        old_owner.verify_owner_steps(
            c["steps"],
            lambda root, ref: c["captured"][(root, ref["path"], ref["sha256"])],
            c["baseline_owners"],
            c["baseline_ledgers"],
            c["current_owners"],
            c["current_ledgers"],
            c["schema_root"],
        )
    write(
        case["root"] / "original-consumer-refusals.json",
        {
            "original_commit": original,
            "original_files": pins,
            "source": ref(case["root"], case["root"] / "inherited-cas-case.json"),
            "publisher": "REFUSED_MISSING_LATEST_OPERATION",
            "semantic_owner": "REFUSED_NON_ADOPTION_PREDECESSOR",
            "native_writes_repeated": False,
        },
    )
