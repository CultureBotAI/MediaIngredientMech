# `data/ingredients/mapped/Horse_blood.yaml`

## Verdict

Pass. The CultureMech residual exact MICRO grounding, restored
claim-level evidence, source-occurrence count, empty synonym set, and final
SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Horse_blood.yaml`.
- Identifier and grounding: `identifier: MICRO:0001234` with
  `ontology_mapping.ontology_id: MICRO:0001234`, label `horse blood`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Source occurrences: 68 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Homovanillic_Acid.yaml data/ingredients/mapped/Homovanillyl_Alcohol.yaml data/ingredients/mapped/Hopanoid.yaml data/ingredients/mapped/Horse_Serum.yaml data/ingredients/mapped/Horse_blood.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the three CHEBI records in this
  batch and skipped for `Horse_blood` because its exact target is a MICRO
  CURIE outside the local CHEBI/OBO subset used for per-record label checks.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1438`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1438`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `MICRO:0001234` as the active MICRO class `horse blood`.
- The CultureMech source label exact-matches the MICRO label after
  case-normalization and does not add an unsupported defibrinated, serum,
  species, or catalog boundary.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Horse_blood` to `MICRO:0001234` and exports no `other` synonym noise.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and CultureMech residual
  grounding row.

## Completeness

- The active MICRO identifier, occurrence count, claim-level grounding
  evidence, aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
