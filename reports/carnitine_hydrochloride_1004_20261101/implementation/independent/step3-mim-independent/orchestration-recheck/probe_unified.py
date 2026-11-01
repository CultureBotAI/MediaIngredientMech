"""Exercise the exact orchestration with real native publishing in external fixtures.

Only producer/checker subprocesses, Git metadata and caller lock/settings are
simulated. The proposal publisher, output reservation and native transaction run.
"""
from pathlib import Path
from contextlib import contextmanager, nullcontext
from types import SimpleNamespace
from unittest.mock import patch
import csv
import hashlib
import io
import json
import runpy
import shutil
import subprocess
import sys

from plugins.repository_settings import RepositorySettings
from plugins.lock_manager import LockManager
import mediaingredientmech.curate.apply_receipt as receipts

OUT = Path(__file__).resolve().parent
RUN = OUT.parents[1]
SCRIPT = RUN / "guarded_unified_carnitine.py"
sys.path.insert(0, str(RUN / "step3-mim"))
FIELDS = ["ingredient_name", "mim_id", "cas_rn", "synonyms", "mapping_status",
          "culturemech_term_id", "chebi_id", "kg_microbe_node_id", "occurrence_count"]
old = {k: "" for k in FIELDS}
old.update(ingredient_name="Carnitine Hydrochloride", mim_id="kgmicrobe.compound:carnitine_hydrochloride", mapping_status="MAPPED", occurrence_count="14")
other = {**old, "ingredient_name": "Unrelated", "mim_id": "NCIT:C1", "occurrence_count": "1"}
new = {**old, "mim_id": "NCIT:C216679", "cas_rn": "461-05-2", "synonyms": "Carnitine (Dl) Hydrochloride|DL-Carnitine Hydrochloride"}


def tsv(rows):
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
    writer.writeheader(); writer.writerows(rows)
    return buf.getvalue().encode()


results = []
original_read = Path.read_bytes
original_reserve = receipts.reserve_receipt_outputs
for case in ("control", "candidate_during_checker", "candidate_after_validation", "new_input_after_snapshot", "new_code_after_snapshot", "changed_code_after_snapshot"):
    root = OUT / "unified-cases" / case
    mim, claw, culture = root / "mim", root / "claw", root / "culture"
    for directory in (mim / "data/ingredients/mapped", mim / "data/ingredients/unmapped", mim / "docs/data",
                      mim / "mappings", mim / "scripts", claw / "scripts", culture / "data/normalized_yaml"):
        directory.mkdir(parents=True)
    script = root / SCRIPT.name
    script.write_bytes(SCRIPT.read_bytes())
    (root / "approved-plan.txt").write_text("external fixture only")
    (mim / "scripts/promote_heptahydrate_ncit.py").write_bytes((RUN / "step3-mim/scripts/promote_heptahydrate_ncit.py").read_bytes())
    (mim / "docs/data/label_index.csv").write_text("label,identifier\n")
    (mim / "mappings/unified_mapping_rejections.tsv").write_text("ingredient_name\trejected_id\tmim_id\treason\n")
    (claw / "scripts/build_unified_ingredient_mapping.py").write_text("# external fixture producer\n")
    (mim / "src").mkdir()
    (mim / "src/fixture_dependency.py").write_text("VALUE = 1\n")
    canonical = mim / "UNIFIED_INGREDIENT_MAPPING.tsv"
    canonical.write_bytes(tsv([old, other]))
    candidate = root / "evidence/unified-candidate.tsv"
    injected = []

    def command(argv, **kwargs):
        if "build_unified_ingredient_mapping.py" in argv[1]:
            candidate.write_bytes(tsv([new, other]))
        elif case == "candidate_during_checker":
            candidate.write_bytes(tsv([new, {**other, "occurrence_count": "999"}]))
            injected.append(str(candidate))
        return subprocess.CompletedProcess(argv, 0)

    @contextmanager
    def reserve(log, *, backup_paths):
        with original_reserve(log, backup_paths=backup_paths) as handles:
            if case == "candidate_after_validation":
                candidate.write_bytes(tsv([new, {**other, "occurrence_count": "999"}]))
                injected.append(str(candidate))
            elif case == "new_input_after_snapshot":
                extra = culture / "data/normalized_yaml/new-medium.yaml"
                extra.write_text("name: fixture medium\ningredients:\n- name: Other source ingredient\n  amount: 1 g/L\n")
                injected.append(str(extra))
            elif case in ("new_code_after_snapshot", "changed_code_after_snapshot"):
                extra = mim / "src" / ("new_dependency.py" if case == "new_code_after_snapshot" else "fixture_dependency.py")
                extra.write_text("VALUE = 2\n")
                injected.append(str(extra))
            yield handles

    settings = SimpleNamespace(get_target=lambda name: SimpleNamespace(path=mim.resolve() if name == "mediaingredientmech" else culture.resolve()))
    failure = None
    with patch.object(RepositorySettings, "from_environment", return_value=settings), \
         patch.object(LockManager, "lock", return_value=nullcontext()), \
         patch.object(subprocess, "run", side_effect=command), \
         patch.object(subprocess, "check_output", side_effect=lambda argv, **kw: "" if "status" in argv else "0" * 40 + "\n"), \
         patch.object(receipts, "reserve_receipt_outputs", reserve), \
         patch.object(sys, "argv", [str(script), "mim", "claw", "evidence"]):
        try:
            runpy.run_path(str(script), run_name="__main__")
        except Exception as exc:
            failure = {"type": type(exc).__name__, "message": str(exc)}
    receipt_path = root / "evidence/unified-generation-receipt.json"
    receipt = json.loads(receipt_path.read_text()) if receipt_path.exists() else None
    canonical_unchanged = canonical.read_bytes() == tsv([old, other])
    if case == "control":
        assert failure is None and receipt["state"] == "complete" and canonical.read_bytes() == tsv([new, other])
    else:
        assert failure and canonical_unchanged
        assert receipt is None or receipt["state"] == "failed"
    results.append({"case": case, "failure": failure, "receipt_state": receipt.get("state") if receipt else None,
                    "injected_paths": injected, "canonical_unchanged": canonical_unchanged,
                    "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest()})
(OUT / "unified-probe-results.json").write_text(json.dumps({"orchestration_sha256": hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),
    "native_publisher_sha256": hashlib.sha256((RUN / "step3-mim/scripts/promote_heptahydrate_ncit.py").read_bytes()).hexdigest(),
    "cases": results, "production_edits": False, "scope": __doc__}, indent=2) + "\n")
print(json.dumps(results, indent=2))
