# `data/ingredients/mapped/Cu_No32_X_3_H2o.yaml`

## Verdict

Needs curation; major. The local trihydrate identity, close mapping to
anhydrous `CHEBI:78036`, registry SSSOM row, and 2/2 count pass, but the
record and final parent SSSOM row still publish anhydrous copper-nitrate
synonyms and an anhydrous InChI/SMILES for `Cu(NO3)2 x 3 H2O`.

## Identity

- Reviewed record: `data/ingredients/mapped/Cu_No32_X_3_H2o.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:cu_no32_x_3_h2o`,
  `ontology_mapping.ontology_id: CHEBI:78036`,
  `ontology_label: copper(II) nitrate`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:78036` returns active `CHEBI:78036` labelled
  `copper(II) nitrate`, an anhydrous parent with the same anhydrous synonyms
  now leaking onto this trihydrate record.
- Live exact OLS searches for `Cu(NO3)2 x 3 H2O` and `copper(II) nitrate
  trihydrate` found no exact CHEBI class, so the local registry identity is
  still warranted.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using
  `kgmicrobe.compound:cu_no32_x_3_h2o` as a primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cu_No32_X_3_H2o.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `Cu_No32_X_3_H2o` was intentionally skipped because its local
  `kgmicrobe.compound` primary identifier and close ChEBI parent are outside
  this CHEBI-focused exact-label validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the paired final SSSOM rows:
  `MIM:Cu_No32_X_3_H2o skos:closeMatch CHEBI:78036` and the sibling
  `skos:exactMatch kgmicrobe.compound:cu_no32_x_3_h2o` registry row.
- `mappings/culturemech_recipe_membership.tsv` contains two
  `kgmicrobe.compound:cu_no32_x_3_h2o` rows and a total occurrence sum of 2,
  matching `occurrence_statistics` `2/2`.
- Major: `synonyms` still asserts `copper(II) nitrate (anhydrous)` and
  `copper(2+) dinitrate` as exact synonyms of the trihydrate. The final
  `CHEBI:78036` close-match SSSOM row repeats both anhydrous parent aliases in
  `other`.
- Major: `chemical_properties.molecular_formula` was corrected to
  `Cu.2NO3.3H2O`, but the active InChI and SMILES still encode the anhydrous
  salt with no water of hydration.

## Completeness

- The local registry identifier, parent CHEBI close match, CAS RN, registry
  SSSOM row, aggregate copy, and occurrence count are populated and agree.
- The incomplete surfaces are the chemistry and synonym payloads that still
  come from the anhydrous parent rather than the trihydrate.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cu_No32_X_3_H2o.yaml`, demote
  `copper(II) nitrate (anhydrous)` and `copper(2+) dinitrate` to rejected or
  parent-only provenance so they no longer publish as exact local aliases.
- Major: remove or replace the anhydrous `chemical_properties.inchi` and
  `chemical_properties.smiles` values; keep `molecular_formula:
  Cu.2NO3.3H2O` and `CAS:10031-43-3` for the trihydrate.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
