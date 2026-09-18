# `data/ingredients/mapped/Thioctic_Acid.yaml`

## Verdict

Pass with minor issues. This rejected tombstone correctly emits no final SSSOM
row after the lipoic-acid stereochemistry repair, but it still retains stale
live-record fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Thioctic_Acid.yaml`.
- Tombstone state: `mapping_status: REJECTED` with `representative:
  CHEBI:16494` after `fix_lipoic_stereochemistry` merged this unsupported
  enantiomer-specific record into the active `(DL)-alpha-Lipoic acid` record.
- Grounding fields: the tombstone now points at `CHEBI:16494` / `lipoic acid`
  and retains rejected R-only lipoic-acid labels for provenance.
- Occurrences: zero; occurrences were transferred to the active generic lipoic
  acid record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine_pyrophosphate` through `Thiolutin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The September 11 `fix_lipoic_stereochemistry` history records that the prior
  enantiomer-specific target was unsupported and that the record was merged
  into the active `CHEBI:16494` generic lipoic-acid representative.
- Local OAK resolves `CHEBI:16494` with canonical label `lipoic acid` and
  related synonym `Thioctic acid`, matching the representative target.
- The final SSSOM has no `MIM:Thioctic_Acid` row; the active
  `MIM:Dl-alpha-lipoic_Acid` row carries the generic/racemic lipoic-acid
  labels, including `Thioctic acid`.

## Completeness

- The tombstone is absent from final SSSOM, has zero occurrences, and points at
  the active representative.
- Minor: the rejected record still carries stale `ingredient_type`,
  `kg_microbe_node_id`, and provisional `VITAMIN_SOURCE` fields that do not
  affect final exports.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected rejected tombstone, active
  representative, #454 repair rows, component references to the active
  `CHEBI:16494`, and final SSSOM row for `MIM:Dl-alpha-lipoic_Acid`.

## Recommended Edits

- Minor: clear stale live-record fields from the rejected
  `data/ingredients/mapped/Thioctic_Acid.yaml` tombstone when tombstone cleanup
  is next run, then rerun strict validation and SSSOM publication.
