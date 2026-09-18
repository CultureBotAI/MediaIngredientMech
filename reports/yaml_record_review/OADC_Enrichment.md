# `data/ingredients/mapped/OADC_Enrichment.yaml`

## Verdict

Pass. OADC Enrichment is intentionally preserved as a local stock-solution
registry ingredient, with no lossy parent ontology mapping and a curated Difco
catalog variant in the final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/OADC_Enrichment.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:oadc_enrichment`
  with `ontology_mapping.ontology_id: kgmicrobe.ingredient:oadc_enrichment`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: OTHER`.
- Synonyms: original `OADC Enrichment` plus `OADC Enrichment (Difco)` as a
  CultureMech `CATALOG_VARIANT`.
- Occurrences: two CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- `scripts/_engine_a_obo_safe.sh` exited 1 for this file, which is the expected
  Engine A skip signal for a local `kgmicrobe.ingredient:` identifier.

## Evidence

- The `#288` promotion documents the identity decision: OADC Enrichment is a
  named multi-component preparation with no exact CHEBI, NCIT, MeSH, FOODON,
  or ENVO term, so it uses the stock-solution fallback registry pattern.
- The final SSSOM row maps `MIM:OADC_Enrichment` exactly to
  `kgmicrobe.ingredient:oadc_enrichment`, keeps `OADC Enrichment (Difco)` as
  the only `other` token, and carries the manual `issue_288_stock_solutions`
  promotion stamp.
- No components are asserted, so there is no partial composition to
  cross-check or over-scoped component evidence to reject.
- No unsupported roles, supplied forms, or environmental contexts are asserted.

## Completeness

- The local registry identity, stock-solution classification, catalog-variant
  synonym, occurrence count, and final SSSOM row agree.
- The hidden and ignored-inclusive search over `data/ingredients`,
  `data/curated`, `mappings`, `reports`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the same OADC identities and no newer
  curated decomposition that supersedes the fallback registry row.

## Recommended Edits

- None.
