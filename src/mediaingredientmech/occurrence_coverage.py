"""Explicit occurrence completeness without changing scientific owner bytes (#1431).

The independent companion binds current owners and evidence; it never promotes a
source identity, supplies complete media counts, or replaces recorded counts.
Missing declarations remain MISSING. Numeric observations are separate from the
media usage API and require independent review of their actual source scope.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from types import ModuleType
from typing import Any

import yaml  # type: ignore[import-untyped]
from linkml.validator import Validator  # type: ignore[import-untyped]
from linkml.validator.plugins import JsonschemaValidationPlugin  # type: ignore[import-untyped]
from linkml.validator.report import Severity  # type: ignore[import-untyped]

from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.utils.culturemech_occurrences import effective_occurrence_statistics

SCHEMA = Path(__file__).parent / "schema" / "occurrence_coverage.yaml"
DEFAULT_COVERAGE = Path(__file__).resolve().parents[2] / "mappings" / "occurrence_coverage.yaml"


class _UnambiguousLoader(yaml.SafeLoader):
    """#1463: a byte hash cannot disambiguate duplicate YAML keys."""

    def compose_node(self, parent, index):
        event = self.peek_event()
        if (
            self.check_event(yaml.AliasEvent)
            or getattr(event, "anchor", None)
            or getattr(event, "tag", None)
        ):
            raise ValueError("coverage YAML must not contain aliases, anchors or explicit tags")
        return super().compose_node(parent, index)

    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise ValueError(f"duplicate or non-string YAML key: {key!r}")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def _load_document(raw: bytes) -> dict[str, Any]:
    result = yaml.load(raw, Loader=_UnambiguousLoader)
    if not isinstance(result, dict):
        raise ValueError("coverage/owner document must contain one mapping")
    return result


def _load_owner_document(raw: bytes) -> dict[str, Any]:
    """#1463: native writers share evidence sequences; the companion stays strict."""
    try:
        if any(getattr(event, "tag", None) for event in yaml.parse(raw)):
            raise ValueError("owner YAML must not contain explicit tags")
        result = _load_yaml(raw.decode("utf-8"))
    except (ValueError, yaml.YAMLError) as exc:
        raise ValueError(f"invalid owner YAML (duplicate keys refused): {exc}") from exc
    if not isinstance(result, dict):
        raise ValueError("owner document must contain one mapping")
    active: set[int] = set()
    checked: set[int] = set()

    def check(value):
        if not isinstance(value, (dict, list)):
            return
        identity = id(value)
        if identity in active:
            raise ValueError("recursive owner YAML alias")
        if identity in checked:
            return
        active.add(identity)
        if isinstance(value, dict):
            if any(not isinstance(key, str) for key in value):
                raise ValueError("non-string owner YAML key")
        for child in value.values() if isinstance(value, dict) else value:
            check(child)
        active.remove(identity)
        checked.add(identity)

    check(result)
    return result


@lru_cache(maxsize=1)
def _review_contract() -> ModuleType:
    """Reuse the maintained native scientific review validator without editing it."""
    path = Path(__file__).resolve().parents[2] / "scripts" / "record_review.py"
    spec = importlib.util.spec_from_file_location("occurrence_native_record_review", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def observation_claim(
    item: Mapping[str, Any], source: Mapping[str, Any], observation: Mapping[str, Any]
) -> str:
    """Exact quantity/scope claim encoded in native ReviewAssessment dimensions."""
    return content_sha256(
        {
            "contract": "mim-occurrence-observation-v1",
            "mim_id": item["mim_id"],
            "owner_sha256": item["owner_sha256"],
            "source": source["source"],
            "source_revision": source["revision"],
            "source_sha256": source["source_sha256"],
            "count": observation["count"],
            "unit": observation["unit"],
            "scope": observation["scope"],
        }
    )


def _observation_reviews(
    bundle_root: Path,
    repo_root: Path,
    item: dict,
    source: dict,
    observation: dict,
    evidence: dict,
    owner_path: Path,
) -> None:
    """#1464: filenames and hashes alone do not constitute assessed support."""
    native = _review_contract()
    claim = observation_claim(item, source, observation)
    identities = []
    review_ids = []
    for role in ("primary", "skeptical"):
        relative = observation[f"{role}_review_path"]
        markdown = str(Path(relative).with_name("review.md"))
        if markdown not in evidence:
            raise ValueError("observation requires a bound native YAML/Markdown pair")
        review = native.parse_review_bundle(
            relative,
            _evidence_file(bundle_root, relative).read_bytes(),
            _evidence_file(bundle_root, markdown).read_bytes(),
        )
        if review["repository"].lower() != "culturebotai/mediaingredientmech":
            raise ValueError("occurrence review belongs to another repository")
        provenance = native.source_provenance(repo_root, review)
        if provenance["status"] in {"invalid", "unverified"}:
            raise ValueError("occurrence review native provenance is not verified")
        if (
            not review["scientific_review"]
            or review["completion"] != "completed"
            or review["verdict"] not in {"pass", "pass_with_limitations"}
        ):
            raise ValueError("occurrence observation requires completed positive scientific review")
        if role == "skeptical" and review["reviewer"]["independence"] != "independent":
            raise ValueError("occurrence skeptical review is not independent")
        inputs = {entry["path"]: entry["sha256"] for entry in review["source"]["inputs"]}
        for name, digest in inputs.items():
            if hashlib.sha256(_evidence_file(repo_root, name).read_bytes()).hexdigest() != digest:
                raise ValueError("occurrence review input has changed")
        owner_relative = str(owner_path.relative_to(repo_root))
        source_relative = str(
            _evidence_file(bundle_root, source["evidence_path"]).relative_to(repo_root)
        )
        if (
            inputs.get(owner_relative) != item["owner_sha256"]
            or inputs.get(source_relative) != source["source_sha256"]
        ):
            raise ValueError("occurrence review must bind current owner and exact source version")
        targets = {
            target["target_id"] for target in review["targets"] if target["path"] == owner_relative
        }
        if (
            item["mim_id"] not in targets
            or item["mim_id"] not in review["scope"]["reviewed_target_ids"]
        ):
            raise ValueError("occurrence review targets another owner")
        supportive = {ev["evidence_id"] for ev in review["evidence"] if ev["support"] == "supports"}
        refuting = {ev["evidence_id"] for ev in review["evidence"] if ev["support"] == "refutes"}
        quantity = [
            a
            for a in review["assessments"]
            if a["area"] == "quantity" and item["mim_id"] in a["target_ids"]
        ]
        for assessment in quantity:
            dimensions = assessment.get("dimensions", [])
            bindings = [d for d in dimensions if d["name"] == "occurrence_claim_sha256"]
            bound_claim = None
            if (
                len(bindings) == 1
                and re.fullmatch(r"[0-9a-f]{64}", bindings[0]["value"])
                and bindings[0]["evidence_ids"]
            ):
                bound_claim = bindings[0]["value"]
            refs = set(assessment["evidence_ids"])
            for dimension in dimensions:
                refs.update(dimension["evidence_ids"])
            disputed = (
                assessment["outcome"] in {"concern", "unknown"}
                or bool(refuting.intersection(refs))
                or (bound_claim == claim and assessment["outcome"] != "supported")
            )
            # #1464: a positive assessment cannot cancel a hold on the same
            # claim. Missing/malformed bindings cannot prove it is unrelated.
            if disputed and bound_claim in {None, claim}:
                raise ValueError("occurrence review has an unresolved or ambiguous quantity claim")
        # Native findings have owner/category/evidence fields but no claim
        # dimension. Do not guess that an unresolved same-owner quantity
        # finding is unrelated, or treat an accepted risk as count support.
        if any(
            f["category"] == "quantity"
            and item["mim_id"] in f["target_ids"]
            and f["status"] not in {"resolved", "rejected"}
            for f in review["findings"]
        ):
            raise ValueError("occurrence review has an unresolved owner quantity finding")
        matching = [
            a
            for a in quantity
            if a["outcome"] == "supported"
            and supportive.intersection(a["evidence_ids"])
            and any(
                d["name"] == "occurrence_claim_sha256"
                and d["value"] == claim
                and supportive.intersection(d["evidence_ids"])
                for d in a.get("dimensions", [])
            )
        ]
        if not matching:
            raise ValueError(
                "occurrence review lacks supported exact owner/source/count/unit/scope claim"
            )
        identities.append(review["reviewer"]["identity"].strip().casefold())
        review_ids.append(review["review_id"])
    if len(set(identities)) != 2 or len(set(review_ids)) != 2:
        raise ValueError("occurrence observation requires distinct primary and skeptical reviewers")


def content_sha256(record: Mapping[str, Any]) -> str:
    """Canonical loaded-content binding shared by individual/aggregate readers."""
    return hashlib.sha256(
        json.dumps(
            record, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


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
    return Validator(
        schema=str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


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
    doc = _load_document(raw)
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
    owners: dict[str, list[tuple[dict, bytes, Path]]] = {k: [] for k in declarations}
    for state in ("mapped", "unmapped"):
        for owner in (ingredients_root / state).glob("*.yaml"):
            data = owner.read_bytes()
            record = _load_owner_document(data)
            if isinstance(record, dict) and record.get("mim_id") in owners:
                owners[record["mim_id"]].append((record, data, owner))
    for mim_id, item in declarations.items():
        candidates = owners[mim_id]
        if len(candidates) != 1:
            raise ValueError(f"coverage needs exactly one current owner: {mim_id}")
        record, data, owner_path = candidates[0]
        if hashlib.sha256(data).hexdigest() != item["owner_sha256"]:
            raise ValueError(f"stale occurrence owner bytes: {mim_id}")
        if content_sha256(record) != item["owner_content_sha256"]:
            raise ValueError(f"stale occurrence owner content: {mim_id}")
        if stored_counts(record) is not None:
            raise ValueError("UNKNOWN cannot override stored counts")
        evidence = {}
        physical_evidence = set()
        for ev in item["evidence"]:
            name = ev["path"]
            if name in evidence:
                raise ValueError("duplicate occurrence evidence path")
            evidence_path = _evidence_file(path.parent, name)
            stat = evidence_path.stat()
            identity = (stat.st_dev, stat.st_ino)
            if identity in physical_evidence:
                raise ValueError("duplicate/aliased physical occurrence evidence")
            physical_evidence.add(identity)
            b = evidence_path.read_bytes()
            if hashlib.sha256(b).hexdigest() != ev["sha256"]:
                raise ValueError(f"stale occurrence evidence: {name}")
            evidence[name] = ev
        source_names = set()
        for source in item["source_coverage"]:
            for key in ("source", "revision", "scope"):
                if not source[key].strip():
                    raise ValueError(f"empty source coverage {key}")
            if source["source"] in source_names:
                raise ValueError("duplicate or ambiguous source name/version")
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
            if record.get("mapping_status") == "REJECTED" and observation["count"]:
                raise ValueError("REJECTED owner cannot acquire positive observed counts")
            if observation["source"] not in source_names:
                raise ValueError("observation source is outside declared coverage")
            if item["reason_code"] in {
                "SOURCE_ATTRIBUTION_WITHHELD",
                "NO_SUPPORTED_OWNER_ATTRIBUTION",
                "SOURCE_REVIEW_PENDING",
            }:
                raise ValueError("unsettled attribution cannot support observed owner counts")
            for key in ("evidence_path", "primary_review_path", "skeptical_review_path"):
                if observation[key] not in evidence:
                    raise ValueError(f"observation lacks bound {key}")
            source = next(
                s for s in item["source_coverage"] if s["source"] == observation["source"]
            )
            _observation_reviews(
                path.parent.resolve(),
                ingredients_root.resolve().parent.parent,
                item,
                source,
                observation,
                evidence,
                owner_path.resolve(),
            )
    return Coverage(declarations, hashlib.sha256(raw).hexdigest())


def default_coverage(root: Path | None = None) -> Coverage | None:
    """No companion means no approved unknowns, not an empty approval artifact."""
    repo = root if root is not None else DEFAULT_COVERAGE.parent.parent
    path = repo / "mappings" / "occurrence_coverage.yaml"
    return load_coverage(path, repo / "data" / "ingredients") if path.exists() else None


def occurrence_view(
    record: Mapping[str, Any],
    counts_by_id: Mapping[str, tuple[int, int]] | None = None,
    coverage: Coverage | None = None,
) -> dict[str, Any]:
    """Return nullable counts plus explicit state; never infer unknown approval."""
    # A null optional structure is displayed as MISSING, never approved UNKNOWN.
    # Strict audit/companion validation still rejects it as complete statistics.
    stored = None if record.get("occurrence_statistics") is None else stored_counts(record)
    declaration = coverage.for_record(record) if coverage else None
    if declaration is not None and coverage is not None:
        if stored is not None:
            raise ValueError("UNKNOWN cannot override recorded counts")
        return {
            "media_count": None,
            "total_occurrences": None,
            "occurrence_statistics_state": "UNKNOWN",
            "occurrence_statistics_reason": declaration["reason"],
            "occurrence_statistics_provenance": {
                "coverage_sha256": coverage.sha256,
                "owner_sha256": declaration["owner_sha256"],
                "reason_code": declaration["reason_code"],
                "evidence": declaration["evidence"],
                "source_coverage": declaration["source_coverage"],
                "observations": declaration.get("observations", []),
            },
        }
    if stored is None:
        # Membership from a subset is not proof of complete usage or approval.
        return {
            "media_count": None,
            "total_occurrences": None,
            "occurrence_statistics_state": "MISSING",
            "occurrence_statistics_reason": "No validated occurrence coverage declaration",
        }
    values = effective_occurrence_statistics(record, counts_by_id)
    media = _integer(values[0], "effective media_count")
    total = _integer(values[1], "effective total_occurrences")
    if media > total:
        raise ValueError("effective media_count exceeds total_occurrences")
    derived = (
        record.get("mapping_status") != "REJECTED"
        and counts_by_id
        and str(record.get("identifier") or "").strip() in counts_by_id
    )
    return {
        "media_count": media,
        "total_occurrences": total,
        "occurrence_statistics_state": "MEMBERSHIP" if derived else "RECORDED",
        "occurrence_statistics_reason": "",
    }


def main() -> int:
    """Read-only validation of a prepared companion, never owner writes."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("coverage", type=Path)
    parser.add_argument("--ingredients-root", type=Path, default=Path("data/ingredients"))
    args = parser.parse_args()
    coverage = load_coverage(args.coverage, args.ingredients_root)
    print(
        f"Validated {len(coverage.declarations)} UNKNOWN bindings; companion SHA256 {coverage.sha256}"
    )
    print(
        "Structural/byte validation only; scientific companion and source reviews remain required."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
