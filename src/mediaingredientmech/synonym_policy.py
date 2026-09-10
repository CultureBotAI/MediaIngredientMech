"""Shared policy for labels retained in an ingredient's synonym history."""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

# These entries preserve a rejected candidate and its provenance in curated
# YAML.  They are not names the record answers to and must not be exposed by
# search/resolution exports or by the SSSOM ``other`` synonym channel.
NON_RESOLVING_SYNONYM_TYPES = frozenset({"REJECTED_LABEL"})

# Curation strings that live in ``synonyms`` but are not names anything answers
# to: role/property annotations carried over from the CultureMech import,
# CultureMech original-amount notes, and bare parentheticals like
# ``(sodium salt)`` or ``(for solid medium, alternative)`` that are fragments of
# a name, not a name. Publishing them as resolvable labels would make internal
# notes resolve to real ingredients.
_CURATION_NOTE_SYNONYM_TEXT = r"^\s*(?:role|properties|cross-references?|original amount)\s*:"
_BARE_PARENTHETICAL = r"^\s*\([^)]*\)\s*$"

CURATION_NOTE_SYNONYM_TEXT = re.compile(_CURATION_NOTE_SYNONYM_TEXT, re.IGNORECASE)
NON_RESOLVING_SYNONYM_TEXT = re.compile(
    f"{_CURATION_NOTE_SYNONYM_TEXT}|{_BARE_PARENTHETICAL}",
    re.IGNORECASE,
)


def is_curation_note_synonym_text(text: Any) -> bool:
    """Return whether synonym text is an importer or curator note."""
    if not text:
        return False
    return bool(CURATION_NOTE_SYNONYM_TEXT.match(str(text)))


def is_resolving_synonym_text(text: Any) -> bool:
    """Return whether synonym text is a real label for a record."""
    if not text:
        return False
    return not NON_RESOLVING_SYNONYM_TEXT.match(str(text))


def is_resolving_synonym(synonym: Mapping[str, Any]) -> bool:
    """Return whether a synonym row is allowed to resolve to its record."""
    synonym_type = str(synonym.get("synonym_type") or "").strip().upper()
    if synonym_type in NON_RESOLVING_SYNONYM_TYPES:
        return False
    return is_resolving_synonym_text(synonym.get("synonym_text"))
