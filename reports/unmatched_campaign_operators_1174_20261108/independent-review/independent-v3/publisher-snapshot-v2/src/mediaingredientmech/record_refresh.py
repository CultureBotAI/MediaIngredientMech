"""Audit-only section-refresh receipts; approvals always require exact record bytes.

A receipt records a bounded section change and its appended curation event.
``peel`` verifies that audit description against the current file by restoring
its previous section value and reproducing the recorded before-bytes.

Verification does not make different record bytes equivalent for approval.
Every edit, including occurrence counts, causal graphs, formatting and audit
history, requires fresh approval bound to the resulting bytes. Receipt chains
cannot advance the reviewed baseline or preserve any earlier approval.

Historical receipts remain readable and the producer can record new audit
receipts. ``REFRESHABLE_SECTIONS`` governs their audit shape only; it grants no
exception to the exact-byte approval policy.
"""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import yaml

REFRESH_DIR = Path("reports/sssom_completion_20260921/record_refreshes")
RECEIPT_KIND = "section_refresh"


@dataclass(frozen=True)
class SectionRule:
    """What a refresh of one section may look like."""

    actions: frozenset[str]
    curators: frozenset[str] | None = None  # None: any curator
    llm_assisted_allowed: bool = True


REFRESHABLE_SECTIONS: dict[str, SectionRule] = {
    # Recipe counts derived from CultureMech's occurrence table (#449, #810).
    "occurrence_statistics": SectionRule(
        actions=frozenset({"CORRECTED"}),
        curators=frozenset({"refresh_occurrence_statistics"}),
        llm_assisted_allowed=False,
    ),
    # Mechanism graphs linking the ingredient to sibling-Mech records.
    # This is an audit shape, never permission to inherit a prior approval.
    "causal_graphs": SectionRule(
        actions=frozenset({"CAUSAL_GRAPH_ADDED", "CAUSAL_GRAPH_UPDATED"}),
    ),
}

# Retired audit shapes remain loadable because receipts are append-only.
# Neither active nor retired receipt shapes carry approvals. Section -> reason.
RETIRED_SECTIONS: dict[str, str] = {}

COUNT_FIELDS = ("media_count", "total_occurrences")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump_record(record: dict) -> bytes:
    """Serialize a record exactly as the per-record writers do."""
    text: str = yaml.dump(record, default_flow_style=False, sort_keys=False, allow_unicode=True)
    return text.encode("utf-8")


def _check_counts(entry: dict, record: dict) -> None:
    """occurrence_statistics refreshes change the two counts and nothing else."""
    path = entry.get("source_record")
    before = entry.get("before_value") or {}
    after = record.get("occurrence_statistics") or {}
    if {k: v for k, v in before.items() if k not in COUNT_FIELDS} != {
        k: v for k, v in after.items() if k not in COUNT_FIELDS
    }:
        raise ValueError(f"occurrence_statistics refresh changed more than the counts: {path}")
    prefix = (
        f"occurrence_statistics {before.get('media_count')}/{before.get('total_occurrences')} -> "
        f"{after.get('media_count')}/{after.get('total_occurrences')}"
    )
    if not str(entry["event"].get("changes", "")).startswith(prefix):
        raise ValueError(f"Refresh event does not state this count change: {path}")


def _check_graphs(entry: dict, record: dict) -> None:
    path = entry.get("source_record")
    if "causal_graphs" not in str(entry["event"].get("changes", "")):
        raise ValueError(f"Refresh event does not name the causal_graphs section: {path}")
    if not record.get("causal_graphs"):
        raise ValueError(f"causal_graphs refresh leaves no graph on the record: {path}")


_SECTION_CHECKS = {"occurrence_statistics": _check_counts, "causal_graphs": _check_graphs}


def peel(content: bytes, entry: dict) -> bytes:
    """Return the bytes ``entry`` refreshed, or raise if it was not that refresh."""
    path = entry.get("source_record")
    section = str(entry.get("section") or "")
    rule = REFRESHABLE_SECTIONS.get(section)
    if rule is None:
        raise ValueError(f"Section {section!r} is not refreshable for a section audit: {path}")
    if sha256(content) != entry["after_yaml_sha256"]:
        raise ValueError(f"Record refresh does not describe the current bytes: {path}")
    if entry["before_yaml_sha256"] == entry["after_yaml_sha256"]:
        raise ValueError(f"Record refresh changes nothing: {path}")
    record = yaml.safe_load(content)
    history = record.get("curation_history") or []
    event = entry["event"]
    if not history or history[-1] != event:
        raise ValueError(f"Refresh event is not the record's last event: {path}")
    if event.get("action") not in rule.actions or (
        rule.curators is not None and event.get("curator") not in rule.curators
    ):
        raise ValueError(f"Refresh event is not a {section} refresh: {path}")
    if not rule.llm_assisted_allowed and event.get("llm_assisted", False) is not False:
        raise ValueError(f"A {section} refresh must not be LLM-assisted: {path}")
    _SECTION_CHECKS[section](entry, record)
    previous = copy.deepcopy(record)
    previous["curation_history"] = history[:-1]
    if entry.get("before_value") is None:
        previous.pop(section, None)
    else:
        previous[section] = copy.deepcopy(entry["before_value"])
    restored = dump_record(previous)
    if sha256(restored) != entry["before_yaml_sha256"]:
        raise ValueError(f"Record refresh changed more than {section}: {path}")
    return restored


def _load_receipts(directory: Path) -> list[dict]:
    receipts = [json.loads(path.read_text()) for path in sorted(directory.glob("*.json"))]
    receipts.sort(key=lambda receipt: receipt.get("sequence", 0))
    if [receipt.get("sequence") for receipt in receipts] != list(range(1, len(receipts) + 1)):
        raise ValueError("Record refresh receipts must be numbered 1..n without gaps")
    for receipt in receipts:
        batch = receipt.get("batch")
        if receipt.get("schema_version") != 1 or receipt.get("kind") != RECEIPT_KIND:
            raise ValueError(f"Unsupported record refresh receipt: {batch}")
        if str(receipt.get("approval", "")).split(":")[0] != "NONE":
            raise ValueError(f"Record refresh receipt {batch} must not carry an approval")
        paths = [entry["source_record"] for entry in receipt["records"]]
        if len(paths) != len(set(paths)):
            raise ValueError(f"Record refresh receipt {batch} lists a record twice")
        for entry in receipt["records"]:
            section = entry.get("section")
            if section not in REFRESHABLE_SECTIONS and section not in RETIRED_SECTIONS:
                raise ValueError(f"Record refresh receipt {batch} refreshes {section!r}")
            entry.setdefault("_batch", batch)
    return receipts


class RecordRefreshes:
    """Read audit receipts while exposing only the record's current exact bytes."""

    def __init__(self, root: Path, directory: Path | None = None):
        self.root = Path(root)
        self.directory = self.root / (directory or REFRESH_DIR)
        self.receipts = _load_receipts(self.directory) if self.directory.is_dir() else []

    def files(self) -> list[Path]:
        return sorted(self.directory.glob("*.json")) if self.directory.is_dir() else []

    def states(self, path: str) -> list[tuple[str, bytes]]:
        """The current ``(sha256, bytes)`` only; missing records have no states.

        Read again on each call so a previously inspected record cannot retain
        approval after its bytes change. Audit receipts never add prior states.
        """
        target = self.root / path
        if not target.is_file():
            return []
        content = target.read_bytes()
        return [(sha256(content), content)]

    def receipts_used(self, path: str, reviewed_sha256: str | None) -> list[tuple[str, str]]:
        """No audit receipt can be used to carry an approval."""
        return []

    def equivalents(self, path: str) -> set[str]:
        """Only the exact current record hash qualifies for a scientific review."""
        return {digest for digest, _content in self.states(path)}

    def matches(self, path: str, reviewed_sha256: str | None) -> bool:
        """Whether the current bytes are exactly those bound by the review."""
        return reviewed_sha256 is not None and reviewed_sha256 in self.equivalents(path)

    def record_at(self, path: str, reviewed_sha256: str) -> dict | None:
        """Return the current record only when the review binds its exact bytes."""
        for digest, content in self.states(path):
            if digest == reviewed_sha256:
                loaded = yaml.safe_load(content)
                return loaded if isinstance(loaded, dict) else None
        return None

    def advance(self, path: str, known: str, target: str) -> str:
        """Keep the reviewed baseline unchanged, regardless of receipt transitions.

        Section receipts are audit history, not authority to bridge a missing
        exact-byte review or mapping-change link (#819).
        """
        return known
