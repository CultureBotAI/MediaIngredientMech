# `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`

## Verdict

Needs curation. The local Modified trace vitamins stock identity, occurrence
count, fallback registry mapping, and final exact row pass, but `see below`
recipe text still publishes in final SSSOM `other`.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Modified_Trace_Vitamins.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:modified_trace_vitamins` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:modified_trace_vitamins`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: two CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mnso4_X_7_H2o` through `Modified_Trace_Vitamins`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- `mappings/unmapped_ingredients_ols_exact_audit.tsv` recorded no exact OLS hit
  before the fallback registry promotion.
- #288 curation kept this as a local mint because the label denotes a named
  multi-component vitamin preparation rather than an external ontology
  substance.
- A fresh exact EBI OLS4 lookup returned no same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Modified_Trace_Vitamins` to the local registry identifier.

## Completeness

- The local stock identity, 2/2 occurrence count, fallback registry rationale,
  and final exact row agree.
- The final SSSOM `other` field still exports `Modified trace vitamins (see
  below)`, which is recipe navigation text rather than a clean synonym.

## Recommended Edits

- Major: mark `Modified trace vitamins (see below)` as `REJECTED_LABEL`, or
  otherwise preserve it only as a resolver alias while filtering it from final
  SSSOM `other`.
