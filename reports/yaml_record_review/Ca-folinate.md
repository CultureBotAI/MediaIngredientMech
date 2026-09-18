# `data/ingredients/mapped/Ca-folinate.yaml`

## Verdict

Pass. The exact `CHEBI:31340` calcium folinate identity, CAS, leucovorin
calcium synonym, vitamin-source role, occurrence count, SSSOM row, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Ca-folinate.yaml`.
- Identifier and grounding: `identifier: CHEBI:31340` with
  `ontology_mapping.ontology_id: CHEBI:31340`,
  `ontology_label: Calcium folinate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Ca-folinate` returns no exact label or synonym,
  but direct OLS lookup for `CHEBI:31340` resolves an active `Calcium folinate`
  term with `Leucovorin calcium` as a synonym and CAS `1492-18-8`.
- PubChem resolves CAS `1492-18-8` to CID 135430945, and the active ChEBI term
  has the same standard InChI as the local `chemical_properties`.

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
  review directories, found the synonym-enrichment row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 649, all 7
  current `mappings/culturemech_recipe_membership.tsv` rows for `CHEBI:31340`,
  and the aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Ca-folinate` to `CHEBI:31340` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field includes `Leucovorin calcium` and
  `CAS:1492-18-8`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, synonym, vitamin-source role,
  single-ingredient classification, formula, InChI, SMILES, 7/7 occurrence
  count, SSSOM row, and aggregate copy are populated.
- No components or environmental contexts are required for this calcium salt
  record.

## Recommended Edits

- None.
