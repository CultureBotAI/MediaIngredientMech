"""Validate ontology term references (CHEBI, FOODON, etc.) in ingredient records."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

_CURIE_RE = re.compile(r"^([A-Z]+):([0-9]+)$")

# Recognised ontology prefixes from the schema
KNOWN_PREFIXES = {"CHEBI", "FOODON", "NCIT", "MESH", "UBERON", "ENVO"}


@dataclass
class OntologyMessage:
    level: str  # "error" or "warning"
    path: str
    message: str


@dataclass
class OntologyValidationResult:
    file_path: str
    messages: list[OntologyMessage] = field(default_factory=list)
    terms_checked: int = 0
    terms_valid: int = 0
    oak_available: bool = False

    @property
    def errors(self) -> list[OntologyMessage]:
        return [m for m in self.messages if m.level == "error"]

    @property
    def warnings(self) -> list[OntologyMessage]:
        return [m for m in self.messages if m.level == "warning"]


def _try_get_oak_adapter(prefix: str):
    """Try to get an OAK adapter for the given prefix. Returns None if unavailable."""
    try:
        from oaklib import get_adapter  # type: ignore[import-untyped]
    except ImportError:
        return None

    # Map prefix to OAK sqlite source
    prefix_to_source = {
        "CHEBI": "sqlite:obo:chebi",
        "FOODON": "sqlite:obo:foodon",
        "NCIT": "sqlite:obo:ncit",
        "UBERON": "sqlite:obo:uberon",
        "ENVO": "sqlite:obo:envo",
    }
    source = prefix_to_source.get(prefix)
    if source is None:
        return None
    try:
        return get_adapter(source)
    except Exception:
        return None


# Cache adapters so we only load each ontology once per session
_adapter_cache: dict[str, Any] = {}
_adapter_failures: set[str] = set()


def _get_adapter(prefix: str):
    if prefix in _adapter_failures:
        return None
    if prefix not in _adapter_cache:
        adapter = _try_get_oak_adapter(prefix)
        if adapter is None:
            _adapter_failures.add(prefix)
            return None
        _adapter_cache[prefix] = adapter
    return _adapter_cache[prefix]


def validate_curie_format(curie: str) -> str | None:
    """Return an error string if the CURIE format is invalid, else None."""
    m = _CURIE_RE.match(curie)
    if not m:
        return f"'{curie}' does not match CURIE pattern PREFIX:NUMERIC_ID"
    prefix = m.group(1)
    if prefix not in KNOWN_PREFIXES:
        return f"Unknown ontology prefix '{prefix}'. Known: {sorted(KNOWN_PREFIXES)}"
    return None


def validate_term_via_oak(curie: str, expected_label: str | None = None) -> list[OntologyMessage]:
    """Use OAK to verify that a term exists and optionally check its label."""
    msgs: list[OntologyMessage] = []
    m = _CURIE_RE.match(curie)
    if not m:
        return msgs  # format errors are caught elsewhere
    prefix = m.group(1)
    adapter = _get_adapter(prefix)
    if adapter is None:
        return msgs  # OAK not available for this prefix

    try:
        label = adapter.label(curie)
    except Exception:
        msgs.append(OntologyMessage("warning", curie, f"OAK lookup failed for {curie}"))
        return msgs

    if label is None:
        msgs.append(OntologyMessage("error", curie, f"Term {curie} not found in {prefix} ontology"))
    elif expected_label and label.lower() != expected_label.lower():
        msgs.append(
            OntologyMessage(
                "warning",
                curie,
                f"Label mismatch for {curie}: expected '{expected_label}', ontology has '{label}'",
            )
        )
    return msgs


def validate_records(
    data: dict[str, Any],
    source: str = "<inline>",
    use_oak: bool = True,
) -> OntologyValidationResult:
    """Validate ontology references in ingredient records.

    Args:
        data: Parsed YAML data (IngredientCollection).
        source: File path for reporting.
        use_oak: Whether to attempt OAK lookups (set False for fast format-only checks).
    """
    result = OntologyValidationResult(file_path=source)

    ingredients = data.get("ingredients")
    if not isinstance(ingredients, list):
        return result

    oak_was_used = False

    for i, rec in enumerate(ingredients):
        if not isinstance(rec, dict):
            continue
        mapping = rec.get("ontology_mapping")
        if not isinstance(mapping, dict):
            continue

        oid = mapping.get("ontology_id")
        if oid is None:
            continue

        result.terms_checked += 1
        path = f"$.ingredients[{i}].ontology_mapping"

        # Format check
        fmt_err = validate_curie_format(str(oid))
        if fmt_err:
            result.messages.append(OntologyMessage("error", path, fmt_err))
            continue

        result.terms_valid += 1  # format is valid

        # OAK lookup
        if use_oak:
            label = mapping.get("ontology_label")
            oak_msgs = validate_term_via_oak(str(oid), expected_label=label)
            if oak_msgs:
                oak_was_used = True
                for om in oak_msgs:
                    om.path = path
                    if om.level == "error":
                        result.terms_valid -= 1
                result.messages.extend(oak_msgs)
            elif _get_adapter(_CURIE_RE.match(str(oid)).group(1)) is not None:  # type: ignore[union-attr]
                oak_was_used = True

    result.oak_available = oak_was_used
    return result
