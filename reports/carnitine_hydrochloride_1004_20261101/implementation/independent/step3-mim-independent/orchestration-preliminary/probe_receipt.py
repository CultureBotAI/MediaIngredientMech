"""Native make_receipt and publish_new_files, with external fixture data only."""
from pathlib import Path
from contextlib import nullcontext
from unittest.mock import patch
import csv
import hashlib
import io
import json
import os
import runpy
import sys

from plugins.lock_manager import LockManager
import mediaingredientmech.ingredient_bundle_refresh as refresh

OUT = Path(__file__).resolve().parent
RUN = OUT.parents[1]
MIM = RUN / "step3-mim"
SCRIPT = RUN / "make_step3_receipt.py"
sha = lambda b: hashlib.sha256(b).hexdigest()
names = ["Carnitine_Hydrochloride.yaml", "Carnitine_Dl_Hydrochloride.yaml", "NLDM_metabolites.yaml"]
subjects = {"MIM:Carnitine_Hydrochloride", "MIM:Carnitine_Dl_Hydrochloride", "MIM:NLDM_metabolites"}
all_rows = list(csv.DictReader((x for x in (MIM / "mappings/ingredient_mappings.sssom.tsv").read_text().splitlines() if not x.startswith("#")), delimiter="\t"))
before_rows = [r for r in all_rows if r["subject_id"] in subjects]
assert len(before_rows) == 6
after_rows = [dict(r) for r in before_rows if r["subject_id"] in {"MIM:Carnitine_Hydrochloride", "MIM:NLDM_metabolites"} and not r["object_id"].startswith("kgmicrobe.compound:")]
assert len(after_rows) == 2
for row in after_rows:
    row["mapping_date"] = "2026-11-01"
    if row["subject_id"] == "MIM:Carnitine_Hydrochloride":
        row["object_id"] = "NCIT:C216679"


def table(rows):
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    return buf.getvalue().encode()


real_read = Path.read_bytes
real_publish = refresh.publish_new_files
original_cwd = Path.cwd()
results = []
for case in ("control", "generated_receipt_replaced", "new_chain_member_after_snapshot"):
    root = OUT / "receipt-cases" / case
    mim = root / "step3-mim"
    folder = mim / "reports/sssom_completion_20260921/mapping_changes"
    folder.mkdir(parents=True)
    (root / "step3-application").mkdir()
    (mim / "mappings").mkdir()
    script = root / SCRIPT.name
    script.write_bytes(SCRIPT.read_bytes())
    (folder / "make_receipt.py").write_bytes((MIM / "reports/sssom_completion_20260921/mapping_changes/make_receipt.py").read_bytes())
    old_bytes, new_bytes = table(before_rows), table(after_rows)
    (root / "step3-application/source-apply.before-ingredient_mappings.sssom.tsv").write_bytes(old_bytes)
    (mim / "mappings/ingredient_mappings.sssom.tsv").write_bytes(new_bytes)
    records = []
    for name in names:
        path = Path("data/ingredients/mapped") / name
        target = mim / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((MIM / path).read_bytes())
        records.append({"source_record": str(path), "shape": "external-fixture", "before_yaml_sha256": "historical-fixture",
                        "after_yaml_sha256": sha(target.read_bytes()), "change": "fixture", "verification": "fixture"})
    (root / "step3-application/source-apply.json").write_text(json.dumps({"records": records}))
    for sequence in range(1, 17):
        (folder / f"existing-{sequence:02}.json").write_text(json.dumps({"sequence": sequence, "after_sha256": sha(old_bytes)}))
    generated = mim / "output/step3-receipt-stage/issue1004-carnitine-hydrochloride-merge.json"
    reads = 0

    def read(path):
        global reads
        if path == generated:
            reads += 1
            if case == "generated_receipt_replaced" and reads == 2:
                payload = json.loads(real_read(path)); payload["approval"] = "APPROVED: injected after checks"
                path.write_text(json.dumps(payload))
        return real_read(path)

    def publish(outputs, verify_snapshot):
        if case == "new_chain_member_after_snapshot":
            (folder / "competing-sequence-17.json").write_text(json.dumps({"sequence": 17, "after_sha256": sha(new_bytes)}))
        return real_publish(outputs, verify_snapshot)

    os.chdir(mim)
    try:
        with patch.object(LockManager, "lock", return_value=nullcontext()), patch.object(Path, "read_bytes", read), patch.object(refresh, "publish_new_files", publish):
            runpy.run_path(str(script), run_name="__main__")
    finally:
        os.chdir(original_cwd)
    published = folder / generated.name
    payload = json.loads(published.read_text())
    results.append({"case": case, "published": str(published), "approval": payload["approval"],
                    "sequence17_count": sum(json.loads(p.read_text())["sequence"] == 17 for p in folder.glob("*.json")),
                    "audit_created": (root / "step3-application/receipt-publication.json").exists()})
(OUT / "receipt-probe-results.json").write_text(json.dumps({"helper_sha256": sha(SCRIPT.read_bytes()), "cases": results,
    "native_maker_and_publisher": True, "only_caller_lock_stubbed": True, "production_writes": False}, indent=2) + "\n")
print(json.dumps(results, indent=2))
