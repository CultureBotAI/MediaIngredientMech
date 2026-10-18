# `data/ingredients/mapped/CHIR-090.yaml`

## Verdict

Pass. The exact `CHEBI:134107` CHIR-090 identity, CAS, long-form ChEBI
synonym, structure fields, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/CHIR-090.yaml`.
- Identifier and grounding: `identifier: CHEBI:134107` with
  `ontology_mapping.ontology_id: CHEBI:134107`,
  `ontology_label: CHIR-090`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `CHIR-090` returns the single active ChEBI hit
  `CHEBI:134107`, whose formula, InChI, SMILES, and exact synonym match the
  local record.
- PubChem resolves CAS `728865-23-4` to CID 11546620 with formula
  `C24H27N3O5` and the same standard InChI stored in `chemical_properties`.

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
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 647, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:CHIR-090` to `CHEBI:134107` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field contains the same ChEBI synonym and
  CAS stored in the YAML.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, ChEBI synonym, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, and aggregate copy are
  populated.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a CultureBotHT compound import that has no CultureMech recipe
  memberships.
- No roles, components, or environmental contexts are required for this
  single-compound record.

## Recommended Edits

- None.
