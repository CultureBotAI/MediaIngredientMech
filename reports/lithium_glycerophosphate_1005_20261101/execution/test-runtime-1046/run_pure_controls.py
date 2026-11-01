"""Offline fresh-process controls; only isolated fixture copies are mutated."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SOURCE = RUN / "step4-mim"
OUT = HERE / "controls"
OUT.mkdir(exist_ok=False)
script = "scripts/curate_lithium_glycerophosphate.py"
test = "tests/test_curate_lithium_glycerophosphate.py"
owned = json.loads((RUN / "step4-writer-checkpoint/manifest.json").read_bytes())["files"]
deps = ["scripts/promote_heptahydrate_ncit.py", "scripts/bump_sssom_header.py",
        "src/mediaingredientmech/curate/apply_receipt.py", "src/mediaingredientmech/curate/curation_event.py",
        "src/mediaingredientmech/validation/write_validated.py", "src/mediaingredientmech/schema/mediaingredientmech.yaml"]
original_hashes = {p: hashlib.sha256((SOURCE / p).read_bytes()).hexdigest() for p in [script, test]}
mutations = [
    ("control", None, None, "pure_"),
    ("candidate_guard_removed", "if row != expected:", "if False and row != expected:", "pure_candidate_claim_substitution_refused and source"),
    ("comment_preservation_removed", 'row["comment"] = old[obj]["comment"]', 'row["comment"] = row["comment"]', "pure_promotion_preserves"),
]
results = []
for name, old, new, selection in mutations:
    root = OUT / name
    root.mkdir()
    for relative in [*owned, *deps]:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE / relative, path)
    writer = root / script
    if old:
        text = writer.read_text()
        assert text.count(old) == 1
        writer.write_text(text.replace(old, new))
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=str(SOURCE / "src") + ":" + str(root))
    command = [sys.executable, "-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider", str(root / test), "-k", selection]
    result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
    (root / "stdout.log").write_text(result.stdout)
    (root / "stderr.log").write_text(result.stderr)
    assert result.returncode == (0 if name == "control" else 1), (name, result.stdout, result.stderr)
    assert "ModuleNotFoundError" not in result.stdout and "ERROR collecting" not in result.stdout
    results.append({"name": name, "selection": selection, "argv": command, "exit_code": result.returncode,
                    "writer_sha256": hashlib.sha256(writer.read_bytes()).hexdigest(),
                    "stdout_sha256": hashlib.sha256(result.stdout.encode()).hexdigest(),
                    "stderr_sha256": hashlib.sha256(result.stderr.encode()).hexdigest()})
assert original_hashes == {p: hashlib.sha256((SOURCE / p).read_bytes()).hexdigest() for p in original_hashes}
receipt = {"issue": 1046, "author_tree_unchanged": True, "source_hashes": original_hashes,
           "scope": "MIM-only pure proposal/promotion tests; no native publisher substitute and no production writes", "runs": results}
(HERE / "controls-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))
