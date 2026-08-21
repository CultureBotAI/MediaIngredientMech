"""Hermetic tests for curation report generation and rendering."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export.report_generator import (
    collect_curation_history,
    compute_curator_progress,
    compute_statistics,
    generate_report,
    load_curated_data,
    load_yaml,
    report_to_json,
    report_to_markdown,
)


@pytest.fixture
def curated_payloads() -> tuple[dict, dict]:
    mapped = {
        "mapped_ingredients": [
            {
                "preferred_term": "glucose",
                "ontology_source": "CHEBI",
                "mapping_quality": "EXACT_MATCH",
                "curation_history": [
                    {
                        "timestamp": "2026-08-18T12:00:00Z",
                        "curator": "alice",
                        "action": "MAPPED",
                    },
                    {
                        "timestamp": "2026-08-20T12:00:00Z",
                        "curator": "bob",
                        "action": "VALIDATED",
                    },
                ],
            },
            {
                "preferred_term": "yeast extract",
                "ontology_source": "FOODON",
                "mapping_quality": "CLOSE_MATCH",
                "curation_history": [
                    {"action": "REVIEWED"},
                    {"timestamp": "2026-08-19T12:00:00Z", "action": "UPDATED"},
                ],
            },
            {"preferred_term": "unknown defaults"},
        ],
        "summary_by_category": [
            {"category": "SIMPLE_CHEMICAL", "unique_mapped_count": 2},
            {"unique_mapped_count": 1},
        ],
        "total_instances": 17,
    }
    unmapped = {
        "unmapped_ingredients": [
            {"mapping_status": "UNMAPPED"},
            {"mapping_status": "NEEDS_EXPERT"},
            {},
        ],
        "summary_by_category": [
            {"category": "UNKNOWN", "unique_unmapped_count": 2},
            {"unique_unmapped_count": 1},
        ],
        "media_count": 9,
    }
    return mapped, unmapped


def test_load_yaml_handles_missing_empty_non_mapping_and_mapping(tmp_path: Path) -> None:
    missing = tmp_path / "missing.yaml"
    assert load_yaml(missing) is None

    empty = tmp_path / "empty.yaml"
    empty.write_text("", encoding="utf-8")
    assert load_yaml(empty) is None

    sequence = tmp_path / "sequence.yaml"
    sequence.write_text("- not\n- a mapping\n", encoding="utf-8")
    assert load_yaml(sequence) is None

    mapping = tmp_path / "mapping.yaml"
    mapping.write_text("mapped_ingredients: []\n", encoding="utf-8")
    assert load_yaml(mapping) == {"mapped_ingredients": []}


def test_load_curated_data_reads_expected_filenames(
    tmp_path: Path, curated_payloads: tuple[dict, dict]
) -> None:
    mapped, unmapped = curated_payloads
    (tmp_path / "mapped_ingredients.yaml").write_text(yaml.safe_dump(mapped), encoding="utf-8")
    (tmp_path / "unmapped_ingredients.yaml").write_text(yaml.safe_dump(unmapped), encoding="utf-8")

    assert load_curated_data(tmp_path) == (mapped, unmapped)


def test_compute_statistics_covers_distributions_and_defaults(
    curated_payloads: tuple[dict, dict],
) -> None:
    stats = compute_statistics(*curated_payloads)

    assert stats == {
        "total_ingredients": 6,
        "total_mapped": 3,
        "total_unmapped": 3,
        "mapping_percentage": 50.0,
        "ontology_distribution": {"CHEBI": 1, "FOODON": 1, "UNKNOWN": 1},
        "quality_distribution": {"EXACT_MATCH": 1, "CLOSE_MATCH": 1, "UNKNOWN": 1},
        "unmapped_status_distribution": {"UNMAPPED": 2, "NEEDS_EXPERT": 1},
        "mapped_category_distribution": {"SIMPLE_CHEMICAL": 2, "UNKNOWN": 1},
        "unmapped_category_distribution": {"UNKNOWN": 1},
        "mapped_total_instances": 17,
        "unmapped_media_count": 9,
    }


def test_compute_statistics_handles_absent_data() -> None:
    stats = compute_statistics(None, None)

    assert stats["total_ingredients"] == 0
    assert stats["mapping_percentage"] == 0.0
    assert stats["ontology_distribution"] == {}
    assert stats["mapped_total_instances"] == 0
    assert stats["unmapped_media_count"] == 0


def test_collect_history_sorts_limits_copies_and_labels_ingredients(
    curated_payloads: tuple[dict, dict],
) -> None:
    mapped, _ = curated_payloads

    events = collect_curation_history(mapped, limit=3)

    assert [event.get("timestamp") for event in events] == [
        "2026-08-20T12:00:00Z",
        "2026-08-19T12:00:00Z",
        "2026-08-18T12:00:00Z",
    ]
    assert [event["ingredient"] for event in events] == [
        "glucose",
        "yeast extract",
        "glucose",
    ]
    assert "ingredient" not in mapped["mapped_ingredients"][0]["curation_history"][0]
    assert collect_curation_history(None) == []


def test_compute_curator_progress_counts_missing_curator(
    curated_payloads: tuple[dict, dict],
) -> None:
    mapped, _ = curated_payloads

    assert compute_curator_progress(mapped) == {"unknown": 2, "alice": 1, "bob": 1}
    assert compute_curator_progress(None) == {}


def test_generate_report_uses_temp_data_and_sets_presence_flags(
    tmp_path: Path, curated_payloads: tuple[dict, dict]
) -> None:
    mapped, _ = curated_payloads
    (tmp_path / "mapped_ingredients.yaml").write_text(yaml.safe_dump(mapped), encoding="utf-8")

    report = generate_report(tmp_path)

    assert datetime.fromisoformat(report["generated_at"]).tzinfo is not None
    assert report["statistics"]["total_mapped"] == 3
    assert report["statistics"]["total_unmapped"] == 0
    assert report["data_files"] == {"mapped_exists": True, "unmapped_exists": False}
    assert report["curation_history"][0]["curator"] == "bob"
    assert report["curator_progress"] == {"unknown": 2, "alice": 1, "bob": 1}


def test_report_to_markdown_renders_all_populated_sections(
    curated_payloads: tuple[dict, dict],
) -> None:
    mapped, unmapped = curated_payloads
    report = {
        "generated_at": "2026-08-20T12:00:00+00:00",
        "statistics": compute_statistics(mapped, unmapped),
        "curation_history": collect_curation_history(mapped, limit=1),
        "curator_progress": compute_curator_progress(mapped),
    }

    markdown = report_to_markdown(report)

    assert markdown.startswith("# MediaIngredientMech Curation Report")
    assert "| Mapping % | 50.0% |" in markdown
    assert "## Ontology Distribution" in markdown
    assert "| CHEBI | 1 |" in markdown
    assert "## Mapping Quality Distribution" in markdown
    assert "## Unmapped Status Distribution" in markdown
    assert "## Curator Progress" in markdown
    assert "## Recent Curation Activity" in markdown
    assert "| 2026-08-20T12:00:00Z | bob | VALIDATED | glucose |" in markdown


def test_report_to_markdown_omits_empty_optional_sections() -> None:
    report = {
        "generated_at": "2026-08-20T12:00:00+00:00",
        "statistics": compute_statistics(None, None),
        "curation_history": [],
        "curator_progress": {},
    }

    markdown = report_to_markdown(report)

    assert "## Overview" in markdown
    assert "## Ontology Distribution" not in markdown
    assert "## Mapping Quality Distribution" not in markdown
    assert "## Unmapped Status Distribution" not in markdown
    assert "## Curator Progress" not in markdown
    assert "## Recent Curation Activity" not in markdown


def test_report_to_json_is_indented_and_stringifies_other_types() -> None:
    encoded = report_to_json({"output": Path("report.md")})

    assert encoded.startswith("{\n  ")
    assert json.loads(encoded) == {"output": "report.md"}
