# `data/ingredients/mapped/Cholinium_Lysinate.yaml`

## Verdict

Pass. The promoted MeSH identity resolves to active `mesh:C000655964`
`cholinium lysinate`, the absorbed `Choline Lysine` duplicate is retained as an
exact synonym, and the zero occurrence count, SSSOM row, and aggregate copy
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cholinium_Lysinate.yaml`.
- Identifier and grounding: `identifier: mesh:C000655964`,
  `ontology_mapping.ontology_id: mesh:C000655964`,
  `ontology_label: cholinium lysinate`, `ontology_source: MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS search resolves exactly one `mesh:C000655964` hit labelled
  `cholinium lysinate`; direct NLM MeSH lookup of `C000655964` reports an
  active SCR chemical with the same label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml data/ingredients/mapped/Cholinium_Lysinate.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  `mesh:C000655964` is outside Engine A term-validation scope. Repository
  row-review triage also classifies the old `UNKNOWN_TERM` as missing prefix
  coverage, not as a bad MeSH CURIE. A narrowed run over the three
  CHEBI-scoped records in this batch passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cholinium_Lysinate` SSSOM row, the
  external-prefix OLS validation row resolving `mesh:C000655964`, the
  expected unknown-term triage row, and matching aggregate/docs rows.
- The absorbed duplicate label `Choline Lysine` appears in the SSSOM `other`
  column and the docs label index as a synonym of the same MeSH identity.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `mesh:C000655964`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, chemical-property, or environment
  claims.

## Completeness

- The exact MeSH identifier, absorbed source label, zero occurrence count,
  SSSOM row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
