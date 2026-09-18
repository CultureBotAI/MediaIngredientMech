# `data/ingredients/mapped/Mwc_Metal_Solution.yaml`

## Verdict

Pass. The local MWC Metal Solution stock identity, occurrence count, fallback
registry rationale, and final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mwc_Metal_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mwc_metal_solution` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:mwc_metal_solution`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: TRACE_METAL_MIX`.
- Occurrences: three CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mucin_From_Porcine_Stomach_Type_III` through `Mycobactin_J`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- A fresh exact EBI OLS4 lookup for `MWC Metal Solution` returned no same-label
  external class.
- #114 curation kept this as a local mint because the label denotes a named,
  recurring, multi-component metal stock rather than an external ontology
  substance.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mwc_Metal_Solution` to the local registry identifier with empty `other`.

## Completeness

- The local stock identity, 3/3 occurrence count, fallback registry rationale,
  and final exact row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
