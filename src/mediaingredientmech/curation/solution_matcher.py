"""Solution/buffer/stock matcher: High-confidence name matching for solution-type ingredients."""

from __future__ import annotations

import logging
import re
from typing import Optional

logger = logging.getLogger(__name__)


def normalize_text(text: str) -> str:
    """Normalize ingredient text for comparison: lowercase, strip, collapse whitespace."""
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    text = text.strip(".,;:")
    return text


class SolutionMatcher:
    """High-confidence name matching for solutions, buffers, and stocks.

    Detects solution/buffer/stock patterns and performs enhanced name normalization
    to identify duplicates that share the same base chemical but differ in type notation.
    """

    # Patterns for detecting solution types
    PATTERNS = {
        "solution": re.compile(r"^(.+?)\s+solution$", re.IGNORECASE),
        "buffer": re.compile(r"^(.+?)\s+buffer$", re.IGNORECASE),
        "stock": re.compile(r"^(.+?)\s+stock(?:\s+solution)?$", re.IGNORECASE),
        "trace": re.compile(r"^trace\s+(elements?|metals?|solution)$", re.IGNORECASE),
        "macro": re.compile(r"^macro\s+(solution|nutrients?)$", re.IGNORECASE),
        "micro": re.compile(r"^micro(?:nutrient)?s?\s+solution$", re.IGNORECASE),
        "vitamin": re.compile(r"^vitamin\s+(solution|mix|mixture)$", re.IGNORECASE),
        "mineral": re.compile(r"^mineral\s+(solution|mix|mixture)$", re.IGNORECASE),
    }

    # Common concentration patterns to normalize
    CONCENTRATION_PATTERN = re.compile(
        r"\b(\d+\.?\d*)\s*(m|mm|µm|um|nm|g/l|mg/l|µg/l|ug/l|%|x)\b", re.IGNORECASE
    )

    def detect_type(self, name: str) -> str:
        """Detect ingredient type based on name patterns.

        Args:
            name: Ingredient name to classify.

        Returns:
            Type string: SOLUTION, BUFFER, STOCK, TRACE_METAL, MACRO, MICRO,
            VITAMIN, MINERAL, or CHEMICAL.
        """
        norm = normalize_text(name)

        # Check for specific patterns
        if self.PATTERNS["trace"].search(norm):
            return "TRACE_METAL"
        if self.PATTERNS["macro"].search(norm):
            return "MACRO"
        if self.PATTERNS["micro"].search(norm):
            return "MICRO"
        if self.PATTERNS["vitamin"].search(norm):
            return "VITAMIN"
        if self.PATTERNS["mineral"].search(norm):
            return "MINERAL"
        if self.PATTERNS["solution"].search(norm):
            return "SOLUTION"
        if self.PATTERNS["buffer"].search(norm):
            return "BUFFER"
        if self.PATTERNS["stock"].search(norm):
            return "STOCK"

        return "CHEMICAL"

    def extract_base_name(self, name: str) -> str:
        """Extract base chemical name by stripping solution/buffer/stock suffix.

        Args:
            name: Ingredient name.

        Returns:
            Base name with type suffix removed.
        """
        norm = normalize_text(name)

        # Try each pattern to extract base name
        for pattern_type, pattern in self.PATTERNS.items():
            match = pattern.search(norm)
            if match:
                # Return the captured group (base name before type suffix)
                return match.group(1).strip()

        # No pattern matched, return normalized name
        return norm

    def normalize_concentration(self, name: str) -> str:
        """Normalize concentration units in name for comparison.

        Converts common concentration variations:
        - µM/uM → um
        - g/L → g_l
        - % → pct
        - 10x → 10x (preserved)

        Args:
            name: Ingredient name with possible concentration.

        Returns:
            Name with normalized concentration units.
        """
        result = name.lower()

        # Normalize common variations
        result = result.replace("µm", "um").replace("µg", "ug")
        result = result.replace("g/l", "g_l").replace("mg/l", "mg_l").replace("ug/l", "ug_l")
        result = result.replace("%", "pct")

        return result

    def match_confidence(self, name1: str, name2: str) -> float:
        """Calculate similarity confidence for two solution/buffer/stock names.

        Scoring:
        - 1.0: Exact normalized base name match
        - 0.9: Same chemical + same type category (both solutions, both buffers, etc.)
        - 0.8: Same chemical + different but compatible types (solution vs. stock)
        - 0.7: Similar base name (token overlap > 0.8)
        - <0.7: Token-based similarity

        Args:
            name1: First ingredient name.
            name2: Second ingredient name.

        Returns:
            Confidence score 0.0-1.0.
        """
        # Detect types
        type1 = self.detect_type(name1)
        type2 = self.detect_type(name2)

        # Extract base names
        base1 = self.extract_base_name(name1)
        base2 = self.extract_base_name(name2)

        # Normalize concentrations if present
        base1_norm = self.normalize_concentration(base1)
        base2_norm = self.normalize_concentration(base2)

        # Exact base name match
        if base1_norm == base2_norm:
            # Same type → highest confidence
            if type1 == type2:
                return 1.0
            # Compatible types (solution/buffer/stock are interchangeable in some contexts)
            if {type1, type2}.issubset({"SOLUTION", "BUFFER", "STOCK"}):
                return 0.9
            # Different types but same base chemical
            return 0.8

        # Token-based similarity for base names
        tokens1 = set(base1_norm.split())
        tokens2 = set(base2_norm.split())

        if tokens1 and tokens2:
            overlap = len(tokens1 & tokens2)
            token_score = overlap / max(len(tokens1), len(tokens2))

            # High token overlap suggests similar ingredients
            if token_score > 0.8:
                return 0.7
            return token_score * 0.6  # Scale down partial matches

        return 0.0

    def find_solution_duplicates(
        self, records: list[dict], threshold: float = 0.9
    ) -> list[tuple[int, int, float]]:
        """Find potential duplicate solution/buffer/stock records.

        Args:
            records: List of ingredient records.
            threshold: Minimum confidence score for duplicate detection.

        Returns:
            List of (idx1, idx2, confidence) tuples for potential duplicates.
        """
        duplicates: list[tuple[int, int, float]] = []

        # Filter to solution-type ingredients
        solution_indices = []
        for idx, record in enumerate(records):
            if record.get("mapping_status") == "REJECTED":
                continue

            name = record.get("preferred_term", "")
            ing_type = self.detect_type(name)

            # Only check solution-type ingredients
            if ing_type in {
                "SOLUTION",
                "BUFFER",
                "STOCK",
                "TRACE_METAL",
                "MACRO",
                "MICRO",
                "VITAMIN",
                "MINERAL",
            }:
                solution_indices.append(idx)

        # Compare all pairs
        for i, idx1 in enumerate(solution_indices):
            for idx2 in solution_indices[i + 1 :]:
                name1 = records[idx1].get("preferred_term", "")
                name2 = records[idx2].get("preferred_term", "")

                confidence = self.match_confidence(name1, name2)
                if confidence >= threshold:
                    duplicates.append((idx1, idx2, confidence))

        logger.info(
            "Found %d potential solution/buffer/stock duplicates (threshold=%.2f)",
            len(duplicates),
            threshold,
        )
        return duplicates

    def get_merge_recommendation(
        self, record1: dict, record2: dict, confidence: float
    ) -> tuple[bool, str]:
        """Get merge recommendation for two solution-type records.

        Args:
            record1: First ingredient record.
            record2: Second ingredient record.
            confidence: Match confidence score.

        Returns:
            Tuple of (should_merge, reason).
        """
        name1 = record1.get("preferred_term", "")
        name2 = record2.get("preferred_term", "")

        type1 = self.detect_type(name1)
        type2 = self.detect_type(name2)

        # Perfect match (1.0) → auto-merge
        if confidence >= 1.0:
            return True, f"Exact base name match ({type1}, {type2})"

        # Very high confidence (0.9) + same type → auto-merge
        if confidence >= 0.9 and type1 == type2:
            return True, f"Same base chemical and type ({type1})"

        # High confidence (0.9) but different types → flag for review
        if confidence >= 0.9:
            return (
                False,
                f"Same base chemical but different types ({type1} vs {type2}), needs review",
            )

        # Moderate confidence (0.7-0.89) → flag for review
        if confidence >= 0.7:
            return False, f"Moderate similarity ({confidence:.2f}), recommend manual review"

        # Low confidence → don't merge
        return False, f"Low confidence ({confidence:.2f})"
