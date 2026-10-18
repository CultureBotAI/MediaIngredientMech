# `data/ingredients/mapped/N-Acetyl-L-glutamine.yaml`

## Verdict

Pass. The exact `CHEBI:21553` N-acetyl-L-glutamine identity, CultureBotHT CAS
provenance, ChEBI synonyms, structure, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-Acetyl-L-glutamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:21553` with
  `ontology_mapping.ontology_id: CHEBI:21553`, label
  `N-acetyl-L-glutamine`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-Acetyl-L-Glutamic_Acid` through
  `N-_2-acetamido-2-aminoethanesulfonic_Acid`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:21553` as active
  `N-acetyl-L-glutamine` and exposes the stored IUPAC name plus
  `NN(2)-acetyl-L-glutamine` as exact synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-Acetyl-L-glutamine` to `CHEBI:21553` with same-substance synonyms and
  `CAS:2490-97-3` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, synonyms, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
