# `data/ingredients/mapped/Liver_Digest.yaml`

## Verdict

Needs curation. The MICRO:0001668 liver-digest identity, mixture type,
occurrence count, and final SSSOM row pass, but
`nutritional_roles.PROTEIN_SOURCE` is still an unsupported provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Liver_Digest.yaml`.
- Identifier and grounding: `identifier: MICRO:0001668` with
  `ontology_mapping.ontology_id: MICRO:0001668`, label `liver digest`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file liver batch:
  exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Liver_powder.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the FOODON-grounded record. The four MICRO-grounded records were
  skipped from the CHEBI/OBO Engine A subset and checked against OLS manually.

## Evidence

- EBI OLS4 resolves `MICRO:0001668` as active `liver digest`.
- The final SSSOM publishes one `skos:exactMatch` row to `MICRO:0001668` and
  has an empty `other` field.
- The aggregate `data/curated/mapped_ingredients.yaml` copy matches the
  per-record identity, refreshed seven-recipe occurrence count, mixture type,
  status, and mapping.
- Major: `nutritional_roles.PROTEIN_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended. The record needs inspected medium-level evidence
  that exact liver digest was supplied as a protein source before retaining that
  role.

## Completeness

- The active MICRO identity, undefined-mixture classification, aggregate copy,
  occurrence count, and final SSSOM row are present and consistent.
- The provisional protein-source role needs curation before it can be treated
  as a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.PROTEIN_SOURCE` in
  `data/ingredients/mapped/Liver_Digest.yaml` with inspected source evidence for
  exact liver digest use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, round-trip, component, and SSSOM validation.
