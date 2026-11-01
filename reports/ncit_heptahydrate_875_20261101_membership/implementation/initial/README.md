# #1031 membership repair implementation evidence

The bounded source implementation is ready for root application and independent review. This directory is append-only evidence for the follow-up to Step 2; no earlier report, application receipt or report inventory was rewritten.

## Scope and exact source

`stable-source.json` binds the code and protected production inputs inspected at 2026-11-01T06:03:47Z on HEAD cb9f59a0d045f104ee2c3c00c8d6c4ad4f4eaf1f. The new writer SHA is `85317d72170174119ced30394194e0b1503bee9cc1fac1035147ad8fe2d064a2`. The reused #1029-repaired producer remains `f7cd1b46dc464cc8801a73f6b1cbd251bd5c0c7ffdf7241eff0e9cbee6f1c131`.

The new operation requires the exact current corrected owner, rejection-ledger and canonical SSSOM hashes. It accepts only the original membership bytes or its exact completed output, verifies the frozen32 recipe/count pairs, refuses destination collisions/partial migration/duplicate keys, preserves header and every unrelated row byte, and sorts with the native key order. It uses the existing held-descriptor reservation checks, caller lock, input rechecks and native validated transaction. A true repeat writes no receipt or history. Owner YAML, canonical SSSOM, rejection ledger and unified mapping are not outputs.

Expected production membership SHA after root application: `55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897`. Before: `6537498d833f45295193865d6cd5f98ad31200c5dbe4a706c6f541dcf30a5064`.

The router adds only the three labels already accepted in the curated record: `Na2HPO4 x 7 H2O`, `Na2HPO4.7H2O`, and `Na2HPO4•7H2O`. Existing case/whitespace normalization is unchanged. It does not broaden the override to middle-dot or long-form names, or to every occurrence sharing a parent/old ID. The native archived-snapshot regression recovers exactly the observed28+4 recipes; the bullet spelling is covered by synthetic routing cases. The frozen membership repair preserves32 pairs even if a future upstream source has a different cohort.

## Results

- Native CLI using RepositorySettings and LockManager: dry-run PASS; no production data applied and no reserved evidence receipt created. The complete proposed32 memberships and input hashes are in `logs/step2-membership-native-dry-run.log`.
- Final writer/routing tests plus existing semantic-identity routing tests: **69 passed, zero skipped, one deselected**. The sole deselection is the committed-artifact assertion, which requires root to apply the reviewed repair. It remains required after application.
- Existing native producer routing/repeated-occurrence tests: **16 passed**,31 deselected by the named focused selection.
- Source-occurrence and occurrence-refresh suites: **23 passed**.
- Native fixture coverage includes receipt and backup replacement by regular files and symlinks at reservation, prepared, after-commit and completion boundaries. Every competitor survives; precommit failures preserve sources and postcommit failures preserve the native journal and beforeimage. No false complete receipt is accepted.
- Effective-count regression verifies historical YAML26/26 remains intact while corrected membership supplies32/32. Native collector sees exactly the frozen32 current-identity recipe pairs; the unrelated plain-parent occurrence retains its owner.
- Ruff check PASS using an already cached binary. An earlier `python -m ruff` attempt failed because Ruff was absent from the isolated MIM environment; that diagnostic is retained. Nothing was installed.

## Fresh-process negative controls

`mutation_controls.py` changes only a fresh test process's in-memory bindings; it never edits maintained source or artifacts. Each mode has a separate process/log/receipt:

| Disabled behavior | Expected regressions observed |
| --- | --- |
| Three finite source-label overrides |13 failures, including the actual native collector;4 already-current-ID cases still pass |
| Membership repair (return original bytes) |1 native migration/preservation test fails |
| Receipt/backup identity checks |16 native reservation-race tests fail |

These are intentional counterfactual failures, distinct from the passing unmodified source. They verify that routing, mutation and reservation safeguards each affect the tested behavior.

## Remaining owner work

Root performs independent-reviewed application, native effective-count export regeneration, committed-artifact and active-owner tests, full relevant QC, append-only portable packaging and publication. No fresh scientific mapping approval is conferred. Chemical-property/BUFFER questions remain outside this membership correction. Step 6 preparation remains paused.
