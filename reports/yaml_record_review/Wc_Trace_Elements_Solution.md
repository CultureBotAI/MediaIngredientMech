# `data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml`

## Verdict

Needs curation. The aggregate row and final SSSOM row match the YAML, but this
named WC trace-elements formulation is asserted as an exact match to generic
`MICRO:0000455` `trace elements solution`, and its `TRACE_ELEMENT` role is
still a provisional in-session LLM inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml`.
- Identifier and grounding: `identifier: MICRO:0000455` with matching
  `ontology_mapping.ontology_id`, label `trace elements solution`, source
  `MICRO`, `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Synonyms: one raw CultureMech surface form, `WC Trace Elements Solution`.
- Occurrences: two CultureMech recipe occurrences across two media.
- Role: `TRACE_ELEMENT` with provisional in-session LLM evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wc_Trace_Elements_Solution` through
  `Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this `MICRO` row has no CHEBI/OBO adapter for that focused check.

## Evidence

- Fresh OLS4 exact-label search for `trace elements solution` in MicrO found
  generic `MICRO:0000455` and many named sibling trace-elements solution
  classes, supporting that MicrO distinguishes generic and formulation-specific
  trace-elements stocks.
- This record's history shows `resolve_unmapped_v2` promoted the primary
  identifier by a `stem-match` auto-upgrade from `UNMAPPED_0066`.
- The final SSSOM row currently has
  `MIM:Wc_Trace_Elements_Solution skos:exactMatch MICRO:0000455`.

## Issues

- Major: the exact primary mapping collapses the named WC formulation onto the
  generic MicrO `trace elements solution` term. This should preserve an exact
  local identity for WC Trace Elements Solution rather than asserting that the
  WC formulation is identical to the generic MicrO bucket.
- Major: `nutritional_roles.TRACE_ELEMENT` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says it was assigned by
  in-session Claude reasoning with no external API and still needs review.

## Completeness

- The aggregate row and final SSSOM row agree with the per-record YAML.
- The record needs a local exact identity and checked role evidence before it
  can be considered fully curated.

## Recommended Edits

- Replace the primary identifier with a `kgmicrobe.ingredient` exact identity
  for WC Trace Elements Solution and keep `MICRO:0000455` only as a broader or
  close generic trace-elements-solution parent if useful.
- Replace or remove the provisional `TRACE_ELEMENT` role evidence.
- Rebuild SSSOM and rerun strict validation, SSSOM invariant validation, and
  the trace-elements exact-to-generic audit.
