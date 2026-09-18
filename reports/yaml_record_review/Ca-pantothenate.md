# `data/ingredients/mapped/Ca-pantothenate.yaml`

## Verdict

Needs curation, minor. This record is correctly rejected after merging into the
active `CHEBI:31345` calcium pantothenate record, but the tombstone still
carries the pre-merge pantothenate anion structure and vitamin-role annotation.

## Identity

- Reviewed record: `data/ingredients/mapped/Ca-pantothenate.yaml`.
- Tombstone state: `identifier: CHEBI:31345`,
  `preferred_term: Ca-pantothenate`, `mapping_status: REJECTED`, and
  `ontology_mapping.ontology_id: CHEBI:31345`.
- Direct OLS lookup for `CHEBI:31345` resolves an active calcium pantothenate
  term with CAS `137-08-6`, and PubChem resolves CAS `137-08-6` to calcium
  pantothenate with formula `C18H32CaN2O10`.
- Hidden/ignored-inclusive search found no live `MIM:Ca-pantothenate` row in
  `mappings/ingredient_mappings.sssom.tsv`; the live calcium pantothenate SSSOM
  mapping is owned by `MIM:Calcium_Pantothenate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/CHIR-090.yaml data/ingredients/mapped/CMC_PY_Horse_Serum.yaml data/ingredients/mapped/Ca-folinate.yaml data/ingredients/mapped/Ca-pantothenate.yaml data/ingredients/mapped/Ca_No32.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/CHIR-090.yaml data/ingredients/mapped/CMC_PY_Horse_Serum.yaml data/ingredients/mapped/Ca-folinate.yaml data/ingredients/mapped/Ca-pantothenate.yaml data/ingredients/mapped/Ca_No32.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed on `kgmicrobe.ingredient:cmc_py_horse_serum` because the local
  kg-microbe ingredient adapter lacks `rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/CHIR-090.yaml data/ingredients/mapped/Ca-folinate.yaml data/ingredients/mapped/Ca-pantothenate.yaml data/ingredients/mapped/Ca_No32.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four ChEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the rejected aggregate copy in
  `data/curated/mapped_ingredients.yaml`, the active exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 668 for
  `MIM:Calcium_Pantothenate`, and no generated review report for this tombstone
  in `reports/yaml_record_review_batch` or `reports/yaml_record_review`.
- The merge history records `MERGED_INTO` on 2026-08-10 and
  `REFRESHED_TOMBSTONE_ONTOLOGY_ID` on 2026-08-15, so the surviving live record
  for the same calcium salt is intentionally `Calcium_Pantothenate`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The rejected duplicate has the merge target identifier and does not publish a
  duplicate `MIM:Ca-pantothenate` row in the SSSOM file.
- Minor gap: `chemical_properties` still describe the older
  `CHEBI:29032` single pantothenate anion with formula `C9H16NO5`, not the
  `CHEBI:31345` calcium salt, and the old vitamin-source role remains attached
  to the rejected tombstone.

## Recommended Edits

- Minor: strip the pre-merge `chemical_properties` and
  `nutritional_roles` from `data/ingredients/mapped/Ca-pantothenate.yaml`, or
  replace them with a compact tombstone note that points to
  `data/ingredients/mapped/Calcium_Pantothenate.yaml`; then run
  `just sync-curated` and focused strict/SSSOM validation.
