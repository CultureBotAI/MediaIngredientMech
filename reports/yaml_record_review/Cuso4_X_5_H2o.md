# `data/ingredients/mapped/Cuso4_X_5_H2o.yaml`

## Verdict

Needs curation; major. The CHEBI pentahydrate identity, formula, CAS RN,
1486/1490 CultureMech count, hydrate audit row, and database-backed
`TRACE_ELEMENT` role pass, but the final SSSOM `other` field still exports the
malformed `CuSO .5H O` token as a synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Cuso4_X_5_H2o.yaml`.
- Current identifier and grounding: `identifier: CHEBI:31440`,
  `ontology_mapping.ontology_id: CHEBI:31440`,
  `ontology_label: copper(II) sulfate pentahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:31440` returns active `CHEBI:31440` labelled
  `copper(II) sulfate pentahydrate` with generalized formula
  `Cu.5H2O.O4S`, CAS `7758-99-8`, InChI, SMILES, and the
  `copper(2+) sulfate--water (1/5)` exact IUPAC synonym.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:31440` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI exact records in this batch.
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

- The record's `chemical_properties` match the live OLS formula, InChI, SMILES,
  and CAS xref for the pentahydrate.
- `mappings/hydrate_review.tsv` classifies `CuSO4 x 5 H2O` as
  `MATCHES_HYDRATE`, `CORRECT`, and `OK`, and `reports/hydrate_grounding.tsv`
  independently reports `OK_HYDRATE_TERM` for `CHEBI:31440`.
- `mappings/culturemech_recipe_membership.tsv` contains 1486 distinct recipes
  and 1490 total occurrences for `CHEBI:31440`, matching
  `occurrence_statistics.media_count` and `.total_occurrences`.
- The final SSSOM row publishes `MIM:Cuso4_X_5_H2o skos:exactMatch
  CHEBI:31440` and keeps only pentahydrate labels or the CAS RN, except for
  the exported `CuSO .5H O` surface form.
- Major: `CuSO .5H O` came from `sssom_other_backfill` and is graph-facing in
  the final SSSOM `other` column, but it is a malformed OCR-like fragment, not
  a real synonym for copper(II) sulfate pentahydrate. The asterisk spelling
  `CuSO4*5 H2O` still denotes the same pentahydrate and is a lower-priority raw
  separator variant.

## Completeness

- The active identity, CAS RN, hydrate-specific chemistry, CultureMech count,
  row-review status, and role evidence are internally consistent.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found no stale anhydrous-primary
  `CHEBI:23414` row for this record. The remaining actionable defect is the
  malformed exported synonym.

## Recommended Edits

- Major: remove `CuSO .5H O` from
  `data/ingredients/mapped/Cuso4_X_5_H2o.yaml` or teach the final SSSOM builder
  to suppress that exact `sssom_other_backfill` artifact.
- Regenerate synchronized products and rerun strict validation, LinkML term
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
