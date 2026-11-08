"""Read-only queue/owner dependency inventory; lexical hits are not identity decisions."""
import datetime
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path.cwd()
OUT = ROOT / "reports/all_unmatched_20261107/worker-07"
QUEUE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    proposals = json.loads((OUT / "proposals.json").read_text())["proposals"]
    decisions = json.loads((OUT / "decisions.json").read_text())["decisions"]
    owners = {o["path"] for d in decisions for o in d["owner_records"]}
    owners.update(p["owner_path"] for p in proposals if p["kind"] == "edit_existing_owner")
    labels, owner_records = {}, {}
    for owner in sorted(owners):
        record = yaml.safe_load((ROOT / owner).read_text())
        owner_records[owner] = {"sha256": sha(ROOT / owner), "proposal_ids": [p["proposal_id"] for p in proposals if p["owner_path"] == owner]}
        for label in [record.get("preferred_term")] + [s.get("synonym_text") for s in record.get("synonyms", [])]:
            if label:
                labels.setdefault(label, set()).add(owner)
    hits, shard_hashes = [], {}
    for path in sorted((QUEUE / "shards").glob("shard-*.json")):
        shard_hashes[str(path.relative_to(QUEUE))] = sha(path)
        if path.name == "shard-07.json":
            continue
        shard = json.loads(path.read_text())
        for case in shard["cases"]:
            entry = case.get("original_kg_entry", {})
            references = {o["path"] for o in entry.get("owners", [])}
            references.update(h["owner"] for h in entry.get("name_hits", []) if h.get("owner"))
            exact = references & owners
            lexical = (labels.get(case["source_label"], set()) | labels.get(case["raw_source_label"], set())) - exact
            if exact or lexical:
                hits.append({"worker_slot": shard["worker_slot"], "case_id": case["case_id"], "source_case_id": case["source_case_id"], "source_label": case["source_label"], "explicit_frozen_owner_references": sorted(exact), "exact_label_only_review_leads": sorted(lexical), "status": "Coordinator must compare other worker's final proposal and source applicability; no other-shard case reviewed or approved here."})
    result = {"generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "scope": "All frozen shard JSON files; direct owner references plus byte-exact labels on worker07 existing owners. Path.glob and explicit file reads include ignored inputs. No current other-worker proposals read.", "limitations": "Does not establish absence of other cross-shard dependencies: source-only cases can lack owner hints and chemically equivalent labels can differ. Lexical overlap is only a review lead, never identity equivalence.", "shard_hashes": shard_hashes, "worker07_owner_inputs": owner_records, "dependencies": hits, "integration_requirements": ["Keep each original baseline before-owner hash; do not adopt another worker's after bytes as a new baseline.", "Reconcile overlapping synonym rejection/addition, stock identity and curation history before guarded writes.", "Withdraw inherited content-bound support for every changed owner and review every new published mapping/alias row.", "Do not merge duplicate placeholder owners, including Titriplex1 and the NTA hydrate source1482/1930 records, merely from this inventory."]}
    (OUT / "cross-shard-dependencies.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"existing_owner_count": len(owners), "other_shard_dependency_cases": len(hits), "other_worker_slots": sorted({h["worker_slot"] for h in hits})}))


if __name__ == "__main__":
    main()
