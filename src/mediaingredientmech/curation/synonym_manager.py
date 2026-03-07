"""Synonym consolidation, duplicate detection, and merging for ingredient records."""

from __future__ import annotations

import logging
import re
from collections import defaultdict
from typing import Any, Optional

logger = logging.getLogger(__name__)


def normalize_text(text: str) -> str:
    """Normalize ingredient text for comparison: lowercase, strip, collapse whitespace."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    # Remove trailing punctuation
    text = text.strip(".,;:")
    return text


class SynonymManager:
    """Manages synonym consolidation and duplicate detection for ingredient records."""

    def __init__(self, records: Optional[list[dict]] = None):
        self._records = records or []
        self._norm_index: dict[str, list[int]] = {}
        self._rebuild_index()

    def _rebuild_index(self) -> None:
        """Build normalized text -> record indices mapping."""
        self._norm_index.clear()
        for i, rec in enumerate(self._records):
            keys = self._extract_normalized_keys(rec)
            for key in keys:
                self._norm_index.setdefault(key, []).append(i)

    def _extract_normalized_keys(self, record: dict) -> set[str]:
        """Extract all normalized names/synonyms from a record."""
        keys = set()
        if record.get("preferred_term"):
            keys.add(normalize_text(record["preferred_term"]))
        for syn in record.get("synonyms", []) or []:
            text = syn.get("synonym_text", "") if isinstance(syn, dict) else str(syn)
            if text:
                keys.add(normalize_text(text))
        return keys

    def set_records(self, records: list[dict]) -> None:
        """Replace internal records and rebuild index."""
        self._records = records
        self._rebuild_index()

    def find_duplicates(self) -> list[list[int]]:
        """Find groups of records that share normalized names/synonyms.

        Returns:
            List of groups, where each group is a list of record indices
            that appear to be duplicates.
        """
        # Build clusters via union-find
        parent: dict[int, int] = {}

        def find(x: int) -> int:
            while parent.get(x, x) != x:
                parent[x] = parent.get(parent[x], parent[x])
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for indices in self._norm_index.values():
            if len(indices) > 1:
                for idx in indices[1:]:
                    union(indices[0], idx)

        # Collect groups
        groups: dict[int, list[int]] = defaultdict(list)
        for i in range(len(self._records)):
            root = find(i)
            if i in parent or any(i in idxs for idxs in self._norm_index.values() if len(idxs) > 1):
                groups[root].append(i)

        return [g for g in groups.values() if len(g) > 1]

    def find_similar(self, text: str) -> list[tuple[int, float]]:
        """Find records similar to the given text.

        Returns:
            List of (record_index, similarity_score) tuples, sorted by score descending.
        """
        norm = normalize_text(text)
        results: list[tuple[int, float]] = []
        norm_tokens = set(norm.split())

        for i, rec in enumerate(self._records):
            keys = self._extract_normalized_keys(rec)
            best_score = 0.0
            for key in keys:
                if norm == key:
                    best_score = 1.0
                    break
                if norm in key or key in norm:
                    best_score = max(best_score, 0.8)
                    continue
                key_tokens = set(key.split())
                if norm_tokens and key_tokens:
                    overlap = len(norm_tokens & key_tokens)
                    score = overlap / max(len(norm_tokens), len(key_tokens))
                    best_score = max(best_score, score)
            if best_score > 0.3:
                results.append((i, best_score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def add_synonym(
        self,
        record_index: int,
        synonym_text: str,
        synonym_type: str = "EXACT_SYNONYM",
        source: str = "curator",
        occurrence_count: Optional[int] = None,
    ) -> dict:
        """Add a synonym to an existing record.

        Returns:
            The new synonym dict that was added.
        """
        if record_index < 0 or record_index >= len(self._records):
            raise IndexError(f"Record index {record_index} out of range")

        new_syn: dict[str, Any] = {
            "synonym_text": synonym_text,
            "synonym_type": synonym_type,
            "source": source,
        }
        if occurrence_count is not None:
            new_syn["occurrence_count"] = occurrence_count

        rec = self._records[record_index]
        if "synonyms" not in rec or rec["synonyms"] is None:
            rec["synonyms"] = []
        rec["synonyms"].append(new_syn)

        # Update index
        norm = normalize_text(synonym_text)
        self._norm_index.setdefault(norm, []).append(record_index)

        return new_syn

    def merge_records(self, target_index: int, source_index: int) -> dict:
        """Merge source record into target, consolidating synonyms and stats.

        The source record's preferred_term becomes a synonym on the target.
        Occurrence stats are combined. The source record is marked REJECTED.

        Returns:
            The updated target record.
        """
        if target_index == source_index:
            raise ValueError("Cannot merge a record with itself")
        target = self._records[target_index]
        source = self._records[source_index]

        # Add source preferred_term as synonym on target
        self.add_synonym(
            target_index,
            source["preferred_term"],
            synonym_type="EXACT_SYNONYM",
            source="merge",
        )

        # Merge synonyms from source
        existing_norms = self._extract_normalized_keys(target)
        for syn in source.get("synonyms", []) or []:
            text = syn.get("synonym_text", "") if isinstance(syn, dict) else str(syn)
            if normalize_text(text) not in existing_norms:
                if isinstance(syn, dict):
                    target.setdefault("synonyms", []).append(syn)
                else:
                    self.add_synonym(target_index, text, source="merge")
                existing_norms.add(normalize_text(text))

        # Merge occurrence stats
        t_stats = target.get("occurrence_statistics") or {}
        s_stats = source.get("occurrence_statistics") or {}
        if s_stats:
            t_stats["total_occurrences"] = (
                t_stats.get("total_occurrences", 0) + s_stats.get("total_occurrences", 0)
            )
            t_stats["media_count"] = (
                t_stats.get("media_count", 0) + s_stats.get("media_count", 0)
            )
            t_samples = t_stats.get("sample_media", []) or []
            s_samples = s_stats.get("sample_media", []) or []
            t_stats["sample_media"] = list(set(t_samples + s_samples))
            target["occurrence_statistics"] = t_stats

        # Mark source as rejected
        source["mapping_status"] = "REJECTED"

        self._rebuild_index()
        return target
