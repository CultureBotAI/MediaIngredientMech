"""Read-only independent actual-application and product verification."""
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import subprocess
import yaml

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
ROOT = RUN / "step2-mim"
OLD = "kgmicrobe.compound:na2hpo4_x_7_h2o"
NEW = "NCIT:C61946"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def headbytes(path):
    return subprocess.check_output(["git", "-C", str(ROOT), "show", "HEAD:" + path])

def table(data, delimiter="\t"):
    return list(csv.DictReader(io.StringIO(data.decode()), delimiter=delimiter))

membership = "mappings/culturemech_recipe_membership.tsv"
before = (RUN / "step2-membership-application/apply.before-membership.tsv").read_bytes()
assert before == headbytes(membership)
after = (ROOT / membership).read_bytes()
receipt = json.loads((RUN / "step2-membership-application/apply.json").read_bytes())
assert receipt["applied"] is True and receipt["state"] == "complete"
assert sha(before) == receipt["before_sha256"]
assert sha(after) == receipt["after_sha256"] == "55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897"
journal = json.loads(Path(receipt["transaction"]["journal"]).read_bytes())
assert journal["status"] == "complete"
assert journal["changed"] == [str(ROOT / membership)]
assert journal["created"] == [] and len(journal["previous"]) == 1
assert journal["previous"][str(ROOT / membership)].encode() == before
assert before.splitlines()[0] == after.splitlines()[0]
ra = table(b"\n".join(line for line in before.splitlines() if not line.startswith(b"#")))
rb = table(b"\n".join(line for line in after.splitlines() if not line.startswith(b"#")))
sa = [(r["recipe_id"], r["occurrences"]) for r in ra if r["mim_identifier"] == OLD]
sb = [(r["recipe_id"], r["occurrences"]) for r in rb if r["mim_identifier"] == NEW]
assert len(sa) == len(sb) == 32 and sa == sb
assert len(ra) == len(rb) == 202098
assert [r for r in ra if r["mim_identifier"] != OLD] == [r for r in rb if r["mim_identifier"] != NEW]
assert not any(r["mim_identifier"] == OLD for r in rb)
assert dict(sb) == {r["recipe_id"]: str(r["occurrences"]) for r in receipt["memberships"]}

prior = yaml.safe_load((ROOT / "reviews/structured/20261101T054115Z-approved-step2-ncit-heptahydrate-review/review.yaml").read_bytes())
changed_prior = []
for entry in prior["source"]["inputs"]:
    content = (ROOT / entry["path"]).read_bytes()
    if sha(content) != entry["sha256"]:
        changed_prior.append(entry["path"])
expected_changed = {
    "scripts/promote_heptahydrate_ncit.py", "tests/test_promote_heptahydrate_ncit.py",
    "data/curated/ALL_INGREDIENTS.md", "data/curated/MAPPED_INGREDIENTS.md",
    "data/curated/all_ingredients_index.csv", "data/curated/all_ingredients_index.json",
    "data/curated/mapped_ingredients_index.csv", "data/curated/mapped_ingredients_index.json",
    "docs/data/all_ingredients.csv", "docs/data/all_ingredients.json", "docs/data/all_ingredients.md",
    "docs/data/ingredients.json", "docs/data/mapped_ingredients.csv", "docs/data/mapped_ingredients.json",
    "docs/data/mapped_ingredients.md",
}
assert set(changed_prior) == expected_changed, changed_prior

def compare_records(path):
    old = json.loads(headbytes(path)); new = json.loads((ROOT / path).read_bytes())
    metadata = None
    if isinstance(old, dict):
        metadata = {k: (old["metadata"][k], new["metadata"][k]) for k in old["metadata"] if old["metadata"][k] != new["metadata"][k]}
        assert set(metadata) == {"generated"}
        old, new = old["ingredients"], new["ingredients"]
    assert len(old) == len(new)
    changed = [(a,b) for a,b in zip(old,new) if a!=b]
    assert len(changed) == 1
    a,b=changed[0]
    assert a.get("identifier",a.get("id")) == b.get("identifier",b.get("id")) == NEW
    delta={k:{"before":a[k],"after":b[k]} for k in a if a[k]!=b[k]}
    assert set(delta).issubset({"occurrences","media_count","total_occurrences"}) and delta
    assert all(d == {"before":26,"after":32} for d in delta.values())
    return {"rows":len(old),"changed_records":1,"delta":delta,"metadata_delta":metadata}

products={p:compare_records(p) for p in (
    "data/curated/all_ingredients_index.json", "data/curated/mapped_ingredients_index.json",
    "docs/data/all_ingredients.json", "docs/data/mapped_ingredients.json", "docs/data/ingredients.json")}
for p in ("data/curated/all_ingredients_index.csv", "data/curated/mapped_ingredients_index.csv",
          "docs/data/all_ingredients.csv", "docs/data/mapped_ingredients.csv"):
    a,b=table(headbytes(p),","),table((ROOT/p).read_bytes(),",")
    assert len(a)==len(b)
    changed=[(x,y) for x,y in zip(a,b) if x!=y]
    assert len(changed)==1
    x,y=changed[0]
    assert x.get("identifier",x.get("Identifier")) == y.get("identifier",y.get("Identifier")) == NEW
    delta={k:{"before":x[k],"after":y[k]} for k in x if x[k]!=y[k]}
    assert all(d=={"before":"26","after":"32"} for d in delta.values())
    products[p]={"rows":len(a),"changed_records":1,"delta":delta}

checks=[]
for name in ("full-qc","final-focused-tests","reviewed-qc","reviewed-export","semantic-integrity",
             "supported-export","supported-qc","companion-export","companion-qc"):
    p=RUN / f"logs/step2-membership-{name}.json"
    meta=json.loads(p.read_bytes()); raw=Path(meta["log"]).read_bytes()
    assert meta["exit_code"]==0 and sha(raw)==meta["log_sha256"]
    checks.append({"receipt":str(p),"command":meta["argv"],"exit_code":meta["exit_code"],
                   "log_sha256":sha(raw),"finished_at":meta["finished_at"]})
owner=yaml.safe_load((ROOT / "data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml").read_bytes())
assert owner["occurrence_statistics"]=={"total_occurrences":26,"media_count":26}
out={"captured_at":datetime.now(timezone.utc).isoformat(),"head":subprocess.check_output(["git","-C",str(ROOT),"rev-parse","HEAD"],text=True).strip(),
     "membership_row_count":len(rb),"migrated_pairs":sa,"unrelated_rows_preserved":len(rb)-len(sb),
     "source_header_preserved":True,"complete_receipt_and_journal_verified":True,"membership_sha256":sha(after),
     "apply_receipt_sha256":sha((RUN / "step2-membership-application/apply.json").read_bytes()),
     "prior_native_inputs_verified":len(prior["source"]["inputs"]),"changed_prior_inputs":changed_prior,
     "unchanged_prior_input_count":len(prior["source"]["inputs"])-len(changed_prior),"product_deltas":products,
     "stored_yaml_statistics":owner["occurrence_statistics"],"checks":checks,"status":"PASS_PENDING_FREEZE_NATIVE_AND_FINAL_HEAD"}
(HERE / "verification.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k not in ("checks","product_deltas","migrated_pairs","changed_prior_inputs")},indent=2))
