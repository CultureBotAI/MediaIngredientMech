# `data/ingredients/mapped/Bafilomycin.yaml`

## Verdict

Pass. The record intentionally retains a `kgmicrobe.compound:bafilomycin`
placeholder because the exact source label is family-level and the reviewed OLS
candidates were specific bafilomycin variants.

## Identity

- Reviewed record: `data/ingredients/mapped/Bafilomycin.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:bafilomycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:bafilomycin`,
  `ontology_label: Bafilomycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- An all-ontology OLS exact search for `Bafilomycin` in labels and synonyms
  returned 0 results. The archived 2026-05-06 placeholder search across
  `chebi`, `mesh`, `ncit`, `micro`, `bto`, and `foodon` likewise found no exact
  candidate.
- The record denotes the broad bafilomycin family label, not `Bafilomycin B1`
  or another specific bafilomycin variant.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto_Tryptic_Soy_Agar_Difco.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Broth_Difco.yaml data/ingredients/mapped/Bafilomycin.yaml data/ingredients/mapped/Bafilomycin_B1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.compound` is a registry prefix, not an OBO ontology adapter. The
  local SSSOM row is an own-identifier registry exact match.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative registry SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 531 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  records `NO_IDENTITY_PROMOTION`: `CHEBI:198365 Bafilomycin J`,
  `CHEBI:201422 Bafilomycin D`, and `CHEBI:205456 Bafilomycin H` were specific
  variants, while the source label was family-level.
- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  row 14 records that no exact label or synonym candidate was found for
  `Bafilomycin` in the 2026-05-06 EBI OLS placeholder search across
  `chebi`, `mesh`, `ncit`, `micro`, `bto`, and `foodon`.
- The provisional `SELECTIVE_AGENT` role is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with review
  recommended; it is not presented as literature-backed evidence.

## Completeness

- The kg-microbe registry identity, placeholder rationale, manual no-promotion
  review, SSSOM row, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, exact CHEBI identifier, or specific
  bafilomycin-variant synonym is required on this family-level placeholder.

## Recommended Edits

- None.
