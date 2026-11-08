"""Real native source-writer known-history-gap preflight in a private repository."""
from pathlib import Path
import importlib.util
import json
import sys

D = Path(__file__).resolve().parent
S = D / "source-snapshot-v1"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


owner = load("mediaingredientmech.curate.campaign_owner_apply", S / "src/mediaingredientmech/curate/campaign_owner_apply.py")
t = load("independent_source_chain_fixture", S / "tests/test_campaign_owner_apply.py")
from mediaingredientmech.export.reviewed_sssom import read_sssom

root = D / "source-chain-fixture-v1"
root.mkdir()
plan = t.setup(root)
rows = read_sssom(root / t.CANONICAL)[2]
s = owner.digest(t.SSSOM)
t.put(root, t.native.BASELINE, {"schema_version": 1, "source_sha256": s, "rows": rows})
for name in (t.native.TRAIT_REFRESH, t.native.PARENT_REFRESH):
    t.put(root, name, {"schema_version": 1, "before_sha256": s, "after_sha256": s, "row_count": 1, "changed_rows": 0, "changes": []})
last = owner.digest(b"latest earlier native owner endpoint")
receipt = {"schema_version": 1, "batch": "history", "sequence": 1, "approval": "NONE: fixture", "before_sha256": s, "after_sha256": s, "before_row_count": 1, "after_row_count": 1, "position_map": [1], "changes": [], "changed_rows": 0, "added_rows": 0, "removed_rows": 0, "records": [{"source_record": t.EDIT, "shape": "existing", "before_yaml_sha256": owner.digest(b"earlier owner"), "after_yaml_sha256": last}]}
t.put(root, t.native.RECEIPTS_DIR + "/historical.json", receipt)
t.run_git(root, "add", "reports")
t.run_git(root, "-c", "user.email=fixture@example.invalid", "-c", "user.name=Fixture", "commit", "-qm", "Private native history fixture")
plan["baseline_commit"] = t.run_git(root, "rev-parse", "HEAD")
t.save_contract(root, plan)
proof = t.native.verify_mapping_chain(root)
before = (root / t.EDIT).read_bytes()
result = {"starting_native_chain_valid": True, "latest_native_owner_sha256": last, "actual_owner_before_sha256": owner.digest(before)}
try:
    prepared = owner.prepare(root, root / "plan.json", root / "acceptance.json")
    result["prepare"] = "accepted"
    applied = owner.apply(prepared, root / "receipt", enabled=True)
    result["apply"] = applied["state"]
    result["verify_completed"] = owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")["state"]
except Exception as error:
    result["error"] = type(error).__name__ + ": " + str(error)
result["source_owner_changed"] = (root / t.EDIT).read_bytes() != before
result["scope"] = "Actual source apply and native checkpoint verifier; no owner-proof or native-generation mock. Private synthetic repo only."
with (D / "source-chain-probe-v1.json").open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(json.dumps(result, indent=2))
