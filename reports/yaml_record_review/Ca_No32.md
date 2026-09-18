# `data/ingredients/mapped/Ca_No32.yaml`

## Verdict

Needs curation, major. The `CHEBI:64205` calcium nitrate remap, CAS, mineral
role, occurrence count, SSSOM row, and aggregate copy agree, but six cadmium
nitrate labels remain as exact synonyms of calcium nitrate and are exported in
SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Ca_No32.yaml`.
- Identifier and grounding: `identifier: CHEBI:64205` with
  `ontology_mapping.ontology_id: CHEBI:64205`,
  `ontology_label: calcium nitrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- The original cadmium nitrate import contamination was correctly remapped from
  `CHEBI:77732` to anhydrous calcium nitrate `CHEBI:64205`; direct OLS lookup
  for `CHEBI:64205` resolves active calcium nitrate with CAS `10124-37-5`,
  formula `Ca.2NO3`, and the same InChI and SMILES as the local
  `chemical_properties`.
- PubChem resolves CAS `10124-37-5` to calcium nitrate, confirming the current
  CAS and structure fields.

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
  review directories, found the synonym-enrichment row, the authoritative exact
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 650, all 37
  current `mappings/culturemech_recipe_membership.tsv` rows for `CHEBI:64205`,
  the active cadmium nitrate row at
  `mappings/ingredient_mappings.sssom.tsv` row 662, the active cadmium nitrate
  tetrahydrate row at row 720, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Ca_No32` to `CHEBI:64205` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- Major gap: cadmium labels `Cadmium(II) nitrate`, `Cd(NO3)2`,
  `Nitric acid, cadmium salt`, `Nitric acid, cadmium salt (2:1)`,
  `cadmium dinitrate`, and `cadmium nitrate` remain as exact synonyms on the
  calcium nitrate YAML record after the remap and are still present in the
  SSSOM `other` field.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, calcium nitrate synonym, mineral-source
  role, single-ingredient classification, formula, InChI, SMILES, 37/37
  occurrence count, SSSOM row, and aggregate copy are populated.
- The wrong cadmium synonyms would make a synonym consumer route cadmium
  nitrate labels to calcium nitrate even though MIM already has separate live
  `CHEBI:77732` cadmium nitrate and `CHEBI:86156` cadmium nitrate tetrahydrate
  records.

## Recommended Edits

- Major: remove the six cadmium nitrate synonyms from
  `data/ingredients/mapped/Ca_No32.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv` so the `MIM:Ca_No32` `other` field
  keeps only calcium nitrate aliases, then run `just sync-curated` and focused
  strict/term/SSSOM validation.
