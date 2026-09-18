# `data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml`

## Verdict

Needs curation. The local DSMZ Medium 976 mineral-solution cross-reference,
fallback registry mapping, #213/#308 remapping, and final exact row pass, but a
malformed open-parenthesis surface still publishes in final SSSOM `other`.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mineral_Solution_See_Medium_No_976.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mineral_solution_see_medium_no_976` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:mineral_solution_see_medium_no_976`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: the record carries a stale 0/0 occurrence count even though the
  2026-08-30 alias backfill and residual triage both record one CultureMech
  mention of its malformed surface.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mineral_3B_Solution_Minus_Phosphorus` through `Minerals`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS hit
  before the fallback registry promotion.
- The #213/#308 curation reaccepted a local identifier for this MediaDive
  cross-reference under the #288 stock-solution convention used by its
  existing cross-reference siblings.
- A fresh exact EBI OLS4 lookup returned no same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mineral_Solution_See_Medium_No_976` to
  `kgmicrobe.ingredient:mineral_solution_see_medium_no_976`.

## Completeness

- The local fallback identity and final exact row agree.
- The final SSSOM `other` field still exports
  `Mineral solution (see Medium No. 976`, which is an unbalanced raw
  CultureMech parse artifact rather than a clean synonym.
- The 0/0 occurrence count is stale relative to the x1 CultureMech mention
  that was recovered by the alias backfill.

## Recommended Edits

- Major: mark `Mineral solution (see Medium No. 976` as `REJECTED_LABEL`, or
  otherwise keep it out of final SSSOM `other` while preserving it only as a
  resolver alias if needed.
- Minor: refresh `occurrence_statistics` from the post-alias CultureMech
  occurrence table so the record no longer reports 0/0.
