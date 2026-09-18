# `data/ingredients/mapped/Oleandomycin.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-maps to active `CHEBI:16869`
oleandomycin, and the record does not export unsupported synonyms or roles.

## Identity

- Reviewed record: `data/ingredients/mapped/Oleandomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:16869` with
  `ontology_mapping.ontology_id: CHEBI:16869`, label `oleandomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 104 MicrobeDecoder source-column occurrences across
  `BacDive_Antibiotic_resistance` and `BacDive_Antibiotic_sensitivity`, with
  zero CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16869` as active `oleandomycin` and
  reports the same formula, InChI, SMILES, and mass stored in the YAML.
- The MicrobeDecoder review table marks `Oleandomycin.yaml` approved after an
  OAK canonical-label check, and the live OLS term confirms the same target.
- The final SSSOM row maps `MIM:Oleandomycin` exactly to `CHEBI:16869`, has no
  `other` tokens, and carries the manual MicrobeDecoder review stamp.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, canonical label, formula, structure, mass, and final
  SSSOM row agree.
- No optional slots are missing for the reviewed MicrobeDecoder trait import.

## Recommended Edits

- None.
