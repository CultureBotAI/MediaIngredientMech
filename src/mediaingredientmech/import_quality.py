"""Conservative mapping-quality translation at the CultureMech boundary.

CultureMech's current aggregate writes ``DIRECT_MATCH`` as a default assumption
for every mapped ingredient. It does not preserve whether the recipe surface
matched an ontology primary label, a synonym, or some other lookup path. MIM
must therefore not translate that value to its stronger, label-level
``EXACT_MATCH`` grade.
"""

from __future__ import annotations


def map_culturemech_quality(source_quality: str | None) -> str:
    """Translate only source grades whose MIM meaning is actually known."""
    if source_quality is None:
        return "PROVISIONAL"
    mapping = {
        "EXACT_MATCH": "EXACT_MATCH",
        "SYNONYM_MATCH": "SYNONYM_MATCH",
        "CAS_RN_LOOKUP": "CAS_RN_LOOKUP",
        "CLOSE_MATCH": "CLOSE_MATCH",
        "MANUAL_CURATION": "MANUAL_CURATION",
    }
    return mapping.get(source_quality, "PROVISIONAL")


def culturemech_quality_note(
    source_quality: str | None,
    imported_quality: str,
    preferred_term: object,
    ontology_label: object,
    *,
    operation: str = "Imported",
) -> str:
    """Explain the translation, retaining source surfaces for later review."""
    prefix = f"{operation} from CultureMech pipeline, source quality={source_quality or 'MISSING'}"
    if source_quality != "DIRECT_MATCH":
        return f"{prefix}; MIM quality={imported_quality}"
    return (
        f"{prefix}; MIM quality=PROVISIONAL because CultureMech DIRECT_MATCH is an "
        f"aggregate default, not preserved primary-label/synonym provenance (#317); "
        f"source surfaces were preferred_term={preferred_term!r}, "
        f"ontology_label={ontology_label!r}"
    )
