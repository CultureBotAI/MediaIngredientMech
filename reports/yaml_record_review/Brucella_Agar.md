# `data/ingredients/mapped/Brucella_Agar.yaml`

## Verdict

Needs curation, minor. The exact `MICRO:0000595` Brucella agar mapping, complex
medium classification, catalog alias, SSSOM row, and aggregate copy agree, but
the occurrence statistics were not refreshed after `Brucella agar (BD-BBL)` was
folded into the record.

## Identity

- Reviewed record: `data/ingredients/mapped/Brucella_Agar.yaml`.
- Identifier and grounding: `identifier: MICRO:0000595` with
  `ontology_mapping.ontology_id: MICRO:0000595`,
  `ontology_label: Brucella agar`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: UNDEFINED_MIXTURE`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Brucella agar` returns `MICRO:0000595`, with the
  sibling `Brucella agar with sheep blood` as a narrower formulation rather
  than the same identity.
- The `Brucella agar (BD-BBL)` alias folds onto the same Brucella agar medium
  label while preserving the vendor/catalog qualifier as a non-exact surface.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucella_Agar.yaml data/ingredients/mapped/Brucine.yaml data/ingredients/mapped/Butamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bromosuccinate.yaml data/ingredients/mapped/Bromothymol_Blue.yaml data/ingredients/mapped/Brucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the prefix-specific MICRO OLS validation row, the
  authoritative exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv`
  row 635, the `Brucella agar (BD-BBL)` residual triage row, four current
  `mappings/culturemech_recipe_membership.tsv` rows for `MICRO:0000595`, and
  the aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Brucella_Agar` to `MICRO:0000595` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field publishes `Brucella agar (BD-BBL)` as
  the catalog alias.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact MICRO identifier, raw extracted label, CultureMech catalog alias,
  complex-medium classification, SSSOM row, and aggregate copy are populated.
- Minor gap: `occurrence_statistics` still says 4/4 even though the later alias
  backfill found one `Brucella agar (BD-BBL)` CultureMech residual mention that
  is still present in `mappings/culturemech_residual_triage.tsv`, and the
  maintained membership export still has only four `MICRO:0000595` rows.
- Components are intentionally absent because this record denotes a complex
  commercial medium rather than a curated recipe instance.

## Recommended Edits

- Minor: refresh `data/ingredients/mapped/Brucella_Agar.yaml` occurrence
  statistics from the maintained CultureMech occurrence table after the
  `Brucella agar (BD-BBL)` alias is represented in the membership export; then
  run `just sync-curated` and focused strict/SSSOM validation.
