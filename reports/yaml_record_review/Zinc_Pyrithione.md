# `data/ingredients/mapped/Zinc_Pyrithione.yaml`

## Verdict

Pass. The CultureBotHT Hans80 antibiotic-panel record maps exactly to active
`CHEBI:32076` zinc pyrithione, and its CAS, formula, InChI, SMILES, exact
synonym, aggregate copy, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Zinc_Pyrithione.yaml`.
- Identifier and grounding: `identifier: CHEBI:32076` with matching
  `ontology_mapping.ontology_id`, canonical label `zinc pyrithione`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `13463-41-7`.
- Structure: formula `C10H8N2O2S2Zn` with populated InChI and SMILES.
- Synonyms: one ChEBI exact synonym,
  `bis[pyridine-2-thiolato-kappaS 1(oxide-kappaO)]zinc`.
- Occurrences: none recorded.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zinc pyrithione` in CHEBI returned the active
  `CHEBI:32076` label `zinc pyrithione`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:Zinc_Pyrithione skos:exactMatch CHEBI:32076`.
- The final `other` field contains only the reviewed ChEBI exact synonym and
  matching `CAS:13463-41-7`.
- The CultureBotHT `Hans80Anti` panel marker remains provenance on the
  grounding, not an inferred selective-agent role.

## Issues

None.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  aggregate copy, and final SSSOM row agree.
- No unsupported nutritional or physicochemical role is asserted.

## Recommended Edits

None.
