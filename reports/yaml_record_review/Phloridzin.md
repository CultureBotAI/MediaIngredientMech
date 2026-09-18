# `data/ingredients/mapped/Phloridzin.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup maps to active `CHEBI:8113` phlorizin, the
`Phloridzin` spelling is a CHEBI synonym of that term, and the final SSSOM row
exports only real exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Phloridzin.yaml`.
- Identifier and grounding: `identifier: CHEBI:8113` with
  `ontology_mapping.ontology_id: CHEBI:8113`, label `phlorizin`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:8113` resolves `CHEBI:8113` `phlorizin`;
  `Phloridzin` and the exported systematic name are synonyms on that term.
- A fresh PubChem lookup for CAS `60-81-1` resolves to Phloridzin with formula
  `C21H24O10`.
- The final SSSOM row was inspected directly and maps `MIM:Phloridzin` exactly
  to `CHEBI:8113`.

## Evidence

- The CHEBI primary identifier, mapping target, CAS `60-81-1`, structured
  formula, SMILES, and InChI all describe phlorizin/phloridzin.
- `CAS_RN_LOOKUP` accurately records the row's CAS-to-CHEBI grounding method,
  while the final own-identifier SSSOM predicate is correctly
  `skos:exactMatch`.
- The final SSSOM `other` values,
  `3,5-dihydroxy-2-[3-(4-hydroxyphenyl)propanoyl]phenyl beta-D-glucopyranoside|CAS:60-81-1`,
  are valid exact synonyms for the current target.
- The record carries no role, parent, component, or environment claims.

## Completeness

- No consequential gap was found for this single-ingredient CHEBI mapping.

## Recommended Edits

- None.
