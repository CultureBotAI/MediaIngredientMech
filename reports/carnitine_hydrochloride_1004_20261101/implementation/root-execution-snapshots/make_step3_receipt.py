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
assert ROOT == RUN / "step3-mim"
folder = ROOT / "reports/sssom_completion_20260921/mapping_changes"
script = folder / "make_receipt.py"
stage = ROOT / "output/step3-receipt-stage"
stage.mkdir(parents=True, exist_ok=False)
batch = "issue1004-carnitine-hydrochloride-merge"
before = RUN / "step3-application/source-apply.before-ingredient_mappings.sssom.tsv"
apply_log = RUN / "step3-application/source-apply.json"
current = ROOT / "mappings/ingredient_mappings.sssom.tsv"
owners = [ROOT / "data/ingredients/mapped" / name for name in ("Carnitine_Hydrochloride.yaml", "Carnitine_Dl_Hydrochloride.yaml", "NLDM_metabolites.yaml")]
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
with LockManager({"my_id": "codex-approved-plan"}).lock("mediaingredientmech", "mapping_receipt_1004"):
    existing = sorted(folder.glob("*.json"))
    receipts = sorted([json.loads(path.read_bytes()) for path in existing], key=lambda r: r["sequence"])
    assert [r["sequence"] for r in receipts] == list(range(1, 17))
    assert receipts[-1]["after_sha256"] == sha(before)
    code = [Path(__file__), ROOT / "src/mediaingredientmech/ingredient_bundle_refresh.py",
            ROOT / "src/mediaingredientmech/curate/apply_receipt.py"]
    snapshot = {path: sha(path) for path in [*existing, script, before, apply_log, current, *owners, *code]}
    spec = importlib.util.spec_from_file_location("native_make_receipt", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.HERE = stage
    sys.argv = [str(script), "--batch", batch, "--sequence", "17", "--issue",
                "https://github.com/CultureBotAI/MediaIngredientMech/issues/1004", "--scope",
                "Approved NCIT hydrochloride identity, duplicate tombstone, rejected free aliases, synchronized NLDM component reference and withdrawal of inherited owner approvals; no scientific approval added.",
                "--before-sssom", str(before), "--apply-log", str(apply_log)]
    module.main()
    generated = stage / (batch + ".json")
    generated_bytes = generated.read_bytes()
    receipt = json.loads(generated_bytes)
    snapshot[generated] = hashlib.sha256(generated_bytes).hexdigest()
    assert receipt["changed_rows"] == 2 and receipt["removed_rows"] == 4 and receipt["added_rows"] == 0
    subjects = {"MIM:Carnitine_Hydrochloride", "MIM:Carnitine_Dl_Hydrochloride", "MIM:NLDM_metabolites"}
    assert set(receipt["touched_subjects"]) == subjects
    assert receipt["after_row_count"] == receipt["before_row_count"] - 4
    assert receipt["approval"].startswith("NONE:") and len(receipt["records"]) == 3
    assert {r["source_record"]: r["after_yaml_sha256"] for r in receipt["records"]} == {str(p.relative_to(ROOT)): sha(p) for p in owners}
    def others(path):
        return [line for line in path.read_bytes().splitlines(keepends=True)
                if not any(line.startswith((subject + "\t").encode()) for subject in subjects)
                and not line.startswith((b"# mapping_date:", b"# mapping_set_version:"))]
    assert others(before) == others(current), "unrelated SSSOM bytes changed"
    destination = folder / generated.name
    def recheck():
        assert snapshot == {path: sha(path) for path in snapshot}, "receipt inputs changed"
        present = set(folder.glob("*.json"))
        assert present - {destination} == set(existing), "receipt chain path set changed"
    publish_new_files([(destination, generated_bytes)], recheck)
    assert destination.read_bytes() == generated_bytes, "published receipt differs from validated bytes"
    audit = {"timestamp": datetime.now(timezone.utc).isoformat(), "native_producer": str(script),
             "producer_sha256": sha(script), "published": str(destination), "receipt_sha256": sha(destination),
             "previous_receipts_unchanged": {str(p): snapshot[p] for p in existing},
             "before_sha256": sha(before), "after_sha256": sha(current), "changed": 2, "removed": 4,
             "added": 0, "other_sssom_bytes_identical": True, "scientific_approval_added": False}
    with (RUN / "step3-application/receipt-publication.json").open("x") as stream:
        json.dump(audit, stream, indent=2); stream.write("\n")
    print(json.dumps(audit, indent=2))
