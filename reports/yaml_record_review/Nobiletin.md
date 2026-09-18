# `data/ingredients/mapped/Nobiletin.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed `Nobiletin` record exact-maps to active
`CHEBI:7602` with matching formula, structure, ChEBI synonym, and final SSSOM
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Nobiletin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7602` with
  `ontology_mapping.ontology_id: CHEBI:7602`, label `nobiletin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7602` as active `nobiletin` with
  formula `C21H22O8`, CAS `478-01-3`, and the same InChI and SMILES as the
  record.
- A fresh PubChem lookup for CAS `478-01-3` resolves to formula `C21H22O8` and
  the same InChI.
- The final SSSOM row maps `MIM:Nobiletin` exactly to `CHEBI:7602`; its
  `other` values are the reviewed ChEBI IUPAC-style synonym plus
  `CAS:478-01-3`.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final
  SSSOM row agree.
- Empty occurrence statistics are expected for this CultureBotHT record.

## Recommended Edits

- None.
