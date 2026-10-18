# `data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml`

## Verdict

Needs curation; major issue. The vitamin-assay Casamino acids variant is
grounded to active `mesh:C017721`, and its CultureMech alias backfill is
represented, but `PROTEIN_SOURCE` is supported only by a provisional
name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml`.
- Identifier and grounding: `identifier: mesh:C017721`,
  `ontology_mapping.ontology_id: mesh:C017721`,
  `ontology_label: casamino acids`, `ontology_source: MESH`,
  `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Direct OLS lookup for `mesh:C017721` returns one active MeSH term labelled
  `casamino acids`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` records
  that prefix-specific OLS lookup resolves the exact MeSH CURIE, superseding
  the older generic `UNKNOWN_TERM` row-review result.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caryomycin.yaml data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable for the kgmicrobe placeholder sibling because the local
  kgmicrobe OAK adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
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
  found the active `MIM:Casamino_Acids_Vitamin_Assay` SSSOM row with
  `mesh:C017721`, the prefix-specific OLS validation row, and matching
  aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `mesh:C017721`, matching `occurrence_statistics` `0/0`.
- The BD-Difco and Difco vitamin-assay aliases added from CultureMech remain
  present as `CATALOG_VARIANT` synonyms.
- The `PROTEIN_SOURCE` role has only `COMPUTATIONAL_PREDICTION` evidence with
  a curator note that explicitly labels it a provisional name-pattern rule.

## Completeness

- The MeSH identifier, CultureBotHT raw synonym, CultureMech catalog-variant
  synonyms, 0/0 occurrence count, SSSOM row, aggregate copy, and docs row are
  populated.
- CAS and chemical-structure fields are correctly absent for this undefined
  protein hydrolysate mixture.

## Recommended Edits

- Major: either replace the provisional
  `nutritional_roles.PROTEIN_SOURCE` evidence in
  `data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml` with inspected
  evidence for the vitamin-assay Casamino acids scope, or remove the role,
  then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
