"""Replay approval-free mapping receipts and prove exact-byte withdrawal.

These proofs are computed from current bound inputs. They are not approvals and
must never be accepted from a report in place of independent recomputation.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path, PurePosixPath

RECEIPTS_DIR = "reports/sssom_completion_20260921/mapping_changes"
SSSOM_SOURCE = "mappings/ingredient_mappings.sssom.tsv"
BASELINE = "reports/sssom_completion_20260921/baseline-mapping-review.json"
TRAIT_REFRESH = "reports/sssom_completion_20260921/trait-synonym-refresh.json"
PARENT_REFRESH = "reports/sssom_completion_20260921/parent-name-refresh.json"
HISTORICAL_CONTEXT = (BASELINE, TRAIT_REFRESH, PARENT_REFRESH)

# The resolution was reviewed at receipt 11, not the original negative row 437.
# Receipt 12 has the same after digest: digest equality cannot select a checkpoint.
HOLD_CHECKPOINTS = {
    "MIM.review:e619555259b8de4a7aed8090e7ac32562f3df3a23c34371cd9cf28647f6ef26f": {
        "sequence": 11,
        "path": RECEIPTS_DIR + "/review-record-issues-20261003.json",
        "sha256": "9b578f6c25c1ebabb8e58c5a59d6188b7c1f2dd3c8c70ed021b35144c6da1226",
        "after_sha256": "2eae181f31d6433c20ffdb9dc2f8c8d7ad0a17a46a3189dea8c307fbc1c7b40e",
        "position": 431,
    }
}
MAPPING_EDGE_KEYS = frozenset(
    {
        "subject",
        "predicate",
        "object",
        "relation",
        "primary_knowledge_source",
        "provided_by",
        "assertion_type",
        "source_record",
        "source_position",
        "confidence",
        "assertion_json",
    }
)


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _digest(content):
    return hashlib.sha256(content).hexdigest()


def _sha(value):
    _require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "Invalid SHA256")
    return value


def _count(value):
    _require(type(value) is int and value >= 0, "Receipt count must be a nonnegative integer")
    return value


def _position(value, count):
    _require(type(value) is int and 1 <= value <= count, "Receipt position outside 1-based range")
    return value


def _relative(name):
    _require(isinstance(name, str) and bool(name), "Missing repository-relative path")
    path = PurePosixPath(name)
    _require(
        not path.is_absolute() and ".." not in path.parts and path.as_posix() == name,
        "Noncanonical repository-relative path",
    )
    return name


def _path(root, name):
    path = root / _relative(name)
    _require(not any(p.is_symlink() for p in (path, *path.parents)), "Aliased receipt input")
    _require(path.resolve().is_relative_to(root), "Receipt input outside repository")
    return path


def _read(root, name):
    return _path(root, name).read_bytes()


def _json(content):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            _require(key not in result, "Duplicate JSON key in receipt input")
            result[key] = value
        return result

    value = json.loads(content, object_pairs_hook=unique)
    _require(isinstance(value, dict), "Receipt input must be an object")
    return value


def _row(value):
    _require(
        isinstance(value, dict)
        and bool(value)
        and all(isinstance(k, str) and isinstance(v, str) for k, v in value.items()),
        "Mapping row must contain string fields",
    )


def _validate_receipt(receipt, *, complete):
    _require(isinstance(receipt, dict), "Receipt must be an object")
    _require(
        type(receipt.get("schema_version")) is int and receipt["schema_version"] == 1,
        "Unsupported mapping receipt schema",
    )
    _require(isinstance(receipt.get("batch"), str) and receipt["batch"], "Missing receipt batch")
    _require(
        isinstance(receipt.get("approval"), str) and receipt["approval"].split(":")[0] == "NONE",
        "Receipt is not an approval-free link",
    )
    _position(receipt.get("sequence"), 2**63 - 1)
    _sha(receipt.get("before_sha256"))
    _sha(receipt.get("after_sha256"))
    before_count = _count(receipt.get("before_row_count"))
    after_count = _count(receipt.get("after_row_count"))
    positions = receipt.get("position_map")
    _require(
        isinstance(positions, list) and len(positions) == before_count,
        "Receipt position map is incomplete",
    )
    destinations = set()
    for target in positions:
        if target is not None:
            _position(target, after_count)
            _require(target not in destinations, "Receipt position map is not injective")
            destinations.add(target)
    changes = receipt.get("changes")
    _require(isinstance(changes, list), "Receipt changes must be a list")
    touched, removed, added = set(), set(), set()
    counts = Counter()
    for change in changes:
        _require(isinstance(change, dict), "Receipt change must be an object")
        kind = change.get("kind")
        _require(kind in {"changed", "removed", "added"}, "Receipt has an unknown change kind")
        counts[kind] += 1
        if kind in {"changed", "removed"}:
            before = _position(change.get("before_position"), before_count)
            _require(before not in touched, "Duplicate original position in receipt changes")
            touched.add(before)
            _row(change.get("before"))
            target = positions[before - 1]
            if kind == "removed":
                _require(target is None, "Receipt removes a row its position map keeps")
                _require(
                    change.get("after_position") is None and change.get("after") is None,
                    "Removed row has an after payload or position",
                )
                removed.add(before)
                continue
            after = _position(change.get("after_position"), after_count)
            _require(target == after, "Receipt moves a changed row inconsistently")
        else:
            _require(
                change.get("before_position") is None and change.get("before") is None,
                "Added row has a before payload or position",
            )
            after = _position(change.get("after_position"), after_count)
            _require(
                after not in destinations and after not in added,
                "Receipt adds a row onto an occupied position",
            )
            added.add(after)
        _row(change.get("after"))
    _require(
        removed == {i for i, p in enumerate(positions, 1) if p is None},
        "Position-map removals differ from declared removed operations",
    )
    _require(
        destinations | added == set(range(1, after_count + 1)),
        "Receipt leaves a hole in the row order",
    )
    for kind in ("changed", "added", "removed"):
        key = kind + "_rows"
        if complete or key in receipt:
            _require(_count(receipt.get(key)) == counts[kind], "Receipt operation count differs")
    records = receipt.get("records", [] if not complete else None)
    _require(isinstance(records, list), "Receipt records must be a list")
    owners = set()
    for record in records:
        _require(isinstance(record, dict), "Receipt owner must be an object")
        owner = _relative(record.get("source_record"))
        _require(
            owner.startswith("data/ingredients/") and owner.endswith(".yaml"),
            "Receipt owner must be an ingredient YAML",
        )
        _require(owner not in owners, "Duplicate owner within one receipt")
        owners.add(owner)
        _require("before_yaml_sha256" in record, "Missing reviewed owner hash")
        if record.get("before_yaml_sha256") is not None:
            _sha(record["before_yaml_sha256"])
        else:
            _require(record.get("shape") == "new_record", "Missing reviewed owner hash")
        _sha(record.get("after_yaml_sha256"))


def _ordered(receipts, *, complete=False):
    _require(isinstance(receipts, list), "Receipts must be a list")
    for receipt in receipts:
        _validate_receipt(receipt, complete=complete)
    ordered = sorted(receipts, key=lambda r: r["sequence"])
    _require(
        [r["sequence"] for r in ordered] == list(range(1, len(ordered) + 1)),
        "Mapping-change receipts must be numbered 1..n without gaps",
    )
    for before, after in zip(ordered, ordered[1:], strict=False):
        _require(
            before["after_sha256"] == after["before_sha256"],
            "Receipt does not chain from the previous link",
        )
        _require(
            before["after_row_count"] == after["before_row_count"],
            "Receipt does not chain row counts",
        )
    return ordered


def _names(root):
    folder = _path(root, RECEIPTS_DIR)
    if not folder.exists():
        return []
    _require(folder.is_dir(), "Receipt inventory is not a directory")
    paths = sorted(folder.glob("*.json"))
    _require(
        set(paths) == set(folder.rglob("*.json")),
        "Nested receipt input is outside native inventory",
    )
    return [p.relative_to(root).as_posix() for p in paths]


def _capture(root):
    names = _names(root)
    contents = {name: _read(root, name) for name in names}
    documents = {name: _json(raw) for name, raw in contents.items()}
    _ordered(list(documents.values()), complete=True)
    ordered_paths = sorted(names, key=lambda name: documents[name]["sequence"])
    return ordered_paths, [documents[name] for name in ordered_paths], contents


def _unchanged(root, contents, receipt_names):
    _require(
        _names(root) == sorted(receipt_names), "Receipt input inventory changed during verification"
    )
    _require(
        all(_read(root, name) == raw for name, raw in contents.items()),
        "Receipt input bytes changed during verification",
    )


def load_receipts(root: Path) -> list[dict]:
    """Read strict documents in sequence order, without annotating archived JSON."""
    root = root.resolve()
    paths, receipts, contents = _capture(root)
    _owner_chains(receipts, paths, {p: _digest(b) for p, b in contents.items()})
    _unchanged(root, contents, paths)
    return receipts


def receipt_paths(root: Path) -> list[str]:
    """Return the exact native inventory in validated sequence order."""
    root = root.resolve()
    paths, receipts, contents = _capture(root)
    _owner_chains(receipts, paths, {p: _digest(b) for p, b in contents.items()})
    _unchanged(root, contents, paths)
    return paths


def _replay(receipts, start, end, baseline_rows, refreshed_rows):
    _sha(start)
    _sha(end)
    _require(
        isinstance(baseline_rows, list) and isinstance(refreshed_rows, dict),
        "Invalid baseline rows",
    )
    for row in baseline_rows:
        _row(row)
    for position, row in refreshed_rows.items():
        _position(position, len(baseline_rows))
        _row(row)
    state = [dict(refreshed_rows.get(i, row)) for i, row in enumerate(baseline_rows, 1)]
    forward, last, link = list(range(1, len(state) + 1)), {}, start
    states = {0: list(state)}
    for receipt in receipts:
        _require(receipt["before_sha256"] == link, "Receipt does not chain from the previous link")
        _require(receipt["before_row_count"] == len(state), "Receipt position map is incomplete")
        positions = receipt["position_map"]
        new_state = [None] * receipt["after_row_count"]
        for position, row in enumerate(state, 1):
            target = positions[position - 1]
            if target is not None:
                new_state[target - 1] = row
        moved = {
            positions[i - 1]: change for i, change in last.items() if positions[i - 1] is not None
        }
        for change in receipt["changes"]:
            if change["kind"] in {"changed", "removed"}:
                _require(
                    state[change["before_position"] - 1] == change["before"],
                    "Receipt does not chain from the reviewed row",
                )
            if change["kind"] != "removed":
                target = change["after_position"]
                new_state[target - 1] = dict(change["after"])
                moved[target] = dict(change, receipt=receipt["batch"])
        _require(
            all(row is not None for row in new_state), "Receipt leaves a hole in the row order"
        )
        forward = [positions[p - 1] if p is not None else None for p in forward]
        state, last, link = new_state, moved, receipt["after_sha256"]
        states[receipt["sequence"]] = list(state)
    _require(link == end, "The last chain link does not produce the reviewed source")
    return forward, last, state, states


def walk_mapping_changes(receipts, *, start_sha256, reviewed_sha256, baseline_rows, refreshed_rows):
    """Strict row replay retaining the assembler's established three-item result."""
    return _replay(
        _ordered(receipts), start_sha256, reviewed_sha256, baseline_rows, refreshed_rows
    )[:3]


def _owner_chains(receipts, paths, hashes):
    chains = {}
    for receipt, path in zip(receipts, paths, strict=True):
        for entry in receipt.get("records", []):
            links = chains.setdefault(entry["source_record"], [])
            before, after = entry["before_yaml_sha256"], entry["after_yaml_sha256"]
            _require(
                not links or links[-1]["after_sha256"] == before, "Owner receipt chain has a gap"
            )
            links.append(
                {
                    "sequence": receipt["sequence"],
                    "receipt_path": path,
                    "receipt_sha256": hashes[path],
                    "before_sha256": before,
                    "after_sha256": after,
                }
            )
    return chains


def _synonym_prefix(baseline, refreshes):
    _require(
        type(baseline.get("schema_version")) is int and baseline["schema_version"] == 1,
        "Unsupported baseline schema",
    )
    _require(isinstance(baseline.get("rows"), list), "Invalid baseline rows")
    for row in baseline["rows"]:
        _row(row)
    state = [dict(row) for row in baseline["rows"]]
    link = _sha(baseline.get("source_sha256"))
    refreshed = {}
    for refresh in refreshes:
        _require(
            type(refresh.get("schema_version")) is int and refresh["schema_version"] == 1,
            "Unsupported synonym refresh schema",
        )
        _require(_sha(refresh.get("before_sha256")) == link, "Synonym refresh digest chain differs")
        link = _sha(refresh.get("after_sha256"))
        _require(
            _count(refresh.get("row_count")) == len(state), "Synonym refresh row count differs"
        )
        changes = refresh.get("changes")
        _require(
            isinstance(changes, list) and _count(refresh.get("changed_rows")) == len(changes),
            "Synonym refresh change count differs",
        )
        seen = set()
        for change in changes:
            _require(isinstance(change, dict), "Synonym refresh change must be an object")
            position = _position(change.get("source_position"), len(state))
            _require(position not in seen, "Duplicate synonym refresh position")
            seen.add(position)
            _row(change.get("before"))
            _row(change.get("after"))
            _require(
                state[position - 1] == change["before"], "Synonym refresh before payload differs"
            )
            _require(
                {k: v for k, v in change["before"].items() if k != "other"}
                == {k: v for k, v in change["after"].items() if k != "other"},
                "Synonym refresh changed non-synonym payload",
            )
            state[position - 1] = dict(change["after"])
            refreshed[position] = state[position - 1]
    return link, refreshed


def verify_mapping_chain(root: Path) -> dict:
    """Capture and replay once per consumer invocation; return internal proof only."""
    from mediaingredientmech.export.reviewed_sssom import read_sssom

    root = root.resolve()
    paths, receipts, contents = _capture(root)
    historical = {name: _path(root, name).exists() for name in HISTORICAL_CONTEXT}
    contents[SSSOM_SOURCE] = _read(root, SSSOM_SOURCE)
    _, _, current = read_sssom(root / SSSOM_SOURCE, content=contents[SSSOM_SOURCE])
    reviewed_sha = _digest(contents[SSSOM_SOURCE])
    if receipts or any(historical.values()):
        _require(all(historical.values()), "Missing or partial historical mapping context")
        for name in HISTORICAL_CONTEXT:
            contents[name] = _read(root, name)
        baseline = _json(contents[BASELINE])
        start, refreshed = _synonym_prefix(
            baseline, [_json(contents[p]) for p in HISTORICAL_CONTEXT[1:]]
        )
        baseline_rows = baseline["rows"]
    else:
        start, refreshed, baseline_rows = reviewed_sha, {}, current
    forward, last, state, states = _replay(receipts, start, reviewed_sha, baseline_rows, refreshed)
    _require(state == current, "Current source rows differ from the reviewed chain's replay")
    hashes = {name: _digest(raw) for name, raw in contents.items()}
    chains = _owner_chains(receipts, paths, hashes)
    _require(
        historical == {name: _path(root, name).exists() for name in HISTORICAL_CONTEXT},
        "Historical mapping context membership changed during verification",
    )
    _unchanged(root, contents, paths)
    return {
        "schema_version": 1,
        "receipts": receipts,
        "receipt_paths": paths,
        "receipt_inputs": {name: hashes[name] for name in paths},
        "input_hashes": hashes,
        "start_sha256": start,
        "reviewed_sha256": reviewed_sha,
        "baseline_rows": baseline_rows,
        "refreshed_rows": refreshed,
        "forward": forward,
        "last": last,
        "state": state,
        "states_after_sequence": states,
        "owner_chains": chains,
    }


def record_supersession(proof: dict, *, owner: str, reviewed_sha256: str, current_sha256: str):
    """Prove withdrawal from this exact archived pin, never approval of new bytes."""
    _relative(owner)
    if not reviewed_sha256 or not current_sha256:
        return None
    _sha(reviewed_sha256)
    _sha(current_sha256)
    if reviewed_sha256 == current_sha256:
        return None
    links = proof["owner_chains"].get(owner, [])
    if not links or links[-1]["after_sha256"] != current_sha256:
        return None
    for index, link in enumerate(links):
        if link["before_sha256"] != reviewed_sha256:
            continue
        running = reviewed_sha256
        selected = links[index:]
        for item in selected:
            _require(item["before_sha256"] == running, "Owner receipt chain has a gap")
            running = item["after_sha256"]
        return {
            "owner_record": owner,
            "reviewed_sha256": reviewed_sha256,
            "current_sha256": current_sha256,
            "receipts": [
                {
                    "sequence": x["sequence"],
                    "path": x["receipt_path"],
                    "sha256": x["receipt_sha256"],
                    "before_sha256": x["before_sha256"],
                    "after_sha256": x["after_sha256"],
                }
                for x in selected
            ],
            "reason": "Exact owner-byte chain supersedes this archived pin; no approval is renewed",
        }
    return None


def assertion_identity(source, kind, position, payload_sha):
    """Preserve the semantic gate's string-position identity formula exactly."""
    content = json.dumps([source, kind, str(position), payload_sha], separators=(",", ":"))
    return "MIM.review:" + _digest(content.encode())


def _edge_id_at(edge, position):
    from mediaingredientmech.export.kgx import packed

    _require(MAPPING_EDGE_KEYS <= edge.keys(), "Incomplete mapping edge")
    _require(
        all(value == "" for key, value in edge.items() if key not in MAPPING_EDGE_KEYS | {"id"}),
        "Unexpected populated mapping edge attributes",
    )
    row = {key: edge[key] for key in MAPPING_EDGE_KEYS}
    row["source_position"] = str(position)
    return "MIM.assertion:" + _digest(packed(row).encode())


def hold_lineage(proof, assertions, edges, resolutions, *, owners, record_hashes):
    """Trace the frozen checkpoint's actual row, including an unmoved endpoint."""
    from mediaingredientmech.export.kgx import packed

    if not proof["receipts"]:
        return {}
    lineage = {}
    for resolution in resolutions:
        frozen_id = resolution.get("assertion_id")
        _require(frozen_id not in lineage, "Duplicate frozen hold resolution")
        checkpoint = HOLD_CHECKPOINTS.get(frozen_id)
        _require(checkpoint is not None, "No maintained receipt checkpoint for hold resolution")
        sequence = checkpoint["sequence"]
        _require(len(proof["receipts"]) >= sequence, "Missing frozen checkpoint receipt prefix")
        receipt = proof["receipts"][sequence - 1]
        _require(
            receipt["sequence"] == sequence
            and proof["receipt_paths"][sequence - 1] == checkpoint["path"]
            and proof["receipt_inputs"].get(checkpoint["path"]) == checkpoint["sha256"]
            and receipt["after_sha256"] == checkpoint["after_sha256"],
            "Frozen receipt checkpoint differs",
        )
        owner = resolution["owner_record"]
        _require(
            not any(
                link["sequence"] > sequence and link["before_sha256"] != link["after_sha256"]
                for link in proof["owner_chains"].get(owner, [])
            ),
            "Resolved held owner changed after the checkpoint",
        )
        origin = _position(checkpoint["position"], len(proof["states_after_sequence"][sequence]))
        row = proof["states_after_sequence"][sequence][origin - 1]
        payload_sha = _digest(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())
        _require(
            payload_sha == resolution["assertion_sha256"]
            and assertion_identity(SSSOM_SOURCE, "mapping", origin, payload_sha) == frozen_id,
            "Frozen checkpoint assertion differs",
        )
        position, suffix = origin, []
        for index in range(sequence, len(proof["receipts"])):
            following = proof["receipts"][index]
            _require(
                not any(c.get("before_position") == position for c in following["changes"]),
                "Receipt changed or removed the resolved held row",
            )
            target = following["position_map"][position - 1]
            _require(target is not None, "Receipt removed the resolved held row")
            path = proof["receipt_paths"][index]
            suffix.append(
                {
                    "sequence": following["sequence"],
                    "path": path,
                    "sha256": proof["receipt_inputs"][path],
                    "before_position": position,
                    "after_position": target,
                }
            )
            position = target
        _require(proof["state"][position - 1] == row, "Resolved held row payload changed")
        matches = [
            a
            for a in assertions
            if a.get("source_record") == SSSOM_SOURCE
            and a.get("assertion_type") == "mapping"
            and a.get("source_position") == str(position)
        ]
        _require(len(matches) == 1, "Missing or duplicate current held assertion")
        assertion = matches[0]
        _require(
            assertion.get("assertion_id")
            == assertion_identity(SSSOM_SOURCE, "mapping", position, payload_sha)
            and assertion.get("assertion_sha256") == payload_sha
            and assertion.get("source_record_sha256") == proof["reviewed_sha256"],
            "Current held assertion identity differs",
        )
        matches = [
            e
            for e in edges
            if e.get("source_record") == SSSOM_SOURCE
            and e.get("assertion_type") == "mapping"
            and e.get("source_position") == str(position)
        ]
        _require(len(matches) == 1, "Missing or duplicate current held edge")
        edge = matches[0]
        _require(
            edge.get("assertion_json") == packed(row)
            and _edge_id_at(edge, origin) == resolution["edge_id"]
            and _edge_id_at(edge, position) == edge.get("id"),
            "Resolved held edge differs",
        )
        _require(
            owners.get(row["subject_id"]) == owner
            and record_hashes.get(owner) == resolution["owner_record_sha256"],
            "Resolved held owner bytes changed",
        )
        lineage[frozen_id] = {
            "assertion_id": assertion["assertion_id"],
            "edge_id": edge["id"],
            "baseline_position": origin,
            "current_position": position,
            "checkpoint": dict(checkpoint),
            "receipts": suffix,
        }
    return lineage
