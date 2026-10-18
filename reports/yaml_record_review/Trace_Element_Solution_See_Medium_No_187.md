# `data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml`

## Verdict

Needs curation, major. The local stock-solution identity and NCIT close match
are synchronized, but the record has no component transcription and the final
SSSOM close row exports a malformed recipe-reference alias.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_element_solution_see_medium_no_187`, close parent
  `ontology_mapping.ontology_id: NCIT:C896`, label `Trace Element`, source
  `NCIT`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id:
  kgmicrobe.ingredient:trace_element_solution_see_medium_no_187`, and
  `ingredient_type: STOCK_SOLUTION`.
- Synonyms: raw mim-queue source form plus malformed raw CultureMech source
  form `Trace element solution (see Medium No. 187`.
- Occurrences: no CultureMech recipe occurrences in the split occurrence
  snapshot.
- Components: none.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Element_Solution_SL-10` through `Trace_Metals_Solution`: exited 0 and
  wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `NCIT` and `kgmicrobe.ingredient` are outside the CHEBI-focused OBO term
  subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Trace Element` returns `NCIT:C896` with label
  `Trace Element`; the May review correctly keeps it as a close category
  rather than as the exact identity.
- The final SSSOM has a close row to `NCIT:C896` and an exact identity row for
  `kgmicrobe.ingredient:trace_element_solution_see_medium_no_187`.
- The NCIT close row exports `Trace element solution (see Medium No. 187` in
  `other`.

## Issues

### Major: a malformed recipe-reference alias reaches final SSSOM

`Trace element solution (see Medium No. 187` is a raw CultureMech source
surface with the parenthetical still open. It is a recipe cross-reference, not
a real synonym of either the NCIT trace-element category or the local stock
identity, so it should not be emitted as a final `other` token.

### Major: the named stock solution is still missing components

The record is deliberately minted as a local stock-solution identity, but there
is no `components` block or `component_assertion`. The `see Medium No. 187`
surface points at a source recipe that should be transcribed before this can
behave like a complete trace-metal stock record.

## Completeness

- The local identity, close NCIT parent, aggregate copy, and final SSSOM rows
  are synchronized.
- The raw cross-reference synonym and missing stock composition remain
  unresolved.

## Recommended Edits

- Transcribe the Medium No. 187 trace-element solution into reviewed
  components, and mark the raw `see Medium` alias so the SSSOM exporter filters
  it out of final `other`.
