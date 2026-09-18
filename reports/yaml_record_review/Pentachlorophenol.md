# `data/ingredients/mapped/Pentachlorophenol.yaml`

## Verdict

Pass. The CultureBotHT import maps exactly to active `CHEBI:17642`
pentachlorophenol, and the final SSSOM row exports only the structured CAS in
`other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Pentachlorophenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17642` with
  `ontology_mapping.ontology_id: CHEBI:17642`, label `pentachlorophenol`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2 CultureMech occurrences across 2 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:17642` resolves `CHEBI:17642`
  `pentachlorophenol`.
- The final SSSOM row was inspected directly and maps
  `MIM:Pentachlorophenol` exactly to `CHEBI:17642`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe pentachlorophenol.
- The final SSSOM row exports only `CAS:87-86-5`, which matches the structured
  CAS-RN.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
