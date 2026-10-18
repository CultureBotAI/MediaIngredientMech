# `data/ingredients/mapped/Carrot.yaml`

## Verdict

Pass. The MediaDive carrot source label is exactly grounded to active
`NCIT:C72000`, and its occurrence count, prefix-specific OLS validation,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carrot.yaml`.
- Identifier and grounding: `identifier: NCIT:C72000`,
  `ontology_mapping.ontology_id: NCIT:C72000`,
  `ontology_label: Carrot`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `NCIT:C72000` returns one active NCIT term labelled
  `Carrot`.
- The older `UNKNOWN_TERM` review state was a prefix-dispatch problem in the
  synonym-review validator; `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`
  records that prefix-specific OLS lookup resolves the exact NCIT CURIE.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carrot` SSSOM row with the
  exact NCIT target, matching aggregate/docs rows, and the prefix-specific OLS
  validation that supersedes the stale `UNKNOWN_TERM` row-review output.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain seven
  distinct recipes and seven occurrences, matching `occurrence_statistics`.

## Completeness

- The exact NCIT food identifier, MediaDive source reference, 7/7 occurrence
  count, SSSOM row, aggregate copy, and docs row are populated.
- No role, component, chemical-property, or environment claims are present.

## Recommended Edits

- None for this record.
