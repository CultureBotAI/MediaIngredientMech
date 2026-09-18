# `data/ingredients/mapped/Physcion.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:38167` physcion,
and the final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Physcion.yaml`.
- Identifier and grounding: `identifier: CHEBI:38167` with
  `ontology_mapping.ontology_id: CHEBI:38167`, label `physcion`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:38167` resolves `CHEBI:38167`
  `physcion` and the exported systematic synonym on the same term.
- A fresh PubChem lookup for CAS `521-61-9` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Physcion` exactly
  to `CHEBI:38167`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `521-61-9`, structured
  formula, SMILES, and InChI all describe physcion.
- The final SSSOM `other` values,
  `1,8-dihydroxy-3-methoxy-6-methylanthracene-9,10-dione|CAS:521-61-9`,
  are valid exact synonyms for the current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
