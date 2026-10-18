# `data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml`

## Verdict

Pass with minor issues. The named local stock-solution identity and final SSSOM
row pass, but older generated unmapped-category summaries still list the
pre-promotion label.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:hunters_trace_stock_solution` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:hunters_trace_stock_solution`, label
  `Hunter's Trace Stock Solution`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Source occurrences: one CultureMech occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hortesin.yaml data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml data/ingredients/mapped/Huperzine_A.yaml data/ingredients/mapped/Hyaluronic_Acid_Sodium_Salt_From_Streptococcus_Equi.yaml data/ingredients/mapped/Hydantoin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the three CHEBI-backed records in
  this batch and skipped for `Hunters_Trace_Stock_Solution` because its exact
  target is a local `kgmicrobe.ingredient` registry CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1448`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1448`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 returned zero hits for `Hunter's Trace Stock Solution`, matching the
  #114 decision to keep a local `kgmicrobe.ingredient` row for a named
  multi-component stock solution that no ontology should be expected to
  contain.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hunters_Trace_Stock_Solution` to
  `kgmicrobe.ingredient:hunters_trace_stock_solution` and exports no `other`
  synonym noise.
- A hidden and ignored-inclusive search over live per-record ingredients,
  `data/curated/unmapped_ingredients.yaml`, and the final SSSOM found no
  active unmapped duplicate of `Hunter's Trace Stock Solution`.
- Minor: the broader hidden and ignored-inclusive search over `data`, `src`,
  `tests`, `mappings`, `scripts`, `conf`, `docs`, and `.claude` found old
  generated category artifacts under `data/curated/unmapped_complex_media.yaml`
  and `data/ingredient_category_summaries/unmapped/complex_mixture.yaml` that
  still list the label as an unmapped complex-media entry.

## Completeness

- The local registry identifier, CultureMech occurrence count, aggregate copy,
  and final SSSOM row are present and consistent.
- The record itself has no unsupported roles or noisy final synonyms.

## Recommended Edits

- Minor: if the old unmapped category summaries are still maintained products,
  regenerate them from the current curated collections so
  `Hunter's Trace Stock Solution` no longer appears as an unmapped entry.
