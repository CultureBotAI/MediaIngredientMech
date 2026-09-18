# `data/ingredients/mapped/Naringin.yaml`

## Verdict

Pass. The exact `CHEBI:28819` naringin identity, CAS-backed structure, ChEBI
IUPAC synonym, and final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Naringin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28819` with
  `ontology_mapping.ontology_id: CHEBI:28819`, label `naringin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media; the record was
  created from CultureBotHT CAS input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Naphthalene_Sulfonic_Acid` through `Natamycin`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28819` as active `naringin` with
  formula `C27H32O14`, CAS `10236-47-2`, and the same InChI and SMILES as the
  record.
- A fresh PubChem CAS lookup for `10236-47-2` resolves to naringin with the
  same InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Naringin` exactly to `CHEBI:28819`, uses the
  canonical object label, and keeps only the same-substance IUPAC synonym plus
  `CAS:10236-47-2` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, IUPAC synonym, empty
  CultureMech occurrence count, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty for the CultureBotHT compound record.

## Recommended Edits

- None.
