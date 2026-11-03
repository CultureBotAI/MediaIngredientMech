# Issue 1122 four-comment remediation handoff

Prepared externally; **not applied**. Independent reviewer must review the frozen proposal before root applies it. No maintained source, test, workflow, snapshot, rule or pin was edited by the author. The old operator/config, native generated candidate, original canonical and original batch25 remain preserved.

The v2 operator is `remediate_parent_comments_v2.py`, SHA-256 `7f2b44c8f7c2dbf9d266fdd49903570fad94c4402bb2260e90058a0b66cf6ed8`. The immutable v2 proposal is `comment-remediation-v2/`, manifest SHA-256 `5162b7f432bc87009a693df5a98d1e18cd30f4aa1806f8aaa78a610da2db8de0`. That proposal includes its exact executed operator, native maker, finding, original projection/config and original canonical/receipt bytes. V1 remains unchanged at `remediate_parent_comments_v1.py`; its exact executed bytes are additionally preserved in `comment-remediation-v1/executed-remediation-operator.py` (SHA625ab3e5ecd42e6f8ffe3382c03df7f23d4d4d8bcb09217efe97d4b88d774c74). The v1 manifest itself was not rewritten; it already binds the v1 executable by path/hash.

Exactly four canonical `comment` cells change. Each becomes `<verbatim current native comment> Historical/superseded parent context: <verbatim former comment>`. Every other row/header cell, raw unrelated row and row position is identical. All original text stays recoverable; the change grants no identity, scientific, role or release approval. The versioned projection config uses schema_version3 to declare this bounded correction layer over the unchanged schema_version2 projection; it retains all original candidate rows, positions, bases, removals and source bindings.

The native receipt maker runs only in a private temporary tree. It first reproduces original batch25 byte-for-byte, then reconstructs corrected batch25 from the **same original pre-batch SSSOM** and **same38 owner/apply records**. All metadata except `after_sha256` and changed row payloads remain identical; the 24 historical predecessors are byte-identical. There is no sequence26. The maintained change, when authorized, is a single native guarded transaction replacing canonical SSSOM and existing batch25 together. The receipt retains its #901 batch identity; #1122 is recorded in the versioned projection remediation and guarded application evidence.

| Proposed endpoint | SHA-256 |
|---|---|
| canonical SSSOM | `d3030e6385a2659a0dbd2c64ad5581568eecd9c10023f4a58de667e8050f20ef` |
| corrected batch25 | `45af9515590918e3420327668d4b89f564457cf97eea9404a34c4da7d17f0e4b` |
| projection-config-v3.json | `5c46422bf88f6553ea8a41bc1c47af3c8b65b746d15f8cefb99de39f4dcd94d0` |

Native dry-run receipt: `logs/step7d-1122-comment-remediation-prepare-c2.json`, exit0. It replayed the captured native candidate offline, verified every current owner and protected input, reproduced the old receipt, replayed corrected25, and passed the actual native publication transaction in dry-run mode. External controls: **58 passed**, `logs/step7d-1122-comment-remediation-controls-c1.json`. These include extra/missing/duplicate targets, wrong positions/CAS/native text, noncomment changes, old-comment loss, row/header drift, sequence26, invented approval/bindings, missing/changed source/snapshot/native/test/workflow/pin inputs, producer/owner inventory changes, symlink/hardlink aliases, forged historical receipt and original batch preimage. No maintained test file was edited.

Native candidate invariants: `logs/step7d-1122-comment-remediation-native-invariants-c1.json`, exit0, zero reject rows (header-only `comments-1122-proposal-rejects-c1.tsv`). Rules A/B1/B2/B3/B5/C/D/E/F/G/H/I/J/K/L passed. **Rule B4 was skipped** by the unchanged native path resolution because its ontology-transform directory is absent in this worktree; this is explicitly not a B4 pass. Root retains the broader environment-specific checks.

## Root application after independent review

Use a fresh external log path; the operator rejects pre-existing receipt/backups, aliased inputs, input drift, missing protected inputs and a changed native25 prefix. It holds the native repository lock. No force operation is involved.

```sh
python3 '/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/run_step7d_mim.py' step7d step7d-1122-comments-apply-v1 -- \
  python -B '/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step7d-execution-20261103/remediate_parent_comments_v2.py' \
  --proposal '/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step7d-execution-20261103/comment-remediation-v2' \
  --manifest-sha256 '5162b7f432bc87009a693df5a98d1e18cd30f4aa1806f8aaa78a610da2db8de0' \
  --log '/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/approved-plan-20261101T031134Z/step7d-execution-20261103/comments-1122-apply-v1.json' --apply
```

Only root may execute that command after the independent review. The operator reserves a new native transaction journal and both original-artifact backups before maintained replacements, verifies all input bytes again, and checks the completed journal plus native25 replay after publication.

## Native dependency refresh after application

Archive the v2 proposal, original artifacts, operator, controls, actual run receipts and review under the maintained Step7d evidence directory without rewriting any previously saved bundle. Advance the existing assembler `REVIEWED_SOURCE` to the new canonical SHA, then run the unchanged native assembler and `--check`; rebuild full KGX and the semantic review; validate integrity and honest open-backlog verdict. Revalidate that all105 selected rows remain WITHHOLD and the24 historical receipts remain byte-identical.

Create a **new immutable companion successor**, for example `reports/step7d_mapping_901_20261103/refresh-v2/`, from the currently committed prior Step7d companion at durable baseline `7d35035f6c521c69fad94f73381c6a6eb7251fff`. Use native `refresh_unchanged_cohort.py` with that explicit baseline/prior path and new output/receipt/prior-copy paths. Its20 owners/51 claims are unchanged; both selectors must move together to this new review, with all other assertions/bytes unchanged. Run the native reviewed/supported exports and their validators.

No owner-driven derived list/index/browser/visualization rebuild is needed for a comment-only SSSOM correction. No unified rebuild/stamp is needed or permitted by this remediation; the reviewed snapshot hashes remain fixed. Native review/SSSOM/graph/companion evidence dependencies do need refresh. Rerun required full QC/suite on the actual corrected final head, obtain independent re-review, and replace the pending PR-body check entries with actual receipts. Update the PR body's canonical SHA and #1122 finding disposition; row counts, 38/29 decisions and six-cell snapshot trace remain unchanged.
