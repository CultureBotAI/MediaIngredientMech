"""Validate isolated proposals against native schema/catalogue without applying them."""
import dataclasses
import datetime
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import yaml

from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient

ROOT = Path.cwd()
OUT = ROOT / "reports/all_unmatched_20261107/worker-07"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    proposals = json.loads((OUT / "proposals.json").read_text())["proposals"]
    baseline = json.loads((OUT / "captures/root-maintained-baseline-hashes.json").read_text())
    changed_baseline = [path for path, digest in baseline["files"].items() if not (ROOT / path).is_file() or sha(ROOT / path) != digest]
    catalogue = {str(path.relative_to(ROOT)): yaml.safe_load(path.read_text()) for state in ("mapped", "unmapped") for path in (ROOT / "data/ingredients" / state).glob("*.yaml")}
    original_record_count = len(catalogue)
    original_ids = defaultdict(list)
    for path, record in catalogue.items():
        original_ids[record["identifier"]].append(path)
    baseline_violations = {str(v) for v in validate_component_partonomy(catalogue.values())}
    results = []
    for proposal in proposals:
        path = OUT / proposal["after_capture"]["path"]
        assert sha(path) == proposal["after_capture"]["sha256"]
        record = yaml.safe_load(path.read_text())
        owner = proposal["owner_path"]
        before = catalogue.get(owner)
        errors = [str(e) for e in validate_ingredient(record)]
        if before is not None:
            assert sha(ROOT / owner) == proposal["before_sha256"]
            old_history = before.get("curation_history", [])
            assert record.get("curation_history", [])[:len(old_history)] == old_history
            assert len(record.get("curation_history", [])) > len(old_history)
        else:
            assert proposal["kind"] == "new_owner" and proposal["before_sha256"] is None
        collisions = [p for p in original_ids.get(record["identifier"], []) if p != owner]
        # Existing historical duplicate IDs are reported, not silently merged.
        introduced_collision = bool(collisions and (before is None or before.get("identifier") != record["identifier"]))
        results.append({"proposal_id": proposal["proposal_id"], "owner_path": owner, "after_sha256": sha(path), "identifier": record["identifier"], "schema_errors": errors, "other_existing_identifier_owners": collisions, "introduced_identifier_collision": introduced_collision})
        catalogue[owner] = record
    identifiers = defaultdict(list)
    for result in results:
        identifiers[result["identifier"]].append(result["proposal_id"])
    proposal_id_collisions = {key: value for key, value in identifiers.items() if len(value) > 1}
    final_violations = validate_component_partonomy(catalogue.values())
    introduced_violations = [dataclasses.asdict(v) for v in final_violations if str(v) not in baseline_violations]
    proposal_ids = {row["identifier"] for row in results}
    proposal_violations = [dataclasses.asdict(v) for v in final_violations if v.record_id in proposal_ids]
    passed = not (changed_baseline or introduced_violations or proposal_violations or proposal_id_collisions or any(r["schema_errors"] or r["introduced_identifier_collision"] for r in results))
    receipt = {"validated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "status": "PASS" if passed else "FAIL", "method": "Native closed-schema validate_ingredient; full catalogue partonomy with proposed owners substituted in memory; identifier collision and append-only history checks; baseline byte preservation. Glob includes ignored records.", "proposals_sha256": sha(OUT / "proposals.json"), "existing_catalogue_record_count": original_record_count, "existing_catalogue_unique_identifier_count": len(original_ids), "baseline_file_count": len(baseline["files"]), "changed_baseline_files": changed_baseline, "baseline_partonomy_violations": sorted(baseline_violations), "introduced_partonomy_violations": introduced_violations, "proposal_partonomy_violations": proposal_violations, "proposal_identifier_collisions": proposal_id_collisions, "results": results, "scientific_approval": False}
    (OUT / "logs/final-proposal-validation.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({key: receipt[key] for key in ("status", "proposals_sha256", "baseline_file_count", "changed_baseline_files", "introduced_partonomy_violations", "proposal_partonomy_violations", "proposal_identifier_collisions")}))
    print(f"Validated {len(results)} isolated proposals; maintained files not written.")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
