# `data/ingredients/mapped/Bacteriocin_Isk_1.yaml`

## Verdict

Pass. The record intentionally retains the local
`kgmicrobe.compound:bacteriocin_isk_1` placeholder because the close
`CHEBI:204272` `Nukacin ISK-1` candidate is not proven to be exact for the
broader Bacteriocin ISK-1 source label, and the synonyms, caution note, SSSOM
row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacteriocin_Isk_1.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:bacteriocin_isk_1` with
  `ontology_mapping.ontology_id: kgmicrobe.compound:bacteriocin_isk_1`,
  `ontology_label: Bacteriocin Isk 1`,
  `ontology_source: kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, and
  `mapping_status: MAPPED`.
- OLS4 exact search across `CHEBI`, `MESH`, and `NCIT` returned no exact
  `Bacteriocin Isk 1` label.
- OLS resolves `CHEBI:204272` to non-obsolete `Nukacin ISK-1`, a related but
  more specific candidate that the current record deliberately does not use as
  an exact identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacitracin.yaml data/ingredients/mapped/Bacl2.yaml data/ingredients/mapped/Bacl2_X_2_H2o.yaml data/ingredients/mapped/Bacteriochlorophyll_A.yaml data/ingredients/mapped/Bacteriocin_Isk_1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation was intentionally skipped for this record because
  `kgmicrobe.compound` is a non-OBO prefix.
- OLS4 lookup for `Bacteriocin Isk 1` found no exact external term; OLS4
  lookup for `CHEBI:204272` confirmed that the candidate is specifically
  `Nukacin ISK-1`.
- DOI handle lookups for `10.5109/24265` and `10.1128/AAC.01623-08` both
  resolved.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 525 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  records the focused OAK/OLS candidate check and Falcon review disposition:
  keep the kg-microbe placeholder and do not assert exact identity to
  `CHEBI:204272` without sequence or provenance confirmation.
- `mappings/unmapped_ingredients_duplicate_review_2026-05-07.md` records the
  absorbed duplicate source label and the same reason for not promoting
  `CHEBI:204272`.
- The SSSOM `other` field preserves the exact and related ISK-1 labels carried
  by the YAML record.

## Completeness

- The local placeholder identifier, exact source synonym, related ISK-1
  synonyms, literature caution, SSSOM row, and aggregate copy are populated.
- No formula, InChI, SMILES, or external exact match should be added until the
  sequence/provenance ambiguity between Bacteriocin ISK-1 and Nukacin ISK-1 is
  resolved.

## Recommended Edits

- None.
