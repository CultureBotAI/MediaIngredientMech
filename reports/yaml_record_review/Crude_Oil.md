# `data/ingredients/mapped/Crude_Oil.yaml`

## Verdict

Pass. The MicrobeDecoder crude-oil label is grounded to active `ENVO:00002984`
petroleum through ENVO's registered `crude oil` synonym, the one BacDive source
occurrence is retained separately from CultureMech recipe counts, and the
published SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Crude_Oil.yaml`.
- Identifier and grounding: `identifier: ENVO:00002984`,
  `ontology_mapping.ontology_id: ENVO:00002984`, `ontology_label: petroleum`,
  `ontology_source: ENVO`, `mapping_quality: SYNONYM_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `ENVO:00002984` returns active `ENVO:00002984` labelled
  `petroleum` with `crude oil` as a related synonym.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `ENVO:00002984` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cresol_Red.yaml data/ingredients/mapped/Crinamine.yaml data/ingredients/mapped/Crotonic_Acid.yaml data/ingredients/mapped/Crude_Oil.yaml data/ingredients/mapped/Cryptotanshinone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cresol_Red.yaml data/ingredients/mapped/Crinamine.yaml data/ingredients/mapped/Crotonic_Acid.yaml data/ingredients/mapped/Cryptotanshinone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch. `Crude_Oil` was
  intentionally skipped because its ENVO primary identifier is outside this
  CHEBI-focused exact-label validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the active `MIM:Crude_Oil` final
  SSSOM row, generated docs rows, the MicrobeDecoder `crude oil` candidate,
  and `record_research_validation.tsv` rows documenting that the earlier ENVO
  disagreement was resolved in favor of `ENVO:00002984`.
- The MicrobeDecoder source tables contain one `BacDive_Metabolite_utilization`
  source occurrence for `crude oil`, matching
  `source_occurrences[0].count: 1`.
- The final SSSOM row correctly maps `SYNONYM_MATCH` to `skos:exactMatch` and
  has an empty `other` column.
- The record asserts no roles, components, supplied forms, or environment
  claims that require narrower supporting evidence.

## Completeness

- The ENVO identifier, final SSSOM row, aggregate copy, source occurrence, and
  generated docs rows are populated and agree.
- Keeping `total_occurrences: 0` and `media_count: 0` is consistent with the
  absence of CultureMech recipe-membership rows for this MicrobeDecoder-only
  source label.

## Recommended Edits

- None.
