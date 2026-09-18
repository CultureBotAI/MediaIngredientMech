# `data/ingredients/mapped/Phenoxyacetic_Acid.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:8075`
phenoxyacetic acid, and the final SSSOM row exports only the structured CAS.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenoxyacetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:8075` with
  `ontology_mapping.ontology_id: CHEBI:8075`, label `phenoxyacetic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8075` resolves `CHEBI:8075`
  `phenoxyacetic acid`.
- A local CAS checksum calculation confirmed that `122-59-8` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenoxyacetic_Acid` exactly to `CHEBI:8075`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe phenoxyacetic acid.
- The final SSSOM row exports only `CAS:122-59-8`, which matches the structured
  CAS-RN.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
