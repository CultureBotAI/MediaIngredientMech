# `data/ingredients/mapped/Parabanic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:74661` parabanic acid, and the final SSSOM keeps only same-substance
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Parabanic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:74661` with
  `ontology_mapping.ontology_id: CHEBI:74661`, label `parabanic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Parabanic Acid` resolves `CHEBI:74661`
  `parabanic acid`.
- A local CAS checksum calculation confirmed that `120-89-8` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Parabanic_Acid`
  exactly to `CHEBI:74661`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the same parabanic acid molecule.
- The final SSSOM exports `imidazolidine-2,4,5-trione` and `CAS:120-89-8`,
  which are both legitimate same-substance labels.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
