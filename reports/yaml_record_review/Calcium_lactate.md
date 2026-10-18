# `data/ingredients/mapped/Calcium_lactate.yaml`

## Verdict

Pass. The residual CultureMech surface form is exactly grounded to active
`FOODON:03413044` calcium lactate, has restored SSSOM-readable provenance, and
is synchronized across the aggregate, SSSOM, docs, and label index.

## Identity

- Reviewed record: `data/ingredients/mapped/Calcium_lactate.yaml`.
- Identifier and grounding: `identifier: FOODON:03413044`,
  `ontology_mapping.ontology_id: FOODON:03413044`,
  `ontology_label: calcium lactate`, `ontology_source: FOODON`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Direct OLS lookup for `FOODON:03413044` returns the active label
  `calcium lactate`.
- An OLS ChEBI search for `calcium lactate` found only
  `calcium lactate gluconate`, which is not the same ingredient.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml data/ingredients/mapped/3-hydroxybutyrate.yaml data/ingredients/mapped/Calcium_lactate.yaml data/ingredients/mapped/Calcium_malate.yaml data/ingredients/mapped/Calprotectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybenzoic_Acid.yaml data/ingredients/mapped/3-hydroxybutyrate.yaml data/ingredients/mapped/Calcium_lactate.yaml data/ingredients/mapped/Calcium_malate.yaml data/ingredients/mapped/Calprotectin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The 2026-08-30 residual-grounding history records one CultureMech mention in
  one recipe and the exact match against the FoodOn label.
- The 2026-09-06 curation event restored
  `culturemech:output/ingredient_occurrences.tsv` into
  `ontology_mapping.evidence`, which is the structured provenance read by the
  SSSOM builder.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Calcium_lactate` SSSOM row,
  matching aggregate/docs rows, and a unique label-index entry.

## Completeness

- The exact FoodOn identifier, 1/1 occurrence count, residual provenance,
  SSSOM row, aggregate copy, docs row, and label-index row are present.
- No synonyms, chemical properties, or roles are asserted, and no narrower
  CHEBI target was found by the bounded ChEBI search.

## Recommended Edits

- None for this record.
