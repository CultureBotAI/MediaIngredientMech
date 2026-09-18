# `data/ingredients/mapped/Bg-11_Medium.yaml`

## Verdict

Needs curation, minor. The named-medium identity, `MICRO:0001348` target, SSSOM
row, occurrence count, and aggregate copy pass, but the active evidence note
says OLS exposes `BG-11 Medium` as an exact synonym while current OLS only
resolves the hyphenated label to canonical `BG 11 medium` by search.

## Identity

- Reviewed record: `data/ingredients/mapped/Bg-11_Medium.yaml`.
- Identifier and grounding: `identifier: MICRO:0001348` with
  `ontology_mapping.ontology_id: MICRO:0001348`,
  `ontology_label: BG 11 medium`, `ontology_source: MICRO`,
  `mapping_quality: SYNONYM_MATCH`, `ingredient_type: NAMED_MEDIUM`, and
  `mapping_status: MAPPED`.
- OLS resolves both `BG-11 Medium` and `BG 11 medium` searches to
  `MICRO:0001348`, whose definition describes a BG-11 culture medium used for
  cyanobacterial autotrophic growth.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bg-11_Medium.yaml data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml data/ingredients/mapped/Bicarbonate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bicarbonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three ChEBI-backed records in this batch.
- Engine A term validation is intentionally skipped for this `MICRO` record:
  the local justfile omits `MICRO` because the sqlite OBO adapter is an empty
  remote stub. The SSSOM validator previously passed with Rule B4 skipped
  because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 588, the
  `unmapped_ingredients_ols_exact_audit.tsv` row that kept this complex mixture
  out of automatic CHEBI/NCIT promotion, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The named-medium classification, MICRO mapping, SSSOM row, occurrence count,
  and aggregate copy are populated.
- Minor gap: the mapping evidence should say this was promoted by a manual
  normalized MICRO label match rather than an exact OLS synonym.
- No component list is required on this record because the identity is a named
  medium class, not a stock component list.

## Recommended Edits

- Minor: update the `data/ingredients/mapped/Bg-11_Medium.yaml`
  `ontology_mapping.evidence` note to describe the current normalized match to
  `MICRO:0001348` `BG 11 medium`, then run `just sync-curated` and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
