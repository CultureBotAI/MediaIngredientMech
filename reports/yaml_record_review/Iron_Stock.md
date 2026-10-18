# `data/ingredients/mapped/Iron_Stock.yaml`

## Verdict

Pass. `Iron Stock` is represented as a local stock-solution registry term after
manual `#114` review found no public ontology class that denotes the recurring
named preparation, and the final SSSOM row points at that fallback CURIE.

## Identity

- Reviewed record: `data/ingredients/mapped/Iron_Stock.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:iron_stock` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:iron_stock`, label
  `Iron Stock`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Stock-solution classification: `solution_type: OTHER`, with a curator note
  that this is a named iron stock solution pending component-level recipe
  curation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Iron_Powder.yaml data/ingredients/mapped/Iron_Stock.yaml data/ingredients/mapped/Isepamicin.yaml data/ingredients/mapped/Isobutyl_Alcohol.yaml data/ingredients/mapped/Isobutyramide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI records.
  `Iron_Stock` was outside adapter scope because its primary identifier is a
  local `kgmicrobe.ingredient` CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1645`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1645`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The `#114` curator evidence records a search across ChEBI, NCIT, MeSH,
  FOODON, and ENVO, and classifies `Iron Stock` as a one-medium named
  multi-component lab preparation rather than a single compound.
- A fresh exact OLS4 search for `Iron Stock` across ChEBI, NCIT, MeSH, FOODON,
  and ENVO returned zero hits, supporting continued use of the local fallback
  registry term.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Iron_Stock` to
  `kgmicrobe.ingredient:iron_stock` with no broad ChEBI parent and empty
  `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, the placeholder promotion
  event from `UNMAPPED_0074`, and no newer exact public ontology mapping for
  the named stock.

## Completeness

- The local fallback identifier, stock-solution type, aggregate copy, and final
  SSSOM row are present and consistent.
- The record intentionally has no CAS RN, structure fields, or single-compound
  ChEBI parent.

## Recommended Edits

- None.
