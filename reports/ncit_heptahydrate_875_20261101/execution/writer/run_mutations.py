"""Fresh-process negative controls in disposable copies, never the working writer."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent / "step2-mim"
relative = Path("scripts/promote_heptahydrate_ncit.py")
original = (ROOT / relative).read_text()
cases = {
    "positive": None,
    "omit_ledger_migration": (
        "ledger = corrected_ledger(inputs[root / LEDGER])",
        "ledger = inputs[root / LEDGER]",
    ),
    "discard_previous_history": (
        'proposal["identifier"] = NEW',
        'proposal["curation_history"] = []\n    proposal["identifier"] = NEW',
    ),
    "discard_historical_source_tokens": (
        'row["source"] = "|".join(dict.fromkeys(parent["source"].split("|") + row["source"].split("|")))',
        'row["source"] = row["source"]',
    ),
    "allow_inherited_validation_stamp": (
        '"mapping_date": date, "validation_method": "", "comment": "",',
        '"mapping_date": date, "comment": "",',
    ),
    "ignore_input_race": (
        'if any(path.read_bytes() != expected for path, expected in inputs.items()):',
        'if False:',
    ),
    "ignore_candidate_hash": (
        'if digest(proposed) != candidate_sha256:',
        'if False:',
    ),
}
results = []
for name, change in cases.items():
    root = OUT / "mutations" / name
    text = original
    if change:
        old, new = change
        assert original.count(old) == 1, name
        text = original.replace(old, new)
    files = [
        "scripts/bump_sssom_header.py", "tests/test_promote_heptahydrate_ncit.py",
        "tests/fixtures/issue875-owner-before.yaml",
        "reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json",
    ]
    for item in files:
        target = root / item
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise FileExistsError(target)
        shutil.copyfile(ROOT / item, target)
    with (root / relative).open("x") as stream:
        stream.write(text)
    env = dict(os.environ, PYTHONPYCACHEPREFIX=str(root / "pycache"), PYTHONDONTWRITEBYTECODE="1")
    args = [sys.executable, "-m", "pytest", "tests/test_promote_heptahydrate_ncit.py",
            "-k", "not committed_surfaces", "-c", "/dev/null", "--confcutdir", str(root),
            "--no-cov", "-q", "--tb=short", "-p", "no:cacheprovider"]
    proc = subprocess.run(args, cwd=root, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    with (root / "pytest.log").open("x") as stream:
        stream.write(proc.stdout)
    result = {"case": name, "exit_code": proc.returncode,
              "source_sha256": hashlib.sha256(text.encode()).hexdigest(),
              "log_sha256": hashlib.sha256(proc.stdout.encode()).hexdigest(),
              "summary": proc.stdout.splitlines()[-1], "argv": args}
    results.append(result)
    print(json.dumps(result))
    assert proc.returncode == (1 if change else 0), result
assert (ROOT / relative).read_text() == original
with (OUT / "mutation-results.json").open("x") as stream:
    json.dump({"completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "working_source_unchanged": True, "fresh_python_process_each": True,
               "results": results}, stream, indent=2)
    stream.write("\n")
