# `data/ingredients/mapped/Cd_No32_X_4_H2o.yaml`

## Verdict

Pass. The cadmium nitrate tetrahydrate record is exactly grounded to active
`CHEBI:86156`, and its CAS, formula, InChI, SMILES, synonyms, SSSOM row,
aggregate copy, and 2/2 occurrence count agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cd_No32_X_4_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86156`,
  `ontology_mapping.ontology_id: CHEBI:86156`,
  `ontology_label: cadmium nitrate tetrahydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:86156` returns one active ChEBI term labelled
  `cadmium nitrate tetrahydrate` with CAS `10022-68-1`, formula
  `Cd.4H2O.2NO3`, and the same InChI and SMILES stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caso42h2osaturated_Solution.yaml data/ingredients/mapped/Caso4_X_2_H2o.yaml data/ingredients/mapped/Caso4_X_7_H2o.yaml data/ingredients/mapped/Catalase.yaml data/ingredients/mapped/Cd_No32_X_4_H2o.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caso4_X_2_H2o.yaml data/ingredients/mapped/Caso4_X_7_H2o.yaml data/ingredients/mapped/Catalase.yaml data/ingredients/mapped/Cd_No32_X_4_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active `MIM:Cd_No32_X_4_H2o` SSSOM row with
  `CHEBI:86156`, the hydrate-review `OK` row, the `CONFIRMED_NO_ACTION`
  row-review disposition, and matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain two
  distinct recipes and two total occurrences for `CHEBI:86156`, matching
  `occurrence_statistics`.
- No role, component, or environment claims are present.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, hydrate synonyms,
  2/2 occurrence count, SSSOM row, aggregate copy, and docs row are populated.

## Recommended Edits

- None for this record.
