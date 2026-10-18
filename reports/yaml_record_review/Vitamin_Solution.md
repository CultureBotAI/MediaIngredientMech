# `data/ingredients/mapped/Vitamin_Solution.yaml`

## Verdict

Needs curation. The exact `MICRO:0000460` vitamin solution identity, aggregate
row, occurrence count, and final SSSOM row pass, but the `VITAMIN_SOURCE` role
is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamin_Solution.yaml`.
- Identifier and grounding: `identifier: MICRO:0000460` with matching
  `ontology_mapping.ontology_id`, label `vitamin solution`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Synonyms: one raw `mim-queue` surface form, `Vitamin solution`.
- Occurrences: six CultureMech recipe occurrences across six media.
- Role: `VITAMIN_SOURCE` with provisional curated name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamin_K1` through `Vitamins-solution`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this `MICRO` row has no CHEBI/OBO adapter for that focused check.

## Evidence

- Fresh OLS4 exact-label search for `vitamin solution` in `MICRO` found the
  active `MICRO:0000460` class with label `vitamin solution`, supporting the
  exact mapping.
- The final SSSOM row correctly has
  `MIM:Vitamin_Solution skos:exactMatch MICRO:0000460`.
- The raw duplicate synonym is not exported into final SSSOM `other`.

## Issues

- Major: `nutritional_roles.VITAMIN_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the curated name-pattern
  rule is provisional and still needs review.

## Completeness

- The exact MICRO mapping, occurrence count, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

- Replace or remove this record's `VITAMIN_SOURCE` role; keep it only if a
  maintained source supports treating the stock solution as a vitamin source in
  the media records that use it.
- Rerun strict validation and SSSOM invariant validation after curation.
