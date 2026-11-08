"""Add explicit cross-author case/proposal backlinks; no owner data is written."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LINKS = (
    ("CM_NAME:039dabd0250ba6972d70407f94c51986665db093b02cf2226cef7fae40a9d43b", "c-proposal-cerium-nitrate-hexahydrate"),
    ("CM_NAME:6d1c05b4d9907e412b50dfffc27eedff590089132cf332c147331bd7967a762d", "c-proposal-lanthanum-nitrate-hexahydrate"),
    ("KG_CASE:9a7243968b0f9f01eb918168d74dcb21b28c38bb6c46824355cbd7ef8514d370", "a-proposal-anhydrous-alum"),
)

if __name__ == "__main__":
    destination = ROOT / "integration/cross-author-backlinks.json"
    if destination.exists():
        raise FileExistsError(destination)
    dpath, ppath = ROOT / "decisions.json", ROOT / "proposals.json"
    decisions, proposals = json.loads(dpath.read_text()), json.loads(ppath.read_text())
    ds = {d["case_id"]: d for d in decisions["decisions"]}
    ps = {p["proposal_id"]: p for p in proposals["proposals"]}
    changes = []
    for cid, pid in LINKS:
        decision, proposal = ds[cid], ps[pid]
        before = json.loads(json.dumps(decision))
        owner = next(o for o in decision["owner_records"] if o["path"] == proposal["owner_path"])
        if owner["sha256"] != proposal["before_sha256"]:
            raise ValueError("Shared owner before hash mismatch")
        decision["proposal_ids"].append(pid)
        decision["no_change_reason"] = None
        decision["evidence_ids"] = list(dict.fromkeys(decision["evidence_ids"] + proposal["evidence_ids"]))
        proposal["case_ids"].append(cid)
        proposal["evidence_ids"] = list(dict.fromkeys(proposal["evidence_ids"] + before["evidence_ids"]))
        decision["integration_note"] = "Root linked the independently researched source case to the same-owner isolated proposal against the original matching baseline hash. These are shared proposal bytes, not an applied edit or release approval. The final link and exact payload require an independent reviewer who did not author the proposal."
        if pid == "c-proposal-cerium-nitrate-hexahydrate":
            decision["applicability"] = decision["applicability"].replace("coordinator must add the cross-subset backlink after combining outputs.", "the cross-subset backlink is now explicit in the worker's assembled outcomes.")
        if pid == "c-proposal-lanthanum-nitrate-hexahydrate":
            decision["missing_requirement"] = None
            decision["reasoning"] += " The shared C proposal resolves the same six-water source substance to exact MeSH concept M0313204, whose primary NLM record supplies CAS10277-43-7; its canonical label resolves in the current available local MeSH cache. It is no longer necessary to defer this proposal for an unidentified parent. Full changed-owner/consumer/publication review remains an integration obligation."
        changes.append({"case_id": cid, "proposal_id": pid, "before_decision": before, "after_decision_sha256": hashlib.sha256(json.dumps(decision, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()})
    dpath.write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n")
    ppath.write_text(json.dumps(proposals, ensure_ascii=False, indent=2) + "\n")
    destination.write_text(json.dumps({"author": "/root", "created_at": datetime.now(timezone.utc).isoformat(), "changes": changes, "independent_review": "pending"}, indent=2) + "\n")
    print({"backlinks_added": len(changes), "independent_review": "pending"})
