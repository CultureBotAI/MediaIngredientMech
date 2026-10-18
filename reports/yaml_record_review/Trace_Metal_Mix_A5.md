# `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`

## Verdict

Needs curation, major. The exact MICRO identity and occurrence count are
synchronized, but a `see below` source alias leaks into final SSSOM and the
`TRACE_ELEMENT` role is still provisional in-session LLM evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Metal_Mix_A5.yaml`.
- Identifier and grounding: `identifier: MICRO:0001349` with matching
  `ontology_mapping.ontology_id`, label `trace metal mix A5`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Synonyms: raw CultureBotHT source form plus raw CultureMech source form
  `Trace Metal Mix A5 (see below)`.
- Occurrences: 2 CultureMech recipe occurrences in 2 media.
- Roles: one `nutritional_roles.TRACE_ELEMENT` facet at confidence `0.6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Element_Solution_SL-10` through `Trace_Metals_Solution`: exited 0 and
  wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this MICRO row
  because `MICRO` is outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Trace metal mix A5` returns `MICRO:0001349` with
  label `trace metal mix A5`.
- The final SSSOM row has
  `MIM:Trace_Metal_Mix_A5 skos:exactMatch MICRO:0001349` and exports
  `Trace Metal Mix A5 (see below)` in `other`.

## Issues

### Major: `see below` is not a true synonym

The final `other` token `Trace Metal Mix A5 (see below)` is a recipe-local
instruction, not an alternate label for the MICRO stock-solution term.

### Major: `TRACE_ELEMENT` is provisional LLM evidence

The only role assertion is still the June in-session Claude prediction with the
curator note `Provisional in-session LLM role assignment; review recommended.`
The exact MICRO identity establishes the stock solution label, but it does not
provide independent role evidence.

## Completeness

- The MICRO identity, occurrence count, aggregate row, and final SSSOM row
  agree.
- The final raw alias and provisional role facet still require curation.

## Recommended Edits

- Filter `Trace Metal Mix A5 (see below)` out of final SSSOM `other`.
- Replace the provisional role evidence with curated recipe or ontology
  evidence, or remove `nutritional_roles` until that evidence is available.
