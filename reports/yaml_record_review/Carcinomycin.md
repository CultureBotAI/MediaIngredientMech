# `data/ingredients/mapped/Carcinomycin.yaml`

## Verdict

Needs curation; major issue. The `kgmicrobe.compound:carcinomycin`
placeholder is intentionally retained after no-hit OLS review, but
`SELECTIVE_AGENT` is asserted from only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Carcinomycin.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:carcinomycin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:carcinomycin`,
  `ontology_label: Carcinomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct exact OLS search for `Carcinomycin` returned 0 hits, matching the
  local `UNKNOWN_TERM` review rows that found no exact candidate in ChEBI,
  MeSH, NCIT, MICRO, BTO, or FoodOn and found no normalized local duplicate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carboxymethyl_Cellulose`, then stopped on `Carcinomycin` because
  the local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carcinomycin` SSSOM row,
  the `UNKNOWN_TERM` placeholder audits, and the aggregate/docs rows for the
  expected local placeholder.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `kgmicrobe.compound:carcinomycin`, matching `occurrence_statistics`
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
  `data/ingredients/mapped/Carcinomycin.yaml` with inspected evidence for this
  kgmicrobe placeholder, or remove the role, then rerun strict validation,
  SSSOM QC, aggregate roundtrip, and `git diff --check`.
