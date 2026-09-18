# `data/ingredients/mapped/Baicalein.yaml`

## Verdict

Pass. The exact `CHEBI:2979` identity, CultureBotHT CAS value, ChEBI exact
synonym, formula, InChI, SMILES, SSSOM row, and aggregate copy all describe
baicalein.

## Identity

- Reviewed record: `data/ingredients/mapped/Baicalein.yaml`.
- Identifier and grounding: `identifier: CHEBI:2979` with
  `ontology_mapping.ontology_id: CHEBI:2979`,
  `ontology_label: baicalein`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:2979` to `baicalein` and returns
  the stored synonym `5,6,7-trihydroxy-2-phenyl-4H-chromen-4-one` as an exact
  synonym.
- PubChem resolves CAS `491-67-8` to formula `C15H10O5` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Baicalein.yaml data/ingredients/mapped/Bakers_Yeast.yaml data/ingredients/mapped/Balhimycin.yaml data/ingredients/mapped/Bandamycin.yaml data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Baicalein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 533 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 366 marked the
  `CHEBI:2979` mapping `CONFIRMED`; the fresh Engine A and OLS checks still
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
