# `data/ingredients/mapped/Creatine.yaml`

## Verdict

Pass. The CultureMech record is grounded to active `CHEBI:16919` creatine, the
CAS RN, formula, InChI, SMILES, exact synonyms, 6/6 CultureMech occurrence
count, final SSSOM row, and aggregate copy agree, and there are no unsupported
roles or component claims.

## Identity

- Reviewed record: `data/ingredients/mapped/Creatine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16919`,
  `ontology_mapping.ontology_id: CHEBI:16919`, `ontology_label: creatine`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:16919`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:16919` returns active `CHEBI:16919` labelled
  `creatine` and includes the record's exported exact synonyms.
- The record stores CAS RN `57-00-1`, formula `C4H9N3O2`, and populated InChI
  and SMILES values for the exact ChEBI identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/CrKSO42_X_12_H2O.yaml data/ingredients/mapped/Cr_No33_X_7_H2o.yaml data/ingredients/mapped/Creatine.yaml data/ingredients/mapped/Creatinine.yaml data/ingredients/mapped/Cresol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cr_No33_X_7_H2o.yaml data/ingredients/mapped/Creatine.yaml data/ingredients/mapped/Creatinine.yaml data/ingredients/mapped/Cresol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `CrKSO42_X_12_H2O` was intentionally skipped because its CAS primary
  identifier and close ChEBI parent are outside this CHEBI-focused exact-label
  validation pass.
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
  `reports` found the active `MIM:Creatine` final SSSOM row, the OAK/OLS
  row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:16919`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 6 rows for `CHEBI:16919`
  whose occurrence weights sum to 6, matching the explicit 6/6
  `occurrence_statistics`.
- The final SSSOM `other` column contains exact creatine synonyms and
  `CAS:57-00-1`; the raw CultureMech `Role: Growth factor` text is filtered
  and does not reach final SSSOM.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms, SSSOM
  row, aggregate copy, docs row, and occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
