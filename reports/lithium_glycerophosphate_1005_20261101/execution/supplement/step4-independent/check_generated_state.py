"""Independent byte/surface comparisons after the real Step4 native execution."""
from pathlib import Path
import csv
import hashlib
import importlib.util
import io
import json
import subprocess
import yaml

OWN = Path(__file__).resolve().parent
RUN = OWN.parent
ROOT = RUN / "step4-mim"
BASE = "838d0c2627552b0094545ebb580b5bb9b1a84d57"
SUBJECT = "MIM:Sn-Glycerol_3-phosphate_Lithium_Salt"
NAME = "sn-Glycerol 3-phosphate lithium salt"
IDENTITY = "kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt"
OWNER = Path("data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml")
sha = lambda data: hashlib.sha256(data).hexdigest()
def prior(path):
    return subprocess.check_output(["git", "show", BASE + ":" + str(path)], cwd=ROOT)
def load(path):
    return yaml.load(path, Loader=yaml.CSafeLoader)

out = {"base": BASE, "production_mutations": False, "checks": {}}
owner = load((ROOT / OWNER).read_bytes())
assert sha((ROOT / OWNER).read_bytes()) == "4b9f262ea27e2ad760b43ae9e3fa4af7e30a4f1af88573335e5beef08832e6e4"
for name in ("mapped", "unmapped"):
    path = Path(f"data/curated/{name}_ingredients.yaml")
    old, new = load(prior(path)), load((ROOT / path).read_bytes())
    assert {k:v for k,v in old.items() if k not in {"generation_date", "ingredients"}} == {k:v for k,v in new.items() if k not in {"generation_date", "ingredients"}}
    if name == "mapped":
        selected = [x for x in new["ingredients"] if x["preferred_term"] == NAME]
        assert selected == [owner]
        assert [x for x in old["ingredients"] if x["preferred_term"] != NAME] == [x for x in new["ingredients"] if x["preferred_term"] != NAME]
    else:
        assert old["ingredients"] == new["ingredients"]
    out["checks"][str(path)] = "PASS: target-only record change; metadata date permitted"

for path in ("docs/data/all_ingredients.json", "docs/data/mapped_ingredients.json", "data/curated/all_ingredients_index.json", "data/curated/mapped_ingredients_index.json"):
    old, new = json.loads(prior(path)), json.loads((ROOT / path).read_bytes())
    assert len(old) == len(new)
    assert [x for x in old if x["preferred_term"] != NAME] == [x for x in new if x["preferred_term"] != NAME]
    before = next(x for x in old if x["preferred_term"] == NAME)
    after = next(x for x in new if x["preferred_term"] == NAME)
    assert after == {**before, "identifier": IDENTITY}
    out["checks"][path] = "PASS: only target identifier changes; other entries exact"

for path in ("docs/data/ingredient_graph.json", "docs/data/ingredient_umap.json"):
    old, new = json.loads(prior(path)), json.loads((ROOT / path).read_bytes())
    assert [x for x in old if x["id"] != SUBJECT] == [x for x in new if x["id"] != SUBJECT]
    before = next(x for x in old if x["id"] == SUBJECT)
    after = next(x for x in new if x["id"] == SUBJECT)
    assert after == {**before, "identifier": IDENTITY, "molecular_formula": "", "cas_rn": ""}
    out["checks"][path] = "PASS: target identity/chemistry metadata corrected; coordinates and others exact"

path = "docs/data/ingredients.json"
old, new = json.loads(prior(path)), json.loads((ROOT / path).read_bytes())
assert {k:v for k,v in old["metadata"].items() if k != "generated"} == {k:v for k,v in new["metadata"].items() if k != "generated"}
assert [x for x in old["ingredients"] if x["record_id"] != SUBJECT] == [x for x in new["ingredients"] if x["record_id"] != SUBJECT]
target = next(x for x in new["ingredients"] if x["record_id"] == SUBJECT)
assert target["id"] == IDENTITY and target["synonym_count"] == 0
assert not target["synonyms"]
out["checks"][path] = "PASS: only target browser metadata and generation timestamp change; rejected aliases absent"

labels = list(csv.DictReader(io.StringIO((ROOT / "docs/data/label_index.csv").read_text())))
selected = [x for x in labels if x["preferred_term"] == NAME]
assert len(selected) == 1 and selected[0]["identifier"] == IDENTITY and selected[0]["label"] == NAME
out["checks"]["label_index"] = "PASS: exactly the preferred label resolves to target, under its local identity"

receipt_path = RUN / "step4-unified-evidence/unified-generation-receipt.json"
receipt = json.loads(receipt_path.read_bytes())
assert receipt["state"] == "complete" and receipt["applied"] is True
assert receipt["transaction"]["changed"] == [str(ROOT / "UNIFIED_INGREDIENT_MAPPING.provenance.json")]
assert receipt["transaction"]["created"] == receipt["transaction"]["unchanged"] == []
artifact = (ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv").read_bytes()
candidate = (RUN / "step4-unified-evidence/unified-candidate.tsv").read_bytes()
assert artifact == candidate == prior("UNIFIED_INGREDIENT_MAPPING.tsv")
assert receipt["before_sha256"] == receipt["after_sha256"] == sha(artifact)
rows = list(csv.DictReader(io.StringIO(artifact.decode()), delimiter="\t"))
assert len(rows) == receipt["rows"] == 4170 and sum(int(r["occurrence_count"]) for r in rows) == receipt["occurrences"] == 209330
assert len({r["ingredient_name"] for r in rows}) == len(rows)
assert not any(r["mapping_status"] == "REJECTED" and not r["mim_id"] for r in rows)
assert not any(r["mim_id"].startswith("kgmicrobe.compound:") and any(r[c].startswith("CHEBI:") for c in ("chebi_id", "culturemech_term_id", "kg_microbe_node_id")) for r in rows)
assert not any(r["ingredient_name"].casefold() == NAME.casefold() for r in rows)
hash_labels = sorted(r["ingredient_name"] for r in rows if r["ingredient_name"].startswith("#"))
assert hash_labels
for path, expected in receipt["input_sha256"].items():
    assert sha(Path(path).read_bytes()) == expected, path
spec = importlib.util.spec_from_file_location("independent_native_freshness", ROOT / "scripts/check_unified_freshness.py")
stamper = importlib.util.module_from_spec(spec); spec.loader.exec_module(stamper)
stamp_path = ROOT / "UNIFIED_INGREDIENT_MAPPING.provenance.json"
stamp = json.loads(stamp_path.read_bytes())
assert sha(stamp_path.read_bytes()) == receipt["provenance_after_sha256"] == "894a4bd1ce014e9a78d7abc27d206112c299f971124c5c8a0059c0e84f6973c4"
assert (stamp["mim_inputs_digest"], stamp["mim_record_count"]) == stamper.inputs_digest(ROOT / "data/ingredients")
assert stamp["artifact_sha256"] == sha(artifact) and stamp["artifact_rows"] == len(rows) and stamp["mim_rev"] == BASE[:8]
out["unified"] = {"artifact_sha256": sha(artifact), "byte_equal_native_candidate_and_base": True, "rows": len(rows), "occurrences": receipt["occurrences"], "hash_prefixed_names_preserved": hash_labels, "bound_input_paths_rechecked": len(receipt["input_sha256"]), "provenance_sha256": sha(stamp_path.read_bytes()), "actual_runtime_claw": receipt["runtime_claw_head"], "producer_claw": receipt["claw_head"], "culturemech": receipt["culturemech_head"]}
for path in (".github/workflows/qc-evidence.yaml", "scripts/.vendored_canon_ref"):
    assert (ROOT / path).read_bytes() == prior(path)
    out["checks"][path] = "PASS: protected file bytes unchanged"
out["verdict"] = "PASS_ACTUAL_GENERATED_SURFACES_WITHOUT_SCIENTIFIC_APPROVAL"
(OWN / "actual-generated-state.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
