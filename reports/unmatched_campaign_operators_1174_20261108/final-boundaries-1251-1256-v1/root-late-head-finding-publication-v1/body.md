Independent W08 adversarial review of PR #1205 head `16c39b63bc95d3e7978ddccc6280b0d57954f4a5` reproduced a mutation-time baseline freshness gap. Native prepare checks HEAD against the accepted `baseline_commit`, but subsequent source apply rechecks do not. The final unrelated-file guard diffs against the current HEAD.

Real private Git demotion lifecycle probes, without mocking native source functions, show:

- Unchanged baseline: prepare, apply and completed verification pass.
- HEAD changed before prepare: refused with `Integration HEAD differs`, before receipt/source writes.
- Empty commit after prepare: apply and completed verification return complete against the old accepted baseline.
- An unrelated tracked file committed after prepare: apply and completed verification also return complete. The diff from the accepted baseline contains the unrelated file; the guard's diff from new HEAD does not.
- An unrelated staged, uncommitted file after prepare: the existing scope guard refuses, preserving a failed/recovery-required receipt.

This is separate from #1255's literal Git path parsing. It demonstrates a real prepared-state freshness/receipt claim defect in private mechanical fixtures, not production campaign corruption or an ability to invent scientific approval. No maintained campaign application has occurred. Source module SHA256 `4500c96280d717e7f2f34760c5f6bb7bbdde47ebe3356b8ccf18a29d13263f78`.

Requested fix: retain and recheck the exact accepted Git baseline throughout the actual source mutation lifecycle, including prewrite and final completion boundaries; compare tracked mutation scope to the accepted baseline rather than a movable HEAD. Preserve all existing file/producer/input/inventory/receipt guards and honest failed recovery evidence. Add real-Git positives and late empty/unrelated commit negatives, including late boundaries and existing edit/create/promotion/demotion shapes as appropriate. No global Git configuration, gate weakening or data change.

Distinguish lifecycle freshness from historical verification: `verify_completed` explicitly permits later canonical publication and serves historical receipts. Do not add an unjustified requirement that all later verification forever remain at the original Git HEAD. Assess and document that historical contract separately while closing the mutation-time gap. The final source/publication integration must still use the authorized unchanged-baseline sequence.

Captured independent evidence: `.temp/all-unmatched-20261107/preflight/late-head-finding-publication-v1/late-head-results-v2.json`, SHA256 `090be4930969fde0b830419d1c27f21feb7e36653f9b769a24b33b67ffe0417e`; original under `workers/w08/worktree/.temp/combined-16c-independent-v1/root-probes/`. Exact scripts and original failed harness log remain preserved; the first harness's missing .gitignore assumption was corrected with a separately retained readback and real staged-file control. W08's complete final review is still running; this issue records the confirmed finding before a fix.

Deduplication checked current all-state campaign/HEAD issues and #1194's body/comments. #1194 concerns late owner membership, #1214 recovery backup bytes, and #1255 quoted paths; none tracks this missing mutation-time Git-baseline recheck. Require an exact-successor adversarial re-review before application.
