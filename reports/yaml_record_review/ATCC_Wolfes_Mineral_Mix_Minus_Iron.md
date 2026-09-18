# `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml`

## Verdict

Needs curation, major. The local ATCC Wolfe's mineral mix minus iron identity
is intentionally represented as a stock solution, but the component recipe is
still absent after promotion to `MAPPED`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:atcc_wolfes_mineral_mix_minus_iron` with the
  same local `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The record intentionally represents a named ATCC Wolfe mineral-stock variant
  as `ingredient_type: STOCK_SOLUTION` and `solution_type: MINERAL_STOCK`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml data/ingredients/mapped/ATCC_Wolfes_Vitamin_Mix.yaml data/ingredients/mapped/A_Trace_Components.yaml data/ingredients/mapped/Abietic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed because the validator tried to resolve registry CURIE
  `kgmicrobe.ingredient:atcc_wolfes_mineral_mix_minus_iron` through the OAK
  sqlite label table and raised `sqlite3.OperationalError: no such table:
  rdfs_label_statement`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The #114 evidence supports minting a local ingredient for an ATCC Wolfe's
  mineral mix variant rather than mapping the mixture to any single chemical.
- The SSSOM row maps `MIM:ATCC_Wolfes_Mineral_Mix_Minus_Iron` to
  `kgmicrobe.ingredient:atcc_wolfes_mineral_mix_minus_iron` with
  `skos:exactMatch` and fallback-registry provenance.
- The curation history and top-level note both still describe this stock as
  pending component-level recipe curation, and there is no `components` block or
  `component_assertion` to show which salts remain after iron is omitted.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, subject-case
  alias rows, unmapped exact-audit row, and ignored aggregate backups.

## Completeness

- The local identifier, stock-solution classification, occurrence count, and
  local registry mapping are populated.
- The component recipe is materially incomplete for a named mixture record.

## Recommended Edits

- In `data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml`, add the
  mineral-stock components and a `component_assertion` for the minus-iron
  formulation, or add an explicit discussion entry if the exact source formula
  cannot be recovered.
- Add supported `MINERAL_SOURCE` and `TRACE_ELEMENT` roles if the curated
  formula establishes them.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation,
  component partonomy, and SSSOM invariants.
