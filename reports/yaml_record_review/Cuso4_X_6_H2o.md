# `data/ingredients/mapped/Cuso4_X_6_H2o.yaml`

## Verdict

Needs curation; major. The current `CHEBI:91246` term resolves as copper(II)
sulfate hexahydrate and the 5/5 occurrence count matches CultureMech, but the
hydrate audit says the upstream source probably meant pentahydrate, and the
`TRACE_ELEMENT` role is still only computationally supported.

## Identity

- Reviewed record: `data/ingredients/mapped/Cuso4_X_6_H2o.yaml`.
- Current identifier and grounding: `identifier: CHEBI:91246`,
  `ontology_mapping.ontology_id: CHEBI:91246`,
  `ontology_label: copper(II) sulfate hexahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:91246` returns active `CHEBI:91246` labelled
  `copper(II) sulfate hexahydrate` with generalized formula `Cu.6H2O.O4S` and
  hydrate-specific InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:91246` as its primary
  identifier.

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

- The record's formula, InChI, SMILES, and final SSSOM `other` labels are all
  hexahydrate-specific and agree with live OLS for `CHEBI:91246`.
- `mappings/culturemech_recipe_membership.tsv` contains 5 distinct recipes and
  5 total occurrences for `CHEBI:91246`, matching
  `occurrence_statistics.media_count` and `.total_occurrences`.
- `reports/hydrate_grounding.tsv` reports `OK_HYDRATE_TERM` because the exact
  CHEBI hexahydrate term itself exists.
- Major: `mappings/hydrate_review.tsv` classifies `CuSO4 x 6 H2O` as
  `NEEDS_SOURCE` and `MEDIADIVE_UPSTREAM`: the row says the source probably
  meant `CuSO4 x 5 H2O`, identifies upstream MediaDive compound 218, and states
  that the graph-facing exact match to `CHEBI:91246` cannot hold unless the
  source confirms true hexahydrate usage.
- Major: `nutritional_roles.TRACE_ELEMENT` is still a
  `COMPUTATIONAL_PREDICTION` from a curated name pattern, with no direct
  source-backed `DATABASE_ENTRY`.

## Completeness

- The local record is structurally coherent after the CHEBI hexahydrate
  promotion, but its correctness still depends on an unresolved upstream
  hydrate decision.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the current SSSOM row, OAK/OLS
  review row, hydrate audit row, and generated indexes but no additional local
  ruling that supersedes the `NEEDS_SOURCE` hydrate audit.

## Recommended Edits

- Major: confirm MediaDive compound 218 against its source. If the label meant
  pentahydrate, correct the upstream source and refresh CultureMech/MIM so the
  5 occurrences attach to `CHEBI:31440` or an appropriate corrected record.
- Major: if the hexahydrate is confirmed, replace the provisional
  `TRACE_ELEMENT` evidence with a source-backed `DATABASE_ENTRY`.
- Regenerate synchronized products and rerun strict validation, hydrate QC,
  SSSOM QC, aggregate roundtrip, and `git diff --check`.
