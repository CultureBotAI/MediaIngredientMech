# `data/ingredients/mapped/Calprotectin.yaml`

## Verdict

Needs curation, minor. The exact `NCIT:C105971` calprotectin mapping now
resolves in prefix-specific OLS validation and is synchronized in SSSOM/docs,
but the top-level notes still describe the pre-resolution unmapped state.

## Identity

- Reviewed record: `data/ingredients/mapped/Calprotectin.yaml`.
- Identifier and grounding: `identifier: NCIT:C105971`,
  `ontology_mapping.ontology_id: NCIT:C105971`,
  `ontology_label: Calprotectin`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `NCIT:C105971` returns the active NCIT label
  `Calprotectin`.

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

- The record was auto-upgraded from `UNMAPPED_0228` by label-normalized NCIT OLS
  matching, and the current direct OLS lookup resolves the CURIE and label
  exactly.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Calprotectin` SSSOM row,
  matching aggregate/docs rows, and a unique label-index entry.
- The same search found a stale `UNKNOWN_TERM` row in the old OAK/OLS review,
  but `mappings/ingredient_mappings_unknown_term_triage.tsv` already resolves
  it as missing validator-prefix coverage: prefix-specific EBI OLS lookup finds
  `NCIT:C105971`.

## Completeness

- The exact NCIT identifier, raw CultureBotHT surface form, NCIT mapping
  evidence, aggregate copy, SSSOM row, and docs row are present.
- `notes` still say the record had no CAS/CHEBI mapping and needed curator
  review. That was true at CultureBotHT import, but the structured mapping has
  since been resolved to NCIT.

## Recommended Edits

- In `data/ingredients/mapped/Calprotectin.yaml`, replace the stale top-level
  `notes` with NCIT-resolution wording or remove the note entirely.
- Regenerate the aggregate/docs products and prove the cleanup with strict
  validation and round-trip verification.
