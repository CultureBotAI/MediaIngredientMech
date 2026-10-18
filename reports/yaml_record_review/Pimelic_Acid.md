# `data/ingredients/mapped/Pimelic_Acid.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:30531` pimelic
acid, and the final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Pimelic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30531` with
  `ontology_mapping.ontology_id: CHEBI:30531`, label `pimelic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:30531` resolves `CHEBI:30531`
  `pimelic acid` and the exported exact synonym on the same term.
- A fresh PubChem lookup for CAS `111-16-0` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Pimelic_Acid`
  exactly to `CHEBI:30531`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `111-16-0`, structured
  formula, SMILES, and InChI all describe pimelic acid.
- The final SSSOM `other` values, `heptanedioic acid|CAS:111-16-0`, are valid
  exact synonyms for the current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
