import csv
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

PATH = Path(__file__).parents[1] / "scripts/build_review_round.py"
SPEC = importlib.util.spec_from_file_location("build_review_round", PATH)
builder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = builder
SPEC.loader.exec_module(builder)


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            [
                "path",
                "verdict",
                "severity",
                "reviewed_at",
                "record_sha256",
                "report",
                "notes",
            ],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def test_build_round_snapshots_reports_and_bundles_issue_bodies(tmp_path):
    report_dir = tmp_path / "reports/yaml_record_review"
    report_dir.mkdir(parents=True)
    bad_report = report_dir / "20261001T000001Z-Glucose.md"
    bad_report.write_text(
        """# YAML Record Review: Glucose

## Findings

- **major**: Final SSSOM still exports an invalid open-chain synonym.
- **minor**: Top-level notes still describe the pre-repair state.

## Recommended Edits

- Fix `data/ingredients/mapped/Glucose.yaml` and rebuild the SSSOM.

## Follow-up Checks

- Re-run `just qc-sssom`.
""",
        encoding="utf-8",
    )
    pass_report = report_dir / "20261001T000002Z-Acetate.md"
    pass_report.write_text(
        """# YAML Record Review: Acetate

## Findings

None found.
""",
        encoding="utf-8",
    )
    manifest = report_dir / "manifest.tsv"
    write_manifest(
        manifest,
        [
            {
                "path": "data/ingredients/mapped/Glucose.yaml",
                "verdict": "needs_curation",
                "severity": "major",
                "reviewed_at": "2026-10-01T00:00:01Z",
                "record_sha256": "abc",
                "report": "reports/yaml_record_review/20261001T000001Z-Glucose.md",
                "notes": "SSSOM synonym noise remains.",
            },
            {
                "path": "data/ingredients/mapped/Acetate.yaml",
                "verdict": "pass",
                "severity": "none",
                "reviewed_at": "2026-10-01T00:00:02Z",
                "record_sha256": "def",
                "report": "reports/yaml_record_review/20261001T000002Z-Acetate.md",
                "notes": "None.",
            },
        ],
    )

    out = builder.build_round(
        root=tmp_path,
        manifest=manifest,
        out_root=tmp_path / "reports/review_rounds",
        round_id="20261001T000000Z-test",
        base_commit="fixture",
        force=False,
    )

    inputs = read_tsv(out / "input_reports.tsv")
    findings = read_tsv(out / "findings.tsv")
    bundles = read_tsv(out / "bundles.tsv")
    issue_plan = read_tsv(out / "issue_plan.tsv")
    round_doc = yaml.safe_load((out / "round.yaml").read_text())

    assert [row["record_path"] for row in inputs] == [
        "data/ingredients/mapped/Glucose.yaml",
        "data/ingredients/mapped/Acetate.yaml",
    ]
    assert len(findings) == 2
    assert {row["category"] for row in findings} == {
        "sssom-other-noise",
        "stale-provenance",
    }
    assert len(bundles) == 2
    assert {row["action"] for row in issue_plan} == {"create"}
    assert round_doc["base_commit"] == "fixture"
    assert round_doc["built_at"].endswith("Z")
    body = next((out / "issue_bodies").glob("*.md")).read_text()
    assert "<!-- mim-review-round: 20261001T000000Z-test -->" in body
    assert "<!-- mim-fingerprints:" in body


def test_legacy_manifest_notes_become_a_fallback_finding(tmp_path):
    report_dir = tmp_path / "reports/yaml_record_review"
    report_dir.mkdir(parents=True)
    report = report_dir / "Glucose.md"
    report.write_text("# `data/ingredients/mapped/Glucose.yaml`\n", encoding="utf-8")
    manifest = report_dir / "manifest.tsv"
    write_manifest(
        manifest,
        [
            {
                "path": "data/ingredients/mapped/Glucose.yaml",
                "verdict": "pass_with_minor_issues",
                "severity": "minor",
                "reviewed_at": "2026-09-16T00:00:01Z",
                "record_sha256": "abc",
                "report": "reports/yaml_record_review/Glucose.md",
                "notes": (
                    "The previous report `reports/yaml_record_review/Glucose.md` "
                    "mentions stale advisory rows."
                ),
            },
        ],
    )

    out = builder.build_round(
        root=tmp_path,
        manifest=manifest,
        out_root=tmp_path / "rounds",
        round_id="legacy",
        base_commit="fixture",
        force=False,
    )

    findings = read_tsv(out / "findings.tsv")
    assert len(findings) == 1
    assert findings[0]["owner_path"] == "data/ingredients/mapped/Glucose.yaml"
    assert findings[0]["category"] == "stale-provenance"


def test_numbered_and_table_findings_are_split(tmp_path):
    report_dir = tmp_path / "reports/yaml_record_review"
    report_dir.mkdir(parents=True)
    report = report_dir / "Glucose.md"
    report.write_text(
        """# YAML Record Review: Glucose

## Findings

1. **major**: `data/ingredients/mapped/Glucose.yaml` lacks a source_occurrences row.
2. **minor**: `mappings/ingredient_mappings.sssom.tsv` still exports synonym noise.

| Severity | Finding | Maintained owner |
| --- | --- | --- |
| blocker | Unsupported role remains | `data/curated/mapped_ingredients.yaml` |

## Recommended Edits

1. Fix `data/ingredients/mapped/Glucose.yaml`.

## Follow-up Checks

1. Run `just qc-sssom`.
""",
        encoding="utf-8",
    )
    manifest = report_dir / "manifest.tsv"
    write_manifest(
        manifest,
        [
            {
                "path": "data/ingredients/mapped/Glucose.yaml",
                "verdict": "needs_curation",
                "severity": "major",
                "reviewed_at": "2026-10-01T00:00:01Z",
                "record_sha256": "abc",
                "report": "reports/yaml_record_review/Glucose.md",
                "notes": "fallback must not collapse the structured findings",
            },
        ],
    )

    out = builder.build_round(
        root=tmp_path,
        manifest=manifest,
        out_root=tmp_path / "rounds",
        round_id="structured",
        base_commit="fixture",
        force=False,
    )

    findings = read_tsv(out / "findings.tsv")
    assert [finding["severity"] for finding in findings] == ["major", "minor", "blocker"]
    assert {finding["category"] for finding in findings} == {
        "source-occurrence-drift",
        "sssom-other-noise",
        "unsupported-role",
    }
    assert "data/curated/mapped_ingredients.yaml" in {
        finding["owner_path"] for finding in findings
    }


def test_none_found_suppresses_manifest_fallback(tmp_path):
    report_dir = tmp_path / "reports/yaml_record_review"
    report_dir.mkdir(parents=True)
    report = report_dir / "Glucose.md"
    report.write_text(
        """# YAML Record Review: Glucose

## Findings

None found.
""",
        encoding="utf-8",
    )
    manifest = report_dir / "manifest.tsv"
    write_manifest(
        manifest,
        [
            {
                "path": "data/ingredients/mapped/Glucose.yaml",
                "verdict": "needs_curation",
                "severity": "major",
                "reviewed_at": "2026-10-01T00:00:01Z",
                "record_sha256": "abc",
                "report": "reports/yaml_record_review/Glucose.md",
                "notes": "fallback must not be used",
            },
        ],
    )

    out = builder.build_round(
        root=tmp_path,
        manifest=manifest,
        out_root=tmp_path / "rounds",
        round_id="none-found",
        base_commit="fixture",
        force=False,
    )

    assert read_tsv(out / "findings.tsv") == []


def test_forced_rebuild_removes_stale_issue_bodies(tmp_path):
    report_dir = tmp_path / "reports/yaml_record_review"
    report_dir.mkdir(parents=True)
    report = report_dir / "Glucose.md"
    report.write_text(
        """# YAML Record Review: Glucose

## Findings

- **major**: `data/ingredients/mapped/Glucose.yaml` lacks a source_occurrences row.
""",
        encoding="utf-8",
    )
    manifest = report_dir / "manifest.tsv"
    write_manifest(
        manifest,
        [
            {
                "path": "data/ingredients/mapped/Glucose.yaml",
                "verdict": "needs_curation",
                "severity": "major",
                "reviewed_at": "2026-10-01T00:00:01Z",
                "record_sha256": "abc",
                "report": "reports/yaml_record_review/Glucose.md",
                "notes": "source occurrences remain stale",
            },
        ],
    )
    out_root = tmp_path / "rounds"
    out = builder.build_round(
        root=tmp_path,
        manifest=manifest,
        out_root=out_root,
        round_id="force",
        base_commit="fixture",
        force=False,
    )
    stale_body = out / "issue_bodies" / "RB-stale.md"
    stale_body.write_text("obsolete", encoding="utf-8")

    with pytest.raises(FileExistsError):
        builder.build_round(
            root=tmp_path,
            manifest=manifest,
            out_root=out_root,
            round_id="force",
            base_commit="fixture",
            force=False,
        )
    builder.build_round(
        root=tmp_path,
        manifest=manifest,
        out_root=out_root,
        round_id="force",
        base_commit="fixture",
        force=True,
    )

    assert not stale_body.exists()
