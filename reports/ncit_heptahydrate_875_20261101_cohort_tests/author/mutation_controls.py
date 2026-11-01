"""Fresh-process controls on isolated copies; never edit the actual repository."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys

OUT = Path(__file__).resolve().parent
RUN = OUT.parent
ROOT = RUN / "step2-mim"
TEST = "tests/test_repair_heptahydrate_membership.py"
paths = [
    TEST,
    "scripts/repair_heptahydrate_membership.py",
    "scripts/promote_heptahydrate_ncit.py",
    "scripts/build_culturemech_membership.py",
    "reports/ncit_heptahydrate_875_20261101_membership/application/apply.before-membership.tsv.gz",
    "reports/ncit_heptahydrate_875_20261101_membership/application/apply.json",
    "reports/sssom_scientific_curation_20261101/audit875/current-culturemech-occurrences.tsv",
]
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
original = {path: sha(ROOT / path) for path in paths}
cases = [
    ("control", "actual_archived_migration or native_membership_growth", 0, "3 passed"),
    ("restore_live_quota", "native_membership_growth", 1, "2 failed"),
    ("discard_repeat_listing", "native_membership_growth and repeat_listing", 1, "1 failed"),
    ("skip_historical_migration", "actual_archived_migration", 1, "1 failed"),
]
results = []
for name, selection, expected, summary in cases:
    fixture = OUT / "mutations" / name
    fixture.mkdir(parents=True)
    for path in paths:
        destination = fixture / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, destination)
    change = None
    if name == "restore_live_quota":
        path = fixture / TEST
        before = '    assert not any(row["mim_identifier"] == guarded.OLD for row in rows)\n'
        after = before + '    assert {row["recipe_id"]: row["occurrences"] for row in rows if row["mim_identifier"] == guarded.NEW} == dict.fromkeys(writer.RECIPES, "1")\n'
        change = (path, before, after)
    elif name == "discard_repeat_listing":
        change = (fixture / "scripts/build_culturemech_membership.py",
                  "            edges[(identifier, recipe_id)] += 1",
                  "            edges[(identifier, recipe_id)] = 1")
    elif name == "skip_historical_migration":
        change = (fixture / "scripts/repair_heptahydrate_membership.py",
                  '    """Preserve every row\'s bytes except the selected identity cell and order."""\n',
                  '    """Preserve every row\'s bytes except the selected identity cell and order."""\n    return before\n')
    if change:
        path, before, after = change
        text = path.read_text()
        assert text.count(before) == 1
        path.write_text(text.replace(before, after))
    cmd = [sys.executable, "-B", "-m", "pytest", "-q", "-o", "addopts=",
           "-p", "no:cacheprovider", "--basetemp", str(fixture / "pytest-tmp"),
           str(fixture / TEST), "-k", selection]
    process = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    log = OUT / f"mutation-{name}.log"
    log.open("x").write(process.stdout + process.stderr)
    assert process.returncode == expected, (name, process.returncode, process.stdout[-3000:])
    assert summary in process.stdout and "ERROR collecting" not in process.stdout
    results.append({"name": name, "argv": cmd, "exit_code": process.returncode,
                    "expected_exit_code": expected, "expected_summary": summary,
                    "log": log.name, "log_sha256": sha(log),
                    "changed_copy": str(change[0].relative_to(OUT)) if change else None,
                    "changed_copy_sha256": sha(change[0]) if change else None})
assert {path: sha(ROOT / path) for path in paths} == original
report = {"at": datetime.now(timezone.utc).isoformat(),
          "source_hashes": original, "production_files_unchanged": True,
          "fresh_python_process_per_case": True, "cases": results}
(OUT / "mutation-results.json").open("x").write(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
