"""Compose three explicitly reviewed additive owner edits against frozen bytes.

Only synonyms, curation history and mapping evidence may be additive. Any removal
or different field edit fails. This produces isolated proposals and remaps case
backlinks; it never writes maintained records or marks review complete.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
PAIRS = (
    ("mohr-hexahydrate", "a-proposal-mohr-hexahydrate", "b-proposal-mohr"),
    ("ammonium-nickel-hexahydrate", "a-proposal-ammonium-nickel-hexahydrate", "b-proposal-nickel_double"),
    ("clarified-rumen-fluid", "a-proposal-clarified-rumen-fluid", "b-proposal-rumen"),
)


def additions(before, after):
    if any(item not in after for item in before):
        raise ValueError("Cannot compose a removal as an additive proposal")
    return [item for item in after if item not in before]


def compose(before, after_values):
    merged = deepcopy(before)
    for after in after_values:
        stripped = deepcopy(after)
        for key in ("synonyms", "curation_history"):
            for item in additions(before.get(key, []), after.get(key, [])):
                if item not in merged.setdefault(key, []):
                    merged[key].append(item)
            if key in before:
                stripped[key] = deepcopy(before[key])
            else:
                stripped.pop(key, None)
        new_evidence = after.get("ontology_mapping", {}).get("evidence", [])
        old_evidence = before.get("ontology_mapping", {}).get("evidence", [])
        for item in additions(old_evidence, new_evidence):
            if item not in merged["ontology_mapping"].setdefault("evidence", []):
                merged["ontology_mapping"]["evidence"].append(item)
        stripped["ontology_mapping"]["evidence"] = deepcopy(old_evidence)
        if stripped != before:
            raise ValueError("Non-additive field edit requires separate reconciliation")
    return merged


if __name__ == "__main__":
    proposal_path, decision_path = ROOT / "proposals.json", ROOT / "decisions.json"
    proposals, decisions = json.loads(proposal_path.read_text()), json.loads(decision_path.read_text())
    by_id = {p["proposal_id"]: p for p in proposals["proposals"]}
    audit_path = ROOT / "integration/shared-proposal-composition.json"
    if audit_path.exists():
        raise FileExistsError(audit_path)
    audit_path.parent.mkdir(exist_ok=True)
    (ROOT / "integration/after").mkdir(exist_ok=True)
    audit = {"created_at": datetime.now(timezone.utc).isoformat(), "author": "/root", "input_proposals_sha256": hashlib.sha256(proposal_path.read_bytes()).hexdigest(), "input_decisions_sha256": hashlib.sha256(decision_path.read_bytes()).hexdigest(), "changes": [], "independent_review": "pending"}
    replacements, new_proposals = {}, []
    for slug, left_id, right_id in PAIRS:
        pair = [by_id[left_id], by_id[right_id]]
        owner_path = pair[0]["owner_path"]
        before_bytes = Path(owner_path).read_bytes()
        before_sha = hashlib.sha256(before_bytes).hexdigest()
        if any(p["owner_path"] != owner_path or p["before_sha256"] != before_sha for p in pair):
            raise ValueError("Owner or baseline mismatch")
        after_values = []
        for p in pair:
            capture = p["after_capture"]
            b = (ROOT / capture["path"]).read_bytes()
            if hashlib.sha256(b).hexdigest() != capture["sha256"]:
                raise ValueError("Fragment after hash mismatch")
            after_values.append(yaml.safe_load(b))
        value = compose(yaml.safe_load(before_bytes), after_values)
        after_path = ROOT / "integration/after" / Path(owner_path).name
        after_path.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=100))
        new_id = f"w02-proposal-{slug}"
        merged = {
            "proposal_id": new_id,
            "case_ids": list(dict.fromkeys(cid for p in pair for cid in p["case_ids"])),
            "description": "Compose the source-backed alias, mapping-evidence and proposed-history additions from " + left_id + " and " + right_id + " against their shared original baseline. No original fields, synonyms or history are removed.",
            "evidence_ids": list(dict.fromkeys(eid for p in pair for eid in p["evidence_ids"])),
            "owner_path": owner_path,
            "kind": "edit_existing_owner",
            "before_sha256": before_sha,
            "after_capture": {"root": "artifact", "path": after_path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(after_path.read_bytes()).hexdigest()},
            "supersedes_fragment_proposals": pair,
            "publication_obligations": "No hold is removed. All original owner/source/rejected-label findings remain. Coordinator integration must withdraw inherited support, apply through guarded writers, synchronize maintained surfaces and re-review the complete publication payload. This source-case review does not approve roles, stocks or all existing aliases.",
            "within_shard_conflict_resolution": "Only additive changes composed; original author payloads preserved under a/ and b/. Independent review of these exact composed bytes remains required.",
        }
        new_proposals.append(merged)
        replacements[left_id] = replacements[right_id] = new_id
        audit["changes"].append({"proposal_id": new_id, "fragment_proposal_ids": [left_id, right_id], "owner_path": owner_path, "before_sha256": before_sha, "after_capture": merged["after_capture"]})
    proposals["proposals"] = [p for p in proposals["proposals"] if p["proposal_id"] not in replacements] + new_proposals
    for decision in decisions["decisions"]:
        decision["proposal_ids"] = list(dict.fromkeys(replacements.get(pid, pid) for pid in decision["proposal_ids"]))
    proposal_path.write_text(json.dumps(proposals, ensure_ascii=False, indent=2) + "\n")
    decision_path.write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n")
    audit["output_proposals_sha256"] = hashlib.sha256(proposal_path.read_bytes()).hexdigest()
    audit["output_decisions_sha256"] = hashlib.sha256(decision_path.read_bytes()).hexdigest()
    audit_path.write_text(json.dumps(audit, indent=2) + "\n")
    print({"proposals": len(proposals["proposals"]), "composed": len(new_proposals), "independent_review": "pending"})
