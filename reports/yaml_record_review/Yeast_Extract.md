# `data/ingredients/mapped/Yeast_Extract.yaml`

## Verdict

Needs curation. The exact `FOODON:03315426` yeast extract identity, aggregate
row, and final exact SSSOM predicate pass, but final SSSOM exports many
vendor/catalog variants plus a truncated concentration string, and the
`PROTEIN_SOURCE` role is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Yeast_Extract.yaml`.
- Identifier and grounding: `identifier: FOODON:03315426` with matching
  `ontology_mapping.ontology_id`, label `yeast extract`, source `FOODON`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- CAS RN: `8013-01-2`.
- Synonyms: raw CultureMech and MicrobeDecoder strings, exact yeast-extract
  synonyms, related Fresh Baker labels, and many manual catalog variants.
- Occurrences: 7,697 total occurrences across 7,617 CultureMech media, plus 46
  MicrobeDecoder metabolite-utilization occurrences.
- Role: `PROTEIN_SOURCE` with provisional curated name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylotriose` through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this FoodOn row has no CHEBI/OBO adapter for that focused check.

## Evidence

- Fresh OLS4 exact-label search for `yeast extract` in FoodOn found active
  `FOODON:03315426` with label `yeast extract`.
- The final SSSOM row correctly has
  `MIM:Yeast_Extract skos:exactMatch FOODON:03315426`.
- The final SSSOM row filters the exact duplicate `Yeast Extract` and
  `yeast extract` strings but still exports raw and catalog-qualified labels.

## Issues

- Major: the final exact `FOODON:03315426` row exports many vendor/catalog
  labels as `other` synonyms, including BD, Difco, Oxoid, BBL, Nacalai Tesque,
  Hardy, Wako, and Flow product-specific strings.
- Major: the same final row exports the truncated concentration string
  `Yeast Extract (0.01 %`, which is not a complete or reusable synonym.
- Major: the same final row also exports source-decorated raw strings such as
  `Yeast extract(CAS: 8013-01-2)` and the duplicate Fresh Baker label with a
  non-ASCII curly apostrophe.
- Major: `nutritional_roles.PROTEIN_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the curated name-pattern
  rule is provisional and still needs review.

## Completeness

- The exact FoodOn mapping, occurrence count, aggregate copy, and final SSSOM
  predicate agree.
- The final synonym set needs to be reduced to true yeast-extract labels.

## Recommended Edits

- Remove or suppress raw CAS-decorated, concentration-truncated, non-ASCII
  duplicate, and vendor/catalog-specific labels from final SSSOM `other`.
- Replace or remove this record's `PROTEIN_SOURCE` role; keep it only if a
  maintained source supports yeast extract as a protein source in media.
- Rebuild SSSOM and rerun strict validation, SSSOM invariant validation, and the
  cross-record `other` synonym audit.
