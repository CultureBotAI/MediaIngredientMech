"""#741: real source writer → pinned native generator → receipt publication.

The tiny catalog is a mechanical fixture, not a scientific owner approval.
No source verifier, generation, receipt maker, or publication gate is mocked.
An installed pinned Claw checkout is an explicit optional integration input.
"""

import copy
import importlib.util
import json
import os
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest

from mediaingredientmech import campaign_publication as publication
from mediaingredientmech.validation import mapping_change_receipts as native

ROOT = Path(__file__).resolve().parents[1]


def fixture_module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tests" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pinned_claw():
    configured = os.environ.get("CLAW_ROOT")
    if not configured:
        pytest.skip("CLAW_ROOT is required for the real pinned-generator integration")
    root = Path(configured).resolve()
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip() == (
        publication.PRODUCER_REVISION
    )
    assert publication.sha((root / "scripts/build_mim_ingredient_sssom.py").read_bytes()) == (
        publication.PRODUCER_SHA
    )
    return root


def make_source_case(root, historical_root=None):
    source = fixture_module("test_campaign_owner_apply")
    mapping = fixture_module("test_campaign_publication")
    plan = source.demotion_case(root)
    if historical_root is not None:
        # Genuine historical bytes and receipt prefix; the published source
        # proposal/review below is an explicitly private mechanical fixture.
        (root / source.EDIT).unlink()
        source.EDIT = "data/ingredients/mapped/Angustmycin.yaml"
        source.DEMOTED = "data/ingredients/unmapped/Angustmycin.yaml"
        source.put(root, source.EDIT, (historical_root / source.EDIT).read_bytes())
        final = source.owner.record((root / source.EDIT).read_bytes())
        final.update(mapping_status="AMBIGUOUS")
        final.pop("ontology_mapping", None)
        final["curation_history"].append(source.event("ANNOTATED", "AMBIGUOUS"))
        source.render(root, "intake/payload-0.yaml", final)
        operation = plan["records"][0]
        operation.update(
            before_source_record=source.EDIT,
            source_record=source.DEMOTED,
            before_yaml_sha256=source.ref(root, source.EDIT)["sha256"],
        )
        proposals = json.loads((root / "intake/proposals.json").read_bytes())
        proposals["proposals"][0].update(
            owner_path=source.EDIT,
            before_sha256=operation["before_yaml_sha256"],
            after_capture={"root": "artifact", **source.ref(root, "intake/payload-0.yaml")},
        )
        source.put(root, "intake/proposals.json", proposals)
    # A local registry owner avoids remote label lookup in this offline fixture.
    source.render(
        root,
        source.UNTOUCHED,
        source.ingredient("kgmicrobe.ingredient:untouched", "Untouched")
        | {
            "ontology_mapping": {
                "ontology_id": "kgmicrobe.ingredient:untouched",
                "ontology_label": "Untouched",
                "ontology_source": "kgmicrobe.ingredient",
                "mapping_quality": "EXACT_MATCH",
            }
        },
    )
    before = mapping.sssom(
        [
            mapping.row("Existing"),
            mapping.row(
                "Existing", "kgmicrobe.compound:existing", object_source="kgmicrobe.compound"
            ),
            mapping.row(
                "Untouched", "kgmicrobe.ingredient:untouched", object_source="kgmicrobe.ingredient"
            ),
        ]
    )
    source.put(root, publication.SOURCE, before)
    mapping.history(root, before)
    if historical_root is not None:
        historical = native.verify_mapping_chain(historical_root)
        assert len(historical["receipts"]) == 27
        assert not historical["owner_chains"].get(source.EDIT)
        assert not historical["owner_chains"].get(source.DEMOTED)
        for path, expected in historical["input_hashes"].items():
            raw = (historical_root / path).read_bytes()
            assert publication.sha(raw) == expected
            source.put(root, path, raw)
        before = (historical_root / publication.SOURCE).read_bytes()
    source.put(root, publication.MAKER, (ROOT / publication.MAKER).read_bytes())
    source.put(root, "pyproject.toml", (ROOT / "pyproject.toml").read_bytes())
    for path, frozen in publication.LOADED_PRODUCERS.items():
        source.put(root, path, frozen.content)
    sidecar = b"subject_id\ttoken_key\ttoken\towner_subject_ids\tdisposition\tinput_surfaces\tsource_refs\tevidence_refs\n"
    baseline = b"subject_id\ttoken_key\n"
    inventory = source.owner.hashes(source.owner.inventory(root))
    source.put(root, "before.json", {"schema_version": 1, "owners": inventory})
    plan["before_inventory"] = source.ref(root, "before.json")
    policy = dict.fromkeys(publication.POLICY_REQUIRED, "historical fixture")
    policy.update(
        schema_version=1,
        policy_version="owned-name-policy-v1",
        approval="NONE: private integration fixture",
        artifacts={
            publication.SOURCE: publication.sha(before),
            publication.SIDECAR: publication.sha(sidecar),
            publication.BASELINE: publication.sha(baseline),
        },
        source_owner_sha256=inventory,
        decisions=[],
        policy_evidence=[],
        source_alias_addition_updates=[{"fixture": "preserve original history"}],
    )
    if historical_root is not None:
        policy = json.loads((historical_root / publication.POLICY).read_bytes())
        sidecar = (historical_root / publication.SIDECAR).read_bytes()
        baseline = (historical_root / publication.BASELINE).read_bytes()
    for path, value in (
        (publication.POLICY, policy),
        (publication.SIDECAR, sidecar),
        (publication.BASELINE, baseline),
    ):
        source.put(root, path, value)
    protected = {
        path: publication.sha((root / path).read_bytes())
        for path in (
            publication.SOURCE,
            publication.POLICY,
            publication.SIDECAR,
            publication.BASELINE,
            *native.HISTORICAL_CONTEXT,
        )
    }
    protected.update(native.verify_mapping_chain(root)["input_hashes"])
    source.put(root, "protected.json", {"schema_version": 1, "files": protected})
    plan["protected_inputs"] = source.ref(root, "protected.json")
    source.run_git(
        root,
        "add",
        "data",
        "mappings",
        "reports",
        "src",
        "scripts",
        "intake",
        "pyproject.toml",
        "before.json",
        "protected.json",
    )
    source.run_git(
        root,
        "-c",
        "user.email=fixture@example.invalid",
        "-c",
        "user.name=Fixture",
        "commit",
        "-qm",
        "Native publication fixture context",
    )
    plan["baseline_commit"] = source.run_git(root, "rev-parse", "HEAD")
    if historical_root is not None:
        # Publish the changed original fixture object, including its actual
        # preimage, before binding the final accepted operation independently.
        head = plan["baseline_commit"]
        plan["intake_heads"] = {"worker-01": head}
        for binding in plan["bindings"]:
            if binding["binding_id"] != "demotion-review":
                binding.update(source.ref(root, binding["path"]))
            if binding["published_head"] is not None:
                binding["published_head"] = head
        for origin in plan["records"][0]["origins"]:
            origin["head_sha"] = head
    source.repin_demotion(root, plan)
    return source, mapping, plan, before, policy, sidecar, baseline


def prepare_native_case(root, historical_root=None):
    claw = pinned_claw()
    source, mapping, source_plan, before, policy, sidecar, baseline = make_source_case(
        root, historical_root
    )
    prefix = native.verify_mapping_chain(root)["receipt_inputs"]
    owner_receipt = root / "source-receipt/application.json"
    source.owner.apply(
        source.owner.prepare(root, root / "plan.json", root / "acceptance.json"),
        owner_receipt.parent,
        enabled=True,
    )
    source_proof = source.owner.verify_completed(root, root / "plan.json", owner_receipt)
    kg = root / "private-kg"
    kg.mkdir()
    source.run_git(kg, "init", "-q")
    source.run_git(
        kg,
        "-c",
        "user.email=fixture@example.invalid",
        "-c",
        "user.name=Fixture",
        "commit",
        "--allow-empty",
        "-qm",
        "Private empty KG fixture",
    )
    output = root / "reports/native"
    output.mkdir(parents=True)
    temporary = root / "temporary"
    temporary.mkdir()
    paths = {
        "candidate": output / "candidate.tsv",
        "sidecar": output / "suppressed.tsv",
        "manifest": output / "generation.json",
    }
    command = [
        sys.executable,
        "-B",
        str(claw / "scripts/build_mim_ingredient_sssom.py"),
        "--output",
        str(paths["candidate"]),
        "--suppressed-aliases-output",
        str(paths["sidecar"]),
        "--generation-manifest-output",
        str(paths["manifest"]),
        "--prior-stamps-from",
        str(root / publication.SOURCE),
    ]
    environment = {
        **os.environ,
        "PYTHONDONTWRITEBYTECODE": "1",
        "MEDIAINGREDIENTMECH_ROOT": str(root),
        "KGMICROBE_ROOT": str(kg),
        "TMPDIR": str(temporary),
        "OPENCLAW_WORKSPACE": str(root / "private-openclaw-workspace"),
        "PATH": str(Path(sys.executable).parent) + os.pathsep + os.environ.get("PATH", ""),
    }
    run = subprocess.run(command, cwd=root, env=environment, capture_output=True, text=True)
    source.put(
        root,
        "reports/native/command.json",
        {
            "argv": command,
            "returncode": run.returncode,
            "environment": {
                key: environment[key]
                for key in (
                    "MEDIAINGREDIENTMECH_ROOT",
                    "KGMICROBE_ROOT",
                    "TMPDIR",
                    "OPENCLAW_WORKSPACE",
                )
            },
        },
    )
    source.put(root, "reports/native/command.log", (run.stdout + run.stderr).encode())
    assert run.returncode == 0, run.stdout + run.stderr
    manifest = json.loads(paths["manifest"].read_bytes())
    assert manifest["external_sssom_validation"] == "passed"
    assert manifest["source_revisions"]["mim"] == source_plan["baseline_commit"]
    if historical_root is None:
        assert paths["sidecar"].read_bytes() == sidecar
    demoted_subject = publication.subject(source.DEMOTED)
    assert all(
        row["subject_id"] != demoted_subject
        for row in publication.table(paths["candidate"].read_bytes())[2]
    )

    def capture(name, value):
        path = source.put(root, "reports/publication-input/" + name, value)
        return source.ref(root, path.relative_to(root).as_posix())

    plan = {
        "schema_version": 1,
        "kind": "unmatched_campaign_publication_v1",
        "issue": publication.ISSUE,
        "approval": "NONE",
        "batch": "issue1174-native-demotion",
        "scope": "Private real source/generation/publication integration; no scientific approval",
        "owner_plan": source.ref(root, "plan.json"),
        "owner_receipt": source.ref(root, "source-receipt/application.json"),
        "publication_producers": {
            p: publication.sha(f.content) for p, f in publication.LOADED_PRODUCERS.items()
        },
        "before": {
            "canonical": capture("before.tsv", before),
            "policy": capture("policy.json", policy),
            "sidecar": capture("sidecar.tsv", sidecar),
            "baseline": capture("baseline.tsv", baseline),
        },
        "generation": {
            **{
                role: source.ref(root, path.relative_to(root).as_posix())
                for role, path in paths.items()
            },
            "producer_root": str(claw),
            "kg_root": str(kg),
        },
        "receipt_prefix": prefix,
        "native_context": {
            p: publication.sha((root / p).read_bytes()) for p in native.HISTORICAL_CONTEXT
        },
        "rows": [
            {
                "owner": source.DEMOTED,
                "before_position": position,
                "native_position": None,
                "preserve_fields": [],
            }
            for position, row in enumerate(publication.table(before)[2], 1)
            if row["subject_id"] == demoted_subject
        ],
    }
    plan_path = source.put(root, "reports/publication-input/plan.json", plan)
    destination = root / "reports/publication"
    destination.mkdir()
    return source, plan, plan_path, destination, source_proof


@pytest.mark.parametrize(
    "fault",
    [
        "missing-slot",
        "candidate-substitution",
        "wrong-revision",
        "retired-source",
        "source-payload",
    ],
)
def test_real_demotion_publication_refuses_stale_or_incomplete_input(tmp_path, fault):
    source, plan, path, destination, _ = prepare_native_case(tmp_path)
    before = {
        p: (tmp_path / p).read_bytes()
        for p in (publication.SOURCE, publication.POLICY, publication.SIDECAR, publication.BASELINE)
    }
    if fault == "missing-slot":
        plan["rows"].pop()
    elif fault == "candidate-substitution":
        candidate = tmp_path / plan["generation"]["candidate"]["path"]
        candidate.write_bytes(candidate.read_bytes().replace(b"Untouched", b"Unreviewed"))
        plan["generation"]["candidate"]["sha256"] = publication.sha(candidate.read_bytes())
        manifest_path = tmp_path / plan["generation"]["manifest"]["path"]
        manifest = json.loads(manifest_path.read_bytes())
        manifest["artifacts"][0]["sha256"] = plan["generation"]["candidate"]["sha256"]
        source.put(tmp_path, plan["generation"]["manifest"]["path"], manifest)
        plan["generation"]["manifest"]["sha256"] = publication.sha(manifest_path.read_bytes())
    elif fault == "wrong-revision":
        name = plan["generation"]["manifest"]["path"]
        manifest = json.loads((tmp_path / name).read_bytes())
        manifest["source_revisions"]["mim"] = "f" * 40
        source.put(tmp_path, name, manifest)
        plan["generation"]["manifest"] = source.ref(tmp_path, name)
    elif fault == "retired-source":
        (tmp_path / source.EDIT).write_bytes(
            (tmp_path / "source-receipt/owner-before-0000.yaml").read_bytes()
        )
    else:
        target = tmp_path / source.DEMOTED
        target.write_bytes(target.read_bytes() + b"# late unaccepted bytes\n")
    source.put(tmp_path, path.relative_to(tmp_path).as_posix(), plan)
    with pytest.raises((ValueError, RuntimeError)):
        publication.publish(tmp_path, path, destination, apply=True)
    assert all((tmp_path / p).read_bytes() == raw for p, raw in before.items())
    assert not list(destination.iterdir())
    assert native.verify_mapping_chain(tmp_path)["receipt_inputs"] == plan["receipt_prefix"]


def test_real_demotion_preserves_27_receipts_and_frozen_hold(tmp_path):
    configured = os.environ.get("CAMPAIGN_HISTORY_ROOT")
    if not configured:
        pytest.skip("CAMPAIGN_HISTORY_ROOT is required for the actual 27-receipt hold integration")
    historical = Path(configured).resolve()
    original = native.verify_mapping_chain(historical)
    assert len(original["receipts"]) == 27
    source, plan, path, destination, _ = prepare_native_case(tmp_path, historical)
    report = json.loads(
        (
            historical / "reports/semantic_review_20260921/resolution/current-review.json"
        ).read_bytes()
    )
    holds = json.loads((historical / report["release_holds"]).read_bytes())
    assert len(holds["resolutions"]) == 1
    resolution = holds["resolutions"][0]
    checkpoint = native.HOLD_CHECKPOINTS[resolution["assertion_id"]]
    held_row = original["states_after_sequence"][checkpoint["sequence"]][checkpoint["position"] - 1]

    def held_lineage(proof):
        from mediaingredientmech.export.kgx import MATCHES, Graph
        from mediaingredientmech.validation import semantic_release

        position = checkpoint["position"]
        for receipt in proof["receipts"][checkpoint["sequence"] :]:
            position = receipt["position_map"][position - 1]
            assert position is not None
        assert proof["state"][position - 1] == held_row
        graph = Graph()
        graph.nodes[held_row["subject_id"]] = {}
        graph.nodes[held_row["object_id"]] = {}
        graph.edge(
            held_row["subject_id"],
            MATCHES[held_row["predicate_id"]],
            held_row["object_id"],
            held_row["predicate_id"],
            "mapping",
            native.SSSOM_SOURCE,
            position,
            held_row,
        )
        owner_hash = publication.sha((historical / resolution["owner_record"]).read_bytes())
        assert owner_hash == resolution["owner_record_sha256"]
        return position, native.hold_lineage(
            proof,
            semantic_release.current_assertions({}, proof["state"], {}, proof["reviewed_sha256"]),
            graph.edges,
            holds["resolutions"],
            owners={held_row["subject_id"]: resolution["owner_record"]},
            record_hashes={resolution["owner_record"]: owner_hash},
        )

    before_position, before_lineage = held_lineage(original)
    assert before_lineage == report["release_hold_lineage"]
    before_rows = publication.table((tmp_path / publication.SOURCE).read_bytes())[3]
    result = publication.publish(tmp_path, path, destination, apply=True)
    assert result["status"] == "complete"
    assert publication.validate(tmp_path, path)["status"] == "verified"
    completed = native.verify_mapping_chain(tmp_path)
    assert completed["receipts"][:27] == original["receipts"]
    assert all(
        (tmp_path / p).read_bytes() == (historical / p).read_bytes()
        for p in original["receipt_paths"]
    )
    receipt = completed["receipts"][-1]
    assert receipt["sequence"] == 28
    removed = {r["before_position"] for r in plan["rows"]}
    assert removed and receipt["removed_rows"] == len(removed)
    assert receipt["added_rows"] == receipt["changed_rows"] == 0
    assert publication.table((tmp_path / publication.SOURCE).read_bytes())[3] == [
        raw for i, raw in enumerate(before_rows, 1) if i not in removed
    ]
    after_position, lineage = held_lineage(completed)
    assert after_position == receipt["position_map"][before_position - 1]
    assert after_position != before_position  # A real preceding deletion, not a fixed coordinate.
    assert lineage and receipt["approval"].startswith("NONE")
    assert all(
        (tmp_path / p).read_bytes() == (historical / p).read_bytes()
        for p in (publication.SIDECAR, publication.BASELINE)
    )
    after_policy = json.loads((tmp_path / publication.POLICY).read_bytes())
    expected_policy = copy.deepcopy(json.loads((historical / publication.POLICY).read_bytes()))
    expected_policy["artifacts"][publication.SOURCE] = publication.sha(
        (tmp_path / publication.SOURCE).read_bytes()
    )
    assert {k: v for k, v in after_policy.items() if k != publication.UPDATE} == expected_policy
    source.put(
        tmp_path,
        "reports/hold-proof.json",
        {
            "scope": "Real receipt/checkpoint/held-owner lineage only; not full semantic-release validation or approval",
            "receipt_prefix": original["receipt_inputs"],
            "new_receipt": result["receipt_sha256"],
            "checkpoint": checkpoint,
            "before_position": before_position,
            "after_position": after_position,
            "lineage": lineage,
        },
    )


@pytest.mark.parametrize("phase", ["reserved", "completion"])
def test_real_demotion_late_retired_source_never_emits_success(tmp_path, monkeypatch, phase):
    source, plan, path, destination, _ = prepare_native_case(tmp_path)
    before = {p: (tmp_path / p).read_bytes() for p in (publication.SOURCE, publication.POLICY)}
    retired_bytes = (tmp_path / "source-receipt/owner-before-0000.yaml").read_bytes()
    entered = []

    def reappear():
        entered.append(phase)
        (tmp_path / source.EDIT).write_bytes(retired_bytes)

    if phase == "reserved":
        original = publication._reserve

        @contextmanager
        def boundary(paths):
            with original(paths) as held:
                reappear()
                yield held

        monkeypatch.setattr(publication, "_reserve", boundary)
    else:
        original_finish = publication.finish_receipt

        def completion(*args, **kwargs):
            reappear()
            return original_finish(*args, **kwargs)

        monkeypatch.setattr(publication, "finish_receipt", completion)
    with pytest.raises((ValueError, RuntimeError), match="membership|retired|inventory"):
        publication.publish(tmp_path, path, destination, apply=True)
    assert entered == [phase]
    if phase == "reserved":
        assert all((tmp_path / p).read_bytes() == raw for p, raw in before.items())
    # A partial mutation is an error, not a rollback claim or a complete receipt.
    for candidate in (
        destination / "publication.json",
        tmp_path / native.RECEIPTS_DIR / (plan["batch"] + ".json"),
    ):
        assert not candidate.exists() or candidate.read_bytes() == b""


def test_real_source_generation_publication_demotion(tmp_path):
    source, plan, plan_path, destination, source_proof = prepare_native_case(tmp_path)
    before = (tmp_path / publication.SOURCE).read_bytes()
    untouched = publication.table(before)[3][-1]
    dry = publication.publish(tmp_path, plan_path, destination)
    assert dry["status"] == "dry_run"
    assert (tmp_path / publication.SOURCE).read_bytes() == before
    result = publication.publish(tmp_path, plan_path, destination, apply=True)
    assert result["status"] == "complete"
    assert publication.validate(tmp_path, plan_path)["status"] == "verified"
    chain = native.verify_mapping_chain(tmp_path)
    receipt = chain["receipts"][-1]
    assert receipt["position_map"] == [None, None, 1]
    assert (receipt["removed_rows"], receipt["added_rows"], receipt["changed_rows"]) == (2, 0, 0)
    assert receipt["records"][0]["shape"] == "demotion"
    assert receipt["records"][0]["before_source_record"] == source.EDIT
    assert (
        receipt["records"][0]["before_yaml_sha256"]
        == source_proof["records"][0]["before_yaml_sha256"]
    )
    assert publication.table((tmp_path / publication.SOURCE).read_bytes())[3] == [untouched]
    assert not (tmp_path / source.EDIT).exists()
    assert (
        source.owner.verify_completed(
            tmp_path, tmp_path / "plan.json", tmp_path / "source-receipt/application.json"
        )["records"][0]["shape"]
        == "demotion"
    )
    current_policy = json.loads((tmp_path / publication.POLICY).read_bytes())
    old_policy = json.loads((tmp_path / plan["before"]["policy"]["path"]).read_bytes())
    old_policy["artifacts"][publication.SOURCE] = publication.sha(
        (tmp_path / publication.SOURCE).read_bytes()
    )
    assert {k: v for k, v in current_policy.items() if k != publication.UPDATE} == old_policy


@pytest.mark.parametrize("unrelated", [False, True])
def test_real_1256_commit_between_source_generation_and_publication_refused(tmp_path, unrelated):
    source, plan, path, destination, _ = prepare_native_case(tmp_path)
    mapping = fixture_module("test_campaign_publication")
    before = {p: (tmp_path / p).read_bytes() for p in (publication.SOURCE, publication.POLICY)}
    mapping.commit_publication_boundary(tmp_path, unrelated=unrelated)
    # Completion remains a historical source proof; it is the live publisher
    # transaction which must refuse this intervening commit.
    assert source.owner.verify_completed(
        tmp_path, tmp_path / "plan.json", tmp_path / "source-receipt/application.json"
    )
    with pytest.raises(ValueError, match="live publication HEAD changed"):
        publication.publish(tmp_path, path, destination, apply=True)
    assert all((tmp_path / p).read_bytes() == raw for p, raw in before.items())
    assert not list(destination.iterdir())
    assert native.verify_mapping_chain(tmp_path)["receipt_inputs"] == plan["receipt_prefix"]


@pytest.mark.parametrize("phase", ["reserved", "before-completion", "after-completion"])
def test_real_1256_late_commit_rechecks_actual_source_generation_publication(
    tmp_path, monkeypatch, phase
):
    _, plan, path, destination, _ = prepare_native_case(tmp_path)
    mapping = fixture_module("test_campaign_publication")
    before = {p: (tmp_path / p).read_bytes() for p in (publication.SOURCE, publication.POLICY)}
    entered = []

    def change_head():
        entered.append(phase)
        mapping.commit_publication_boundary(tmp_path)

    if phase == "reserved":
        original = publication._reserve

        @contextmanager
        def reservation(paths):
            with original(paths) as handles:
                change_head()
                yield handles

        monkeypatch.setattr(publication, "_reserve", reservation)
    else:
        original = publication.finish_receipt

        def completion(*args, **kwargs):
            if phase == "before-completion":
                change_head()
            result = original(*args, **kwargs)
            if phase == "after-completion":
                change_head()
            return result

        monkeypatch.setattr(publication, "finish_receipt", completion)
    with pytest.raises(ValueError, match="live publication HEAD changed"):
        publication.publish(tmp_path, path, destination, apply=True)
    assert entered == [phase]
    if phase == "reserved":
        assert all((tmp_path / p).read_bytes() == raw for p, raw in before.items())
    for p in [
        destination / "publication.json",
        tmp_path / native.RECEIPTS_DIR / (plan["batch"] + ".json"),
    ]:
        assert not p.exists() or p.read_bytes() == b""


def test_real_1256_historical_completed_validation_after_commit(tmp_path):
    source, _, path, destination, _ = prepare_native_case(tmp_path)
    mapping = fixture_module("test_campaign_publication")
    # Source synchronization may create derived files without committing.
    source.put(tmp_path, "data/curated/fixture-derived.yaml", b"fixture: derived sync\n")
    assert publication.publish(tmp_path, path, destination, apply=True)["status"] == "complete"
    before = {p: (tmp_path / p).read_bytes() for p in (publication.SOURCE, publication.POLICY)}
    mapping.commit_publication_boundary(tmp_path, unrelated=True)
    assert publication.validate(tmp_path, path)["status"] == "verified"
    assert source.owner.verify_completed(
        tmp_path, tmp_path / "plan.json", tmp_path / "source-receipt/application.json"
    )
    assert all((tmp_path / p).read_bytes() == raw for p, raw in before.items())


@pytest.mark.parametrize("boundary", ["source-proof", "reserved-output-proof"])
@pytest.mark.parametrize("complete_call", [1, 2])
def test_real_1256_full_final_recheck_closes_head_after_proofs(
    tmp_path, monkeypatch, boundary, complete_call
):
    """W08-21061-PUB-001: real proof results are unchanged by the fault wrapper."""
    source, plan, path, destination, proof = prepare_native_case(tmp_path)
    mapping = fixture_module("test_campaign_publication")
    native_path = tmp_path / native.RECEIPTS_DIR / (plan["batch"] + ".json")
    log = destination / "publication.json"
    seen = []
    injected = []

    def after_actual_proof():
        if (
            log.exists()
            and log.read_bytes()
            and json.loads(log.read_bytes()).get("status") == "complete"
        ):
            seen.append(boundary)
            if len(seen) == complete_call:
                mapping.commit_publication_boundary(tmp_path, unrelated=True)
                injected.append(source.run_git(tmp_path, "rev-parse", "HEAD"))

    if boundary == "source-proof":
        actual = publication._owner_proof

        def source_proof(*args, **kwargs):
            result = actual(*args, **kwargs)
            after_actual_proof()
            return result

        monkeypatch.setattr(publication, "_owner_proof", source_proof)
    else:
        actual = publication.check_reserved

        def reserved_proof(handle, target):
            result = actual(handle, target)
            if target == native_path:
                after_actual_proof()
            return result

        monkeypatch.setattr(publication, "check_reserved", reserved_proof)
    error = None
    result = None
    try:
        result = publication.publish(tmp_path, path, destination, apply=True)
    except ValueError as caught:
        error = str(caught)
    source.put(
        tmp_path,
        "reports/final-recheck-observation.json",
        {
            "scope": "Real source, native generation, native receipt and guarded publication; fault wrapper only commits after unchanged real proof",
            "boundary": boundary,
            "complete_call": complete_call,
            "baseline": proof["baseline_commit"],
            "actual_head": source.run_git(tmp_path, "rev-parse", "HEAD"),
            "injected": injected,
            "error": error,
            "returned_result": result,
            "publication_receipt_nonempty": bool(log.read_bytes()),
            "native_receipt_nonempty": bool(native_path.read_bytes()),
        },
    )
    assert len(injected) == 1
    assert injected[0] != proof["baseline_commit"]
    assert error is not None and "live publication HEAD changed" in error
    assert result is None
    assert log.read_bytes() == b""
    assert native_path.read_bytes() == b""
    assert (destination / "canonical-before.tsv").read_bytes() == (
        tmp_path / plan["before"]["canonical"]["path"]
    ).read_bytes()
    assert (destination / "policy-before.json").read_bytes() == (
        tmp_path / plan["before"]["policy"]["path"]
    ).read_bytes()


def test_real_1256_tracked_derived_sync_and_historical_proof_remain_valid(tmp_path, monkeypatch):
    """Actual tracked synchronization is allowed; historical owner drift is not."""
    original = make_source_case

    def tracked_fixture(root, historical_root=None):
        values = original(root, historical_root)
        source, _, plan, *_ = values
        source.put(root, "data/curated/derived-fixture.yaml", b"fixture: before synchronization\n")
        source.run_git(root, "add", "--", "data/curated/derived-fixture.yaml")
        source.run_git(
            root,
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "Private tracked derived baseline",
        )
        plan["baseline_commit"] = source.run_git(root, "rev-parse", "HEAD")
        source.repin_demotion(root, plan)
        return values

    monkeypatch.setattr(sys.modules[__name__], "make_source_case", tracked_fixture)
    source, _, path, destination, proof = prepare_native_case(tmp_path)
    derived = tmp_path / "data/curated/derived-fixture.yaml"
    derived.write_bytes(b"fixture: synchronized uncommitted data\n")
    assert b"data/curated/derived-fixture.yaml\0" in source.owner.git(
        tmp_path, "diff", "--name-only", "-z", "HEAD", "--"
    )
    assert publication.publish(tmp_path, path, destination, apply=True)["status"] == "complete"
    mapping = fixture_module("test_campaign_publication")
    mapping.commit_publication_boundary(tmp_path, unrelated=True)
    assert publication.validate(tmp_path, path)["status"] == "verified"
    receipt_before = (destination / "publication.json").read_bytes()
    policy_before = (tmp_path / publication.POLICY).read_bytes()
    owner = tmp_path / proof["records"][0]["source_record"]
    owner.write_bytes(owner.read_bytes() + b"# unapproved current owner drift\n")
    with pytest.raises((ValueError, RuntimeError), match="inventory|changed"):
        publication.validate(tmp_path, path)
    assert (destination / "publication.json").read_bytes() == receipt_before
    assert (tmp_path / publication.POLICY).read_bytes() == policy_before
