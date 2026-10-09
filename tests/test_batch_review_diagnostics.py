"""Diagnostic reports must not claim scientific review or count issues as records."""

import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("batch_review_cli", ROOT / "scripts/batch_review.py")
batch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(batch)


def result(*, failed=False):
    return SimpleNamespace(
        summary={"P1": 0, "P2": 0, "P3": 0, "P4": 0},
        all_issues=[],
        all_suggestions=[],
        failed=[{"ingredient": "fixture", "error": "unavailable"}] if failed else [],
    )


def test_empty_issue_list_is_not_zero_reviewed_records(tmp_path):
    report = tmp_path / "diagnostics.json"
    batch.generate_json_report(result(failed=True), report, records_attempted=7)
    metadata = json.loads(report.read_text())["metadata"]
    assert metadata["scientific_review"] is False
    assert metadata["review_status"] == "diagnostic_only"
    assert metadata["total_reviewed"] == 6
    assert metadata["records_attempted"] == 7
    assert metadata["total_issues"] == 0


@pytest.mark.parametrize(
    "renderer,suffix",
    [
        (batch.generate_markdown_report, "md"),
        (batch.generate_html_dashboard, "html"),
    ],
)
def test_clean_diagnostics_are_not_completed_scientific_review(tmp_path, renderer, suffix):
    report = tmp_path / f"diagnostics.{suffix}"
    renderer(result(), report)
    text = report.read_text()
    assert "scientific_review: false" in text
    assert "Not a completed scientific review" in text
    assert "scripts/record_review.py" in text


@pytest.mark.parametrize("records,failed", [([], False), ([{"identifier": "EX:1"}], True)])
def test_empty_or_failed_batch_does_not_succeed(monkeypatch, records, failed):
    monkeypatch.setattr(batch, "load_mapped_ingredients", lambda: records)
    monkeypatch.setattr(
        batch,
        "IngredientReviewer",
        lambda **kwargs: SimpleNamespace(batch_review=lambda *a, **k: result(failed=failed)),
    )
    monkeypatch.setattr(batch.sys, "argv", ["batch_review.py", "--dry-run"])
    assert batch.main() == 1
