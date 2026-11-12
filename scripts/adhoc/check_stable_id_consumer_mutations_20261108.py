"""Exercise stable-ID consumer regressions against source copies (#1265, 2026-11-08).

Inputs: current owned source/tests and offline development Python environment.
Outputs: retained copied sources, pytest logs and results.json under a new
repository .temp directory. No live source, record, Git or session writes.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
CASES = (
    ("filename_browser_id", "scripts/browser_export.py", "'record_id': mim_id,", "'record_id': Path(source_file).stem,",
     "tests/test_stable_id_consumers.py::test_browser_uses_stable_identity_and_preserves_mapping_and_alias_search"),
    ("filename_resolver", "scripts/build_pages_site.py", 'page = f"ingredient/{entry.mim_id.replace(\':\', \'_\')}/index.html"',
     'page = f"ingredient/{source.stem}/index.html"',
     "tests/test_public_ingredient_site.py::test_stable_route_survives_label_filename_and_directory_change"),
    ("no_tombstone_resolution", "scripts/build_pages_site.py",
     'target = entry.mim_id if status == "active" else resolve_id(registry, entry.mim_id)', 'target = entry.mim_id',
     "tests/test_public_ingredient_site.py::test_retired_and_merged_ids_keep_tombstones_through_replacement_chain"),
    ("unbound_registry", "scripts/build_pages_site.py", '        REGISTRY_PATH.as_posix(): repo / REGISTRY_PATH,\n', '',
     "tests/test_public_ingredient_site.py::test_registry_and_lifecycle_are_bound_to_site_freshness"),
    ("unbound_lifecycle", "scripts/build_pages_site.py", '        LIFECYCLE_PATH.as_posix(): repo / LIFECYCLE_PATH,\n', '',
     "tests/test_public_ingredient_site.py::test_registry_and_lifecycle_are_bound_to_site_freshness"),
    ("ambiguous_alias_selected", "src/mediaingredientmech/curie.py", 'if len(targets) > 1:', 'if False:',
     "tests/test_stable_id_consumers.py::test_legacy_external_alias_ambiguity_never_selects_a_record"),
    ("subject_ids_from_filenames", "scripts/check_sssom_subject_files.py", '            if verdict:',
     '            if subject[4:] in {path.stem for path in (root / "data/ingredients/unmapped").glob("*.yaml")}:',
     "tests/test_sssom_subject_records.py::test_numeric_subject_survives_filename_and_label_change"),
    ("unresolved_subject_success", "scripts/check_sssom_subject_files.py", '    return 1 if unresolved else 0',
     '    return 0',
     "tests/test_sssom_subject_records.py::test_unknown_subject_exits_nonzero_even_with_matching_filename"),
    ("lifecycle_mapping_transfer", "src/mediaingredientmech/curie.py",
     'self._resolve_reference(s, follow_replacements=False)',
     'self._resolve_reference(s, follow_replacements=True)',
     "tests/test_stable_id_consumers.py::test_lifecycle_redirect_never_transfers_old_mapping_evidence"),
    ("lifecycle_query_equivalence", "src/mediaingredientmech/curie.py",
     'r = self._resolve_reference(mim_curie, follow_replacements=False)',
     'r = self.resolve(mim_curie)',
     "tests/test_stable_id_consumers.py::test_lifecycle_redirect_never_transfers_old_mapping_evidence"),
    ("unbound_visualization_inputs", "scripts/build_pages_site.py",
     'VISUALIZATION_ASSETS = ("data/ingredient_umap.json", "data/ingredient_graph.json")',
     'VISUALIZATION_ASSETS = ()',
     "tests/test_public_ingredient_site.py::test_visualization_source_identity_changes_invalidate_site"),
    ("unbound_visualization_outputs", "scripts/build_pages_site.py",
     'VISUALIZATION_ASSETS = ("data/ingredient_umap.json", "data/ingredient_graph.json")',
     'VISUALIZATION_ASSETS = ()',
     "tests/test_public_ingredient_site.py::test_visualization_output_identity_changes_invalidate_site"),
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.relative_to(ROOT / ".temp")
    output.mkdir(parents=True, exist_ok=False)
    seed = output / "control"
    shutil.copytree(ROOT / "src", seed / "src", ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for relative in [
        "scripts/browser_export.py", "scripts/build_pages_site.py",
        "scripts/check_sssom_subject_files.py", "tests/test_sssom_subject_records.py",
        "tests/test_stable_id_consumers.py", "tests/test_public_ingredient_site.py",
        *[f"docs/{name}" for name in ("index.html", "browser.html", "theme-toggle.js", "map-record-navigation.js", "ingredient_umap.html", "ingredient_graph.html")],
    ]:
        destination = seed / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, destination)
    selected = sorted({case[4] for case in CASES})
    results = []
    for name, relative, old, new, test in [("control", "", "", "", ""), *CASES]:
        tree = seed if name == "control" else output / name
        if name != "control":
            shutil.copytree(seed, tree, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
            path = tree / relative
            original = path.read_text()
            assert original.count(old) == 1, (name, original.count(old))
            path.write_text(original.replace(old, new, 1))
        environment = dict(os.environ, PYTHONPATH=str(tree / "src"), PYTHONDONTWRITEBYTECODE="1")
        command = [sys.executable, "-m", "pytest", "-c", "/dev/null", "-q", *(selected if name == "control" else [test])]
        run = subprocess.run(command, cwd=tree, env=environment, capture_output=True, text=True, timeout=180)
        log = output / f"{name}.log"
        log.write_text(run.stdout + run.stderr)
        expected = run.returncode == 0 if name == "control" else run.returncode == 1 and " failed" in run.stdout
        results.append({"case": name, "exit_code": run.returncode, "expected_result": expected, "log": log.name})
        (output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
        print(json.dumps(results[-1]), flush=True)
        if not expected:
            raise SystemExit(f"Unexpected mutation result: {name}; inspect retained log")


if __name__ == "__main__":
    main()
