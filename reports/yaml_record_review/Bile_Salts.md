# `data/ingredients/mapped/Bile_Salts.yaml`

## Verdict

Needs curation, minor. The defined `CHEBI:22868` bile salt class, undefined
mixture classification, SSSOM row, occurrence count, and aggregate copy pass,
but top-level `notes` still describe the old unmapped review state.

## Identity

- Reviewed record: `data/ingredients/mapped/Bile_Salts.yaml`.
- Identifier and grounding: `identifier: CHEBI:22868` with
  `ontology_mapping.ontology_id: CHEBI:22868`,
  `ontology_label: bile salt`, `ontology_source: CHEBI`,
  `mapping_quality: LEXICAL_MATCH`, `ingredient_type: UNDEFINED_MIXTURE`, and
  `mapping_status: MAPPED`.
- OLS search for `Bile salts` now returns a newer exact-label
  `CHEBI:753636` class, but that term has no definition, synonyms, xrefs, or
  annotations. The current `CHEBI:22868` term is defined and lists `bile salts`
  as a related synonym, so this review does not treat the current target as
  wrong.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bicine.yaml data/ingredients/mapped/Bicine_Buffer.yaml data/ingredients/mapped/Bicyclomycin.yaml data/ingredients/mapped/Bile_Acid.yaml data/ingredients/mapped/Bile_Salts.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bicine.yaml data/ingredients/mapped/Bicine_Buffer.yaml data/ingredients/mapped/Bicyclomycin.yaml data/ingredients/mapped/Bile_Acid.yaml data/ingredients/mapped/Bile_Salts.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 594, the OAK/OLS confirmation row
  in `mappings/ingredient_mappings_row_review_manifest.tsv`, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_recipe_membership.tsv` contains 4 rows for
  `CHEBI:22868`, matching the record's refreshed 4/4 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The ChEBI class identifier, undefined-mixture classification, SSSOM row,
  occurrence statistics, and aggregate copy are populated.
- Minor gap: top-level `notes` still say no CAS-RN or CHEBI mapping was
  available and curator review was needed, even though the record is now
  mapped.

## Recommended Edits

- Minor: replace the stale import note in
  `data/ingredients/mapped/Bile_Salts.yaml` with a current note that records the
  accepted `CHEBI:22868` class mapping and the existence of definition-free
  `CHEBI:753636`, then run `just sync-curated` and focused strict/term
  validation.
