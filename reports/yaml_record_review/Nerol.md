# `data/ingredients/mapped/Nerol.yaml`

## Verdict

Pass. The exact `CHEBI:29452` nerol identity, CAS-backed structure, reviewed
ChEBI synonym, and final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nerol.yaml`.
- Identifier and grounding: `identifier: CHEBI:29452` with
  `ontology_mapping.ontology_id: CHEBI:29452`, label `nerol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Neomycin_F` through `Netilmycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:29452` as active `nerol` with
  formula `C10H18O`, CAS `106-25-2`, the same InChI and SMILES as the record,
  and the retained IUPAC synonym.
- A fresh PubChem CAS lookup for `106-25-2` resolves to a compound with the
  same formula and InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Nerol` exactly to `CHEBI:29452` and keeps only
  the checked IUPAC synonym plus `CAS:106-25-2` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 0/0 occurrence count, and
  final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
