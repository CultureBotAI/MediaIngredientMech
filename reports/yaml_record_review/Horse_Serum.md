# `data/ingredients/mapped/Horse_Serum.yaml`

## Verdict

Needs curation. The MICRO `horse serum` identity passes, but source-specific
CultureMech labels are active synonyms and all five are published in the final
SSSOM `other` column as if they were exact labels for generic horse serum.

## Identity

- Reviewed record: `data/ingredients/mapped/Horse_Serum.yaml`.
- Identifier and grounding: `identifier: MICRO:0001235` with
  `ontology_mapping.ontology_id: MICRO:0001235`, label `horse serum`, source
  `MICRO`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Source occurrences: 30 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Homovanillic_Acid.yaml data/ingredients/mapped/Homovanillyl_Alcohol.yaml data/ingredients/mapped/Hopanoid.yaml data/ingredients/mapped/Horse_Serum.yaml data/ingredients/mapped/Horse_blood.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the three CHEBI records in this
  batch and skipped for `Horse_Serum` because its exact target is a MICRO
  CURIE outside the local CHEBI/OBO subset used for per-record label checks.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1438`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1438`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `MICRO:0001235` as the active MICRO class `horse serum`, so the
  exact MICRO grounding is current.
- The row-review manifest already records the older `UNKNOWN_TERM` row as a
  missing-prefix validator coverage issue and instructs curators to keep the
  mapping.
- Major: the aliases `Horse Serum (Gibco)*`, `Horse Serum (RM1239)`,
  `Horse Serum (not inactivated)`, `Horse serum (Invitrogen)`, and
  `Horse serum (Oxoid)` were imported from raw CultureMech occurrence text
  because they folded onto the published label, but the record does not cite
  product-specific evidence showing that the vendor/catalog strings are true
  resolving aliases for this MIM subject. `Horse Serum (not inactivated)` is a
  supplied-state claim rather than an exact synonym for all horse serum.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Horse_Serum`
  to `MICRO:0001235`; its `other` column exports all five source-specific
  labels above.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and CultureMech residual
  ALIAS rows.

## Completeness

- The active MICRO identifier, occurrence count, aggregate copy, and final
  exact-match row are present and consistent.
- The record is incomplete until the CultureMech vendor/catalog/state strings
  are either curated as supported same-subject aliases or moved out of the
  exported synonym surface.

## Recommended Edits

- Major: remove `Horse Serum (Gibco)*`, `Horse Serum (RM1239)`,
  `Horse Serum (not inactivated)`, `Horse serum (Invitrogen)`, and
  `Horse serum (Oxoid)` from exported synonyms unless each raw occurrence is
  backed by product-specific evidence that it names the same generic MICRO
  subject; keep them as non-exported provenance or source labels if needed,
  then regenerate `mappings/ingredient_mappings.sssom.tsv` and rerun strict,
  round-trip, id-label, component, and SSSOM validation.
