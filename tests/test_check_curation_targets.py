"""Guards for the curation-target pathspec assertion (issue #181).

The curation-history advisory COUNTS how many curation targets a PR changed; it
never asserts. So a pathspec matching nothing yields 0 and the job reports "no
curation records changed" — the check reads healthiest exactly when it has
stopped working. `data/custom/*.yaml` matched zero tracked files for its whole
life for this reason (#180).
"""

import importlib.util
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent


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
    specs_file.write_text(
        "# a comment\n\ntargets: data/one/**\n   \n  # indented\ntargets: data/two\n"
    )

    assert mod.load_specs(specs_file) == ["data/one/**", "data/two"]


def test_roles_partition_the_list(tmp_path):
    """`targets` drives the changed-count; `history` counts ADDED records. Mixing
    them would make every history-adding PR register as a curation change."""
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("targets: data/one/**\nhistory: history/**/*.yaml\n")

    assert mod.load_specs(specs_file, "targets") == ["data/one/**"]
    assert mod.load_specs(specs_file, "history") == ["history/**/*.yaml"]
    assert len(mod.load_specs(specs_file)) == 2  # the assertion covers both


def test_an_empty_list_exits_2_not_1(tmp_path):
    """Exit 2 = broken config, 1 = a real finding. Collapsing them would make a
    missing config indistinguishable from a dead pathspec."""
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("# only comments\n")

    try:
        mod.load_specs(specs_file)
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("an empty spec list must not be accepted silently")


def test_a_malformed_line_exits_2(tmp_path):
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("data/one/**\n")  # missing the `role:` prefix

    try:
        mod.load_specs(specs_file)
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("a line without a role must not be accepted")


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
    specs_file.write_text("targets: data/curated/*.yaml\ntargets: data/custom/*.yaml\n")

    assert mod.main(["--specs", str(specs_file)]) == 1


def test_flat_vs_nested_is_the_distinction_that_bites():
    """`**/` needs an intervening directory level, so the nested form matches
    nothing against a flat tree. This is what #164 was about."""
    mod = _load()
    assert mod.match_count("data/curated/*.yaml", ROOT) > 0
    assert mod.match_count("data/curated/**/*.yaml", ROOT) == 0


def test_a_plain_star_does_cross_a_slash():
    """The converse, pinned because an earlier draft of the docstring claimed the
    opposite: git pathspecs without :(glob) use wildmatch WITHOUT WM_PATHNAME, so
    `*` crosses `/`. There is no 'partial miss' to warn about."""
    mod = _load()
    flat = mod.match_count("data/ingredients/*.yaml", ROOT)
    nested = mod.match_count("data/ingredients/**/*.yaml", ROOT)

    assert flat == nested > 2000


# --- the workflow and the gate must read the same list -----------------------


def test_print_specs_round_trips_through_shell_parsing(capsys):
    """The workflow does `eval set -- $specs`, so the emitted string must parse
    back to exactly the specs — a parity-of-quotes check would not prove that."""
    mod = _load()
    assert mod.main(["--print-specs", "--role", "targets"]) == 0
    out = capsys.readouterr().out.strip()

    expected = mod.load_specs(ROOT / "conf" / "curation_targets.txt", "targets")
    assert shlex.split(out) == expected


def test_print_specs_survives_a_spec_containing_a_quote(tmp_path, capsys):
    """f"'{spec}'" would emit an unparseable string; shlex.quote does not."""
    mod = _load()
    specs_file = tmp_path / "targets.txt"
    specs_file.write_text("targets: it's/a/*.yaml\n")

    assert mod.main(["--specs", str(specs_file), "--print-specs"]) == 0
    assert shlex.split(capsys.readouterr().out.strip()) == ["it's/a/*.yaml"]


def _advisory_step_script() -> str:
    workflow = yaml.safe_load((ROOT / ".github" / "workflows" / "curation-history.yaml").read_text())
    for job in workflow["jobs"].values():
        for step in job["steps"]:
            if "advisory" in str(step.get("name", "")).lower():
                return step["run"]
    raise AssertionError("advisory step not found")


def test_workflow_consumes_the_shared_list_rather_than_its_own_copy():
    """If the workflow re-inlined its pathspecs, the gate would assert a list
    nobody uses — the drift this issue is about. Checking for the OLD literal
    string would only catch a straight revert, so assert instead that no spec
    from the shared file appears verbatim in the step."""
    mod = _load()
    script = _advisory_step_script()
    # Comments legitimately NAME the specs when explaining the history; only
    # executable lines may not carry them. Same prose-vs-code distinction the
    # instruction-reference checker makes.
    code = "\n".join(
        line for line in script.splitlines() if not line.strip().startswith("#")
    )

    assert "check_curation_targets.py --print-specs" in code
    for spec in mod.load_specs(ROOT / "conf" / "curation_targets.txt"):
        assert spec not in code, f"{spec!r} is inlined in the workflow again"


def test_gate_runs_before_the_dependency_install():
    """The gate needs only the stdlib and git; a dependency-install failure must
    not mask it."""
    workflow = yaml.safe_load((ROOT / ".github" / "workflows" / "curation-history.yaml").read_text())
    names = [str(s.get("name", "")) for s in workflow["jobs"]["history"]["steps"]]
    gate = next(i for i, n in enumerate(names) if "pathspecs still match" in n)
    install = next(i for i, n in enumerate(names) if n == "Install uv")

    assert gate < install


def test_workflow_triggers_on_its_own_config_and_script():
    """A PR editing only the spec list must fire this workflow. Otherwise it
    merges green and the next unrelated curation PR fails the gate — a hole
    shaped exactly like the bug the gate prevents."""
    workflow = yaml.safe_load((ROOT / ".github" / "workflows" / "curation-history.yaml").read_text())
    paths = workflow[True]["pull_request"]["paths"]

    assert "conf/curation_targets.txt" in paths
    assert "scripts/check_curation_targets.py" in paths


def test_every_shipped_spec_contributes_matches():
    """`> 2000` would pass on the ingredient corpus alone even if every other
    spec were deleted. Assert each one individually instead."""
    mod = _load()
    specs = mod.load_specs(ROOT / "conf" / "curation_targets.txt")

    assert len(specs) == 5
    for spec in specs:
        assert mod.match_count(spec, ROOT) > 0, f"{spec} matches nothing"
