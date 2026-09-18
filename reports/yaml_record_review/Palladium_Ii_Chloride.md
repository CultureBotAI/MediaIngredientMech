# `data/ingredients/mapped/Palladium_Ii_Chloride.yaml`

## Verdict

Pass. The CultureBotHT record maps exactly to active `CHEBI:53434`
palladium(II) chloride, and the final SSSOM keeps only same-salt synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Palladium_Ii_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:53434` with
  `ontology_mapping.ontology_id: CHEBI:53434`, label
  `palladium(II) chloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Palladium(II) chloride` resolves
  `CHEBI:53434` `palladium(II) chloride`.
- A local CAS checksum calculation confirmed that `7647-10-1` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Palladium_Ii_Chloride` exactly to `CHEBI:53434`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe palladium dichloride.
- `Palladium chloride` is a legitimate same-salt synonym for the `PdCl2`
  record, and `CAS:7647-10-1` matches the structured
  `chemical_properties.cas_rn`.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
