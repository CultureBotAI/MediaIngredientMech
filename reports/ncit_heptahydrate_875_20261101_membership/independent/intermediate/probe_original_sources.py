"""Independent same-cause #1033 check of original #875 source-phase writer."""
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
ROOT = RUN / "step2-mim"
sys.path[:0] = [str(ROOT), str(ROOT / "src"), str(RUN / "claw-source/src")]
spec = importlib.util.spec_from_file_location("independent_original_sources", ROOT / "scripts/promote_heptahydrate_ncit.py")
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
fixture = HERE / "original-sources-valid-owner-race"
artifact = ROOT / "reports/ncit_heptahydrate_875_20261101/execution/application"
before = {
    writer.OWNER: (artifact / "source-apply.before.yaml").read_bytes(),
    writer.LEDGER: (artifact / "source-apply.before-ledger.tsv").read_bytes(),
    writer.SSSOM: subprocess.check_output(["git", "-C", str(ROOT), "show", "40b787d37d33d544551389ff019f2d64ad63d7cc:mappings/ingredient_mappings.sssom.tsv"]),
    writer.EVIDENCE: (ROOT / writer.EVIDENCE).read_bytes(),
}
assert writer.digest(before[writer.OWNER]) == writer.OWNER_BEFORE
assert writer.digest(before[writer.LEDGER]) == writer.LEDGER_BEFORE
assert writer.digest(before[writer.SSSOM]) == writer.SSSOM_BEFORE
for rel, data in before.items():
    path = fixture / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
competitor = fixture / "data/ingredients/mapped/.ignored-backup/competing.yaml"
record = writer.yaml.safe_load((ROOT / writer.OWNER).read_bytes())
record["preferred_term"] = "Competing phosphate heptahydrate owner"
validated = writer.render(record)
original = writer.reserve_receipt_outputs

@contextmanager
def reserve(*args, **kwargs):
    with original(*args, **kwargs) as handles:
        competitor.parent.mkdir()
        competitor.write_bytes(validated)
        yield handles

writer.reserve_receipt_outputs = reserve
log = fixture / "evidence/source-apply.json"
out = {"captured_at": datetime.now(timezone.utc).isoformat(), "source_hash": writer.digest((ROOT / "scripts/promote_heptahydrate_ncit.py").read_bytes()),
       "before_sha256": {str(p): writer.digest(b) for p, b in before.items()},
       "competing_owner_native_validated": True}
try:
    result = writer.apply_sources(fixture, log, apply=True)
except Exception as error:
    out.update({"outcome": "REFUSED", "error": str(error), "type": type(error).__name__})
else:
    out.update({"outcome": "APPLIED_WITH_COMPETING_OWNER", "applied": result["applied"],
                "receipt_state": json.loads(log.read_text())["state"], "transaction": result["transaction"]})
finally:
    writer.reserve_receipt_outputs = original
out["input_changes"] = {str(p): (fixture / p).read_bytes() != b for p,b in before.items()}
out["competing_owner_preserved"] = competitor.read_bytes() == validated
(HERE / "original-sources-valid-owner-race.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
