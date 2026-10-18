# `data/ingredients/mapped/Oxolinate.yaml`

## Verdict

Pass. The MicrobeDecoder `Oxolinate` label exact-matches active `CHEBI:59066`
oxolinate, and the populated structure matches the deprotonated oxolinate
identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxolinate.yaml`.
- Identifier and grounding: `identifier: CHEBI:59066` with
  `ontology_mapping.ontology_id: CHEBI:59066`, label `oxolinate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: four MicrobeDecoder source-column occurrences across
  `BacDive_Antibiotic_resistance` and `BacDive_Antibiotic_sensitivity`; zero
  CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxolinate` exactly
  to `CHEBI:59066`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:59066` as active `oxolinate`, the
  conjugate base of oxolinic acid, and reports the same formula, InChI, SMILES,
  and mass stored in the YAML.
- The MicrobeDecoder import and review history use the same exact ChEBI label.
- The final SSSOM row carries the MicrobeDecoder source and the manual
  `review-ingredients` approval stamp.
- No synonyms, roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, deprotonated structure, source occurrence count, and
  final SSSOM row agree.
- The record does not export oxolinic-acid parent labels as oxolinate
  synonyms.

## Recommended Edits

- None.
