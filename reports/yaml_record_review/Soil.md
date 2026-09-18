# `data/ingredients/mapped/Soil.yaml`

## Verdict

Pass. The exact `ENVO:00001998` soil identity, undefined-mixture type,
environmental context, occurrence count, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Soil.yaml`.
- Identifier and grounding: `identifier: ENVO:00001998` with
  `ontology_mapping.ontology_id: ENVO:00001998`, label `soil`, source `ENVO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 46 source occurrences across 46 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Thiosulfate_Pentahydrate` through `Soil`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this ENVO-primary
  record and its ENVO environmental context.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `ENVO:00001998` with label `soil`.
- The environmental context repeats `ENVO:00001998` with `NATURAL_SOURCE`, which
  is appropriate for a record whose ingredient is soil itself.
- Final SSSOM publishes one exact ENVO row with no unsafe `other` payload.

## Completeness

- The ENVO ID, label, ingredient type, environmental context, occurrence count,
  and final exact row agree.
- Chemical, role, component, and additional synonym fields are correctly empty.

## Recommended Edits

- None.
