# `data/ingredients/mapped/Phenazine_Methosulfate.yaml`

## Verdict

Pass. The CAS-to-CHEBI lookup maps to active `CHEBI:8055`
5-methylphenazinium methyl sulfate, and the final SSSOM synonyms match the
structured salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenazine_Methosulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:8055` with
  `ontology_mapping.ontology_id: CHEBI:8055`, label
  `5-methylphenazinium methyl sulfate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8055` resolves `CHEBI:8055`
  `5-methylphenazinium methyl sulfate`.
- A local CAS checksum calculation confirmed that `299-11-6` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenazine_Methosulfate` exactly to `CHEBI:8055`.

## Evidence

- The CAS-derived CHEBI primary identifier, mapping target, structured formula,
  InChI, SMILES, and exact chemical synonym all describe phenazine methosulfate.
- The `CAS_RN_LOOKUP` grade accurately records how the mapping was established;
  Rule D still emits the own-identifier row as `skos:exactMatch`.
- The final SSSOM row exports only the exact synonym and `CAS:299-11-6`.

## Completeness

- No consequential gap was found for this CAS-to-CHEBI mapping.

## Recommended Edits

- None.
