# `data/ingredients/mapped/P-ii_Metal_Solution.yaml`

## Verdict

Pass. `P-II Metal Solution` is a named stock solution with no exact public
ontology term, so the local `kgmicrobe.ingredient:p-ii_metal_solution` identity
row is the right fallback.

## Identity

- Reviewed record: `data/ingredients/mapped/P-ii_Metal_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:p-ii_metal_solution` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:p-ii_metal_solution`,
  label `P-II Metal Solution`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Occurrences: one CultureMech occurrence in one medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct CHEBI/OBO label validation was skipped for this local
  `kgmicrobe.ingredient` record.
- The final SSSOM row was inspected directly and maps
  `MIM:P-ii_Metal_Solution` exactly to the local
  `kgmicrobe.ingredient:p-ii_metal_solution` registry term.

## Evidence

- A fresh exact OLS4 search for the quoted `P-II Metal Solution` label returned
  zero documents, matching the promotion evidence that no external ontology
  term denotes this lab preparation.
- The record uses `STOCK_SOLUTION` plus `TRACE_METAL_MIX`, so it correctly
  mints under `kgmicrobe.ingredient` rather than `kgmicrobe.compound`.
- The final SSSOM row exports the local ingredient identity with no `other`
  tokens and with the expected `UNKNOWN_TERM` validation stamp for a local
  registry row.
- No unsupported roles or chemical structure fields are asserted.

## Completeness

- The local identifier, stock-solution classification, occurrence count, and
  final SSSOM row agree.
- Component-level recipe curation remains intentionally absent until a bounded
  P-II stock formulation source is curated.

## Recommended Edits

- None.
