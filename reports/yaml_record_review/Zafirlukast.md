# `data/ingredients/mapped/Zafirlukast.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:10100` zafirlukast, and its CAS, formula, InChI, SMILES, exact synonym,
aggregate copy, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Zafirlukast.yaml`.
- Identifier and grounding: `identifier: CHEBI:10100` with matching
  `ontology_mapping.ontology_id`, canonical label `zafirlukast`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `107753-78-6`.
- Structure: formula `C31H33N3O6S` with populated InChI and SMILES.
- Synonyms: one ChEBI systematic exact synonym,
  `cyclopentyl
  3-[2-methoxy-4-(2-methylphenylsulfonylcarbamoyl)benzyl]-1-methyl-1H-indol-5-ylcarbamate`.
- Occurrences: none recorded, which is coherent for a CultureBotHT-only
  chemical import.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zafirlukast` in CHEBI returned the active
  `CHEBI:10100` label `zafirlukast`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:Zafirlukast skos:exactMatch CHEBI:10100`.
- The final `other` field contains only the reviewed ChEBI systematic synonym
  and matching `CAS:107753-78-6`.

## Issues

None.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
