# `data/ingredients/mapped/Caso4_X_7_H2o.yaml`

## Verdict

Needs curation; major issue. The unresolved calcium sulfate seven-water label
now correctly keeps a local identity and only close-matches anhydrous
`CHEBI:31346`, but both current nutritional roles lack inspected evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Caso4_X_7_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:caso4_x_7_h2o`,
  `ontology_mapping.ontology_id: CHEBI:31346`,
  `ontology_label: calcium sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The active SSSOM surface publishes two rows for `MIM:Caso4_X_7_H2o`: a
  `skos:closeMatch` to the active anhydrous calcium sulfate parent and a
  `skos:exactMatch` registry row to the local kgmicrobe identifier.
- Chemical properties are intentionally empty after #344 removed the inherited
  anhydrous CAS, formula, InChI, and SMILES.

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
  backups, found both active `MIM:Caso4_X_7_H2o` SSSOM rows, the hydrate-review
  `LOCAL_IDENTITY_RETAINED` row, the sibling anhydrous/dihydrate rows, and
  matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain four
  distinct recipes and four total occurrences for
  `kgmicrobe.compound:caso4_x_7_h2o`, matching `occurrence_statistics`.
- `SULFUR_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from a
  provisional name-pattern rule, and `MINERAL_SOURCE` has an empty `evidence`
  list.

## Completeness

- The local identifier, anhydrous-parent closeMatch, registry identity row,
  4/4 occurrence count, rejected anhydrous aliases, SSSOM rows, aggregate copy,
  and docs row are populated.
- Chemical structure fields are correctly absent until the malformed MediaDive
  hydration count is corrected upstream or matched to an exact source form.

## Recommended Edits

- Major: either replace `nutritional_roles.SULFUR_SOURCE` with inspected
  evidence for this unresolved seven-water calcium sulfate label, or remove the
  role.
- Major: add inspected evidence to `nutritional_roles.MINERAL_SOURCE`, or
  remove the role if the bulk-cation assertion is unsupported for this local
  hydrate identity, then rerun strict validation, SSSOM QC, aggregate
  roundtrip, and `git diff --check`.
