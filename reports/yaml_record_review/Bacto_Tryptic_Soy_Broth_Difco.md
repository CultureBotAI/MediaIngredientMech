# `data/ingredients/mapped/Bacto_Tryptic_Soy_Broth_Difco.yaml`

## Verdict

Needs curation, minor. The record is correctly tombstoned as a duplicate of the
live `Bacto Tryptic Soy Broth` record at `MICRO:0000113`, but its top-level
`notes` still describe the obsolete imported-unmapped state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Bacto_Tryptic_Soy_Broth_Difco.yaml`.
- Identifier and grounding: `identifier: MICRO:0000113` with
  `ontology_mapping.ontology_id: MICRO:0000113`,
  `ontology_label: tryptic soy broth`, `ontology_source: MICRO`,
  `mapping_quality: LEXICAL_MATCH`, and `mapping_status: REJECTED`.
- Prefix-specific OLS exact search in `micro` resolves `MICRO:0000113` to
  `tryptic soy broth`.
- The 2026-08-05 `MERGED_INTO` event says this `(Difco)` spelling was merged
  into the live `MICRO:0000113` `Bacto Tryptic Soy Broth` record; no separate
  SSSOM row remains for the tombstone, as expected for a rejected duplicate.

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
  `data/curated/backups`, found the aggregate copy in
  `data/curated/mapped_ingredients.yaml` and no live SSSOM row for this
  rejected tombstone.
- The current raw synonym `Bacto Tryptic Soy Broth (Difco)` is the original
  `communitymech-unmapped` spelling that the live base record absorbed as
  `source: merged_record`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` and the
  fresh OLS exact query both resolve `MICRO:0000113` to `tryptic soy broth`, so
  the old `UNKNOWN_TERM` MICRO review rows are validator-prefix coverage
  artifacts, not evidence of an invalid MICRO identifier.
- The only stale claim is the top-level `notes` field: it still says this row
  has no CHEBI/NCIT match and needs curator review, even though the record was
  later stem-matched to MICRO and then rejected as a merged duplicate.

## Completeness

- The rejected status, merge curation event, zero transferred occurrences, raw
  source synonym, `UNDEFINED_MIXTURE` type, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, or component list is required for this
  tombstone.

## Recommended Edits

- Minor: update `notes` in
  `data/ingredients/mapped/Bacto_Tryptic_Soy_Broth_Difco.yaml` to describe the
  current rejected tombstone state and the live `Bacto Tryptic Soy Broth`
  representative, then run `just sync-curated`.
