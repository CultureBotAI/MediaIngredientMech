"""#1392: native adoption retains two genuine, distinct scientific baselines."""

import copy

import pytest
import yaml

from mediaingredientmech.validation import semantic_owner_transition as transition_api
from tests.stable_publication_fixture import NativeReviewAdoptionFixture
from tests.test_semantic_owner_transition import (
    captured_document,
    document,
    pin,
    rebind,
    replace,
    run,
)
from tests.test_stable_id_adoption import api, command, commit


@pytest.fixture(scope="module")
def distinct_baselines(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("native-distinct-baselines")
    originals = [
        {"identifier": "CHEBI:1", "preferred_term": "Exact", "mapping_status": "MAPPED"},
        {"identifier": "UNMAPPED_1", "preferred_term": "Move", "mapping_status": "UNMAPPED"},
    ]
    paths = ["data/ingredients/mapped/Exact.yaml", "data/ingredients/unmapped/Move.yaml"]
    corrected = {}
    for name, original in zip(paths, originals, strict=True):
        api.record_curation_event(
            original,
            curator="synthetic",
            action="CREATED",
            timestamp="2025-01-01T00:00:00Z",
            changes="Original synthetic scientific event; no real substance approval.",
        )
        revised = copy.deepcopy(original)
        revised["notes"] = "Synthetic corrected provenance before the later source campaign."
        api.record_curation_event(
            revised,
            curator="synthetic",
            action="CORRECTED_SOURCE_PROVENANCE",
            timestamp="2025-12-01T00:00:00Z",
            changes="Synthetic pre-ID provenance correction.",
        )
        corrected[name] = revised
    with pytest.MonkeyPatch.context() as patch:
        fixture = NativeReviewAdoptionFixture(
            tmp,
            patch,
            original_records=originals,
            legacy_corrections=corrected,
        )
        fixture.prepare()
        fixture.accept()
        application = api.apply(
            fixture.root,
            fixture.stage,
            fixture.acceptance,
            fixture.receipt,
            enabled=True,
        )
        assert application["state"] == "COMPLETE"
        assert (
            api.verify_completed(fixture.root, fixture.stage, fixture.receipt / "application.json")[
                "status"
            ]
            == "COMPLETE_CURRENT_CANDIDATE"
        )
    root = fixture.root
    captured = {}

    def store(owner_root, ref, raw=None):
        if raw is None:
            raw = (owner_root / ref["path"]).read_bytes()
        assert api.sha(raw) == ref["sha256"]
        key = (str(owner_root), ref["path"], ref["sha256"])
        assert key not in captured or captured[key] == raw
        captured[key] = raw
        return raw

    step = {
        "kind": "adoption",
        "root": str(root),
        "receipt": pin(fixture.receipt / "application.json", root),
        "manifest": pin(fixture.stage / "manifest.json", root),
        "afterimages": {},
    }
    receipt = api.document(store(root, step["receipt"]))
    manifest = api.document(store(root, step["manifest"]))
    step["request"] = manifest["request"]
    store(root, step["request"])
    before = {}
    for name, ref in receipt["beforeimages"].items():
        assert ref is not None
        before[name] = store(root, ref)
        store(root, {"path": name, "sha256": api.sha(before[name])}, before[name])
    for name, expected in manifest["outputs"].items():
        ref = {
            "path": str((fixture.stage / "candidate" / name).relative_to(root)),
            "sha256": expected,
        }
        store(root, ref)
        step["afterimages"][name] = ref
    for name, expected in manifest["inputs"].items():
        if (str(root), name, expected) not in captured:
            store(root, {"path": name, "sha256": expected})
    for name, expected in manifest["legacy_inputs"].items():
        store(fixture.legacy, {"path": name, "sha256": expected})
    store(root, receipt["acceptance"])
    for ref in receipt["retired_sources"].values():
        store(root, ref)
    return {
        "steps": [step],
        "captured": captured,
        "baseline_owners": {n: b for n, b in before.items() if n.startswith("data/ingredients/")},
        "baseline_ledgers": {n: before[n] for n in transition_api.LEDGERS},
        "current_owners": {
            str(p.relative_to(root)): p.read_bytes() for p in root.glob("data/ingredients/*/*.yaml")
        },
        "current_ledgers": {n: (root / n).read_bytes() for n in transition_api.LEDGERS},
        "schema_root": root,
    }


@pytest.fixture
def case(distinct_baselines):
    return copy.deepcopy(distinct_baselines)


def test_native_distinct_committed_baselines_reconstruct_complete_adoption(case):
    step = case["steps"][0]
    request, manifest = (document(case, step, key) for key in ("request", "manifest"))
    migration = captured_document(
        case,
        step["root"],
        {
            "path": api.MIGRATION,
            "sha256": manifest["inputs"][api.MIGRATION],
        },
    )
    legacy = request["legacy"]
    plan = captured_document(case, legacy["root"], legacy["plan"])
    before = captured_document(case, legacy["root"], plan["before_inventory"])["owners"]
    assert migration["source_commit"] != plan["baseline_commit"]
    assert before != {r["path"]: r["before_sha256"] for r in migration["records"]}
    assert api.baseline_inventory(case["schema_root"], plan["baseline_commit"]) == before
    selected = {r["before_source_record"] for r in plan["records"]}
    assert "data/ingredients/mapped/Exact.yaml" not in selected
    proof = run(case)
    assert proof
    for name in ("data/ingredients/mapped/Exact.yaml", "data/ingredients/mapped/Move.yaml"):
        record = api.load_yaml(case["current_owners"][name])
        assert record["notes"].startswith("Synthetic corrected provenance")
        actions = [event["action"] for event in record["curation_history"]]
        assert actions == [
            "CREATED",
            "CORRECTED_SOURCE_PROVENANCE",
            "ASSIGNED_MIM_ID",
            "ADOPTED_CAMPAIGN_MIM_ID",
        ]


@pytest.mark.parametrize(
    "attack", ["missing_commit", "wrong_commit", "wrong_preimage", "omitted_owner"]
)
def test_original_mint_baseline_requires_complete_actual_git_bytes(case, attack):
    step = case["steps"][0]
    manifest = document(case, step, "manifest")
    ref = {"path": api.MIGRATION, "sha256": manifest["inputs"][api.MIGRATION]}
    migration = captured_document(case, step["root"], ref)
    if attack == "missing_commit":
        migration["source_commit"] = "0" * 40
        reason = "Git command failed"
    elif attack == "wrong_commit":
        migration["source_commit"] = manifest["head"]
        reason = "original mint Git baseline differs"
    elif attack == "wrong_preimage":
        migration["records"][0]["before_sha256"] = "0" * 64
        reason = "original mint Git baseline differs"
    else:
        migration["records"].pop()
        reason = "source baseline differs"
    changed = replace(case, step["root"], ref, api.encoded(migration))
    manifest["inputs"][api.MIGRATION] = changed["sha256"]
    rebind(case, step, manifest=manifest)
    with pytest.raises(ValueError, match=reason):
        run(case)


def rewrite_legacy(case, change):
    """Rebind every immediate source-plan/application/context link, retaining reviews."""
    step = case["steps"][0]
    request, manifest = (document(case, step, key) for key in ("request", "manifest"))
    legacy = request["legacy"]
    root = legacy["root"]
    plan = captured_document(case, root, legacy["plan"])
    application = captured_document(case, root, legacy["application"])
    acceptance = captured_document(case, root, application["acceptance"])
    before = captured_document(case, root, plan["before_inventory"])
    after = captured_document(case, root, plan["after_inventory"])
    change(request, manifest, plan, application, before, after)
    for field, value in [("before_inventory", before), ("after_inventory", after)]:
        plan[field] = replace(case, root, plan[field], api.encoded(value))
        manifest["legacy_inputs"][plan[field]["path"]] = plan[field]["sha256"]
        application[field] = value["owners"]
    legacy["plan"] = replace(case, root, legacy["plan"], api.encoded(plan))
    manifest["legacy_inputs"][legacy["plan"]["path"]] = legacy["plan"]["sha256"]
    application["plan"] = legacy["plan"]
    application["baseline_commit"] = acceptance["baseline_commit"] = plan["baseline_commit"]
    acceptance["plan_sha256"] = legacy["plan"]["sha256"]
    application["acceptance"] = replace(
        case, root, application["acceptance"], api.encoded(acceptance)
    )
    manifest["legacy_inputs"][application["acceptance"]["path"]] = application["acceptance"][
        "sha256"
    ]
    legacy["application"] = replace(case, root, legacy["application"], api.encoded(application))
    manifest["legacy_inputs"][legacy["application"]["path"]] = legacy["application"]["sha256"]
    context = captured_document(case, step["root"], request["context"])
    context.update(
        legacy_plan=plan,
        legacy_application=legacy["application"],
        legacy_inventory=application["after_inventory"],
    )
    request["context"] = replace(case, step["root"], request["context"], api.encoded(context))
    manifest["inputs"][request["context"]["path"]] = request["context"]["sha256"]
    rebind(case, step, request=request, manifest=manifest)


@pytest.mark.parametrize(
    "attack", ["missing_commit", "wrong_commit", "wrong_hash", "omitted_owner", "extra_owner"]
)
def test_corrected_baseline_cannot_be_authorized_by_rehashed_json(case, attack):
    def change(request, manifest, plan, application, before, after):
        if attack == "missing_commit":
            plan["baseline_commit"] = "0" * 40
        elif attack == "wrong_commit":
            migration = captured_document(
                case,
                case["steps"][0]["root"],
                {
                    "path": api.MIGRATION,
                    "sha256": manifest["inputs"][api.MIGRATION],
                },
            )
            plan["baseline_commit"] = migration["source_commit"]
        elif attack == "wrong_hash":
            before["owners"][next(iter(before["owners"]))] = "0" * 64
        elif attack == "omitted_owner":
            before["owners"].pop(next(iter(before["owners"])))
        else:
            before["owners"]["data/ingredients/mapped/Invented.yaml"] = "0" * 64

    rewrite_legacy(case, change)
    reason = (
        "Git command failed"
        if attack == "missing_commit"
        else (
            "source baseline differs"
            if attack in {"omitted_owner", "extra_owner"}
            else "corrected legacy Git baseline differs"
        )
    )
    with pytest.raises(ValueError, match=reason):
        run(case)


def test_even_genuine_rehashed_legacy_baseline_cannot_rewrite_original_history(case, tmp_path):
    clone = tmp_path / "same-mim-authority"
    command(case["schema_root"], "clone", "--no-hardlinks", str(case["schema_root"]), str(clone))
    command(
        clone,
        "remote",
        "set-url",
        "origin",
        "https://github.com/CultureBotAI/MediaIngredientMech.git",
    )
    command(clone, "config", "user.name", "Synthetic reviewer")
    command(clone, "config", "user.email", "fixture@example.invalid")
    case["schema_root"] = clone

    def change(request, manifest, plan, application, before, after):
        # Use a genuine new commit, not a fake hash, then rebind the full claim.
        command(clone, "checkout", "--detach", plan["baseline_commit"])
        name = "data/ingredients/mapped/Exact.yaml"
        record = yaml.safe_load((clone / name).read_bytes())
        record["curation_history"][0]["changes"] = "Rewritten original science"
        raw = yaml.safe_dump(record, sort_keys=False).encode()
        (clone / name).write_bytes(raw)
        plan["baseline_commit"] = commit(clone)
        ref = replace(case, request["legacy"]["root"], {"path": name}, raw)
        before["owners"][name] = after["owners"][name] = ref["sha256"]
        manifest["legacy_inputs"][name] = ref["sha256"]
        # Restore the schema worktree; immutable baseline objects stay available.
        command(clone, "checkout", "--detach", document(case, case["steps"][0], "manifest")["head"])

    rewrite_legacy(case, change)
    with pytest.raises(ValueError, match="original source/mint history differs"):
        run(case)


@pytest.mark.parametrize("quote_paths", ["true", "false"])
def test_git_baseline_reader_preserves_literal_unusual_owner_names(tmp_path, quote_paths):
    from tests.test_stable_id_adoption import initialize

    initialize(tmp_path)
    command(tmp_path, "config", "core.quotePath", quote_paths)
    name = 'data/ingredients/mapped/Unicode-α-"quoted"-line\nbreak.yaml'
    path = tmp_path / name
    path.parent.mkdir(parents=True)
    raw = b"identifier: UNMAPPED_1\n"
    path.write_bytes(raw)
    revision = commit(tmp_path)
    assert transition_api._git_baseline_owners(tmp_path, revision) == {name: raw}
