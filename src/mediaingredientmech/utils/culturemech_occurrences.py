"""Helpers for CultureMech occurrence-table rows."""

from __future__ import annotations

import re
from collections.abc import Mapping

AIR_DRIED_GARDEN_SOIL_ID = "kgmicrobe.ingredient:air-dried_garden_soil"


def _source_label_key(value: str) -> str:
    """Normalize exact source labels without making broad lexical guesses."""
    value = re.sub(r"\s*-\s*", "-", value.strip().casefold())
    value = re.sub(r"-+", "-", value)
    return re.sub(r"\s+", " ", value)


# CultureMech's vendored MIM label index can lag local MIM identity curation.
# These are source labels that CultureMech still resolves to a broader parent,
# but MIM now publishes as narrower local registry records.
SOURCE_LABEL_IDENTIFIER_OVERRIDES = {
    _source_label_key("air-dried garden soil"): AIR_DRIED_GARDEN_SOIL_ID,
}


def mim_identifier_for_occurrence(row: Mapping[str, str]) -> str:
    """Return the MIM identifier that should own one CultureMech occurrence row."""
    source_label = _source_label_key(row.get("preferred_term") or "")
    return SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(
        source_label,
        (row.get("resolved_identifier") or "").strip(),
    )
