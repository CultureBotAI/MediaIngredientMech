# `data/ingredients/mapped/Co_No32_X_6_H2o.yaml`

## Verdict

Pass. The CultureMech cobalt dinitrate hexahydrate record is exactly grounded to
active `CHEBI:86214`; its CAS RN, hydrate-specific formula, InChI, SMILES,
236-count CultureMech occurrence total, hydrate synonyms, SSSOM row, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Co_No32_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86214`,
  `ontology_mapping.ontology_id: CHEBI:86214`,
  `ontology_label: cobalt dinitrate hexahydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:86214` returns active `CHEBI:86214` labelled
  `cobalt dinitrate hexahydrate` with CAS RN `10026-22-9`, formula
  `Co.6H2O.2NO3`, and the same InChI and SMILES stored in
  `chemical_properties`.
- The `reports/hydrate_grounding.tsv` and `mappings/hydrate_review.tsv`
  hydrate audits both classify this record as a correct hexahydrate-specific
  `CHEBI:86214` grounding.
- The raw `Role: Mineral source; Properties: ...` synonym is filtered from
  final SSSOM by local synonym policy, and all hydrate formula variants that do
  reach the final `other` column denote the same hexahydrate.

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
  `reports` found the active exact `MIM:Co_No32_X_6_H2o` SSSOM row, the
  OAK/OLS row-review confirmation, the hydrate audits, and matching
  aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  `CHEBI:86214` only as this record's `identifier` and `ontology_id`. Separate
  `component_id: CHEBI:86214` references in stock-solution records correctly
  point to this ingredient rather than duplicating its identity.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 234 rows for `CHEBI:86214`
  whose occurrence weights sum to 236, matching the explicit 234/236
  `occurrence_statistics`.
- The `TRACE_ELEMENT` role is supported by a `DATABASE_ENTRY` that preserves
  CultureMech's imported `Mineral` role text.

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, hydrate synonyms,
  SSSOM row, aggregate copy, docs row, occurrence count, and role evidence are
  populated and agree.

## Recommended Edits

- None for this record.
