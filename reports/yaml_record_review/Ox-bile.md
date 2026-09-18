# `data/ingredients/mapped/Ox-bile.yaml`

## Verdict

Pass. The record denotes animal-derived ox bile as an undefined mixture and is
mapped to `MICRO:0000610` ox bile, the material term that exactly matches the
curated identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Ox-bile.yaml`.
- Identifier and grounding: `identifier: MICRO:0000610` with
  `ontology_mapping.ontology_id: MICRO:0000610`, label `ox bile`, source
  `MICRO`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO-targeted term validation was skipped for this MICRO-primary
  record by the repository's Engine A OBO-safe wrapper.
- The final SSSOM row was inspected directly and maps `MIM:Ox-bile` exactly to
  `MICRO:0000610`.

## Evidence

- A fresh OLS4 MICRO exact lookup for `ox bile` returned `MICRO:0000610` as
  `ox bile`; the adjacent `MICRO:0000609` result is `ox bile salts`, not this
  material record.
- The Edison literature annotation and `UNDEFINED_MIXTURE` classification both
  describe ox bile as a variable animal bile material or preparation, and the
  MICRO term models that material directly.
- The final SSSOM row publishes only the MICRO exact row and has no `other`
  tokens, so the raw `Ox-bile` synonym in YAML does not create synonym noise.
- No roles, components, supplied forms, or chemical structures are asserted.

## Completeness

- The material-level MICRO grounding is complete for this record's current
  scope; the record deliberately does not try to enumerate bile-salt
  constituents.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`,
  `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`, and the unified
  snapshot found distinct unresolved desiccated ox-bile labels, but those are
  separate records and do not invalidate this active `Ox-bile` mapping.

## Recommended Edits

- None.
