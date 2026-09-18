# `data/ingredients/mapped/Bedaquiline.yaml`

## Verdict

Pass. The exact `CHEBI:72292` identity, CultureBotHT CAS value, ChEBI exact
synonym, formula, InChI, SMILES, SSSOM row, and aggregate copy all describe
bedaquiline.

## Identity

- Reviewed record: `data/ingredients/mapped/Bedaquiline.yaml`.
- Identifier and grounding: `identifier: CHEBI:72292` with
  `ontology_mapping.ontology_id: CHEBI:72292`,
  `ontology_label: bedaquiline`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:72292` to `bedaquiline` and
  returns the stored stereospecific systematic name as an exact synonym.
- PubChem resolves CAS `843663-66-1` to formula `C32H31BrN2O2` and the same
  standard InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Bedaquiline.yaml data/ingredients/mapped/Beef.yaml data/ingredients/mapped/Beef_Brain_Powder.yaml data/ingredients/mapped/Beef_Extract.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bedaquiline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 542 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 373 marked the
  `CHEBI:72292` mapping `CONFIRMED`; the fresh Engine A and OLS checks still
  agree with that verdict.
- PubChem confirms that the CAS-backed compound carries the same formula and
  InChI as the stored CultureBotHT/ChEBI chemistry.

## Completeness

- The exact CHEBI identifier, CAS registry number, formula, InChI, SMILES,
  ChEBI exact synonym, SSSOM row, and aggregate copy are populated.
- No source occurrence, role, component list, or supplied-form split is required
  for this single-compound record with zero recorded medium occurrences.

## Recommended Edits

- None.
