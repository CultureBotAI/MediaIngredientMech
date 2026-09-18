# `data/ingredients/mapped/Vulgamycin.yaml`

## Verdict

Needs curation. The exact MeSH `enterocin` synonym identity, aggregate row, and
final SSSOM row pass, but the `SELECTIVE_AGENT` role is still a provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Vulgamycin.yaml`.
- Identifier and grounding: `identifier: mesh:C012306` with matching
  `ontology_mapping.ontology_id`, label `enterocin`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: zero.
- Role: `SELECTIVE_AGENT` with provisional curated name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Voso4_X_N_H2o` through `Washed_agar`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary records in this
  batch; this MeSH row has no OBO adapter for that focused check.

## Evidence

- Fresh OLS4 exact search for `Vulgamycin` in MeSH returns one active hit,
  `mesh:C012306`, with label `enterocin` and related synonym `vulgamycin`.
- The final SSSOM row correctly has
  `MIM:Vulgamycin skos:exactMatch mesh:C012306`.
- The final SSSOM row has no `other` labels.

## Issues

- Major: `physicochemical_roles.SELECTIVE_AGENT` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the curated name-pattern
  rule is provisional and still needs review.

## Completeness

- The exact MeSH mapping, aggregate copy, and final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `physicochemical_roles.SELECTIVE_AGENT`; keep
  it only if a maintained source supports Vulgamycin as a selective agent in
  media.
- Rerun strict validation and SSSOM invariant validation after curation.
