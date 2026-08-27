"""Corpus-level validation for ingredient component partonomy.

LinkML validates each ``StockComponent`` in isolation, but the important
invariants are relational: a local reference must resolve somewhere in the
active MIM catalog, a parent cannot contain itself, and concentration values
and units form a pair.  This module keeps those checks OAK- and network-free.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$")
COMPONENT_PARENT_TYPES = frozenset({"NAMED_MEDIUM", "UNDEFINED_MIXTURE", "STOCK_SOLUTION"})


@dataclass(frozen=True)
class PartonomyViolation:
    """One component-partonomy invariant failure."""

    code: str
    record_id: str
    message: str

    def __str__(self) -> str:
        return f"{self.code}\t{self.record_id}\t{self.message}"


def _normalise_label(value: object) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return " ".join(text.split())


def _active_identifier_labels(
    records: Iterable[dict[str, Any]],
) -> dict[str, set[str]]:
    """Labels for identifiers represented by at least one non-rejected MIM record.

    The historical catalog contains baseline-tracked duplicate identifiers, so
    resolution intentionally means "one or more records claim this identity",
    not "one physical YAML document".
    """

    index: dict[str, set[str]] = {}
    for record in records:
        identifier = record.get("identifier")
        if not identifier or record.get("mapping_status") == "REJECTED":
            continue
        labels = index.setdefault(str(identifier), set())
        labels.add(_normalise_label(record.get("preferred_term")))
        labels.add(_normalise_label((record.get("ontology_mapping") or {}).get("ontology_label")))
        for synonym in record.get("synonyms") or []:
            labels.add(_normalise_label(synonym.get("synonym_text")))
        labels.discard("")
    return index


def validate_component_partonomy(
    records: Iterable[dict[str, Any]],
) -> list[PartonomyViolation]:
    """Return every semantic partonomy violation in ``records``."""

    materialised = list(records)
    active_labels = _active_identifier_labels(materialised)
    active_ids = set(active_labels)
    violations: list[PartonomyViolation] = []

    def add(code: str, record_id: str, message: str) -> None:
        violations.append(PartonomyViolation(code, record_id, message))

    for record in materialised:
        record_id = str(record.get("identifier") or "<missing identifier>")
        components = record.get("components") or []
        assertion = record.get("component_assertion")
        parent_labels = {
            _normalise_label(record.get("preferred_term")),
            _normalise_label((record.get("ontology_mapping") or {}).get("ontology_label")),
        }
        parent_labels.update(
            _normalise_label(synonym.get("synonym_text"))
            for synonym in record.get("synonyms") or []
        )
        parent_labels.discard("")

        if components and not assertion:
            add(
                "MISSING_ASSERTION",
                record_id,
                "components requires component_assertion with method and evidence",
            )
        if not components and assertion:
            add(
                "ORPHAN_ASSERTION",
                record_id,
                "component_assertion is present but components is empty",
            )
        if components and record.get("ingredient_type") not in COMPONENT_PARENT_TYPES:
            add(
                "INVALID_PARENT_TYPE",
                record_id,
                "components is only valid for a medium, mixture, or stock solution",
            )
        if assertion:
            evidence = assertion.get("evidence") if isinstance(assertion, dict) else None
            if not evidence:
                add("MISSING_ASSERTION_EVIDENCE", record_id, "component_assertion needs evidence")
            else:
                for position, item in enumerate(evidence, start=1):
                    if not str((item or {}).get("source") or "").strip():
                        add(
                            "BLANK_EVIDENCE_SOURCE",
                            record_id,
                            f"component assertion evidence {position} has no source",
                        )
        seen_ids: dict[str, int] = {}
        seen_names: dict[str, int] = {}
        for position, component in enumerate(components, start=1):
            component_id = str(component.get("component_id") or "").strip()
            component_name = str(component.get("component_name") or "").strip()
            scope = component.get("reference_scope")
            where = f"component {position} ({component_name or '<unnamed>'})"

            if not component_name:
                add("BLANK_COMPONENT_NAME", record_id, f"component {position} has no name")

            if component_id and not CURIE_RE.fullmatch(component_id):
                add("MALFORMED_CURIE", record_id, f"{where}: {component_id!r}")

            if scope == "MIM_CATALOG":
                if not component_id:
                    add("MISSING_COMPONENT_ID", record_id, f"{where}: MIM_CATALOG needs an id")
                elif component_id not in active_ids:
                    add(
                        "UNRESOLVED_MIM_REFERENCE",
                        record_id,
                        f"{where}: no active MIM record has identifier {component_id}",
                    )
                elif _normalise_label(component_name) not in active_labels[component_id]:
                    add(
                        "REFERENCE_LABEL_MISMATCH",
                        record_id,
                        f"{where}: name is not a preferred term, ontology label, or synonym "
                        f"of an active {component_id} record",
                    )
            elif scope == "EXTERNAL_TERM":
                if not component_id:
                    add("MISSING_COMPONENT_ID", record_id, f"{where}: EXTERNAL_TERM needs an id")
                elif component_id in active_ids:
                    add(
                        "STALE_EXTERNAL_SCOPE",
                        record_id,
                        f"{where}: {component_id} is now represented in MIM",
                    )
            elif scope == "UNMAPPED":
                if component_id:
                    add(
                        "UNMAPPED_WITH_ID",
                        record_id,
                        f"{where}: UNMAPPED must omit component_id",
                    )
            else:
                add("MISSING_REFERENCE_SCOPE", record_id, f"{where}: scope is required")

            if component_id == record_id:
                add("SELF_REFERENCE", record_id, f"{where}: a record cannot contain itself")
            if _normalise_label(component_name) in parent_labels:
                add(
                    "SELF_REFERENCE_NAME",
                    record_id,
                    f"{where}: component name repeats the parent identity",
                )

            if component_id and component_id in seen_ids:
                add(
                    "DUPLICATE_COMPONENT_ID",
                    record_id,
                    f"{where}: repeats the id from component {seen_ids[component_id]}",
                )
            elif component_id:
                seen_ids[component_id] = position

            name_key = _normalise_label(component_name)
            if name_key and name_key in seen_names:
                add(
                    "DUPLICATE_COMPONENT_NAME",
                    record_id,
                    f"{where}: repeats the name from component {seen_names[name_key]}",
                )
            elif name_key:
                seen_names[name_key] = position

            has_value = bool(str(component.get("concentration_value") or "").strip())
            has_unit = bool(str(component.get("concentration_unit") or "").strip())
            if has_value != has_unit:
                add(
                    "INCOMPLETE_CONCENTRATION",
                    record_id,
                    f"{where}: concentration_value and concentration_unit must occur together",
                )

    return violations


def load_ingredient_records(ingredients_dir: Path) -> list[dict[str, Any]]:
    """Load individual ingredient YAML files below ``ingredients_dir``."""

    records: list[dict[str, Any]] = []
    for path in sorted(ingredients_dir.rglob("*.yaml")):
        try:
            document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            raise ValueError(f"{path}: invalid YAML: {exc}") from exc
        if not isinstance(document, dict):
            raise ValueError(f"{path}: expected a mapping")
        records.append(document)
    return records


def load_curated_records(curated_dir: Path) -> list[dict[str, Any]]:
    """Load the two authoritative curated ingredient collections."""

    records: list[dict[str, Any]] = []
    for filename in ("mapped_ingredients.yaml", "unmapped_ingredients.yaml"):
        path = curated_dir / filename
        try:
            document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            raise ValueError(f"{path}: invalid YAML: {exc}") from exc
        ingredients = document.get("ingredients") if isinstance(document, dict) else None
        if not isinstance(ingredients, list):
            raise ValueError(f"{path}: expected an ingredients list")
        if not all(isinstance(record, dict) for record in ingredients):
            raise ValueError(f"{path}: every ingredient must be a mapping")
        records.extend(ingredients)
    return records
