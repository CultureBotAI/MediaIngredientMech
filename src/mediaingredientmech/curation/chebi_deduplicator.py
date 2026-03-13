"""CHEBI ID deduplicator: Find and merge ingredients with shared CHEBI IDs."""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from mediaingredientmech.curation.ingredient_curator import IngredientCurator

from mediaingredientmech.curation.synonym_manager import SynonymManager

logger = logging.getLogger(__name__)

# Quality ranking for choosing merge target (higher is better)
QUALITY_RANK = {
    "EXACT_MATCH": 5,
    "SYNONYM_MATCH": 4,
    "CLOSE_MATCH": 3,
    "MANUAL_CURATION": 2,
    "LLM_ASSISTED": 1,
    "PROVISIONAL": 0,
}


class CHEBIDeduplicator:
    """Find and merge ingredient records with shared CHEBI IDs.

    This implements the PRIMARY merge rule: Records sharing a CHEBI ID MUST be merged.
    """

    def __init__(self, curator: IngredientCurator):
        """Initialize deduplicator with curator instance.

        Args:
            curator: IngredientCurator managing the records.
        """
        self.curator = curator
        self.synonym_manager = SynonymManager(curator.records)

    def find_chebi_duplicates(self) -> dict[str, list[int]]:
        """Group record indices by shared CHEBI ID.

        Returns:
            Dict mapping CHEBI ID to list of record indices.
            Only includes CHEBI IDs with 2+ records.
        """
        chebi_groups: dict[str, list[int]] = defaultdict(list)

        for idx, record in enumerate(self.curator.records):
            # Skip REJECTED records
            if record.get("mapping_status") == "REJECTED":
                continue

            # Extract CHEBI ID from ontology mapping
            ontology_mapping = record.get("ontology_mapping")
            if not ontology_mapping:
                continue

            ontology_id = ontology_mapping.get("ontology_id", "")
            if not ontology_id or not ontology_id.startswith("CHEBI:"):
                continue

            chebi_groups[ontology_id].append(idx)

        # Filter to only duplicates (2+ records)
        duplicates = {cid: indices for cid, indices in chebi_groups.items() if len(indices) > 1}

        logger.info("Found %d CHEBI IDs with duplicates", len(duplicates))
        return duplicates

    def choose_merge_target(self, duplicate_group: list[int]) -> int:
        """Select best record as merge target.

        Selection criteria (in order):
        1. Highest mapping quality (EXACT_MATCH > SYNONYM_MATCH > ...)
        2. Highest occurrence count
        3. Lowest index (first imported)

        Args:
            duplicate_group: List of record indices with same CHEBI ID.

        Returns:
            Index of the record to use as merge target.
        """
        if not duplicate_group:
            raise ValueError("Cannot choose target from empty group")

        if len(duplicate_group) == 1:
            return duplicate_group[0]

        def score_record(idx: int) -> tuple[int, int, int]:
            """Return (quality_rank, occurrence_count, -index) for sorting."""
            record = self.curator.records[idx]

            # Quality score
            mapping = record.get("ontology_mapping", {})
            quality = mapping.get("mapping_quality", "PROVISIONAL")
            quality_score = QUALITY_RANK.get(quality, 0)

            # Occurrence count
            stats = record.get("occurrence_statistics", {})
            occurrences = stats.get("total_occurrences", 0)

            # Prefer lower index (older/first imported) as tiebreaker
            return (quality_score, occurrences, -idx)

        # Sort by quality (desc), occurrences (desc), index (asc)
        sorted_group = sorted(duplicate_group, key=score_record, reverse=True)
        target_idx = sorted_group[0]

        logger.debug(
            "Selected target index %d from group %s (quality=%s, occurrences=%d)",
            target_idx,
            duplicate_group,
            self.curator.records[target_idx]
            .get("ontology_mapping", {})
            .get("mapping_quality", "UNKNOWN"),
            self.curator.records[target_idx]
            .get("occurrence_statistics", {})
            .get("total_occurrences", 0),
        )

        return target_idx

    def should_auto_merge(self, target_idx: int, source_idx: int) -> tuple[bool, str]:
        """Determine if records should be auto-merged without confirmation.

        Args:
            target_idx: Merge target record index.
            source_idx: Source record index.

        Returns:
            Tuple of (should_merge, reason).
        """
        target = self.curator.records[target_idx]
        source = self.curator.records[source_idx]

        # Get ontology mappings
        target_mapping = target.get("ontology_mapping", {})
        source_mapping = source.get("ontology_mapping", {})

        target_quality = target_mapping.get("mapping_quality", "UNKNOWN")
        source_quality = source_mapping.get("mapping_quality", "UNKNOWN")

        target_chebi = target_mapping.get("ontology_id", "")
        source_chebi = source_mapping.get("ontology_id", "")

        # Must have same CHEBI ID
        if target_chebi != source_chebi:
            return False, "Different CHEBI IDs"

        # Never merge if one is NEEDS_EXPERT
        if (
            target.get("mapping_status") == "NEEDS_EXPERT"
            or source.get("mapping_status") == "NEEDS_EXPERT"
        ):
            return False, "One record is NEEDS_EXPERT"

        # Auto-merge if same quality
        if target_quality == source_quality:
            return True, f"Same CHEBI ID + same quality ({target_quality})"

        # Auto-merge if target has higher quality
        target_rank = QUALITY_RANK.get(target_quality, 0)
        source_rank = QUALITY_RANK.get(source_quality, 0)
        if target_rank > source_rank:
            return True, f"Same CHEBI ID + higher quality target ({target_quality} > {source_quality})"

        # Flag for review if source has higher quality
        return (
            False,
            f"Source has higher quality ({source_quality} > {target_quality}), needs review",
        )

    def merge_duplicates(
        self, dry_run: bool = True, auto_merge: bool = False
    ) -> dict[str, Any]:
        """Find and merge all CHEBI duplicates.

        Args:
            dry_run: If True, only preview merges without executing.
            auto_merge: If True, automatically merge records that pass auto-merge criteria.

        Returns:
            Dict with merge results:
            - merged: List of (target_idx, source_indices, chebi_id) tuples
            - flagged: List of (chebi_id, indices, reason) tuples
            - total_removed: Count of records that will be REJECTED
        """
        duplicates = self.find_chebi_duplicates()

        merged: list[tuple[int, list[int], str]] = []
        flagged: list[tuple[str, list[int], str]] = []
        total_removed = 0

        for chebi_id, indices in duplicates.items():
            # Choose merge target
            target_idx = self.choose_merge_target(indices)
            source_indices = [i for i in indices if i != target_idx]

            # Check if all merges in this group can be auto-merged
            can_auto_merge = True
            reasons = []

            for source_idx in source_indices:
                should_merge, reason = self.should_auto_merge(target_idx, source_idx)
                reasons.append(reason)
                if not should_merge:
                    can_auto_merge = False

            # Execute or flag
            if can_auto_merge and (auto_merge or not dry_run):
                # Perform merges
                for source_idx in sorted(source_indices, reverse=True):
                    if not dry_run:
                        logger.info(
                            "Merging %s (idx %d) into %s (idx %d) - %s",
                            self.curator.records[source_idx].get("preferred_term"),
                            source_idx,
                            self.curator.records[target_idx].get("preferred_term"),
                            target_idx,
                            reasons[source_indices.index(source_idx)],
                        )
                        self.synonym_manager.merge_records(target_idx, source_idx)

                merged.append((target_idx, source_indices, chebi_id))
                total_removed += len(source_indices)
            else:
                # Flag for manual review
                flagged.append((chebi_id, indices, "; ".join(set(reasons))))
                logger.info(
                    "Flagged for review: CHEBI %s with %d records - %s",
                    chebi_id,
                    len(indices),
                    "; ".join(set(reasons)),
                )

        return {
            "merged": merged,
            "flagged": flagged,
            "total_removed": total_removed,
            "dry_run": dry_run,
        }

    def validate_no_chebi_duplicates(self) -> tuple[bool, list[str]]:
        """Validate that no CHEBI ID duplicates remain.

        Returns:
            Tuple of (is_valid, list_of_errors).
        """
        duplicates = self.find_chebi_duplicates()
        if not duplicates:
            return True, []

        errors = []
        for chebi_id, indices in duplicates.items():
            non_rejected = [
                i
                for i in indices
                if self.curator.records[i].get("mapping_status") != "REJECTED"
            ]
            if len(non_rejected) > 1:
                errors.append(
                    f"CHEBI {chebi_id} still has {len(non_rejected)} non-REJECTED records"
                )

        return len(errors) == 0, errors
