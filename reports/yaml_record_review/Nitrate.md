# `data/ingredients/mapped/Nitrate.yaml`

## Verdict

Pass. The MicrobeDecoder and CultureMech nitrate surface exactly maps to
active `CHEBI:17632`, and its ChEBI/PubChem structure, reviewed import
history, occurrence counts, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17632` with
  `ontology_mapping.ontology_id: CHEBI:17632`, label `nitrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 7 CultureMech recipe occurrences across 7 media, plus 2321
  MicrobeDecoder source occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Niso4_X_6_H2o` through `Nitrilotriacetic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17632` as active `nitrate` with
  formula `NO3` and the same InChI and SMILES as the record.
- The final SSSOM row maps `MIM:Nitrate` exactly to `CHEBI:17632` and emits no
  `other` synonym noise.

## Completeness

- The active ChEBI term, formula, structure, imported MicrobeDecoder evidence,
  refreshed CultureMech count, ingredient type, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
