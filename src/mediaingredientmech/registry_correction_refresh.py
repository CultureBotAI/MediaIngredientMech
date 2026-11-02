"""Bounded #753/#870 transition proof; this is not a new review or approval.

The historical policy owner map describes canonical inputs, not today's whole
corpus. Only Izalpinin's entry advances; six pointer-only owners are separately
proved against their reviewed preimages. Both earlier FORM reviews remain exact.
"""

from __future__ import annotations

import re
import subprocess
from copy import deepcopy
from datetime import date, datetime, timedelta

from mediaingredientmech.ingredient_bundle_contract import (
    _base_table,
    canonical_json,
    content_sha256,
    read_json,
)
from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.validation.mapping_change_receipts import (
    HISTORICAL_CONTEXT,
    RECEIPTS_DIR,
    SSSOM_SOURCE,
    receipt_paths,
)

CAS_OWNER = "data/ingredients/mapped/Izalpinin.yaml"
NODE_OWNERS = {
    "data/ingredients/mapped/Casamino_Acids.yaml": ("FOODON:03315719", "CHEBI:78020"),
    "data/ingredients/mapped/Casein.yaml": ("FOODON:03420180", "CHEBI:3448"),
    "data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml": (
        "kgmicrobe.ingredient:0_2_thiamine_pyrophosphate",
        "CHEBI:9532",
    ),
    "data/ingredients/mapped/Fish-sperm_Dna.yaml": (
        "kgmicrobe.ingredient:fish-sperm_dna",
        "CHEBI:16991",
    ),
    "data/ingredients/mapped/Bacto_Soytone.yaml": ("FOODON:03315720", "CHEBI:8150"),
    "data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml": (
        "kgmicrobe.ingredient:fish-sperm_dna",
        "CHEBI:16991",
    ),
}
FORM_REVIEWS = tuple(
    "reports/sssom_completion_20260921/mapping_review/form_reviews/901-" + n + "-v1.json"
    for n in ("melezitose", "sodium-perchlorate")
)
CAS_PACKET = "reports/izalpinin_registry_753_20261101/source-evidence.json"
NODE_PACKET = "reports/step7a_source_753_870_20261101/source-evidence.json"
PACKETS = {
    CAS_PACKET: "407a0dba0d455af7f01c98b9151c5f8f13527c494f160157c15eb3af032ea758",
    NODE_PACKET: "9d9dc2192eaef73d23ce686f10161468ca1055d781a27fbc197957d4e2917fb3",
}
CAS_SOURCE = "PubChem CID 5318691; MedChemExpress Izalpinin; MIM correction #753"
# Exact bounded note/history in the guarded writer: known LIPIDMAPS candidate,
# unresolved primary/source policy, WITHHOLD, and no CAS Registry certification.
# These digests do not authorize arbitrary newly appended evidence or assertions.
CAS_EVIDENCE_SHA = "85fc0a2150cbe70d9ae1d19ab942c0de970ace019164cc0f8aa8e9aa6a0ca74b"
CAS_CHANGE_SHA = "1000f80b94b817a152347f3873e8955ddfaf951c51ef9e131b24467b08b55a67"
VERIFIERS = tuple(
    "src/mediaingredientmech/" + n
    for n in (
        "registry_correction_refresh.py",
        "ingredient_bundle_refresh.py",
        "ingredient_bundle_contract.py",
        "validation/mapping_change_receipts.py",
        "export/reviewed_sssom.py",
        "curie.py",
        "mapping_scope.py",
        "review_claims.py",
        "synonym_policy.py",
    )
)


def require(condition, message):
    if not condition:
        raise ValueError("Registry correction: " + message)


def receipt_inventory(root):
    """Include ignored and nested files; native inventory must contain them all."""
    paths = {p.relative_to(root).as_posix() for p in (root / RECEIPTS_DIR).rglob("*.json")}
    require(paths == set(receipt_paths(root)), "receipt inventory differs")
    return paths


def _event(before, after, action, curator, not_before):
    old, new = before.get("curation_history"), after.get("curation_history")
    require(
        isinstance(old, list)
        and isinstance(new, list)
        and len(new) == len(old) + 1
        and new[:-1] == old,
        "expected one history append with preserved prefix",
    )
    event = new[-1]
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
        "history event fields differ",
    )
    require(
        event["action"] == action
        and event["curator"] == curator
        and event["previous_status"] == event["new_status"] == before["mapping_status"]
        and event["llm_assisted"] is True
        and event["llm_model"] == "gpt-6"
        and isinstance(event["changes"], str)
        and event["changes"],
        "history event contract differs",
    )
    require(isinstance(event["timestamp"], str), "history timestamp must be text")
    when = datetime.fromisoformat(event["timestamp"])
    require(
        when.utcoffset() == timedelta(0) and when >= datetime.fromisoformat(not_before),
        "history timestamp precedes evidence or is not UTC",
    )
    return event


def _node_transition(name, before, after, packet):
    identity, node = NODE_OWNERS[name]
    require(
        before.get("identifier") == identity and before.get("kg_microbe_node_id") == node,
        "node owner preimage identity differs",
    )
    event = _event(
        before, after, "REMOVED_STALE_KG_MICROBE_NODE_ID", "Codex", packet["evidence_not_before"]
    )
    expected_changes = (
        f"Removed stale kg_microbe_node_id {node} after the recorded "
        f"identity correction to {identity} (#870). Preserved primary "
        "identity, ontology mapping, chemistry, synonyms, roles, counts, status "
        "and existing tombstone metadata. Source-only correction: the fixed "
        "unified snapshot still contains the documented 21 stale cells in 15 "
        "rows; #870 remains open. No mapping, role or release approval. "
        f"Decision: {packet['decision_url']}; evidence: {NODE_PACKET} sha256={PACKETS[NODE_PACKET]}."
    )
    require(event["changes"] == expected_changes, "node history claim differs")
    restored = deepcopy(after)
    require("kg_microbe_node_id" not in restored, "stale node was not removed")
    restored["kg_microbe_node_id"] = node
    restored["curation_history"].pop()
    require(restored == before, "node cleanup changed another source field")


def _cas_transition(before, after, packet):
    require(
        before.get("identifier") == "cas:480-14-4"
        and before["ontology_mapping"]["ontology_id"] == "cas:480-14-4"
        and before["chemical_properties"]["cas_rn"] == "480-14-4"
        and after.get("identifier") == "cas:480-14-8"
        and after["ontology_mapping"]["ontology_id"] == "cas:480-14-8"
        and after["chemical_properties"]["cas_rn"] == "480-14-8",
        "CAS owner identities differ",
    )
    event = _event(
        before, after, "CORRECTED_EXISTING_CAS_VALUE", "claude", packet["evidence_not_before"]
    )
    require(
        content_sha256(canonical_json(event["changes"])) == CAS_CHANGE_SHA,
        "CAS history claim differs",
    )
    old_evidence = before["ontology_mapping"]["evidence"]
    evidence = after["ontology_mapping"]["evidence"]
    require(
        isinstance(evidence, list)
        and len(evidence) == len(old_evidence) + 1
        and evidence[:-1] == old_evidence
        and content_sha256(canonical_json(evidence[-1])) == CAS_EVIDENCE_SHA,
        "CAS evidence append differs",
    )
    require(
        after["chemical_properties"]["data_source"] == CAS_SOURCE
        and after["chemical_properties"]["retrieval_date"] == event["timestamp"],
        "CAS active provenance differs",
    )
    restored = deepcopy(after)
    restored["identifier"] = before["identifier"]
    restored["ontology_mapping"]["ontology_id"] = before["ontology_mapping"]["ontology_id"]
    restored["ontology_mapping"]["evidence"].pop()
    restored["curation_history"].pop()
    for field in ("cas_rn", "data_source", "retrieval_date"):
        restored["chemical_properties"][field] = before["chemical_properties"][field]
    require(restored == before, "CAS correction changed another source field")
    # The native generator joins evidence sources and the last curator in this
    # order. Its KG source lookup is CHEBI-only, so this CAS row has no KG suffix.
    source = "|".join(
        [f"MIM:{item['source'].strip()}" for item in evidence if item.get("source", "").strip()]
        + ["MIM:curator=" + event["curator"]]
    )
    return event, source


def _row_transition(before, current, receipt, event, expected_source):
    headers = [
        [
            line
            for line in values[SSSOM_SOURCE].splitlines(keepends=True)
            if line.startswith(b"#")
            and not re.match(rb"# (mapping_date|mapping_set_version):", line)
        ]
        for values in (before, current)
    ]
    require(headers[0] == headers[1], "unrelated canonical header bytes changed")
    _, old_columns, old_rows = _base_table(before[SSSOM_SOURCE])
    _, columns, rows = _base_table(current[SSSOM_SOURCE])
    require(
        old_columns == columns
        and len(old_rows) == len(rows)
        and receipt["position_map"] == list(range(1, len(rows) + 1))
        and receipt["changed_rows"] == 1
        and receipt["added_rows"] == receipt["removed_rows"] == 0,
        "expected one changed row and identity position map",
    )
    change = receipt["changes"][0]
    old, new = change["before"], change["after"]
    allowed = {"object_id", "other", "source", "mapping_date", "validation_method"}
    require(
        old["subject_id"] == new["subject_id"] == "MIM:Izalpinin"
        and old["object_id"] == "cas:480-14-4"
        and new["object_id"] == "cas:480-14-8"
        and old["other"] == "CAS:480-14-4"
        and new["other"] == "CAS:480-14-8"
        and new["validation_method"] == ""
        and new["source"] == expected_source
        and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", new["mapping_date"])
        and date.fromisoformat(new["mapping_date"])
        == datetime.fromisoformat(event["timestamp"]).date()
        and {k: v for k, v in old.items() if k not in allowed}
        == {k: v for k, v in new.items() if k not in allowed},
        "CAS row exceeds the reviewed field allowlist",
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
    changed = change["before_position"]
    require(
        all(
            a == b
            for i, (a, b) in enumerate(zip(old_lines, new_lines, strict=True))
            if i != changed
        ),
        "unrelated canonical row bytes changed",
    )


def verify_registry_transition(prior, before, current, context, update, proof, historical, member):
    """Replay the exact reviewed seven-owner suffix, never a general batch escape."""
    root = context.root.resolve()
    require(
        update["issue"] == 753 and update["source_record"] == CAS_OWNER,
        "wrong registry update issue or owner",
    )
    owners = {CAS_OWNER, *NODE_OWNERS}
    require(not owners.intersection(prior["record_inputs"]), "changed owner belongs to cohort")
    receipt = proof["receipts"][-1]
    records = {r["source_record"]: r for r in receipt["records"]}
    require(
        set(records) == owners and len(receipt["records"]) == len(owners),
        "expected exactly the seven reviewed owners",
    )
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
        and receipt_inventory(root) == prefix | {proof["receipt_paths"][-1]},
        "historical receipt inventory is not the exact current prefix",
    )
    inputs = {}

    def capture(name):
        raw = member(root, name).read_bytes()
        inputs[name] = content_sha256(raw)
        return raw

    for name in sorted(prefix | set(HISTORICAL_CONTEXT) | set(FORM_REVIEWS)):
        require(capture(name) == historical(name), "historical receipt/FORM bytes changed: " + name)
    packets = {}
    for name, expected in PACKETS.items():
        raw = capture(name)
        require(content_sha256(raw) == expected, "reviewed source packet changed")
        packet = packets[name] = read_json(raw)
        for path, info in packet["files"].items():
            raw = capture(path)
            require(
                content_sha256(raw) == info["sha256"] and len(raw) == info["bytes"],
                "reviewed source capture changed",
            )
    node_packet, cas_packet = packets[NODE_PACKET], packets[CAS_PACKET]
    for name in sorted(owners):
        old_raw, raw = historical(name), capture(name)
        record = records[name]
        expected = (
            cas_packet["owner_before_sha256"]
            if name == CAS_OWNER
            else node_packet["owners"][name]["sha256"]
        )
        require(
            content_sha256(old_raw) == expected == record["before_yaml_sha256"]
            and content_sha256(raw) == record["after_yaml_sha256"],
            "actual owner endpoints differ: " + name,
        )
        # Reuse the native unique-key parser: duplicate fields must not disappear
        # while comparing the complete source payloads.
        old, new = _load_yaml(old_raw.decode()), _load_yaml(raw.decode())
        shape = "registry_value_correction" if name == CAS_OWNER else "stale_node_pointer_removal"
        require(record["shape"] == shape, "native owner transition type differs")
        if name == CAS_OWNER:
            event, expected_source = _cas_transition(old, new, cas_packet)
        else:
            _node_transition(name, old, new, node_packet)
    _row_transition(before, current, receipt, event, expected_source)
    owned_decisions = []
    for values in (before, current):
        base = read_json(values[prior["base_review"]])
        decisions = [d for d in base["decisions"] if d["owner_record"] in owners]
        require(
            sum(d["owner_record"] == CAS_OWNER for d in decisions) == 1
            and all(d["disposition"] == "WITHHOLD" for d in decisions),
            "registry correction must retain all affected mapping holds",
        )
        owned_decisions.append({(d["owner_record"], d["source_position"]) for d in decisions})
    require(owned_decisions[0] == owned_decisions[1], "affected review membership changed")
    for name in VERIFIERS:
        capture(name)
    return {
        "owners": sorted(owners),
        "historical_receipt_count": len(prefix),
        "current_receipt_count": len(proof["receipt_paths"]),
        "form_reviews_byte_preserved": list(FORM_REVIEWS),
        "policy_owner_map_contract": "Historical canonical inputs; only Izalpinin advances.",
        "scientific_approval_added": False,
        "input_sha256": inputs,
    }
