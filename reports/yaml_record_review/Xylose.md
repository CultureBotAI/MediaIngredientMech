# `data/ingredients/mapped/Xylose.yaml`

## Verdict

Needs curation. The exact `CHEBI:18222` xylose identity, source-backed
`CARBON_SOURCE` role, aggregate row, and final SSSOM row pass, but the
`ENERGY_SOURCE` role is still a provisional computational inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylose.yaml`.
- Identifier and grounding: `identifier: CHEBI:18222` with matching
  `ontology_mapping.ontology_id`, label `xylose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `C5H10O5`.
- Synonyms: raw CultureMech role strings plus three clean kg-microbe synonyms.
- Occurrences: 23 CultureMech recipe occurrences across 23 media.
- Roles: `CARBON_SOURCE` imported from CultureMech original role text and
  provisional `ENERGY_SOURCE`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylitol` through `Xylotetraose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:18222` returns active label `xylose`, formula
  `C5H10O5`, and synonym coverage for the clean kg-microbe synonyms.
- The `CARBON_SOURCE` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Carbon Source`.
- The final SSSOM row correctly has
  `MIM:Xylose skos:exactMatch CHEBI:18222`.
- The raw `Role:`/`Properties:` CultureMech strings are filtered from final
  SSSOM `other`, as intended.

## Issues

- Major: `nutritional_roles.ENERGY_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the role was provisional
  and still needs review.

## Completeness

- The exact CHEBI mapping, occurrence count, source-backed carbon-source role,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `ENERGY_SOURCE` role; keep it only if a
  maintained source supports xylose as an energy source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
