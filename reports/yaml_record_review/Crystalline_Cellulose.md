# `data/ingredients/mapped/Crystalline_Cellulose.yaml`

## Verdict

Pass. The MicrobeDecoder label maps exactly to active `CHEBI:62968`
crystalline cellulose, its one BacDive source occurrence is retained separately
from CultureMech recipe counts, and the final SSSOM row has no unsafe `other`
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Crystalline_Cellulose.yaml`.
- Identifier and grounding: `identifier: CHEBI:62968`,
  `ontology_mapping.ontology_id: CHEBI:62968`,
  `ontology_label: crystalline cellulose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `match_level: EXACT` by equality of the record and ontology identifiers.
- Live OLS lookup by `CHEBI:62968` returns active `CHEBI:62968` labelled
  `crystalline cellulose`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:62968` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cu_No32_X_3_H2o.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `Cu_No32_X_3_H2o` was intentionally skipped because its local
  `kgmicrobe.compound` primary identifier and close ChEBI parent are outside
  this CHEBI-focused exact-label validation pass.
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
  `scripts`, `tests`, and `reports` found the active
  `MIM:Crystalline_Cellulose` final SSSOM row, generated docs rows, the
  MicrobeDecoder crystalline-cellulose candidate, and the auto-mapped review
  row that promoted the exact-label ChEBI match.
- The MicrobeDecoder source tables contain one
  `BacDive_Metabolite_utilization` source occurrence for `crystalline
  cellulose`, matching `source_occurrences[0].count: 1`.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:62968` rows,
  which agrees with the MicrobeDecoder-only `0/0` `occurrence_statistics`.
- The final SSSOM row has an empty `other` column.
- The record asserts no roles, components, supplied forms, or environment
  claims that require narrower supporting evidence.

## Completeness

- The ChEBI identifier, final SSSOM row, aggregate copy, source occurrence, and
  generated docs rows are populated and agree.
- `synonyms: []` is acceptable because no additional same-subject labels have
  been curated locally for this MicrobeDecoder import.

## Recommended Edits

- None.
