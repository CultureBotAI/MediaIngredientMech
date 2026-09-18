# `data/ingredients/mapped/N-acetyl-glutamine.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:73685` N(2)-acetylglutamine identity, FEBA
provenance, structure, occurrence count, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyl-glutamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:73685` with
  `ontology_mapping.ontology_id: CHEBI:73685`, label
  `N(2)-acetylglutamine`, source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: ten FEBA media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-_3-oxohexanoyl-dl-homoserine_Lactone` through
  `N-acetyl-glutamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:73685` as active
  `N(2)-acetylglutamine` and exposes the stored IUPAC name plus
  `N(2)-acetylglutamine` as exact synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetyl-glutamine` to `CHEBI:73685` with same-substance synonyms and
  `CAS:5817-09-4` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, FEBA occurrence count, and final
  row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
