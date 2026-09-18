# `data/ingredients/mapped/Xyloglucan_From_Tamarind.yaml`

## Verdict

Needs curation. The CAS fallback identity, aggregate row, and final exact SSSOM
row pass, but the `CARBON_SOURCE` role is still a provisional name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xyloglucan_From_Tamarind.yaml`.
- Identifier and grounding: `identifier: cas:37294-28-3` with matching
  `ontology_mapping.ontology_id`, label `Xyloglucan from tamarind`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `37294-28-3`.
- Synonyms: none.
- Occurrences: zero.
- Role: `CARBON_SOURCE` with provisional curated name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylitol` through `Xylotetraose`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this CAS-primary fallback row has no OBO adapter for that focused
  check.

## Evidence

- Fresh OLS4 exact search for CAS `37294-28-3` returned no hits, so no active
  OLS term currently supersedes the CAS fallback.
- The final SSSOM row correctly has
  `MIM:Xyloglucan_From_Tamarind skos:exactMatch cas:37294-28-3`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the curated name-pattern
  rule is provisional and still needs review.

## Completeness

- The exact CAS identity, aggregate copy, and final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports tamarind xyloglucan as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
