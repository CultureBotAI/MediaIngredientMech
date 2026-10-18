# `data/ingredients/mapped/P-iv_Metal_Solution.yaml`

## Verdict

Pass. `P-IV Metal Solution` is a named trace-metal stock solution with a local
`kgmicrobe.ingredient` identity, a complete source-backed UTEX component list,
and no unsafe final SSSOM synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/P-iv_Metal_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:p-iv_metal_solution` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:p-iv_metal_solution`,
  label `P-IV Metal Solution`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Occurrences: 16 CultureMech occurrences across 16 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct CHEBI/OBO label validation was skipped for this local
  `kgmicrobe.ingredient` record.
- The repository component-partonomy validator passed after this batch with 83
  decompositions, 505 components, and zero violations.
- The final SSSOM row was inspected directly and maps
  `MIM:P-iv_Metal_Solution` exactly to the local
  `kgmicrobe.ingredient:p-iv_metal_solution` registry term.

## Evidence

- A fresh exact OLS4 search for the quoted `P-IV Metal Solution` label returned
  zero documents, matching the promotion evidence that no external ontology
  term denotes this lab preparation.
- The `component_assertion` records the UTEX HEPES Medium P-IV formulation as
  complete per liter, including disodium EDTA dihydrate, iron chloride
  hexahydrate, manganese chloride tetrahydrate, zinc chloride, cobalt chloride
  hexahydrate, sodium molybdate dihydrate, and distilled water.
- The `TRACE_ELEMENT` role is source-backed by the same UTEX technical report,
  not by a name-list inference.
- The final SSSOM row exports the local ingredient identity with no `other`
  tokens and with the expected `UNKNOWN_TERM` validation stamp for a local
  registry row.

## Completeness

- The local identifier, stock-solution classification, component assertion,
  trace-element role, occurrence count, and final SSSOM row agree.

## Recommended Edits

- None.
