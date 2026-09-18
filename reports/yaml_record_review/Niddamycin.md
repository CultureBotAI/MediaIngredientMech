# `data/ingredients/mapped/Niddamycin.yaml`

## Verdict

Pass. The MicrobeDecoder source label exactly maps to active `CHEBI:31908`
Niddamycin, and its ChEBI/PubChem structure, reviewed import history, and final
SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Niddamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:31908` with
  `ontology_mapping.ontology_id: CHEBI:31908`, label `Niddamycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1 MicrobeDecoder source occurrence and no CultureMech media
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicotine_Fluka` through `Nisin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:31908` as active `Niddamycin` with
  formula `C39H63NO14` and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for the ChEBI CAS `20283-69-6` resolves to
  niddamycin with a matching formula and structure.
- The final SSSOM row maps `MIM:Niddamycin` exactly to `CHEBI:31908` and emits
  no `other` synonym noise.

## Completeness

- The active ChEBI term, formula, structure, MicrobeDecoder occurrence count,
  ingredient type, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
