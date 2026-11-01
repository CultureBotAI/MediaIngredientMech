"""Run the native unified producer, validate its staged output, then publish it."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import importlib.util
import subprocess
import sys

from plugins.repository_settings import RepositorySettings
from plugins.lock_manager import LockManager

run = Path(__file__).resolve().parent
if len(sys.argv) != 4:
    raise SystemExit("usage: guarded_unified_carnitine.py MIM_WORKTREE CLAW_WORKTREE NEW_EVIDENCE_DIR")
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
              claw / "scripts/build_unified_ingredient_mapping.py", Path(__file__),
              run / "approved-plan.txt"]
    # Bind the producer, checker and native publisher before loading/executing
    # them, including their repository-local implementation dependencies.
    for directory in (mim / "scripts", mim / "src", claw / "src", claw / "plugins"):
        paths += list(directory.rglob("*.py"))
    return {str(p): sha(p) for p in sorted(set(paths))}

publisher_path = mim / "scripts/promote_heptahydrate_ncit.py"
with LockManager({"my_id": "codex-approved-plan"}).lock("mediaingredientmech", "approved_unified_rebuild"):
    before = canonical.read_bytes()
    snapshot = inputs()
    spec = importlib.util.spec_from_file_location("approved_unified_native_publisher", publisher_path)
    publisher = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = publisher
    spec.loader.exec_module(publisher)
    assert inputs() == snapshot, "Code/input bytes changed during publisher import"
    subprocess.run([sys.executable, str(claw / "scripts/build_unified_ingredient_mapping.py"),
                    "--culturemech", str(culture), "--mim", str(mim),
                    "--output", str(candidate), "--format", "tsv"], check=True, cwd=mim)
    proposed = candidate.read_bytes()
    subprocess.run([sys.executable, str(mim / "scripts/check_unified_rejections.py"),
                    "--artifact", str(candidate)], check=True, cwd=mim)
    assert candidate.read_bytes() == proposed, "Candidate changed during validation"
    rows = list(csv.DictReader(io.StringIO(proposed.decode(), newline=""), delimiter="\t"))
    rejected = [r for r in rows if r["mapping_status"] == "REJECTED" and not r["mim_id"]]
    leaked = [r for r in rows if r["mim_id"].startswith("kgmicrobe.compound:") and
              any(r[c].startswith("CHEBI:") for c in ("culturemech_term_id", "chebi_id", "kg_microbe_node_id"))]
    assert not rejected, rejected
    assert not leaked, leaked
    assert inputs() == snapshot, "Producer inputs changed during generation"
    assert canonical.read_bytes() == before, "Canonical changed during generation"
    before_rows = list(csv.DictReader(before.decode().splitlines(), delimiter="\t"))
    before_by_name = {row["ingredient_name"]: row for row in before_rows}
    after_by_name = {row["ingredient_name"]: row for row in rows}
    assert len(before_by_name) == len(before_rows) and len(after_by_name) == len(rows)
    assert before_by_name.keys() == after_by_name.keys(), "ingredient population changed"
    changed = {name for name in before_by_name if before_by_name[name] != after_by_name[name]}
    assert changed == {"Carnitine Hydrochloride"}, changed
    old_row, new_row = before_by_name["Carnitine Hydrochloride"], after_by_name["Carnitine Hydrochloride"]
    assert old_row["mim_id"] == "kgmicrobe.compound:carnitine_hydrochloride"
    assert new_row["mim_id"] == "NCIT:C216679" and new_row["cas_rn"] == "461-05-2"
    assert {key for key in old_row if old_row[key] != new_row[key]} <= {"mim_id", "cas_rn", "synonyms"}
    forbidden = {"dl-carnitine", "3-hydroxy-4-(trimethylammonio)butanoate", "carnitinamide chloride"}
    assert not forbidden & {token.strip().casefold() for token in new_row["synonyms"].split("|")}
    captured_inputs = {Path(path): Path(path).read_bytes() for path in snapshot}
    assert all(hashlib.sha256(data).hexdigest() == snapshot[str(path)] for path, data in captured_inputs.items())
    captured_inputs.update({canonical: before, candidate: proposed})
    after_sha = hashlib.sha256(proposed).hexdigest()
    receipt = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operation": "native_unified_generation_with_validated_atomic_publication",
        "before_sha256": hashlib.sha256(before).hexdigest(),
        "after_sha256": after_sha, "input_sha256": snapshot,
        "bounded_changed_rows": sorted(changed),
        "native_publisher_sha256": hashlib.sha256(captured_inputs[publisher_path]).hexdigest(),
        "rows": len(rows), "occurrences": sum(int(r["occurrence_count"]) for r in rows),
        "rejected_empty_identity": len(rejected), "local_compound_chebi_leaks": len(leaked),
        "approved_plan_sha256": sha(run / "approved-plan.txt"),
        "mim_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=mim, text=True).strip(),
        "claw_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=claw, text=True).strip(),
        "culturemech_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=culture, text=True).strip(),
    }
    def recheck_complete_input_set():
        assert inputs() == snapshot, "Producer input paths or bytes changed before publication"

    result = publisher.publish(
        mim, {canonical.relative_to(mim): proposed}, captured_inputs,
        evidence / "unified-generation-receipt.json", {evidence / "unified-before.tsv": before},
        receipt, apply=True, validate_scope=recheck_complete_input_set,
    )
    assert sha(canonical) == after_sha
    print(json.dumps({key: value for key, value in result.items() if key != "input_sha256"}, indent=2))
