"""Independent #1031 review; real native transactions only in external fixtures."""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
ROOT = RUN / "step2-mim"
sys.path[:0] = [str(ROOT), str(ROOT / "src"), str(RUN / "claw-source/src")]
spec = importlib.util.spec_from_file_location("independent_membership_writer", ROOT / "scripts/repair_heptahydrate_membership.py")
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
guarded = writer.guarded

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

tracked = [ROOT / p for p in [*writer.ANCHORS, writer.MEMBERSHIP,
    Path("scripts/repair_heptahydrate_membership.py"), Path("tests/test_repair_heptahydrate_membership.py"),
    Path("src/mediaingredientmech/utils/culturemech_occurrences.py"),
    Path("scripts/promote_heptahydrate_ncit.py")]]
preimages = {str(p.relative_to(ROOT)): sha(p) for p in tracked}

def fixture(name):
    root = HERE / name
    for rel in [*writer.ANCHORS, writer.MEMBERSHIP]:
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, target)
    return root, root / "evidence/repair.json"

results = []
root, log = fixture("native-success")
before = {str(p): (root / p).read_bytes() for p in [*writer.ANCHORS, writer.MEMBERSHIP]}
result = writer.repair(root, log, apply=True)
after_receipt = log.read_bytes()
second = writer.repair(root, log, apply=True)
assert result["applied"] is True
assert sha(root / writer.MEMBERSHIP) == writer.AFTER_SHA
assert all((root / p).read_bytes() == before[str(p)] for p in writer.ANCHORS)
assert log.with_suffix(".before-membership.tsv").read_bytes() == before[str(writer.MEMBERSHIP)]
assert not second["changed"] and log.read_bytes() == after_receipt
results.append({"case": "real_native_complete_apply_and_noop", "outcome": "PASS",
                "receipt": str(log), "sha256": sha(log), "transaction": result["transaction"]})

original = guarded.reserve_receipt_outputs
root, log = fixture("destination-owner-after-reservation")
competitor = root / "data/ingredients/mapped/.ignored-racing-owner/competitor.yaml"

@contextmanager
def insert_owner_after_reservation(*args, **kwargs):
    with original(*args, **kwargs) as handles:
        competitor.parent.mkdir()
        competitor.write_text(f"identifier: {guarded.NEW}\npreferred_term: competing owner\nmapping_status: MAPPED\n")
        yield handles

guarded.reserve_receipt_outputs = insert_owner_after_reservation
try:
    try:
        result = writer.repair(root, log, apply=True)
    except Exception as error:
        results.append({"case": "destination_owner_introduced_after_reservation", "outcome": "REFUSED",
                        "error": str(error), "type": type(error).__name__, "after_sha256": sha(root / writer.MEMBERSHIP)})
    else:
        results.append({"case": "destination_owner_introduced_after_reservation", "outcome": "APPLIED_WITH_COMPETING_OWNER",
                        "after_sha256": sha(root / writer.MEMBERSHIP), "result": result,
                        "receipt_state": json.loads(log.read_text())["state"],
                        "competing_owner_preserved": competitor.read_text()})
finally:
    guarded.reserve_receipt_outputs = original

out = {"captured_at": datetime.now(timezone.utc).isoformat(), "input_hashes": preimages,
       "input_hashes_unchanged": preimages == {str(p.relative_to(ROOT)): sha(p) for p in tracked}, "results": results}
(HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
