# `data/ingredients/mapped/Bergenin.yaml`

## Verdict

Pass. The exact `CHEBI:69499` Bergenin identity, CAS, formula, InChI, SMILES,
SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bergenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:69499` with
  `ontology_mapping.ontology_id: CHEBI:69499`,
  `ontology_label: Bergenin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:69499` for `Bergenin`.
- PubChem CID 66065 carries `CHEBI:69499`, formula `C14H16O9`, and the same
  standard InChI stored under `chemical_properties`.

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
  `mappings/ingredient_mappings.sssom.tsv` row 566 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 389 confirmed the
  `CHEBI:69499` mapping, and the fresh Engine A and OLS checks still agree with
  that verdict.
- PubChem also has a hydrate CID tied to CAS `108032-11-7`, but the anhydrous
  Bergenin CID carries the same CAS, CHEBI xref, formula, and InChI used here,
  so the current record has no hydrate-specific conflict to split.

## Completeness

- The exact CHEBI identifier, CAS registry number, formula, InChI, SMILES,
  single-ingredient classification, SSSOM row, and aggregate copy are
  populated.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
