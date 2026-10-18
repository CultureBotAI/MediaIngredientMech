# `data/ingredients/mapped/LCFM_Carbon_Mix.yaml`

## Verdict

Pass. The local registry grounding, stock-solution classification, occurrence
count, empty final `other` field, and final SSSOM row are consistent for this
named LCFM carbon-source pre-mix.

## Identity

- Reviewed record: `data/ingredients/mapped/LCFM_Carbon_Mix.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:lcfm_carbon_mix` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:lcfm_carbon_mix`, label
  `LCFM Carbon mix`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Stock type: `solution_type: CARBON_SOURCE_MIX`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `L-valine` through `L_-tartaric_Acid`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-valine.yaml data/ingredients/mapped/LL-37.yaml data/ingredients/mapped/L_-tartaric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records. Engine A term validation was
  skipped for this local `kgmicrobe.ingredient` registry record because the
  prefix is outside the CHEBI/OBO prefix scope.

## Evidence

- The manual promotion describes LCFM Carbon mix as a named, recurring
  multi-component preparation used by two CultureBot media, with no exact
  CHEBI, NCIT, MeSH, FOODON, or ENVO class after normalized label and synonym
  search.
- Fresh exact OLS search across CHEBI, NCIT, MeSH, FOODON, and ENVO for
  `LCFM Carbon mix` found no class, and a PubChem name lookup returned no CID.
- The `STOCK_SOLUTION` and `CARBON_SOURCE_MIX` facets match the note that this
  is a carbon-source stock/pre-mix pending component-level recipe curation.
- The final SSSOM publishes one `skos:exactMatch` row to the local
  `kgmicrobe.ingredient` identifier with an empty `other` field.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the historical batch-validator warnings
  caused by the local registry prefix.

## Completeness

- The fallback identity, stock type, occurrence count, aggregate copy, and final
  SSSOM row are present and consistent.
- Missing component-level recipe curation is explicitly documented in the
  reviewed note and does not undermine the local identity row.

## Recommended Edits

- None.
