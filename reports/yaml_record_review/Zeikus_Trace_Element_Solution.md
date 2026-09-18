# `data/ingredients/mapped/Zeikus_Trace_Element_Solution.yaml`

## Verdict

Pass. Zeikus trace element solution is preserved as a local stock-solution
identity, the broad NCIT trace-element class is only a close match, the JCM
recipe transcription is complete, and the final SSSOM exports the expected
local exact row plus external close row.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Zeikus_Trace_Element_Solution.yaml`.
- Identifier and local identity:
  `identifier: kgmicrobe.ingredient:zeikus_trace_element_solution` with
  `kg_microbe_node_id` preserving the same local identifier for the final exact
  registry row.
- External grounding: `ontology_id: NCIT:C896`, label `Trace Element`, source
  `NCIT`, and `mapping_quality: CLOSE_MATCH`.
- `ingredient_type: STOCK_SOLUTION` and `solution_type: TRACE_METAL_MIX`.
- Components: a complete `RECIPE_TRANSCRIPTION` assertion enumerates
  nitrilotriacetic acid, Fe/Mn/Co/Ca/Zn/Cu salts, boric acid, sodium molybdate
  dihydrate, NaCl, sodium selenite pentahydrate, and distilled water with
  liter-scale concentrations from JCM Medium No. 684.
- Role: source-backed `TRACE_ELEMENT` evidence from the JCM trace-mineral
  solution.
- Occurrences: one CultureMech occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/validate_component_partonomy.py` found 83
  decompositions, 505 components, and zero violations.
- Focused Engine A label validation was skipped because the exact identity is a
  local `kgmicrobe.ingredient` row and the external parent is NCIT.

## Evidence

- Fresh MediaDive lookup for J849 found recipe row 8,
  `Zeikus trace element solution`, `compound_id` 1914, with attribute
  `see Medium No. 684`.
- Fresh JCM Medium No. 684 lookup found the `Trace mineral solution` recipe
  with the same twelve components and the same grams-per-liter or
  milliliters-per-liter amounts recorded in this YAML.
- The final SSSOM exports the broad row as
  `MIM:Zeikus_Trace_Element_Solution skos:closeMatch NCIT:C896`.
- The final SSSOM also exports the exact local row as
  `MIM:Zeikus_Trace_Element_Solution skos:exactMatch
  kgmicrobe.ingredient:zeikus_trace_element_solution`.
- The raw duplicate label is not exported into final SSSOM `other`.

## Issues

None.

## Completeness

- The local stock-solution identity, broad NCIT parent, complete component
  assertion, component concentrations, trace-element role, occurrence count,
  aggregate copy, and two final SSSOM rows agree.

## Recommended Edits

None.
