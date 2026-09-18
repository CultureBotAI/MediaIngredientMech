# `data/ingredients/mapped/Paclitaxel.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:45863` paclitaxel, and the final SSSOM keeps only same-substance
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Paclitaxel.yaml`.
- Identifier and grounding: `identifier: CHEBI:45863` with
  `ontology_mapping.ontology_id: CHEBI:45863`, label `paclitaxel`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Paclitaxel` resolves `CHEBI:45863`
  `paclitaxel`.
- A local CAS checksum calculation confirmed that `33069-62-4` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps `MIM:Paclitaxel`
  exactly to `CHEBI:45863`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the same paclitaxel molecule.
- The long `EXACT_SYNONYM` in YAML is the same chemical name exported in final
  SSSOM `other`.
- The final SSSOM also exports `CAS:33069-62-4`, which matches the structured
  `chemical_properties.cas_rn` value and has a valid check digit.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
