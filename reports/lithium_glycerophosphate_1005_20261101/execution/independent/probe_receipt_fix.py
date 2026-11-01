"""Independently re-review #1043/#1044 with the actual repaired wrapper/native gates."""
from pathlib import Path
import csv
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys

OWN = Path(__file__).resolve().parent
RUN = OWN.parent
CASE = OWN / "receipt-fixture"
ROOT = CASE / "step4-mim"
APP = CASE / "step4-application"
OUTPUT = OWN / "receipt-fix-controls"
OUTPUT.mkdir(exist_ok=False)
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
wrapper = RUN / "make_step4_receipt.py"
assert sha(wrapper) == "64e3a3396f61d3892484afb8be1fc748cf6019f422539d196531997d79683717"
shutil.copyfile(CASE / wrapper.name, OUTPUT / "original-wrapper.py")
shutil.copyfile(wrapper, CASE / wrapper.name)
canonical = ROOT / "mappings/ingredient_mappings.sssom.tsv"
baseline = ROOT / "mappings/other_cross_record_baseline.tsv"
candidate = CASE / "native-candidate.tsv"
promotion = APP / "promotion.json"
published = ROOT / "reports/sssom_completion_20260921/mapping_changes/issue1005-lithium-glycerophosphate-identity.json"
stage = ROOT / "output/step4-receipt-stage"
audit = APP / "receipt-publication.json"
originals = {p: p.read_bytes() for p in (canonical, baseline, candidate, promotion)}
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", MEDIAINGREDIENTMECH_ROOT=str(ROOT),
           OPENCLAW_WORKSPACE=str(CASE / "workspace"))
env["PYTHONPATH"] = str(ROOT / "src") + ":" + env.get("PYTHONPATH", "")
argv = [sys.executable, "-B", str(CASE / wrapper.name), "--candidate", str(candidate), "--promotion-log", str(promotion)]
results = {"wrapper_sha256": sha(wrapper), "issues": [1043, 1044], "fixture_only": True, "cases": {}}

def corrupt_row(field):
    lines = canonical.read_text().splitlines(keepends=True)
    header = next(x for x in lines if not x.startswith("#")).rstrip("\n").split("\t")
    for index, line in enumerate(lines):
        if line.startswith("MIM:Sn-Glycerol_3-phosphate_Lithium_Salt\t"):
            row = next(csv.DictReader(io.StringIO("\t".join(header) + "\n" + line), delimiter="\t"))
            if row["object_id"] == "CHEBI:15978":
                row[field] = ""
                out = io.StringIO(newline="")
                csv.DictWriter(out, fieldnames=header, delimiter="\t", lineterminator="\n").writerow(row)
                lines[index] = out.getvalue()
    canonical.write_text("".join(lines))

for case in ("positive", "audit_collision", "comment_loss", "stamp_loss", "baseline_drift", "missing_promotion", "substituted_promotion", "candidate_substitution"):
    assert not published.exists() and not audit.exists() and not stage.exists()
    for path, content in originals.items():
        path.write_bytes(content)
    if case == "audit_collision": audit.write_text("competing audit bytes\n")
    if case == "comment_loss": corrupt_row("comment")
    if case == "stamp_loss": corrupt_row("validation_method")
    if case == "baseline_drift": baseline.write_bytes(originals[baseline] + b"\n")
    if case == "missing_promotion": promotion.unlink()
    if case == "substituted_promotion":
        receipt = json.loads(originals[promotion]); receipt["approval"] = "APPROVED"
        promotion.write_text(json.dumps(receipt))
    if case == "candidate_substitution": candidate.write_bytes(originals[candidate] + b"\n")
    proc = subprocess.run(argv, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    case_dir = OUTPUT / case
    case_dir.mkdir()
    (case_dir / "log.txt").write_text(proc.stdout)
    result = {"exit_code": proc.returncode, "published": published.exists(), "audit": audit.exists()}
    if case == "positive":
        assert proc.returncode == 0 and published.exists() and audit.exists(), proc.stdout
        record = json.loads(audit.read_bytes())
        assert record["promotion_receipt_sha256"] == sha(promotion)
        assert record["candidate_sha256"] == sha(candidate)
        assert record["receipt_sha256"] == sha(published)
    else:
        assert proc.returncode != 0 and not published.exists(), proc.stdout
        if case == "audit_collision":
            assert audit.read_text() == "competing audit bytes\n"
        else:
            assert not audit.exists()
    for path in (published, audit):
        if path.exists(): shutil.move(path, case_dir / path.name)
    if stage.exists(): shutil.move(stage, case_dir / "staged")
    results["cases"][case] = result

for path, content in originals.items(): path.write_bytes(content)
results["verdict"] = "PASS: positive control publishes jointly; all seven negative controls refuse without a new receipt."
results["production_mutations"] = False
(OUTPUT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
