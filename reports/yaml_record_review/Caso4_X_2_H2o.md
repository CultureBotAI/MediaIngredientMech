# `data/ingredients/mapped/Caso4_X_2_H2o.yaml`

## Verdict

Needs curation; major issue. The calcium sulfate dihydrate identity, CAS,
structure fields, synonym set, SSSOM row, aggregate copy, and occurrence count
agree, but `MINERAL_SOURCE` has no evidence object.

## Identity

- Reviewed record: `data/ingredients/mapped/Caso4_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:32583`,
  `ontology_mapping.ontology_id: CHEBI:32583`,
  `ontology_label: calcium sulfate dihydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:32583`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:32583` returns one active ChEBI term labelled
  `calcium sulfate dihydrate` with CAS `10101-41-4`, formula
  `Ca.2H2O.O4S`, and the same InChI and SMILES stored in
  `chemical_properties`.
- The non-dihydrate potassium phosphate and anhydrous calcium sulfate labels
  from #464 remain only as `REJECTED_LABEL` entries.

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
  backups, found the active `MIM:Caso4_X_2_H2o` SSSOM row with `CHEBI:32583`,
  the hydrate-review `OK` row, the synonym-enrichment
  `ALREADY_REPRESENTED` disposition, and matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 158
  distinct recipes and 158 total occurrences for `CHEBI:32583`, matching
  `occurrence_statistics`.
- `SULFUR_SOURCE` preserves the imported CultureMech `Mineral` role text as a
  `DATABASE_ENTRY` evidence item. `MINERAL_SOURCE` was added by the #128
  residual-role repair but carries an empty `evidence` list.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, hydrate synonyms,
  rejected non-dihydrate aliases, 158/158 occurrence count, SSSOM row,
  aggregate copy, and docs row are populated.

## Recommended Edits

- Major: add inspected evidence to
  `nutritional_roles.MINERAL_SOURCE` in
  `data/ingredients/mapped/Caso4_X_2_H2o.yaml`, or remove the role if the
  bulk-cation assertion is not supported for calcium sulfate dihydrate, then
  rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
