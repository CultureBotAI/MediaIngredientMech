# `data/ingredients/mapped/N-acetyl-glutamic_Acid.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:172431` Acetyl-Glu identity, FEBA provenance,
structure, occurrence count, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyl-glutamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:172431` with
  `ontology_mapping.ontology_id: CHEBI:172431`, label `Acetyl-Glu`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: ten FEBA media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-_3-oxohexanoyl-dl-homoserine_Lactone` through
  `N-acetyl-glutamine`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:172431` as active `Acetyl-Glu` with
  `2-acetamidopentanedioic acid` as an exact synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetyl-glutamic_Acid` to `CHEBI:172431` with the ChEBI synonym and
  `CAS:5817-08-3` in `other`.

## Completeness

- The active ChEBI target, CAS RN, structure, FEBA occurrence count, and final
  row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
