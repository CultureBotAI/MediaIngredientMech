# `data/ingredients/mapped/Casein_Peptone.yaml`

## Verdict

Needs curation; major issue. The curated FoodOn parent grounding for the
casein-peptone family, synonyms, SSSOM row, aggregate copy, and occurrence
count agree, but `PROTEIN_SOURCE` is asserted from only a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Casein_Peptone.yaml`.
- Identifier and grounding: `identifier: FOODON:03315719`,
  `ontology_mapping.ontology_id: FOODON:03315719`,
  `ontology_label: mammalian milk protein (hydrolyzed)`,
  `ontology_source: FOODON`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Direct OLS lookup for `FOODON:03315719` returns one active FoodOn term
  labelled `mammalian milk protein (hydrolyzed)`.
- The close FoodOn grounding is an intentional parent mapping for the commercial
  casein-peptone family because FoodOn has no exact casein-peptone child term.

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
  backups, found the active `MIM:Casein_Peptone` SSSOM row with
  `FOODON:03315719`, the synonym-enrichment `ALREADY_REPRESENTED`
  disposition, matching aggregate/docs rows, and the same curated label family
  in `mappings/complex_ingredients.tsv`.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 1247
  distinct recipes and 1313 total occurrences for `FOODON:03315719`, matching
  `occurrence_statistics`.
- The `PROTEIN_SOURCE` role has only `COMPUTATIONAL_PREDICTION` evidence with
  a curator note that explicitly labels it a provisional name-pattern rule.

## Completeness

- The FoodOn parent identifier, casein-peptone synonyms, 1247/1313 occurrence
  count, SSSOM row, aggregate copy, and docs row are populated.
- CAS and chemical-structure fields are correctly absent for this undefined
  commercial protein hydrolysate mixture.

## Recommended Edits

- Major: either replace the provisional
  `nutritional_roles.PROTEIN_SOURCE` evidence in
  `data/ingredients/mapped/Casein_Peptone.yaml` with inspected evidence for
  this casein-peptone family scope, or remove the role, then rerun strict
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
