# `data/ingredients/mapped/A_Trace_Components.yaml`

## Verdict

Needs curation, major. The local trace-component stock identity is intentionally
represented with a fallback kg-microbe ingredient, but the component recipe is
absent and the only raw synonym still includes a sterilization instruction.

## Identity

- Reviewed record: `data/ingredients/mapped/A_Trace_Components.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:a_trace_components` with the same local
  `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The record intentionally represents a named trace-component stock/pre-mix as
  `ingredient_type: STOCK_SOLUTION` and `solution_type: TRACE_METAL_MIX`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix.yaml data/ingredients/mapped/ATCC_Wolfes_Mineral_Mix_Minus_Iron.yaml data/ingredients/mapped/ATCC_Wolfes_Vitamin_Mix.yaml data/ingredients/mapped/A_Trace_Components.yaml data/ingredients/mapped/Abietic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/A_Trace_Components.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed because the validator tried to resolve registry CURIE
  `kgmicrobe.ingredient:a_trace_components` through the OAK sqlite label table
  and raised `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The #114 evidence supports minting a local ingredient for a named
  multi-component trace stock instead of mapping it to any single chemical.
- The SSSOM row maps `MIM:A_Trace_Components` to
  `kgmicrobe.ingredient:a_trace_components` with `skos:exactMatch` and
  promotion provenance.
- The record has no `components` block or `component_assertion`, so the
  composition of the trace-component stock is still not recoverable from the
  curated YAML.
- `A+ Trace Components (sterilize before adding)` includes a preparation
  instruction; it is a useful raw source surface, but it should not be exported
  as the exact `other` label that appears in the SSSOM row.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, unmapped
  exact-audit row, and ignored aggregate backups.

## Completeness

- The local identifier, stock-solution classification, occurrence count, and
  local registry mapping are populated.
- The trace-component recipe and exact synonym handling are materially
  incomplete.

## Recommended Edits

- In `data/ingredients/mapped/A_Trace_Components.yaml`, add the stock solution
  components and a `component_assertion`, or add a discussion entry documenting
  the bounded search if the exact formulation cannot be recovered.
- Move `A+ Trace Components (sterilize before adding)` to occurrence-only
  provenance or strip the parenthetical instruction before SSSOM export.
- Add supported `TRACE_ELEMENT` or `MINERAL_SOURCE` roles if the curated
  formula establishes them.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation,
  component partonomy, and SSSOM invariants.
