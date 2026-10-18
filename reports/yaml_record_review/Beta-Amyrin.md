# `data/ingredients/mapped/Beta-Amyrin.yaml`

## Verdict

Pass. The exact `CHEBI:10352` beta-amyrin identity, CAS `559-70-6`, exact
synonym, formula, InChI, SMILES, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-Amyrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:10352` with
  `ontology_mapping.ontology_id: CHEBI:10352`,
  `ontology_label: beta-amyrin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:10352` for `beta-amyrin` and lists
  `olean-12-en-3beta-ol` as an exact synonym.
- PubChem resolves CAS `559-70-6` to formula `C30H50O` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galacto-pyranosyl-D-arabinose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed on the intentional `kgmicrobe.compound` fallback in the same batch
  because that registry prefix is not resolvable through the OAK/OLS adapter.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-Amyrin.yaml data/ingredients/mapped/Beta-D-fucose.yaml data/ingredients/mapped/Beta-D-galactoside.yaml data/ingredients/mapped/Beta-D-glucuronic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 568 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 391 confirmed the
  `CHEBI:10352` mapping, and the fresh Engine A and OLS checks still agree with
  that verdict.
- The SSSOM `other` column retains both CAS `559-70-6` and the exact CHEBI
  synonym `olean-12-en-3beta-ol`.

## Completeness

- The exact CHEBI identifier, CAS registry number, exact synonym, formula,
  InChI, SMILES, single-ingredient classification, SSSOM row, and aggregate
  copy are populated.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
