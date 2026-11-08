"""#1195 successor adversarial case: dependency imported before owner operator."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

D = Path(__file__).resolve().parent
P = D / "preloaded-dependency-package-v1"
sys.path.insert(0, str(P / "src"))
from mediaingredientmech.curate import publication_guard

path = Path(publication_guard.__file__)
executing_dependency = path.read_bytes()
path.write_bytes(executing_dependency + b"\n# Private change after dependency import but before operator import.\n")
from mediaingredientmech.curate import campaign_owner_apply as owner

spec = importlib.util.spec_from_file_location("preloaded_dependency_fixture", P / "tests/test_campaign_owner_apply.py")
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
root = D / "preloaded-dependency-fixture-v1"
root.mkdir()
t.setup(root)
try:
    ready = owner.prepare(root, root / "plan.json", root / "acceptance.json")
    result = owner.apply(ready, root / "receipt")
    outcome = {"accepted": True, "applied": result["applied"]}
except Exception as error:
    outcome = {"accepted": False, "error": type(error).__name__ + ": " + str(error)}
sha = lambda raw: hashlib.sha256(raw).hexdigest()
report = {"operator_sha256": sha(Path(owner.__file__).read_bytes()), "loaded_dependency_sha256": sha(executing_dependency), "operator_claimed_loaded_dependency_sha256": sha(owner.LOADED_PRODUCERS["src/mediaingredientmech/curate/publication_guard.py"].content), "actual_on_disk_dependency_sha256": sha(path.read_bytes()), "same_function_object_is_used": owner.FrozenFile is publication_guard.FrozenFile, "outcome": outcome, "scope": "Private package/fixture and dry-run only. Uses a fresh process, with a legitimate already-imported native dependency before importing the new owner operator."}
with (D / "preloaded-dependency-result-v1.json").open("x") as f:
    json.dump(report, f, indent=2)
    f.write("\n")
print(json.dumps(report, indent=2))
