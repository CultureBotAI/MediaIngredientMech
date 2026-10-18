# `data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`

## Verdict

Pass. The over-conflated trypticase-peptone synonym was extracted into a
complete-media record, stem-matched to `MICRO:0000114` `tryptic soy agar`, and
the `(Difco)` duplicate was merged into the same record with no SSSOM drift.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`.
- Identifier and grounding: `identifier: MICRO:0000114` with
  `ontology_mapping.ontology_id: MICRO:0000114`,
  `ontology_label: tryptic soy agar`, `ontology_source: MICRO`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `micro` resolves `MICRO:0000114` to
  `tryptic soy agar`.
- The record denotes the complete Bacto Tryptic Soy Agar formulation, not
  trypticase peptone.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto-tryptone.yaml data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml data/ingredients/mapped/Bacto_Peptone.yaml data/ingredients/mapped/Bacto_Soytone.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `MICRO` is omitted from the OBO prefix set in `just validate-terms`; OLS
  exact search separately resolved `MICRO:0000114`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 529 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The 2026-04-19 curation event records why this was extracted from
  `Trypticase_Peptone.yaml`: Bacto Tryptic Soy Agar is a complete formulation,
  not a synonym of a base ingredient.
- The 2026-08-05 duplicate merge records the absorbed
  `Bacto Tryptic Soy Agar (Difco)` synonym and links it to the same
  `MICRO:0000114` identity.

## Completeness

- The exact MICRO identifier, raw source synonyms, `UNDEFINED_MIXTURE`
  ingredient type, SSSOM row, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, or component list is required for this
  un-decomposed commercial medium.

## Recommended Edits

- None.
