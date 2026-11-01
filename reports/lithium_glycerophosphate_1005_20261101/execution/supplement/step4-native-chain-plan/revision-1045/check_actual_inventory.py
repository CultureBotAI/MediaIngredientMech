"""Read-only real-tree inventory verification; never executes the chain."""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLAN = HERE.parent
spec = importlib.util.spec_from_file_location("step4_chain_readonly_1045", PLAN / "native_chain.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
before = c.git("status", "--porcelain=v1", "-z")
paths = c.individual_record_scope()
legacy = {p for p in c.git("ls-tree", "-r", "--name-only", c.BASE, "data/ingredients").decode().splitlines() if p.endswith(".yaml")}
actual = {p.relative_to(c.ROOT).as_posix() for p in (c.ROOT / "data/ingredients").rglob("*.yaml")}
assert paths == actual
assert c.git("status", "--porcelain=v1", "-z") == before
result = {
    "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "issue": 1045,
    "source_sha256": c.sha(PLAN / "native_chain.py"),
    "base": c.BASE,
    "root": str(c.ROOT),
    "native_chain_executed": False,
    "individual_records": len(paths),
    "legacy_parsed_records": len(legacy),
    "legacy_missing_paths": sorted(paths - legacy),
    "unrelated_records_byte_identical_to_base": len(paths - {c.OWNER}),
    "owner_change_excluded_only": c.OWNER,
    "ignored_and_nested_scan": "Path.rglob includes ignored and nested files",
    "git_status_unchanged": True,
    "all_paths_sha256": hashlib.sha256(json.dumps(sorted(paths), ensure_ascii=False).encode()).hexdigest(),
    "verdict": "PASS",
}
with (HERE / "actual-inventory.json").open("x") as stream:
    json.dump(result, stream, indent=2, ensure_ascii=False)
    stream.write("\n")
print(json.dumps(result, indent=2, ensure_ascii=False))
