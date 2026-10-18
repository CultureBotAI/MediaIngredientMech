# `data/ingredients/mapped/Benzyl_Isothiocyanate.yaml`

## Verdict

Pass. The exact `CHEBI:17484` benzyl-isothiocyanate identity, CAS
`622-78-6`, exact synonym, formula, InChI, SMILES, SSSOM row, and aggregate
copy all agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Benzyl_Isothiocyanate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17484` with
  `ontology_mapping.ontology_id: CHEBI:17484`,
  `ontology_label: benzyl isothiocyanate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:17484` as the
  `benzyl isothiocyanate` class and `(isothiocyanatomethyl)benzene` as an exact
  synonym.
- PubChem resolves CAS `622-78-6` to formula `C8H7NS` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 561 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 385 confirmed the
  `CHEBI:17484` mapping, and the fresh Engine A and OLS checks still agree
  with that verdict.
- The SSSOM `other` column retains both CAS `622-78-6` and the exact CHEBI
  synonym `(isothiocyanatomethyl)benzene`.

## Completeness

- The exact CHEBI identifier, CAS registry number, exact synonym, formula,
  InChI, SMILES, single-ingredient classification, SSSOM row, and aggregate
  copy are populated.
- The zero `occurrence_statistics` are coherent for a CultureBotHT-imported
  record with no current CultureMech recipe memberships.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
