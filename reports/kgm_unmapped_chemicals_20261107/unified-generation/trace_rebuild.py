"""Bind the native rebuild and trace its complete cell delta to #1149."""

import csv
import hashlib
import json
import os
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def main():
    culture = Path(os.environ["CULTUREMECH_ROOT"])
    claw = Path(os.environ["CLAW_ROOT"])
    artifact = "UNIFIED_INGREDIENT_MAPPING.tsv"
    before = git(ROOT, "show", "0dac278466699129a083343a921c2e0ca18a9ab4:" + artifact)
    after = (HERE / "candidate.tsv").read_bytes()
    old = list(csv.DictReader(before.decode().splitlines(), delimiter="\t"))
    new = list(csv.DictReader(after.decode().splitlines(), delimiter="\t"))
    assert [r["ingredient_name"] for r in old] == [r["ingredient_name"] for r in new]
    owner_path = "data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml"
    owner_bytes = (ROOT / owner_path).read_bytes()
    owner = yaml.safe_load(owner_bytes)
    assert owner["identifier"] == owner["ontology_mapping"]["ontology_id"] == "CHEBI:32138"
    assert owner["chemical_properties"]["cas_rn"] == "6131-90-4"
    alias = "Na acetate x 3 H2O"
    assert any(s.get("synonym_text") == alias for s in owner["synonyms"])
    cells = []
    for line, (a, b) in enumerate(zip(old, new, strict=True), 2):
        for col in a:
            if a[col] == b[col]:
                continue
            assert b["mim_id"] == owner["identifier"]
            assert b["chebi_id"] == owner["ontology_mapping"]["ontology_id"]
            assert b["cas_rn"] == owner["chemical_properties"]["cas_rn"]
            assert b["mapping_status"] == "MAPPED"
            if col == "synonyms":
                prior = a[col].split("|") if a[col] else []
                assert alias in b[col].split("|")
                if prior:
                    assert set(b[col].split("|")) == set(prior) | {alias}
            else:
                assert b["ingredient_name"] == alias
                assert col in {"chebi_id", "cas_rn", "kg_microbe_node_id", "mim_id", "mapping_status"}
                assert not a[col] or (col == "mapping_status" and a[col] == "TERM_ID_NO_MIM")
                if col == "kg_microbe_node_id":
                    assert b[col] == owner["kg_microbe_node_id"]
            cells.append({"line": line, "ingredient": b["ingredient_name"], "column": col,
                          "before": a[col], "after": b[col], "owner": owner_path,
                          "owner_sha256": sha(owner_bytes), "issue": 1149})
    assert len(cells) == 13 and len({c["line"] for c in cells}) == 8
    inputs = {}
    for category in ("mapped", "unmapped"):
        for path in sorted((ROOT / "data/ingredients" / category).glob("*.yaml")):
            inputs["mim:" + str(path.relative_to(ROOT))] = sha(path.read_bytes())
    for rel in ("docs/data/label_index.csv", "mappings/unified_mapping_rejections.tsv"):
        inputs["mim:" + rel] = sha((ROOT / rel).read_bytes())
    for path in sorted((culture / "data/normalized_yaml").rglob("*.yaml")):
        inputs["culturemech:" + str(path.relative_to(culture))] = sha(path.read_bytes())
    for rel in ("output/ingredients_list.tsv", "output/ingredient_occurrences.tsv"):
        inputs["culturemech_comparison:" + rel] = sha((culture / rel).read_bytes())
    for rel in ["scripts/build_unified_ingredient_mapping.py", "plugins/ingredient_name_normalizer.py"]:
        inputs["claw:" + rel] = sha((claw / rel).read_bytes())
    for path in sorted((claw / "src/kg_microbe_fleet").rglob("*.py")):
        inputs["claw:" + str(path.relative_to(claw))] = sha(path.read_bytes())
    report = {"baseline": "0dac278466699129a083343a921c2e0ca18a9ab4",
              "mim_working_tree_inputs": True,
              "culturemech_revision": git(culture, "rev-parse", "HEAD").decode().strip(),
              "culturemech_status": git(culture, "status", "--porcelain").decode(),
              "claw_revision": git(claw, "rev-parse", "HEAD").decode().strip(),
              "before_sha256": sha(before), "after_sha256": sha(after),
              "rows": len(new), "same_membership_and_order": True,
              "changed_cells": cells, "inputs": inputs,
              "decision": "Promote native rebuild: every changed cell traces to the scientifically reviewed #1149 owner alias. No new recipe membership or other identity change."}
    output = HERE / "traced-rebuild.json"
    with output.open("x") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
