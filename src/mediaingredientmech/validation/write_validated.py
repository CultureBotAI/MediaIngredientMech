"""Write-time validation: dump an ingredient record (or collection) to YAML
*only if* it passes closed-schema LinkML validation.

This is the write-time gate that the audit found missing across the 23+
YAML writers in this repo: writes go through `yaml.safe_dump(...)` with no
validation, so structural drift (unknown fields, missing required fields,
enum / pattern violations) only surfaces at downstream consumers.

Use::

    from mediaingredientmech.validation.write_validated import (
        write_validated_ingredient,
        ValidationFailedError,
    )

    try:
        write_validated_ingredient(record, output_path)
    except ValidationFailedError as exc:
        # Bad record refused; print categorized errors and abort.
        print(exc.summary())
        raise

The validator is shared across calls (LinkML schema parse + JSON-schema
emit is the slow part), so calling this in a tight migration loop is
cheap.

Ported from CultureMech's `src/culturemech/validation/write_validated.py`.
Keep the two in sync if the semantics ever diverge.
"""

from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import Any

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity, ValidationResult

DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema" / "mediaingredientmech.yaml"

_VALIDATORS: dict[Path, Validator] = {}
_VALIDATOR_LOCK = Lock()


class ValidationFailedError(Exception):
    """Raised when an ingredient fails closed-schema validation before write."""

    def __init__(self, path: Path | None, errors: list[ValidationResult]):
        self.path = path
        self.errors = errors
        super().__init__(self.summary())

    def summary(self) -> str:
        lines = [
            f"validation failed: {len(self.errors)} error(s)"
            + (f" for {self.path}" if self.path else "")
        ]
        for err in self.errors[:10]:
            lines.append(f"  - {err.message[:200]}")
        if len(self.errors) > 10:
            lines.append(f"  ... + {len(self.errors) - 10} more")
        return "\n".join(lines)


def _get_validator(schema_path: Path) -> Validator:
    """Cache validators keyed by resolved schema path so callers can mix
    schemas in the same process without silently reusing a stale instance."""
    key = Path(schema_path).resolve()
    with _VALIDATOR_LOCK:
        if key not in _VALIDATORS:
            _VALIDATORS[key] = Validator(
                schema=str(key),
                validation_plugins=[JsonschemaValidationPlugin(closed=True)],
            )
        return _VALIDATORS[key]


def infer_target_class(instance: dict[str, Any]) -> str:
    """Pick the right root class for this record.

    `data/curated/*.yaml` files are `IngredientCollection`s (top-level
    `ingredients: [...]` list); individual `data/ingredients/**/*.yaml`
    files are `IngredientRecord`s (top-level `identifier:`).

    Mirrors `scripts/validate_strict.py:infer_target_class` — keep the two
    in sync if routing rules change.
    """
    if not isinstance(instance, dict):
        return "IngredientRecord"
    if isinstance(instance.get("ingredients"), list):
        return "IngredientCollection"
    return "IngredientRecord"


def validate_ingredient(
    record: dict[str, Any],
    *,
    target_class: str | None = None,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
) -> list[ValidationResult]:
    """Return the list of ERROR-severity validation results (empty when clean)."""
    validator = _get_validator(schema_path)
    tc = target_class or infer_target_class(record)
    report = validator.validate(record, target_class=tc)
    return [r for r in report.results if r.severity == Severity.ERROR]


def write_validated_ingredient(
    record: dict[str, Any],
    path: Path,
    *,
    target_class: str | None = None,
    schema_path: Path = DEFAULT_SCHEMA_PATH,
    yaml_kwargs: dict[str, Any] | None = None,
) -> None:
    """Write `record` to `path` as YAML, but only if validation passes.

    Raises `ValidationFailedError` (without writing) when closed-schema
    validation finds any error. Use in place of `yaml.safe_dump(record, fh)`
    inside enrichment / migration / merge scripts.
    """
    errors = validate_ingredient(
        record, target_class=target_class, schema_path=schema_path
    )
    if errors:
        raise ValidationFailedError(path, errors)
    # Match the existing repo convention (yaml_handler.save_yaml +
    # IngredientCurator) so re-running this helper over an existing file
    # produces a byte-identical diff instead of churning block / flow style.
    opts = {
        "default_flow_style": False,
        "sort_keys": False,
        "allow_unicode": True,
        "width": 80,
        **(yaml_kwargs or {}),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(record, f, **opts)
