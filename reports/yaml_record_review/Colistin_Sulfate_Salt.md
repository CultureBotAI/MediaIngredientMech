# `data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`

## Verdict

Needs curation; minor. This record is a rejected duplicate tombstone merged into
the active `Colistin_Sulfate` record at `NCIT:C386`; its final SSSOM row was
dropped and the old `CHEBI:37943` target no longer appears in the current YAML.
The only cleanup gaps are stale `ingredient_type` and provisional
`SELECTIVE_AGENT` fields left on the rejected zero-occurrence duplicate.

## Identity

- Reviewed record: `data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`.
- Identifier and grounding: `identifier: NCIT:C386`,
  `ontology_mapping.ontology_id: NCIT:C386`, `ontology_label: Colistin Sulfate`,
  `ontology_source: NCIT`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: REJECTED`.
- Live OLS lookup by `NCIT:C386` returns active `NCIT:C386` labelled
  `Colistin Sulfate` with exact synonyms including `Colistin Sulfate`.
- The September 2026 CAS-counterion curation history shows this duplicate was
  merged into the existing NCIT row because its old CAS-selected `CHEBI:37943`
  grounding denoted colistin without sulfate.
- `chemical_properties` is now empty, so no stale `CHEBI:37943` colistin
  structure is carried forward.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml data/ingredients/mapped/Colistin_Sulfate.yaml data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Colistin_Sulfate` and `Colistin_Sulfate_Salt` were intentionally skipped
  because they are grounded to NCIT, while this LinkML term-validation pass was
  limited to CHEBI records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found this rejected `NCIT:C386` tombstone, the active
  `MIM:Colistin_Sulfate` final SSSOM row, stale pre-merge row-review artifacts
  for the old `CHEBI:37943` grounding, and matching generated docs rows.
- Hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found the active `MIM:Colistin_Sulfate` row and no
  `MIM:Colistin_Sulfate_Salt` row, matching the tombstone curation note that
  SSSOM rows were dropped.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `NCIT:C386` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The rejected record has no synonyms, no source occurrences, no CAS RN, no
  structure values, and no final SSSOM `other` export.
- `SELECTIVE_AGENT` still has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked as a provisional
  name-pattern role despite this row now being a rejected duplicate.

## Completeness

- The tombstone pointer, empty chemistry block, lack of active SSSOM export, and
  `0/0` occurrence count are internally consistent.
- The cleanup gap is limited to stale fields left behind on the rejected
  duplicate and does not affect final SSSOM identity rows.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`, remove the
  residual `ingredient_type` and `physicochemical_roles` from the rejected
  duplicate.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
