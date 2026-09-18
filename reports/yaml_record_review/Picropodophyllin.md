# `data/ingredients/mapped/Picropodophyllin.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup maps to active `CHEBI:75251`
picropodophyllotoxin, `Picropodophyllin` is a synonym of that term, and the
final SSSOM row exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Picropodophyllin.yaml`.
- Identifier and grounding: `identifier: CHEBI:75251` with
  `ontology_mapping.ontology_id: CHEBI:75251`, label `picropodophyllotoxin`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `picropodophyllotoxin` resolves
  `CHEBI:75251` `picropodophyllotoxin`; `Picropodophyllin` and the exported
  systematic name are synonyms on that term.
- A fresh PubChem lookup for CAS `477-47-4` resolves to one compound CID.
- The final SSSOM row was inspected directly and maps `MIM:Picropodophyllin`
  exactly to `CHEBI:75251`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `477-47-4`, structured
  formula, SMILES, and InChI all describe picropodophyllotoxin/picropodophyllin.
- `CAS_RN_LOOKUP` accurately records the row's CAS-to-CHEBI grounding method,
  while the final own-identifier SSSOM predicate is correctly
  `skos:exactMatch`.
- The final SSSOM `other` values contain only the long systematic CHEBI
  synonym and `CAS:477-47-4`.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient CHEBI mapping.

## Recommended Edits

- None.
