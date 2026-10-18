# `data/ingredients/mapped/Bicine.yaml`

## Verdict

Pass. This record is a rejected tombstone whose occurrences were merged into
`Bicine_Buffer`; its pointer now agrees with the surviving `CHEBI:40957`
record, it publishes no SSSOM row, and its aggregate copy matches the
per-record YAML.

## Identity

- Reviewed record: `data/ingredients/mapped/Bicine.yaml`.
- Tombstone state: `mapping_status: REJECTED` after the 2026-08-13
  `merge_buffer_class_duplicates` merge.
- Tombstone pointer: `identifier: CHEBI:40957` and
  `ontology_mapping.ontology_id: CHEBI:40957`, refreshed on 2026-08-15 after
  the merge target moved from the structureless `CHEBI:39065` class to the
  exact `BICINE buffer` record.
- OLS search for `BICINE` returns `CHEBI:40957`
  `N,N-bis(2-hydroxyethyl)glycine`, the active target record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bicine.yaml data/ingredients/mapped/Bicine_Buffer.yaml data/ingredients/mapped/Bicyclomycin.yaml data/ingredients/mapped/Bile_Acid.yaml data/ingredients/mapped/Bile_Salts.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bicine.yaml data/ingredients/mapped/Bicine_Buffer.yaml data/ingredients/mapped/Bicyclomycin.yaml data/ingredients/mapped/Bile_Acid.yaml data/ingredients/mapped/Bile_Salts.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the aggregate tombstone in
  `data/curated/mapped_ingredients.yaml`.
- A hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no `MIM:Bicine` row, which agrees with the tombstone history saying its
  SSSOM rows were dropped.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The merge target pointer, rejected status, merge history, and surviving
  source-role provenance are present.
- No standalone SSSOM row, occurrence count, or active role edge is expected
  from this tombstone.

## Recommended Edits

- None.
