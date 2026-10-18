# `data/ingredients/mapped/Co-trimoxazole.yaml`

## Verdict

Pass. The MicrobeDecoder co-trimoxazole import is exactly grounded to active
`CHEBI:3770`; the record correctly treats it as a structureless two-component
drug mixture, and its 37-count MicrobeDecoder source occurrence, zero
CultureMech membership, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Co-trimoxazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:3770`,
  `ontology_mapping.ontology_id: CHEBI:3770`,
  `ontology_label: co-trimoxazole`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:3770` returns active `CHEBI:3770` labelled
  `co-trimoxazole` and describes it as the trimethoprim/sulfamethoxazole
  two-component mixture.
- The record has no `chemical_properties` or `ingredient_type`. That is
  consistent with the #322 classifier behavior for ChEBI primaries that lack a
  structural definition.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cloxacillin.yaml data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Co-trimoxazole.yaml data/ingredients/mapped/Co_No32.yaml data/ingredients/mapped/Co_No32_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cloxacillin.yaml data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Co-trimoxazole.yaml data/ingredients/mapped/Co_No32.yaml data/ingredients/mapped/Co_No32_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Co-trimoxazole` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:3770` only as this record's `identifier` and `ontology_id`.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:co_trimoxazole` in `BacDive_Antibiotic_resistance` and
  `BacDive_Antibiotic_sensitivity` with count 37, matching the explicit
  `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:3770`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The final SSSOM row has an empty `other` column.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, source occurrence, SSSOM row, aggregate copy, and
  docs row are populated and agree.

## Recommended Edits

- None for this record.
