# `data/ingredients/mapped/Oxacillin.yaml`

## Verdict

Pass. The MicrobeDecoder `Oxacillin` label exact-matches active `CHEBI:7809`
oxacillin, the ChEBI structure agrees with the YAML chemistry, and the final
SSSOM row has no unsupported synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Oxacillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7809` with
  `ontology_mapping.ontology_id: CHEBI:7809`, label `oxacillin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 63 MicrobeDecoder source-column occurrences across
  `BacDive_Antibiotic_resistance`, `BacDive_Antibiotic_sensitivity`, and
  `BacDive_Metabolite_utilization`; zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps `MIM:Oxacillin`
  exactly to `CHEBI:7809`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7809` as active `oxacillin` and
  reports the same formula, InChI, SMILES, and mass stored in the YAML.
- The MicrobeDecoder import and review history place this record on the same
  exact ChEBI label used by the live term.
- The final SSSOM row carries the MicrobeDecoder source and the manual
  `review-ingredients` approval stamp.
- No synonyms, roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, formula, structure, source occurrence count, and final
  SSSOM row agree.
- The oxacillin free acid remains distinct from the adjacent
  `Oxacillin_Sodium_Salt` record, preserving the salt boundary.

## Recommended Edits

- None.
