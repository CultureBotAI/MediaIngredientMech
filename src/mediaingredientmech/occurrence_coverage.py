"""Explicit occurrence completeness without changing scientific owner bytes (#1431).

The independent companion binds current owners and evidence; it never promotes a
source identity, supplies complete media counts, or replaces recorded counts.
Missing declarations remain MISSING. Numeric observations are separate from the
media usage API and require independent review of their actual source scope.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

from mediaingredientmech.utils.culturemech_occurrences import effective_occurrence_statistics

SCHEMA = Path(__file__).parent / "schema" / "occurrence_coverage.yaml"
DEFAULT_COVERAGE = Path(__file__).resolve().parents[2] / "mappings" / "occurrence_coverage.yaml"


def content_sha256(record: Mapping[str, Any]) -> str:
    """Canonical loaded-content binding shared by individual/aggregate readers."""
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False,
                                    separators=(",", ":"), default=str).encode()).hexdigest()


def _integer(value: Any, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer (not bool)")
    return value


def stored_counts(record: Mapping[str, Any]) -> tuple[int, int] | None:
    """Absent is not zero; partially present statistics are invalid, not unknown."""
    if "occurrence_statistics" not in record:
        return None
    st = record["occurrence_statistics"]
    if not isinstance(st, Mapping):
        raise ValueError("occurrence_statistics must be a complete mapping")
    media = _integer(st.get("media_count"), "media_count")
    total = _integer(st.get("total_occurrences"), "total_occurrences")
    if media > total:
        raise ValueError("media_count exceeds total_occurrences")
    if record.get("mapping_status") == "REJECTED" and (media or total):
        raise ValueError("REJECTED owner has nonzero occurrences")
    return media, total


def _timestamp(value: Any) -> None:
    dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("coverage timestamps must include a timezone")


def _evidence_file(root: Path, name: str) -> Path:
    rel = Path(name)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("coverage evidence path must be contained and relative")
    target = (root / rel).resolve(strict=True)
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        raise ValueError("coverage evidence escapes its bundle or is not a file")
    return target


@lru_cache(maxsize=1)
def _validator() -> Validator:
    return Validator(schema=str(SCHEMA),
                     validation_plugins=[JsonschemaValidationPlugin(closed=True)])


@dataclass(frozen=True)
class Coverage:
    """Only constructed by the byte-binding validator; rechecked on every lookup."""
    declarations: Mapping[str, dict[str, Any]]
    sha256: str

    def for_record(self, record: Mapping[str, Any]) -> dict[str, Any] | None:
        item = self.declarations.get(str(record.get("mim_id") or ""))
        if item is not None and content_sha256(record) != item["owner_content_sha256"]:
            raise ValueError("coverage declaration has stale owner content")
        return item


def load_coverage(path: Path, ingredients_root: Path) -> Coverage:
    """Validate closed shape, current owner bytes, and contained evidence hashes.

    Evidence binding is not scientific approval: actual reasons and observations
    still require the independent review used for publication of the companion.
    """
    raw = path.read_bytes()
    doc = yaml.safe_load(raw)
    report = _validator().validate(doc, target_class="OccurrenceCoverage")
    errors = [r.message for r in report.results if r.severity == Severity.ERROR]
    if errors:
        raise ValueError("invalid occurrence coverage: " + "; ".join(errors))
    _timestamp(doc["created_at"])
    declarations = {}
    for item in doc["declarations"]:
        mim_id = item["mim_id"]
        if mim_id in declarations:
            raise ValueError(f"duplicate occurrence declaration: {mim_id}")
        declarations[mim_id] = item
    owners: dict[str, list[tuple[dict, bytes]]] = {k: [] for k in declarations}
    for state in ("mapped", "unmapped"):
        for owner in (ingredients_root / state).glob("*.yaml"):
            data = owner.read_bytes()
            record = yaml.safe_load(data)
            if isinstance(record, dict) and record.get("mim_id") in owners:
                owners[record["mim_id"]].append((record, data))
    for mim_id, item in declarations.items():
        candidates = owners[mim_id]
        if len(candidates) != 1:
            raise ValueError(f"coverage needs exactly one current owner: {mim_id}")
        record, data = candidates[0]
        if hashlib.sha256(data).hexdigest() != item["owner_sha256"]:
            raise ValueError(f"stale occurrence owner bytes: {mim_id}")
        if content_sha256(record) != item["owner_content_sha256"]:
            raise ValueError(f"stale occurrence owner content: {mim_id}")
        if stored_counts(record) is not None:
            raise ValueError("UNKNOWN cannot override stored counts")
        evidence = {}
        for ev in item["evidence"]:
            name = ev["path"]
            if name in evidence:
                raise ValueError("duplicate occurrence evidence path")
            b = _evidence_file(path.parent, name).read_bytes()
            if hashlib.sha256(b).hexdigest() != ev["sha256"]:
                raise ValueError(f"stale occurrence evidence: {name}")
            evidence[name] = ev
        source_names = set()
        for source in item["source_coverage"]:
            for key in ("source", "revision", "scope"):
                if not source[key].strip():
                    raise ValueError(f"empty source coverage {key}")
            source_names.add(source["source"])
            _timestamp(source["scanned_at"])
            _integer(source["row_count"], "source row_count")
            if "distinct_media_count" in source:
                _integer(source["distinct_media_count"], "distinct_media_count")
            ev = evidence.get(source["evidence_path"])
            if ev is None or ev["sha256"] != source["source_sha256"]:
                raise ValueError("source coverage must bind exact retained source evidence")
        for observation in item.get("observations", []):
            _integer(observation["count"], "observed count")
            if observation["source"] not in source_names:
                raise ValueError("observation source is outside declared coverage")
            if item["reason_code"] in {"SOURCE_ATTRIBUTION_WITHHELD", "NO_SUPPORTED_OWNER_ATTRIBUTION", "SOURCE_REVIEW_PENDING"}:
                raise ValueError("unsettled attribution cannot support observed owner counts")
            for key in ("evidence_path", "primary_review_path", "skeptical_review_path"):
                if observation[key] not in evidence:
                    raise ValueError(f"observation lacks bound {key}")
            if observation["primary_review_path"] == observation["skeptical_review_path"]:
                raise ValueError("observation requires separate primary and skeptical evidence")
    return Coverage(declarations, hashlib.sha256(raw).hexdigest())


def default_coverage(root: Path | None = None) -> Coverage | None:
    """No companion means no approved unknowns, not an empty approval artifact."""
    repo = root if root is not None else DEFAULT_COVERAGE.parent.parent
    path = repo / "mappings" / "occurrence_coverage.yaml"
    return load_coverage(path, repo / "data" / "ingredients") if path.exists() else None


def occurrence_view(record: Mapping[str, Any], counts_by_id: Mapping[str, tuple[int, int]] | None = None,
                    coverage: Coverage | None = None) -> dict[str, Any]:
    """Return nullable counts plus explicit state; never infer unknown approval."""
    stored = stored_counts(record)
    declaration = coverage.for_record(record) if coverage else None
    if declaration is not None:
        if stored is not None:
            raise ValueError("UNKNOWN cannot override recorded counts")
        return {"media_count": None, "total_occurrences": None,
                "occurrence_statistics_state": "UNKNOWN",
                "occurrence_statistics_reason": declaration["reason"],
                "occurrence_statistics_provenance": {
                    "coverage_sha256": coverage.sha256,
                    "owner_sha256": declaration["owner_sha256"],
                    "reason_code": declaration["reason_code"],
                    "evidence": declaration["evidence"],
                    "source_coverage": declaration["source_coverage"],
                    "observations": declaration.get("observations", [])}}
    if stored is None:
        # Membership from a subset is not proof of complete usage or approval.
        return {"media_count": None, "total_occurrences": None,
                "occurrence_statistics_state": "MISSING",
                "occurrence_statistics_reason": "No validated occurrence coverage declaration"}
    values = effective_occurrence_statistics(record, counts_by_id)
    media = _integer(values[0], "effective media_count")
    total = _integer(values[1], "effective total_occurrences")
    if media > total:
        raise ValueError("effective media_count exceeds total_occurrences")
    derived = record.get("mapping_status") != "REJECTED" and counts_by_id and str(record.get("identifier") or "").strip() in counts_by_id
    return {"media_count": media, "total_occurrences": total,
            "occurrence_statistics_state": "MEMBERSHIP" if derived else "RECORDED",
            "occurrence_statistics_reason": ""}
