# `data/ingredients/mapped/Piplartine.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:8241` Piplartine,
and the final SSSOM row exports only the safe CAS synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Piplartine.yaml`.
- Identifier and grounding: `identifier: CHEBI:8241` with
  `ontology_mapping.ontology_id: CHEBI:8241`, label `Piplartine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8241` resolves `CHEBI:8241`
  `Piplartine`.
- A fresh PubChem lookup for CAS `20069-09-4` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Piplartine` exactly
  to `CHEBI:8241`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `20069-09-4`, structured
  formula, SMILES, and InChI all describe piplartine.
- The final SSSOM row exports only `CAS:20069-09-4` in `other`.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
