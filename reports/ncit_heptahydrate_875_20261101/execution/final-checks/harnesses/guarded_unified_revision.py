"""Run the native unified producer, validate its staged output, then publish it."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import os
import subprocess
import sys

from plugins.repository_settings import RepositorySettings
from plugins.lock_manager import LockManager
from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs

run = Path(__file__).resolve().parent
if len(sys.argv) != 4:
    raise SystemExit("usage: guarded_unified_revision.py MIM_WORKTREE CLAW_WORKTREE NEW_EVIDENCE_DIR")
step, producer, evidence_name = sys.argv[1:]
for name in (step, producer, evidence_name):
    if Path(name).name != name or name in (".", ".."):
        raise SystemExit("all locations must be named children of this run")
settings = RepositorySettings.from_environment()
mim = settings.get_target("mediaingredientmech").path
culture = settings.get_target("culturemech").path
assert mim == (run / step).resolve()
claw = run / producer
if subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=all"], cwd=claw, text=True).strip():
    raise SystemExit("producer must be a clean isolated checkout")
evidence = run / evidence_name
evidence.mkdir(exist_ok=False)
candidate = evidence / "unified-candidate.tsv"
assert not candidate.exists()
canonical = mim / "UNIFIED_INGREDIENT_MAPPING.tsv"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inputs():
    paths = sorted((culture / "data/normalized_yaml").rglob("*.yaml"))
    paths += sorted((mim / "data/ingredients/mapped").glob("*.yaml"))
    paths += sorted((mim / "data/ingredients/unmapped").glob("*.yaml"))
    paths += [mim / "docs/data/label_index.csv", mim / "mappings/unified_mapping_rejections.tsv",
              claw / "scripts/build_unified_ingredient_mapping.py"]
    return {str(p): sha(p) for p in paths}

with LockManager({"my_id": "codex-approved-plan"}).lock("mediaingredientmech", "approved_unified_rebuild"), reserve_receipt_outputs(
    evidence / "unified-generation-receipt.json", backup_paths=(evidence / "unified-before.tsv",)
) as (receipt_handle, backup_handle):
    before = canonical.read_bytes()
    snapshot = inputs()
    subprocess.run([sys.executable, str(claw / "scripts/build_unified_ingredient_mapping.py"),
                    "--culturemech", str(culture), "--mim", str(mim),
                    "--output", str(candidate), "--format", "tsv"], check=True, cwd=mim)
    subprocess.run([sys.executable, str(mim / "scripts/check_unified_rejections.py"),
                    "--artifact", str(candidate)], check=True, cwd=mim)
    with candidate.open(newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    rejected = [r for r in rows if r["mapping_status"] == "REJECTED" and not r["mim_id"]]
    leaked = [r for r in rows if r["mim_id"].startswith("kgmicrobe.compound:") and
              any(r[c].startswith("CHEBI:") for c in ("culturemech_term_id", "chebi_id", "kg_microbe_node_id"))]
    assert not rejected, rejected
    assert not leaked, leaked
    assert inputs() == snapshot, "Producer inputs changed during generation"
    assert canonical.read_bytes() == before, "Canonical changed during generation"
    backup_handle.write(before)
    backup_handle.flush()
    temporary = canonical.with_suffix(".approved-plan-stage.tsv")
    with temporary.open("xb") as f:
        f.write(candidate.read_bytes())
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, canonical)
    receipt = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operation": "native_unified_generation_with_validated_atomic_publication",
        "before_sha256": hashlib.sha256(before).hexdigest(),
        "after_sha256": sha(canonical), "input_sha256": snapshot,
        "rows": len(rows), "occurrences": sum(int(r["occurrence_count"]) for r in rows),
        "rejected_empty_identity": len(rejected), "local_compound_chebi_leaks": len(leaked),
        "approved_plan_sha256": sha(run / "approved-plan.txt"),
        "mim_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mim, text=True).strip(),
        "claw_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=claw, text=True).strip(),
        "culturemech_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=culture, text=True).strip(),
    }
    json.dump(receipt, receipt_handle, indent=2)
    receipt_handle.write("\n")
    receipt_handle.flush()
    print(json.dumps({k: v for k, v in receipt.items() if k != "input_sha256"}, indent=2))
