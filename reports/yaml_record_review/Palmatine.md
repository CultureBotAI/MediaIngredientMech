# `data/ingredients/mapped/Palmatine.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:16096` palmatine, and the final SSSOM keeps only same-substance
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Palmatine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16096` with
  `ontology_mapping.ontology_id: CHEBI:16096`, label `palmatine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Palmatine` resolves `CHEBI:16096`
  `palmatine`.
- A local CAS checksum calculation confirmed that `3486-67-7` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Palmatine` exactly
  to `CHEBI:16096`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the same palmatine cation.
- The long `EXACT_SYNONYM` in YAML is the same same-form name exported in final
  SSSOM `other`.
- The final SSSOM also exports `CAS:3486-67-7`, which matches the structured
  `chemical_properties.cas_rn` value and has a valid check digit.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
