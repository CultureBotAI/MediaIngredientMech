# `data/ingredients/mapped/White_Wine.yaml`

## Verdict

Needs curation. The exact `NCIT:C84877` White Wine identity, aggregate row,
occurrence count, and final SSSOM row pass, but the record is classified as a
`SINGLE_INGREDIENT` even though white wine is a fermented beverage mixture.

## Identity

- Reviewed record: `data/ingredients/mapped/White_Wine.yaml`.
- Identifier and grounding: `identifier: NCIT:C84877` with matching
  `ontology_mapping.ontology_id`, label `White Wine`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: five CultureMech recipe occurrences across five media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wc_Trace_Elements_Solution` through
  `Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this NCIT row has no CHEBI/OBO adapter for that focused check.

## Evidence

- Fresh OLS4 exact-label search for `White Wine` in NCIT found one active NCIT
  hit, `NCIT:C84877`, with label `White Wine` and a definition as an alcoholic
  beverage made from fermented white grapes.
- The final SSSOM row correctly has
  `MIM:White_Wine skos:exactMatch NCIT:C84877`.

## Issues

- Major: `ingredient_type: SINGLE_INGREDIENT` is incompatible with the mapped
  NCIT identity for a fermented white-grape beverage. The schema reserves
  `SINGLE_INGREDIENT` for pure compounds or single ingredients, while white
  wine is a complex mixture.

## Completeness

- The exact NCIT mapping, occurrence count, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

- Reclassify this record as `UNDEFINED_MIXTURE` unless a more specific local
  stock-solution treatment is intended.
- Rerun strict validation and SSSOM invariant validation after curation.
