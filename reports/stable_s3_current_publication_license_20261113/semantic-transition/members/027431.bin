"""2026-11-12: seal bounded four-owner primary groundwork, not native approval.

Reads current owner/table and exact primary captures. Writes notes, pins and
readback only beside this script. No corpus change, native invocation or votes.
"""
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import yaml

OUT = Path(__file__).resolve().parent
C = OUT.parents[1]
TC = C / "integration/stable-adoption-real-canary-target"
W01 = C / "workers/w01/worktree"
W10 = C / "workers/w10/worktree/reports/all_unmatched_20261107/ancillary_xanthine1258_proposal_v1"
OWNER_NAMES = ["Sodium_Acetate_Trihydrate", "Xanthine", "Arabinan_From_Sugar_Beet", "CeNO33_X_6_H2O"]
paths = [TC / ("data/ingredients/mapped/" + name + ".yaml") for name in OWNER_NAMES]
paths += [TC / name for name in [
    "AGENTS.md", "MAPPING_SEMANTICS.md", "docs/record-reviews.md",
    "docs/record-review-profile.md", "docs/INGREDIENT_SCOPE_PROFILE.md",
    ".claude/skills/review-sssom-output/SKILL.md", "mappings/ingredient_mappings.sssom.tsv",
    "reports/stable_ids_1265_20261108/mapping-review.json",
    "reports/stable_ids_1265_20261108/mapping-evidence.json",
    "reports/sssom_completion_20260921/mapping_review/chemical-scope-review.md",
    "reports/separate-real-canary-existing-owner-inputs-v1/COPY-PROVENANCE.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/arabinan-manufacturer-capture.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/arabinan-chebi.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/cerium-mediadive1587.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/cerium-pubchem16211466.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/cerium-pubchem-synonyms.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/cerium-meshM0319657.json",
    "reports/separate-real-canary-existing-owner-inputs-v1/cerium-sigma238538.json",
    ".temp/real-canary-existing-skeptic-final-v1/cerium/completed-review.yaml",
    ".temp/real-canary-existing-owner-primary-final-v1/HANDOFF.json",
]]
paths += [W01 / ("reports/kgm_unmapped_chemicals_20261107/sodium-acetate/sources/" + name)
          for name in ["chebi-32138.json", "mediadive-1315.json"]]
paths += [W10 / name for name in ["archive/inputs/additional-08-chebi17712.capture",
    "archive/inputs/additional-10-chebi17712-metadata.json", "archive/science/whole-owner-source-matrix.json"]]
paths += sorted(OUT.glob("*.body")) + sorted(OUT.glob("*.receipt.json")) + [OUT / "PUBLIC-REFRESH.json"]
raw = {str(path): path.read_bytes() for path in paths}
sha = lambda b: hashlib.sha256(b).hexdigest()
pins = {name: {"sha256": sha(body), "bytes": len(body)} for name, body in raw.items()}
owners = {name: yaml.safe_load(raw[str(TC / ("data/ingredients/mapped/" + name + ".yaml"))]) for name in OWNER_NAMES}
old = json.loads(raw[str(TC / "reports/stable_ids_1265_20261108/mapping-review.json")])
proof = json.loads(raw[str(TC / "reports/stable_ids_1265_20261108/mapping-evidence.json")])
table = raw[str(TC / "mappings/ingredient_mappings.sssom.tsv")].decode()
rows = list(csv.DictReader([line for line in table.splitlines() if not line.startswith("#")], delimiter="\t"))
selected = []
for position, row in enumerate(rows, 1):
    if row["subject_id"] not in {record["mim_id"] for record in owners.values()}:
        continue
    decision = next(item for item in old["decisions"] if item["source_position"] == position)
    evidence = proof["entries"][str(position)]
    row_hash = sha(json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())
    assert row_hash == decision["row_sha256"] == evidence["row_sha256"]
    selected.append({"position": position, "row": row, "old_decision": decision,
                     "old_owner_sha256": evidence["owner_record_sha256"],
                     "current_owner_sha256": sha((TC / decision["owner_record"]).read_bytes())})
fresh = {key: json.loads((OUT / (key + ".body")).read_bytes())
         for key in ["chebi32138", "chebi17712", "chebi48517", "chebi22590", "meshM0319657"]}
assert fresh["chebi32138"]["ascii_name"] == owners["Sodium_Acetate_Trihydrate"]["ontology_mapping"]["ontology_label"]
assert fresh["chebi32138"]["chemical_data"]["formula"] == owners["Sodium_Acetate_Trihydrate"]["chemical_properties"]["molecular_formula"]
for key in ["chebi17712", "chebi48517"]:
    assert "69-89-6" in {entry["accession_number"] for entry in fresh[key]["database_accessions"]["CAS"]}
assert fresh["meshM0319657"]["@type"].endswith("#Concept")
assert "descriptor" in owners["CeNO33_X_6_H2O"]["ontology_mapping"]["evidence"][1]["notes"]
assert all(Path(name).read_bytes() == body for name, body in raw.items())
readback = {"at": datetime.now(timezone.utc).isoformat(), "reviewer": "/root/canary_publication_primary",
    "status": "CURRENT_OWNER_MAPPING_GROUNDWORK_NOT_PUBLICATION_REVIEW",
    "head_observed": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=TC).decode().strip(),
    "owner_count": len(owners), "canonical_rows_observed": len(rows), "selected_current_rows": selected,
    "owners": {name: {"mim_id": record["mim_id"], "identifier": record["identifier"],
                        "ontology_mapping": record["ontology_mapping"], "synonyms": record.get("synonyms", [])}
               for name, record in owners.items()},
    "source_refresh": json.loads((OUT / "PUBLIC-REFRESH.json").read_bytes()),
    "earlier_web_tool_attempt": {"count": 5, "result": "All exact API opens returned inaccessible via web tool; preserved as failed access, then ordinary direct public retrieval succeeded.",
                                 "tool": "web.run.open", "urls": [entry["url"] for entry in json.loads((OUT / "PUBLIC-REFRESH.json").read_bytes()).values()]},
    "limitations": ["No generated selection yet; no future row disposition or canonical installation/release approval.",
        "Current owner assessment is not source-wide identity, role, supplied grade or subclass authorization.",
        "Original native reports and historical mapping decisions remain immutable; changed owner bytes withdraw inherited support.",
        "No claim of exhaustive current ontology/CAS namespace search."]}
for name, data in [("INPUT-PINS.json", pins), ("READBACK.json", readback)]:
    with (OUT / name).open("x") as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
print(json.dumps({"readback": str(OUT / "READBACK.json"), "sha256": sha((OUT / "READBACK.json").read_bytes()), "pins": len(pins)}))
