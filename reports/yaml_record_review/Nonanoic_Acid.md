# `data/ingredients/mapped/Nonanoic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed `Nonanoic acid` record exact-maps to active
`CHEBI:29019` with matching formula, structure, synonym, and final SSSOM
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Nonanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:29019` with
  `ontology_mapping.ontology_id: CHEBI:29019`, label `nonanoic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:29019` as active `nonanoic acid`
  with formula `C9H18O2`, CAS `112-05-0`, and the same InChI and SMILES as the
  record.
- The final SSSOM row maps `MIM:Nonanoic_Acid` exactly to `CHEBI:29019`; its
  `other` values are `Pelargonic acid` and `CAS:112-05-0`.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final SSSOM
  row agree.
- Empty occurrence statistics are expected for this CultureBotHT source record.

## Recommended Edits

- None.
