"""Private completed-publisher membership counterexample, isolated boundaries."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import pytest

D = Path(__file__).resolve().parent
S = D / "snapshot-v1"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


c = load("mediaingredientmech.campaign_publication", S / "src/mediaingredientmech/campaign_publication.py")
t = load("independent_publication_fixture", S / "tests/test_campaign_publication.py")
out = []
for attack in (False, True):
    directory = D / "publisher-inventory-fixtures-v1" / ("late-addition" if attack else "positive")
    directory.mkdir(parents=True)
    with pytest.MonkeyPatch.context() as monkey:
        case = t.case.__wrapped__(directory, monkey)
        publication = c.publish(case["root"], case["path"], case["out"], apply=True)
        assert publication["status"] == "complete"
        generation = c._generation
        unexpected = case["root"] / "data/ingredients/unmapped/Unexpected_late.yaml"

        def late_generation(*args, **kwargs):
            value = generation(*args, **kwargs)
            unexpected.write_text("identifier: UNMAPPED_9999\npreferred_term: Unexpected late owner\nmapping_status: UNMAPPED\n")
            return value

        if attack:
            monkey.setattr(c, "_generation", late_generation)
        try:
            verified = c.validate(case["root"], case["path"])
            result = {"returned": verified["status"]}
        except Exception as error:
            result = {"error": type(error).__name__ + ": " + str(error)}
        out.append({"case": "late_addition" if attack else "positive", "outcome": result, "unexpected_present": unexpected.exists(), "inventory_matches_claimed": t.inventory(case["root"]) == case["owner_proof"]["after_inventory"]})
report = {"source_sha256": hashlib.sha256((S / "src/mediaingredientmech/campaign_publication.py").read_bytes()).hexdigest(), "scope": "Author's synthetic fixture isolates owner proof and generation as explicit mocks, while native receipt replay, projection, policy and publication filesystem operations are real. Demonstrates the outer validator's missing final membership recheck, not full native generation.", "results": out}
with (D / "publisher-inventory-probe-v1.json").open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, indent=2))
