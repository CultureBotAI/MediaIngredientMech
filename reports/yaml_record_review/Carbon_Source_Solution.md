# `data/ingredients/mapped/Carbon_Source_Solution.yaml`

## Verdict

Pass. The record intentionally models a source-stock placeholder as a
repository-local `kgmicrobe.ingredient` term after an exact no-hit ontology
review, and its stock-solution typing, occurrence count, SSSOM row, and
aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carbon_Source_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:carbon_source_solution`,
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:carbon_source_solution`,
  `ontology_label: Carbon source solution`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: CARBON_SOURCE_MIX`.
- The record denotes an underspecified carbon-source premix rather than a
  single chemical. Direct exact OLS search for `"Carbon source solution"`
  returned 0 hits, and the retained #288 curation evidence correctly mints a
  local kgmicrobe term with no parent instead of pretending the mixture is
  exactly one component.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_Source_Solution.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_Source_Solution.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carbenicillin_Disodium_Salt`, `Carbomycin`, and
  `Carbon_Monoxide`, then stopped on `Carbon_Source_Solution` because the
  local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carbon_Source_Solution`
  SSSOM row with the local target, the current docs/aggregate rows, and the
  older exact-OLS audit row that found no label hit while the record was still
  unmapped.
- The current `mappings/culturemech_recipe_membership.tsv` row contains one
  distinct recipe and one occurrence, matching `occurrence_statistics`.
- The lone `RAW_TEXT` synonym duplicates the preferred source label and is
  appropriately scoped to the original `mim-queue` import.

## Completeness

- The local identifier, stock-solution classification, carbon-source-mix
  classification, 1/1 occurrence count, SSSOM row, aggregate copy, and docs row
  are populated.
- Component rows are absent because the source label only says `Carbon source
  solution`; the record correctly retains that underspecification instead of
  inventing mixture members.

## Recommended Edits

- None for this record.
