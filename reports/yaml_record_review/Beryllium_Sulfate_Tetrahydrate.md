# `data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml`

## Verdict

Pass. The exact hydrate-specific `CHEBI:53502` beryllium sulfate tetrahydrate
identity, CAS `7787-56-6`, formula, InChI, SMILES, occurrence count, SSSOM row,
and aggregate copy all agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53502` with
  `ontology_mapping.ontology_id: CHEBI:53502`,
  `ontology_label: beryllium sulfate tetrahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:53502` for `beryllium sulfate
  tetrahydrate` and lists `beryllium sulfate--water (1/4)` as an exact synonym.
- PubChem resolves CAS `7787-56-6` to formula `BeH8O8S` and the same standard
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
  `mappings/ingredient_mappings.sssom.tsv` row 567 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 390 confirmed the
  `CHEBI:53502` mapping, and the fresh Engine A and OLS checks still agree with
  that verdict.
- `mappings/hydrate_review.tsv` row 92 marks the same CAS and CHEBI pairing
  `CORRECT`, with a `MATCHES_HYDRATE` supplied-form verdict.

## Completeness

- The exact hydrate CHEBI identifier, CAS registry number, exact synonym,
  formula, InChI, SMILES, 1/1 occurrence count, single-ingredient
  classification, SSSOM row, and aggregate copy are populated.
- No component list, role, or parent anchor is required because a
  hydrate-specific CHEBI term exists.

## Recommended Edits

- None.
