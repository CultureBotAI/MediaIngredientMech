# `data/ingredients/mapped/Phosphate_Buffer_Stock_Solution.yaml`

## Verdict

Needs curation; major. The record correctly preserves a local stock-solution
identity with `NCIT:C29321` only as a close phosphate-buffer parent, but
`BUFFER` is still supported only by a provisional name-list inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Phosphate_Buffer_Stock_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:phosphate_buffer_stock_solution` with
  `ontology_mapping.ontology_id: NCIT:C29321`, label `Phosphate Buffer`,
  source `NCIT`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: 1 CultureMech occurrence in 1 recipe.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- The row-review and unknown-term triage tables were inspected directly; they
  record `kgmicrobe.ingredient:phosphate_buffer_stock_solution` as an expected
  local registry identifier and the `NCIT:C29321` UNKNOWN_TERM result as a
  prefix-validator coverage artifact.
- The final SSSOM rows were inspected directly: they preserve the exact local
  registry identity and the close NCIT parent mapping.

## Evidence

- The 2026-05-05 manual review correctly changed the primary identifier from
  `NCIT:C29321` to the local stock-solution registry CURIE because a phosphate
  buffer stock solution is a preparation variant, not exactly the generic
  phosphate-buffer class.
- The raw CultureMech synonym is a duplicate of the preferred term and is
  filtered from final SSSOM `other`.
- Major: the `BUFFER` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from a provisional curated name-pattern rule.

## Completeness

- The local registry row and the NCIT parent row are complete enough for this
  stock-solution record.
- Physicochemical-role evidence remains incomplete while the buffer role is
  provisional.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Phosphate_Buffer_Stock_Solution.yaml`, replace
  `physicochemical_roles.BUFFER` with source-backed evidence or remove the
  provisional role facet until it is curated.
