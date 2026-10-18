# `data/ingredients/mapped/Bandamycin.yaml`

## Verdict

Pass. The record intentionally retains a `kgmicrobe.compound:bandamycin`
placeholder because no exact external ontology candidate or normalized local
duplicate was found.

## Identity

- Reviewed record: `data/ingredients/mapped/Bandamycin.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:bandamycin` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:bandamycin`,
  `ontology_label: Bandamycin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, and `mapping_status: MAPPED`.
- An all-ontology OLS exact search for `Bandamycin` in labels and synonyms
  returned 0 results. The archived 2026-05-06 placeholder search across
  `chebi`, `mesh`, `ncit`, `micro`, `bto`, and `foodon` likewise found no exact
  candidate.
- The record denotes the kg-microbe bandamycin placeholder imported from
  `BacDive_Metabolite_production`, not a resolved CHEBI or NCIT class.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Baicalein.yaml data/ingredients/mapped/Bakers_Yeast.yaml data/ingredients/mapped/Balhimycin.yaml data/ingredients/mapped/Bandamycin.yaml data/ingredients/mapped/Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml`:
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
  `mappings/ingredient_mappings.sssom.tsv` row 536 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_unknown_term_nohit_review.tsv` records
  `NO_LOCAL_DUPLICATE_NO_OLS_CANDIDATE` for this record, matching the 2026-05-09
  curation history note.
- Hidden/ignored-inclusive search found the source label in
  `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv`, both tied to a single
  `BacDive_Metabolite_production` occurrence.
- The provisional `SELECTIVE_AGENT` role is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with review
  recommended; it is not presented as literature-backed evidence.

## Completeness

- The kg-microbe registry identity, placeholder rationale, manual no-hit review,
  SSSOM row, and aggregate copy are populated.
- No CAS, formula, InChI, SMILES, exact CHEBI identifier, or external synonym is
  required while no exact external candidate is known.

## Recommended Edits

- None.
