# `data/ingredients/mapped/Bergapten.yaml`

## Verdict

Pass. The CAS-derived `CHEBI:18293` 5-methoxypsoralen identity, Bergapten
synonym, CAS `484-20-8`, formula, InChI, SMILES, SSSOM row, and aggregate copy
all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bergapten.yaml`.
- Identifier and grounding: `identifier: CHEBI:18293` with
  `ontology_mapping.ontology_id: CHEBI:18293`,
  `ontology_label: 5-methoxypsoralen`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:18293` for `Bergapten`.
- PubChem resolves CAS `484-20-8` to formula `C12H8O4` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in the batch.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 565 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 388 confirmed the
  `CHEBI:18293` mapping, and the fresh Engine A and OLS checks still agree with
  that verdict.
- The 2026-08-24 regrade correctly preserved `CAS_RN_LOOKUP`, because the
  CultureBotHT CAS xref created the CHEBI grounding.

## Completeness

- The exact CHEBI identifier, CAS registry number, exact synonym, formula,
  InChI, SMILES, single-ingredient classification, SSSOM row, and aggregate
  copy are populated.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
