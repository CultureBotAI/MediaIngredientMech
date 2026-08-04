"""Guards for the agent-instruction rot check (issue #185).

Skills, commands and /goal prompts are executable in practice: an agent reads
them and does what they say, so when they drift they fail silently. This check is
the mechanical version of noticing. Its own failure modes matter as much as its
successes — a docs check that cries wolf gets switched off, and one that cannot
fire is decoration.
"""

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "check_instruction_refs", ROOT / "scripts" / "check_instruction_refs.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _doc(tmp_path: Path, body: str, name: str = "SKILL.md") -> Path:
    path = tmp_path / name
    path.write_text(body)
    return path


RECIPES = {"qc", "sync-curated", "export-individual"}


# --- it must fire on real rot ------------------------------------------------


def test_flags_a_recipe_that_does_not_exist(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Run `just no-such-recipe` afterwards.\n")

    findings = mod.scan_file(doc, tmp_path, RECIPES)

    assert [(f.kind, f.ref) for f in findings] == [("recipe", "no-such-recipe")]


def test_flags_a_path_that_does_not_exist(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Then read `scripts/imaginary_helper.py` for details.\n")

    findings = mod.scan_file(doc, tmp_path, RECIPES)

    assert [(f.kind, f.ref) for f in findings] == [("path", "scripts/imaginary_helper.py")]


def test_flags_references_inside_fenced_blocks(tmp_path):
    """Most command references in these docs live in fenced blocks, not spans."""
    mod = _load()
    doc = _doc(tmp_path, "```bash\njust no-such-recipe\n```\n")

    findings = mod.scan_file(doc, tmp_path, RECIPES)

    assert [f.ref for f in findings] == ["no-such-recipe"]


# --- it must NOT cry wolf ----------------------------------------------------


def test_prose_saying_just_is_not_a_recipe_reference(tmp_path):
    """"...just the collection" must not be read as `just the`. A docs check that
    reports English as breakage is a docs check people turn off."""
    mod = _load()
    doc = _doc(tmp_path, "This rewrites just the collection, not the records.\n")

    assert mod.scan_file(doc, tmp_path, RECIPES) == []


def test_bare_filename_in_prose_is_not_a_path_claim(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Check `mapped_ingredients.yaml` for the header counts.\n")

    assert mod.scan_file(doc, tmp_path, RECIPES) == []


def test_existing_recipe_and_path_are_clean(tmp_path):
    mod = _load()
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "real.py").write_text("")
    doc = _doc(tmp_path, "Run `just qc`, then read `scripts/real.py`.\n")

    assert mod.scan_file(doc, tmp_path, RECIPES) == []


def test_path_relative_to_the_document_resolves(tmp_path):
    """Skills reference their own reference/*.md relatively, not from repo root."""
    mod = _load()
    skill_dir = tmp_path / ".claude" / "skills" / "demo"
    (skill_dir / "reference").mkdir(parents=True)
    (skill_dir / "reference" / "detail.md").write_text("")
    doc = _doc(skill_dir, "See `reference/detail.md`.\n")

    assert mod.scan_file(doc, tmp_path, RECIPES) == []


def test_inline_suppression_silences_a_line(tmp_path):
    mod = _load()
    doc = _doc(
        tmp_path,
        f"Write it to `data/curation/todo.yaml` {mod.INLINE_SUPPRESS}\n",
    )

    assert mod.scan_file(doc, tmp_path, RECIPES) == []


# --- the shipped configuration must actually be enforcing --------------------


def test_repo_config_is_enforcing_and_every_exception_has_a_reason():
    """An unexplained ignore entry is indistinguishable from the rot this
    detects, and `severity: warn` over a clean corpus is decoration."""
    import yaml

    cfg = yaml.safe_load((ROOT / "conf" / "instruction_refs.yaml").read_text())

    assert cfg["severity"] == "error"
    for key in ("ignore_recipes", "ignore_paths"):
        for entry in cfg.get(key) or []:
            assert entry.get("reason", "").strip(), f"{key} entry without a reason: {entry}"


def test_the_real_corpus_is_clean():
    """The check ships green, so any future finding is a real regression."""
    mod = _load()
    cfg_path = ROOT / "conf" / "instruction_refs.yaml"
    assert mod.main(["--config", str(cfg_path)]) == 0
