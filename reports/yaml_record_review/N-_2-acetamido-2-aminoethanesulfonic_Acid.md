# `data/ingredients/mapped/N-_2-acetamido-2-aminoethanesulfonic_Acid.yaml`

## Verdict

Needs curation. The exact `CHEBI:39060` ACES identity, CAS metadata, duplicate
merge, occurrence count, and final exact row pass, but the buffer role is only
a provisional ChEBI-ancestry prediction.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/N-_2-acetamido-2-aminoethanesulfonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:39060` with
  `ontology_mapping.ontology_id: CHEBI:39060`, label
  `N-(2-acetamido)-2-aminoethanesulfonic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 15 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-Acetyl-L-Glutamic_Acid` through
  `N-_2-acetamido-2-aminoethanesulfonic_Acid`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:39060` as active
  `N-(2-acetamido)-2-aminoethanesulfonic acid` and exposes
  `2-[(2-amino-2-oxoethyl)amino]ethanesulfonic acid` as an exact synonym.
- The 2026-08-13 duplicate merge records that `ACES` was a structureless class
  for the same buffer and retained that trivial label as a synonym on this
  structured record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-_2-acetamido-2-aminoethanesulfonic_Acid` to `CHEBI:39060` with
  same-substance synonyms and `CAS:7365-82-4` in `other`.

## Completeness

- The active ChEBI target, CAS RN, ACES duplicate merge, 15/15 occurrence
  count, and final row agree.
- `BUFFER` has only `COMPUTATIONAL_PREDICTION` evidence from ChEBI-ancestry
  closure with a provisional curator note.

## Recommended Edits

- Major: replace the provisional ancestry-derived `BUFFER` role with
  source-backed CultureMech or ontology evidence, or remove the role.
