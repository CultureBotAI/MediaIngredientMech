"""Report immutable-queue owner references and exact label overlaps only.

This never reviews another worker's cases or infers chemical equivalence from a
label. The coordinator must reconcile each reported possible dependency.
"""
import hashlib
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parent
QUEUE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5")


def owner_mentions(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in ("owner_record", "record_path", "owner_path") and isinstance(child, str):
                yield child
            yield from owner_mentions(child)
    elif isinstance(value, list):
        for child in value:
            yield from owner_mentions(child)


def collect(proposal_path):
    proposals = json.loads(proposal_path.read_text())["proposals"]
    contexts = []
    for path in sorted((QUEUE / "shards").glob("shard-*.json")):
        shard = json.loads(path.read_text())
        for case in shard["cases"]:
            contexts.append((path, case, set(owner_mentions(case))))
    report = []
    for proposal in proposals:
        after = ROOT / proposal["after_capture"]["path"]
        if hashlib.sha256(after.read_bytes()).hexdigest() != proposal["after_capture"]["sha256"]:
            raise ValueError(f"after changed: {after}")
        owner = yaml.safe_load(after.read_text())
        labels = {owner["preferred_term"]: "preferred_term"}
        for synonym in owner.get("synonyms", []):
            labels[synonym["synonym_text"]] = synonym.get("synonym_type", "UNSPECIFIED")
        matches = []
        for path, case, mentions in contexts:
            reasons = []
            if proposal["owner_path"] in mentions:
                reasons.append({"kind": "embedded_owner_path", "value": proposal["owner_path"]})
            for field in ("source_label", "raw_source_label"):
                label = case[field]
                if label and label in labels:
                    reasons.append({"kind": "exact_lexical_overlap", "source_field": field, "value": label, "proposed_owner_label_type": labels[label]})
            if reasons:
                matches.append({"shard": path.name, "shard_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "case_id": case["case_id"], "source": case["source"], "reasons": reasons})
        report.append({"proposal_id": proposal["proposal_id"], "owner_path": proposal["owner_path"], "before_sha256": proposal.get("before_sha256"), "matches": matches})
    return {"proposal_input_sha256": hashlib.sha256(proposal_path.read_bytes()).hexdigest(), "scope": "All immutable queue shards searched for explicit owner path fields and exact source label equality against proposed preferred/synonym text, including rejected labels. This is dependency discovery, not identity review of unassigned cases.", "dependencies": report}


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: find_cross_shard_dependencies.py PROPOSALS_JSON NEW_OUTPUT_JSON")
    destination = Path(sys.argv[2])
    if destination.exists():
        raise FileExistsError(destination)
    destination.write_text(json.dumps(collect(Path(sys.argv[1])), indent=2) + "\n")
