# `data/ingredients/mapped/Na2-edta_X_2_H2o.yaml`

## Verdict

Pass with minor issues. The record is an inert `REJECTED` tombstone merged into
the live `CHEBI:64758` `Na2EDTA` dihydrate record, and no final SSSOM row is
published for `MIM:Na2-edta_X_2_H2o`; stale pre-merge fields remain but no
longer affect the mapped output.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2-edta_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:64758` with
  `ontology_mapping.ontology_id: CHEBI:64758`, label
  `EDTA disodium salt dihydrate`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: REJECTED`.
- Occurrences: 0 after the 2026-08-13 merge into the live
  `Na2EDTA` dihydrate record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2-edta_X_2_H2o` through `Na2HPO4-NaH2PO4_Buffer`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI
  tombstone.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:64758` as active
  `EDTA disodium salt dihydrate`, with `cas:6381-92-6`, formula
  `C10H14N2O8.2H2O.2Na`, and the expected dihydrate synonyms.
- The #321/#334 history correctly records the hydrate split from anhydrous
  `CHEBI:64734`, the local hydrate mint, and the later merge into specific
  `CHEBI:64758` once the exact ChEBI hydrate was found.
- A hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no `MIM:Na2-edta_X_2_H2o` subject row. The old label survives only as a
  synonym on the live `MIM:Na2edta2h2o` row.
- Minor: the tombstone still carries stale anhydrous EDTA synonyms, stale
  `CHELATOR` inference, and the obsolete `cas_rn: 7487-55-0`. Those fields are
  misleading in-place but are inert because the record is rejected and publishes
  no final mapping row.

## Completeness

- The rejected status, zero occurrence count, tombstone history, refreshed
  `CHEBI:64758` target, absence of a final `MIM:Na2-edta_X_2_H2o` row, and live
  `Na2EDTA` dihydrate replacement row agree.
- No new evidence is required unless a future curation pass chooses to strip the
  stale pre-tombstone fields for readability.

## Recommended Edits

- Minor: optionally clean the stale pre-merge chemical, synonym, and `CHELATOR`
  fields from `data/ingredients/mapped/Na2-edta_X_2_H2o.yaml` while preserving
  the curation history that explains the rejected tombstone. Rerun strict
  validation and final SSSOM validation afterward to confirm the tombstone
  remains unpublished.
