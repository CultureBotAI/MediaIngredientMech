# `data/ingredients/mapped/P-Coumaric_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-RN `501-98-4` resolves to active `CHEBI:32374`
trans-4-coumaric acid, and both the reviewed synonym and final CAS token agree
with that trans-isomer identity.

## Identity

- Reviewed record: `data/ingredients/mapped/P-Coumaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:32374` with
  `ontology_mapping.ontology_id: CHEBI:32374`, label
  `trans-4-coumaric acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `501-98-4`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data --labels` exited 0 across this
  five-record CHEBI batch.
- The final SSSOM row was inspected directly and maps
  `MIM:P-Coumaric_Acid` exactly to `CHEBI:32374`.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32374` as active
  `trans-4-coumaric acid`, reports CAS `501-98-4`, and carries both
  `p-Coumaric acid` and `(2E)-3-(4-hydroxyphenyl)prop-2-enoic acid` as
  same-term synonyms.
- The YAML formula `C9H8O3`, InChI, and SMILES agree with the live ChEBI
  trans-isomer structure.
- The final SSSOM row correctly emits the reviewed IUPAC synonym and
  `CAS:501-98-4` in `other`.
- The row-review manifest already confirmed the `CHEBI:32374` ontology row.
- No roles, supplied forms, or components are asserted.

## Completeness

- The active ChEBI term, CAS-RN, trans-isomer structure, exact synonym, and
  final SSSOM row agree.

## Recommended Edits

- None.
