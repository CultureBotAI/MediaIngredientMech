"""Read-only native occurrence/membership regression probe; writes only this folder."""
import csv
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
ROOT = RUN / "step2-mim"
CULTURE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech")
OCC = CULTURE / "output/ingredient_occurrences.tsv"
OLD = "kgmicrobe.compound:na2hpo4_x_7_h2o"
NEW = "NCIT:C61946"
sys.path.insert(0, str(ROOT / "src"))
import yaml
from mediaingredientmech.utils.culturemech_occurrences import (
    SOURCE_LABEL_IDENTIFIER_OVERRIDES, _source_label_key,
    mim_identifier_for_occurrence, membership_counts, effective_occurrence_statistics,
)

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()

csv.field_size_limit(1 << 30)
member = ROOT / "mappings/culturemech_recipe_membership.tsv"
owner = ROOT / "data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml"
inputs = [member, owner, OCC, ROOT / "src/mediaingredientmech/utils/culturemech_occurrences.py",
          ROOT / "scripts/build_culturemech_membership.py", ROOT / "scripts/refresh_occurrence_statistics.py",
          ROOT / "tests/test_culturemech_membership.py", ROOT / "docs/data/ingredients.json",
          ROOT / "docs/data/mapped_ingredients.json", ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv"]
before = {str(p): sha(p) for p in inputs}
record = yaml.safe_load(owner.read_text())
rows = list(csv.DictReader((line for line in member.open() if not line.startswith("#")), delimiter="\t"))
old_members = [r for r in rows if r["mim_identifier"] == OLD]
new_members = [r for r in rows if r["mim_identifier"] == NEW]
selected = []
with OCC.open() as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        label = row.get("preferred_term", "")
        if "na2hpo4" in label.lower() or "sodium phosphate dibasic heptahydrate" in label.lower() or "carnitine" in label.lower():
            selected.append(row)
native = load("native_membership_independent", ROOT / "scripts/build_culturemech_membership.py")
refresh = load("native_stats_independent", ROOT / "scripts/refresh_occurrence_statistics.py")
known = native.mim_identifiers()
edges, unknown = native.collect(OCC, known)
counts, total, recipes = refresh.read_occurrences(OCC)
grouped = Counter((r["preferred_term"], r["resolved_identifier"], mim_identifier_for_occurrence(r)) for r in selected)
source_labels = sorted({r["preferred_term"] for r in selected if r["resolved_identifier"] == OLD})
minimum_scope = ["Na2HPO4 x 7 H2O", "Na2HPO4.7H2O", "Na2HPO4·7H2O", "Na2HPO4•7H2O"]
extended_scope = minimum_scope + ["Sodium phosphate dibasic heptahydrate"]
hypotheses = []
for labelset in (source_labels, minimum_scope, extended_scope):
    # In-memory fixtures only: never write implementation or artifacts.
    original = SOURCE_LABEL_IDENTIFIER_OVERRIDES.copy()
    try:
        SOURCE_LABEL_IDENTIFIER_OVERRIDES.update({_source_label_key(label): NEW for label in labelset})
        candidate_edges, candidate_unknown = native.collect(OCC, known)
        candidate_counts, _, _ = refresh.read_occurrences(OCC)
        differences = sorted(set(candidate_edges) ^ set(edges))
        hypotheses.append({"labels": labelset, "new_memberships": [
            {"identifier": k[0], "recipe_id": k[1], "occurrences": v}
            for k, v in sorted(candidate_edges.items()) if k[0] == NEW],
            "new_count": candidate_counts.get(NEW), "old_count": candidate_counts.get(OLD),
            "old_unknown_count": candidate_unknown.get(OLD), "edge_key_difference": differences})
    finally:
        SOURCE_LABEL_IDENTIFIER_OVERRIDES.clear()
        SOURCE_LABEL_IDENTIFIER_OVERRIDES.update(original)
browser = json.loads((ROOT / "docs/data/ingredients.json").read_text())
flat = json.loads((ROOT / "docs/data/mapped_ingredients.json").read_text())
unified = list(csv.DictReader((ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv").open(), delimiter="\t"))
out = {"captured_at": datetime.now(timezone.utc).isoformat(), "head": git(ROOT, "rev-parse", "HEAD"),
       "tree": git(ROOT, "rev-parse", "HEAD^{tree}"), "git_status": git(ROOT, "status", "--short"),
       "culturemech_head": git(CULTURE, "rev-parse", "HEAD"), "inputs": before,
       "current_membership_header": member.read_text().splitlines()[0],
       "old_memberships": old_members, "old_membership_count": len(old_members),
       "old_membership_occurrences": sum(int(r["occurrences"]) for r in old_members),
       "new_memberships": new_members, "known_old": OLD in known, "known_new": NEW in known,
       "native_collect_new_count": sum(k[0] == NEW for k in edges),
       "native_collect_old_unknown_recipes": unknown.get(OLD),
       "native_refresh_old_count": counts.get(OLD), "native_refresh_new_count": counts.get(NEW),
       "stored_statistics": record["occurrence_statistics"],
       "effective_statistics": effective_occurrence_statistics(record, membership_counts(member)),
       "source_grouped": [{"name": k[0], "resolved_identifier": k[1], "native_route": k[2], "rows": v}
                          for k, v in sorted(grouped.items())],
       "browser_rows": [r for r in browser["ingredients"] if r.get("identifier") == NEW],
       "flat_rows": [r for r in flat if r.get("identifier") == NEW],
       "unified_rows": [r for r in unified if r.get("mim_id") == NEW],
       "proposed_scope_simulations_not_implementation": hypotheses,
       "all_inputs_unchanged": before == {str(p): sha(p) for p in inputs}}
(HERE / "selected-occurrences.json").write_text(json.dumps(selected, indent=2) + "\n")
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: out[k] for k in ("head", "old_membership_count", "old_membership_occurrences",
    "new_memberships", "known_old", "known_new", "native_collect_old_unknown_recipes",
    "native_refresh_old_count", "native_refresh_new_count", "stored_statistics", "effective_statistics", "all_inputs_unchanged")}, indent=2))
