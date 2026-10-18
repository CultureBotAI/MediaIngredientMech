# `data/ingredients/mapped/Nicotinamide_N-oxide.yaml`

## Verdict

Pass. The exact `CHEBI:89640` nicotinamide N-oxide identity, CAS-backed
structure, CultureBotHT provenance, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicotinamide_N-oxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:89640` with
  `ontology_mapping.ontology_id: CHEBI:89640`, label
  `Nicotinamide N-oxide`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicl2_X_2_H2o` through `Nicotinamide_N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:89640` as active
  `Nicotinamide N-oxide` with formula `C6H6N2O2`, CAS `1986-81-8`, and the
  same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `1986-81-8` resolves to nicotinamide N-oxide
  with the same InChI, confirming the chemical block and CultureBotHT CAS.
- The final SSSOM row maps `MIM:Nicotinamide_N-oxide` exactly to `CHEBI:89640`
  and exports only `CAS:1986-81-8` in `other`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, CultureBotHT provenance,
  ingredient type, and final exact row agree.
- No role, component, or environment assertions are present; those optional
  slots are appropriately empty.

## Recommended Edits

- None.
