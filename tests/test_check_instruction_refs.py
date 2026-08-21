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


def _scan(mod, doc, root, tracked=frozenset()):
    """scan_file returns (findings, unverifiable); tests mostly want the findings."""
    findings, _ = mod.scan_file(doc, root, RECIPES, set(tracked))
    return findings


# --- it must fire on real rot ------------------------------------------------


def test_flags_a_recipe_that_does_not_exist(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Run `just no-such-recipe` afterwards.\n")

    findings = _scan(mod, doc, tmp_path)

    assert [(f.kind, f.ref) for f in findings] == [("recipe", "no-such-recipe")]


def test_flags_a_path_that_does_not_exist(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Then read `scripts/imaginary_helper.py` for details.\n")

    findings = _scan(mod, doc, tmp_path)

    assert [(f.kind, f.ref) for f in findings] == [("path", "scripts/imaginary_helper.py")]


def test_flags_references_inside_fenced_blocks(tmp_path):
    """Most command references in these docs live in fenced blocks, not spans."""
    mod = _load()
    doc = _doc(tmp_path, "```bash\njust no-such-recipe\n```\n")

    findings = _scan(mod, doc, tmp_path)

    assert [f.ref for f in findings] == ["no-such-recipe"]


def test_flags_an_unsupported_documented_cli_option(tmp_path):
    mod = _load()
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "apply.py").write_text(
        'import click\n@click.command()\n@click.option("--dry-run", is_flag=True)\ndef main(dry_run): pass\n'
    )
    doc = _doc(
        tmp_path,
        "```bash\npython scripts/apply.py --dry-run --validate\n```\n",
    )

    findings = _scan(mod, doc, tmp_path, tracked={"scripts/apply.py"})

    assert [(f.kind, f.command, f.ref) for f in findings] == [
        ("option", "scripts/apply.py", "--validate")
    ]


def test_cli_check_joins_backslash_continuations(tmp_path):
    mod = _load()
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "apply.py").write_text(
        'import argparse\np = argparse.ArgumentParser()\np.add_argument("--suggestions")\n'
    )
    body = "```bash\npython scripts/apply.py " + "\\" + "\n"
    body += "  --suggestions batch.yaml " + "\\" + "\n"
    body += "  --invalid\n```\n"
    doc = _doc(tmp_path, body)

    findings = _scan(mod, doc, tmp_path, tracked={"scripts/apply.py"})

    assert [(f.kind, f.ref) for f in findings] == [("option", "--invalid")]


# --- it must NOT cry wolf ----------------------------------------------------


def test_prose_saying_just_is_not_a_recipe_reference(tmp_path):
    """ "...just the collection" must not be read as `just the`. A docs check that
    reports English as breakage is a docs check people turn off."""
    mod = _load()
    doc = _doc(tmp_path, "This rewrites just the collection, not the records.\n")

    assert _scan(mod, doc, tmp_path) == []


def test_bare_filename_in_prose_is_not_a_path_claim(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Check `mapped_ingredients.yaml` for the header counts.\n")

    assert _scan(mod, doc, tmp_path) == []


def test_existing_recipe_and_tracked_path_are_clean(tmp_path):
    mod = _load()
    doc = _doc(tmp_path, "Run `just qc`, then read `scripts/real.py`.\n")

    assert _scan(mod, doc, tmp_path, tracked={"scripts/real.py"}) == []


def test_a_file_on_disk_but_untracked_does_not_count_as_existing(tmp_path):
    """The property CI taught us. Resolving against the filesystem made the
    result depend on local layout: a sibling ../culturebotai-claw checkout and
    generated artifacts like reports/label_drift.tsv exist on a dev machine and
    not in CI, so the check passed locally and failed in CI. Existence must mean
    tracked in git, or the guard answers differently depending on who runs it."""
    mod = _load()
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "untracked.py").write_text("")
    doc = _doc(tmp_path, "Read `scripts/untracked.py`.\n")

    findings = _scan(mod, doc, tmp_path, tracked=set())

    assert [f.ref for f in findings] == ["scripts/untracked.py"]


def test_out_of_repo_reference_is_counted_not_failed(tmp_path):
    """A ../ path cannot be verified from here. Failing on it would be wrong;
    dropping it silently would hide how much is unchecked, so it is counted."""
    mod = _load()
    doc = _doc(tmp_path, "See `../culturebotai-claw/scripts/build_x.py`.\n")

    findings, unverifiable = mod.scan_file(doc, tmp_path, RECIPES, set())

    assert findings == []
    assert unverifiable == 1


def test_path_relative_to_the_document_resolves(tmp_path):
    """Skills reference their own reference/*.md relatively, not from repo root."""
    mod = _load()
    skill_dir = tmp_path / ".claude" / "skills" / "demo"
    skill_dir.mkdir(parents=True)
    doc = _doc(skill_dir, "See `reference/detail.md`.\n")
    tracked = {".claude/skills/demo/reference/detail.md"}

    assert _scan(mod, doc, tmp_path, tracked=tracked) == []


def test_inline_suppression_silences_a_line(tmp_path):
    mod = _load()
    doc = _doc(
        tmp_path,
        f"Write it to `data/curation/todo.yaml` {mod.INLINE_SUPPRESS}\n",
    )

    assert _scan(mod, doc, tmp_path) == []


# --- the shipped configuration must actually be enforcing --------------------


def test_repo_config_is_enforcing_and_every_exception_has_a_reason():
    """An unexplained ignore entry is indistinguishable from the rot this
    detects, and `severity: warn` over a clean corpus is decoration."""
    import yaml

    cfg = yaml.safe_load((ROOT / "conf" / "instruction_refs.yaml").read_text())

    assert cfg["severity"] == "error"
    assert "CLAUDE.md" in cfg["targets"]
    assert "docs/*CURATION*.md" in cfg["targets"]
    for key in ("ignore_recipes", "ignore_paths"):
        for entry in cfg.get(key) or []:
            assert entry.get("reason", "").strip(), f"{key} entry without a reason: {entry}"


def test_the_real_corpus_is_clean():
    """The check ships green, so any future finding is a real regression."""
    mod = _load()
    cfg_path = ROOT / "conf" / "instruction_refs.yaml"
    assert mod.main(["--config", str(cfg_path)]) == 0


def test_recipe_parsing_needs_no_just_binary_and_finds_parameterised_recipes(tmp_path):
    """Shelling out to `just --list` made the check unrunnable wherever `just`
    is absent — including this repo's own pytest workflow, where it failed for
    exactly that reason. Parsing must also handle recipes with parameters and
    ignore `:=` variable assignments."""
    mod = _load()
    (tmp_path / "justfile").write_text(
        'research_dir := "research"\n'
        "qc: validate-all validate-strict\n"
        "  echo hi\n"
        'apply-role-research-results batch *args="":\n'
        "  echo apply\n"
        "# a comment: not a recipe\n"
    )

    assert mod.known_recipes(tmp_path) == {"qc", "apply-role-research-results"}
