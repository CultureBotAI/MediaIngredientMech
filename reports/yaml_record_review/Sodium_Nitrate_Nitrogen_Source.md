# `data/ingredients/mapped/Sodium_Nitrate_Nitrogen_Source.yaml`

## Verdict

Pass. This is a rejected same-substance sodium nitrate duplicate; it points at
the same active `CHEBI:63005` identity as `NaNO3` and emits no final SSSOM row.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sodium_Nitrate_Nitrogen_Source.yaml`.
- Identifier and grounding: `identifier: CHEBI:63005` with
  `ontology_mapping.ontology_id: CHEBI:63005`, label `sodium nitrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: REJECTED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: this tombstone has `0` occurrences after the #226 merge into the
  live `NaNO3` sodium nitrate record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Nitrate_Nitrogen_Source` through `Sodium_Pantothenate`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- `uv run --frozen python scripts/run_shared_evidence_validator.py` is
  unavailable because the sibling `culturebotai-claw` checkout is absent.

## Evidence

- Local OAK term lookup resolves `CHEBI:63005` as sodium nitrate, matching the
  mapping and the backfilled sodium nitrate structure.
- The merge history records that this role-qualified source label was merged
  into `CHEBI:63005` `NaNO3` and tombstoned as `REJECTED`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found no final SSSOM subject row for
  `MIM:Sodium_Nitrate_Nitrogen_Source`; the only remaining indexed references
  are an alias row and the cross-record baseline entry.

## Completeness

- The rejected duplicate keeps its provenance and no longer carries any
  occurrences that would be lost from the live record.
- The role-qualified `Sodium nitrate (nitrogen source)` label still published
  by `MIM:Nano3` is already tracked in the `Nano3` review report, not owned by
  this tombstone.

## Recommended Edits

- None for this record.
