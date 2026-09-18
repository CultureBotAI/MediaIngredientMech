# `data/ingredients/mapped/Clotrimazole.yaml`

## Verdict

Pass. The CultureBotHT clotrimazole record is exactly grounded to active
`CHEBI:3764`; its CAS RN, formula, InChI, SMILES, ChEBI exact synonym, zero
occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Clotrimazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:3764`,
  `ontology_mapping.ontology_id: CHEBI:3764`,
  `ontology_label: clotrimazole`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:3764` returns active `CHEBI:3764` labelled
  `clotrimazole` with CAS RN `23593-75-1`, formula `C22H17ClN2`, and the same
  InChI and SMILES stored in `chemical_properties`.
- `1-[(2-chlorophenyl)(diphenyl)methyl]-1H-imidazole` is a ChEBI exact synonym
  for `CHEBI:3764`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Clarithromycin.yaml data/ingredients/mapped/Clavulanic_Acid.yaml data/ingredients/mapped/Clindamycin.yaml data/ingredients/mapped/Clofazimine.yaml data/ingredients/mapped/Clotrimazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Clarithromycin.yaml data/ingredients/mapped/Clavulanic_Acid.yaml data/ingredients/mapped/Clindamycin.yaml data/ingredients/mapped/Clofazimine.yaml data/ingredients/mapped/Clotrimazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Clotrimazole` SSSOM row, the OAK/OLS
  row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:3764` only in this active record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:3764`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The final SSSOM `other` column contains the exact ChEBI synonym
  `1-[(2-chlorophenyl)(diphenyl)methyl]-1H-imidazole` and the matching
  `CAS:23593-75-1` value.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.

## Recommended Edits

- None for this record.
