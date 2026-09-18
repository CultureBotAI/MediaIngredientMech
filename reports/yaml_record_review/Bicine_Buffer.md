# `data/ingredients/mapped/Bicine_Buffer.yaml`

## Verdict

Pass. The surviving exact `CHEBI:40957` BICINE buffer identity, absorbed
`Bicine` synonym, CAS, formula, InChI, SMILES, SSSOM row, occurrence count, and
aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bicine_Buffer.yaml`.
- Identifier and grounding: `identifier: CHEBI:40957` with
  `ontology_mapping.ontology_id: CHEBI:40957`,
  `ontology_label: N,N-bis(2-hydroxyethyl)glycine`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- OLS search for `BICINE` returns `CHEBI:40957`, and PubChem resolves CAS
  `150-25-4` to the same formula and standard InChI stored under
  `chemical_properties`.

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
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 591, the OAK/OLS confirmation row
  in `mappings/ingredient_mappings_row_review_manifest.tsv`, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_recipe_membership.tsv` contains 7 rows for
  `CHEBI:40957`, matching the record's refreshed 7/7 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, single-ingredient classification, CAS RN,
  formula, InChI, SMILES, buffer role, SSSOM row, occurrence statistics, and
  aggregate copy are populated.
- The old `Bicine` surface form is preserved as a raw synonym from the rejected
  duplicate merge.

## Recommended Edits

- None.
