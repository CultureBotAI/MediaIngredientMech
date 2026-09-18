# `data/ingredients/mapped/Caryomycin.yaml`

## Verdict

Needs curation; major issue. The `kgmicrobe.compound:caryomycin`
placeholder is intentionally retained after no-hit OLS review, but
`SELECTIVE_AGENT` is asserted from only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Caryomycin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:caryomycin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:caryomycin`,
  `ontology_label: Caryomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct exact OLS search for `Caryomycin` returned 0 hits, matching the
  local `UNKNOWN_TERM` review rows that found no external exact candidate and
  retained the kg-microbe placeholder.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caryomycin.yaml data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable for this record because the local kgmicrobe OAK adapter has no
  `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology sibling records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review-report directories,
  found the active `MIM:Caryomycin` SSSOM row, the `UNKNOWN_TERM` placeholder
  audits, and the aggregate/docs rows for the expected local placeholder.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `kgmicrobe.compound:caryomycin`, matching `occurrence_statistics`
  `0/0`.
- The `SELECTIVE_AGENT` role has only `COMPUTATIONAL_PREDICTION` evidence with
  a curator note that explicitly labels it a provisional name-pattern rule.

## Completeness

- The placeholder identity, no-hit review note, 0/0 occurrence count, SSSOM
  row, aggregate copy, and docs row are populated.
- Chemical properties are correctly absent for a no-hit local placeholder.

## Recommended Edits

- Major: either replace the provisional
  `physicochemical_roles.SELECTIVE_AGENT` evidence in
  `data/ingredients/mapped/Caryomycin.yaml` with inspected evidence for this
  kgmicrobe placeholder, or remove the role, then rerun strict validation,
  SSSOM QC, aggregate roundtrip, and `git diff --check`.
