"""Validate ontology term references (CHEBI, FOODON, etc.) in ingredient records."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

# CURIE pattern broadened to match prefixes actually present in mapped
# records: prefix may include letters of either case and an optional dot, and
# local IDs may be alphanumeric (`NCIT:C80654`) or contain hyphens
# (`cas:247167-54-0`). Prefix case is preserved (not normalised) — KNOWN_PREFIXES
# is checked case-sensitively against the SSSOM curie_map below.
_CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9.]*):([A-Za-z0-9][A-Za-z0-9._~-]*)$")

# Recognised ontology prefixes. Case-sensitive (e.g. `mesh:` and `MESH:` are
# both accepted, but only the exact spellings listed here); keep in sync with
# the SSSOM curie_map that the claw builder emits for ingredient mappings.
KNOWN_PREFIXES = {
    "CHEBI",
    "FOODON",
    "NCIT",
    "MESH",
    "mesh",
    "UBERON",
    "ENVO",
    "MICRO",
    "BTO",
    "cas",
    "kgmicrobe.compound",
    "kgmicrobe.ingredient",
    "registry",
}


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


_CAS_RN_RE = re.compile(r"\b(\d{2,7}-\d{2}-\d)\b")


def find_cas_as_chebi_violations(rec: dict[str, Any]) -> list[tuple[str, str, str]]:
    """Return ``(field_path, chebi_id, cas_rn)`` when a CHEBI ID's digits equal a de-hyphenated CAS RN (#702)."""
    cas_map: dict[str, str] = {}
    chem = rec.get("chemical_properties")
    if isinstance(chem, dict) and chem.get("cas_rn"):
        for m in _CAS_RN_RE.finditer(str(chem["cas_rn"])):
            rn = m.group(1)
            cas_map[rn.replace("-", "")] = rn
    for sf in rec.get("supplied_form") or []:
        if isinstance(sf, dict) and sf.get("cas_rn"):
            for m in _CAS_RN_RE.finditer(str(sf["cas_rn"])):
                rn = m.group(1)
                cas_map[rn.replace("-", "")] = rn
    for syn in rec.get("synonyms") or []:
        if isinstance(syn, dict) and syn.get("synonym_text"):
            if (syn.get("synonym_type") or "").strip().upper() == "REJECTED_LABEL":
                continue
            for m in _CAS_RN_RE.finditer(str(syn["synonym_text"])):
                rn = m.group(1)
                cas_map[rn.replace("-", "")] = rn
    if not cas_map:
        return []
    violations: list[tuple[str, str, str]] = []
    ident = str(rec.get("identifier") or "").strip()
    if ident.startswith("CHEBI:"):
        digits = ident.split(":", 1)[1].strip()
        if digits in cas_map:
            violations.append(("identifier", ident, cas_map[digits]))
    mapping = rec.get("ontology_mapping")
    if isinstance(mapping, dict):
        oid = str(mapping.get("ontology_id") or "").strip()
        if oid.startswith("CHEBI:"):
            digits = oid.split(":", 1)[1].strip()
            if digits in cas_map:
                violations.append(("ontology_mapping.ontology_id", oid, cas_map[digits]))
    return violations


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

    # Accept both the collection shape (`ingredients: [...]`) and the
    # individual-record shape (the document itself is an IngredientRecord).
    # Match schema_validator: a record has either `identifier` (canonical) or
    # `ontology_id` (legacy) as its primary key. Also accept any document with
    # an `ontology_mapping` block.
    ingredients = data.get("ingredients")
    if not isinstance(ingredients, list):
        if (
            isinstance(data.get("ontology_mapping"), dict)
            or "identifier" in data
            or "ontology_id" in data
        ):
            ingredients = [data]
            path_prefix = "$"
        else:
            return result
    else:
        path_prefix = None

    oak_was_used = False

    for i, rec in enumerate(ingredients):
        if not isinstance(rec, dict):
            continue
        rec_prefix = path_prefix if path_prefix is not None else f"$.ingredients[{i}]"
        for field_name, chebi_id, cas_rn in find_cas_as_chebi_violations(rec):
            result.messages.append(
                OntologyMessage(
                    "error",
                    f"{rec_prefix}.{field_name}",
                    f"CAS-as-ChEBI violation (#702): {chebi_id} has digits matching de-hyphenated CAS RN {cas_rn}",
                )
            )
        mapping = rec.get("ontology_mapping")
        if not isinstance(mapping, dict):
            continue

        oid = mapping.get("ontology_id")
        if oid is None:
            continue

        result.terms_checked += 1
        path = f"{rec_prefix}.ontology_mapping"

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
