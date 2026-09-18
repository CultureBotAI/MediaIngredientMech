# `data/ingredients/mapped/Mycobactin_J.yaml`

## Verdict

Pass. The exact `CHEBI:205364` Mycobactin J identity, CultureMech occurrence
provenance, retained spelling variant, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mycobactin_J.yaml`.
- Identifier and grounding: `identifier: CHEBI:205364` with
  `ontology_mapping.ontology_id: CHEBI:205364`, label `Mycobactin J`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mucin_From_Porcine_Stomach_Type_III` through `Mycobactin_J`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:205364` as active `Mycobactin J`.
- The structured mapping evidence correctly points to the CultureMech
  occurrence table that supplied the exact `Mycobactin J` surface.
- The merge history records `Mycobactine J` as a reviewed spelling variant; the
  final SSSOM keeps only that spelling variant in `other`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mycobactin_J` to `CHEBI:205364`.

## Completeness

- The active ChEBI target, CultureMech provenance, 1/1 occurrence count,
  spelling-variant handling, and final row agree.
- The record does not assert unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
