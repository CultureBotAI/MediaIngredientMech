# `data/ingredients/mapped/Nicotinamide.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:17154` nicotinamide identity,
CAS-backed structure, occurrence count, synonym cleanup, and final SSSOM row
pass, but `VITAMIN_SOURCE` is still only a provisional ChEBI-ancestry
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicotinamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:17154` with
  `ontology_mapping.ontology_id: CHEBI:17154`, label `nicotinamide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 254 CultureMech recipe occurrences across 254 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicl2_X_2_H2o` through `Nicotinamide_N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17154` as active `nicotinamide` with
  formula `C6H6N2O`, CAS `98-92-0`, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `98-92-0` resolves to nicotinamide with the
  same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nicotinamide` exactly to `CHEBI:17154` and the
  exported `other` values are same-substance aliases plus `CAS:98-92-0`.
- Major: `nutritional_roles.VITAMIN_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry. The raw
  CultureMech `Growth factor` text is retained only as filtered RAW_TEXT.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 254/254 occurrence count,
  synonyms, and final exact row otherwise agree.
- The remaining consequential gap is the unsupported provisional vitamin role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nicotinamide.yaml`, replace the
  provisional ChEBI-ancestry `VITAMIN_SOURCE` evidence with inspected
  source-backed role evidence, or remove the role.
