from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import sys
from plugins.lock_manager import LockManager
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files

ROOT = Path.cwd().resolve()
RUN = Path(__file__).resolve().parent
assert ROOT == RUN / "step2-mim"
folder = ROOT / "reports/sssom_completion_20260921/mapping_changes"
script = folder / "make_receipt.py"
stage = ROOT / "output/step2-receipt-stage"
stage.mkdir(parents=True, exist_ok=False)
batch = "issue875-ncit-exact-heptahydrate"
before = RUN / "step2-application/source-apply.before.sssom.tsv"
apply_log = RUN / "step2-application/source-apply.json"
current = ROOT / "mappings/ingredient_mappings.sssom.tsv"
owner = ROOT / "data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml"
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
with LockManager({"my_id": "codex-approved-plan"}).lock("mediaingredientmech", "mapping_receipt_875"):
    existing = sorted(folder.glob("*.json"))
    receipts = sorted([json.loads(path.read_bytes()) for path in existing], key=lambda r: r["sequence"])
    assert [r["sequence"] for r in receipts] == list(range(1, 16))
    assert receipts[-1]["after_sha256"] == sha(before)
    snapshot = {path: sha(path) for path in [*existing, script, before, apply_log, current, owner]}
    spec = importlib.util.spec_from_file_location("native_make_receipt", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.HERE = stage
    sys.argv = [str(script), "--batch", batch, "--sequence", "16", "--issue",
                "https://github.com/CultureBotAI/MediaIngredientMech/issues/875", "--scope",
                "Exact NCIT heptahydrate identity and removal of obsolete parent/registry rows; unrelated claims remain held.",
                "--before-sssom", str(before), "--apply-log", str(apply_log)]
    module.main()
    generated = stage / (batch + ".json")
    receipt = json.loads(generated.read_bytes())
    assert receipt["changed_rows"] == receipt["removed_rows"] == 1 and receipt["added_rows"] == 0
    assert receipt["touched_subjects"] == ["MIM:Na2hpo4_X_7_H2o"]
    assert receipt["after_row_count"] == receipt["before_row_count"] - 1
    assert receipt["approval"].startswith("NONE:") and len(receipt["records"]) == 1
    assert receipt["records"][0]["after_yaml_sha256"] == sha(owner)
    others = lambda path: [line for line in path.read_bytes().splitlines(keepends=True)
                           if not line.startswith(b"MIM:Na2hpo4_X_7_H2o\t")]
    assert others(before) == others(current), "unrelated SSSOM bytes changed"
    def recheck():
        assert snapshot == {path: sha(path) for path in snapshot}, "receipt inputs changed"
    destination = folder / generated.name
    publish_new_files([(destination, generated.read_bytes())], recheck)
    audit = {"timestamp": datetime.now(timezone.utc).isoformat(), "native_producer": str(script),
             "producer_sha256": sha(script), "published": str(destination), "receipt_sha256": sha(destination),
             "previous_receipts_unchanged": {str(p): snapshot[p] for p in existing},
             "before_sha256": sha(before), "after_sha256": sha(current), "changed": 1, "removed": 1,
             "added": 0, "other_sssom_bytes_identical": True, "scientific_approval_added": False}
    with (RUN / "step2-application/receipt-publication.json").open("x") as stream:
        json.dump(audit, stream, indent=2); stream.write("\n")
    print(json.dumps(audit, indent=2))
