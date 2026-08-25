"""Regression tests for retiring unsafe CultureMech intake paths (#453)."""

from __future__ import annotations

import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path
from types import ModuleType

from mediaingredientmech.import_quality import (
    culturemech_quality_note,
    map_culturemech_quality,
)

_REPO_ROOT = Path(__file__).parent.parent


def _load_script(name: str) -> ModuleType:
    path = _REPO_ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


import_mod = _load_script("import_from_culturemech")
merge_mod = _load_script("merge_culturemech_updates")
prepare_mod = _load_script("prepare_unmapped_for_curation")
enrich_mod = _load_script("enrich_with_concentration_notes")


def test_direct_match_and_unknown_source_quality_remain_provisional():
    assert map_culturemech_quality("DIRECT_MATCH") == "PROVISIONAL"
    assert map_culturemech_quality(None) == "PROVISIONAL"
    assert map_culturemech_quality("UNKNOWN") == "PROVISIONAL"


def test_explicit_source_grades_are_preserved():
    assert map_culturemech_quality("EXACT_MATCH") == "EXACT_MATCH"
    assert map_culturemech_quality("SYNONYM_MATCH") == "SYNONYM_MATCH"
    assert map_culturemech_quality("CAS_RN_LOOKUP") == "CAS_RN_LOOKUP"
    assert map_culturemech_quality("CLOSE_MATCH") == "CLOSE_MATCH"
    assert map_culturemech_quality("MANUAL_CURATION") == "MANUAL_CURATION"


def test_quality_note_explains_ambiguous_direct_match_without_strengthening_it():
    note = culturemech_quality_note(
        "DIRECT_MATCH",
        "PROVISIONAL",
        "HEPES",
        "2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid",
    )

    assert "MIM quality=PROVISIONAL" in note
    assert "aggregate default" in note
    assert "preferred_term='HEPES'" in note


def test_quality_note_preserves_explicit_source_grade():
    note = culturemech_quality_note(
        "SYNONYM_MATCH",
        "SYNONYM_MATCH",
        "NaCl",
        "sodium chloride",
        operation="Proposed",
    )

    assert note == (
        "Proposed from CultureMech pipeline, source quality=SYNONYM_MATCH; "
        "MIM quality=SYNONYM_MATCH"
    )


def _run_retired_script(
    script: str, args: list[str], tmp_path: Path
) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_REPO_ROOT / "scripts" / script), *args],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )


def test_retired_bulk_import_cli_fails_before_reading_or_writing_paths(tmp_path):
    source_dir = tmp_path / "source-does-not-exist"
    output_dir = tmp_path / "curated"
    output_dir.mkdir()
    sentinel = output_dir / "mapped_ingredients.yaml"
    sentinel.write_bytes(b"curated sentinel\n")

    result = _run_retired_script(
        "import_from_culturemech.py",
        ["--source-dir", str(source_dir), "--output-dir", str(output_dir)],
        tmp_path,
    )

    assert result.returncode == 2
    assert "bulk importer is retired" in result.stderr
    assert "No files were read or written" in result.stderr
    assert not source_dir.exists()
    assert sentinel.read_bytes() == b"curated sentinel\n"
    assert list(output_dir.iterdir()) == [sentinel]


def test_retired_merge_cli_fails_before_reading_or_writing_paths(tmp_path):
    sentinel = tmp_path / "mapped_ingredients.yaml"
    sentinel.write_bytes(b"curated sentinel\n")

    result = _run_retired_script(
        "merge_culturemech_updates.py", ["--dry-run", "--verbose"], tmp_path
    )

    assert result.returncode == 2
    assert "merge utility is retired" in result.stderr
    assert "No files were read or written" in result.stderr
    assert sentinel.read_bytes() == b"curated sentinel\n"
    assert list(tmp_path.iterdir()) == [sentinel]


def test_other_retired_intake_writers_fail_before_reading_or_writing(tmp_path):
    sentinel = tmp_path / "mapped_ingredients.yaml"
    sentinel.write_bytes(b"curated sentinel\n")

    invocations = (
        ("prepare_unmapped_for_curation.py", []),
        ("enrich_with_concentration_notes.py", ["--dry-run"]),
    )
    for script, args in invocations:
        result = _run_retired_script(script, args, tmp_path)
        assert result.returncode == 2
        assert "is retired" in result.stderr
        assert "No files were read or written" in result.stderr
        assert sentinel.read_bytes() == b"curated sentinel\n"
        assert list(tmp_path.iterdir()) == [sentinel]


def test_retired_modules_expose_no_conversion_merge_or_file_io_api():
    retired_import_names = (
        "convert_mapped_ingredient",
        "convert_unmapped_ingredient",
        "import_mapped",
        "import_unmapped",
        "load_source",
    )
    retired_merge_names = (
        "archive_ingredient",
        "import_new_ingredient",
        "load_yaml",
        "merge_ingredient",
        "perform_merge",
        "save_yaml",
    )
    retired_prepare_names = (
        "categorize_unmapped",
        "convert_unmapped_ingredient",
        "load_yaml",
        "normalize_term",
        "prepare_unmapped",
        "save_yaml",
    )
    retired_enrich_names = (
        "enrich_ingredient",
        "extract_concentration_notes",
        "load_yaml",
        "normalize_term",
        "perform_enrichment",
        "save_yaml",
    )

    assert [name for name in retired_import_names if hasattr(import_mod, name)] == []
    assert [name for name in retired_merge_names if hasattr(merge_mod, name)] == []
    assert [name for name in retired_prepare_names if hasattr(prepare_mod, name)] == []
    assert [name for name in retired_enrich_names if hasattr(enrich_mod, name)] == []


def test_import_data_recipe_is_environment_independent_and_fail_closed():
    justfile = (_REPO_ROOT / "justfile").read_text(encoding="utf-8")
    recipe = re.search(r"(?m)^import-data:\n(?P<body>(?:    .*\n)+)", justfile)

    assert recipe is not None
    assert "uv run" not in recipe.group("body")
    assert "retired" in recipe.group("body")
    assert "exit 2" in recipe.group("body")

    if shutil.which("just") is not None:
        result = subprocess.run(
            ["just", "import-data"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 2
        assert "bulk import is retired" in result.stderr
        assert "no files were read or written" in result.stderr


def test_maintained_instructions_do_not_advertise_retired_intake_commands():
    files = [
        _REPO_ROOT / "README.md",
        _REPO_ROOT / "docs" / "CURATION_GUIDE.md",
        _REPO_ROOT / "docs" / "WORKFLOWS.md",
        *(_REPO_ROOT / ".claude" / "skills").rglob("*.md"),
    ]
    runnable_instructions = (
        "just import-data",
        "python scripts/import_from_culturemech.py",
        "python3 scripts/import_from_culturemech.py",
        "python scripts/merge_culturemech_updates.py",
        "python3 scripts/merge_culturemech_updates.py",
        "python scripts/prepare_unmapped_for_curation.py",
        "python3 scripts/prepare_unmapped_for_curation.py",
        "python scripts/enrich_with_concentration_notes.py",
        "python3 scripts/enrich_with_concentration_notes.py",
    )
    unsupported_claims = (
        "kgx_export.py",
        "export_to_culturemech.py",
        "import missing high-frequency ingredients",
        "CultureMech import/export scripts",
    )

    violations = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for instruction in (*runnable_instructions, *unsupported_claims):
            if instruction in text:
                violations.append(f"{path.relative_to(_REPO_ROOT)}: {instruction}")

    assert violations == []


def test_historical_integration_note_is_explicitly_superseded():
    note = (_REPO_ROOT / "notes" / "KG-MICROBE-INTEGRATION-SUMMARY.md").read_text(encoding="utf-8")

    assert "Historical snapshot — superseded" in note[:500]
    assert "All four legacy CultureMech intake writers are" in note[:500]
    assert "fail-closed under #453" in note[:500]
