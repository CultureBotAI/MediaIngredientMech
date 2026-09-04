#!/usr/bin/env python3
"""Rank MIM ingredient records by causal-graph readiness.

Faceted role assignments are the ingredient-to-function edges that a causal
graph exporter can use directly. Stock/pre-mix component assertions are
has-part edges. This script scores each individual IngredientRecord YAML by
grounding quality, role coverage, role evidence, and component evidence so the
least graph-ready records can be researched first.

Lower scores need review first:

    just score-causal-graph-readiness
    just score-causal-graph-readiness --status mapped --limit 50
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.utils.role_iteration import (  # noqa: E402
    FACET_ROLE_SLOTS,
    iter_role_assignments,
)

DEFAULT_INGREDIENTS_DIR = ROOT / "data" / "ingredients"
DEFAULT_OUT = ROOT / "reports" / "causal_graph_readiness.tsv"
STATUSES = ("mapped", "unmapped")
COMPONENT_PARENT_TYPES = {"NAMED_MEDIUM", "STOCK_SOLUTION", "UNDEFINED_MIXTURE"}
SAFE_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

FIELDNAMES = [
    "rank",
    "readiness_score",
    "identity_score",
    "role_content_score",
    "role_evidence_score",
    "component_score",
    "path",
    "identifier",
    "preferred_term",
    "mapping_status",
    "mapping_quality",
    "ingredient_type",
    "total_occurrences",
    "role_count",
    "populated_role_facets",
    "best_role_evidence",
    "issues",
]

MAPPING_QUALITY_POINTS = {
    "EXACT_MATCH": 10.0,
    "SYNONYM_MATCH": 9.0,
    "CAS_RN_LOOKUP": 8.0,
    "MANUAL_CURATION": 8.0,
    "CLOSE_MATCH": 6.0,
    "NARROW_MATCH": 5.0,
    "BROAD_MATCH": 5.0,
    "FALLBACK_REGISTRY": 3.0,
    "LEXICAL_MATCH": 2.0,
    "LLM_ASSISTED": 2.0,
    "PROVISIONAL": 1.0,
    "PLACEHOLDER": 0.0,
}

CITATION_TYPE_POINTS = {
    "PEER_REVIEWED_PUBLICATION": 0.45,
    "DATABASE_ENTRY": 0.35,
    "TECHNICAL_REPORT": 0.30,
    "PREPRINT": 0.25,
    "MANUAL_CURATION": 0.20,
    "COMPUTATIONAL_PREDICTION": 0.10,
}


@dataclass(frozen=True)
class ScoreRow:
    path: Path
    identity_score: float
    role_content_score: float
    role_evidence_score: float
    component_score: float
    total_occurrences: int
    role_count: int
    populated_role_facets: int
    best_role_evidence: float
    issues: tuple[str, ...]
    identifier: str
    preferred_term: str
    mapping_status: str
    mapping_quality: str
    ingredient_type: str

    @property
    def readiness_score(self) -> float:
        return round(
            self.identity_score
            + self.role_content_score
            + self.role_evidence_score
            + self.component_score,
            3,
        )

    def to_tsv(self, rank: int, root: Path) -> dict[str, str | int]:
        rel = self.path.relative_to(root) if self.path.is_relative_to(root) else self.path
        return {
            "rank": rank,
            "readiness_score": f"{self.readiness_score:.3f}",
            "identity_score": f"{self.identity_score:.3f}",
            "role_content_score": f"{self.role_content_score:.3f}",
            "role_evidence_score": f"{self.role_evidence_score:.3f}",
            "component_score": f"{self.component_score:.3f}",
            "path": str(rel),
            "identifier": self.identifier,
            "preferred_term": self.preferred_term,
            "mapping_status": self.mapping_status,
            "mapping_quality": self.mapping_quality,
            "ingredient_type": self.ingredient_type,
            "total_occurrences": self.total_occurrences,
            "role_count": self.role_count,
            "populated_role_facets": self.populated_role_facets,
            "best_role_evidence": f"{self.best_role_evidence:.3f}",
            "issues": ";".join(self.issues),
        }


def _float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def citation_score(citation: dict[str, Any]) -> float:
    """Score one RoleCitation from 0.0 to 1.0."""
    score = CITATION_TYPE_POINTS.get(citation.get("reference_type"), 0.0)
    if citation.get("doi") or citation.get("pmid"):
        score += 0.20
    if citation.get("url"):
        score += 0.10
    if citation.get("reference_text"):
        score += 0.05
    if citation.get("excerpt"):
        score += 0.15
    if citation.get("curator_note"):
        score += 0.10
    return min(1.0, score)


def best_citation_score(evidence: Sequence[dict[str, Any]]) -> float:
    return max((citation_score(citation) for citation in evidence), default=0.0)


def _mapping_evidence_points(evidence: Sequence[dict[str, Any]]) -> float:
    if not evidence:
        return 0.0
    score = 0.0
    for item in evidence:
        if item.get("pmid") or item.get("doi"):
            score = max(score, 4.0)
        elif item.get("source"):
            score = max(score, 2.0)
        if item.get("snippet") and item.get("supports") == "SUPPORT":
            score = max(score, 5.0)
    return score


def score_identity(record: dict[str, Any]) -> tuple[float, list[str]]:
    ontology_mapping = record.get("ontology_mapping") or {}
    mapping_status = record.get("mapping_status") or ""
    mapping_quality = ontology_mapping.get("mapping_quality") or ""
    issues: list[str] = []

    if mapping_status != "MAPPED":
        issues.append("not_mapped")
    if mapping_quality in {"FALLBACK_REGISTRY", "LEXICAL_MATCH", "PROVISIONAL", "PLACEHOLDER"}:
        issues.append(f"weak_mapping_quality:{mapping_quality}")
    if not ontology_mapping.get("evidence"):
        issues.append("mapping_missing_evidence")

    score = 0.0
    if mapping_status == "MAPPED":
        score += 5.0
    score += MAPPING_QUALITY_POINTS.get(mapping_quality, 0.0)
    score += _mapping_evidence_points(ontology_mapping.get("evidence") or [])
    return min(20.0, score), issues


def score_roles(record: dict[str, Any]) -> tuple[float, float, int, int, float, list[str]]:
    roles = list(iter_role_assignments(record, slots=FACET_ROLE_SLOTS))
    role_count = len(roles)
    populated_facets = len({slot for slot, _ in roles})
    issues: list[str] = []

    if not roles:
        return 0.0, 0.0, 0, 0, 0.0, ["no_ingredient_roles"]

    confidences = [_float(assignment.get("confidence"), 0.0) for _, assignment in roles]
    avg_confidence = sum(confidences) / len(confidences)
    if avg_confidence < 0.8:
        issues.append("low_average_role_confidence")

    evidence_scores: list[float] = []
    for slot, assignment in roles:
        role = assignment.get("role") or "UNKNOWN"
        evidence = assignment.get("evidence") or []
        best = best_citation_score(evidence)
        evidence_scores.append(best)
        if not evidence:
            issues.append(f"role_missing_evidence:{slot}.{role}")
        elif best <= CITATION_TYPE_POINTS["COMPUTATIONAL_PREDICTION"] + 0.20:
            issues.append(f"role_lacks_external_evidence:{slot}.{role}")
        if slot == "cellular_metabolic_roles" and not assignment.get("metabolic_context"):
            issues.append(f"cellular_role_missing_metabolic_context:{role}")

    role_content = min(40.0, 12.0 + min(role_count, 4) * 3.0 + populated_facets * 2.0)
    role_content += min(avg_confidence, 1.0) * 10.0
    role_evidence = sum(evidence_scores) / len(evidence_scores) * 30.0
    return (
        min(50.0, role_content),
        min(30.0, role_evidence),
        role_count,
        populated_facets,
        max(evidence_scores, default=0.0),
        issues,
    )


def score_components(record: dict[str, Any]) -> tuple[float, list[str]]:
    ingredient_type = record.get("ingredient_type") or ""
    components = record.get("components") or []
    assertion = record.get("component_assertion") or {}
    issues: list[str] = []

    if not components:
        if ingredient_type in COMPONENT_PARENT_TYPES:
            issues.append("no_component_edges")
            return 0.0, issues
        return 10.0, issues

    score = 2.0
    if assertion:
        score += 4.0
        if assertion.get("evidence"):
            score += 4.0
        else:
            issues.append("component_assertion_missing_evidence")
    else:
        issues.append("components_missing_assertion")
    return min(10.0, score), issues


def score_record(path: Path, record: dict[str, Any]) -> ScoreRow:
    identity_score, identity_issues = score_identity(record)
    (
        role_content_score,
        role_evidence_score,
        role_count,
        populated_facets,
        best_evidence,
        role_issues,
    ) = score_roles(record)
    component_score, component_issues = score_components(record)
    ontology_mapping = record.get("ontology_mapping") or {}
    occurrence_statistics = record.get("occurrence_statistics") or {}
    return ScoreRow(
        path=path,
        identity_score=identity_score,
        role_content_score=role_content_score,
        role_evidence_score=role_evidence_score,
        component_score=component_score,
        total_occurrences=_int(occurrence_statistics.get("total_occurrences")),
        role_count=role_count,
        populated_role_facets=populated_facets,
        best_role_evidence=best_evidence,
        issues=tuple(identity_issues + role_issues + component_issues),
        identifier=str(record.get("identifier") or ""),
        preferred_term=str(record.get("preferred_term") or path.stem),
        mapping_status=str(record.get("mapping_status") or ""),
        mapping_quality=str(ontology_mapping.get("mapping_quality") or ""),
        ingredient_type=str(record.get("ingredient_type") or ""),
    )


def collect_paths(ingredients_dir: Path, statuses: Iterable[str]) -> list[Path]:
    paths: list[Path] = []
    for status in statuses:
        status_dir = ingredients_dir / status
        if not status_dir.exists():
            continue
        paths.extend(sorted(status_dir.glob("*.yaml")))
    return paths


def rank_records(
    paths: Iterable[Path],
    min_occurrences: int = 0,
    include_rejected: bool = False,
) -> list[ScoreRow]:
    rows: list[ScoreRow] = []
    for path in paths:
        record = yaml.load(path.read_text(encoding="utf-8"), Loader=SAFE_LOADER) or {}
        if not isinstance(record, dict):
            continue
        if not include_rejected and record.get("mapping_status") == "REJECTED":
            continue
        row = score_record(path, record)
        if row.total_occurrences >= min_occurrences:
            rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            row.readiness_score,
            row.role_evidence_score,
            -row.total_occurrences,
            row.preferred_term.lower(),
            str(row.path),
        ),
    )


def write_tsv(rows: Sequence[ScoreRow], out: Path, root: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for rank, row in enumerate(rows, start=1):
            writer.writerow(row.to_tsv(rank, root))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--ingredients-dir",
        type=Path,
        default=DEFAULT_INGREDIENTS_DIR,
        help="Directory with mapped/ and unmapped/ ingredient YAML subdirectories.",
    )
    parser.add_argument(
        "--status",
        choices=STATUSES,
        action="append",
        help="Restrict to a status subdirectory. Repeatable; defaults to both.",
    )
    parser.add_argument(
        "--min-occurrences",
        type=int,
        default=0,
        help="Only include records with at least this many total_occurrences.",
    )
    parser.add_argument(
        "--include-rejected",
        action="store_true",
        help="Include REJECTED tombstone records in the worklist.",
    )
    parser.add_argument("--limit", type=int, help="Limit rows written after sorting.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    statuses = tuple(args.status) if args.status else STATUSES
    rows = rank_records(
        collect_paths(args.ingredients_dir, statuses),
        args.min_occurrences,
        include_rejected=args.include_rejected,
    )
    if args.limit is not None:
        rows = rows[: args.limit]
    write_tsv(rows, args.out, ROOT)
    print(f"wrote {len(rows)} ranked records to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
