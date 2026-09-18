# `data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml`

## Verdict

Pass. The over-conflated trypticase-peptone synonym was extracted into a
complete-media record, stem-matched to `MICRO:0000113` `tryptic soy broth`, and
the `(Difco)` duplicate was merged into the same record with no SSSOM drift.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml`.
- Identifier and grounding: `identifier: MICRO:0000113` with
  `ontology_mapping.ontology_id: MICRO:0000113`,
  `ontology_label: tryptic soy broth`, `ontology_source: MICRO`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- Prefix-specific OLS exact search in `micro` resolves `MICRO:0000113` to
  `tryptic soy broth`.
- The record denotes the complete Bacto Tryptic Soy Broth formulation, not
  trypticase peptone.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto_Tryptic_Soy_Agar_Difco.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Broth_Difco.yaml data/ingredients/mapped/Bafilomycin.yaml data/ingredients/mapped/Bafilomycin_B1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `MICRO` is omitted from the OBO prefix set in `just validate-terms`; OLS
  exact search separately resolved `MICRO:0000113`.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 530 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The 2026-04-19 curation event records why this was extracted from
  `Trypticase_Peptone.yaml`: Bacto Tryptic Soy Broth is a complete
  formulation, not a synonym of the base ingredient.
- The 2026-08-05 duplicate merge records the absorbed
  `Bacto Tryptic Soy Broth (Difco)` synonym and links it to the same
  `MICRO:0000113` identity.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` and the
  fresh OLS exact query both resolve `MICRO:0000113` to `tryptic soy broth`, so
  the old `UNKNOWN_TERM` MICRO review rows are validator-prefix coverage
  artifacts, not evidence of an invalid MICRO identifier.
- `mappings/other_cross_record_baseline.tsv` still carries an `UNREVIEWED`
  cross-record entry for the `(Difco)` raw label. The 2026-08-05 tombstone
  merge resolved that duplicate by merging
  `Bacto_Tryptic_Soy_Broth_Difco.yaml` into this live base record.

## Completeness

- The exact MICRO identifier, raw source synonyms, `UNDEFINED_MIXTURE`
  ingredient type, SSSOM row, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, or component list is required for this
  un-decomposed commercial medium.

## Recommended Edits

- None.
