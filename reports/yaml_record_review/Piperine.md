# `data/ingredients/mapped/Piperine.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:28821` piperine,
and the final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Piperine.yaml`.
- Identifier and grounding: `identifier: CHEBI:28821` with
  `ontology_mapping.ontology_id: CHEBI:28821`, label `piperine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:28821` resolves `CHEBI:28821`
  `piperine` and the exported systematic synonym on the same term.
- A fresh PubChem lookup for CAS `94-62-2` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Piperine` exactly
  to `CHEBI:28821`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `94-62-2`, structured
  formula, SMILES, and InChI all describe piperine.
- The final SSSOM `other` values,
  `1-[(2E,4E)-5-(1,3-benzodioxol-5-yl)penta-2,4-dienoyl]piperidine|CAS:94-62-2`,
  are valid exact synonyms for the current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
