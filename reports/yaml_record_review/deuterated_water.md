# `data/ingredients/mapped/deuterated_water.yaml`

## Verdict

Pass. The PubChem CAS lookup maps the FEBA deuterated-water record to active
`CHEBI:41981` dideuterium oxide, and its CAS, formula, InChI, SMILES, exact
synonyms, aggregate copy, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/deuterated_water.yaml`.
- Identifier and grounding: `identifier: CHEBI:41981` with matching
  `ontology_mapping.ontology_id`, canonical label `dideuterium oxide`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7789-20-0`.
- Structure: formula `D2O` with populated InChI and SMILES.
- Synonyms: exact deuterated-water names and formulas from kg-microbe.
- Occurrences: one FEBA occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 4-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `dideuterium oxide` in CHEBI returned the active
  `CHEBI:41981` label `dideuterium oxide`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:deuterated_water skos:exactMatch CHEBI:41981`.
- The final `other` field contains only exact deuterated-water synonyms and
  matching `CAS:7789-20-0`.

## Issues

None.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  FEBA occurrence count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
