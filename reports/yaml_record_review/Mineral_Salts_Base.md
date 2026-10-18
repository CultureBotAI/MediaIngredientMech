# `data/ingredients/mapped/Mineral_Salts_Base.yaml`

## Verdict

Pass. The local Mineral salts base stock-solution identity, fallback registry
mapping, and final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mineral_Salts_Base.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mineral_salts_base` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:mineral_salts_base`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: no CultureMech recipe occurrences.

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
- #288 curation kept this as a local mint because Mineral salts base is a
  named multi-component preparation rather than an external ontology
  substance.
- A fresh exact EBI OLS4 lookup returned no same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mineral_Salts_Base` to
  `kgmicrobe.ingredient:mineral_salts_base` with empty `other`.

## Completeness

- The local stock identity, fallback registry rationale, zero CultureMech
  occurrence count, and final SSSOM row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
