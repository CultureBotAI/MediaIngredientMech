# `data/ingredients/mapped/N-Acetyl-L-Glutamic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:17533` N-acetyl-L-glutamic acid identity,
CultureBotHT CAS provenance, duplicate absorption, structure, and final exact
row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-Acetyl-L-Glutamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17533` with
  `ontology_mapping.ontology_id: CHEBI:17533`, label
  `N-acetyl-L-glutamic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: two CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-Acetyl-L-Glutamic_Acid` through
  `N-_2-acetamido-2-aminoethanesulfonic_Acid`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17533` as active
  `N-acetyl-L-glutamic acid` and exposes the stored IUPAC name as an exact
  synonym.
- The 2026-05-11 duplicate absorption kept `N-alpha-Acetyl-L-glutamate` on the
  exact stereochemistry and formula represented by `CHEBI:17533`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-Acetyl-L-Glutamic_Acid` to `CHEBI:17533` with same-substance synonyms
  and `CAS:1188-37-0` in `other`.

## Completeness

- The active ChEBI target, CAS RN, duplicate absorption, 2/2 occurrence count,
  and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
