# `data/ingredients/mapped/Paraquat_Dichloride.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record maps exactly to active
`CHEBI:28786` paraquat dichloride, and the final SSSOM keeps same-form labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Paraquat_Dichloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:28786` with
  `ontology_mapping.ontology_id: CHEBI:28786`, label `paraquat dichloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Paraquat dichloride` resolves `CHEBI:28786`
  `paraquat dichloride`.
- A local CAS checksum calculation confirmed that `1910-42-5` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Paraquat_Dichloride` exactly to `CHEBI:28786`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe the dichloride salt of the paraquat dication.
- The final SSSOM exports the curated CultureBotHT surface `Paraquat`, the
  expanded exact synonym, and `CAS:1910-42-5`, which matches the structured
  CAS-RN.
- There are no asserted role facets requiring additional source support.

## Completeness

- No consequential gap was found for this single-ingredient exact CHEBI
  mapping.

## Recommended Edits

- None.
