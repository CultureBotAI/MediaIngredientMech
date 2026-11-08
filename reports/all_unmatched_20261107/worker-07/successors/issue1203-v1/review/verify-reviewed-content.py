"""Independent issue1203 integrity check; does not grant scientific approval.

Inputs: published predecessor, immutable shard, current successor ledgers.
Output: a new reviewer receipt under this review directory; no maintained writes.
Author: /root/mg_independent_reviewer, 2026-11-08.
"""
import datetime
import hashlib
import json
from pathlib import Path

import yaml

from mediaingredientmech.validation.write_validated import validate_ingredient

ROOT = Path.cwd()
ARTIFACT = ROOT / "reports/all_unmatched_20261107/worker-07"
SUCCESSOR = ARTIFACT / "successors/issue1203-v1"
QUEUE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5")
CHANGED = {
    "CM_NAME:9dd78dd62f6762ad602b4126b067042b0cc68ba65bd212f9a10b07ec20b33e8e",
    "KG_CASE:ac6686c0d61be7f652dcf0c2a495b463e1adf24fee613329fd02707bd19d759d",
}


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def main():
    old = {x["case_id"]: x for x in read(ARTIFACT / "decisions.json")["decisions"]}
    new = {x["case_id"]: x for x in read(SUCCESSOR / "decisions.json")["decisions"]}
    frozen = {x["case_id"]: x for x in read(QUEUE / "shards/shard-07.json")["cases"]}
    assert set(old) == set(new) == set(frozen)
    assert {key for key in old if old[key] != new[key]} == CHANGED
    for key, decision in new.items():
        case = frozen[key]
        assert decision["case_input_sha256"] == digest(case)
        assert decision["source"] == {field: case[field] for field in ("source", "source_case_id", "source_label", "raw_source_label")}
        assert decision["occurrence_ids"] == [o["occurrence_id"] for o in case.get("occurrences", [])]
    evidence = {e["evidence_id"]: e for e in read(SUCCESSOR / "evidence.json")["evidence"]}
    old_evidence = {e["evidence_id"]: e for e in read(ARTIFACT / "evidence.json")["evidence"]}
    assert all(evidence[key] == value for key, value in old_evidence.items())
    for item in evidence.values():
        capture = item["capture"]
        root = ARTIFACT if capture["root"] == "artifact" else QUEUE
        assert sha(root / capture["path"]) == capture["sha256"], item["evidence_id"]
    proposals = {p["proposal_id"]: p for p in read(SUCCESSOR / "proposals.json")["proposals"]}
    old_proposals = {p["proposal_id"]: p for p in read(ARTIFACT / "proposals.json")["proposals"]}
    assert set(old_proposals) - set(proposals) == {"B-PROPOSAL-Mgso4_X_7_H2o", "C-P08"}
    assert set(proposals) - set(old_proposals) == {"C-P08-ISSUE1203-V1", "W07-MG350-ISSUE1203-V1"}
    assert all(proposals[key] == old_proposals[key] for key in set(proposals) & set(old_proposals))
    payloads = []
    for proposal in proposals.values():
        capture = proposal["after_capture"]
        assert sha(ARTIFACT / capture["path"]) == capture["sha256"]
        assert all(proposal["proposal_id"] in new[key]["proposal_ids"] for key in proposal["case_ids"])
        assert all(key in evidence for key in proposal["evidence_ids"])
        if proposal["proposal_id"] not in old_proposals:
            record = yaml.safe_load((ARTIFACT / capture["path"]).read_text())
            errors = [str(error) for error in validate_ingredient(record)]
            assert not errors
            assert record["identifier"].startswith("kgmicrobe.ingredient:")
            assert record["ingredient_type"] == "STOCK_SOLUTION"
            assert record["ontology_mapping"]["ontology_id"] == record["identifier"]
            assert record["component_assertion"]["completeness"] == "UNKNOWN"
            assert len(record["components"]) == 1
            assert record["components"][0]["component_id"] == "CHEBI:31795"
            assert all(s["synonym_text"] != "Mg(SO4) x 7 H2O" for s in record.get("synonyms", []))
            assert "culturemech_reference" not in record
            payloads.append({"proposal_id": proposal["proposal_id"], "capture": capture, "schema_errors": errors})
    occurrence_file = SUCCESSOR / "occurrence-dispositions.json"
    rows = read(occurrence_file)["occurrences"]
    authored = read(SUCCESSOR / "research/occurrence-assessment.json")["occurrences"]
    assert len(rows) == len(authored) == 17
    for authored_row, row in zip(authored, rows):
        assert all(row[key] == value for key, value in authored_row.items())
        material = row["resolved_material_identifier"]
        if row["stock_concentration"]:
            proposal = proposals[row["proposal_ids"][0]]
            record = yaml.safe_load((ARTIFACT / proposal["after_capture"]["path"]).read_text())
            assert material == record["identifier"]
            assert row["occurrence_id"] in proposal["occurrence_ids"]
            assert row["stock_concentration"]["value"] == record["components"][0]["concentration_value"]
        else:
            assert material == "CHEBI:31795" and row["proposal_ids"] == []
    result = {
        "reviewer": "/root/mg_independent_reviewer",
        "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "PASS",
        "scientific_approval_established": False,
        "exact_case_bindings": len(new),
        "changed_case_ids": sorted(CHANGED),
        "unchanged_case_count": len(new) - len(CHANGED),
        "proposal_count": len(proposals),
        "unchanged_proposal_count": len(set(proposals) & set(old_proposals)),
        "evidence_hashes_verified": len(evidence),
        "occurrence_routes_verified": len(rows),
        "changed_payloads": payloads,
        "inputs": {str(path.relative_to(ARTIFACT)): sha(path) for path in [SUCCESSOR / "decisions.json", SUCCESSOR / "evidence.json", SUCCESSOR / "proposals.json", occurrence_file, SUCCESSOR / "supersession.json"]},
    }
    output = SUCCESSOR / "review/independent-structural-check-v1.json"
    assert not output.exists()
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
