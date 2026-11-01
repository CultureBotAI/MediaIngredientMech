"""Fresh-process counterfactuals in tiny isolated copies; never edit the author tree."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SOURCE = RUN / "step4-mim"
OUT = RUN / "step4-writer-controls"
OUT.mkdir(exist_ok=False)
script = "scripts/curate_lithium_glycerophosphate.py"
test = "tests/test_curate_lithium_glycerophosphate.py"
frozen = json.loads((HERE / "manifest.json").read_bytes())["files"]
for name, meta in frozen.items():
    assert hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == meta["sha256"]
dependencies = ["scripts/promote_heptahydrate_ncit.py", "scripts/bump_sssom_header.py",
                "src/mediaingredientmech/curate/apply_receipt.py", "src/mediaingredientmech/curate/curation_event.py",
                "src/mediaingredientmech/validation/write_validated.py", "src/mediaingredientmech/schema/mediaingredientmech.yaml"]
mutations = [
    ("control", None, None, "proposal_exact or native_promotion_preserves or candidate_claim_substitution or completed_promotion_requires or native_commit_boundary"),
    ("free_acid_retained", 'chemistry = record.pop("chemical_properties")', 'chemistry = record["chemical_properties"]', "proposal_exact"),
    ("candidate_guard_removed", 'if row != expected:', 'if False and row != expected:', "candidate_claim_substitution_refused and source"),
    ("receipt_check_removed", 'if (any(value.get(k) != v for k, v in expected.items())', 'if False and (any(value.get(k) != v for k, v in expected.items())', "completed_promotion_requires and approval"),
    ("scope_callback_removed", 'validate_scope=lambda: validate_scope(root, inputs))', 'validate_scope=None)', "native_commit_boundary and destination_owner"),
    ("comment_preservation_removed", 'row["comment"] = old[obj]["comment"]', 'row["comment"] = row["comment"]', "native_promotion_preserves"),
]
results = []
for name, old, new, selection in mutations:
    root = OUT / name
    root.mkdir()
    for relative in [*frozen, *dependencies]:
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE / relative, destination)
    path = root / script
    body = path.read_text()
    if old:
        assert body.count(old) == (2 if name == "scope_callback_removed" else 1)
        path.write_text(body.replace(old, new))
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", MIM_SSSOM_PRODUCER=str(RUN / "claw-cas-guard"))
    command = [sys.executable, "-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider", str(root / test), "-k", selection]
    process = subprocess.run(command, cwd=SOURCE, env=env, capture_output=True, text=True)
    (root / "stdout.log").write_text(process.stdout)
    (root / "stderr.log").write_text(process.stderr)
    assert (process.returncode == 0) if name == "control" else (process.returncode == 1), (name, process.stdout, process.stderr)
    assert "ERROR collecting" not in process.stdout and "ModuleNotFoundError" not in process.stdout
    results.append({"name": name, "selection": selection, "argv": command, "exit_code": process.returncode,
                    "writer_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
                    "stderr_sha256": hashlib.sha256(process.stderr.encode()).hexdigest()})
for name, meta in frozen.items():
    assert hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == meta["sha256"]
receipt = {"timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(), "scope": "Fresh-process tiny fixture copies; native transaction helpers, actual guard failures, no production edits",
           "author_tree_unchanged": True, "source_manifest_sha256": hashlib.sha256((HERE / "manifest.json").read_bytes()).hexdigest(),
           "runs": results}
(OUT / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
