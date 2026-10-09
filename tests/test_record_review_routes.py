"""Schema-gap diagnostics must hand off to a registered assessed review."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_curate_audit_saves_review_without_changing_scientific_inputs():
    text = (ROOT / ".claude/skills/curate-yaml-record/SKILL.md").read_text()
    metadata = yaml.safe_load(text.split("---", 2)[1])
    assert metadata["metadata"]["version"] == "2.0.0"
    assert "preserves scientific inputs and saves a new structured review" in text


def test_schema_gap_route_delegates_and_preserves_native_axes():
    profile = yaml.safe_load((ROOT / "conf/record_review.yaml").read_text())
    path = ".claude/skills/schema-gap-analysis/SKILL.md"
    assert path in profile["skills"]
    text = (ROOT / path).read_text()
    for name in ("review-yaml-record", "review-yaml-category"):
        assert f".claude/skills/{name}/SKILL.md" in profile["skills"]
        assert f"../{name}/SKILL.md" in text
    for required in (
        "docs/record-reviews.md",
        "reviews/structured/<timestamp>-<slug>/",
        "scripts/record_review.py save --content",
        "schema / instances / process",
        "audit_axis",
        "scientific_review: false",
        "both aggregate and per-record selectors",
        "P1-P4",
        "SSSOM/release gates",
        "separate curation intent",
    ):
        assert required in text
