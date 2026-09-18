# `data/ingredients/mapped/Soy_Flour.yaml`

## Verdict

Pass. The exact FOODON soybean flour identity, soy-flour synonym grounding,
undefined-mixture type, occurrence count, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Soy_Flour.yaml`.
- Identifier and grounding: `identifier: FOODON:03302142` with
  `ontology_mapping.ontology_id: FOODON:03302142`, label `soybean flour`,
  source `FOODON`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 2 source occurrences across 2 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sorgoleone` through `Soya_Peptone`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `FOODON:03302142` with label
  `soybean flour` and exact synonym `soy flour`.
- The record is a plant-derived mixture and is therefore correctly classified
  as `UNDEFINED_MIXTURE`.
- Final SSSOM publishes one exact FOODON row with no unsafe `other` payload.

## Completeness

- The FOODON ID, synonym-exact surface form, mixture type, occurrence count, and
  final exact row agree.
- Chemical, role, component, and additional synonym fields are correctly empty.

## Recommended Edits

- None.
