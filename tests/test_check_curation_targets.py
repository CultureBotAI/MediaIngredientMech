"""Guards for the curation-target pathspec assertion (issue #181).

The curation-history advisory COUNTS how many curation targets a PR changed; it
never asserts. So a pathspec matching nothing yields 0 and the job reports "no
curation records changed" — the check reads healthiest exactly when it has
stopped working. `data/custom/*.yaml` matched zero tracked files for its whole
life for this reason (#180).
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "check_curation_targets", ROOT / "scripts" / "check_curation_targets.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


# --- parsing the shared list -------------------------------------------------


def test_comments_and_blank_lines_are_ignored(tmp_path):
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("# a comment\n\ndata/one/**\n   \n  # indented comment\ndata/two\n")

    assert mod.load_specs(specs_file) == ["data/one/**", "data/two"]


def test_an_empty_list_is_a_configuration_error(tmp_path):
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("# only comments\n")

    try:
        mod.load_specs(specs_file)
    except SystemExit as exc:
        assert "lists no pathspecs" in str(exc)
    else:
        raise AssertionError("an empty spec list must not be accepted silently")


# --- the assertion itself ----------------------------------------------------


def test_passes_when_every_spec_matches():
    """The shipped list must be green, so any future finding is a regression."""
    mod = _load()
    assert mod.main([]) == 0


def test_fails_on_a_spec_that_matches_nothing(tmp_path):
    """The historical bug, re-injected: data/custom/*.yaml matches nothing
    because that directory holds a .tsv."""
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("data/curated/*.yaml\ndata/custom/*.yaml\n")

    assert mod.main(["--specs", str(specs_file)]) == 1


def test_flat_vs_nested_is_the_distinction_that_bites(tmp_path):
    """`**/` needs an intervening directory level, so the nested form matches
    nothing against a flat tree. This is what #164 was about."""
    mod = _load()
    assert mod.match_count("data/curated/*.yaml", ROOT) > 0
    assert mod.match_count("data/curated/**/*.yaml", ROOT) == 0


# --- the workflow and the gate must read the same list -----------------------


def test_print_specs_emits_a_shell_consumable_list(capsys):
    """The workflow evaluates this; quoting must survive so a `*` is passed to
    git rather than expanded by the shell."""
    mod = _load()
    assert mod.main(["--print-specs"]) == 0
    out = capsys.readouterr().out.strip()

    assert "'data/ingredients/**/*.yaml'" in out
    assert out.count("'") % 2 == 0


def test_workflow_consumes_the_shared_list_rather_than_its_own_copy():
    """If the workflow inlined its own pathspecs again, the gate would assert a
    list nobody uses — which is the drift this issue is about."""
    workflow = (ROOT / ".github" / "workflows" / "curation-history.yaml").read_text()

    assert "check_curation_targets.py --print-specs" in workflow
    # The old inline list must not come back.
    assert "'data/ingredients/**/*.yaml' 'data/curated/*.yaml'" not in workflow


def test_shipped_list_matches_what_the_workflow_would_count():
    """End to end: the specs the gate asserts are the specs git actually uses."""
    mod = _load()
    specs = mod.load_specs(ROOT / "conf" / "curation_targets.txt")
    proc = subprocess.run(
        ["git", "ls-files", "--", *specs], cwd=ROOT, capture_output=True, text=True, check=True
    )

    assert len(proc.stdout.split()) > 2000  # the per-record corpus alone is ~2,257
