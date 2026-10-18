# `data/ingredients/mapped/N-Acetyl-L-aspartic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:21547` N-acetyl-L-aspartic acid identity, CultureBotHT
CAS provenance, structure, ChEBI synonym, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-Acetyl-L-aspartic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:21547` with
  `ontology_mapping.ontology_id: CHEBI:21547`, label
  `N-acetyl-L-aspartic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-Acetyl-L-Glutamic_Acid` through
  `N-_2-acetamido-2-aminoethanesulfonic_Acid`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:21547` as active
  `N-acetyl-L-aspartic acid` and exposes the stored IUPAC name as an exact
  synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-Acetyl-L-aspartic_Acid` to `CHEBI:21547` with the ChEBI IUPAC synonym
  and `CAS:997-55-7` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, synonym, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
