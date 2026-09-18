# `data/ingredients/mapped/Avocatin_B.yaml`

## Verdict

Needs curation; severity major. The exact MeSH `avocatin B` identity is sound,
but the record does not model Avocatin B as the 1:1 Avocadene and Avocadyne
compound already represented by neighboring CHEBI records.

## Identity

- Reviewed record: `data/ingredients/mapped/Avocatin_B.yaml`.
- Identifier and grounding: `identifier: mesh:C000709627` with
  `ontology_mapping.ontology_id: mesh:C000709627`,
  `ontology_label: avocatin B`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search for `Avocatin B` in MeSH resolved non-obsolete
  `mesh:C000709627`.
- The MeSH record's related synonym states the composition as a 1:1 compound of
  16-heptadecene-1,2,4-triol and 16-heptadecyne-1,2,4-triol; those are the
  local `Avocadene` and `Avocadyne` records.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Avidin.yaml data/ingredients/mapped/Avocadene.yaml data/ingredients/mapped/Avocadyne.yaml data/ingredients/mapped/Avocatin_B.yaml data/ingredients/mapped/Avoparcin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Avocatin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS exact search for `Avocatin B` and
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` both
  resolve `mesh:C000709627`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 504 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv`,
  `mappings/ingredient_mappings_unknown_term_triage.tsv`, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` all agree that
  `mesh:C000709627` is an exact resolvable MeSH target.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` leaves sibling
  `Avocatin A` unmapped after no exact OLS hit, so this record is not hiding a
  broader avocatin-family collapse.
- The lone `RAW_TEXT` synonym repeats the preferred term from CultureBotHT; it
  is not harmful but becomes redundant once the exact MeSH label is present.
- No components or `ingredient_type` are populated even though Avocatin B is the
  1:1 Avocadene/Avocadyne compound.

## Completeness

- The exact MeSH identifier, label, SSSOM row, and aggregate copy are
  populated.
- The missing Avocadene and Avocadyne components are a material modeling gap
  because the component records already exist and MeSH spells out the 1:1
  composition.
- The 0/0 occurrence count is correct for a CultureBotHT-only record not
  present in CultureMech recipe memberships.

## Recommended Edits

- Set `ingredient_type` to the repository's mixture/decomposition value for a
  two-component compound and add 1:1 components for
  `data/ingredients/mapped/Avocadene.yaml` and
  `data/ingredients/mapped/Avocadyne.yaml`.
- Remove or retype the redundant `Avocatin B` raw synonym if local synonym
  policy treats a preferred-term echo as noise.
- Synchronize the aggregate, regenerate affected flat outputs, and rerun focused
  strict validation, component partonomy, SSSOM invariants, and flat-export
  coverage.
