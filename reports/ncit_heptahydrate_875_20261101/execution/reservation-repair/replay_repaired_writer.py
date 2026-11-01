"""Replay repaired writer on isolated before-images; never edit production data."""

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import sys

import yaml

run = Path(__file__).resolve().parent.parent
repo = run / "step2-mim"
destination = Path(__file__).resolve().parent / "isolated-replay"
destination.mkdir(exist_ok=False)
sys.path.insert(0, str(run / "claw-source/src"))
spec = importlib.util.spec_from_file_location("repair_replay_writer", repo / "scripts/promote_heptahydrate_ncit.py")
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
sha = lambda data: hashlib.sha256(data).hexdigest()
production_paths = [repo / writer.OWNER, repo / writer.LEDGER, repo / writer.SSSOM]
production_paths += [p for p in (run / "step2-application").rglob("*") if p.is_file()]
before = {str(p): sha(p.read_bytes()) for p in production_paths}
inputs = {
    writer.OWNER: run / "step2-application/source-apply.before.yaml",
    writer.LEDGER: run / "step2-application/source-apply.before-ledger.tsv",
    writer.SSSOM: run / "step2-application/source-apply.before.sssom.tsv",
    writer.EVIDENCE: repo / writer.EVIDENCE,
}
for relative, source in inputs.items():
    target = destination / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as stream:
        stream.write(source.read_bytes())
candidate = destination / "native-candidate.tsv"
with candidate.open("xb") as stream:
    stream.write((repo / "output/step2-native-candidate/candidate.sssom.tsv").read_bytes())
source_log, promotion_log = destination / "source.json", destination / "promotion.json"
source_result = writer.apply_sources(destination, source_log, apply=True)
promotion_result = writer.promote(destination, promotion_log, source_log, candidate,
                                  sha(candidate.read_bytes()), apply=True)
assert (destination / writer.LEDGER).read_bytes() == (repo / writer.LEDGER).read_bytes()
assert (destination / writer.SSSOM).read_bytes() == (repo / writer.SSSOM).read_bytes()
old_owner = yaml.safe_load(inputs[writer.OWNER].read_bytes())
new_owner = yaml.safe_load((destination / writer.OWNER).read_bytes())
assert new_owner["curation_history"][:-1] == old_owner["curation_history"]
source_repeat = writer.apply_sources(destination, source_log, apply=True)
promotion_repeat = writer.promote(destination, promotion_log, source_log, candidate,
                                  sha(candidate.read_bytes()), apply=True)
assert source_repeat["changed"] is False and promotion_repeat["changed"] is False
assert before == {str(p): sha(p.read_bytes()) for p in production_paths}
native = Path(sys.modules["kg_microbe_write.transaction"].__file__)
result = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "scope": "Author replay in an isolated fixture containing only the target owner and full frozen ledger/SSSOM; not independent review or a production reapplication.",
    "writer_sha256": sha((repo / "scripts/promote_heptahydrate_ncit.py").read_bytes()),
    "original_application_writer_sha256": "a66389a3379a761ee263aceb08222b6508f57cb9b8e69e996e82af732b59bb85",
    "native_transaction_path": str(native), "native_transaction_sha256": sha(native.read_bytes()),
    "candidate_sha256": sha(candidate.read_bytes()),
    "source_result": source_result, "promotion_result": promotion_result,
    "source_repeat": source_repeat, "promotion_repeat": promotion_repeat,
    "ledger_bytes_identical_to_production": True, "canonical_bytes_identical_to_production": True,
    "source_history_prefix_preserved": True,
    "fixture_event_timestamp": new_owner["curation_history"][-1]["timestamp"],
    "fixture_event_note": "New actual replay timestamp; the production event was not copied or rewritten.",
    "production_inputs_and_historical_receipts_unchanged": before,
    "scientific_approval_added": False,
}
with (Path(__file__).resolve().parent / "replay-result.json").open("x") as stream:
    json.dump(result, stream, indent=2); stream.write("\n")
print(json.dumps({key: result[key] for key in ["writer_sha256", "ledger_bytes_identical_to_production",
    "canonical_bytes_identical_to_production", "source_history_prefix_preserved", "scientific_approval_added"]}, indent=2))
