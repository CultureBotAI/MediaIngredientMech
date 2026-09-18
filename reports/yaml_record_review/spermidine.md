# `data/ingredients/mapped/spermidine.yaml`

## Verdict

Pass. The PubChem CAS lookup maps the FEBA spermidine record to active
`CHEBI:16610`, and its CAS, formula, InChI, SMILES, exact synonyms, aggregate
copy, and final SSSOM row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/spermidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16610` with matching
  `ontology_mapping.ontology_id`, canonical label `spermidine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `124-20-9`.
- Structure: formula `C7H19N3` with populated InChI and SMILES.
- Synonyms: exact spermidine synonyms from kg-microbe.
- Occurrences: 14 FEBA occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 4-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `spermidine` in CHEBI returned the active
  `CHEBI:16610` label `spermidine`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:spermidine skos:exactMatch CHEBI:16610`.
- The final `other` field contains only exact spermidine synonyms and matching
  `CAS:124-20-9`.

## Issues

None.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  FEBA occurrence count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
