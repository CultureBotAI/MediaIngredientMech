# `data/ingredients/mapped/O-Phospho-L-serine.yaml`

## Verdict

Pass. The CultureMech residual ingredient exact-maps to active `CHEBI:15811`
`O-phospho-L-serine`, and its restored mapping evidence is present in the final
SSSOM source field.

## Identity

- Reviewed record: `data/ingredients/mapped/O-Phospho-L-serine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15811` with
  `ontology_mapping.ontology_id: CHEBI:15811`, label `O-phospho-L-serine`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `match_level: EXACT`.
- Occurrences: one CultureMech media occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:15811` as active
  `O-phospho-L-serine`, lists `O-Phospho-L-serine` as a related synonym, and
  preserves the L-serine stereochemistry in its definition.
- `mappings/culturemech_residual_groundings.tsv` records the original
  `O-Phospho-L-serine` residual as a new `CHEBI:15811` record, matching both
  the `CREATED_FROM_CULTUREMECH_RESIDUAL` history entry and the later
  structured evidence repair.
- The final SSSOM row maps `MIM:O-Phospho-L-serine` exactly to `CHEBI:15811`,
  has no `other` tokens, and includes
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.
- No unsupported synonyms, roles, components, supplied forms, or environmental
  contexts are asserted.

## Completeness

- The active ChEBI term, exact CultureMech grounding, restored structured
  evidence, occurrence count, and final SSSOM row agree.
- No optional chemistry fields are required for this residual CultureMech
  lexical grounding to an active ChEBI class.

## Recommended Edits

- None.
