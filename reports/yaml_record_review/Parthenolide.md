# `data/ingredients/mapped/Parthenolide.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:7939` parthenolide, and the final SSSOM keeps only same-substance
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Parthenolide.yaml`.
- Identifier and grounding: `identifier: CHEBI:7939` with
  `ontology_mapping.ontology_id: CHEBI:7939`, label `parthenolide`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Parthenolide` resolves `CHEBI:7939`
  `parthenolide`.
- A local CAS checksum calculation confirmed that `20554-84-1` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps `MIM:Parthenolide`
  exactly to `CHEBI:7939`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the same parthenolide molecule.
- The long `EXACT_SYNONYM` in YAML is the same same-form name exported in final
  SSSOM `other`.
- The final SSSOM also exports `CAS:20554-84-1`, which matches the structured
  `chemical_properties.cas_rn` value and has a valid check digit.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
