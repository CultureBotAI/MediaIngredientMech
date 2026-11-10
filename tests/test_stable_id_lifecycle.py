"""Explicit split/deprecation addresses never choose scientific successors (#1300)."""

import importlib.util
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.curie import CurieNormalizer
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    Lifecycle,
    Mint,
    Registry,
    StableIdError,
    UnresolvedIdError,
    allocate_ids,
    append_lifecycle,
    check_append_only,
    dump_lifecycle,
    dump_registry,
    inspect_id,
    inspect_ids,
    parse_registry,
    resolve_id,
    validate_records,
    validate_registry,
)


def mid(number):
    return f"MIM:{number:07d}"


def minted(count=6):
    return Registry(
        tuple(Mint(mid(n), f"Historical {n}", "2026-11-08") for n in range(1, count + 1))
    )


def event(number, status, targets="", time="2026-11-08T12:00:00Z"):
    return Lifecycle(mid(number), status, targets, time, "Reviewed scope; receipt <source>")


def history():
    return Registry(
        minted().entries,
        (
            event(1, "merged", mid(2)),
            event(2, "split", f"{mid(3)}|{mid(4)}"),
            event(3, "retired", mid(5)),
            event(4, "deprecated"),
        ),
    )


def save_corpus(root, registry):
    (root / REGISTRY_PATH).parent.mkdir(parents=True)
    (root / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (root / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
    for identifier, (status, _) in registry.states.items():
        if status == "active":
            path = root / "data/ingredients/mapped" / f"{identifier.replace(':', '_')}.yaml"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                yaml.safe_dump(
                    {
                        "mim_id": identifier,
                        "identifier": "CHEBI:1",
                        "preferred_term": identifier,
                        "legacy_identifiers": ["kgmicrobe.compound:shared"],
                    }
                )
            )
    mappings = root / "mappings"
    mappings.mkdir()
    (mappings / "mim_curie_aliases.tsv").write_text(
        "old_curie\tcurrent_curie\nMIM:Old\tMIM:0000001\nMIM:Dead\tMIM:0000004\n"
        "MIM:Split\tMIM:0000002\n"
    )
    (mappings / "ingredient_mappings.sssom.tsv").write_text(
        "subject_id\tobject_id\tpredicate_id\n"
        "MIM:0000001\tCHEBI:999\tskos:exactMatch\n"
        "MIM:0000002\tCHEBI:998\tskos:exactMatch\n"
        "MIM:0000004\tCHEBI:997\tskos:exactMatch\n"
        "MIM:0000005\tCHEBI:5\tskos:broadMatch\n"
        "MIM:0000006\tCHEBI:6\tskos:exactMatch\n"
    )


def test_typed_inspection_preserves_direct_split_targets_and_chain_context():
    registry = history()
    results = inspect_ids(registry)
    assert results[mid(1)] == inspect_id(registry, mid(1))
    assert results[mid(1)].identifier == mid(1)
    assert results[mid(1)].at_id == mid(2)
    assert results[mid(1)].status == "split"
    assert results[mid(1)].successors == (mid(3), mid(4))
    assert results[mid(4)].status == "deprecated" and results[mid(4)].successors == ()
    assert results[mid(3)].status == "active" and results[mid(3)].at_id == mid(5)
    assert resolve_id(registry, mid(3)) == mid(5)
    for number, status in [(1, "split"), (2, "split"), (4, "deprecated")]:
        with pytest.raises(UnresolvedIdError) as caught:
            resolve_id(registry, mid(number))
        assert caught.value.resolution == results[mid(number)]
        assert status in str(caught.value)
    with pytest.raises(StableIdError, match="Unknown"):
        inspect_id(registry, mid(7))


def test_split_does_not_resolve_even_if_both_children_later_merge_to_same_record():
    registry = Registry(
        minted().entries,
        (
            event(1, "split", f"{mid(2)}|{mid(3)}"),
            event(2, "merged", mid(4)),
            event(3, "merged", mid(4)),
        ),
    )
    validate_registry(registry)
    assert resolve_id(registry, mid(2)) == resolve_id(registry, mid(3)) == mid(4)
    with pytest.raises(UnresolvedIdError):
        resolve_id(registry, mid(1))


@pytest.mark.parametrize(
    "targets",
    [
        "",
        mid(2),
        f"{mid(2)}|{mid(2)}",
        f"{mid(3)}|{mid(2)}",
        f"{mid(2)}|{mid(9)}",
        f"{mid(1)}|{mid(2)}",
        f"{mid(2)}|",
        f"|{mid(2)}|{mid(3)}",
        f"{mid(2)}||{mid(3)}",
        f"{mid(2)} |{mid(3)}",
        f"{mid(2)},{mid(3)}",
        "MIM:0000000|MIM:0000002",
        "MIM:٢|MIM:0000003",
        None,
        [mid(2), mid(3)],
    ],
)
def test_split_target_encoding_refuses_malformed_duplicate_unknown_and_self(targets):
    with pytest.raises(StableIdError):
        validate_registry(Registry(minted().entries, (event(1, "split", targets),)))


@pytest.mark.parametrize("targets", [mid(2), f"{mid(2)}|{mid(3)}", " ", None])
def test_deprecation_has_no_guessed_successor(targets):
    with pytest.raises(StableIdError, match="no replacement"):
        validate_registry(Registry(minted().entries, (event(1, "deprecated", targets),)))


@pytest.mark.parametrize(
    "events",
    [
        (event(1, "split", f"{mid(2)}|{mid(3)}"), event(2, "merged", mid(1))),
        (event(1, "split", f"{mid(2)}|{mid(3)}"), event(3, "split", f"{mid(1)}|{mid(4)}")),
        (event(1, "deprecated"), event(1, "merged", mid(2))),
        (event(1, "split", f"{mid(2)}|{mid(3)}"), event(1, "deprecated")),
        (event(1, "deprecated", time="2026-11-07T12:00:00Z"),),
        (event(1, "deprecated", time="2026-11-08T12:00:00"),),
        (event(1, "deprecated"), event(2, "deprecated", time="2026-11-08T11:00:00Z")),
    ],
)
def test_new_states_preserve_graph_terminal_and_time_guards(events):
    with pytest.raises(StableIdError):
        validate_registry(Registry(minted().entries, events))


def test_split_event_cannot_predate_any_target_mint():
    entries = (*minted(2).entries, Mint(mid(3), "New target", "2026-11-09"))
    with pytest.raises(StableIdError, match="predates"):
        validate_registry(Registry(entries, (event(1, "split", f"{mid(2)}|{mid(3)}"),)))


def test_new_events_append_without_rewriting_old_bytes_or_reusing_ids():
    old = Registry(minted().entries, (event(1, "retired", mid(2)),))
    raw_mints, raw_events = dump_registry(old), dump_lifecycle(old)
    new = append_lifecycle(old, **event(2, "split", f"{mid(3)}|{mid(4)}").__dict__)
    new = append_lifecycle(new, **event(4, "deprecated").__dict__)
    assert dump_registry(new) == raw_mints
    check_append_only(dump_lifecycle(new), raw_events, label="lifecycle")
    assert parse_registry(raw_mints, dump_lifecycle(new)) == new
    plan = allocate_ids(
        new, {"new.yaml": {"preferred_term": "Reviewed new concept"}}, minted_on="2026-11-09"
    )
    assert plan.assignments == {"new.yaml": mid(7)}
    assert plan.registry.entries[:6] == new.entries and plan.registry.events == new.events
    for number in (1, 2, 4):
        with pytest.raises(StableIdError, match="active"):
            allocate_ids(new, {"old.yaml": {"mim_id": mid(number)}}, minted_on="2026-11-09")
    with pytest.raises(StableIdError, match="rewrites"):
        check_append_only(
            dump_lifecycle(new).replace(b"Reviewed", b"Changed"), raw_events, label="lifecycle"
        )


def test_active_inventory_still_requires_exactly_all_live_ids():
    registry = history()
    records = {
        "a.yaml": {"mim_id": mid(5)},
        "b.yaml": {"mim_id": mid(6), "mapping_status": "REJECTED"},
    }
    validate_records(registry, records)
    for number in (1, 2, 4):
        with pytest.raises(StableIdError, match="unknown or retired"):
            validate_records(registry, {**records, "old.yaml": {"mim_id": mid(number)}})
    with pytest.raises(StableIdError, match="exactly one"):
        validate_records(registry, {"a.yaml": records["a.yaml"]})


def test_graph_validation_handles_long_chains_without_recursion():
    registry = Registry(
        minted(1200).entries, tuple(event(n, "merged", mid(n + 1)) for n in range(1, 1200))
    )
    assert resolve_id(registry, mid(1)) == mid(1200)


def test_normalizer_keeps_split_deprecated_and_scientific_mapping_boundaries(tmp_path):
    save_corpus(tmp_path, history())
    normalizer = CurieNormalizer(repo_root=tmp_path)
    for reference in (mid(1), "mim:0000001", mid(2), "MIM:Old", "MIM:Split"):
        assert normalizer.resolve(reference).problem == "SPLIT_SUBJECT"
        assert normalizer.equivalent_term(reference).problem == "SPLIT_SUBJECT"
    for reference in (mid(4), "mim:0000004", "MIM:Dead"):
        assert normalizer.resolve(reference).problem == "DEPRECATED_SUBJECT"
        assert normalizer.equivalent_term(reference).problem == "DEPRECATED_SUBJECT"
    assert normalizer.resolve(mid(3)).curie == mid(5)
    assert normalizer.equivalent_term(mid(3)).problem == "RETIRED_SUBJECT"
    assert normalizer.equivalent_term(mid(5)).problem == "NO_EXACT_MATCH"
    assert normalizer.equivalent_term(mid(6)).curie == "CHEBI:6"
    assert normalizer.resolve("kgmicrobe.compound:shared").problem == "AMBIGUOUS_ALIAS"
    assert normalizer.resolve(mid(9)).problem == "UNKNOWN_SUBJECT"
    assert set(normalizer._mappings) == {mid(5), mid(6)}


def test_conflicting_historical_aliases_never_choose_a_terminal_or_split_child(tmp_path):
    save_corpus(tmp_path, history())
    aliases = tmp_path / "mappings/mim_curie_aliases.tsv"
    with aliases.open("a") as f:
        f.write("MIM:Shared\tMIM:0000002\nMIM:Shared\tMIM:0000004\n")
    with pytest.raises(ValueError, match="Conflicting historical MIM alias"):
        CurieNormalizer(repo_root=tmp_path)


def test_all_stable_pages_survive_split_deprecation_without_arbitrary_redirects(tmp_path):
    save_corpus(tmp_path, history())
    script = Path(__file__).resolve().parents[1] / "scripts/build_pages_site.py"
    spec = importlib.util.spec_from_file_location("lifecycle_site", script)
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    pages = builder.resolver_documents(tmp_path)
    assert len(pages) == 6
    first = pages["ingredient/MIM_0000001/index.html"]
    split = pages["ingredient/MIM_0000002/index.html"]
    dead = pages["ingredient/MIM_0000004/index.html"]
    for html in (first, split):
        assert 'href="../MIM_0000003/"' in html and 'href="../MIM_0000004/"' in html
        assert "No single successor is selected" in html
        assert (
            'http-equiv="refresh"' not in html and "Open the current replacement record" not in html
        )
        assert "receipt &lt;source&gt;" in html and "receipt <source>" not in html
    assert "Historical 1" in first and "replacement chain reaches" in first
    assert "Historical 2" in split
    assert "deprecated without a justified successor" in dead
    assert 'href="../MIM_' not in dead and 'http-equiv="refresh"' not in dead
    assert 'href="../MIM_0000005/"' in pages["ingredient/MIM_0000003/index.html"]
    assert 'http-equiv="refresh"' in pages["ingredient/MIM_0000005/index.html"]


def test_older_merge_reaches_later_deprecation_without_breaking_other_lookup(tmp_path):
    registry = Registry(minted(3).entries, (event(1, "merged", mid(2)), event(2, "deprecated")))
    save_corpus(tmp_path, registry)
    assert inspect_id(registry, mid(1)).at_id == mid(2)
    normalizer = CurieNormalizer(repo_root=tmp_path)
    assert normalizer.resolve(mid(1)).problem == "DEPRECATED_SUBJECT"
    assert normalizer.resolve(mid(3)).curie == mid(3)
