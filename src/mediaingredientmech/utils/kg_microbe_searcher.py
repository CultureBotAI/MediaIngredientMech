"""KG-Microbe searcher: Index and search CultureMech mapped ingredients."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Optional

import yaml

logger = logging.getLogger(__name__)


def normalize_text(text: str) -> str:
    """Normalize ingredient text for comparison: lowercase, strip, collapse whitespace."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = text.strip(".,;:")
    return text


class KGMicrobeSearcher:
    """Search and index CultureMech's 995 mapped ingredients by CHEBI ID or name.

    This class provides search capabilities against the KG-Microbe baseline
    (CultureMech mapped ingredients) to help identify duplicates and potential matches.
    """

    def __init__(self, culturemech_path: Path):
        """Initialize searcher by loading CultureMech mapped ingredients.

        Args:
            culturemech_path: Path to CultureMech mapped_ingredients.yaml file.
        """
        self.culturemech_path = Path(culturemech_path)
        self.records: list[dict[str, Any]] = []
        self.chebi_index: dict[str, list[int]] = {}
        self.name_index: dict[str, list[int]] = {}
        self._load_and_index()

    def _load_and_index(self) -> None:
        """Load CultureMech data and build search indices."""
        if not self.culturemech_path.exists():
            logger.warning("CultureMech file not found: %s", self.culturemech_path)
            return

        with open(self.culturemech_path) as f:
            data = yaml.safe_load(f) or {}

        self.records = data.get("mapped_ingredients", []) or []
        logger.info("Loaded %d CultureMech mapped ingredients", len(self.records))

        # Build indices
        self._build_indices()

    def _build_indices(self) -> None:
        """Build CHEBI ID and normalized name indices."""
        self.chebi_index.clear()
        self.name_index.clear()

        for idx, record in enumerate(self.records):
            # Index by CHEBI ID
            ontology_id = record.get("ontology_id", "")
            if ontology_id and ontology_id.startswith("CHEBI:"):
                self.chebi_index.setdefault(ontology_id, []).append(idx)

            # Index by normalized preferred term
            preferred = record.get("preferred_term", "")
            if preferred:
                norm = normalize_text(preferred)
                self.name_index.setdefault(norm, []).append(idx)

            # Index by normalized ontology label
            label = record.get("ontology_label", "")
            if label:
                norm_label = normalize_text(label)
                self.name_index.setdefault(norm_label, []).append(idx)

        logger.info(
            "Built indices: %d CHEBI IDs, %d normalized names",
            len(self.chebi_index),
            len(self.name_index),
        )

    def search_by_chebi_id(self, chebi_id: str) -> list[dict[str, Any]]:
        """Find CultureMech records with matching CHEBI ID.

        Args:
            chebi_id: CHEBI identifier (e.g., "CHEBI:26710")

        Returns:
            List of matching CultureMech records.
        """
        if not chebi_id or not chebi_id.startswith("CHEBI:"):
            return []

        indices = self.chebi_index.get(chebi_id, [])
        return [self.records[i] for i in indices]

    def search_by_name(
        self, name: str, threshold: float = 0.8
    ) -> list[tuple[dict[str, Any], float]]:
        """Fuzzy name search with similarity scores.

        Args:
            name: Ingredient name to search for.
            threshold: Minimum similarity score (0.0-1.0).

        Returns:
            List of (record, score) tuples, sorted by score descending.
        """
        norm = normalize_text(name)
        results: list[tuple[dict[str, Any], float]] = []
        norm_tokens = set(norm.split())

        for idx, record in enumerate(self.records):
            best_score = 0.0

            # Check preferred term
            preferred = record.get("preferred_term", "")
            if preferred:
                score = self._similarity_score(norm, normalize_text(preferred), norm_tokens)
                best_score = max(best_score, score)

            # Check ontology label
            label = record.get("ontology_label", "")
            if label:
                score = self._similarity_score(norm, normalize_text(label), norm_tokens)
                best_score = max(best_score, score)

            if best_score >= threshold:
                results.append((record, best_score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def _similarity_score(self, norm: str, key: str, norm_tokens: set[str]) -> float:
        """Calculate similarity score between normalized strings.

        Returns:
            1.0 for exact match, 0.8 for substring, token overlap ratio otherwise.
        """
        if norm == key:
            return 1.0
        if norm in key or key in norm:
            return 0.8

        key_tokens = set(key.split())
        if norm_tokens and key_tokens:
            overlap = len(norm_tokens & key_tokens)
            return overlap / max(len(norm_tokens), len(key_tokens))

        return 0.0

    def find_matches(self, ingredient_record: dict[str, Any]) -> dict[str, list]:
        """Find all potential matches for an ingredient record.

        Searches both by CHEBI ID (if mapped) and by name similarity.

        Args:
            ingredient_record: MediaIngredientMech ingredient record.

        Returns:
            Dict with 'chebi_matches' and 'name_matches' lists.
        """
        matches = {"chebi_matches": [], "name_matches": []}

        # Search by CHEBI ID if record is mapped
        ontology_mapping = ingredient_record.get("ontology_mapping")
        if ontology_mapping:
            chebi_id = ontology_mapping.get("ontology_id", "")
            if chebi_id and chebi_id.startswith("CHEBI:"):
                chebi_results = self.search_by_chebi_id(chebi_id)
                matches["chebi_matches"] = chebi_results

        # Search by preferred term
        preferred = ingredient_record.get("preferred_term", "")
        if preferred:
            name_results = self.search_by_name(preferred, threshold=0.7)
            matches["name_matches"] = name_results

        return matches

    def get_statistics(self) -> dict[str, Any]:
        """Get statistics about CultureMech data.

        Returns:
            Dict with counts and breakdown by ontology source.
        """
        total = len(self.records)
        source_counts: dict[str, int] = {}

        for record in self.records:
            source = record.get("ontology_source", "UNKNOWN")
            source_counts[source] = source_counts.get(source, 0) + 1

        return {
            "total_records": total,
            "unique_chebi_ids": len(self.chebi_index),
            "unique_names": len(self.name_index),
            "source_breakdown": source_counts,
        }
