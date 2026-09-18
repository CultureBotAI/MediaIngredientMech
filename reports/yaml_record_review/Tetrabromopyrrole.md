# `data/ingredients/mapped/Tetrabromopyrrole.yaml`

## Verdict

Needs curation - major. The local fallback row is synchronized, but live OLS now
resolves the exact MeSH supplementary concept that the curated note already
identified as the future promotion target.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetrabromopyrrole.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:tetrabromopyrrole` with the same
  `ontology_mapping.ontology_id`, label `Tetrabromopyrrole`, source
  `kgmicrobe.compound`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-production row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tertiomycin_B` through `Tetrachloroethene`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.compound` fallback row because that prefix is intentionally outside
  the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Tetrabromopyrrole` resolves
  `mesh:C000654730` with label `tetrabromopyrrole`.
- The structured mapping evidence already notes that upstream MeSH has
  `mesh:C000654730` and that the record should be promoted once the cached MeSH
  build can validate it.
- The final SSSOM has exactly one exact local registry row for
  `MIM:Tetrabromopyrrole`, points at
  `kgmicrobe.compound:tetrabromopyrrole`, names `kgm:compound`, and publishes
  no unsafe `other` synonyms.

## Completeness

- The local fallback identity, aggregate row, MicrobeDecoder source occurrence,
  and final SSSOM row agree mechanically.
- The fallback is stale as an external-ontology grounding because the exact
  upstream MeSH term exists and is recorded in the YAML as the intended
  promotion target.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder import,
  local promotion, aggregate, final SSSOM, and generated rows.

## Recommended Edits

- Major: promote `data/ingredients/mapped/Tetrabromopyrrole.yaml` from
  `kgmicrobe.compound:tetrabromopyrrole` to `mesh:C000654730` once the local
  MeSH adapter or its configured exceptions can validate that term.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` and docs so the
  final row points at MeSH rather than the temporary local compound fallback.
