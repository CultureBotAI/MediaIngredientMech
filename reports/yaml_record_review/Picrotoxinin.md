# `data/ingredients/mapped/Picrotoxinin.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:8206`
picrotoxinin, and the final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Picrotoxinin.yaml`.
- Identifier and grounding: `identifier: CHEBI:8206` with
  `ontology_mapping.ontology_id: CHEBI:8206`, label `picrotoxinin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8206` resolves `CHEBI:8206`
  `picrotoxinin` and the exported systematic synonym on the same term.
- A fresh PubChem lookup for CAS `17617-45-7` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Picrotoxinin`
  exactly to `CHEBI:8206`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `17617-45-7`, structured
  formula, SMILES, and InChI all describe picrotoxinin.
- The final SSSOM row exports the systematic CHEBI exact synonym and
  `CAS:17617-45-7`; both are exact for the current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
