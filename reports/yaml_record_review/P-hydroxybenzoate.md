# `data/ingredients/mapped/P-hydroxybenzoate.yaml`

## Verdict

Needs curation; major. The `CHEBI:17879` 4-hydroxybenzoate identity, CAS-RN,
and final SSSOM row pass, but the `CARBON_SOURCE` role is only a provisional
in-session LLM assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/P-hydroxybenzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17879` with
  `ontology_mapping.ontology_id: CHEBI:17879`, label `4-hydroxybenzoate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: six CultureMech occurrences across six media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 for this
  CHEBI-only record.
- The final SSSOM row was inspected directly and maps
  `MIM:P-hydroxybenzoate` exactly to `CHEBI:17879`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17879` as active
  `4-hydroxybenzoate`, reports CAS `456-23-5`, and reports the same formula,
  InChI, and SMILES stored in the YAML.
- The single active synonym, `4-hydroxybenzoate`, is the ChEBI exact synonym
  and is not redundantly exported in `other`.
- The final SSSOM row carries only the matching structured CAS value,
  `CAS:456-23-5`, in `other`.
- The row-review manifest already confirmed the `CHEBI:17879` ontology row.
- The `CARBON_SOURCE` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from an in-session LLM role assignment.

## Completeness

- The active ChEBI term, CAS-RN, anion structure, occurrence count, and exact
  final SSSOM row agree.

## Recommended Edits

- Major: in `data/ingredients/mapped/P-hydroxybenzoate.yaml`, either replace
  `nutritional_roles.CARBON_SOURCE` with cited experimental or recipe evidence,
  or remove the provisional role facet until source-backed role evidence is
  curated.
