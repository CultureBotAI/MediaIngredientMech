# `data/ingredients/mapped/Sugar_Beet_Molasses.yaml`

## Verdict

Needs curation - major. `FOODON:00003412` resolves, but it denotes the sugar
beet root, not sugar beet molasses; FoodOn has a closer sugar-beet-molasses
class.

## Identity

- Reviewed record: `data/ingredients/mapped/Sugar_Beet_Molasses.yaml`.
- Identifier and grounding: `identifier: FOODON:00003412` with
  `ontology_mapping.ontology_id: FOODON:00003412`, label `sugar beet`, source
  `FOODON`, `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: 3 occurrences across 3 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sucrose` through `Sugars`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `FOODON:00003412` with label `sugar beet`
  and a definition for the primary root of a sugar beet plant.
- Fresh FoodOn search for `sugar beet molasses` resolves
  `FOODON:03543005`, whose label and definition are specific to molasses
  obtained from sugar beet.
- Major: the record exact-matches and publishes `FOODON:00003412` even though
  sugar beet molasses is not the sugar beet root.

## Completeness

- The aggregate row, 3/3 occurrence count, and final SSSOM row mirror the same
  wrong FOODON target.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the original stem-match promotion and the final
  SSSOM row, but no local curation that evaluated `FOODON:03543005`.

## Recommended Edits

- Major: reground `data/ingredients/mapped/Sugar_Beet_Molasses.yaml` from
  `FOODON:00003412` to a molasses-specific term such as `FOODON:03543005` if
  live FoodOn confirms that term fits the source labels, then synchronize the
  aggregate and rebuild the final SSSOM row.
