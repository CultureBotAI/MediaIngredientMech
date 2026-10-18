# `data/ingredients/mapped/Na-tartrate.yaml`

## Verdict

Pass with minor issues. The record is an inert `REJECTED` tombstone merged into
the live `CHEBI:63017` `Sodium tartrate` record, and no final SSSOM row is
published for `MIM:Na-tartrate`; stale pre-merge fields remain but no longer
affect the mapped output.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-tartrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63017` with
  `ontology_mapping.ontology_id: CHEBI:63017`, label `sodium L-tartrate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, and `mapping_status: REJECTED`.
- Occurrences: 0 after the 2026-08-10 merge into `CHEBI:63017`
  `Sodium tartrate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-stearate` through `Na2-edta`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI tombstone.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:63017` as active `sodium L-tartrate`,
  with `cas:868-18-8`, formula `C4H4O6.2Na`, and the same disodium tartrate
  identity asserted by the live replacement record.
- A hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no `MIM:Na-tartrate` subject row. The old label survives only as
  `Na-tartrate` in the `MIM:Sodium_Tartrate` row's `other` column.
- Minor: the tombstone still carries stale L-tartrate anion structure and a
  `CARBON_SOURCE` facet whose original role text says `Mineral`. Those fields
  are misleading in-place but are inert because the record is rejected and
  publishes no final mapping row.

## Completeness

- The rejected status, zero occurrence count, tombstone history, refreshed
  target, absence of a final `MIM:Na-tartrate` row, and live `Sodium tartrate`
  replacement row agree.
- No new evidence is required unless a future curation pass chooses to strip the
  stale pre-tombstone fields for readability.

## Recommended Edits

- Minor: optionally clean the stale pre-merge chemical, synonym, and
  `CARBON_SOURCE` fields from `data/ingredients/mapped/Na-tartrate.yaml` while
  preserving the curation history that explains the rejected tombstone. Rerun
  strict validation and final SSSOM validation afterward to confirm the
  tombstone remains unpublished.
