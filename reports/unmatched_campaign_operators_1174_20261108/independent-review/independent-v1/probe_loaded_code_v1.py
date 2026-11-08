"""Private stale-import source pin control; no shared or maintained edits."""
from pathlib import Path
import hashlib
import importlib.util
import json
import shutil
import sys

D = Path(__file__).resolve().parent
S = D / "snapshot-v1"
P = D / "loaded-code-private-package-v1"
shutil.copytree(S, P)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


path = P / "src/mediaingredientmech/curate/campaign_owner_apply.py"
original = path.read_bytes()
module = load("mediaingredientmech.curate.campaign_owner_apply", path)
fixture = load("independent_loaded_fixture", P / "tests/test_campaign_owner_apply.py")
# Represents a file change after a long-lived process imports its operator,
# before the reviewed on-disk bytes and copied plan producer pins are captured.
path.write_bytes(original + b"\n# Private deterministic changed-producer fixture.\n")
root = D / "loaded-code-fixture-v1"
root.mkdir()
fixture.setup(root)
try:
    prepared = module.prepare(root, root / "plan.json", root / "acceptance.json")
    result = module.apply(prepared, root / "receipt")
    outcome = {"accepted": True, "applied": result["applied"]}
except Exception as error:
    outcome = {"accepted": False, "error": type(error).__name__ + ": " + str(error)}
report = {"loaded_source_sha256": hashlib.sha256(original).hexdigest(), "pinned_on_disk_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "fixture_producer_sha256": hashlib.sha256((root / "src/mediaingredientmech/curate/campaign_owner_apply.py").read_bytes()).hexdigest(), "outcome": outcome, "scope": "Private changed-import proof; no actual owner application, scientific data or maintained code writes."}
with (D / "loaded-code-probe-v1.json").open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, indent=2))
