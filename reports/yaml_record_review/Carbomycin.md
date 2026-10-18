# `data/ingredients/mapped/Carbomycin.yaml`

## Verdict

Pass. The record intentionally uses an active exact NCIT Carbomycin term
instead of the inaccessible local ChEBI candidate, and its MicrobeDecoder
source provenance, curator ruling, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carbomycin.yaml`.
- Identifier and grounding: `identifier: NCIT:C166659`,
  `ontology_mapping.ontology_id: NCIT:C166659`,
  `ontology_label: Carbomycin`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Direct OLS lookup for `NCIT:C166659` returns one active NCIT term labelled
  `Carbomycin`.
- The mapping history deliberately rejected local `CHEBI:756054` for this
  repository after a curator ruling: NCIT is exact, resolves in the local term
  stack, and must not be swapped back to the newer ChEBI ID without a new
  curator decision.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_Source_Solution.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_Source_Solution.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carbenicillin_Disodium_Salt`, `Carbomycin`, and
  `Carbon_Monoxide`, then stopped on `Carbon_Source_Solution` because the
  local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  review-report directories, found the active `MIM:Carbomycin` SSSOM row with
  `NCIT:C166659`, plus the stale deferred ChEBI proposal and local-audit rows
  that are explicitly superseded by the final NCIT curator ruling.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `NCIT:C166659`, matching `occurrence_statistics` `0/0`.
- The retained `source_occurrences` entry records one MicrobeDecoder
  `BacDive_Metabolite_production` import, and no synonym, role, component, or
  chemical-property claims require narrower evidence.

## Completeness

- The exact NCIT mapping, MicrobeDecoder occurrence provenance, curator ruling,
  SSSOM row, aggregate copy, and docs row are populated.
- Chemical structure slots are empty, appropriately for an NCIT mapping where
  this record does not carry a CAS-derived structural assertion.

## Recommended Edits

- None for this record.
