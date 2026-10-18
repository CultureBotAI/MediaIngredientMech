# `data/ingredients/mapped/Narbomycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact `CHEBI:29649` narbomycin identity,
ChEBI/PubChem-backed structure, reviewed promotion, source occurrence, and
final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Narbomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:29649` with
  `ontology_mapping.ontology_id: CHEBI:29649`, label `narbomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences and 1 MicrobeDecoder source
  occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Naphthalene_Sulfonic_Acid` through `Natamycin`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:29649` as active `narbomycin` with
  formula `C28H47NO7`, and the same InChI and SMILES as the record.
- A fresh PubChem name lookup for `narbomycin` resolves to a compound with the
  same formula and InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Narbomycin` exactly to `CHEBI:29649`, uses the
  canonical object label, and emits no `other` synonym noise.

## Completeness

- The active ChEBI term, formula, structure, MicrobeDecoder occurrence, empty
  CultureMech occurrence count, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty for the imported trait record.

## Recommended Edits

- None.
