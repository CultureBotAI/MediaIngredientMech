# `data/ingredients/mapped/Perillic_Acid.yaml`

## Verdict

Pass. The record now maps exactly to the stereospecific `CHEBI:109544` term for
the minus perillic-acid enantiomer, and the inherited stereo-unspecified label
is rejected rather than exported.

## Identity

- Reviewed record: `data/ingredients/mapped/Perillic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:109544` with
  `ontology_mapping.ontology_id: CHEBI:109544`, label
  `(4R)-4-(1-methylethenyl)-1-cyclohexenecarboxylic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:109544` resolves the current
  stereospecific CHEBI target.
- The final SSSOM row was inspected directly and maps `MIM:Perillic_Acid`
  exactly to `CHEBI:109544`.

## Evidence

- The #456 curator judgment records why PubChem CID 5702197 supports replacing
  the old stereo-unspecified `CHEBI:36999` parent with the current
  `CHEBI:109544` target.
- The structured InChI and SMILES now carry stereochemistry for the same
  enantiomer.
- The inherited `4-(prop-1-en-2-yl)cyclohex-1-ene-1-carboxylic acid` parent
  label is typed `REJECTED_LABEL`, and final SSSOM exports no `other` tokens.

## Completeness

- No consequential gap was found after the stereochemical regrounding.

## Recommended Edits

- None.
