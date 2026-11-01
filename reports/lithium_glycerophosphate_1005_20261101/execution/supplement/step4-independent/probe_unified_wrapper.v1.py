"""Small exact-wrapper/native-producer/publication boundary fixtures; no real writes.

Only fixture repository identity and CLI dispatch are adapted. The real native
builder functions, rejection checker, stamper, publisher and lock execute.
Production CLI identity and full-corpus replay remain root execution checks.
"""
from pathlib import Path
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from types import SimpleNamespace
import hashlib
import importlib.util
import io
import json
import os
import runpy
import shutil
import subprocess
import sys

OWN = Path(__file__).resolve().parent
RUN = OWN.parent
CASE = OWN / "unified-fixture"
ROOT = CASE / "step4-mim"
CULTURE = CASE / "culture-fixture"
CLAW = RUN / "claw-cas-guard"
MIM = RUN / "step4-mim"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(RUN / "guarded_unified_lithium.py") == "b70676c62d8d1e60206a76cd93fe5fc758de7e254ca46db512e3c7516fbc037a"
CASE.mkdir(exist_ok=False)
ROOT.mkdir()
for rel in ("scripts/promote_heptahydrate_ncit.py", "scripts/check_unified_freshness.py", "scripts/check_unified_rejections.py", "data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml"):
    p = ROOT / rel; p.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(MIM / rel, p)
(ROOT / "data/ingredients/unmapped").mkdir()
(ROOT / "docs/data").mkdir(parents=True)
(ROOT / "docs/data/label_index.csv").write_text("label,identifier,preferred_term,mapping_status,ambiguity\n")
(ROOT / "mappings").mkdir()
(ROOT / "mappings/unified_mapping_rejections.tsv").write_text("ingredient_name\trejected_id\tmim_id\treason\n")
(CULTURE / "data/normalized_yaml").mkdir(parents=True)
recipe = CULTURE / "data/normalized_yaml/native_fixture.yaml"
recipe.write_text("id: CultureMech:independent_fixture\ningredients:\n- preferred_term: '#N2'\n- preferred_term: '#Ar'\n")
recipe_before = recipe.read_bytes()
shutil.copyfile(RUN / "guarded_unified_lithium.py", CASE / "guarded_unified_lithium.py")
shutil.copyfile(RUN / "approved-plan.txt", CASE / "approved-plan.txt")
(CASE / "claw-producer").symlink_to(CLAW, target_is_directory=True)
spec = importlib.util.spec_from_file_location("independent_unified_native", CLAW / "scripts/build_unified_ingredient_mapping.py")
native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)

def build(target):
    names, chebis, ontologies = native.load_mim_index(ROOT)
    labels = native.load_mim_label_index(ROOT)
    rejected = native.load_mapping_rejections(ROOT, names, label_index=labels,
        live=native.live_records(names, chebis, ontologies))
    occurrences = native.scan_culturemech(CULTURE)
    native.write_tsv(native.build_unified_rows(occurrences, names, chebis, ontologies, rejected, labels), target)

canonical = ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv"
build(canonical)
canonical_before = canonical.read_bytes()
assert b"#N2\t" in canonical_before and b"#Ar\t" in canonical_before
provenance = ROOT / "UNIFIED_INGREDIENT_MAPPING.provenance.json"
provenance_before = b'{"fixture_unstamped": true}\n'
provenance.write_bytes(provenance_before)
original_env = dict(os.environ)
os.environ.update(MEDIAINGREDIENTMECH_ROOT=str(ROOT), CULTUREMECH_ROOT=str(CULTURE),
                  OPENCLAW_WORKSPACE=str(CASE / "workspace"), PYTHONDONTWRITEBYTECODE="1")
from plugins.repository_settings import RepositorySettings
from mediaingredientmech.curate import apply_receipt
original_settings = RepositorySettings.from_environment
original_run = subprocess.run
original_output = subprocess.check_output
original_reserve = apply_receipt.reserve_receipt_outputs
RepositorySettings.from_environment = classmethod(lambda cls: SimpleNamespace(
    get_target=lambda name: SimpleNamespace(path=ROOT if name == "mediaingredientmech" else CULTURE)))

def dispatched(argv, *args, **kwargs):
    if len(argv) > 1 and str(argv[1]).endswith("build_unified_ingredient_mapping.py"):
        build(Path(argv[argv.index("--output") + 1]))
        return subprocess.CompletedProcess(argv, 0)
    return original_run(argv, *args, **kwargs)

def context_git(argv, *args, **kwargs):
    if argv == ["git", "rev-parse", "HEAD"] and kwargs.get("cwd") in (ROOT, CULTURE):
        return "ISOLATED_FIXTURE_NO_GIT_REVISION\n"
    return original_output(argv, *args, **kwargs)

subprocess.run = dispatched
subprocess.check_output = context_git
results = {"wrapper_sha256": sha(CASE / "guarded_unified_lithium.py"), "fixture_only": True,
           "limited_adaptations": ["RepositorySettings identity is a fixture proxy, not a real Git attestation", "CLI builder dispatch invokes unmodified native builder functions on tiny inputs"], "cases": {}}
try:
    for case in ("positive", "candidate_drift", "new_input_record", "culture_input_drift"):
        provenance.write_bytes(provenance_before)
        evidence = CASE / case
        injected = ROOT / "data/ingredients/unmapped/New_ignored_input.yaml"
        @contextmanager
        def boundary(*args, **kwargs):
            with original_reserve(*args, **kwargs) as handles:
                if case == "candidate_drift":
                    path = evidence / "unified-candidate.tsv"
                    path.write_bytes(path.read_bytes() + b"\n")
                elif case == "new_input_record":
                    injected.write_text("identifier: UNMAPPED_FIXTURE\npreferred_term: fixture\nmapping_status: UNMAPPED\n")
                elif case == "culture_input_drift":
                    recipe.write_bytes(recipe_before + b"\n")
                yield handles
        apply_receipt.reserve_receipt_outputs = boundary
        stream = io.StringIO()
        sys.argv = [str(CASE / "guarded_unified_lithium.py"), "step4-mim", "claw-producer", case]
        error = None
        try:
            with redirect_stdout(stream), redirect_stderr(stream):
                runpy.run_path(str(CASE / "guarded_unified_lithium.py"), run_name="__main__")
        except Exception as exc:
            error = type(exc).__name__ + ": " + str(exc)
        (OWN / ("unified-" + case + ".log")).write_text(stream.getvalue() + (error or "") + "\n")
        assert canonical.read_bytes() == canonical_before
        if case == "positive":
            assert error is None, error
            receipt = json.loads((evidence / "unified-generation-receipt.json").read_bytes())
            stamp = json.loads(provenance.read_bytes())
            assert receipt["canonical_written"] is False and receipt["rows"] == stamp["artifact_rows"] == 2
            assert receipt["before_sha256"] == receipt["after_sha256"] == sha(canonical)
        else:
            assert error is not None and provenance.read_bytes() == provenance_before
        results["cases"][case] = {"expected_failure": case != "positive", "error": error,
                                  "canonical_unchanged": True, "provenance_changed": provenance.read_bytes() != provenance_before}
        if injected.exists(): injected.unlink()
        recipe.write_bytes(recipe_before)
finally:
    RepositorySettings.from_environment = original_settings
    subprocess.run, subprocess.check_output = original_run, original_output
    apply_receipt.reserve_receipt_outputs = original_reserve
    os.environ.clear(); os.environ.update(original_env)
results["production_mutations"] = False
results["verdict"] = "PASS_LIMITED_NATIVE_WRAPPER_CONTROLS"
(OWN / "unified-wrapper-controls.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
