# `data/ingredients/mapped/Nutrient_Broth_No_2.yaml`

## Verdict

Pass. The record is an intentionally undefined nutrient-broth mixture mapped
to active `MICRO:0000082`, and the final SSSOM `other` values are curated
catalog variants of the same nutrient-broth subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Nutrient_Broth_No_2.yaml`.
- Identifier and grounding: `identifier: MICRO:0000082` with
  `ontology_mapping.ontology_id: MICRO:0000082`, label `nutrient broth`,
  source `MICRO`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: six CultureMech `CATALOG_VARIANT` aliases plus the original raw
  `Nutrient broth No. 2` surface.
- Occurrences: 53 CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- `scripts/_engine_a_obo_safe.sh` exited 1 for this file, which is the expected
  Engine A skip signal for a `MICRO:` term; `validate-products` and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` cover this prefix.

## Evidence

- A fresh prefix-specific EBI OLS4 search for `nutrient broth` in `micro`
  resolves a single exact `MICRO:0000082` class with label `nutrient broth`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` likewise
  records `MICRO:0000082` as `RESOLVED_EXACT_CURIE`, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the final
  `UNKNOWN_TERM` stamp as missing validator-prefix coverage rather than a bad
  mapping.
- The final SSSOM row maps `MIM:Nutrient_Broth_No_2` exactly to
  `MICRO:0000082`; its six pipe-delimited `other` tokens are the curated
  `CATALOG_VARIANT` aliases present in the YAML.
- No unsupported roles, components, supplied forms, or environmental contexts
  are asserted.

## Completeness

- The curated mixture identity, synonym payload, occurrence count, row-review
  triage, and final SSSOM row agree.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports`, `docs`, and `UNIFIED_INGREDIENT_MAPPING.tsv` found additional
  unresolved CultureMech labels such as `Bacto Nutrient Broth (Difco)`, but not
  a contradiction of this record's active exact `MICRO:0000082` mapping.

## Recommended Edits

- None for this record.
