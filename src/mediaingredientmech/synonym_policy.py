"""Shared policy for labels retained in an ingredient's synonym history."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

# These entries preserve a rejected candidate and its provenance in curated
# YAML.  They are not names the record answers to and must not be exposed by
# search/resolution exports or by the SSSOM ``other`` synonym channel.
NON_RESOLVING_SYNONYM_TYPES = frozenset({"REJECTED_LABEL"})


def is_resolving_synonym(synonym: Mapping[str, Any]) -> bool:
    """Return whether a synonym row is allowed to resolve to its record."""
    synonym_type = str(synonym.get("synonym_type") or "").strip().upper()
    return synonym_type not in NON_RESOLVING_SYNONYM_TYPES
