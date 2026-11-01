"""Strict receipt replay and exact-byte withdrawal proofs, without corpus quotas."""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import itertools
import json

import pytest

from mediaingredientmech.export.kgx import Graph, packed
from mediaingredientmech.validation import mapping_change_receipts as mcr


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def row(name="A", obj="CHEBI:1", **extra):
    return {
        "subject_id": "MIM:" + name,
        "subject_label": name,
        "predicate_id": "skos:exactMatch",
        "object_id": obj,
        "object_label": "term " + obj,
        "other": "",
        "confidence": "",
    } | extra


def sssom(rows):
    out = io.StringIO()
    out.write("# mapping_set_id: https://example.org/test\n# predicate_semantics: skos\n")
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


def write(root, name, value):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        value if isinstance(value, bytes) else (json.dumps(value, indent=2) + "\n").encode()
    )
    return path


def change(kind, before, after, before_position, after_position):
    return {
        "kind": kind,
        "before": before,
        "after": after,
        "before_position": before_position,
        "after_position": after_position,
    }


def receipt(before, after, positions, changes=(), *, sequence=1, records=()):
    return dict(
        schema_version=1,
        batch=f"batch-{sequence}",
        sequence=sequence,
        approval="NONE: mapping changes grant no approval",
        before_sha256=sha(sssom(before)),
        after_sha256=sha(sssom(after)),
        before_row_count=len(before),
        after_row_count=len(after),
        position_map=list(positions),
        changes=list(changes),
        records=list(records),
        **{
            kind + "_rows": sum(c["kind"] == kind for c in changes)
            for kind in ("added", "changed", "removed")
        },
    )


def walk(receipts, before, after):
    return mcr.walk_mapping_changes(
        receipts,
        start_sha256=sha(sssom(before)),
        reviewed_sha256=sha(sssom(after)),
        baseline_rows=before,
        refreshed_rows={},
    )


def history(root, rows):
    source_sha = sha(sssom(rows))
    write(root, mcr.BASELINE, {"schema_version": 1, "source_sha256": source_sha, "rows": rows})
    for name in (mcr.TRAIT_REFRESH, mcr.PARENT_REFRESH):
        write(
            root,
            name,
            {
                "schema_version": 1,
                "before_sha256": source_sha,
                "after_sha256": source_sha,
                "row_count": len(rows),
                "changed_rows": 0,
                "changes": [],
            },
        )


def repository(root, before, after=None, receipts=()):
    after = before if after is None else after
    history(root, before)
    write(root, mcr.SSSOM_SOURCE, sssom(after))
    for item in receipts:
        write(root, f"{mcr.RECEIPTS_DIR}/link-{item['sequence']}.json", item)
    return mcr.verify_mapping_chain(root)


def test_valid_reorder_removal_addition_and_repeated_correction():
    a, b, c = row(), row("B"), row("C")
    b2, b3, d = row("B", "CHEBI:2"), row("B", "CHEBI:3"), row("D")
    before, middle, after = [a, b, c], [c, b2, a], [b3, a, d]
    first = receipt(before, middle, [3, 2, 1], [change("changed", b, b2, 2, 2)])
    second = receipt(
        middle,
        after,
        [None, 1, 2],
        [
            change("changed", b2, b3, 2, 1),
            change("removed", c, None, 1, None),
            change("added", None, d, None, 3),
        ],
        sequence=2,
    )
    forward, last, state = walk([second, first], before, after)
    assert forward == [2, 1, None]
    assert state == after
    assert last[1]["receipt"] == "batch-2" and last[3]["kind"] == "added"
    assert "receipt" not in first and "receipt" not in first["changes"][0]


@pytest.mark.parametrize("value", [0, -1, True, False, 1.0, "1", 2])
def test_position_map_requires_true_one_based_integer(value):
    rows = [row()]
    item = receipt(rows, rows, [value])
    with pytest.raises(ValueError, match="position outside"):
        walk([item], rows, rows)


@pytest.mark.parametrize(
    "field", ["sequence", "before_row_count", "after_row_count", "changed_rows"]
)
def test_bool_is_not_a_sequence_or_count(field):
    rows = [row()]
    item = receipt(rows, rows, [1])
    item[field] = True
    with pytest.raises(ValueError, match="integer|position outside"):
        walk([item], rows, rows)


@pytest.mark.parametrize("field", ["schema_version", "changed_rows", "added_rows", "removed_rows"])
def test_published_document_domains_are_not_coerced(tmp_path, field):
    rows = [row()]
    item = receipt(rows, rows, [1])
    item[field] = True
    write(tmp_path, mcr.RECEIPTS_DIR + "/link-1.json", item)
    with pytest.raises(ValueError):
        mcr.load_receipts(tmp_path)


def test_silent_removal_is_refused_before_replay():
    before, after = [row(), row("B")], [row()]
    item = receipt(before, after, [1, None])
    with pytest.raises(ValueError, match="removals differ"):
        walk([item], before, after)


@pytest.mark.parametrize("kind", ["changed", "removed"])
def test_duplicate_original_change_is_refused_even_when_payloads_agree(kind):
    before, after = [row(), row("B")], [row(), row("B", "CHEBI:2")]
    c = change("changed", before[1], after[1], 2, 2)
    duplicate = c if kind == "changed" else change("removed", before[1], None, 2, None)
    item = receipt(before, after, [1, 2], [c, duplicate])
    with pytest.raises(ValueError, match="Duplicate original position"):
        walk([item], before, after)


def test_duplicate_addition_and_unaccounted_hole_are_refused():
    before, after = [row()], [row(), row("B")]
    c = change("added", None, after[1], None, 2)
    with pytest.raises(ValueError, match="occupied position"):
        walk([receipt(before, after, [1], [c, c])], before, after)
    with pytest.raises(ValueError, match="hole"):
        walk([receipt(before, after, [1])], before, after)


@pytest.mark.parametrize(
    "mutate,message",
    [
        (lambda r: r.update(changed_rows=1), "operation count"),
        (lambda r: r.update(approval="APPROVED"), "approval-free"),
        (lambda r: r.update(sequence=2), "numbered 1..n"),
        (lambda r: r.update(before_sha256=sha("wrong")), "previous link"),
        (lambda r: r.update(after_sha256=sha("wrong")), "reviewed source"),
    ],
)
def test_noop_receipt_still_checks_full_contract(mutate, message):
    rows = [row()]
    item = receipt(rows, rows, [1])
    mutate(item)
    with pytest.raises(ValueError, match=message):
        walk([item], rows, rows)


def test_operation_before_payload_and_position_must_match():
    before, after = [row()], [row("A", "CHEBI:2")]
    item = receipt(before, after, [1], [change("changed", row("wrong"), after[0], 1, 1)])
    with pytest.raises(ValueError, match="reviewed row"):
        walk([item], before, after)
    for value in (0, False, "1"):
        item["changes"][0].update(before=before[0], before_position=value)
        with pytest.raises(ValueError, match="position outside"):
            walk([item], before, after)


def test_minimal_zero_history_fixture_has_only_current_identity(tmp_path):
    rows = [row()]
    write(tmp_path, mcr.SSSOM_SOURCE, sssom(rows))
    proof = mcr.verify_mapping_chain(tmp_path)
    assert proof["receipts"] == proof["receipt_paths"] == []
    assert proof["receipt_inputs"] == proof["owner_chains"] == {}
    assert proof["forward"] == [1]
    assert proof["baseline_rows"] == proof["state"] == proof["states_after_sequence"][0] == rows
    assert proof["start_sha256"] == proof["reviewed_sha256"] == sha(sssom(rows))
    assert proof["input_hashes"] == {mcr.SSSOM_SOURCE: sha(sssom(rows))}


def test_complete_historical_prefix_without_receipts_is_valid(tmp_path):
    proof = repository(tmp_path, [row()])
    assert proof["receipt_paths"] == []
    assert set(proof["input_hashes"]) == {*mcr.HISTORICAL_CONTEXT, mcr.SSSOM_SOURCE}


@pytest.mark.parametrize(
    "present", [p for n in (1, 2) for p in itertools.combinations(mcr.HISTORICAL_CONTEXT, n)]
)
def test_each_partial_historical_context_is_refused(tmp_path, present):
    rows = [row()]
    history(tmp_path, rows)
    write(tmp_path, mcr.SSSOM_SOURCE, sssom(rows))
    for name in set(mcr.HISTORICAL_CONTEXT) - set(present):
        (tmp_path / name).unlink()
    with pytest.raises(ValueError, match="partial historical"):
        mcr.verify_mapping_chain(tmp_path)


def test_deleting_all_real_fixture_receipts_cannot_adopt_current_as_baseline(tmp_path):
    before, after = [row()], [row("A", "CHEBI:2")]
    item = receipt(before, after, [1], [change("changed", before[0], after[0], 1, 1)])
    assert repository(tmp_path, before, after, [item])["state"] == after
    for path in (tmp_path / mcr.RECEIPTS_DIR).glob("*.json"):
        path.unlink()
    with pytest.raises(ValueError, match="reviewed source"):
        mcr.verify_mapping_chain(tmp_path)


def test_nonempty_receipts_require_historical_prefix(tmp_path):
    rows = [row()]
    repository(tmp_path, rows, receipts=[receipt(rows, rows, [1])])
    for name in mcr.HISTORICAL_CONTEXT:
        (tmp_path / name).unlink()
    with pytest.raises(ValueError, match="historical"):
        mcr.verify_mapping_chain(tmp_path)


def test_synonym_prefix_is_replayed_and_cannot_change_identity(tmp_path):
    original, refreshed = row(), dict(row(), other="alias|β alias")
    history(tmp_path, [original])
    for name in (mcr.TRAIT_REFRESH, mcr.PARENT_REFRESH):
        write(
            tmp_path,
            name,
            {
                "schema_version": 1,
                "before_sha256": sha(sssom([original])),
                "after_sha256": sha(sssom([refreshed])),
                "row_count": 1,
                "changed_rows": 1,
                "changes": [{"source_position": 1, "before": original, "after": refreshed}],
            },
        )
        original = refreshed
    write(tmp_path, mcr.SSSOM_SOURCE, sssom([refreshed]))
    assert mcr.verify_mapping_chain(tmp_path)["refreshed_rows"] == {1: refreshed}
    path = tmp_path / mcr.TRAIT_REFRESH
    doc = json.loads(path.read_bytes())
    doc["changes"][0]["after"]["object_id"] = "CHEBI:99"
    write(tmp_path, mcr.TRAIT_REFRESH, doc)
    with pytest.raises(ValueError, match="non-synonym"):
        mcr.verify_mapping_chain(tmp_path)


@pytest.mark.parametrize(
    "surface", [mcr.BASELINE, mcr.SSSOM_SOURCE, mcr.RECEIPTS_DIR + "/link-1.json"]
)
def test_parse_and_hash_use_captured_bytes_and_refuse_late_drift(tmp_path, monkeypatch, surface):
    rows = [row()]
    repository(tmp_path, rows, receipts=[receipt(rows, rows, [1])])
    original = mcr._read
    changed = False

    def racing_read(root, name):
        nonlocal changed
        value = original(root, name)
        if name == surface and not changed:
            changed = True
            (root / name).write_bytes(value + b"\n")
        return value

    monkeypatch.setattr(mcr, "_read", racing_read)
    with pytest.raises(ValueError, match="bytes changed"):
        mcr.verify_mapping_chain(tmp_path)


def test_late_receipt_pathset_addition_is_refused(tmp_path, monkeypatch):
    rows = [row()]
    repository(tmp_path, rows, receipts=[receipt(rows, rows, [1])])
    original = mcr._json
    changed = False

    def racing_json(raw):
        nonlocal changed
        doc = original(raw)
        if not changed:
            changed = True
            write(tmp_path, mcr.RECEIPTS_DIR + "/unexpected.json", doc)
        return doc

    monkeypatch.setattr(mcr, "_json", racing_json)
    with pytest.raises(ValueError, match="inventory changed"):
        mcr.verify_mapping_chain(tmp_path)


def test_loader_rejects_duplicate_json_keys_and_path_aliases(tmp_path):
    rows = [row()]
    path = write(tmp_path, mcr.RECEIPTS_DIR + "/link-1.json", receipt(rows, rows, [1]))
    raw = path.read_bytes()
    path.write_bytes(raw.replace(b'"sequence": 1', b'"sequence": 1, "sequence": 1'))
    with pytest.raises(ValueError, match="Duplicate JSON"):
        mcr.load_receipts(tmp_path)
    original = tmp_path / "original.json"
    original.write_bytes(raw)
    path.unlink()
    path.symlink_to(original)
    with pytest.raises(ValueError, match="Aliased"):
        mcr.receipt_paths(tmp_path)


def owner(before, after, **fields):
    return dict(
        source_record="data/ingredients/mapped/A.yaml",
        before_yaml_sha256=before,
        after_yaml_sha256=after,
        **fields,
    )


def test_per_plan_supersession_uses_its_own_exact_pin_and_retains_noops(tmp_path):
    rows = [row()]
    h1, h2, h3 = map(sha, ("old", "middle", "new"))
    items = [
        receipt(rows, rows, [1], sequence=i, records=[owner(a, b)])
        for i, (a, b) in enumerate(((h1, h2), (h2, h2), (h2, h3)), 1)
    ]
    proof = repository(tmp_path, rows, receipts=items)
    path = owner(h1, h3)["source_record"]
    first = mcr.record_supersession(proof, owner=path, reviewed_sha256=h1, current_sha256=h3)
    second = mcr.record_supersession(proof, owner=path, reviewed_sha256=h2, current_sha256=h3)
    assert [r["sequence"] for r in first["receipts"]] == [1, 2, 3]
    assert [r["sequence"] for r in second["receipts"]] == [2, 3]
    assert "no approval" in first["reason"]
    for old, new in ((h3, h3), (sha("unknown"), h3), (h1, sha("wrong terminal")), (None, h3)):
        assert (
            mcr.record_supersession(proof, owner=path, reviewed_sha256=old, current_sha256=new)
            is None
        )
    assert (
        mcr.record_supersession(
            proof, owner="data/ingredients/mapped/B.yaml", reviewed_sha256=h1, current_sha256=h3
        )
        is None
    )
    assert mcr.load_receipts(tmp_path) == items
    assert mcr.receipt_paths(tmp_path) == proof["receipt_paths"]


@pytest.mark.parametrize("mode", ["gap", "duplicate", "missing-before"])
def test_invalid_owner_links_are_refused(tmp_path, mode):
    rows = [row()]
    h1, h2 = sha("old"), sha("new")
    records = [owner(h1, h2)]
    if mode == "duplicate":
        records *= 2
    if mode == "missing-before":
        records[0]["before_yaml_sha256"] = None
    items = [receipt(rows, rows, [1], records=records)]
    if mode == "gap":
        items.append(receipt(rows, rows, [1], sequence=2, records=[owner(h1, h2)]))
    with pytest.raises(ValueError, match="Owner receipt chain|Duplicate owner|Missing reviewed"):
        repository(tmp_path, rows, receipts=items)


def test_new_record_birth_is_not_an_archived_approval(tmp_path):
    rows = [row()]
    proof = repository(
        tmp_path,
        rows,
        receipts=[receipt(rows, rows, [1], records=[owner(None, sha("born"), shape="new_record")])],
    )
    assert (
        mcr.record_supersession(
            proof,
            owner=owner(None, "")["source_record"],
            reviewed_sha256=sha("imagined"),
            current_sha256=sha("born"),
        )
        is None
    )


def held_fixture(tmp_path, monkeypatch, *, move=True, operation=None):
    held = dict(row("Held"), other="α|β", confidence="")
    before = [row(), held]
    first = receipt(before, before, [1, 2])
    after, changes = (
        ([held], [change("removed", before[0], None, 1, None)]) if move else (before, [])
    )
    positions = [None, 1] if move else [1, 2]
    if operation == "changed":
        after = [dict(held, other="new")]
        changes.append(change("changed", held, after[0], 2, 1))
    elif operation == "samepayload":
        changes.append(change("changed", held, held, 2, 1))
    elif operation == "readded":
        positions = [None, None]
        changes.extend(
            [change("removed", held, None, 2, None), change("added", None, held, None, 1)]
        )
    second = receipt(before, after, positions, changes, sequence=2)
    proof = repository(tmp_path, before, after, [first, second])
    payload_sha = sha(json.dumps(held, sort_keys=True, separators=(",", ":")))
    frozen_id = mcr.assertion_identity(mcr.SSSOM_SOURCE, "mapping", 2, payload_sha)
    path = proof["receipt_paths"][0]
    checkpoint = {
        "sequence": 1,
        "path": path,
        "sha256": proof["receipt_inputs"][path],
        "after_sha256": first["after_sha256"],
        "position": 2,
    }
    monkeypatch.setattr(mcr, "HOLD_CHECKPOINTS", {frozen_id: checkpoint})
    position = 1 if move else 2
    graph = Graph()
    graph.nodes[held["subject_id"]] = {}
    graph.nodes[held["object_id"]] = {}
    for pos in (2, position):
        graph.edge(
            held["subject_id"],
            "biolink:exact_match",
            held["object_id"],
            "skos:exactMatch",
            "mapping",
            mcr.SSSOM_SOURCE,
            pos,
            held,
        )
    old_edge, edge = graph.edges
    # Native TSV projection includes empty optional columns outside the 11 hash fields.
    edge.update(publications="", metabolic_context="", concentration_value="")
    assertion = {
        "assertion_id": mcr.assertion_identity(mcr.SSSOM_SOURCE, "mapping", position, payload_sha),
        "source_record": mcr.SSSOM_SOURCE,
        "source_record_sha256": proof["reviewed_sha256"],
        "assertion_type": "mapping",
        "source_position": str(position),
        "assertion_sha256": payload_sha,
    }
    owner_path, owner_sha = "data/ingredients/mapped/Held.yaml", sha("unchanged owner")
    resolution = {
        "assertion_id": frozen_id,
        "assertion_sha256": payload_sha,
        "edge_id": old_edge["id"],
        "owner_record": owner_path,
        "owner_record_sha256": owner_sha,
    }
    kwargs = {"owners": {held["subject_id"]: owner_path}, "record_hashes": {owner_path: owner_sha}}
    return proof, [assertion], [edge], [resolution], kwargs


@pytest.mark.parametrize("move", [True, False])
def test_checkpoint_suffix_lineage_includes_moved_and_unmoved_rows(tmp_path, monkeypatch, move):
    proof, assertions, edges, resolutions, kwargs = held_fixture(tmp_path, monkeypatch, move=move)
    result = mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)
    item = result[resolutions[0]["assertion_id"]]
    assert item["baseline_position"] == 2
    assert item["current_position"] == (1 if move else 2)
    assert [r["sequence"] for r in item["receipts"]] == [2]
    assert item["edge_id"] == edges[0]["id"]
    assert "\\u007c" in edges[0]["assertion_json"]
    assert mcr.assertion_identity(
        mcr.SSSOM_SOURCE, "mapping", 2, "payload"
    ) == mcr.assertion_identity(mcr.SSSOM_SOURCE, "mapping", "2", "payload")


@pytest.mark.parametrize("operation", ["changed", "readded", "samepayload"])
def test_held_payload_cannot_be_changed_or_removed_and_readded(tmp_path, monkeypatch, operation):
    proof, assertions, edges, resolutions, kwargs = held_fixture(
        tmp_path, monkeypatch, operation=operation
    )
    with pytest.raises(ValueError, match="changed or removed"):
        mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)


@pytest.mark.parametrize(
    "kind",
    [
        "same-digest-later-checkpoint",
        "path",
        "hash",
        "owner",
        "assertion",
        "duplicate-assertion",
        "duplicate-edge",
        "edge-payload",
        "edge-id",
    ],
)
def test_frozen_checkpoint_and_current_identity_boundaries(tmp_path, monkeypatch, kind):
    proof, assertions, edges, resolutions, kwargs = held_fixture(tmp_path, monkeypatch, move=False)
    checkpoint = mcr.HOLD_CHECKPOINTS[resolutions[0]["assertion_id"]]
    if kind == "same-digest-later-checkpoint":
        assert proof["receipts"][0]["after_sha256"] == proof["receipts"][1]["after_sha256"]
        checkpoint["sequence"] = 2
    elif kind == "path":
        checkpoint["path"] = proof["receipt_paths"][1]
    elif kind == "hash":
        checkpoint["sha256"] = sha("wrong")
    elif kind == "owner":
        kwargs["record_hashes"][resolutions[0]["owner_record"]] = sha("changed owner")
    elif kind == "assertion":
        assertions[0]["source_record_sha256"] = sha("stale source")
    elif kind == "duplicate-assertion":
        assertions.append(copy.deepcopy(assertions[0]))
    elif kind == "duplicate-edge":
        edges.append(copy.deepcopy(edges[0]))
    elif kind == "edge-payload":
        edges[0]["assertion_json"] = packed(row("wrong"))
    else:
        edges[0]["id"] = "MIM.assertion:" + sha("wrong")
    with pytest.raises(ValueError):
        mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)


def test_checkpoint_requires_complete_prefix_and_no_caller_override(tmp_path, monkeypatch):
    proof, assertions, edges, resolutions, kwargs = held_fixture(tmp_path, monkeypatch)
    frozen = resolutions[0]["assertion_id"]
    mcr.HOLD_CHECKPOINTS[frozen]["sequence"] = 3
    with pytest.raises(ValueError, match="Missing frozen checkpoint"):
        mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)
    resolutions[0]["checkpoint"] = {"sequence": 1}
    with pytest.raises(ValueError, match="Missing frozen checkpoint"):
        mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)


def test_identical_payload_cannot_substitute_a_different_row_lineage(tmp_path, monkeypatch):
    proof, assertions, edges, resolutions, kwargs = held_fixture(tmp_path, monkeypatch)
    held = proof["states_after_sequence"][1][1]
    proof["states_after_sequence"][1][0] = copy.deepcopy(held)
    # A retained duplicate payload does not replace the specifically reviewed row.
    following = proof["receipts"][1]
    following["position_map"] = [1, None]
    following["changes"] = [change("removed", held, None, 2, None)]
    with pytest.raises(ValueError, match="changed or removed"):
        mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)


def test_populated_optional_mapping_edge_field_is_not_silently_ignored(tmp_path, monkeypatch):
    proof, assertions, edges, resolutions, kwargs = held_fixture(tmp_path, monkeypatch)
    edges[0]["publications"] = "doi:unreviewed"
    with pytest.raises(ValueError, match="populated mapping edge"):
        mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)


def test_assertion_formula_matches_native_inventory_with_unicode_and_pipes():
    from mediaingredientmech.validation.semantic_release import current_assertions

    mapping = dict(row(), other="α|β")
    native = current_assertions({}, [mapping], {}, sha("canonical"))[0]
    payload = sha(json.dumps(mapping, sort_keys=True, separators=(",", ":")))
    assert native["assertion_id"] == mcr.assertion_identity(mcr.SSSOM_SOURCE, "mapping", 1, payload)


def test_zero_receipts_emit_no_fabricated_hold_proof():
    assert mcr.hold_lineage({"receipts": []}, [], [], [], owners={}, record_hashes={}) == {}


@pytest.mark.parametrize("move", [True, False])
@pytest.mark.parametrize(
    "mode", ["restored", "changed", "noop", "other-owner", "before-checkpoint"]
)
def test_frozen_owner_byte_history_after_checkpoint(tmp_path, monkeypatch, move, mode):
    proof, assertions, edges, resolutions, kwargs = held_fixture(tmp_path, monkeypatch, move=move)
    resolution = resolutions[0]
    reviewed = resolution["owner_record_sha256"]
    altered = sha("intermediate owner bytes")
    held_owner = resolution["owner_record"]

    def owner_link(before, after, path=held_owner):
        return {"source_record": path, "before_yaml_sha256": before, "after_yaml_sha256": after}

    if mode == "before-checkpoint":
        # The checkpoint itself reviews the changed owner bytes. Only its suffix is restricted.
        name = proof["receipt_paths"][0]
        first = json.loads((tmp_path / name).read_bytes())
        first["records"] = [owner_link(altered, reviewed)]
        path = write(tmp_path, name, first)
        mcr.HOLD_CHECKPOINTS[resolution["assertion_id"]]["sha256"] = sha(path.read_bytes())
    else:
        if mode == "restored":
            links = [owner_link(reviewed, altered), owner_link(altered, reviewed)]
        elif mode == "changed":
            links = [owner_link(reviewed, altered)]
            kwargs["record_hashes"][held_owner] = altered
        elif mode == "noop":
            links = [owner_link(reviewed, reviewed)]
        else:
            links = [owner_link(reviewed, altered, "data/ingredients/mapped/Other.yaml")]
        rows = proof["state"]
        for sequence, link in enumerate(links, 3):
            item = receipt(rows, rows, range(1, len(rows) + 1), sequence=sequence, records=[link])
            write(tmp_path, f"{mcr.RECEIPTS_DIR}/link-{sequence}.json", item)

    # Rebuild the proof from the actual fixture files: no caller-supplied owner chain.
    proof = mcr.verify_mapping_chain(tmp_path)
    if mode in {"restored", "changed"}:
        with pytest.raises(ValueError, match="held owner changed after the checkpoint"):
            mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)
    else:
        result = mcr.hold_lineage(proof, assertions, edges, resolutions, **kwargs)
        assert result[resolution["assertion_id"]]["current_position"] == (1 if move else 2)
        assert result[resolution["assertion_id"]]["edge_id"] == edges[0]["id"]
