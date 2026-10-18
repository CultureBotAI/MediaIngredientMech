# `data/ingredients/mapped/Trace_Element_Solution_SL-10.yaml`

## Verdict

Pass. The DSMZ SL-10 trace-element stock solution is represented as a local
`kgmicrobe.ingredient` identity with a broad NCIT close match, complete
component transcription, reviewed trace-element role, aggregate row, and final
SSSOM rows that agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Element_Solution_SL-10.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_element_solution_sl-10`, close parent
  `ontology_mapping.ontology_id: NCIT:C896`, label `Trace Element`, source
  `NCIT`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: kgmicrobe.ingredient:trace_element_solution_sl-10`, and
  `ingredient_type: STOCK_SOLUTION`.
- Solution type: `TRACE_METAL_MIX`.
- Synonyms: raw CommunityMech source form `Trace element solution SL-10`.
- Occurrences: no CultureMech recipe occurrences in the split 8c79a66fec
  occurrence snapshot.
- Components: complete DSMZ solution 4178 transcription covering HCl,
  iron(II) chloride tetrahydrate, zinc chloride, manganese(II) chloride
  tetrahydrate, boric acid, cobalt(II) chloride hexahydrate, copper(II)
  chloride dihydrate, nickel(II) chloride hexahydrate, sodium molybdate
  dihydrate, and distilled water.
- Roles: reviewed `nutritional_roles.TRACE_ELEMENT` facet with DSMZ technical
  report evidence.

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
  `Trace Element`; the stock-solution review correctly keeps it as a close
  category rather than as the exact identity.
- The component assertion cites DSMZ solution 4178 and is marked
  `RECIPE_TRANSCRIPTION` / `COMPLETE`.
- The final SSSOM has a close row to `NCIT:C896` and an exact identity row for
  `kgmicrobe.ingredient:trace_element_solution_sl-10`; both rows leave `other`
  empty.

## Completeness

- The local identity, NCIT close match, component block, `STOCK_SOLUTION` and
  `TRACE_METAL_MIX` classifications, DSMZ trace-element role, aggregate copy,
  and final SSSOM rows agree.
- No raw source label or component label leaks into final SSSOM `other`.

## Recommended Edits

- None.
