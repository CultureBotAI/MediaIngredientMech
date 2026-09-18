# `data/ingredients/mapped/Oat_flakes.yaml`

## Verdict

Pass. The CultureMech residual ingredient exact-maps to active
`FOODON:03306272` `oat flakes`, and its restored mapping evidence is present
in the final SSSOM source field.

## Identity

- Reviewed record: `data/ingredients/mapped/Oat_flakes.yaml`.
- Identifier and grounding: `identifier: FOODON:03306272` with
  `ontology_mapping.ontology_id: FOODON:03306272`, label `oat flakes`, source
  `FOODON`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `match_level: EXACT`.
- Occurrences: 11 CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `FOODON:03306272` as active `oat flakes`.
- `mappings/culturemech_residual_groundings.tsv` records the original
  `Oat flakes` residual as a new `FOODON:03306272` record, matching both the
  `CREATED_FROM_CULTUREMECH_RESIDUAL` history entry and the later structured
  evidence repair.
- The final SSSOM row maps `MIM:Oat_flakes` exactly to `FOODON:03306272`, has
  no `other` tokens, and includes
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.
- No unsupported synonyms, roles, components, supplied forms, or environmental
  contexts are asserted.

## Completeness

- The active FOODON term, exact CultureMech grounding, restored structured
  evidence, occurrence count, and final SSSOM row agree.
- No optional components or roles are needed for the reviewed exact FOODON food
  product mapping.

## Recommended Edits

- None.
