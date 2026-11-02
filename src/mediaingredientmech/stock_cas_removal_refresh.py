"""Verify the bounded #871/#268 source correction without renewing approval.

The policy manifest retains historical canonical-input owner pins. Thiamine's
pin crosses the preserved node-removal receipt and the new stock-CAS receipt;
the fourteen chemistry-only owners are verified separately and not restamped.
"""

from __future__ import annotations

import re
import subprocess
from copy import deepcopy
from datetime import date, datetime, timedelta
from pathlib import Path

from mediaingredientmech.ingredient_bundle_contract import (
    _base_table,
    content_sha256,
    read_json,
)
from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.validation.mapping_change_receipts import (
    HISTORICAL_CONTEXT,
    RECEIPTS_DIR,
    SSSOM_SOURCE,
    receipt_paths,
    record_supersession,
)

PACKET = "reports/hydrate_stock_chemistry_871_268_20261102/source-evidence.json"
PACKET_SHA256 = "44c88cc3ca03038e5e5c94b35c8d6dfd05412451b8d9c75d402512e526b4ef94"
STOCK = "data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml"
SUBJECT = "MIM:02_Thiamine_Pyrophosphate"
IDENTITY = "kgmicrobe.ingredient:0_2_thiamine_pyrophosphate"
CAS_TOKEN = "CAS:154-87-0"
HISTORICAL_OWNER = "7eece9fb547e213646a2313b9f9bb8f5988f0d13e08d53b2255a33b43f8a659f"
ACTUAL_PREIMAGE = "6d6db9a0040730973f390da1e492ee4e2afa672adc95e2e526d37f99def9bc5a"
BRIDGE = RECEIPTS_DIR + "/issue753-870-registry-and-node-corrections.json"
FORM_REVIEWS = tuple(
    "reports/sssom_completion_20260921/mapping_review/form_reviews/901-" + name + "-v1.json"
    for name in ("melezitose", "sodium-perchlorate")
)
VERIFIERS = tuple(
    "src/mediaingredientmech/" + name
    for name in (
        "stock_cas_removal_refresh.py",
        "ingredient_bundle_refresh.py",
        "ingredient_bundle_contract.py",
        "validation/mapping_change_receipts.py",
        "export/reviewed_sssom.py",
        "curie.py",
        "mapping_scope.py",
        "review_claims.py",
        "synonym_policy.py",
        "sssom_metadata.py",
    )
)
_CODE = Path(__file__).read_bytes()


def require(condition, message):
    if not condition:
        raise ValueError("Stock CAS removal: " + message)


def receipt_inventory(root):
    """Include ignored and nested receipt files, rather than trusting an allowlist."""
    paths = {p.relative_to(root).as_posix() for p in (root / RECEIPTS_DIR).rglob("*.json")}
    require(paths == set(receipt_paths(root)), "receipt inventory differs")
    return paths


def verify_source_transition(name, before, after, packet):
    """Compare the complete source shape with the immutable fifteen-owner matrix."""
    spec = packet["owners"][name]
    require(
        before.get("identifier") == spec["identifier"]
        and before.get("mapping_status") == spec["mapping_status"],
        "preimage identity/status differs: " + name,
    )
    old_history, history = before.get("curation_history"), after.get("curation_history")
    require(
        isinstance(old_history, list)
        and len(old_history) == spec["history_count"]
        and isinstance(history, list)
        and len(history) == len(old_history) + 1
        and history[:-1] == old_history,
        "expected one history append with exact prefix: " + name,
    )
    event = history[-1]
    require(
        isinstance(event, dict)
        and set(event)
        == {
            "timestamp",
            "curator",
            "action",
            "changes",
            "previous_status",
            "new_status",
            "llm_assisted",
            "llm_model",
        },
        "history event shape differs: " + name,
    )
    require(
        event["curator"] == packet["curator"]
        and event["action"] == packet["action"]
        and event["changes"] == spec["event_changes"]
        and event["previous_status"] == event["new_status"] == spec["mapping_status"]
        and event["llm_assisted"] is True
        and event["llm_model"] == packet["llm_model"],
        "history attribution differs: " + name,
    )
    require(isinstance(event["timestamp"], str), "history timestamp must be text")
    when = datetime.fromisoformat(event["timestamp"])
    require(
        when.utcoffset() == timedelta(0)
        and when >= datetime.fromisoformat(packet["evidence_not_before"]),
        "history predates evidence or is not UTC",
    )
    expected = deepcopy(before)
    for path in spec["delete"]:
        parts = path.split(".")
        parent = expected
        for key in parts[:-1]:
            require(isinstance(parent, dict) and key in parent, "missing deletion parent")
            parent = parent[key]
        require(isinstance(parent, dict) and parts[-1] in parent, "missing deletion field")
        del parent[parts[-1]]
    for path, value in spec["set"].items():
        parts = path.split(".")
        parent = expected
        for key in parts[:-1]:
            require(isinstance(parent, dict) and key in parent, "missing assignment parent")
            parent = parent[key]
        require(isinstance(parent, dict), "assignment parent is not a mapping")
        parent[parts[-1]] = deepcopy(value)
    expected["curation_history"].append(event)
    require(after == expected, "source changed outside reviewed matrix: " + name)
    return event


def expected_stock_source(record):
    """Native source vocabulary for this local registry row, without a KG suffix."""
    evidence = record["ontology_mapping"].get("evidence", [])
    sources = [
        f"MIM:{item['source'].strip()}" for item in evidence if item.get("source", "").strip()
    ]
    return "|".join(sources + ["MIM:curator=" + record["curation_history"][-1]["curator"]])


def verify_row_transition(before, current, receipt, event, source):
    """Only the exact stock CAS token and explicitly derived provenance may change."""
    headers = [
        [
            line
            for line in values[SSSOM_SOURCE].splitlines(keepends=True)
            if line.startswith(b"#")
            and not re.match(rb"# (mapping_date|mapping_set_version):", line)
        ]
        for values in (before, current)
    ]
    require(headers[0] == headers[1], "unrelated canonical header changed")
    _, old_columns, old_rows = _base_table(before[SSSOM_SOURCE])
    _, columns, rows = _base_table(current[SSSOM_SOURCE])
    require(
        old_columns == columns
        and len(old_rows) == len(rows)
        and receipt["position_map"] == list(range(1, len(rows) + 1))
        and receipt["changed_rows"] == 1
        and len(receipt["changes"]) == 1
        and receipt["added_rows"] == receipt["removed_rows"] == 0,
        "expected exactly one changed row with identity position map",
    )
    change = receipt["changes"][0]
    old, new = change["before"], change["after"]
    require(isinstance(old, dict) and isinstance(new, dict), "changed row endpoints absent")
    tokens = old["other"].split("|")
    require(tokens.count(CAS_TOKEN) == 1, "stock CAS token missing or duplicated")
    allowed = {"other", "source", "mapping_date", "validation_method"}
    require(
        old["subject_id"] == new["subject_id"] == SUBJECT
        and old["object_id"] == new["object_id"] == IDENTITY
        and old["predicate_id"] == new["predicate_id"] == "skos:exactMatch"
        and new["other"] == "|".join(token for token in tokens if token != CAS_TOKEN)
        and new["source"] == source
        and new["validation_method"] == ""
        and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", new["mapping_date"])
        and date.fromisoformat(new["mapping_date"])
        == datetime.fromisoformat(event["timestamp"]).date()
        and {k: v for k, v in old.items() if k not in allowed}
        == {k: v for k, v in new.items() if k not in allowed},
        "stock row exceeds exact CAS/provenance scope",
    )
    old_lines, new_lines = (
        [
            line
            for line in values[SSSOM_SOURCE].splitlines(keepends=True)
            if not line.startswith(b"#")
        ]
        for values in (before, current)
    )
    require(len(old_lines) == len(new_lines) == len(rows) + 1, "unexpected raw row layout")
    position = change["before_position"]
    require(position == change["after_position"], "changed row moved")
    require(
        all(
            a == b
            for i, (a, b) in enumerate(zip(old_lines, new_lines, strict=True))
            if i != position
        ),
        "unrelated canonical row bytes changed",
    )


def verify_stock_transition(prior, before, current, context, update, proof, historical, member):
    """Verify exact source shapes, immutable prefix and both historical-owner links."""
    root = context.root.resolve()
    require(
        update["issue"] == 268 and update["source_record"] == STOCK, "wrong issue or stock owner"
    )
    require(update["historical_owner_sha256"] == HISTORICAL_OWNER, "wrong historical stock pin")
    require(update["owner_before_sha256"] == ACTUAL_PREIMAGE, "wrong actual stock preimage")
    historical_paths = (
        subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", context.baseline, "--", RECEIPTS_DIR], cwd=root
        )
        .decode()
        .splitlines()
    )
    prefix = {p for p in historical_paths if p.endswith(".json")}
    require(
        prefix == set(proof["receipt_paths"][:-1])
        and receipt_inventory(root) == prefix | {proof["receipt_paths"][-1]}
        and proof["receipt_paths"][-2] == BRIDGE,
        "historical receipt inventory is not the exact expected prefix",
    )
    inputs: dict[str, str] = {}

    def capture(name):
        raw = member(root, name).read_bytes()
        digest = content_sha256(raw)
        require(
            name not in inputs or inputs[name] == digest, "conflicting proof input hash: " + name
        )
        inputs[name] = digest
        return raw

    for name in sorted(prefix | set(HISTORICAL_CONTEXT) | set(FORM_REVIEWS)):
        require(capture(name) == historical(name), "historical receipt/FORM bytes changed: " + name)
    packet_raw = capture(PACKET)
    require(content_sha256(packet_raw) == PACKET_SHA256, "reviewed source packet changed")
    packet = read_json(packet_raw)
    for name, info in packet["files"].items():
        raw = capture(name)
        require(
            content_sha256(raw) == info["sha256"] and len(raw) == info["bytes"],
            "source capture changed",
        )
    owners = set(packet["owners"])
    require(len(owners) == 15 and STOCK in owners, "source owner scope differs")
    require(
        not owners.intersection(prior["record_inputs"]), "changed owner belongs to companion cohort"
    )
    receipt = proof["receipts"][-1]
    records = {r["source_record"]: r for r in receipt["records"]}
    require(
        set(records) == owners and len(receipt["records"]) == 15,
        "expected exactly fifteen source owners",
    )
    for name in sorted(owners):
        spec = packet["owners"][name]
        old_raw, raw = historical(name), capture(name)
        record = records[name]
        require(
            content_sha256(old_raw) == spec["before_yaml_sha256"] == record["before_yaml_sha256"]
            and old_raw == capture(spec["preimage"])
            and content_sha256(raw) == record["after_yaml_sha256"]
            and record["shape"] == spec["shape"],
            "actual owner endpoints/shape differ: " + name,
        )
        old, new = _load_yaml(old_raw.decode()), _load_yaml(raw.decode())
        event = verify_source_transition(name, old, new, packet)
        if name == STOCK:
            stock_event, stock_source = event, expected_stock_source(new)
    historical_link = record_supersession(
        proof,
        owner=STOCK,
        reviewed_sha256=HISTORICAL_OWNER,
        current_sha256=update["owner_after_sha256"],
    )
    suffix = record_supersession(
        proof,
        owner=STOCK,
        reviewed_sha256=ACTUAL_PREIMAGE,
        current_sha256=update["owner_after_sha256"],
    )
    require(
        historical_link is not None
        and suffix is not None
        and [r["path"] for r in historical_link["receipts"]] == [BRIDGE, proof["receipt_paths"][-1]]
        and [r["path"] for r in suffix["receipts"]] == [proof["receipt_paths"][-1]],
        "stock owner chain is not the exact historical bridge plus current suffix",
    )
    verify_row_transition(before, current, receipt, stock_event, stock_source)
    memberships = []
    for values in (before, current):
        decisions = [
            d
            for d in read_json(values[prior["base_review"]])["decisions"]
            if d["owner_record"] in owners
        ]
        require(
            len(decisions) == 27 and all(d["disposition"] == "WITHHOLD" for d in decisions),
            "all 27 scoped mappings must retain WITHHOLD",
        )
        memberships.append({(d["owner_record"], d["source_position"]) for d in decisions})
    require(memberships[0] == memberships[1], "affected mapping membership changed")
    for name in VERIFIERS:
        capture(name)
    require(member(root, VERIFIERS[0]).read_bytes() == _CODE, "loaded stock verifier differs")
    return {
        "owners": sorted(owners),
        "historical_receipt_count": len(prefix),
        "current_receipt_count": len(proof["receipt_paths"]),
        "form_reviews_byte_preserved": list(FORM_REVIEWS),
        "stock_historical_supersession": historical_link,
        "stock_actual_preimage_supersession": suffix,
        "policy_owner_map_contract": "Historical canonical inputs; only thiamine advances across two proved links.",
        "scientific_approval_added": False,
        "input_sha256": inputs,
    }
