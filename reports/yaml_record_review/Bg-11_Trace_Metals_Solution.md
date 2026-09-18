# `data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml`

## Verdict

Pass. The local `kgmicrobe.ingredient:bg-11_trace_metals_solution` registry
identity, stock-solution classification, absence of an external OBO target,
SSSOM row, occurrence count, and aggregate copy all agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:bg-11_trace_metals_solution` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:bg-11_trace_metals_solution`,
  `ontology_label: BG-11 Trace Metals Solution`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`,
  `ingredient_type: STOCK_SOLUTION`, `solution_type: TRACE_METAL_MIX`, and
  `mapping_status: MAPPED`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bg-11_Medium.yaml data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml data/ingredients/mapped/Bicarbonate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bicarbonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three ChEBI-backed records in this batch.
- Engine A term validation is intentionally skipped for this local registry
  record. The SSSOM validator previously passed with Rule B4 skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact registry SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 589, the corresponding unknown
  local-term validation status, the case alias for the historical
  `MIM:BG-11_Trace_Metals_Solution` subject, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/unmapped_ingredients_ols_exact_audit.tsv` found no exact OLS hit
  for the original complex-mixture label, and a live OLS search for
  `BG-11 Trace Metals Solution` returned no class hits.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The local registry identifier, stock-solution classification, trace-metal
  mix subtype, SSSOM row, occurrence count, alias row, and aggregate copy are
  populated.
- No CHEBI, NCIT, MeSH, FOODON, or ENVO parent should be forced for this named
  lab preparation, and the record correctly avoids mapping the whole stock to
  any single component.

## Recommended Edits

- None.
