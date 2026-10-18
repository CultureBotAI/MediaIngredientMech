# `data/ingredients/mapped/Bicarbonate.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:17544` hydrogencarbonate identity,
restored CultureMech occurrence-table evidence, SSSOM row, occurrence count,
and aggregate copy pass, but the post-creation record is missing
`ingredient_type: SINGLE_INGREDIENT` and the evidence note overstates
`Bicarbonate` as an exact ChEBI synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Bicarbonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17544` with
  `ontology_mapping.ontology_id: CHEBI:17544`,
  `ontology_label: hydrogencarbonate`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- OLS returns current `CHEBI:17544` `hydrogencarbonate` for a
  `hydrogencarbonate` query, and `Bicarbonate` is present as a related ChEBI
  synonym on that term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bg-11_Medium.yaml data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml data/ingredients/mapped/Bicarbonate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bicarbonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three ChEBI-backed records in this batch.
- Engine A term validation is intentionally skipped for the two non-ChEBI
  records here: `MICRO` is omitted by the local justfile's OBO-safe adapter list
  and `kgmicrobe.ingredient` is a local registry prefix.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 590, the source row in
  `mappings/culturemech_residual_groundings.tsv`, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_residual_triage.tsv` still has buffered bicarbonate
  solution residuals, but the hidden/ignored-inclusive search did not find a
  second standalone `Bicarbonate` record under `data/ingredients`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, normalized synonym mapping, restored structured
  mapping evidence, SSSOM row, occurrence statistics, and aggregate copy are
  populated.
- Minor gap: this exact ChEBI oxoanion record has not been through the
  ingredient-type classifier and lacks `ingredient_type: SINGLE_INGREDIENT`.
- Minor gap: the evidence note says `Bicarbonate` was an exact ontology synonym,
  but current OLS exposes that surface form as a related synonym.

## Recommended Edits

- Minor: set `ingredient_type: SINGLE_INGREDIENT` and tighten the
  `ontology_mapping.evidence` note in
  `data/ingredients/mapped/Bicarbonate.yaml`; then run `just sync-curated` and
  focused strict/term validation.
