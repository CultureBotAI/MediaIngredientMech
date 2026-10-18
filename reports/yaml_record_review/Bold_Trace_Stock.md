# `data/ingredients/mapped/Bold_Trace_Stock.yaml`

## Verdict

Needs curation, major. The local `kgmicrobe.ingredient:bold_trace_stock`
identity, stock-solution classification, registry SSSOM row, and mapped
aggregate copy agree, but the old `UNMAPPED_0065` `Bold Trace Stock` entry is
still present in the active unmapped complex-media collection.

## Identity

- Reviewed record: `data/ingredients/mapped/Bold_Trace_Stock.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:bold_trace_stock` with the same
  `ontology_mapping.ontology_id`, `ontology_label: Bold Trace Stock`,
  `ontology_source: kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: STOCK_SOLUTION`,
  `solution_type: TRACE_METAL_MIX`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Bold Trace Stock` returned 0 results across OLS,
  preserving the premise that this named trace-stock recipe needs a local
  registry identity rather than an ontology exact match.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bleomycin.yaml data/ingredients/mapped/Bleomycin_Sulfate.yaml data/ingredients/mapped/Blood.yaml data/ingredients/mapped/Bluensomycin.yaml data/ingredients/mapped/Bold_Trace_Stock.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation is intentionally skipped for this record because
  `kgmicrobe.ingredient` has no OBO adapter; the registry identity is covered
  by strict schema validation and the SSSOM invariant check.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the old no-exact-OLS audit row, the authoritative
  registry SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 615, and
  the mapped aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The same hidden/ignored-inclusive search also found stale active unmapped
  rows for `UNMAPPED_0065` in `data/curated/unmapped_complex_media.yaml` and
  `data/curated/UNMAPPED_COMPLEX_MEDIA.md`. No
  `data/ingredients/unmapped/Bold_Trace_Stock.yaml` per-record file exists.
- The local SSSOM row maps `MIM:Bold_Trace_Stock` to
  `kgmicrobe.ingredient:bold_trace_stock` with `skos:exactMatch`, which is the
  registry/identity shape required for a locally minted stock-solution ID.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The local stock identifier, raw CultureMech synonym, stock-solution and
  trace-metal classification, mapped SSSOM row, occurrence count, and mapped
  aggregate copy are populated.
- Major gap: the stale unmapped aggregate copy still publishes the same source
  label as `UNMAPPED_0065`, so mapped/unmapped category views disagree.

## Recommended Edits

- Major: remove the stale `UNMAPPED_0065` `Bold Trace Stock` row from the
  maintained unmapped complex-media collection, regenerate
  `data/curated/UNMAPPED_COMPLEX_MEDIA.md`, and rerun strict validation plus
  the round-trip/category checks that cover these curated collection files.
