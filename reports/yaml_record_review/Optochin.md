# `data/ingredients/mapped/Optochin.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-maps to active `CHEBI:86455` optochin,
and the record does not export unsupported synonyms or roles.

## Identity

- Reviewed record: `data/ingredients/mapped/Optochin.yaml`.
- Identifier and grounding: `identifier: CHEBI:86455` with
  `ontology_mapping.ontology_id: CHEBI:86455`, label `optochin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 18 MicrobeDecoder source-column occurrences across
  `BacDive_Antibiotic_resistance` and `BacDive_Antibiotic_sensitivity`, with
  zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:86455` as active `optochin` and
  reports the same formula, InChI, SMILES, and mass stored in the YAML.
- The MicrobeDecoder review table marks `Optochin.yaml` approved after an OAK
  canonical-label check, and the live OLS term confirms the same target.
- The final SSSOM row maps `MIM:Optochin` exactly to `CHEBI:86455`, has no
  `other` tokens, and carries the manual MicrobeDecoder review stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, canonical label, formula, structure, mass, and final
  SSSOM row agree.
- No optional slots are missing for the reviewed MicrobeDecoder trait import.

## Recommended Edits

- None.
