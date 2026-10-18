# `data/ingredients/mapped/Α-lipoic_Acid.yaml`

## Verdict

Pass with minor issues. This rejected S-lipoic tombstone correctly emits no
final SSSOM row after the lipoic-acid stereochemistry repair, but it still
retains stale live-record fields.

## Identity

- Reviewed record: same path as the report heading.
- Tombstone state: `mapping_status: REJECTED` with
  `representative: CHEBI:16494` after `fix_lipoic_stereochemistry` merged this
  unsupported S-only record into the active `(DL)-alpha-Lipoic acid` record.
- Grounding fields: the tombstone now points at `CHEBI:16494` / `lipoic acid`
  and retains rejected S-only lipoic-acid labels for provenance.
- Occurrences: zero; occurrences were transferred to the active generic/racemic
  lipoic-acid record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 4-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Focused final-output search was run with `rg --no-ignore --hidden`; ignored
  files were included.

## Evidence

- The September 11 `fix_lipoic_stereochemistry` history records that the prior
  S-only target was unsupported and that the record was merged into the active
  `CHEBI:16494` generic lipoic-acid representative.
- The final SSSOM has no row for this Greek-alpha MIM subject; the active
  `MIM:Dl-alpha-lipoic_Acid` row carries the generic/racemic lipoic-acid
  labels.

## Issues

- Minor: the rejected record still carries stale `ingredient_type`,
  `chemical_properties`, and provisional `VITAMIN_SOURCE` fields that do not
  affect final SSSOM exports.

## Completeness

- The tombstone is absent from final SSSOM, has zero occurrences, and points at
  the active representative.

## Recommended Edits

- Clear stale live-record fields from the rejected tombstone when tombstone
  cleanup is next run, then rerun strict validation and SSSOM publication.
