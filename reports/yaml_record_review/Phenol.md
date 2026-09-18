# `data/ingredients/mapped/Phenol.yaml`

## Verdict

Needs curation; major. The CultureMech import maps exactly to active
`CHEBI:15882` phenol, but the `CARBON_SOURCE` role is only a provisional
in-session LLM assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:15882` with
  `ontology_mapping.ontology_id: CHEBI:15882`, label `phenol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 7 CultureMech occurrences across 7 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:15882` resolves `CHEBI:15882` `phenol`
  and returns the kg-microbe synonym set carried by this record.
- A local CAS checksum calculation confirmed that `108-95-2` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Phenol` exactly to
  `CHEBI:15882`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe phenol.
- The kg-microbe synonyms all appear on the OLS4 `CHEBI:15882` response, and
  final SSSOM exports only those synonyms plus `CAS:108-95-2`.
- Major: the `CARBON_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from provisional in-session Claude
  reasoning.

## Completeness

- The exact CHEBI mapping and final synonym surface are complete enough.
- Role evidence remains incomplete because no source-backed carbon-source
  assertion has been curated.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phenol.yaml`, either replace
  `nutritional_roles.CARBON_SOURCE` with cited source evidence that supports
  the carbon-source role for phenol, or remove the provisional role facet until
  source-backed role evidence is curated.
