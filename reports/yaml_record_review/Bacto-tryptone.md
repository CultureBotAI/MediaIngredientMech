# `data/ingredients/mapped/Bacto-tryptone.yaml`

## Verdict

Pass. The record was repaired away from a wrong detergent mapping and now
exact-maps the Difco/BD Bacto-tryptone label to `MICRO:0000182` `tryptone`;
the MICRO target, occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacto-tryptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000182` with
  `ontology_mapping.ontology_id: MICRO:0000182`,
  `ontology_label: tryptone`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `micro` resolves `MICRO:0000182` to `tryptone`.
- The current mapping deliberately uses MICRO's precise tryptone term rather
  than the broader `FOODON:03315719` hydrolyzed milk-protein parent, and the
  stale `CHEBI:78018` dodecylphosphocholine mapping plus wrong CAS RN were
  removed.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto-tryptone.yaml data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml data/ingredients/mapped/Bacto_Peptone.yaml data/ingredients/mapped/Bacto_Soytone.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `MICRO` is omitted from the OBO prefix set in `just validate-terms`; OLS
  exact search separately resolved `MICRO:0000182`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 526 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `MICRO:0000182` exactly, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` documents the older
  UNKNOWN_TERM row as a missing prefix-dispatch issue rather than a mapping
  problem.
- `mappings/complex_ingredients.tsv` groups Bacto Tryptone labels under the
  same tryptone family, matching the current MICRO upgrade.
- The 2026-08-27 occurrence refresh updated the CultureMech count to
  1583 media and 1600 total occurrences.

## Completeness

- The exact MICRO identifier, Bacto Tryptone aliases, `UNDEFINED_MIXTURE`
  ingredient type, provisional `PROTEIN_SOURCE` role, occurrence count, SSSOM
  row, and aggregate copy are populated.
- No CAS, formula, InChI, or SMILES should be asserted for this undefined
  enzymatic casein digest.

## Recommended Edits

- None.
