"""Private counterexample for a late direct-owner addition during verification."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
from datetime import datetime, timezone

D = Path(__file__).resolve().parent
S = D / "snapshot-v1"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


owner = load("mediaingredientmech.curate.campaign_owner_apply", S / "src/mediaingredientmech/curate/campaign_owner_apply.py")
fixture = load("independent_owner_fixture", S / "tests/test_campaign_owner_apply.py")
results = []
for attack in (False, True):
    root = D / "completed-inventory-fixtures-v1" / ("late-addition" if attack else "positive")
    root.mkdir(parents=True, exist_ok=False)
    fixture.setup(root)
    prepared = owner.prepare(root, root / "plan.json", root / "acceptance.json")
    application = owner.apply(prepared, root / "receipt", enabled=True)
    assert application["state"] == "complete"
    original = owner._validate_records
    unexpected = root / "data/ingredients/unmapped/Unexpected_late.yaml"
    injected = []

    def late_validate(*args, **kwargs):
        value = original(*args, **kwargs)
        # Runs after verify_completed captured current membership, before its
        # native checkpoint validation and final input-location/byte checks.
        unexpected.write_text("identifier: UNMAPPED_9999\npreferred_term: Unexpected late owner\nmapping_status: UNMAPPED\n")
        injected.append(str(unexpected))
        return value

    if attack:
        owner._validate_records = late_validate
    try:
        result = owner.verify_completed(root, root / "plan.json", root / "receipt/application.json")
        outcome = {"returned": result["state"], "reported_owner_count": len(result["after_inventory"])}
    except Exception as error:
        outcome = {"error": type(error).__name__ + ": " + str(error)}
    finally:
        owner._validate_records = original
    actual = owner.hashes(owner.inventory(root))
    results.append({"case": "late_addition" if attack else "positive", "injected": injected, "outcome": outcome, "actual_owner_count": len(actual), "unexpected_present": unexpected.exists(), "actual_inventory_matches_proof": actual == application["after_inventory"]})
report = {"at": datetime.now(timezone.utc).isoformat(), "source_sha256": hashlib.sha256((S / "src/mediaingredientmech/curate/campaign_owner_apply.py").read_bytes()).hexdigest(), "scope": "Private synthetic repositories; actual native source application and completion verifier. No maintained files or corpus edits.", "results": results}
p = D / "completed-inventory-probe-v1.json"
with p.open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, indent=2))
