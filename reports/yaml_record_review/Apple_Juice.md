# `data/ingredients/mapped/Apple_Juice.yaml`

## Verdict

Pass. The record exactly denotes FoodOn `apple juice`, preserves the
CultureMech residual occurrence evidence that introduced it, and the FoodOn
mapping, occurrence count, SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Apple_Juice.yaml`.
- Identifier and grounding: `identifier: FOODON:00001059` with
  `ontology_mapping.ontology_id: FOODON:00001059`,
  `ontology_source: FOODON`, `mapping_quality: EXACT_MATCH`,
  `match_level: EXACT`, and `mapping_status: MAPPED`.
- EBI OLS resolves `FOODON:00001059` to non-obsolete FoodOn `apple juice`, with
  a definition describing apple juice as a fruit juice made from apples.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apidaecin_IB.yaml data/ingredients/mapped/Apigenin.yaml data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml data/ingredients/mapped/Apiole.yaml data/ingredients/mapped/Apple_Juice.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Apple_Juice.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_residual_groundings.tsv` records `Apple Juice` as a
  residual CultureMech label with 1 mention across 1 recipe and a new exact
  grounding to `FOODON:00001059` `apple juice`.
- `mappings/culturemech_residual_triage.tsv` carries the same
  `FOODON:00001059` decision for `Apple Juice`.
- `mappings/ingredient_mappings.sssom.tsv` row 448 maps `MIM:Apple_Juice` to
  `FOODON:00001059` with `skos:exactMatch` and the
  `manual:claude_culturemech_residual_grounding|CREATED|2026-08-30` trailer.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, residual grounding and triage rows, and SSSOM row.

## Completeness

- FoodOn identity, CultureMech source evidence, curation history, SSSOM, and the
  aggregate copy are populated.
- Components and chemical properties are correctly absent because the record
  denotes a food product, not a pure chemical or decomposed stock mixture.
- No role, environmental context, discussion, or dataset entry is needed.

## Recommended Edits

- None.
