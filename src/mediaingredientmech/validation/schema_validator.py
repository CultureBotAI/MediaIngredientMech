"""Validate YAML data files against the MediaIngredientMech LinkML schema."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "mediaingredientmech.yaml"

# Enum values extracted at module load from the schema YAML so validation
# stays in sync without needing linkml-runtime to parse the schema.
_SCHEMA_CACHE: dict[str, Any] | None = None


def _load_schema() -> dict[str, Any]:
    global _SCHEMA_CACHE
    if _SCHEMA_CACHE is None:
        with open(SCHEMA_PATH) as fh:
            _SCHEMA_CACHE = yaml.safe_load(fh)
    return _SCHEMA_CACHE


def _enum_values(enum_name: str) -> set[str]:
    schema = _load_schema()
    enum_def = schema.get("enums", {}).get(enum_name, {})
    return set(enum_def.get("permissible_values", {}).keys())


@dataclass
class ValidationMessage:
    level: str  # "error" or "warning"
    path: str  # JSONPath-like location
    message: str


@dataclass
class SchemaValidationResult:
    file_path: str
    messages: list[ValidationMessage] = field(default_factory=list)

    @property
    def errors(self) -> list[ValidationMessage]:
        return [m for m in self.messages if m.level == "error"]

    @property
    def warnings(self) -> list[ValidationMessage]:
        return [m for m in self.messages if m.level == "warning"]

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0


# ---------------------------------------------------------------------------
# Validators for individual classes
# ---------------------------------------------------------------------------

_CURIE_PATTERN = re.compile(r"^[A-Z]+:[0-9]+$")
_ONTOLOGY_SOURCES = _enum_values("OntologySourceEnum") if SCHEMA_PATH.exists() else set()
_MAPPING_STATUSES = _enum_values("MappingStatusEnum") if SCHEMA_PATH.exists() else set()
_MAPPING_QUALITIES = _enum_values("MappingQualityEnum") if SCHEMA_PATH.exists() else set()
_EVIDENCE_TYPES = _enum_values("EvidenceTypeEnum") if SCHEMA_PATH.exists() else set()
_SYNONYM_TYPES = _enum_values("SynonymTypeEnum") if SCHEMA_PATH.exists() else set()
_CURATION_ACTIONS = _enum_values("CurationActionEnum") if SCHEMA_PATH.exists() else set()


def _check_required(data: dict, field_name: str, path: str, msgs: list[ValidationMessage]):
    if field_name not in data or data[field_name] is None:
        msgs.append(ValidationMessage("error", path, f"Missing required field '{field_name}'"))
        return False
    return True


def _check_enum(
    data: dict,
    field_name: str,
    allowed: set[str],
    path: str,
    msgs: list[ValidationMessage],
):
    val = data.get(field_name)
    if val is not None and val not in allowed:
        msgs.append(
            ValidationMessage(
                "error", path, f"Invalid value '{val}' for '{field_name}'. Allowed: {sorted(allowed)}"
            )
        )


def _check_type(
    data: dict,
    field_name: str,
    expected_type: type,
    type_name: str,
    path: str,
    msgs: list[ValidationMessage],
):
    val = data.get(field_name)
    if val is not None and not isinstance(val, expected_type):
        msgs.append(
            ValidationMessage(
                "warning", path, f"Field '{field_name}' should be {type_name}, got {type(val).__name__}"
            )
        )


def _validate_mapping_evidence(ev: Any, path: str, msgs: list[ValidationMessage]):
    if not isinstance(ev, dict):
        msgs.append(ValidationMessage("error", path, "Evidence entry must be a mapping"))
        return
    _check_required(ev, "evidence_type", path, msgs)
    _check_enum(ev, "evidence_type", _EVIDENCE_TYPES, path, msgs)
    score = ev.get("confidence_score")
    if score is not None:
        try:
            score_f = float(score)
            if not (0.0 <= score_f <= 1.0):
                msgs.append(
                    ValidationMessage("warning", path, f"confidence_score {score_f} outside 0.0-1.0")
                )
        except (TypeError, ValueError):
            msgs.append(
                ValidationMessage("error", path, f"confidence_score '{score}' is not a number")
            )


def _validate_ontology_mapping(mapping: Any, path: str, msgs: list[ValidationMessage]):
    if not isinstance(mapping, dict):
        msgs.append(ValidationMessage("error", path, "ontology_mapping must be a mapping"))
        return
    _check_required(mapping, "ontology_id", path, msgs)
    _check_required(mapping, "ontology_label", path, msgs)
    _check_required(mapping, "ontology_source", path, msgs)
    _check_required(mapping, "mapping_quality", path, msgs)

    oid = mapping.get("ontology_id")
    if oid and not _CURIE_PATTERN.match(str(oid)):
        msgs.append(
            ValidationMessage("error", path, f"ontology_id '{oid}' does not match CURIE pattern ^[A-Z]+:[0-9]+$")
        )

    _check_enum(mapping, "ontology_source", _ONTOLOGY_SOURCES, path, msgs)
    _check_enum(mapping, "mapping_quality", _MAPPING_QUALITIES, path, msgs)

    for i, ev in enumerate(mapping.get("evidence") or []):
        _validate_mapping_evidence(ev, f"{path}.evidence[{i}]", msgs)


def _validate_synonym(syn: Any, path: str, msgs: list[ValidationMessage]):
    if not isinstance(syn, dict):
        msgs.append(ValidationMessage("error", path, "Synonym entry must be a mapping"))
        return
    _check_required(syn, "synonym_text", path, msgs)
    _check_enum(syn, "synonym_type", _SYNONYM_TYPES, path, msgs)
    _check_type(syn, "occurrence_count", int, "integer", path, msgs)


def _validate_occurrence_stats(stats: Any, path: str, msgs: list[ValidationMessage]):
    if not isinstance(stats, dict):
        msgs.append(ValidationMessage("error", path, "occurrence_statistics must be a mapping"))
        return
    _check_required(stats, "total_occurrences", path, msgs)
    _check_required(stats, "media_count", path, msgs)
    _check_type(stats, "total_occurrences", int, "integer", path, msgs)
    _check_type(stats, "media_count", int, "integer", path, msgs)


def _validate_curation_event(evt: Any, path: str, msgs: list[ValidationMessage]):
    if not isinstance(evt, dict):
        msgs.append(ValidationMessage("error", path, "Curation event must be a mapping"))
        return
    _check_required(evt, "timestamp", path, msgs)
    _check_required(evt, "curator", path, msgs)
    _check_required(evt, "action", path, msgs)
    _check_enum(evt, "action", _CURATION_ACTIONS, path, msgs)
    _check_enum(evt, "previous_status", _MAPPING_STATUSES, path, msgs)
    _check_enum(evt, "new_status", _MAPPING_STATUSES, path, msgs)
    _check_type(evt, "llm_assisted", bool, "boolean", path, msgs)


def _validate_ingredient_record(rec: Any, path: str, msgs: list[ValidationMessage]):
    if not isinstance(rec, dict):
        msgs.append(ValidationMessage("error", path, "Ingredient record must be a mapping"))
        return
    _check_required(rec, "identifier", path, msgs)
    _check_required(rec, "preferred_term", path, msgs)
    _check_required(rec, "mapping_status", path, msgs)
    _check_enum(rec, "mapping_status", _MAPPING_STATUSES, path, msgs)

    if rec.get("ontology_mapping") is not None:
        _validate_ontology_mapping(rec["ontology_mapping"], f"{path}.ontology_mapping", msgs)

    for i, syn in enumerate(rec.get("synonyms") or []):
        _validate_synonym(syn, f"{path}.synonyms[{i}]", msgs)

    if rec.get("occurrence_statistics") is not None:
        _validate_occurrence_stats(rec["occurrence_statistics"], f"{path}.occurrence_statistics", msgs)

    for i, evt in enumerate(rec.get("curation_history") or []):
        _validate_curation_event(evt, f"{path}.curation_history[{i}]", msgs)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def validate_data(data: dict[str, Any], source: str = "<inline>") -> SchemaValidationResult:
    """Validate a parsed YAML dict against the schema."""
    result = SchemaValidationResult(file_path=source)

    if not isinstance(data, dict):
        result.messages.append(ValidationMessage("error", "$", "Top-level document must be a mapping"))
        return result

    _check_type(data, "total_count", int, "integer", "$", result.messages)
    _check_type(data, "mapped_count", int, "integer", "$", result.messages)
    _check_type(data, "unmapped_count", int, "integer", "$", result.messages)

    ingredients = data.get("ingredients")
    if ingredients is None:
        result.messages.append(ValidationMessage("warning", "$", "No 'ingredients' list found"))
        return result

    if not isinstance(ingredients, list):
        result.messages.append(ValidationMessage("error", "$.ingredients", "'ingredients' must be a list"))
        return result

    for i, rec in enumerate(ingredients):
        _validate_ingredient_record(rec, f"$.ingredients[{i}]", result.messages)

    return result


def validate_file(file_path: str | Path) -> SchemaValidationResult:
    """Load a YAML file and validate against the schema."""
    fp = Path(file_path)
    if not fp.exists():
        result = SchemaValidationResult(file_path=str(fp))
        result.messages.append(ValidationMessage("error", "$", f"File not found: {fp}"))
        return result

    try:
        with open(fp) as fh:
            data = yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        result = SchemaValidationResult(file_path=str(fp))
        result.messages.append(ValidationMessage("error", "$", f"YAML parse error: {exc}"))
        return result

    return validate_data(data or {}, source=str(fp))
