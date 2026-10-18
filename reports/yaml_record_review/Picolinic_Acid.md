# `data/ingredients/mapped/Picolinic_Acid.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:28747` picolinic
acid, and the final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Picolinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28747` with
  `ontology_mapping.ontology_id: CHEBI:28747`, label `picolinic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:28747` resolves `CHEBI:28747`
  `picolinic acid` and the exported uppercase synonym on the same term.
- A fresh PubChem lookup for CAS `98-98-6` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Picolinic_Acid`
  exactly to `CHEBI:28747`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `98-98-6`, structured
  formula, SMILES, and InChI all describe picolinic acid.
- The final SSSOM `other` values,
  `PYRIDINE-2-CARBOXYLIC ACID|CAS:98-98-6`, are valid exact synonyms for the
  current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
