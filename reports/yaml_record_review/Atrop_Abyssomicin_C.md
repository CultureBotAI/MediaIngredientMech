# `data/ingredients/mapped/Atrop_Abyssomicin_C.yaml`

## Verdict

Pass. The former kg-microbe placeholder was promoted to MeSH concept
`mesh:C509797`, whose OLS record carries the exact `atrop-abyssomicin C`
synonym, and the duplicate unmapped source was merged into the same exact
identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Atrop_Abyssomicin_C.yaml`.
- Identifier and grounding: `identifier: mesh:C509797` with
  `ontology_mapping.ontology_id: mesh:C509797`,
  `ontology_label: abyssomicin C`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact-synonym search for `Atrop Abyssomicin C` in MeSH resolved
  `mesh:C509797` and returned `atrop-abyssomicin C` as the matching synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Atrazin.yaml data/ingredients/mapped/Atrop_Abyssomicin_C.yaml data/ingredients/mapped/Auraptene.yaml data/ingredients/mapped/Aureothricin.yaml data/ingredients/mapped/Avermectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Atrop_Abyssomicin_C.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS exact-synonym search for `Atrop Abyssomicin C` confirmed the MeSH target
  and the `atrop-abyssomicin C` synonym.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 495 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  `mesh:C509797` as a resolved exact CURIE.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` and
  `mappings/unmapped_ingredients_duplicate_review_2026-05-07.md` document that
  `Atrop-abyssomicin_C.yaml` was a duplicate exact-synonym hit and belonged on
  this mapped record.
- The provisional `SELECTIVE_AGENT` role is explicitly marked as a
  computational prediction from a curated name-pattern rule, not as database or
  literature evidence.

## Completeness

- The exact MeSH identifier, mapped label, retained exact synonym, SSSOM row,
  aggregate copy, duplicate-merge history, and provisional role evidence are
  populated.
- The 0/0 occurrence count is correct for a kg-microbe placeholder-derived
  record with no CultureMech recipe membership.
- No chemical structure fields are expected for this exact MeSH registry record.

## Recommended Edits

- None.
