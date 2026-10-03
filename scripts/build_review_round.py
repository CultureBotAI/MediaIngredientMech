#!/usr/bin/env python3
"""Build a review-round ledger from YAML review report output.

The per-record YAML review manifest answers "what did this report say about
this record at this content hash?"  A review round answers the next workflow
question: "which report findings should become bundled GitHub issues, and
which later fixes retired them?"  This script snapshots a manifest into that
round shape without touching GitHub.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import subprocess
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "reports" / "yaml_record_review" / "manifest.tsv"
DEFAULT_OUT = ROOT / "reports" / "review_rounds"

SEVERITY_RANK = {"none": 0, "minor": 1, "major": 2, "blocker": 3}
ISSUE_TIER = {"minor": "P2", "major": "P1", "blocker": "P0"}

INPUT_FIELDS = [
    "round_id",
    "report",
    "record_path",
    "record_sha256",
    "reviewed_at",
    "verdict",
    "severity",
    "report_sha256",
    "notes",
]
FINDING_FIELDS = [
    "round_id",
    "finding_id",
    "fingerprint",
    "severity",
    "category",
    "owner_path",
    "record_path",
    "record_sha256",
    "report",
    "summary",
    "recommended_edit",
    "followup_check",
    "status",
]
BUNDLE_FIELDS = [
    "round_id",
    "bundle_id",
    "severity",
    "category",
    "title",
    "owner_area",
    "affected_count",
    "finding_count",
    "finding_ids",
    "status",
    "issue_number",
]
ISSUE_PLAN_FIELDS = [
    "round_id",
    "bundle_id",
    "action",
    "issue_number",
    "title",
    "reason",
    "severity",
    "category",
    "affected_count",
    "finding_count",
]
ISSUES_FIELDS = [
    "round_id",
    "bundle_id",
    "issue_number",
    "issue_url",
    "action",
    "created_at",
    "finding_ids",
]
FIXES_FIELDS = [
    "issue_number",
    "bundle_id",
    "pr_number",
    "merge_commit",
    "fixed_paths",
    "fixed_at",
    "validation",
]
RETIREMENT_FIELDS = [
    "old_finding_id",
    "fingerprint",
    "issue_number",
    "retired_by_report",
    "retired_record_sha256",
    "retired_at",
    "retirement_reason",
]
VALIDATION_FIELDS = ["round_id", "check", "status", "detail"]

PATH_RE = re.compile(
    r"(data/(?:ingredients|curated)/[^\s`)]+?\.yaml|"
    r"mappings/[^\s`)]+?\.tsv|"
    r"scripts/[^\s`)]+?\.py|"
    r"reports/[^\s`)]+?\.(?:tsv|json|md))"
)
FINDING_RE = re.compile(
    r"^\*\*(?P<severity>blocker|major|minor|none)\*\*:?\s*(?P<summary>.+)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ReviewInput:
    round_id: str
    report: str
    record_path: str
    record_sha256: str
    reviewed_at: str
    verdict: str
    severity: str
    report_sha256: str
    notes: str


@dataclass(frozen=True)
class Finding:
    round_id: str
    finding_id: str
    fingerprint: str
    severity: str
    category: str
    owner_path: str
    record_path: str
    record_sha256: str
    report: str
    summary: str
    recommended_edit: str
    followup_check: str
    status: str = "open"


@dataclass(frozen=True)
class Bundle:
    round_id: str
    bundle_id: str
    severity: str
    category: str
    title: str
    owner_area: str
    affected_count: int
    finding_count: int
    finding_ids: str
    status: str = "planned"
    issue_number: str = ""


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def stable_id(prefix: str, *parts: str) -> str:
    content = "\0".join(parts).encode("utf-8")
    return f"{prefix}-{hashlib.sha256(content).hexdigest()[:20]}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text: str) -> str:
    return " ".join(text.casefold().split())


def max_severity(severities: Iterable[str]) -> str:
    return max(severities, key=lambda severity: SEVERITY_RANK.get(severity, 0))


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]) -> None:
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


def markdown_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = defaultdict(list)
    current = ""
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip().casefold()
            continue
        if current:
            sections[current].append(line)
    return dict(sections)


def bullet_items(lines: Sequence[str]) -> list[str]:
    items: list[str] = []
    current: list[str] = []
    for line in lines:
        if line.startswith("- "):
            if current:
                items.append(" ".join(current))
            current = [line[2:].strip()]
        elif current and (line.startswith("  ") or not line.strip()):
            current.append(line.strip())
    if current:
        items.append(" ".join(current))
    return [item.strip() for item in items if item.strip()]


def parsed_report_fields(report: Path) -> tuple[list[tuple[str, str]], list[str], list[str]]:
    sections = markdown_sections(report.read_text(encoding="utf-8"))
    findings: list[tuple[str, str]] = []
    for item in bullet_items(sections.get("findings", [])):
        if item.strip(".").casefold() == "none found":
            continue
        match = FINDING_RE.match(item)
        if match:
            severity = match.group("severity").casefold()
            summary = match.group("summary").strip()
        else:
            severity = ""
            summary = item
        findings.append((severity, summary))
    recommended = [
        item
        for item in bullet_items(sections.get("recommended edits", []))
        if item.strip(".").casefold() != "none"
    ]
    checks = bullet_items(sections.get("follow-up checks", []))
    return findings, recommended, checks


def classify_finding(summary: str, recommended_edit: str) -> str:
    text = f"{summary} {recommended_edit}".casefold()
    if "source_occurrences" in text or "occurrence" in text:
        return "source-occurrence-drift"
    if "sssom" in text and (
        "synonym" in text or "other" in text or "export" in text or "noise" in text
    ):
        return "sssom-other-noise"
    if "component" in text and (
        "missing" in text or "lack" in text or "absent" in text or "no component" in text
    ):
        return "missing-component-partonomy"
    if "provisional" in text or "computational" in text or "unsupported role" in text:
        return "unsupported-role"
    if "kgscan" in text or "stale" in text or "discussion" in text or "notes" in text:
        return "stale-provenance"
    if "cas" in text or "formula" in text or "chemistry" in text:
        return "chemistry-metadata"
    if "curation_history" in text or "timestamp" in text:
        return "curation-history"
    if "exact" in text and (
        "chebi" in text
        or "ontology" in text
        or "salt" in text
        or "hydrate" in text
        or "stereoisomer" in text
    ):
        return "identity-grounding"
    if "unmapped" in text or "no exact ontology" in text:
        return "unresolved-identity"
    if "ingredient_type" in text:
        return "ingredient-type"
    if "synchroniz" in text or "aggregate" in text or "data/curated" in text:
        return "record-synchronization"
    return "record-curation"


def find_owner_path(summary: str, recommended_edit: str, record_path: str) -> str:
    match = PATH_RE.search(f"{summary} {recommended_edit}")
    if match:
        return match.group(1).strip("`")
    return record_path


def owner_area(path: str) -> str:
    if path.startswith("mappings/"):
        return "final-sssom"
    if path.startswith("data/curated/"):
        return "curated-collections"
    if path.startswith("data/ingredients/mapped/"):
        return "mapped-records"
    if path.startswith("data/ingredients/unmapped/"):
        return "unmapped-records"
    return path.split("/", 1)[0]


def read_inputs(manifest: Path, root: Path, round_id: str) -> list[ReviewInput]:
    rows = []
    for row in read_tsv(manifest):
        report_path = root / row["report"]
        if not report_path.exists():
            raise FileNotFoundError(f"manifest references missing report: {row['report']}")
        rows.append(
            ReviewInput(
                round_id=round_id,
                report=row["report"],
                record_path=row["path"],
                record_sha256=row["record_sha256"],
                reviewed_at=row["reviewed_at"],
                verdict=row["verdict"],
                severity=row["severity"] or "none",
                report_sha256=sha256(report_path),
                notes=row.get("notes", ""),
            )
        )
    return rows


def findings_from_inputs(inputs: Sequence[ReviewInput], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for item in inputs:
        if SEVERITY_RANK.get(item.severity, 0) == 0:
            continue
        report = root / item.report
        parsed_findings, recommended, checks = parsed_report_fields(report)
        if not parsed_findings:
            parsed_findings = [(item.severity, item.notes.strip())]
        for index, (severity, summary) in enumerate(parsed_findings, start=1):
            severity = severity or item.severity
            summary = summary.strip()
            if not summary:
                continue
            recommended_edit = recommended[0] if recommended else ""
            followup_check = checks[0] if checks else ""
            category = classify_finding(summary, recommended_edit)
            owner = find_owner_path(summary, recommended_edit, item.record_path)
            finding_id = stable_id(
                "RF",
                item.report,
                item.record_sha256,
                str(index),
                summary,
            )
            fingerprint = stable_id(
                "RFP",
                category,
                owner,
                item.record_path,
                normalized(summary),
            )
            findings.append(
                Finding(
                    round_id=item.round_id,
                    finding_id=finding_id,
                    fingerprint=fingerprint,
                    severity=severity,
                    category=category,
                    owner_path=owner,
                    record_path=item.record_path,
                    record_sha256=item.record_sha256,
                    report=item.report,
                    summary=summary,
                    recommended_edit=recommended_edit,
                    followup_check=followup_check,
                )
            )
    return findings


def bundle_findings(round_id: str, findings: Sequence[Finding]) -> list[Bundle]:
    grouped: dict[tuple[str, str], list[Finding]] = defaultdict(list)
    for finding in findings:
        grouped[(finding.category, owner_area(finding.owner_path))].append(finding)

    bundles = []
    for (category, area), items in sorted(grouped.items()):
        severity = max_severity(item.severity for item in items)
        tier = ISSUE_TIER.get(severity, "P2")
        affected = sorted({item.record_path for item in items})
        bundle_id = stable_id("RB", category, area)
        title = f"[{tier}] {category.replace('-', ' ')} in {len(affected)} {area} record(s)"
        bundles.append(
            Bundle(
                round_id=round_id,
                bundle_id=bundle_id,
                severity=severity,
                category=category,
                title=title,
                owner_area=area,
                affected_count=len(affected),
                finding_count=len(items),
                finding_ids=",".join(sorted(item.finding_id for item in items)),
            )
        )
    return bundles


def md_escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render_issue_body(
    bundle: Bundle,
    findings: Sequence[Finding],
    max_rows: int = 25,
) -> str:
    ordered = sorted(
        findings,
        key=lambda item: (
            -SEVERITY_RANK.get(item.severity, 0),
            item.record_path,
            item.finding_id,
        ),
    )
    rows = [
        "| Severity | Record | Report | Finding |",
        "| --- | --- | --- | --- |",
    ]
    for finding in ordered[:max_rows]:
        rows.append(
            "| "
            f"{finding.severity} | "
            f"`{md_escape_cell(finding.record_path)}` | "
            f"`{md_escape_cell(finding.report)}` | "
            f"{md_escape_cell(finding.summary)} |"
        )
    if len(ordered) > max_rows:
        rows.append(
            f"| ... | ... | ... | {len(ordered) - max_rows} additional finding(s) "
            "are tracked in `findings.tsv`. |"
        )

    checks = sorted({finding.followup_check for finding in ordered if finding.followup_check})
    check_lines = "\n".join(f"- {check}" for check in checks[:10]) or "- See `findings.tsv`."
    fingerprints = "\n".join(sorted({finding.fingerprint for finding in ordered}))

    return f"""## Summary

Review round `{bundle.round_id}` grouped {bundle.finding_count} `{bundle.category}`
finding(s) across {bundle.affected_count} `{bundle.owner_area}` record(s).

{chr(10).join(rows)}

## Follow-up Checks

{check_lines}

## Tracking

- Bundle: `{bundle.bundle_id}`
- Category: `{bundle.category}`
- Severity: `{bundle.severity}`

<!-- mim-review-round: {bundle.round_id} -->
<!-- mim-review-bundle: {bundle.bundle_id} -->
<!-- mim-fingerprints:
{fingerprints}
-->
"""


def render_issue_plan(bundles: Sequence[Bundle]) -> str:
    rows = [
        "# Review Round Issue Plan",
        "",
        "| Action | Severity | Bundle | Affected | Findings | Title |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]
    for bundle in sorted(
        bundles,
        key=lambda item: (
            -SEVERITY_RANK.get(item.severity, 0),
            item.category,
            item.bundle_id,
        ),
    ):
        rows.append(
            "| create | "
            f"{bundle.severity} | "
            f"`{bundle.bundle_id}` | "
            f"{bundle.affected_count} | "
            f"{bundle.finding_count} | "
            f"{md_escape_cell(bundle.title)} |"
        )
    rows.append("")
    rows.append(
        "Edit `issue_plan.tsv` after deduplicating against open GitHub issues. "
        "Only create issue bodies for bundles that are still marked `create`."
    )
    rows.append("")
    return "\n".join(rows)


def current_git_commit(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def asdicts(items: Iterable[object]) -> list[dict[str, object]]:
    return [dict(item.__dict__) for item in items]


def build_round(
    *,
    root: Path,
    manifest: Path,
    out_root: Path,
    round_id: str,
    base_commit: str,
    force: bool,
) -> Path:
    out_dir = out_root / round_id
    if out_dir.exists() and not force:
        raise FileExistsError(f"{out_dir} already exists; pass --force to replace ledgers")
    out_dir.mkdir(parents=True, exist_ok=True)

    issue_body_dir = out_dir / "issue_bodies"
    issue_body_dir.mkdir(exist_ok=True)

    inputs = read_inputs(manifest, root, round_id)
    findings = findings_from_inputs(inputs, root)
    bundles = bundle_findings(round_id, findings)
    by_finding = {finding.finding_id: finding for finding in findings}

    for bundle in bundles:
        bundled_findings = [
            by_finding[finding_id]
            for finding_id in bundle.finding_ids.split(",")
            if finding_id
        ]
        (issue_body_dir / f"{bundle.bundle_id}.md").write_text(
            render_issue_body(bundle, bundled_findings),
            encoding="utf-8",
        )

    issue_plan = [
        {
            "round_id": bundle.round_id,
            "bundle_id": bundle.bundle_id,
            "action": "create",
            "issue_number": "",
            "title": bundle.title,
            "reason": "new bundled review-output finding cluster",
            "severity": bundle.severity,
            "category": bundle.category,
            "affected_count": bundle.affected_count,
            "finding_count": bundle.finding_count,
        }
        for bundle in bundles
    ]
    validation = [
        {
            "round_id": round_id,
            "check": "input_reports",
            "status": "pass",
            "detail": f"captured {len(inputs)} manifest row(s)",
        },
        {
            "round_id": round_id,
            "check": "findings",
            "status": "pass",
            "detail": f"normalized {len(findings)} open finding(s)",
        },
        {
            "round_id": round_id,
            "check": "bundles",
            "status": "pass",
            "detail": f"planned {len(bundles)} issue bundle(s)",
        },
    ]

    round_doc = {
        "round_id": round_id,
        "kind": "yaml_record_review_issue_planning",
        "base_commit": base_commit,
        "source_manifest": rel(manifest, root),
        "built_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "input_report_count": len(inputs),
        "finding_count": len(findings),
        "bundle_count": len(bundles),
    }

    write_tsv(out_dir / "input_reports.tsv", INPUT_FIELDS, asdicts(inputs))
    write_tsv(out_dir / "findings.tsv", FINDING_FIELDS, asdicts(findings))
    write_tsv(out_dir / "bundles.tsv", BUNDLE_FIELDS, asdicts(bundles))
    write_tsv(out_dir / "issue_plan.tsv", ISSUE_PLAN_FIELDS, issue_plan)
    write_tsv(out_dir / "issues.tsv", ISSUES_FIELDS, [])
    write_tsv(out_dir / "fixes.tsv", FIXES_FIELDS, [])
    write_tsv(out_dir / "retirements.tsv", RETIREMENT_FIELDS, [])
    write_tsv(out_dir / "validation.tsv", VALIDATION_FIELDS, validation)
    (out_dir / "round.yaml").write_text(yaml.safe_dump(round_doc, sort_keys=False), encoding="utf-8")
    (out_dir / "issue_plan.md").write_text(render_issue_plan(bundles), encoding="utf-8")
    return out_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="YAML review manifest to snapshot.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="Directory under which the round subdirectory is written.",
    )
    parser.add_argument(
        "--round-id",
        default=datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ-yaml-review-issues"),
        help="Round directory name.",
    )
    parser.add_argument(
        "--base-commit",
        help="Git commit reviewed by this round; defaults to the current HEAD.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite TSV/YAML ledgers in an existing round directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = args.manifest.resolve()
    root = ROOT
    try:
        out_dir = build_round(
            root=root,
            manifest=manifest,
            out_root=args.out.resolve(),
            round_id=args.round_id,
            base_commit=args.base_commit or current_git_commit(root),
            force=args.force,
        )
    except Exception as exc:
        raise SystemExit(f"error: {exc}") from exc
    try:
        output = out_dir.relative_to(root)
    except ValueError:
        output = out_dir
    print(f"wrote review round to {output}")


if __name__ == "__main__":
    main()
