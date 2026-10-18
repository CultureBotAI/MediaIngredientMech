# `data/ingredients/mapped/Beta-Lapachone.yaml`

## Verdict

Pass. The exact `CHEBI:10429` beta-lapachone identity, CAS `4707-32-8`, exact
synonym, formula, InChI, SMILES, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Beta-Lapachone.yaml`.
- Identifier and grounding: `identifier: CHEBI:10429` with
  `ontology_mapping.ontology_id: CHEBI:10429`,
  `ontology_label: beta-lapachone`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Engine A label validation accepts `CHEBI:10429` with label `beta-lapachone`;
  the earlier OAK/OLS row review also confirmed this target.
- PubChem resolves CAS `4707-32-8` to formula `C15H14O3` and the same standard
  InChI stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-D-xylose.yaml data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Beta-Lapachone.yaml data/ingredients/mapped/Beta-Lipomycin.yaml data/ingredients/mapped/Beta-alanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-D-xylose.yaml data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Beta-Lapachone.yaml data/ingredients/mapped/Beta-Lipomycin.yaml data/ingredients/mapped/Beta-alanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 576 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 393 confirmed the
  `CHEBI:10429` mapping, and the fresh Engine A check still agrees with that
  verdict.
- The SSSOM `other` column retains both CAS `4707-32-8` and the exact CHEBI
  synonym `2,2-dimethyl-3,4-dihydro-2H-benzo[h]chromene-5,6-dione`.

## Completeness

- The exact CHEBI identifier, CAS registry number, exact synonym, formula,
  InChI, SMILES, single-ingredient classification, SSSOM row, and aggregate
  copy are populated.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
