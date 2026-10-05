"""Section refreshes that keep a content-bound review attached to a record.

Every scientific review in this repository is bound to the exact bytes of the
records it read, so any edit to a record file withdraws the review's approval
of that record's claims. That is the point -- but it also means a change to a
section no review reads (recipe counts refreshed from CultureMech, a causal
graph added beside the record's mapping) withdraws approvals that never
depended on it.

A refresh receipt (``record_refreshes/*.json``) records, per record, the one
section that changed, its value before (``null`` when the section is new), the
bytes before and after, and the one curation event the change appended.
Nothing is taken on trust: a verifier peels the receipt off the CURRENT file
-- restores the section's previous value, drops that event, re-serializes --
and the result must hash to the recorded ``before`` exactly. Only then is the
earlier hash an equivalent of the current file for review purposes. Any other
change on the record stops the peel, so it never extends past a mapping
change, a synonym edit, a role change or an unrecorded write.

Only sections in ``REFRESHABLE_SECTIONS`` can be refreshed this way, because no
review binds their content. A section must leave that list the moment a review
starts to read it -- ``causal_graphs`` once graph edges are exported and
reviewed as assertions.

A receipt approves nothing. It only lets an existing review bound to the
earlier bytes keep applying to bytes that differ by one unreviewed section and
its audit event.
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
    # Mechanism graphs linking the ingredient to sibling-Mech records. No
    # review in reports/ reads them yet; they are not part of the semantic
    # release's assertion inventory or the reviewed SSSOM.
    "causal_graphs": SectionRule(
        actions=frozenset({"CAUSAL_GRAPH_ADDED", "CAUSAL_GRAPH_UPDATED"}),
    ),
}

COUNT_FIELDS = ("media_count", "total_occurrences")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump_record(record: dict) -> bytes:
    """Serialize a record exactly as the per-record writers do."""
    return yaml.dump(record, default_flow_style=False, sort_keys=False, allow_unicode=True).encode(
        "utf-8"
    )


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
    section = entry.get("section")
    rule = REFRESHABLE_SECTIONS.get(section)
    if rule is None:
        raise ValueError(f"Section {section!r} is not refreshable without review: {path}")
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
            if entry.get("section") not in REFRESHABLE_SECTIONS:
                raise ValueError(
                    f"Record refresh receipt {batch} refreshes {entry.get('section')!r}"
                )
    return receipts


class RecordRefreshes:
    """The verified review equivalents of each record's current bytes."""

    def __init__(self, root: Path, directory: Path | None = None):
        self.root = Path(root)
        self.directory = self.root / (directory or REFRESH_DIR)
        self.receipts = _load_receipts(self.directory) if self.directory.is_dir() else []
        self._entries: dict[str, list[dict]] = {}
        for receipt in self.receipts:
            for entry in receipt["records"]:
                self._entries.setdefault(entry["source_record"], []).append(entry)
        self._states: dict[str, list[tuple[str, bytes]]] = {}

    def files(self) -> list[Path]:
        return sorted(self.directory.glob("*.json")) if self.directory.is_dir() else []

    def states(self, path: str) -> list[tuple[str, bytes]]:
        """``(sha256, bytes)`` for the current file, then each verified earlier state."""
        if path not in self._states:
            content = (self.root / path).read_bytes()
            states = [(sha256(content), content)]
            for entry in reversed(self._entries.get(path, [])):
                if entry["after_yaml_sha256"] != states[-1][0]:
                    break  # a change no receipt describes intervened; nothing earlier is equivalent
                content = peel(content, entry)
                states.append((entry["before_yaml_sha256"], content))
            self._states[path] = states
        return self._states[path]

    def equivalents(self, path: str) -> set[str]:
        return {digest for digest, _content in self.states(path)}

    def matches(self, path: str, reviewed_sha256: str | None) -> bool:
        """Whether a review bound to ``reviewed_sha256`` still applies to ``path``."""
        return reviewed_sha256 is not None and reviewed_sha256 in self.equivalents(path)

    def record_at(self, path: str, reviewed_sha256: str) -> dict | None:
        """The record as the review bound to ``reviewed_sha256`` read it."""
        for digest, content in self.states(path):
            if digest == reviewed_sha256:
                return yaml.safe_load(content)
        return None

    def advance(self, path: str, known: str, target: str) -> str:
        """Follow recorded refresh transitions from ``known`` toward ``target``.

        Chain bookkeeping for a later mapping-change receipt whose ``before``
        is a refreshed hash. It grants nothing: approval still needs ``matches``.
        """
        transitions = {
            entry["before_yaml_sha256"]: entry["after_yaml_sha256"]
            for entry in self._entries.get(path, [])
        }
        seen = set()
        while known != target and known in transitions and known not in seen:
            seen.add(known)
            known = transitions[known]
        return known
