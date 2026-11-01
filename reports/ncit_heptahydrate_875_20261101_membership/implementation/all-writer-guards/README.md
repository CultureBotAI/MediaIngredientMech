# #1033: original source and promotion paths

This append-only revision extends the same owner-uniqueness fix to both original publishing call sites, following the independent native reproductions and recorded issue-scope expansion. The earlier membership correction remains unchanged. All files bound by both earlier evidence indexes were verified unchanged before this revision was frozen.

`apply_sources()` and `promote()` now pass the explicit `validate_scope` callback into native precommit validation. Promotion also checks for a conflicting destination before returning a completed-output no-op. The guarded publisher, exact input hashes, caller lock, held receipt/backup descriptors and failure journaling remain in place. This is a precommit guard; it does not claim protection from arbitrary later edits.

Final original/shared writer SHA-256: `768166cfb726e3a751b451a89bebfa30c8dea7e22f05ba085cf4fb9db96550ee`. Final original-writer tests: `e8f8c23cd99c5ddb5d85b350d6df06be7bad871531eb4a57d164c344bd34da34`. Exact source snapshots and all other source/protected hashes are preserved here. Earlier historical producer hashes and production receipts remain immutable and were not relabeled as executions of this code.

Validation:

- Four new native regressions fail on the preceding code: valid owner inserted after reservation in the source path; the same in promotion; valid pre-existing promotion conflict; valid pre-existing conflict on the completed-output path.
- Final combined suite: **158 passed, no skips, one deselected**. This includes all original84 writer tests plus the four new cases, the membership tests and existing semantic identity routing tests. The deselected committed-membership assertion awaits root application.
- Both post-reservation cases preserve the valid competing owner, all original inputs, beforeimages and a failed receipt, with no committed native journal or mutation. Pre-existing conflicts are rejected without a new receipt. Existing successful/no-op paths remain covered.
- A separate fresh test process removes only the passed scope callbacks. Both post-reservation regressions fail again; the mutation plugin affects that test process only.
- Native locked membership CLI dry-run and Ruff PASS on the revised shared producer. No production source/ledger/SSSOM/history application was performed.

Independent source-path and promotion-path reproduction results are copied under `independent-original/`. Re-review, root membership application, export regeneration, artifact checks and publication remain separate. No new scientific approval or later-plan work is asserted.
