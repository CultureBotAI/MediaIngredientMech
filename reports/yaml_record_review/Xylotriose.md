# `data/ingredients/mapped/Xylotriose.yaml`

## Verdict

Needs curation. The exact `CHEBI:149429` xylotriose identity, aggregate row,
and final SSSOM row pass, but the `CARBON_SOURCE` role is still a provisional
ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylotriose.yaml`.
- Identifier and grounding: `identifier: CHEBI:149429` with matching
  `ontology_mapping.ontology_id`, label `xylotriose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `47592-59-6`.
- Synonyms: none.
- Occurrences: zero.
- Role: `CARBON_SOURCE` with provisional ChEBI-ancestry evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylotriose` through `Yeast_Extract_Gluconate`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on this CHEBI-primary
  record exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:149429` returns active label `xylotriose` and a
  definition for trisaccharides composed of three xylose moieties.
- The final SSSOM row correctly has
  `MIM:Xylotriose skos:exactMatch CHEBI:149429`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the ChEBI-ancestry role
  was provisional and still needs review.

## Completeness

- The exact CHEBI mapping, aggregate copy, and final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports xylotriose as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
