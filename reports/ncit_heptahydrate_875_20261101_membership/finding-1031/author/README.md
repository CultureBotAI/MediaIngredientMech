# Step 2 membership omission: bounded remediation plan

Read-only inspection of Step 2 HEAD `cb9f59a0d045f104ee2c3c00c8d6c4ad4f4eaf1f`. No source repair, production data edit, GitHub mutation or regeneration performed. Step 6 preparation is paused.

## Verified finding

`mappings/culturemech_recipe_membership.tsv` SHA-256 `6537498d833f45295193865d6cd5f98ad31200c5dbe4a706c6f541dcf30a5064` contains **32**, not 42, retired-ID rows, one occurrence each, and no `NCIT:C61946` row. The file has 202,098 membership rows. `input-cohort.json` preserves every selected recipe/count pair and hashes the unrelated row payloads.

The archived audit875 occurrence snapshot has 35 rows; 28 `Na2HPO4 x 7 H2O` and four `Na2HPO4.7H2O` rows still carry the retired local identifier. The native router returns that old identifier, and the native membership collector with the new active NCIT identifier produces no NCIT edges and reports the 32 old-ID recipes as unknown. See `native-consumer.json`. This is a reproduction on the existing archived snapshot, not a claim about today's full upstream corpus.

The existing active-owner membership test fails with exactly that dangling ID (`baseline-ownership-test.log`). The native effective-count helper falls back to stored YAML 26/26 because NCIT has no membership key. Restoring the original cohort to the corrected identifier will restore effective 32/32; stored historical YAML statistics need not change.

## Smallest repair after the finding is filed and implementation authorized

1. Add a separately named membership repair phase or narrowly scoped guarded writer. Do not reapply the already recorded source correction or rewrite its immutable receipts/history. Pin the current owner, ledger, canonical SSSOM, membership and source-evidence input hashes. Require the owner already denotes exact NCIT:C61946, the ledger's coupled identity is migrated, and no conflicting active owner or destination membership exists.
2. Change only `mim_identifier` on the exact 32 frozen `(recipe_id, occurrences)` pairs. Preserve the metadata/header and all unrelated row payloads, then sort by the native `(mim_identifier, recipe_id)` order. Assert unchanged total edge count, recipe universe, occurrence sum, distinct identifier count and exact selected pair set. Do not call the full membership builder on a newer upstream table. Reject unknown preimages, missing/extra pairs, destination collisions and partial migration. Completed exact output must be an idempotent no-op.
3. Use the existing native transaction and caller lock, reserving the new receipt and exact beforeimage exclusively. Retain descriptor identities and check paths before commit and completion, as in the repaired #1029 producer. Preserve competitor paths and journal on failure. The receipt explicitly states this is an identity-key migration of an existing source snapshot, not a count refresh or new scientific approval.
4. Extend `SOURCE_LABEL_IDENTIFIER_OVERRIDES` in `src/mediaingredientmech/utils/culturemech_occurrences.py` only for the record's existing accepted labels: preferred `Na2HPO4 x 7 H2O`, `Na2HPO4.7H2O`, and `Na2HPO4•7H2O`. The current exact source-label normalization remains unchanged. Do not remap every CHEBI:34683 or old-ID occurrence globally; sibling hydrate/plain-phosphate labels remain independent. Broader spellings not already accepted require separate justification and are outside this minimal plan.
5. Root regenerates native list/browser exports and inspects their expected effective-count change to 32/32, along with any visualization metadata which consumes effective counts. No ingredient YAML, aggregate YAML or SSSOM row change is needed for this artifact repair. Refresh review producer hashes and perform the required independent review on the final commit; preserve frozen earlier evidence and clearly append this correction.

## Focused acceptance and negative controls

- Exact 32-pair fixture migration, unrelated rows/header preserved, native sort/uniqueness, no old-ID row, NCIT count32 and occurrence32; no broader 42/35/current-upstream assumption.
- Fail safely on wrong input hash, missing/extra selected pair, duplicated key, existing destination rows, partial state, occupied receipt/backup, changed input between checks, and receipt/backup replacement at each guarded phase; use the real native transaction. Test exact repeat no-op without a new history event.
- Native `mim_identifier_for_occurrence` tests cover all three accepted spellings, whitespace/case normalization and old-local/parent/blank incoming IDs as applicable. Negative controls cover anhydrous `Na2HPO4`, sibling 1/2/3/6/12-hydrate names, buffer names and unrelated labels; their original routing remains unchanged.
- Native `collect` fixture uses the frozen32 occurrence cohort, exact known NCIT owner, repeated-occurrence accounting and no old-ID unknown bucket. Preserve all recipe IDs/counts. The accepted bullet synonym may be a synthetic fixture, clearly distinguished from the observed28+4 snapshot.
- Existing `test_culturemech_membership.py`, `test_semantic_identity_occurrences.py`, occurrence/export consumers and the guarded-writer tests pass. The active-owner regression must become green; effective exports must report32/32 while YAML stays26/26.
- Fresh-process mutation controls remove the new router entries and restore the original membership table separately; the corresponding routing and artifact tests must each fail for their intended reason. Run full repository checks on final generated products before re-review/queue.

## Code evidence

- `src/mediaingredientmech/utils/culturemech_occurrences.py:51`: finite source-label override table; `:147` native routing; `:156` membership aggregation; `:176` effective counts and fallback.
- `scripts/build_culturemech_membership.py:74`: native collect skips/report unknown IDs; `:100` native sorted artifact writer.
- `tests/test_culturemech_membership.py:125`: sorted invariant; `:146`: every published ID must have an active owner; `:269` and `:367`: existing hydrate-routing regression patterns.
- `scripts/promote_heptahydrate_ncit.py:211`: guarded receipt/backups/native transaction; `:273`: original owner/ledger phase omitted membership, so use an explicitly new repair operation.
- `scripts/export_lists.py:539` and `scripts/browser_export.py:147`: published effective statistics consume membership.
