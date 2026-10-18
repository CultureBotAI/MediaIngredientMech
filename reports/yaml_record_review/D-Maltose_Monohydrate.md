# `data/ingredients/mapped/D-Maltose_Monohydrate.yaml`

## Verdict

Needs curation, with major role and final-SSSOM synonym issues. The CAS primary
identifier, 20/20 CAS occurrence count, fixed maltose parent, and `CLOSE_MATCH`
hydrate regrade pass, but the active synonyms include anhydrous maltose labels
that leak into `other`, and the carbon/energy roles are only computationally
supported.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Maltose_Monohydrate.yaml`.
- Current identifier and grounding: `identifier: cas:6363-53-7`,
  `ontology_mapping.ontology_id: CHEBI:17306`,
  `ontology_label: maltose`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17306` returns active `CHEBI:17306` labelled
  `maltose`, the anhydrous close-match parent.
- A live exact CHEBI/NCIT label/synonym search for `D-Maltose monohydrate`
  returned no exact candidate.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:6363-53-7` as its
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Leucrose.yaml data/ingredients/mapped/D-Lysine.yaml data/ingredients/mapped/D-Maltose_Monohydrate.yaml data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml data/ingredients/mapped/D-Methionine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Lysine.yaml data/ingredients/mapped/D-Methionine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two CHEBI-primary exact records in this batch.
  This record, `D-Leucrose`, and `D-Mannose_6-phosphate_Sodium_Salt` were
  intentionally skipped because their primary identifiers are CAS registry
  CURIEs.
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

- The family-mismatch and #342 curation evidence correctly moved this record
  off the stale unrelated `CHEBI:233428` hit and now keeps `CHEBI:17306` only as
  a close anhydrous parent.
- `mappings/culturemech_recipe_membership.tsv` contains 20
  `cas:6363-53-7` rows, matching the record's refreshed 20/20
  `occurrence_statistics`.
- The final SSSOM emits both exact CAS and close maltose-parent rows.
- `alpha-D-glucopyranosyl-(1->4)-D-glucopyranose` and
  `alpha-D-glucopyranosyl-(1->4)-D-glucose` are anhydrous `CHEBI:17306`
  synonyms; publishing them in `other` for the monohydrate MIM subject erases
  the hydrate boundary.
- The `CARBON_SOURCE` and `ENERGY_SOURCE` facets are supported only by
  `COMPUTATIONAL_PREDICTION` and their own `curator_note` values call them
  provisional.

## Completeness

- No exact CHEBI or NCIT replacement for D-maltose monohydrate was found in
  live OLS, so the bounded identity fix is not a remapping.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found the expected parent, CAS-registry, and
  row-review surfaces and no curated exact ontology successor for this
  monohydrate.

## Recommended Edits

- In `data/ingredients/mapped/D-Maltose_Monohydrate.yaml`, remove or demote the
  two active anhydrous maltose synonyms so the final SSSOM no longer publishes
  them in `other`, then regenerate the final SSSOM.
- In the same record, either replace the computational `CARBON_SOURCE` and
  `ENERGY_SOURCE` evidence with direct source-backed media-role evidence, or
  remove those role facets; then rerun strict validation and the final SSSOM
  build.
