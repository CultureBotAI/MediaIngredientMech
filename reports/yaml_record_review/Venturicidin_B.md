# `data/ingredients/mapped/Venturicidin_B.yaml`

## Verdict

Pass. The MeSH label-exact identity, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Venturicidin_B.yaml`.
- Identifier and grounding: `identifier: mesh:C068160` with matching
  `ontology_mapping.ontology_id`, label `venturicidin B`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vanillyl_Alcohol` through `Veratric_Acid`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this MeSH-primary row is outside that focused check.

## Evidence

- Fresh OLS4 exact-label search in MeSH returns a single active `mesh:C068160`
  class labeled `venturicidin B`, matching the promoted placeholder identity.
- The final SSSOM row correctly has
  `MIM:Venturicidin_B skos:exactMatch mesh:C068160` with no unsupported
  synonyms in `other`.

## Issues

None.

## Completeness

- The MeSH exact mapping, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
