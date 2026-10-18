# `data/ingredients/mapped/Phloretin.yaml`

## Verdict

Pass. The CultureBotHT CAS import maps exactly to active `CHEBI:17276`
phloretin, and the final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Phloretin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17276` with
  `ontology_mapping.ontology_id: CHEBI:17276`, label `phloretin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `phloretin` returns active `CHEBI:17276`
  `phloretin` and the exported systematic synonym on the same term.
- A fresh PubChem lookup for CAS `60-82-2` resolves to Phloretin with formula
  `C15H14O5`.
- The final SSSOM row was inspected directly and maps `MIM:Phloretin` exactly
  to `CHEBI:17276`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `60-82-2`, structured
  formula, SMILES, and InChI all describe phloretin.
- The final SSSOM `other` values,
  `3-(4-hydroxyphenyl)-1-(2,4,6-trihydroxyphenyl)propan-1-one|CAS:60-82-2`,
  are valid exact synonyms for the current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
