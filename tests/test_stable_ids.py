"""Stable identity survives label/mapping changes; old allocations never disappear."""

import importlib.util
import subprocess
from dataclasses import replace
from pathlib import Path

import pytest

from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    Lifecycle,
    Mint,
    Registry,
    StableIdError,
    allocate_ids,
    append_lifecycle,
    build_record_index,
    check_append_only,
    dump_lifecycle,
    dump_registry,
    parse_registry,
    resolve_id,
    resolver_url,
    validate_history,
    validate_id,
    validate_records,
    validate_registry,
)


def minted(count=3):
    return Registry(
        tuple(Mint(f"MIM:{n:07d}", f"label {n}", "2026-11-08") for n in range(1, count + 1))
    )


def records(count=3):
    return {
        f"unmapped/{n}.yaml": {"mim_id": f"MIM:{n:07d}", "preferred_term": f"label {n}"}
        for n in range(1, count + 1)
    }


def event(identifier="MIM:0000001", replacement="MIM:0000002", **kwargs):
    return Lifecycle(
        identifier,
        kwargs.get("status", "merged"),
        replacement,
        "2026-11-08T12:00:00Z",
        "Reviewed duplicate resolution",
    )


def test_initial_allocation_orders_paths_and_repeated_plans_preserve_ids():
    original = {
        "unmapped/z.yaml": {"preferred_term": "z"},
        "mapped/a.yaml": {"preferred_term": "a"},
    }
    plan = allocate_ids(Registry(), original, minted_on="2026-11-08")
    assert plan.assignments == {"mapped/a.yaml": "MIM:0000001", "unmapped/z.yaml": "MIM:0000002"}
    assigned = {
        path: {**record, "mim_id": plan.assignments[path]} for path, record in original.items()
    }
    assigned["unmapped/z.yaml"].update(preferred_term="Corrected name", identifier="CHEBI:1")
    assigned["mapped/new-name.yaml"] = assigned.pop("unmapped/z.yaml")
    repeated = allocate_ids(plan.registry, assigned, minted_on="2026-11-09")
    assert repeated.registry == plan.registry
    assert repeated.assignments["mapped/new-name.yaml"] == "MIM:0000002"
    assert "mim_id" not in original["mapped/a.yaml"]


def test_mint_after_retirement_uses_highest_ever_id():
    registry = Registry(minted().entries, (event(),))
    plan = allocate_ids(registry, {"new.yaml": {"preferred_term": "next"}}, minted_on="2026-11-08")
    assert plan.assignments == {"new.yaml": "MIM:0000004"}
    assert plan.registry.entries[:3] == registry.entries
    assert plan.registry.events == registry.events


@pytest.mark.parametrize(
    "value",
    [
        None,
        1,
        "MIM:0000000",
        "MIM:1",
        "MIM:00000001",
        "MIM:0000001\n",
        "mim:0000001",
        "MIM:١٢٣٤٥٦٧",
    ],
)
def test_exact_id_shape(value):
    with pytest.raises(StableIdError):
        validate_id(value)


def test_resolver_expands_numeric_suffix():
    assert (
        resolver_url("MIM:0000001")
        == "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_0000001"
    )


@pytest.mark.parametrize(
    "entries",
    [
        (Mint("MIM:0000002", "skipped", "2026-11-08"),),
        (*minted(2).entries, minted(2).entries[-1]),
        (replace(minted(1).entries[0], status="retired", replaced_by="MIM:0000002"),),
    ],
)
def test_registry_rejects_gaps_reuse_and_mutated_mint_state(entries):
    with pytest.raises(StableIdError):
        validate_registry(Registry(entries))


def test_roundtrip_retains_exact_mint_labels_and_original_status():
    registry = Registry((Mint("MIM:0000001", 'α "label"\u2028suffix', "2026-11-08"),))
    assert parse_registry(dump_registry(registry), dump_lifecycle(registry)) == registry


@pytest.mark.parametrize(
    "events",
    [
        (event(replacement="MIM:0000009"),),
        (event(replacement="MIM:0000001"),),
        (event(), event(identifier="MIM:0000002", replacement="MIM:0000001")),
        (event(), event(replacement="MIM:0000003")),
        (event(status="active"),),
        (replace(event(), changed_at="2026-11-08T12:00:00"),),
    ],
)
def test_invalid_lifecycle_history_fails(events):
    with pytest.raises(StableIdError):
        validate_registry(Registry(minted().entries, events))


@pytest.mark.parametrize("route", ["planner", "persisted-ledger"])
def test_concept_split_status_is_not_a_supported_lifecycle(route):
    registry = minted()
    original = (dump_registry(registry), dump_lifecycle(registry))
    proposal = event(status="split")
    with pytest.raises(StableIdError, match="Lifecycle status must be retired or merged"):
        if route == "planner":
            append_lifecycle(registry, **proposal.__dict__)
        else:
            raw_event = "\t".join(proposal.__dict__.values()).encode() + b"\n"
            parse_registry(original[0], original[1] + raw_event)
    assert (dump_registry(registry), dump_lifecycle(registry)) == original


@pytest.mark.parametrize(
    "replacements",
    [
        ["MIM:0000002", "MIM:0000003"],
        ("MIM:0000002", "MIM:0000003"),
        "MIM:0000002|MIM:0000003",
        "MIM:0000002,MIM:0000003",
        "MIM:0000002 MIM:0000003",
    ],
)
def test_concept_split_cannot_hide_multiple_replacements_in_retirement(replacements):
    registry = minted()
    original = (dump_registry(registry), dump_lifecycle(registry))
    proposal = event(status="retired", replacement=replacements)
    with pytest.raises(StableIdError, match="Expected a positive seven-digit MIM identifier"):
        append_lifecycle(registry, **proposal.__dict__)
    if isinstance(replacements, str):
        raw_event = "\t".join(proposal.__dict__.values()).encode() + b"\n"
        with pytest.raises(StableIdError, match="Expected a positive seven-digit MIM identifier"):
            parse_registry(original[0], original[1] + raw_event)
    assert (dump_registry(registry), dump_lifecycle(registry)) == original


def test_replacement_chain_retains_old_mints_and_resolves_active_target():
    first = append_lifecycle(minted(), **event().__dict__)
    second = append_lifecycle(
        first, **event(identifier="MIM:0000002", replacement="MIM:0000003").__dict__
    )
    assert resolve_id(second, "MIM:0000001") == "MIM:0000003"
    assert second.entries == minted().entries
    assert second.states["MIM:0000001"] == ("merged", "MIM:0000002")
    with pytest.raises(StableIdError, match="Unknown"):
        resolve_id(second, "MIM:0000004")


@pytest.mark.parametrize("mode", ["missing", "duplicate", "unknown", "retired", "missing-record"])
def test_complete_inventory_cannot_lose_or_reuse_ids(mode):
    registry = minted()
    current = records()
    if mode == "missing":
        del current["unmapped/1.yaml"]["mim_id"]
    elif mode == "duplicate":
        current["unmapped/2.yaml"]["mim_id"] = "MIM:0000001"
    elif mode == "unknown":
        current["unmapped/2.yaml"]["mim_id"] = "MIM:0000009"
    elif mode == "retired":
        registry = Registry(registry.entries, (event(),))
    else:
        current.pop("unmapped/1.yaml")
    with pytest.raises(StableIdError):
        validate_records(registry, current)


def test_mapping_rejection_is_not_identity_retirement():
    current = records()
    current["unmapped/1.yaml"]["mapping_status"] = "REJECTED"
    validate_records(minted(), current)


def test_legacy_alias_ambiguity_is_preserved_and_never_silently_selected():
    current = records(2)
    current["unmapped/1.yaml"]["legacy_identifiers"] = ["MIM:old_name", "kgmicrobe.compound:shared"]
    current["unmapped/2.yaml"]["legacy_identifiers"] = ["kgmicrobe.compound:shared"]
    validate_records(minted(2), current)
    index = build_record_index(current)
    assert index.lookup("MIM:0000001") == index.lookup("MIM:old_name") == "unmapped/1.yaml"
    assert len(index.ambiguous_aliases["kgmicrobe.compound:shared"]) == 2
    with pytest.raises(StableIdError, match="ambiguous"):
        index.lookup("kgmicrobe.compound:shared")


def test_append_only_compares_existing_bytes_not_just_ids():
    old = dump_registry(minted(2))
    check_append_only(dump_registry(minted()), old, label="registry")
    with pytest.raises(StableIdError, match="rewrites"):
        check_append_only(old.replace(b"label 1", b"label X"), old, label="registry")
    with pytest.raises(StableIdError, match="removes"):
        check_append_only(dump_registry(minted(1)), old, label="registry")


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def test_trusted_history_rejects_existing_row_edits_and_terminal_event_rewrites(tmp_path):
    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Fixture")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    (tmp_path / REGISTRY_PATH).parent.mkdir(parents=True)
    registry = Registry(minted().entries, (event(),))
    for path, value in [
        (REGISTRY_PATH, dump_registry(registry)),
        (LIFECYCLE_PATH, dump_lifecycle(registry)),
    ]:
        (tmp_path / path).write_bytes(value)
    git(tmp_path, "add", "data")
    git(tmp_path, "commit", "-qm", "mint fixture")
    base = git(tmp_path, "rev-parse", "HEAD")
    validate_history(tmp_path, base)
    original = (tmp_path / LIFECYCLE_PATH).read_bytes()
    (tmp_path / LIFECYCLE_PATH).write_bytes(original.replace(b"MIM:0000002", b"MIM:0000003"))
    with pytest.raises(StableIdError, match="rewrites"):
        validate_history(tmp_path, base)
    (tmp_path / LIFECYCLE_PATH).write_bytes(original)
    original = (tmp_path / REGISTRY_PATH).read_bytes()
    (tmp_path / REGISTRY_PATH).write_bytes(original.replace(b"label 1", b"label X"))
    with pytest.raises(StableIdError, match="rewrites"):
        validate_history(tmp_path, base)


def test_cli_rejects_duplicate_yaml_id_fields():
    file = Path(__file__).parents[1] / "scripts/validate_stable_ids.py"
    spec = importlib.util.spec_from_file_location("validate_stable_ids", file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with pytest.raises(StableIdError, match="Duplicate YAML key"):
        module.yaml.load(
            "mim_id: MIM:0000001\nmim_id: MIM:0000002\n", Loader=module.UniqueKeyLoader
        )


@pytest.mark.parametrize("identifier", ["MIM:0000001", None, "MIM:0000000", "MIM:0000001\n"])
def test_authoritative_schema_requires_exact_stable_identity(identifier):
    from mediaingredientmech.validation.write_validated import validate_ingredient

    record = {"identifier": "UNMAPPED_0001", "preferred_term": "Test", "mapping_status": "UNMAPPED"}
    if identifier is not None:
        record["mim_id"] = identifier
    errors = validate_ingredient(record)
    assert bool(errors) == (identifier != "MIM:0000001")


def test_extra_duplicate_record_fails_even_when_every_active_id_is_present():
    current = records()
    current["mapped/duplicate.yaml"] = dict(current["unmapped/1.yaml"])
    with pytest.raises(StableIdError, match="Duplicate MIM ID"):
        validate_records(minted(), current)


def test_terminal_ids_are_registered_but_have_no_current_record():
    registry = Registry(minted().entries, (event(),))
    current = records()
    del current["unmapped/1.yaml"]
    validate_records(registry, current)
    assert resolve_id(registry, "MIM:0000001") == "MIM:0000002"


def test_ci_checks_trusted_history_for_pr_and_merge_group_without_path_skips():
    import yaml

    root = Path(__file__).parents[1]
    workflow = yaml.load(
        (root / ".github/workflows/qc-stable-ids.yaml").read_text(), Loader=yaml.BaseLoader
    )
    assert "pull_request" in workflow["on"]
    assert "merge_group" in workflow["on"]
    assert not workflow["on"]["pull_request"]
    assert workflow["on"]["merge_group"] == {"types": ["checks_requested"]}
    assert "github.event.pull_request.base.sha" in workflow["env"]["MIM_ID_BASE"]
    assert "github.event.merge_group.base_sha" in workflow["env"]["MIM_ID_BASE"]
    steps = workflow["jobs"]["qc"]["steps"]
    assert steps[0]["with"]["fetch-depth"] == "0"
    assert (
        steps[-1]["run"]
        == 'python scripts/validate_stable_ids.py --require-history --base "$MIM_ID_BASE"'
    )


def historical_inventory(tmp_path, current, registry):
    import yaml

    git(tmp_path, "init", "-q")
    git(tmp_path, "config", "user.name", "Fixture")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    (tmp_path / REGISTRY_PATH).parent.mkdir(parents=True)
    (tmp_path / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (tmp_path / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
    for path, record in current.items():
        destination = tmp_path / "data/ingredients" / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(yaml.safe_dump(record))
    git(tmp_path, "add", "data")
    git(tmp_path, "commit", "-qm", "trusted inventory")
    return git(tmp_path, "rev-parse", "HEAD")


def test_same_path_id_swap_fails_even_with_unique_complete_registry_inventory(tmp_path):
    import yaml

    current = records(2)
    base = historical_inventory(tmp_path, current, minted(2))
    current["unmapped/1.yaml"]["mim_id"], current["unmapped/2.yaml"]["mim_id"] = (
        current["unmapped/2.yaml"]["mim_id"],
        current["unmapped/1.yaml"]["mim_id"],
    )
    validate_records(minted(2), current)
    for path, record in current.items():
        (tmp_path / "data/ingredients" / path).write_text(yaml.safe_dump(record))
    with pytest.raises(StableIdError, match="changed permanent mim_id"):
        validate_history(tmp_path, base)


def test_record_move_name_and_mapping_changes_keep_permanent_identity(tmp_path):
    import yaml

    current = records(2)
    base = historical_inventory(tmp_path, current, minted(2))
    first = current.pop("unmapped/1.yaml")
    first.update(preferred_term="Corrected label", identifier="CHEBI:123")
    current["mapped/renamed.yaml"] = first
    (tmp_path / "data/ingredients/unmapped/1.yaml").unlink()
    destination = tmp_path / "data/ingredients/mapped/renamed.yaml"
    destination.parent.mkdir(parents=True)
    destination.write_text(yaml.safe_dump(first))
    validate_records(minted(2), current)
    validate_history(tmp_path, base)


def test_initial_mint_may_add_identity_to_existing_historical_record(tmp_path):
    import yaml

    current = records(1)
    del current["unmapped/1.yaml"]["mim_id"]
    base = historical_inventory(tmp_path, current, Registry())
    current["unmapped/1.yaml"]["mim_id"] = "MIM:0000001"
    (tmp_path / "data/ingredients/unmapped/1.yaml").write_text(
        yaml.safe_dump(current["unmapped/1.yaml"])
    )
    (tmp_path / REGISTRY_PATH).write_bytes(dump_registry(minted(1)))
    validate_records(minted(1), current)
    validate_history(tmp_path, base)


@pytest.mark.parametrize("alias", ["MIM:0000002", "MIM:0000000", "MIM:12", "MIM:٠٠٠٠٠٠١"])
def test_numeric_mim_alias_cannot_impersonate_unknown_permanent_id(alias):
    index = build_record_index({"record.yaml": {
        "mim_id": "MIM:0000001", "legacy_identifiers": [alias, "MIM:old_name"],
    }})
    assert index.aliases[alias] == ("record.yaml",), "Historical text remains preserved"
    assert index.lookup("MIM:0000001") == "record.yaml"
    assert index.lookup("MIM:old_name") == "record.yaml"
    with pytest.raises(StableIdError, match="MIM (ID|identifier)"):
        index.lookup(alias)
