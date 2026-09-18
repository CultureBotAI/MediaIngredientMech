# `data/ingredients/mapped/Oxytetracycline.yaml`

## Verdict

Pass. The MicrobeDecoder `Oxytetracycline` label exact-matches active
`CHEBI:27701` oxytetracycline, and the structure agrees with the anhydrous
free-base record rather than the adjacent hydrochloride salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxytetracycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:27701` with
  `ontology_mapping.ontology_id: CHEBI:27701`, label `oxytetracycline`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 41 MicrobeDecoder source-column occurrences across
  `BacDive_Antibiotic_resistance`, `BacDive_Antibiotic_sensitivity`, and
  `BacDive_Metabolite_production`; zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxytetracycline`
  exactly to `CHEBI:27701`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:27701` as active
  `oxytetracycline` and reports the same formula, InChI, SMILES, and mass
  stored in the YAML.
- The MicrobeDecoder import and review history place this record on the same
  exact ChEBI label used by the live term.
- The final SSSOM row carries the MicrobeDecoder source and the manual
  `review-ingredients` approval stamp.
- No synonyms, roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, formula, structure, source occurrence count, and final
  SSSOM row agree.
- `Oxytetracycline_Hydrochloride` remains a separate salt record, so this row
  does not erase salt specificity.

## Recommended Edits

- None.
