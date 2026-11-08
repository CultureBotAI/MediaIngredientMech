"""Independent native projection of the two label-scope successors; read-only."""
import copy
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import yaml

HERE = Path(__file__).resolve().parent
D = HERE.parent.parent
W = D.parents[3]
sys.path.insert(0, str(W / "src"))
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.export.reviewed_sssom import _safe_synonyms

producer_path = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py")
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

assert sha(producer_path) == "38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc"
sys.path.insert(0, str(producer_path.parent))
spec = importlib.util.spec_from_file_location("skeptical_native_producer", producer_path)
producer = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = producer
spec.loader.exec_module(producer)
selected = json.loads((W / "reports/all_unmatched_20261107/worker-01/shard/proposals.json").read_text())["proposals"]
ids = ["CS-PROP-JCM1430_FERROUS_SULFATE_HCL_STOCK", "CS-PROP-NBRC1321_CO2_BICARBONATE_STOCK"]
results = []
for pid in ids:
    proposal = next(x for x in selected if x["proposal_id"] == pid)
    old_path = W / "reports/all_unmatched_20261107/worker-01" / proposal["after_capture"]["path"]
    new_path = D / "payloads" / (pid + ".yaml")
    old, new = yaml.safe_load(old_path.read_text()), yaml.safe_load(new_path.read_text())
    owner = Path(proposal["owner_path"])
    before = producer._row_from_yaml(owner, {}, {}, {}, {}, record=old, owners={})
    after = producer._row_from_yaml(owner, {}, {}, {}, {}, record=new, owners={})
    for row in before:
        _safe_synonyms(row, old)
    for row in after:
        _safe_synonyms(row, new)
    synonyms = [{"token": x["synonym_text"], "old_type": x["synonym_type"],
                 "new_type": y["synonym_type"], "old_resolves": is_resolving_synonym(x),
                 "new_resolves": is_resolving_synonym(y),
                 "before_other": any(x["synonym_text"] in z.get("other", "").split("|") for z in before),
                 "after_other": any(x["synonym_text"] in z.get("other", "").split("|") for z in after)}
                for x, y in zip(old["synonyms"], new["synonyms"])]
    results.append({"proposal_id": pid, "before": {"path": str(old_path), "sha256": sha(old_path)},
                    "after": {"path": str(new_path), "sha256": sha(new_path)},
                    "synonyms": synonyms, "before_rows": before, "after_rows": after,
                    "same_identity_predicates": [(x["subject_id"], x["predicate_id"], x["object_id"]) for x in before] ==
                    [(x["subject_id"], x["predicate_id"], x["object_id"]) for x in after]})
    if pid == ids[0]:
        wrong = copy.deepcopy(new)
        wrong["synonyms"].append(copy.deepcopy(old["synonyms"][0]))
        wrong_rows = producer._row_from_yaml(owner, {}, {}, {}, {}, record=wrong, owners={})
        try:
            for row in after:
                _safe_synonyms(row, wrong)
            rejected = False
            error = None
        except ValueError as exc:
            rejected = True
            error = str(exc)
        counterexample = {"description": "The actual producer removes a token when any active rejected entry shares it; the actual supported gate independently refuses the positive row when checked against that contradictory record.", "in_memory_only": True, "producer_excludes_token": not any(new["synonyms"][0]["synonym_text"] in row.get("other", "").split("|") for row in wrong_rows), "rejected": rejected, "error": error}

assert results[0]["synonyms"][0]["new_resolves"] and results[0]["synonyms"][0]["after_other"]
assert not results[0]["synonyms"][0]["old_resolves"] and not results[0]["synonyms"][0]["before_other"]
assert all(not x["new_resolves"] and not x["after_other"] for x in results[1]["synonyms"])
assert all(x["same_identity_predicates"] for x in results)
assert counterexample["rejected"] and counterexample["producer_excludes_token"]
output = {"reviewer": "/root/skeptical_review", "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "result": "PASS", "producer": {"path": str(producer_path), "sha256": sha(producer_path)},
          "script": {"path": str(Path(__file__).resolve()), "sha256": sha(Path(__file__).resolve())},
          "proposals": results, "negative_control": counterexample,
          "limits": ["Actual pinned native producer and supported alias gate executed on isolated records. Empty external overrides are explicit, not a canonical build or global ownership approval.",
                     "Independent native preferred-owner search is separately bound; this check does not establish substance identity.",
                     "The retired negative iron assertion remains in immutable predecessor and audit lineage; it is not simultaneously active in the successor."],
          "scientific_approval": False, "release_approval": False}
q = HERE / "label-projection-independent-v2.json"
with q.open("x") as f:
    json.dump(output, f, indent=2, ensure_ascii=False); f.write("\n")
print(json.dumps({"path": str(q), "sha256": sha(q), "result": "PASS", "negative_control": counterexample}, indent=2))
