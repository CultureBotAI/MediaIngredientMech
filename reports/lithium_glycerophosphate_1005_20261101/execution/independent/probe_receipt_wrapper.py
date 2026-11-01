"""Run the exact Step4 receipt wrapper on an isolated native two-phase fixture."""
from pathlib import Path
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys

OWN = Path(__file__).resolve().parent
RUN = OWN.parent
MIM = RUN / "step4-mim"
BASE = RUN / "step3-mim"
CASE = OWN / "receipt-fixture"
ROOT = CASE / "step4-mim"

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

assert sha(RUN / "make_step4_receipt.py") == "1b907e603d31b3c7f33582ea43ad6ed443b0981a30febe9d5d71f94ce173b4fe"
CASE.mkdir(exist_ok=False)
ROOT.mkdir()
shutil.copytree(MIM / "src", ROOT / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
for rel in (
    "scripts/curate_lithium_glycerophosphate.py", "scripts/promote_heptahydrate_ncit.py",
    "scripts/bump_sssom_header.py", "tests/fixtures/issue1005-before/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml",
):
    target = ROOT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(MIM / rel, target)
reports = Path("reports/sssom_completion_20260921")
for source in [*(BASE / reports / "mapping_changes").glob("*.json"),
               BASE / reports / "mapping_changes/make_receipt.py",
               BASE / reports / "assemble_review.py",
               *(BASE / reports / name for name in ("baseline-mapping-review.json", "trait-synonym-refresh.json", "parent-name-refresh.json"))]:
    target = ROOT / source.relative_to(BASE)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
for rel in ("approved-plan.txt", "make_step4_receipt.py"):
    shutil.copyfile(RUN / rel, CASE / rel)

writer = load("review_fixture_lithium", ROOT / "scripts/curate_lithium_glycerophosphate.py")
for rel in writer.BEFORE:
    target = ROOT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BASE / rel, target)
    assert sha(target) == writer.BEFORE[rel]
app = CASE / "step4-application"
source_log = app / "source-apply.json"
writer.apply_sources(ROOT, MIM / writer.EVIDENCE, source_log, apply=True)

producer = RUN / "claw-cas-guard/scripts/build_mim_ingredient_sssom.py"
sys.path.insert(0, str(producer.parent))
builder = load("review_fixture_native_builder", producer)
rows = builder._row_from_yaml(ROOT / writer.OWNER, {}, {"CHEBI:15978": "native_ontology:chebi"},
    {"CHEBI:15978": ("Glycerol 3-phosphate", ["sn-glycerol 3-(dihydrogen phosphate)"])},
    {"CHEBI:15978": "sn-glycerol 3-phosphate"})
builder.apply_replayed_stamps(rows, builder._load_existing_validation_method(ROOT / writer.SSSOM))
fields, _ = writer.table((ROOT / writer.SSSOM).read_bytes())
out = io.StringIO(newline="")
stream = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
stream.writeheader(); stream.writerows(rows)
candidate = CASE / "native-candidate.tsv"
candidate.write_text(out.getvalue())
writer.promote(ROOT, candidate, source_log, app / "promotion.json", apply=True, candidate_sha256=sha(candidate))
correct_canonical = (ROOT / writer.SSSOM).read_bytes()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", MEDIAINGREDIENTMECH_ROOT=str(ROOT),
           OPENCLAW_WORKSPACE=str(CASE / "workspace"))
env["PYTHONPATH"] = str(ROOT / "src") + ":" + env.get("PYTHONPATH", "")
published = ROOT / reports / "mapping_changes/issue1005-lithium-glycerophosphate-identity.json"
stage = ROOT / "output/step4-receipt-stage"
audit = app / "receipt-publication.json"
results = {"wrapper_sha256": sha(CASE / "make_step4_receipt.py"), "fixture_only": True,
           "native_producer_sha256": sha(producer), "source_writer_sha256": sha(ROOT / "scripts/curate_lithium_glycerophosphate.py"),
           "cases": {}}

def run(label):
    proc = subprocess.run([sys.executable, "-B", str(CASE / "make_step4_receipt.py")], cwd=ROOT,
                          env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (OWN / f"receipt-{label}.log").write_text(proc.stdout)
    results["cases"][label] = {"exit_code": proc.returncode, "published": published.exists(),
       "published_sha256": sha(published) if published.exists() else None,
       "audit_exists": audit.exists(), "log": f"receipt-{label}.log"}
    return proc

def preserve(label):
    saved = CASE / f"saved-{label}"
    saved.mkdir()
    for path in (published, audit):
        if path.exists():
            shutil.move(path, saved / path.name)
    if stage.exists():
        shutil.move(stage, saved / "staged")

positive = run("positive")
assert positive.returncode == 0, positive.stdout
preserve("positive")

audit.write_text("competing audit bytes\n")
collision = run("audit-collision")
assert collision.returncode != 0 and published.exists(), collision.stdout
assert audit.read_text() == "competing audit bytes\n"
results["cases"]["audit-collision"]["finding"] = "Receipt18 was published before the audit output collision was checked."
preserve("audit-collision")

# A same-shape target edit after the valid native promotion: preserve all rows,
# identifiers, predicates and stamps but remove required #390 provenance.
lines = correct_canonical.decode().splitlines(keepends=True)
for index, line in enumerate(lines):
    if line.startswith(writer.SUBJECT + "\t"):
        row = next(csv.DictReader(io.StringIO("\t".join(fields) + "\n" + line), delimiter="\t"))
        if row["object_id"] == writer.PARENT:
            assert row["comment"].startswith("[#390")
            row["comment"] = ""
            out = io.StringIO(newline="")
            csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n").writerow(row)
            lines[index] = out.getvalue()
(ROOT / writer.SSSOM).write_text("".join(lines))
tamper = run("post-promotion-comment-loss")
assert tamper.returncode == 0 and published.exists(), tamper.stdout
results["cases"]["post-promotion-comment-loss"]["finding"] = "Wrapper accepts target comment loss after promotion because it binds only the source receipt."
preserve("post-promotion-comment-loss")
(ROOT / writer.SSSOM).write_bytes(correct_canonical)
results["production_mutations"] = False
(OWN / "receipt-wrapper-results.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
