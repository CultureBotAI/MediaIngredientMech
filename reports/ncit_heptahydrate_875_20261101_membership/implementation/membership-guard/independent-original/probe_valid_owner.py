"""Follow-up: the competing owner is itself accepted by the native serializer."""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import yaml

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
ROOT = RUN / "step2-mim"
sys.path[:0] = [str(ROOT), str(ROOT / "src"), str(RUN / "claw-source/src")]
spec = importlib.util.spec_from_file_location("membership_writer_valid_owner", ROOT / "scripts/repair_heptahydrate_membership.py")
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
guarded = writer.guarded
fixture = HERE / "valid-owner-after-reservation"
for rel in [*writer.ANCHORS, writer.MEMBERSHIP]:
    path = fixture / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / rel, path)
record = yaml.safe_load((ROOT / guarded.OWNER).read_bytes())
record["preferred_term"] = "Competing phosphate heptahydrate owner"
validated = guarded.render(record)
competitor = fixture / "data/ingredients/mapped/.ignored-backup/competing.yaml"
original = guarded.reserve_receipt_outputs

@contextmanager
def insert_valid_owner(*args, **kwargs):
    with original(*args, **kwargs) as handles:
        competitor.parent.mkdir()
        competitor.write_bytes(validated)
        yield handles

guarded.reserve_receipt_outputs = insert_valid_owner
log = fixture / "evidence/repair.json"
result = writer.repair(fixture, log, apply=True)
guarded.reserve_receipt_outputs = original
try:
    guarded.unique_destination(fixture)
except ValueError as error:
    uniqueness_error = str(error)
else:
    uniqueness_error = None
out = {"captured_at": datetime.now(timezone.utc).isoformat(),
       "writer_sha256": hashlib.sha256((ROOT / "scripts/repair_heptahydrate_membership.py").read_bytes()).hexdigest(),
       "competing_owner_validated_by_native_serializer": True,
       "competing_owner_sha256": hashlib.sha256(validated).hexdigest(),
       "receipt": str(log), "result_applied": result["applied"],
       "receipt_state": json.loads(log.read_text())["state"],
       "after_sha256": hashlib.sha256((fixture / writer.MEMBERSHIP).read_bytes()).hexdigest(),
       "uniqueness_check_after_success": uniqueness_error}
(HERE / "valid-owner-race.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
