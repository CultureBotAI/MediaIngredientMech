# `data/ingredients/mapped/Casitone.yaml`

## Verdict

Needs curation; major issue. The exact `MICRO:0000606` casitone grounding,
catalog variants, SSSOM row, aggregate copy, and occurrence count agree, but
`PROTEIN_SOURCE` is asserted from only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Casitone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000606`,
  `ontology_mapping.ontology_id: MICRO:0000606`,
  `ontology_label: casitone`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Direct OLS lookup for `MICRO:0000606` returns one active MICRO term labelled
  `casitone` with exact synonyms for the Bacto Casitone and pancreatic digest
  of casein surfaces.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  that prefix-specific OLS lookup resolves the exact MICRO CURIE, superseding
  the older generic `UNKNOWN_TERM` row-review result.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Casein_Peptone.yaml data/ingredients/mapped/Casein_hydrolysate.yaml data/ingredients/mapped/Casitone.yaml data/ingredients/mapped/Casitone_Yeast_Extract_Rumen_Fluid.yaml data/ingredients/mapped/Caso4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Casein_Peptone.yaml data/ingredients/mapped/Caso4.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed both Engine-A-supported OBO records in this batch.
- MICRO records in this batch were checked by direct prefix-specific OLS lookup
  and by the existing prefix-specific OLS validation TSV, rather than through
  the sqlite-backed Engine A path that the `justfile` intentionally skips for
  MICRO.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, and 0 violations.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active `MIM:Casitone` SSSOM row with `MICRO:0000606`, the
  prefix-specific OLS validation row, matching aggregate/docs rows, and the
  earlier FOODON-to-MICRO specificity repair.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 282
  distinct recipes and 282 total occurrences for `MICRO:0000606`, matching
  `occurrence_statistics`.
- The `PROTEIN_SOURCE` role has only `COMPUTATIONAL_PREDICTION` evidence with
  a curator note that explicitly labels it a provisional name-pattern rule.

## Completeness

- The MICRO identifier, Casitone catalog variants, 282/282 occurrence count,
  SSSOM row, aggregate copy, and docs row are populated.
- CAS and chemical-structure fields are correctly absent for this undefined
  commercial protein hydrolysate mixture.

## Recommended Edits

- Major: either replace the provisional
  `nutritional_roles.PROTEIN_SOURCE` evidence in
  `data/ingredients/mapped/Casitone.yaml` with inspected evidence for this
  pancreatic casein digest scope, or remove the role, then rerun strict
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
