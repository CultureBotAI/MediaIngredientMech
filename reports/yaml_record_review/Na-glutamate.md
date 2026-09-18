# `data/ingredients/mapped/Na-glutamate.yaml`

## Verdict

Pass with minor issues. The record is an inert `REJECTED` tombstone merged into
the live `CHEBI:64243` `Sodium L-glutamate` record, and no final SSSOM row is
published for `MIM:Na-glutamate`; its stale role and structure fields should be
cleaned eventually but no longer affect the mapped output.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-glutamate.yaml`.
- Identifier and grounding: `identifier: CHEBI:64243` with
  `ontology_mapping.ontology_id: CHEBI:64243`, label
  `monosodium L-glutamate`, source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  and `mapping_status: REJECTED`.
- Occurrences: 0 after the 2026-08-10 merge into `CHEBI:64243`
  `Sodium L-glutamate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-formate` through `Na-laurate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI tombstone.

## Evidence

- Fresh OLS4 and OAK lookups resolve `CHEBI:64243` as active
  `monosodium L-glutamate`, which matches the live merge target named in the
  2026-08-10 and 2026-08-15 tombstone history.
- A hidden/ignored-inclusive search of `mappings/ingredient_mappings.sssom.tsv`
  found no `MIM:Na-glutamate` subject row. The old label survives only as
  `Na-glutamate` in the `MIM:Sodium_L-glutamate` row's `other` column.
- Minor: the tombstone still carries stale structure, synonym, and
  `NITROGEN_SOURCE` fields from the pre-merge L-glutamate anion assertion. Those
  fields are misleading in-place but are inert because the record is rejected
  and publishes no final mapping row.

## Completeness

- The rejected status, zero occurrence count, tombstone history, absence of a
  final `MIM:Na-glutamate` row, and live `Sodium L-glutamate` replacement row
  agree.
- No new evidence is required unless a future curation pass chooses to strip the
  stale pre-tombstone fields for readability.

## Recommended Edits

- Minor: optionally clean the stale pre-merge chemical, synonym, and
  `NITROGEN_SOURCE` fields from `data/ingredients/mapped/Na-glutamate.yaml`
  while preserving the curation history that explains the rejected tombstone.
  Rerun strict validation and final SSSOM validation afterward to confirm the
  tombstone remains unpublished.
