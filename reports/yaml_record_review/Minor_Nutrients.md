# `data/ingredients/mapped/Minor_Nutrients.yaml`

## Verdict

Pass. The local Minor Nutrients stock/pre-mix identity, occurrence count,
fallback registry mapping, and final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Minor_Nutrients.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:minor_nutrients` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:minor_nutrients`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: OTHER`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Minimycin` through `Mitomycin_C`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- #114 curation kept this as a local mint because Minor Nutrients is a named,
  recurring, multi-component preparation rather than an external ontology
  substance.
- A fresh exact EBI OLS4 lookup returned no same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Minor_Nutrients` to `kgmicrobe.ingredient:minor_nutrients` with empty
  `other`.

## Completeness

- The local stock identity, fallback registry rationale, 1/1 occurrence count,
  and final SSSOM row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
