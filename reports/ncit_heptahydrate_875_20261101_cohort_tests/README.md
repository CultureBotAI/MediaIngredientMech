# #1034: historical migration coverage and evolving live membership

This append-only report accompanies a test-only correction in `tests/test_repair_heptahydrate_membership.py` (SHA-256 `a615daeb6276bcf32a3d879efa9b09a4c1c379751ee8a9330f66fb9ab7b384b3`). No producer, guarded writer, routing rule, production data, export, mapping approval or earlier evidence bundle changed. Work began on `0bbe5e6816dc3d4332ab164d04a979cface4e179`; the native capture and exact committed-head review for the follow-up are outside this frozen package.

[Issue #1034](https://github.com/CultureBotAI/MediaIngredientMech/issues/1034) was filed before the fix. The prior test incorrectly required live NCIT:C61946 memberships always to equal the one-time migration's 32 recipes with one occurrence each. The independent proof runs the actual producer and ordinary full-table invariants: a legitimate new recipe yields 33/33; a repeated listing yields 32/33. Both failed the old live assertion while ownership, sortedness, uniqueness and stable-ID checks passed. These are synthetic future-source controls, not new current CultureMech observations. See `independent/finding-1034/`.

The exact 32-pair assertion now replays the actual pure writer against the **already committed immutable gzip preimage**, verifies the original receipt's input/output hashes, and checks the exact recipe/count pairs, header, unrelated rows and idempotence. The live assertion still rejects the retired identifier and imposes no fixed cohort size. Two regressions execute the native producer's `main()` and effective-count helper for the valid 33/33 and 32/33 cases; the fixture owner's historical 26/26 YAML is unchanged. The ordinary active-owner invariants remain in the focused suite.

The historical input is referenced, not duplicated:

- `reports/ncit_heptahydrate_875_20261101_membership/application/apply.before-membership.tsv.gz`: compressed SHA-256 `a0833c3a21c9364d4874f7b7ba7217afcd4f87c84244e0284e487c97f3cc42e6`; decompressed SHA-256 `6537498d833f45295193865d6cd5f98ad31200c5dbe4a706c6f541dcf30a5064`.
- The adjacent original `apply.json` binds the repaired output SHA-256 `55ce5fabd42eb4cc1df628d4fd6a45b813caccbc7d7773105ece5633dd313897`. It remains the single production application receipt; this test correction did not reapply the writer.

Verification completed before package freeze:

| Check | Result | Evidence |
| --- | --- | --- |
| Author focused repair + generic membership suite | 90 passed | `author/checks/step2-test1034-focused.*` |
| Fresh-process isolated baseline | 3 passed | `author/mutation-control.log` |
| Restore old live quota | Both growth cases fail as expected | `author/mutation-restore_live_quota.log` |
| Discard repeated-listing counts | Count regression fails as expected | `author/mutation-discard_repeat_listing.log` |
| Bypass historical migration | Archived after-hash regression fails as expected | `author/mutation-skip_historical_migration.log` |
| Independent corrected-runtime focused suite | 90 passed, no skips | `independent/re-review/focused-v2.log` |
| Independent full-table baseline/new/repeated source controls | All current-owner and ordinary native invariants pass | `independent/re-review/results.json` |
| Independent fresh-process control/mutations | Baseline green; all three negative controls red | `independent/re-review/verification-v2.json` |
| Root broader focused suite | 223 passed | `root-checks/step2-cohort-tests-final-focused.*` |
| Root full `just qc` | Exit 0 at 2026-11-01 07:10:31 UTC | `root-checks/step2-cohort-tests-final-qc.json`, `.log.gz` |

The root focused log SHA-256 is `8c385959e3bc1dbfffcfd5e97ac6cecfc0d95dac1a4107b7df096b404f8d12b0`; the uncompressed full-QC log SHA-256 is `8823de5827adc7af77f242e8297527c40f6702a97a5811c486b1f49f09e218d3`. `check-log-bindings.json` lets the read-only verifier check the actual log bytes against successful execution receipts. Dependency deprecation warnings are retained in the logs.

The independent preliminary review found no remaining in-scope defect. Its stable report is `independent/re-review/review.md`, SHA-256 `e4579b048a0c84c6e0115ec9ccfdb7a2b8fd6e37f58e72bd4fb1a3cbf746520f`. It verifies 364 protected production/report inputs and 437 unchanged inputs from the prior exact-head review, with this test file as the sole expected change among that prior review's 438 inputs. Both earlier native review files are preserved. This is preliminary source verification, not a new exact-head or queue verdict.

Initial reviewer failures are preserved honestly. The first standalone command imported the editable Step 1 package rather than the current Step 2 worktree, and the first external mutation invocation lacked its temporary directory's parent. `runtime-and-copy-verification.json` demonstrates the actual module origins and 28 copied fixture inputs; `check_v2.py`, `*-v2.log` and `verification-v2.json` contain the corrected explicit-worktree runs. Initial `focused.log`, `control.log`, `check.log` and `check.py` remain diagnostic failures and are not counted as passing validation. No source change was needed to correct those reviewer invocations.

The prior `0bbe5e6` queue-readiness verdict is **superseded** by #1034. Root removed PR #1030 from the queue before merge and cancelled the old integration suite; the cancelled integration is **not a pass**. `finding/pr-hold.md` and its publication receipt preserve that disclosure. A new native capture, ordinary follow-up commit, independent exact-head review, remote checks and queue validation must follow outside this package. No scientific mapping approval or release approval is added here.

`author/` contains before/final test snapshots, patch, immutable authored inventory, protected-input hashes, harness and red/green evidence. `independent/` contains bounded copies of the actual finding and re-review. Full-sized membership fixtures and pytest temporary trees are intentionally omitted; original scripts/results bind their inputs and outcomes. Historical harnesses retain their original run paths and exclusive-output assumptions, so reproduce them in fresh external directories with the recorded environment rather than running them over frozen evidence. Nested historical inventories retain their original scope and do not assert that omitted fixture trees were copied here.

Run `python -B reports/ncit_heptahydrate_875_20261101_cohort_tests/verify.py` from the repository, or supply `--repository PATH`. It only reads files. It verifies this package, four successful receipt/log pairs, the original gzip/receipt binding and 368 point-in-time repository references. This is a historical evidence verifier, **not** a CI rule freezing the live corpus: later legitimate curation may change a referenced file and therefore fail a current-checkout historical comparison. The package's inventory is self-excluded and its hash is recorded in the external handoff. Earlier frozen reports are untouched.
