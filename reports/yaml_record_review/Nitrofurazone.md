# `data/ingredients/mapped/Nitrofurazone.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed `Nitrofurazone` record exact-maps to active
`CHEBI:44368` with matching formula, structure, ChEBI synonym, and final SSSOM
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrofurazone.yaml`.
- Identifier and grounding: `identifier: CHEBI:44368` with
  `ontology_mapping.ontology_id: CHEBI:44368`, label `nitrofurazone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:44368` as active `nitrofurazone`
  with formula `C6H6N4O4`, CAS `59-87-0`, and the same InChI and SMILES as the
  record.
- A fresh PubChem lookup for CAS `59-87-0` resolves to formula `C6H6N4O4` and
  the same base connectivity as the CHEBI record.
- The final SSSOM row maps `MIM:Nitrofurazone` exactly to `CHEBI:44368`; its
  `other` values are the reviewed ChEBI IUPAC-style synonym plus
  `CAS:59-87-0`.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final
  SSSOM row agree.
- Empty occurrence statistics are expected for this CultureBotHT antimicrobial
  panel entry.

## Recommended Edits

- None.
