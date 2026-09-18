# `data/ingredients/mapped/Nitrofurantoin.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed `Nitrofurantoin` record exact-maps to active
`CHEBI:71415` with matching formula, structure, ChEBI synonym, and final SSSOM
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrofurantoin.yaml`.
- Identifier and grounding: `identifier: CHEBI:71415` with
  `ontology_mapping.ontology_id: CHEBI:71415`, label `nitrofurantoin`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech recipe occurrences are recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:71415` as active
  `nitrofurantoin` with formula `C8H6N4O5`, CAS `67-20-9`, and the same InChI
  and SMILES as the record.
- A fresh PubChem lookup for CAS `67-20-9` resolves to formula `C8H6N4O5` and
  the same InChI.
- The final SSSOM row maps `MIM:Nitrofurantoin` exactly to `CHEBI:71415`; its
  `other` values are the reviewed ChEBI IUPAC-style synonym plus
  `CAS:67-20-9`.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, synonym, and final
  SSSOM row agree.
- Empty occurrence statistics are expected for this CultureBotHT antimicrobial
  panel entry.

## Recommended Edits

- None.
