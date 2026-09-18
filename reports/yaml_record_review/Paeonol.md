# `data/ingredients/mapped/Paeonol.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:69581` Paeonol, and the final SSSOM keeps only the matching CAS synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Paeonol.yaml`.
- Identifier and grounding: `identifier: CHEBI:69581` with
  `ontology_mapping.ontology_id: CHEBI:69581`, label `Paeonol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Paeonol` resolves `CHEBI:69581` `Paeonol`.
- A local CAS checksum calculation confirmed that `552-41-0` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Paeonol` exactly to
  `CHEBI:69581`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the same paeonol molecule.
- The final SSSOM exports only `CAS:552-41-0` in `other`; that value matches
  the structured `chemical_properties.cas_rn`.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
