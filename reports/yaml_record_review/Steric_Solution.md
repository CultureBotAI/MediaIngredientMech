# `data/ingredients/mapped/Steric_Solution.yaml`

## Verdict

Pass. The record intentionally models a named Steric solution preparation as a
local `kgmicrobe.ingredient` identity, has no unsafe SSSOM synonym payload, and
is the only live Steric-solution per-record file under `data`.

## Identity

- Reviewed record: `data/ingredients/mapped/Steric_Solution.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:steric_solution`
  with `ontology_mapping.ontology_id: kgmicrobe.ingredient:steric_solution`,
  label `Steric solution`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`,
  `ingredient_type: STOCK_SOLUTION`, and `solution_type: OTHER`.
- Synonyms: one `Steric solution` raw-text source label from the MIM queue.
- Occurrences: 1 source occurrence in 1 CultureMech medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Steffimycin` through `Streptomycin`: exited 0 and wrote zero ERROR rows.
- Engine A term validation was skipped for this local `kgmicrobe.ingredient`
  target; the non-OBO CURIE is covered by the product validator rather than
  OAK.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 lookup for `Steric solution` returned zero documents,
  matching the local fallback decision in `MIM curation (#288)`.
- A gitignore-independent `find data -name '*Steric*'` found only
  `data/ingredients/mapped/Steric_Solution.yaml`; there is no live unmapped
  per-record duplicate.
- The final SSSOM row is a local identity row with empty `other`.

## Completeness

- The local identifier, stock-solution type, raw label, occurrence count,
  aggregate copy, and final SSSOM row agree.
- The component formula for this named preparation remains unresolved, but
  that is explicitly recorded in the May 2026 and August 2026 curation notes.

## Recommended Edits

- None.
