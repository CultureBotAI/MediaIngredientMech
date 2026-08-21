"""Configuration guards for the truthful quality and coverage gates."""

from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_coverage_gate_separates_maintained_package_from_legacy_scripts() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    justfile = (ROOT / "justfile").read_text(encoding="utf-8")

    assert '"--cov=mediaingredientmech"' in pyproject
    assert '"--cov=scripts"' in pyproject
    assert "--cov-fail-under" not in pyproject
    assert "--include='src/mediaingredientmech/*' --fail-under=35" in justfile
    script_report = "coverage report --include='scripts/*'"
    assert script_report in justfile
    assert f"{script_report} --fail-under" not in justfile


def test_general_pytest_workflow_enforces_the_same_package_floor() -> None:
    workflow = (ROOT / ".github" / "workflows" / "tests.yaml").read_text(encoding="utf-8")

    assert "--include='src/mediaingredientmech/*' --fail-under=35" in workflow
    assert "coverage report --include='scripts/*'" in workflow
