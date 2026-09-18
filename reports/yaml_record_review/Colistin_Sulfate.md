# `data/ingredients/mapped/Colistin_Sulfate.yaml`

## Verdict

Needs curation; major. The active MicrobeDecoder record is intentionally
grounded to `NCIT:C386` Colistin Sulfate by curator ruling, live OLS resolves
that NCIT term, the MicrobeDecoder source count matches the residual trait
label, the final SSSOM row is narrow, and the `Colistin sulfate salt` duplicate
was correctly merged here. The material gap is that `SELECTIVE_AGENT` is only a
provisional computational name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Colistin_Sulfate.yaml`.
- Identifier and grounding: `identifier: NCIT:C386`,
  `ontology_mapping.ontology_id: NCIT:C386`, `ontology_label: Colistin Sulfate`,
  `ontology_source: NCIT`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `NCIT:C386` returns active `NCIT:C386` labelled
  `Colistin Sulfate` with exact synonyms including `Colistin Sulfate`.
- The August 2026 curator ruling explicitly says this NCIT grounding is final
  for this repository because live upstream `CHEBI:759883` was absent from the
  local semsql build, and it must not be restored without a new curator
  decision.
- The September 2026 CAS-counterion curation history shows the CAS-derived
  `Colistin sulfate salt` duplicate was merged into this NCIT row because the
  old `CHEBI:37943` xref denoted colistin without sulfate.

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
  `reports` found the active `MIM:Colistin_Sulfate` final SSSOM row, the
  rejected `Colistin_Sulfate_Salt` duplicate, stale pre-ruling ChEBI research
  rows, and matching generated docs rows.
- Hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found an active `MIM:Colistin_Sulfate` row grounded to `NCIT:C386` and no row
  for the rejected duplicate, matching the merge.
- Hidden/ignored-inclusive search of
  `data/custom/microbedecoder/unmapped_labels.tsv` found
  `kgmicrobe.trait:colistin_sulfate` in `BacDive_Antibiotic_resistance` with
  count 2, matching `occurrence_statistics.source_occurrences`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `NCIT:C386` rows,
  matching the explicit 0/0 CultureMech `occurrence_statistics`.
- The final SSSOM `other` column contains only `CAS:1264-72-8`, so the prior
  raw `Colistin sulfate salt` duplicate label is not exported as an extra
  synonym on this NCIT row.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked as a provisional
  name-pattern role.

## Completeness

- The NCIT identifier, curator ruling, duplicate merge, CAS RN, MicrobeDecoder
  occurrence count, SSSOM row, aggregate copy, and docs row are populated and
  agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Colistin_Sulfate.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for colistin
  sulfate as a selective agent in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
