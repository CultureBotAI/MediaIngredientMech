# `data/ingredients/mapped/Natamycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact `CHEBI:7488` natamycin identity,
ChEBI/PubChem-backed structure, reviewed promotion, source occurrences, and
final exact SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Natamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7488` with
  `ontology_mapping.ontology_id: CHEBI:7488`, label `natamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences and 3 MicrobeDecoder source
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Naphthalene_Sulfonic_Acid` through `Natamycin`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7488` as active `natamycin` with
  formula `C33H47NO13`, CAS `7681-93-8`, and the same InChI and SMILES as the
  record.
- A fresh PubChem name lookup for `natamycin` resolves to a compound with the
  same formula and InChI, confirming the chemical block.
- The final SSSOM row maps `MIM:Natamycin` exactly to `CHEBI:7488`, uses the
  canonical object label, and emits no `other` synonym noise.

## Completeness

- The active ChEBI term, formula, structure, MicrobeDecoder occurrences, empty
  CultureMech occurrence count, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty for the imported trait record.

## Recommended Edits

- None.
