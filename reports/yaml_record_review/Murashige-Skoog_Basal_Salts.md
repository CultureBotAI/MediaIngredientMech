# `data/ingredients/mapped/Murashige-Skoog_Basal_Salts.yaml`

## Verdict

Pass. The local Murashige-Skoog basal salts stock identity, 1/1 occurrence
count, fallback registry rationale, and final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Murashige-Skoog_Basal_Salts.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:murashige-skoog_basal_salts` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:murashige-skoog_basal_salts`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mucin_From_Porcine_Stomach_Type_III` through `Mycobactin_J`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- A fresh exact EBI OLS4 lookup for `Murashige-Skoog basal salts` returned no
  same-label external class.
- #288 curation kept this as a local mint because the label denotes a named
  multi-component basal-salts preparation rather than an external ontology
  substance.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Murashige-Skoog_Basal_Salts` to the local registry identifier with empty
  `other`.

## Completeness

- The local stock identity, 1/1 occurrence count, fallback registry rationale,
  and final exact row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
