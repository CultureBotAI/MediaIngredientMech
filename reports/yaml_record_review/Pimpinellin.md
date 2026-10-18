# `data/ingredients/mapped/Pimpinellin.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:8213` Pimpinellin,
and the final SSSOM row exports only the safe CAS synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Pimpinellin.yaml`.
- Identifier and grounding: `identifier: CHEBI:8213` with
  `ontology_mapping.ontology_id: CHEBI:8213`, label `Pimpinellin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8213` resolves `CHEBI:8213`
  `Pimpinellin`.
- A fresh PubChem lookup for CAS `131-12-4` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Pimpinellin`
  exactly to `CHEBI:8213`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `131-12-4`, structured
  formula, SMILES, and InChI all describe pimpinellin.
- The final SSSOM row exports only `CAS:131-12-4` in `other`.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
