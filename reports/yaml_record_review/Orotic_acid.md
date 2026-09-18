# `data/ingredients/mapped/Orotic_acid.yaml`

## Verdict

Pass. The CAS-derived `Orotic acid` grounding resolves to active `CHEBI:16742`,
the chemistry block agrees with that identity, and the final SSSOM `other`
tokens are same-compound names plus the matching structured CAS-RN.

## Identity

- Reviewed record: `data/ingredients/mapped/Orotic_acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16742` with
  `ontology_mapping.ontology_id: CHEBI:16742`, label `orotic acid`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: six CultureMech occurrences across six media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- The final SSSOM row was inspected directly and maps `MIM:Orotic_acid`
  exactly to `CHEBI:16742`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:16742` as active `orotic acid`.
- The YAML CAS-RN `65-86-1`, molecular formula `C5H4N2O4`, InChI, and SMILES
  are consistent with the CHEBI identity.
- The three exported synonyms are same-compound names for orotic acid, and the
  final SSSOM keeps the CAS value in normalized `CAS:65-86-1` form from the
  structured chemistry block.
- No roles, supplied forms, components, or mixture assertions are present.

## Completeness

- The active ChEBI term, CAS-RN, formula, structure, occurrence counts, and
  final SSSOM row agree.
- The stale free-text note about four FEBA formulations is not the source of
  truth for the refreshed six-occurrence CultureMech count and does not reach
  the final SSSOM.

## Recommended Edits

- None.
