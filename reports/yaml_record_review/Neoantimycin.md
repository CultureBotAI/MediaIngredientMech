# `data/ingredients/mapped/Neoantimycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact `CHEBI:215310` neoantimycin identity,
ChEBI/PubChem-backed structure, reviewed promotion, source occurrence, and
final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Neoantimycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:215310` with
  `ontology_mapping.ontology_id: CHEBI:215310`, label `Neoantimycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences and 1 MicrobeDecoder source
  occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Natural_Sea_Water` through `Neomycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:215310` as active `Neoantimycin` with
  formula `C36H46N2O12` and the same InChI and SMILES as the record.
- A fresh PubChem name lookup for `Neoantimycin` resolves to the same formula,
  InChI, and SMILES, confirming the chemical block.
- The final SSSOM row maps `MIM:Neoantimycin` exactly to `CHEBI:215310`, uses
  the canonical object label, and emits no `other` synonym noise.

## Completeness

- The active ChEBI term, formula, structure, MicrobeDecoder source occurrence,
  empty CultureMech occurrence count, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty for the imported trait record.

## Recommended Edits

- None.
