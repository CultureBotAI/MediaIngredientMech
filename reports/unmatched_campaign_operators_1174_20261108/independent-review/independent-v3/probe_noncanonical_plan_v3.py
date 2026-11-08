"""Private noncanonical accepted-plan path roundtrip control."""
from pathlib import Path
import importlib.util
import json
import sys

D = Path(__file__).resolve().parent
S = D / "source-snapshot-v2"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


owner = load("mediaingredientmech.curate.campaign_owner_apply", S / "src/mediaingredientmech/curate/campaign_owner_apply.py")
t = load("independent_noncanonical_fixture", S / "tests/test_campaign_owner_apply.py")
root = D / "noncanonical-plan-fixture-v1"
root.mkdir()
t.setup(root)
plan = root / "intake/../plan.json"
acceptance = root / "intake/../acceptance.json"
before = (root / t.EDIT).read_bytes()
result = {}
try:
    prepared = owner.prepare(root, plan, acceptance)
    result["prepare"] = "accepted"
    result["plan_ref"] = prepared.plan_ref
    result["acceptance_ref"] = prepared.acceptance_ref
    result["apply"] = owner.apply(prepared, root / "receipt", enabled=True)["state"]
    try:
        result["verify_completed"] = owner.verify_completed(root, plan, root / "receipt/application.json")["state"]
    except Exception as error:
        result["verification_error"] = type(error).__name__ + ": " + str(error)
except Exception as error:
    result["preflight_error"] = type(error).__name__ + ": " + str(error)
result["source_changed"] = (root / t.EDIT).read_bytes() != before
result["scope"] = "Actual native source application; all references address private fixture files, no symlinks or external filesystem writes."
with (D / "noncanonical-plan-probe-v1.json").open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(json.dumps(result, indent=2))
