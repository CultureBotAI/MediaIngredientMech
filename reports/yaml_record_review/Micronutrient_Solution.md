# `data/ingredients/mapped/Micronutrient_Solution.yaml`

## Verdict

Pass. The formulation-specific local stock-solution identity, #288 fallback
registry mapping, occurrence count, and final exact kg-microbe row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Micronutrient_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:micronutrient_solution` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:micronutrient_solution`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgso4_X_7_H2o` through `Middlebrook_7H10_Agar`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- The #288 curation searched CHEBI, NCIT, MeSH, FOODON, and ENVO by label and
  synonym and kept this as a local stock-solution mint because no external term
  denotes this multi-component preparation.
- A fresh exact OLS4 search for `micronutrient solution` returned no same-label
  external class; the only hit was the different `Gaffron micronutrient
  solution` class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Micronutrient_Solution` to
  `kgmicrobe.ingredient:micronutrient_solution` with empty `other`.

## Completeness

- The local identifier, fallback registry mapping, stock-solution type, 1/1
  occurrence count, and final registry row agree.

## Recommended Edits

- None.
