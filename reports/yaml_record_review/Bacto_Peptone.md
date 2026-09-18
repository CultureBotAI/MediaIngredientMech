# `data/ingredients/mapped/Bacto_Peptone.yaml`

## Verdict

Pass. The record exact-maps the Bacto/meat-peptone family to `MICRO:0000178`
`peptone`, preserves the curated catalog variants and related peptone labels,
and the SSSOM row plus aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacto_Peptone.yaml`.
- Identifier and grounding: `identifier: MICRO:0000178` with
  `ontology_mapping.ontology_id: MICRO:0000178`,
  `ontology_label: peptone`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `micro` resolves `MICRO:0000178` to `peptone`.
- The current mapping deliberately uses MICRO's precise peptone term rather
  than the broader `FOODON:03315718` hydrolyzed animal-protein parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto-tryptone.yaml data/ingredients/mapped/Bacto_Brain_Heart_Infusion.yaml data/ingredients/mapped/Bacto_Peptone.yaml data/ingredients/mapped/Bacto_Soytone.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Agar.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `MICRO` is omitted from the OBO prefix set in `just validate-terms`; OLS
  exact search separately resolved `MICRO:0000178`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 528 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `MICRO:0000178` exactly, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` documents the older
  UNKNOWN_TERM row as a missing prefix-dispatch issue rather than a mapping
  problem.
- `mappings/complex_ingredients.tsv` groups the Bacto, meat, Neopeptone, Oxoid,
  gelatin, universal, and fish peptone variants covered by this curated
  family.
- The 2026-08-27 occurrence refresh updated the CultureMech count to
  2251 media and 2255 total occurrences.

## Completeness

- The exact MICRO identifier, synonym set, `UNDEFINED_MIXTURE` ingredient type,
  provisional `PROTEIN_SOURCE` role, occurrence count, SSSOM row, and aggregate
  copy are populated.
- No CAS, formula, InChI, or SMILES should be asserted for this undefined
  peptone mixture.

## Recommended Edits

- None.
