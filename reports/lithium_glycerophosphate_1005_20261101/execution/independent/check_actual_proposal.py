"""Read-only binding of the real Step4 source execution and candidate proposal."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import yaml

OWN = Path(__file__).resolve().parent
RUN = OWN.parent
ROOT = RUN / "step4-mim"

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

sha = lambda b: hashlib.sha256(b).hexdigest()
writer = load("independent_actual_lithium_writer", ROOT / "scripts/curate_lithium_glycerophosphate.py")
maker = load("independent_actual_receipt", ROOT / "reports/sssom_completion_20260921/mapping_changes/make_receipt.py")
candidate = ROOT / "output/step4-native-candidate/candidate.sssom.tsv"
candidate_bytes = candidate.read_bytes()
assert sha(candidate_bytes) == "c96267c778bf86af6125b144fc32b3382df7c22883439190f88dc3c15005143a"
source_log = RUN / "step4-application/source-apply.json"
owner = (ROOT / writer.OWNER).read_bytes()
bound, receipt = writer.source_receipt(ROOT, source_log, owner)
before_owner = bound[writer.backups(source_log)[writer.OWNER]]
before = bound[writer.backups(source_log)[writer.SSSOM]]
baseline = bound[writer.backups(source_log)[writer.BASELINE]]
proposed = writer.promoted_sssom(before, candidate_bytes, owner)
proposed_baseline = writer.retired_baseline(baseline)
old, new = yaml.safe_load(before_owner), yaml.safe_load(owner)
assert new["identifier"] == "kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt"
assert new["supplied_form"] == [{"name": "sn-Glycerol 3-phosphate lithium salt", "cas_rn": "17989-41-2", "form": "lithium salt", "supplier": "Sigma-Aldrich", "catalog_number": "94124", "notes": "free-acid CAS/FW; Li stoichiometry unstated"}]
assert "chemical_properties" not in new
assert new["curation_history"][:-1] == old["curation_history"]
assert new["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"]
assert json.dumps(old["chemical_properties"], sort_keys=True) in new["curation_history"][-1]["changes"]
assert new["nutritional_roles"] == old["nutritional_roles"] and new["synonyms"] == old["synonyms"]
assert all(new[k] == old[k] for k in old if k not in {"identifier", "chemical_properties", "curation_history", "ontology_mapping"})
prior, current = maker.rows_of(before), maker.rows_of(proposed)
changes, positions = maker.align(prior, current)
assert [x["kind"] for x in changes].count("changed") == 2
assert [x["kind"] for x in changes].count("removed") == 1
assert len(changes) == 3
assert all((x["after"] or x["before"])["subject_id"] == writer.SUBJECT for x in changes)
target = [r for r in current if r["subject_id"] == writer.SUBJECT]
old_by_object = {r["object_id"]: r for r in prior if r["subject_id"] == writer.SUBJECT}
assert {r["object_id"] for r in target} == {writer.PARENT, writer.NEW}
for row in target:
    previous = old_by_object[row["object_id"]]
    assert row["validation_method"] == previous["validation_method"]
    assert set(previous["source"].split("|")) <= set(row["source"].split("|"))
    assert row["mapping_date"] == new["curation_history"][-1]["timestamp"][:10]
    if row["object_id"] == writer.PARENT:
        assert row["comment"] == previous["comment"] and "#390" in row["comment"]
        assert row["other"] == "" and row["predicate_id"] == "skos:broadMatch"
    else:
        assert row["other"] == "CAS:17989-41-2" and row["predicate_id"] == "skos:exactMatch"
def unrelated(content):
    return [x for x in content.splitlines(keepends=True) if not x.startswith((writer.SUBJECT + "\t").encode()) and not x.startswith((b"# mapping_date:", b"# mapping_set_version:"))]
assert unrelated(before) == unrelated(proposed)
assert len(baseline.splitlines()) - len(proposed_baseline.splitlines()) == 1
result = {"verdict": "PASS_READONLY_ACTUAL_PROPOSAL", "source_receipt_sha256": sha(source_log.read_bytes()),
          "owner_sha256": sha(owner), "candidate_sha256": sha(candidate_bytes),
          "canonical_before_sha256": sha(before), "canonical_proposed_sha256": sha(proposed),
          "baseline_proposed_sha256": sha(proposed_baseline), "rows_before": len(prior), "rows_proposed": len(current),
          "changed": 2, "removed": 1, "added": 0, "source_execution_revalidated": True,
          "unrelated_canonical_bytes_preserved": True, "target_rows": target,
          "science_approval_added": False, "production_writes": False}
(OWN / "actual-proposal.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
