# `data/ingredients/mapped/Co_No32.yaml`

## Verdict

Needs curation; major. The CultureMech cobalt dinitrate record is exactly
grounded to active `CHEBI:86209`; its CAS RN, formula, InChI, SMILES, 18/18
CultureMech occurrence count, synonyms, SSSOM row, and aggregate copy agree.
The material gap is that `TRACE_ELEMENT` is supported solely by a provisional
in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Co_No32.yaml`.
- Identifier and grounding: `identifier: CHEBI:86209`,
  `ontology_mapping.ontology_id: CHEBI:86209`,
  `ontology_label: cobalt dinitrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:86209` returns active `CHEBI:86209` labelled
  `cobalt dinitrate` with CAS RN `10141-05-6`, formula `Co.2NO3`, and the same
  InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cloxacillin.yaml data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Co-trimoxazole.yaml data/ingredients/mapped/Co_No32.yaml data/ingredients/mapped/Co_No32_X_6_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cloxacillin.yaml data/ingredients/mapped/Cloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Co-trimoxazole.yaml data/ingredients/mapped/Co_No32.yaml data/ingredients/mapped/Co_No32_X_6_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `reports` found the active exact `MIM:Co_No32` SSSOM row, the OAK/OLS
  row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:86209` only as this record's `identifier` and `ontology_id`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 18 rows for `CHEBI:86209`
  whose occurrence weights sum to 18, matching the explicit 18/18
  `occurrence_statistics`.
- The final SSSOM `other` column contains the expected cobalt dinitrate
  synonym strings and the matching `CAS:10141-05-6` value.
- `TRACE_ELEMENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `claude_in_session_curation` and is explicitly marked "Provisional
  in-session LLM role assignment; review recommended."

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, synonyms, SSSOM
  row, aggregate copy, docs row, and occurrence count are populated and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Co_No32.yaml`, either replace
  `nutritional_roles.TRACE_ELEMENT` with inspected evidence for cobalt
  dinitrate as a trace element in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
